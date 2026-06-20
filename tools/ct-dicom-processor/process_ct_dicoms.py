#!/usr/bin/env python
"""
Convert local CT DICOM files into PNG review assets and an anonymized manifest.

The script intentionally avoids writing patient identifiers, UIDs, accession
numbers, exact dates, facility names, or raw DICOM metadata to outputs.
Generated images can still contain burned-in PHI if the source DICOM has text in
the pixels, so default filters skip risky series such as dose reports, screen
saves, scouts, localizers, and objects marked as burned-in.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


WINDOWS = {
    "soft": (40.0, 400.0),
    "lung": (-600.0, 1500.0),
    "bone": (500.0, 2000.0),
    "brain": (40.0, 80.0),
}

RISKY_TEXT_PATTERNS = (
    "dose",
    "report",
    "screen",
    "save",
    "secondary capture",
    "localizer",
    "locator",
    "scout",
    "topogram",
    "surview",
)


@dataclass
class DicomItem:
    path: Path
    ds: Any
    series_key: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create local CT review PNGs/contact sheets and an anonymized manifest."
    )
    parser.add_argument("--input", required=True, type=Path, help="Folder containing DICOM files.")
    parser.add_argument("--output", required=True, type=Path, help="Output folder for local review assets.")
    parser.add_argument(
        "--window",
        choices=["soft", "lung", "bone", "brain", "auto"],
        default="soft",
        help="CT window to apply. 'auto' uses DICOM WindowCenter/WindowWidth when available.",
    )
    parser.add_argument(
        "--contact-count",
        type=int,
        default=25,
        help="Maximum sampled images per series contact sheet.",
    )
    parser.add_argument(
        "--skip-slices",
        action="store_true",
        help="Only write contact sheets and manifest, not every per-slice PNG.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Read and group DICOMs, then print a summary without writing images.",
    )
    parser.add_argument(
        "--include-non-diagnostic",
        action="store_true",
        help="Include scout/localizer/dose/report/screen-save-like series. Private use only.",
    )
    parser.add_argument(
        "--include-burned-in",
        action="store_true",
        help="Include objects marked BurnedInAnnotation=YES. Private use only.",
    )
    parser.add_argument(
        "--include-series-descriptions",
        action="store_true",
        help="Include sanitized SeriesDescription values in the manifest. Off by default.",
    )
    return parser.parse_args()


def import_runtime_deps():
    try:
        import numpy as np
        import pydicom
        from PIL import Image, ImageDraw
    except ImportError as exc:
        raise SystemExit(
            "Missing dependency. Run: pip install -r tools/ct-dicom-processor/requirements.txt"
        ) from exc
    return np, pydicom, Image, ImageDraw


def scalar(value: Any) -> Any:
    if value is None:
        return None
    if isinstance(value, (str, int, float)):
        return value
    try:
        if len(value) == 0:
            return None
        return value[0]
    except TypeError:
        return value


def list_value(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    try:
        return [str(v) for v in value]
    except TypeError:
        return [str(value)]


def number(value: Any) -> float | None:
    value = scalar(value)
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def safe_decimal(value: Any) -> float | None:
    parsed = number(value)
    if parsed is None:
        return None
    return round(parsed, 6)


def sanitized_text(value: Any, max_len: int = 80) -> str | None:
    if value is None:
        return None
    text = re.sub(r"[^A-Za-z0-9 _./+-]", "", str(value)).strip()
    text = re.sub(r"\s+", " ", text)
    if not text:
        return None
    return text[:max_len]


def looks_risky_text(text: str) -> bool:
    lowered = text.lower()
    return any(pattern in lowered for pattern in RISKY_TEXT_PATTERNS)


def is_risky_series(ds: Any) -> tuple[bool, str | None]:
    image_type = " ".join(list_value(getattr(ds, "ImageType", None)))
    series_description = str(getattr(ds, "SeriesDescription", "") or "")
    sop_class = str(getattr(ds, "SOPClassUID", "") or "")
    combined = f"{image_type} {series_description} {sop_class}"
    if looks_risky_text(combined):
        return True, "series resembles dose/report/screen-save/scout/localizer"
    return False, None


def has_burned_in_annotation(ds: Any) -> bool:
    value = str(getattr(ds, "BurnedInAnnotation", "") or "").strip().upper()
    return value == "YES"


def series_key_for(ds: Any, fallback: str) -> str:
    uid = getattr(ds, "SeriesInstanceUID", None)
    if uid:
        return str(uid)
    series_number = getattr(ds, "SeriesNumber", None)
    image_type = "_".join(list_value(getattr(ds, "ImageType", None)))
    return f"series-{series_number or 'unknown'}-{image_type or fallback}"


def read_dicoms(input_dir: Path):
    _, pydicom, _, _ = import_runtime_deps()
    items: list[DicomItem] = []
    skipped: list[dict[str, str]] = []
    for path in sorted(input_dir.rglob("*")):
        if not path.is_file():
            continue
        try:
            ds = pydicom.dcmread(str(path), force=True)
        except Exception:
            continue
        if "PixelData" not in ds:
            skipped.append({"reason": "no PixelData"})
            continue
        if str(getattr(ds, "Modality", "") or "").upper() != "CT":
            skipped.append({"reason": "not CT modality"})
            continue
        items.append(DicomItem(path=path, ds=ds, series_key=series_key_for(ds, path.stem)))
    return items, skipped


def sort_position(ds: Any, file_name: str) -> tuple[int, float | int | str]:
    image_position = getattr(ds, "ImagePositionPatient", None)
    if image_position is not None:
        try:
            return (0, float(image_position[2]))
        except (IndexError, TypeError, ValueError):
            pass
    slice_location = number(getattr(ds, "SliceLocation", None))
    if slice_location is not None:
        return (1, slice_location)
    instance_number = number(getattr(ds, "InstanceNumber", None))
    if instance_number is not None:
        return (2, instance_number)
    return (3, file_name)


def grouped_series(items: list[DicomItem]) -> list[list[DicomItem]]:
    groups: dict[str, list[DicomItem]] = {}
    for item in items:
        groups.setdefault(item.series_key, []).append(item)
    series = list(groups.values())
    for group in series:
        group.sort(key=lambda item: sort_position(item.ds, item.path.name))
    series.sort(
        key=lambda group: (
            number(getattr(group[0].ds, "SeriesNumber", None)) or 999999,
            str(getattr(group[0].ds, "SeriesInstanceUID", "") or group[0].path.name),
        )
    )
    return series


def resolve_window(ds: Any, mode: str) -> tuple[float, float]:
    if mode == "auto":
        center = number(getattr(ds, "WindowCenter", None))
        width = number(getattr(ds, "WindowWidth", None))
        if center is not None and width is not None and width > 0:
            return center, width
        return WINDOWS["soft"]
    return WINDOWS[mode]


def pixel_array_hu(ds: Any):
    np, _, _, _ = import_runtime_deps()
    pixels = ds.pixel_array.astype(np.float32)
    slope = number(getattr(ds, "RescaleSlope", 1.0)) or 1.0
    intercept = number(getattr(ds, "RescaleIntercept", 0.0)) or 0.0
    return pixels * slope + intercept


def window_to_uint8(array: Any, center: float, width: float):
    np, _, _, _ = import_runtime_deps()
    lower = center - width / 2.0
    upper = center + width / 2.0
    clipped = np.clip(array, lower, upper)
    scaled = (clipped - lower) / max(upper - lower, 1.0)
    return (scaled * 255.0).astype(np.uint8)


def image_for_item(item: DicomItem, window_mode: str):
    _, _, Image, _ = import_runtime_deps()
    center, width = resolve_window(item.ds, window_mode)
    pixels = window_to_uint8(pixel_array_hu(item.ds), center, width)
    return Image.fromarray(pixels), center, width


def evenly_sample(items: list[DicomItem], max_count: int) -> list[tuple[int, DicomItem]]:
    if max_count <= 0 or len(items) <= max_count:
        return list(enumerate(items, start=1))
    indexes = sorted({round(i * (len(items) - 1) / (max_count - 1)) for i in range(max_count)})
    return [(idx + 1, items[idx]) for idx in indexes]


def save_contact_sheet(
    sampled: list[tuple[int, Any]],
    output_path: Path,
    window_mode: str,
    thumb_size: int = 220,
) -> tuple[float | None, float | None]:
    _, _, Image, ImageDraw = import_runtime_deps()
    if not sampled:
        return None, None
    cols = min(5, len(sampled))
    rows = math.ceil(len(sampled) / cols)
    label_height = 22
    sheet = Image.new("L", (cols * thumb_size, rows * (thumb_size + label_height)), color=16)
    draw = ImageDraw.Draw(sheet)
    first_center = None
    first_width = None
    for position, (slice_index, item) in enumerate(sampled):
        img, center, width = image_for_item(item, window_mode)
        if first_center is None:
            first_center = center
            first_width = width
        img.thumbnail((thumb_size, thumb_size))
        x = (position % cols) * thumb_size
        y = (position // cols) * (thumb_size + label_height)
        x_offset = x + (thumb_size - img.width) // 2
        sheet.paste(img, (x_offset, y))
        draw.text((x + 4, y + thumb_size + 4), f"slice {slice_index}", fill=235)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output_path)
    return first_center, first_width


def manifest_for_series(
    index: int,
    items: list[DicomItem],
    folder_name: str,
    contact_sheet: str | None,
    slice_paths: list[str],
    window_center: float | None,
    window_width: float | None,
    include_series_descriptions: bool,
) -> dict[str, Any]:
    ds = items[0].ds
    entry: dict[str, Any] = {
        "series_index": index,
        "folder": folder_name,
        "modality": sanitized_text(getattr(ds, "Modality", None)),
        "series_number": sanitized_text(getattr(ds, "SeriesNumber", None)),
        "image_type": list_value(getattr(ds, "ImageType", None)),
        "count": len(items),
        "rows": int(getattr(ds, "Rows", 0) or 0),
        "columns": int(getattr(ds, "Columns", 0) or 0),
        "window_center": window_center,
        "window_width": window_width,
        "slice_thickness_mm": safe_decimal(getattr(ds, "SliceThickness", None)),
        "pixel_spacing_mm": [safe_decimal(v) for v in list_value(getattr(ds, "PixelSpacing", None))],
        "contact_sheet": contact_sheet,
        "slice_pngs": slice_paths,
    }
    if include_series_descriptions:
        entry["series_description_sanitized"] = sanitized_text(
            getattr(ds, "SeriesDescription", None)
        )
    return entry


def write_outputs(args: argparse.Namespace, accepted_series: list[list[DicomItem]], skipped: list[dict[str, str]]) -> None:
    _, _, _, _ = import_runtime_deps()
    args.output.mkdir(parents=True, exist_ok=True)
    manifest: dict[str, Any] = {
        "note": (
            "Anonymized manifest generated from local CT DICOMs. It intentionally omits "
            "patient identifiers, UIDs, accession numbers, exact dates, and facility names."
        ),
        "window_mode": args.window,
        "series": [],
        "skipped": skipped,
    }

    for series_index, items in enumerate(accepted_series, start=1):
        folder_name = f"series_{series_index:03d}"
        series_dir = args.output / "png" / folder_name
        slice_paths: list[str] = []
        window_center: float | None = None
        window_width: float | None = None

        if not args.skip_slices:
            series_dir.mkdir(parents=True, exist_ok=True)
            for slice_index, item in enumerate(items, start=1):
                img, center, width = image_for_item(item, args.window)
                if window_center is None:
                    window_center = center
                    window_width = width
                rel_path = Path("png") / folder_name / f"slice_{slice_index:03d}.png"
                img.save(args.output / rel_path)
                slice_paths.append(rel_path.as_posix())

        sampled = evenly_sample(items, args.contact_count)
        contact_rel = Path("contact_sheets") / f"{folder_name}_contact_sheet.png"
        center, width = save_contact_sheet(sampled, args.output / contact_rel, args.window)
        if window_center is None:
            window_center = center
            window_width = width

        manifest["series"].append(
            manifest_for_series(
                series_index,
                items,
                folder_name,
                contact_rel.as_posix(),
                slice_paths,
                window_center,
                window_width,
                args.include_series_descriptions,
            )
        )

    manifest_path = args.output / "manifest.anonymized.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def print_summary(accepted_series: list[list[DicomItem]], skipped: list[dict[str, str]]) -> None:
    print(f"processable_series={len(accepted_series)}")
    for index, items in enumerate(accepted_series, start=1):
        ds = items[0].ds
        series_number = sanitized_text(getattr(ds, "SeriesNumber", None)) or "unknown"
        image_type = "/".join(list_value(getattr(ds, "ImageType", None))) or "unknown"
        rows = getattr(ds, "Rows", "?")
        columns = getattr(ds, "Columns", "?")
        print(
            f"  series_{index:03d}: series_number={series_number} "
            f"count={len(items)} size={rows}x{columns} image_type={image_type}"
        )
    print(f"skipped_items={len(skipped)}")
    reason_counts: dict[str, int] = {}
    for item in skipped:
        reason_counts[item["reason"]] = reason_counts.get(item["reason"], 0) + 1
    for reason, count in sorted(reason_counts.items()):
        print(f"  skipped_count={count} reason={reason}")


def main() -> int:
    args = parse_args()
    if not args.input.exists():
        print(f"Input folder not found: {args.input}", file=sys.stderr)
        return 2

    items, skipped = read_dicoms(args.input)
    accepted: list[DicomItem] = []
    for item in items:
        if has_burned_in_annotation(item.ds) and not args.include_burned_in:
            skipped.append({"reason": "BurnedInAnnotation=YES"})
            continue
        risky, reason = is_risky_series(item.ds)
        if risky and not args.include_non_diagnostic:
            skipped.append({"reason": reason or "risky non-diagnostic series"})
            continue
        accepted.append(item)

    accepted_series = grouped_series(accepted)
    if args.dry_run:
        print_summary(accepted_series, skipped)
        return 0

    write_outputs(args, accepted_series, skipped)
    print_summary(accepted_series, skipped)
    print(f"wrote={args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
