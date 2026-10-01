---
layout: default
title: Denosumab
parent: Model Prediction Only (L5)
nav_order: 257
evidence_level: L5
indication_count: 2
---

# Denosumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Denosumab: From Osteoporosis and Bone Loss to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Denosumab is a bone-targeted drug marketed in Canada, and the literature describes its use in osteoporosis and bone loss. The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, but **no clinical trials and no publications** currently support this specific prediction. This is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data; the literature describes osteoporosis and bone loss |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this record. Denosumab is marketed in Canada under several brand names. The literature describes its use in osteoporosis and in bone loss from androgen-deprivation therapy. Mechanistically, it may be applicable to diabetic retinopathy, but this has not been verified.

One possible route is modulation of the RANKL/OPG pathway. That could affect inflammation and vascular remodelling in the diabetic retina. This idea is speculative. No trial or publication tests it for severe nonproliferative diabetic retinopathy, and without the original mechanism data the link cannot be checked.

The very high TxGNN score (0.996) is the only support for this prediction. It should be treated as a hypothesis for further study, not as evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for severe nonproliferative diabetic retinopathy.

The model's second-ranked prediction, **diabetic retinopathy** (score 99.23%), has one loosely related trial:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00925600](https://clinicaltrials.gov/study/NCT00925600) | Phase 3 | Completed | 769 | Placebo-controlled study of new or worsening lens opacifications in men with non-metastatic prostate cancer receiving denosumab for bone loss. It is an ocular (lens) safety study with no efficacy evidence for retinopathy. |

---

## Literature Evidence

Currently no related literature available for severe nonproliferative diabetic retinopathy.

For the second-ranked prediction, **diabetic retinopathy**, only indirect literature was found:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38899553](https://pubmed.ncbi.nlm.nih.gov/38899553/) | 2024 | Observational / review (design unconfirmed) | Diabetes Obes Metab | Real-world cohort analysis with meta-analysis. It evaluated denosumab's effect on type 2 diabetes incidence and on long-term outcomes, including retinopathy, compared with bisphosphonates. |
| [36960265](https://pubmed.ncbi.nlm.nih.gov/36960265/) | 2023 | Cohort / risk assessment | Cureus | Fracture-risk (FRAX) assessment in adults with type 2 diabetes. It is not denosumab-specific and does not address retinopathy. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2560895 | OSENVELT | — | — |
| 2545764 | WYOST | — | — |
| 2343541 | PROLIA | — | — |
| 2545411 | JUBBONTI | — | — |
| 2368153 | XGEVA | — | — |

A sixth authorization exists (6 in total), but only five are listed in the data. Dosage form and indication text are not provided for any of them.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. No trials or publications address severe nonproliferative diabetic retinopathy, and the indirect evidence for diabetic retinopathy is weak. The only related trial is a lens-safety study. Mechanism and safety data are also missing, so this cannot move to safety screening.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) to test the proposed RANKL/OPG link to the diabetic retina
- Health Canada product monograph warnings and contraindications
- Preclinical or observational evidence of denosumab's effect on retinal disease
- Approved indication text for each Canadian licence

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

