---
layout: default
title: Dinutuximab
parent: Model Prediction Only (L5)
nav_order: 286
evidence_level: L5
indication_count: 4
---

# Dinutuximab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Dinutuximab: Repurposing Evaluation, Top Prediction "Vertebral Anomalies and Variable Endocrine and T-Cell Dysfunction" (Best-Supported Candidate: Ganglioneuroblastoma)

## One-Sentence Summary

Dinutuximab is an anti-GD2 monoclonal antibody, marketed in Canada as UNITUXIN and used in neuroblastoma.
The TxGNN model's top-ranked prediction is **vertebral anomalies and variable endocrine and T-cell dysfunction**, a rare developmental syndrome, but it has **0 clinical trials** and **0 publications** behind it.
The best-supported candidate is the 2nd-ranked prediction, **ganglioneuroblastoma**, with **7 clinical trials** and **2 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied Canadian licence data |
| Predicted New Indication | Vertebral anomalies and variable endocrine and T-cell dysfunction (rank 1) |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

For comparison, the other predictions are:

| Rank | Predicted Indication | Score | Evidence Level | Decision |
|------|------|------|------|------|
| 2 | Ganglioneuroblastoma | 99.39% | L2 | Proceed with Guardrails |
| 3 | Retroperitoneal neoplasm | 99.35% | L5 | Hold |
| 4 | Chronic myelogenous leukaemia, BCR-ABL1 positive | 99.31% | L5 | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the database. From general knowledge, dinutuximab is a chimeric antibody that binds the disialoganglioside GD2 on tumour cells. It kills them through antibody-dependent cellular cytotoxicity (ADCC) and complement-dependent cytotoxicity (CDC).

**Rank 1 (vertebral anomalies and endocrine/T-cell dysfunction):** No mechanistic rationale can be identified. This is a rare developmental syndrome with immune involvement and no known GD2-driven pathology. The 99.42% score is a graph-based prediction only, with no supporting trials or literature.

**Rank 2 (ganglioneuroblastoma):** The mechanism is directly plausible. Ganglioneuroblastoma sits in the neuroblastic tumour spectrum, whose cells express GD2, and GD2 targeting is the basis for dinutuximab's use in high-risk neuroblastoma. Two caveats apply:
- The supplied trials enrol neuroblastoma populations, not ganglioneuroblastoma specifically. Differentiated, Schwannian-stroma-rich tumours may express less GD2, so histology-specific applicability needs confirmation.
- Because the original indication is missing from the dataset, it is unclear whether this is on-label use or true repurposing. Verify against the Canadian label.

**Ranks 3 and 4:** "Retroperitoneal neoplasm" is an anatomical category rather than a GD2-defined disease. The link likely arises because neuroblastoma can occur in the retroperitoneum. Chronic myelogenous leukaemia is driven by the BCR-ABL1 kinase and has no established GD2 dependence. Neither has trials or literature.

---

## Clinical Trial Evidence

**Rank 1 (top prediction):** Currently no related clinical trials registered.

**Ganglioneuroblastoma (rank 2, best-supported candidate):**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01767194](https://clinicaltrials.gov/study/NCT01767194) | Phase 2 | Completed | 73 | Randomised trial of irinotecan/temozolomide with temsirolimus or dinutuximab in relapsed/refractory neuroblastoma. Results published (PMID 28549783). Strongest completed clinical evidence. |
| [NCT06172296](https://clinicaltrials.gov/study/NCT06172296) | Phase 3 | Recruiting | 478 | Adds dinutuximab to induction chemotherapy and multimodal therapy in newly diagnosed high-risk neuroblastoma. No results yet. |
| [NCT03126916](https://clinicaltrials.gov/study/NCT03126916) | Phase 3 | Recruiting | 750 | Adds 131I-MIBG or an ALK inhibitor to intensive therapy in high-risk neuroblastoma or ganglioneuroblastoma. Dinutuximab is likely part of the backbone but is not the tested variable. |
| [NCT04385277](https://clinicaltrials.gov/study/NCT04385277) | Phase 2 | Active, not recruiting | 41 | Pilot of dinutuximab, GM-CSF and isotretinoin with irinotecan/temozolomide after consolidation in high-risk neuroblastoma. |
| [NCT03786783](https://clinicaltrials.gov/study/NCT03786783) | Phase 2 | Active, not recruiting | 42 | Pilot induction regimen incorporating ch14.18 (dinutuximab) and sargramostim in newly diagnosed high-risk neuroblastoma. |
| [NCT07375563](https://clinicaltrials.gov/study/NCT07375563) | Phase 3 | Recruiting | 5 | Chemoimmunotherapy plus autologous NK cells in relapsed/refractory high-risk neuroblastoma and ganglioneuroblastoma. Very small enrolment. |
| [NCT07437963](https://clinicaltrials.gov/study/NCT07437963) | Phase 1/2 | Not yet recruiting | 76 | Dinutuximab/cyclophosphamide/topotecan/GM-CSF with or without iberdomide in relapsed/refractory neuroblastoma. No data yet. |

---

## Literature Evidence

**Rank 1 (top prediction):** Currently no related literature available.

**Ganglioneuroblastoma (rank 2, best-supported candidate):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28549783](https://pubmed.ncbi.nlm.nih.gov/28549783/) | 2017 | RCT | The Lancet. Oncology | COG ANBL1221, an open-label randomised Phase 2 trial. Tested adding temsirolimus or dinutuximab to irinotecan-temozolomide in relapsed/refractory neuroblastoma. |
| [37929737](https://pubmed.ncbi.nlm.nih.gov/37929737/) | 2025 | Case report / Review | Current Pediatric Reviews | Late relapse in neuroblastoma. Background on the poor outcomes of relapsed/refractory disease. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2483076 | UNITUXIN |

Dosage form, manufacturer and approved-indication text were not included in the supplied record.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-GD2 monoclonal antibody acting through ADCC/CDC) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Follow institutional handling procedures for antineoplastic biologics and the package insert |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug.

---

## Conclusion and Next Steps

**Decision: Hold** for the top-ranked prediction (vertebral anomalies and variable endocrine and T-cell dysfunction).

**Rationale:**
- The score is high (99.42%), but there are no trials, no literature and no plausible GD2-related mechanism, so this is an unsupported graph prediction.
- Ranks 3 and 4 are also Hold for the same reasons.
- **Ganglioneuroblastoma** is the only prediction with meaningful support and would be **Proceed with Guardrails** (L2). It has a plausible GD2 mechanism, a completed randomised Phase 2 trial and several ongoing Phase 2/3 trials. Level L2 rather than L1 because the Phase 3 trials are still recruiting with no reported results.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications. This is a blocking gap for safety screening.
- Mechanism-of-action data from DrugBank.
- The approved indication text from the Canadian licence, to confirm whether ganglioneuroblastoma is on-label or a true repurposing case.
- Evidence of GD2 expression in ganglioneuroblastoma, especially the differentiated, Schwannian-stroma-rich subtypes.
- Results from the ongoing Phase 3 trials (NCT06172296, NCT03126916).

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

