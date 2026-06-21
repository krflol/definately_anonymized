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
- `docs/benefits-financial-assistance.md` - public-safe benefits, leave, SSDI/SSI, VA, and assistance planning.
- `docs/va-toxic-exposure-afff-pfas.md` - generalized VA toxic-exposure/AFFF-PFAS strategy without service identifiers.
- `docs/plain-english-treatment-explainers.md` - patient-facing explanations of treatment categories in the research matrix.
- `docs/glossary-head-neck-cancer.md` - searchable glossary of clinical and benefits-relevant terms.
- `docs/reviewer-synthesis-staging-first.md` - outside-review synthesis emphasizing classification and staging before treatment speculation.
- `daily-action-plans/` - public-safe daily operating plans using relative dates.
- `research/` - diagnosis-specific research notes on immunotherapy, HPV vaccines/mRNA, CRISPR/cell therapy, HPV ctDNA, and trials.
- `tools/` - reproducible local tooling, including a DICOM CT processor that keeps generated medical images out of Git.
- `templates/` - reusable trackers for future clinical, results, and benefits updates without adding private identifiers.
- `ANONYMIZATION.md` - rules used to remove or generalize identifying information.

## Key Open Clinical Questions

- What is the primary site: tonsil, base of tongue, other oropharynx, oral cavity, larynx/hypopharynx, skin, or unknown primary?
- Is this formally staged as HPV-mediated oropharyngeal SCC?
- What are cT, cN, cM, AJCC 8 stage, node size/laterality, and extranodal-extension suspicion?
- Is additional HPV DNA/RNA/genotype testing needed beyond p16?
- What is the full stage after PET/CT and complete workup?
- Should PD-L1 CPS be run on the biopsy specimen?
- Is treatment expected to be surgery-based, radiation/chemoradiation-based, or trial-based?
- Does perioperative pembrolizumab apply only if the exact surgery-based/resectable/PD-L1 CPS criteria fit?
- Should HPV ctDNA / TTMV-HPV DNA be drawn as a pretreatment baseline?
- Are there trial options worth screening before standard treatment begins?
- Which benefits/work-leave/VA claim tracks should be started before treatment creates income or insurance disruption?
- Does generalized submarine AFFF/PFAS exposure support a VA direct service-connection / TERA theory, separate from any PACT Act covered-location presumption?

## Public-Record Guardrails

- Avoid exact dates, names, accession numbers, medical-record numbers, facility names, phone numbers, addresses, and raw report text.
- Keep raw DICOMs, CT screenshots, pathology reports, portal screenshots, ZIP files, and clinician messages out of this repo.
- Use relative timeline labels such as `Day -34`, `Day 0`, and `Day +2`.
- Daily plans should use relative labels such as `Day +6`, not calendar dates.
- Add new facts as summaries, not pasted medical-record blocks.
- Keep military service history generalized; do not publish command, boat, hull, deployment, location, service-date, or witness details.

## Source References

Primary public sources used in the research notes include NCI, FDA, and ClinicalTrials.gov pages. See `research/source-log.md`.
