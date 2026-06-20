# CT DICOM Processor

This tool converts a local DICOM CT folder into review PNGs, contact sheets, and an anonymized manifest.

It is included so the imaging workflow is reproducible without publishing DICOM files or derived images.

## Privacy Model

The script does not write patient name, patient ID, accession number, study UID, series UID, exact study dates, facility names, or clinician names to the manifest.

It also skips risky series by default:

- dose reports;
- screen saves;
- scout/localizer images;
- DICOM objects marked with burned-in annotation.

Those skipped series can contain text burned into the pixel data. Use overrides only for private local review.

## Install

From this repository folder:

```powershell
cd tools\ct-dicom-processor
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Basic Use

```powershell
python process_ct_dicoms.py --input C:\path\to\dicom_folder --output output\ct_review
```

This creates:

- `png/` - windowed 8-bit PNG slices;
- `contact_sheets/` - evenly sampled contact sheets per series;
- `manifest.anonymized.json` - non-identifying metadata and output paths.

The default CT window is soft tissue, which is usually more useful for neck soft-tissue review:

```powershell
python process_ct_dicoms.py --input C:\path\to\dicom_folder --output output\ct_review --window soft
```

Other windows:

```powershell
python process_ct_dicoms.py --input C:\path\to\dicom_folder --output output\ct_lung --window lung
python process_ct_dicoms.py --input C:\path\to\dicom_folder --output output\ct_bone --window bone
```

## Safer Dry Run

List processable and skipped series without writing images:

```powershell
python process_ct_dicoms.py --input C:\path\to\dicom_folder --output output\ct_review --dry-run
```

## Private-Only Overrides

Include likely non-diagnostic series such as scout/localizer:

```powershell
python process_ct_dicoms.py --input C:\path\to\dicom_folder --output output\ct_review --include-non-diagnostic
```

Include DICOM objects marked as burned-in:

```powershell
python process_ct_dicoms.py --input C:\path\to\dicom_folder --output output\ct_review --include-burned-in
```

These overrides are for local private review only. Do not commit the outputs.

## Limits

- This is not a diagnostic viewer.
- It does not replace radiology interpretation.
- It does not guarantee that pixel data contains no burned-in PHI.
- Review generated images manually before sharing anywhere.

