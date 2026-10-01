---
layout: default
title: Enzalutamide
parent: Model Prediction Only (L5)
nav_order: 332
evidence_level: L5
indication_count: 10
---

# Enzalutamide
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

# Enzalutamide: From Prostate Cancer to Prostate Cancer/Brain Cancer Susceptibility

## One-Sentence Summary

Enzalutamide is an androgen receptor (AR) inhibitor marketed for prostate cancer. The TxGNN model ranks **prostate cancer/brain cancer susceptibility** as its top prediction, but this term describes a genetic susceptibility phenotype rather than a treatable disease. It has **0 clinical trials** and **0 publications** linked, so this is a graph prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate cancer (inferred from the dataset's rationale notes; the licence indication text is empty) |
| Predicted New Indication | Prostate cancer/brain cancer susceptibility |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Enzalutamide is known to be an AR signalling inhibitor, and the dataset's own rationale describes it as an AR inhibitor whose approved use is in prostate cancer.

The prostate cancer half of the predicted term overlaps with the approved use, which likely explains the high score of 0.997. The term itself is a susceptibility phenotype, not a disease state that can be treated. There is no rationale for treating brain cancer susceptibility. The score reflects network proximity in the knowledge graph, not a validated mechanism.

**Where the evidence is.** Most of the other top-10 predictions are rare benign tumours or broad categories with no linked evidence (all L5, Hold). The exception is **prostate neoplasm** (rank 9, score 98.37%). It has 50 linked trials, including a completed Phase 3b RCT, and is graded L1 (Proceed with Guardrails). That entry is on-label use in prostate cancer, not true repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the predicted indication "prostate cancer/brain cancer susceptibility".

For reference, the strongest trials linked to the on-label entry (prostate neoplasm) are:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02288247](https://clinicaltrials.gov/study/NCT02288247) | Phase 3b | Completed | 688 | Randomized, double-blind, placebo-controlled study of continuing enzalutamide alongside docetaxel plus prednisolone in chemotherapy-naïve mCRPC after progression on enzalutamide alone |
| [NCT02815033](https://clinicaltrials.gov/study/NCT02815033) | Phase 2 | Completed | 66 | Single-arm study of enzalutamide with PET/CT and MRI imaging in hormone-sensitive metastatic prostate cancer |
| [NCT02124668](https://clinicaltrials.gov/study/NCT02124668) | Phase 2 | Completed | 30 | Single-arm safety study in progressive mCRPC after docetaxel |

Only 10 of 50 trials were provided for review.

---

## Literature Evidence

Currently no related literature available for the predicted indication. The on-label entry (prostate neoplasm) has 0 linked publications. The literature attached to the benign prostate neoplasm entry (rank 8) includes the Phase 3 RCTs PROSPER ([29949494](https://pubmed.ncbi.nlm.nih.gov/29949494/), nmCRPC) and PREVAIL ([27477525](https://pubmed.ncbi.nlm.nih.gov/27477525/), mCRPC). These concern malignant prostate cancer, not the predicted susceptibility term.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2407329 | XTANDI |

Dosage form and approved indication text are not available in the source data.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted hormonal therapy (androgen receptor inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

No Canadian label warnings, contraindications, or drug interaction records are available in the Evidence Pack (the interaction query returned no results). Please refer to the package insert for safety information.

The dataset's rationale notes flag seizure risk, fatigue, and cardiovascular effects as concerns that would be hard to justify in benign or non-treatable conditions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction is a genetic susceptibility phenotype with no linked trials or literature, so it is not actionable as a repurposing target. The only well-supported entry, prostate neoplasm, is existing approved use rather than a new indication.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking gap; needed for any safety screening)
- Mechanism of action data and original indications from DrugBank
- Confirmation of the approved populations (e.g., CRPC, nmCRPC, mHSPC) against current Canadian labeling
- If a genuine new indication is sought, a review of lower-ranked predictions beyond the prostate-related terms, since none of the top-10 entries shows a novel, evidence-backed opportunity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

