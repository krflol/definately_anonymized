# Imaging Summary

## Scope

This is an anonymized summary of the private CT review work. No DICOM files, screenshots, image-derived assets, facility metadata, or raw imaging reports are included in this repository.

## Current Imaging Context

- Non-contrast CT neck was available for private review.
- The clinically relevant abnormality was on the patient-right side, matching the biopsy site.
- Earlier metadata reportedly described the side incorrectly; this public record preserves only the clinically confirmed patient-right laterality.
- The CT was not a complete staging study.
- Initial PET/CT staging has since been summarized in the private vault. No raw report text or exact imaging date is published here.

## Interpretable Clinical Takeaways

- The visible patient-right neck/cervical-chain abnormality aligns with the later biopsy-proven malignant lymph-node disease.
- PET/CT identified avid patient-right neck nodal disease.
- PET/CT showed tonsillar/oropharyngeal uptake, with right tonsil/oropharynx a suspected primary site, but bilateral tonsillar uptake may require clinical correlation before treating PET alone as definitive primary-site proof.
- PET/CT did not report suspicious FDG uptake in chest, abdomen, pelvis, or bone.
- The current imaging frame is therefore provisional local-regional / `M0`, pending clinician-confirmed staging and primary-site workup.
- Contrast CT/MRI neck or directed ENT evaluation may still be needed depending on oncology/ENT/radiation plan.

## Public Repo Exclusions

Excluded from this repo:

- DICOM files.
- CT viewer exports.
- Contact sheets and annotated slices.
- Raw scanner metadata.
- Facility names and exact imaging dates.

## Reproducible Local Tooling

This repository includes a reusable DICOM CT processing tool at `tools/ct-dicom-processor/`. The tool can generate local PNG review images, contact sheets, and an anonymized manifest from a private DICOM folder.

Generated images and manifests are ignored by Git. They should be used locally for review only unless separately de-identified and manually approved for publication.

## Questions For Care Team

- What imaging is required for final staging?
- Does the care team accept the PET/CT as confirming `M0`?
- Does the tonsillar/oropharyngeal uptake identify a primary site, or is further ENT evaluation/biopsy needed?
- Does left-sided tonsillar uptake appear physiologic, inflammatory, synchronous disease, or clinically irrelevant?
- Is contrast MRI or contrast CT neck needed?
- Are there additional suspicious lymph nodes?
- Does imaging suggest a primary site, or is this still an occult-primary workup?
