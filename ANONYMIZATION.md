# Anonymization Rules

This folder is intended for a public or semi-public GitHub repository.

## Removed Or Generalized

- Patient name and initials.
- Patient date of birth.
- Medical record numbers and patient IDs.
- Pathology accession numbers.
- Case numbers and order numbers.
- Exact collection, exam, report, and verification dates.
- Facility names, VA locations, clinic names, city/state identifiers, and addresses.
- Clinician names and signatures.
- Raw report text copied from the medical record.
- DICOM files, images, screenshots, ZIP files, and generated CT review assets.
- Exact military service dates, command names, boat/hull identifiers, deployment locations, witness names, and detailed private exposure statements.

## Preserved

- Clinically meaningful age band: adult male in his 30s.
- Laterality: patient-right, because it is clinically relevant.
- Diagnosis: metastatic squamous cell carcinoma in a cervical lymph node.
- Key biomarkers: CK5 positive; p16 block positive.
- Flow cytometry result summarized at a high level.
- Generalized military-service exposure context when relevant: former submarine service with reported AFFF/PFAS exposure.
- Relative sequence of events.
- Research sources and trial identifiers from public databases.

## Date Handling

Exact dates are converted to relative labels:

- `Day 0`: biopsy day / tissue obtained.
- `Day +1`: tissue received or pathology processing event.
- `Day +2`: final pathology signed and communicated.
- `Day +6`: first full daily action plan after confirmed pathology and benefits planning.
- Earlier imaging is listed as `Day -34` based on the internal project timeline, without publishing the calendar date.

If future updates require more precision, use month/quarter labels only if the privacy benefit is worth the clinical context tradeoff.

## Future Update Checklist

Before committing new content, search the export folder for:

- Names.
- Locations.
- Exact dates.
- Accession numbers.
- Medical record or case numbers.
- Screenshots or raw portal text.
- Image filenames copied from the private vault.
- Military service identifiers: boat, hull, command, deployment, exact service dates, duty section, or witness names.
