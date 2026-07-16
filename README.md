# Anonymized Cancer Care Record

This repository is an anonymized, patient-maintained record of a head-and-neck cancer diagnostic and treatment-planning effort. It preserves the clinical decision trail, research, care questions, and treatment-readiness work without publishing identifiable medical records.

> **Snapshot status: Day +29.** Diagnostic primary-site surgery is complete. Patient-right tonsil and patient-right base-of-tongue pathology are pending. The biopsy-proven patient-right cervical-node cancer remains known disease.

## Current Clinical Snapshot

### Confirmed

| Domain | Current fact |
| --- | --- |
| Patient | Adult male in his 30s. |
| Presentation | Patient-right cervical lymph-node conglomerate / neck mass. |
| Controlling diagnosis | Metastatic squamous cell carcinoma in a patient-right cervical lymph node, moderate to poorly differentiated. |
| Biomarkers | CK5 positive; p16 positive with block staining. |
| Flow cytometry | No significant lymphoid immunophenotypic abnormalities; lymphoma is not supported by the sampled node. |
| Distant staging | PET/CT supports a provisional local-regional / `cM0` frame, with no suspicious uptake reported in the chest, abdomen, pelvis, or bones. |
| Leading origin | HPV-mediated oropharyngeal squamous cell carcinoma remains the leading possibility, but the exact primary site and HPV-specific result are not yet established. |

A later portal/billing label described adenocarcinoma metastatic to a head-and-neck lymph node. Case-management review confirmed that the controlling backend pathology remained squamous cell carcinoma and that the conflicting label was administrative/coding-related. This record does not treat adenocarcinoma as a second diagnosis.

### Latest Clinical Event

On `Day +29`, a diagnostic primary-site procedure:

- inspected the oral cavity, oropharynx, larynx, and hypopharynx using suspension microlaryngoscopy;
- obtained a few small patient-right base-of-tongue biopsies;
- removed the patient-right tonsil en bloc;
- did not include a neck dissection or removal of the known malignant cervical node;
- reported minimal blood loss, no complications, and stable recovery transfer.

The procedure was documented as an effort to identify the primary site. It was not documented as complete removal of all known cancer.

### Precise Current Interpretation

- **Tonsil positive / tongue base negative:** the patient-right tonsil would be the likely primary. Gross primary-site tissue may have been removed, but margins and surgical intent must establish whether primary-site control was definitive.
- **Tongue base positive:** that site was only biopsied, so the tongue-base primary would remain in place.
- **Both positive or both negative:** specialist pathology and tumor-board interpretation are required.
- **Every outcome:** the established patient-right cervical-node SCC remains because no neck dissection occurred.

The current working frame remains potentially curable locoregional disease, not proven distant metastatic disease. Formal treatment intent and the definitive surgery-versus-radiation/chemoradiation pathway remain pending.

### Staging Status

HPV-associated oropharyngeal cancers diagnosed in 2026 use **AJCC Version 9**. An earlier provisional line transcribed as approximately `T2 N2a M0 / Stage III` did not identify the staging system and should not be carried forward as the formal current stage.

The next written staging line should provide:

> `cT__ cN__ cM0, AJCC Version 9 HPV-associated oropharynx, clinical Stage __; imaging-detected extranodal extension present/absent/indeterminate.`

Because no neck dissection occurred, this operation cannot provide a complete pathologic nodal category, involved-node count, or pathologic extranodal-extension assessment.

## Immediate Decision Gates

1. Obtain final pathology for the patient-right tonsil and patient-right base-of-tongue biopsies.
2. If the tonsil is positive, capture tumor size, histologic type, HPV-specific testing, margins, lymphovascular invasion, perineural invasion, and AJCC Version 9 `pT`.
3. Obtain the written AJCC Version 9 `cT/cN/cM`, stage group, and imaging-detected extranodal-extension assessment.
4. Document the definitive plan for the known patient-right cervical-node disease: neck dissection, radiation, chemoradiation, or another multidisciplinary plan.
5. Identify which future event, if any, will count as definitive oncologic surgery.
6. Resolve HPV DNA/RNA/genotype, PD-L1 CPS, cisplatin eligibility, tumor-board review, and pretreatment supportive-care needs.
7. Ask whether HPV ctDNA should be drawn before definitive nodal treatment, accurately labeled as post-tonsillectomy rather than a true preoperative baseline.
8. Screen newly diagnosed trials only if exact eligibility remains plausible and screening will not delay curative care.

