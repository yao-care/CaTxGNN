---
layout: default
title: Abemaciclib
parent: Model Prediction Only (L5)
nav_order: 13
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Abemaciclib: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Abemaciclib"
predicted_indications: ["rheumatoid arthritis", "hyperthyroidism", "multiple endocrine neoplasia", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "homozygous familial hypercholesterolemia", "heart disease", "Laubry-Pezzi syndrome", "Pierre Robin syndrome associated with a chromosomal anomaly", "Jeune syndrome situs inversus", "amyotrophic lateral sclerosis"]
---

# Abemaciclib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Abemaciclib: From Its Approved Use to Rheumatoid Arthritis

## One-Sentence Summary

Abemaciclib is an oral CDK4/6 inhibitor marketed in Canada as VERZENIO. The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but there are currently **no registered clinical trials** and only **2 publications** (one observational cohort, one preclinical study), so the prediction rests mainly on the model score and mechanistic plausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the licence records contain no indication text) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 97.32% |
| Evidence Level | L4 (preclinical or mechanistic studies only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Abemaciclib is known as a cyclin-dependent kinase 4/6 (CDK4/6) inhibitor, a class of drugs that blocks cell-cycle progression. Its efficacy in its original (oncology) use has been established, and mechanistically it may be applicable to rheumatoid arthritis.

In rheumatoid arthritis, overproliferation of fibroblast-like synoviocytes and expansion of immune cells drive joint damage. CDK4/6 inhibition could plausibly suppress both processes, which is the basis of the biological link. A preclinical nanoplatform study that delivers abemaciclib to synoviocytes, inducing cell-cycle arrest and apoptosis, points in the same direction.

This link is still hypothetical. The only clinical literature is an observational study of immune-mediated diseases in breast cancer patients taking CDK4/6 inhibitors. It describes how such diseases occur or progress, not any therapeutic benefit. The preclinical study does not test abemaciclib as a clinical therapy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40504547](https://pubmed.ncbi.nlm.nih.gov/40504547/) | 2025 | Cohort | The Oncologist | Examined pre-existing and emerging immune-mediated diseases in HR+/HER2- breast cancer patients receiving CDK4/6 inhibitors plus endocrine therapy. It addresses disease occurrence and course, not treatment benefit. |
| [42289719](https://pubmed.ncbi.nlm.nih.gov/42289719/) | 2026 | Preclinical | Journal of Nanobiotechnology | A pH-responsive nanoplatform loaded with abemaciclib induced cell-cycle arrest and apoptosis in fibroblast-like synoviocytes for RA treatment. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02487101 | VERZENIO | Not listed | Not listed |
| 02487098 | VERZENIO | Not listed | Not listed |
| 02487136 | VERZENIO | Not listed | Not listed |
| 02487128 | VERZENIO | Not listed | Not listed |

All four authorizations are valid single-ingredient products.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (CDK4/6 kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions (typically blood counts, liver and renal function) |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 potential interactions. The first 20 reviewed include several rated **Major**: clarithromycin, cobicistat, deferiprone, samarium (153Sm) lexidronam and lumacaftor. Many others are rated **Moderate**, including aprepitant, clotrimazole, dexamethasone, metformin, fluconazole, erythromycin, chloramphenicol, ticagrelor and roflumilast. Several of these are CYP3A-related, so co-medication in an RA population would need careful review.
- **Other literature signals** (from literature retrieved for other predicted indications): reports on CDK4/6 inhibitors describe QTc prolongation, thromboembolic events (specifically noted with abemaciclib), atrial arrhythmias and kidney injury signals. These matter if long-term use in a non-oncology population is considered.

Package insert warnings and contraindications were not available for this report; please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (97.32%), but no clinical trials exist, the clinical literature does not show therapeutic benefit, and the only supportive work is preclinical. The oncology-level safety profile, including cardiovascular and thromboembolic signals, would also need justification in a chronic inflammatory condition.

**To proceed, the following is needed:**
- Mechanism-of-action data and the approved indication text from the package insert
- Health Canada package insert warnings and contraindications for a formal safety screen
- Preclinical efficacy data for abemaciclib in RA models (for example, arthritis animal models)
- A risk-benefit assessment of long-term safety (cardiovascular, thromboembolic, haematological) in RA patients
- An interaction review against common RA co-medications, such as corticosteroids and metformin
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

