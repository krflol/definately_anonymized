# Anonymized Cancer Care Record

This repository is an anonymized, patient-maintained record of a head-and-neck cancer diagnostic and treatment-planning effort.

It is designed to preserve the decision trail, research notes, questions for clinicians, and treatment-readiness work without publishing identifiable medical records.

## Current Clinical Snapshot

- Patient: adult male in his 30s.
- Presentation: patient-right cervical lymph-node conglomerate / neck mass.
- Biopsy result: metastatic squamous cell carcinoma, moderate to poorly differentiated.
- Immunohistochemistry: CK5 positive; p16 positive with block staining.
- Flow cytometry: no significant lymphoid immunophenotypic abnormalities.
- Current interpretation: HPV-mediated oropharyngeal squamous cell carcinoma is a leading possibility, but primary site and full stage are pending.

## What This Is Not

- Not medical advice.
- Not a complete medical record.
- Not raw pathology, imaging, or portal export data.
- Not a substitute for oncology, ENT, radiation oncology, dental, speech/swallow, nutrition, or tumor-board guidance.

## Repository Structure

- `docs/` - anonymized clinical summaries, timeline, oral-care notes, and lifestyle/treatment-readiness plan.
- `research/` - diagnosis-specific research notes on immunotherapy, HPV vaccines/mRNA, CRISPR/cell therapy, HPV ctDNA, and trials.
- `tools/` - reproducible local tooling, including a DICOM CT processor that keeps generated medical images out of Git.
- `templates/` - reusable trackers for future updates without adding private identifiers.
- `ANONYMIZATION.md` - rules used to remove or generalize identifying information.

## Key Open Clinical Questions

- What is the primary site: tonsil, base of tongue, other oropharynx, oral cavity, larynx/hypopharynx, skin, or unknown primary?
- Is this formally staged as HPV-mediated oropharyngeal SCC?
- Is additional HPV DNA/RNA/genotype testing needed beyond p16?
- What is the full stage after PET/CT and complete workup?
- Should PD-L1 CPS be run on the biopsy specimen?
- Is treatment expected to be surgery-based, radiation/chemoradiation-based, or trial-based?
- Are there trial options worth screening before standard treatment begins?

## Public-Record Guardrails

- Avoid exact dates, names, accession numbers, medical-record numbers, facility names, phone numbers, addresses, and raw report text.
- Keep raw DICOMs, CT screenshots, pathology reports, portal screenshots, ZIP files, and clinician messages out of this repo.
- Use relative timeline labels such as `Day -34`, `Day 0`, and `Day +2`.
- Add new facts as summaries, not pasted medical-record blocks.

## Source References

Primary public sources used in the research notes include NCI, FDA, and ClinicalTrials.gov pages. See `research/source-log.md`.
