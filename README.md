# Anonymized Cancer Care Record

This repository is an anonymized, patient-maintained record of a head-and-neck cancer diagnostic and treatment-planning effort.

It is designed to preserve the decision trail, research notes, questions for clinicians, and treatment-readiness work without publishing identifiable medical records.

## Current Clinical Snapshot

- Patient: adult male in his 30s.
- Presentation: patient-right cervical lymph-node conglomerate / neck mass.
- Biopsy result: metastatic squamous cell carcinoma, moderate to poorly differentiated.
- Immunohistochemistry: CK5 positive; p16 positive with block staining.
- Flow cytometry: no significant lymphoid immunophenotypic abnormalities.
- Initial PET/CT supports a provisional local-regional / `M0` frame, without suspicious uptake reported in the chest, abdomen, pelvis, or bones.
- Primary-site workup update: diagnostic suspension microlaryngoscopy inspected the upper aerodigestive tract, small patient-right base-of-tongue biopsies were taken, and the patient-right tonsil was removed en bloc. No neck dissection was performed.
- Current interpretation: HPV-mediated oropharyngeal squamous cell carcinoma remains the leading possibility. Tonsil and base-of-tongue pathology, exact primary site, AJCC Version 9 TNM/stage, and definitive treatment of the known neck-node disease remain pending.

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
- `docs/provisional-m0-locoregional-research.md` - research update specific to provisional M0 locoregional disease.
- `docs/diagnostic-primary-site-procedure.md` - anonymized operative-event summary, pathology branches, and updated decision points.
- `docs/nutrition-formula-and-feeding-tube-readiness.md` - oral formula and stockpile plan for a reactive feeding-tube strategy.
- `daily-action-plans/` - public-safe daily operating plans using relative dates.
- `research/` - diagnosis-specific research notes on immunotherapy, HPV vaccines/mRNA, CRISPR/cell therapy, HPV ctDNA, and trials.
- `tools/` - reproducible local tooling, including a DICOM CT processor that keeps generated medical images out of Git.
- `templates/` - reusable trackers for future clinical, results, and benefits updates without adding private identifiers.
- `ANONYMIZATION.md` - rules used to remove or generalize identifying information.

## Key Open Clinical Questions

- Do the patient-right tonsil or patient-right base-of-tongue specimens contain carcinoma, and which site is the primary?
- If the tonsil is positive, what are tumor size, HPV-specific result, margins, lymphovascular invasion, and perineural invasion?
- Is this formally staged as HPV-mediated oropharyngeal SCC?
- What are cT, cN, cM, AJCC Version 9 stage, node size/laterality, and imaging-detected extranodal-extension status?
- Is additional HPV DNA/RNA/genotype testing needed beyond p16?
- Should PD-L1 CPS be run on the biopsy specimen?
- What is the definitive plan for the known patient-right cervical-node disease: neck dissection, radiation, chemoradiation, or another tumor-board plan?
- Was the recent procedure solely diagnostic, and which later event, if any, will count as definitive oncologic surgery?
- Does perioperative pembrolizumab apply only if the exact surgery-based/resectable/PD-L1 CPS criteria fit?
- Should HPV ctDNA / TTMV-HPV DNA be drawn before definitive nodal treatment, labeled as post-tonsillectomy rather than a true preoperative baseline?
- If provisional `M0` is confirmed, which curative-intent lane applies: surgery-based, definitive chemoradiation, or trial?
- If oral intake drops during treatment, what is the local timeline for NG tube, PEG/RIG, IV hydration, formula authorization, and supply delivery?
- Does any newly diagnosed trial remain technically available after a diagnostic tonsillectomy, without delaying standard curative care?
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