## Current Research Position

- Standard curative-intent staging and treatment remain the priority.
- FDA-approved perioperative pembrolizumab applies only to a defined PD-L1-positive, resectable locally advanced, surgery-based sequence that begins before definitive surgery.
- The recent diagnostic procedure does not automatically close every neoadjuvant trial window, but eligibility now requires direct protocol/site review.
- HPV therapeutic vaccines, mRNA approaches, engineered T-cell therapy, and CRISPR remain trial-stage or earlier for this setting.
- HPV ctDNA is an adjunct and possible trial tool, not a replacement for pathology, imaging, examination, or formal staging.
- De-intensification should be protocol-driven or specifically supported by the multidisciplinary team; it should not be assumed safer because the tumor may be HPV-associated.

## Quick Links

- [Clinical summary](docs/clinical-summary.md)
- [Relative timeline](docs/timeline.md)
- [Pathology summary](docs/pathology-summary.md)
- [Imaging summary](docs/imaging-summary.md)
- [Diagnostic primary-site procedure](docs/diagnostic-primary-site-procedure.md)
- [Provisional M0 and staging update](docs/provisional-m0-locoregional-research.md)
- [Plain-English treatment explainers](docs/plain-english-treatment-explainers.md)
- [Head-and-neck cancer glossary](docs/glossary-head-neck-cancer.md)
- [Nutrition and feeding-tube readiness](docs/nutrition-formula-and-feeding-tube-readiness.md)
- [Benefits and financial assistance](docs/benefits-financial-assistance.md)
- [VA toxic-exposure / AFFF-PFAS notes](docs/va-toxic-exposure-afff-pfas.md)
- [Emerging-treatment research index](research/README.md)
- [Clinical-trial search playbook](research/clinical-trial-search.md)
- [Research source log](research/source-log.md)

Post-tonsillectomy recovery and emergency guardrails are summarized in [the diagnostic procedure note](docs/diagnostic-primary-site-procedure.md#immediate-recovery-guardrails). The surgeon's discharge instructions control.

## Repository Structure

- `docs/` - anonymized clinical summaries, timeline, operative abstraction, oral care, nutrition, lifestyle, benefits, and treatment-readiness notes.
- `daily-action-plans/` - public-safe operating plans using relative dates.
- `research/` - diagnosis-specific notes on immunotherapy, HPV vaccines/mRNA, cell therapy, CRISPR, HPV ctDNA, de-intensification, and trials.
- `tools/` - reproducible local tooling, including a DICOM CT processor that keeps generated medical images out of Git.
- `templates/` - reusable clinical, result, appointment, and benefits trackers.
- `ANONYMIZATION.md` - publication rules and relative-date conventions.

## What This Is Not

- Not medical advice or a complete medical record.
- Not a substitute for oncology, ENT, radiation oncology, pathology, dental, speech/swallow, nutrition, or tumor-board guidance.
- Not a repository for raw reports, DICOMs, screenshots, portal exports, or direct identifiers.

## Public-Record Guardrails

- No names, exact patient dates, accession numbers, record numbers, facilities, phone numbers, addresses, or raw report text.
- Raw DICOMs, CT screenshots, pathology reports, portal screenshots, ZIP files, and clinician messages remain private.
- Patient events use relative labels such as `Day -34`, `Day 0`, and `Day +29`.
- Military-service details remain generalized; command, vessel, deployment, service dates, locations, and witness details are excluded.
- New facts are summarized and manually reviewed before publication.

## Sources

Primary public sources include NCI, FDA, the American College of Surgeons/AJCC, CAP, ClinicalTrials.gov, and major peer-reviewed studies. See the [research source log](research/source-log.md).
