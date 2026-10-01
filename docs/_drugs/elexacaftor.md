---
layout: default
title: Elexacaftor
parent: Model Prediction Only (L5)
nav_order: 318
evidence_level: L5
indication_count: 10
---

# Elexacaftor
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

# Elexacaftor: From Cystic Fibrosis to Rheumatoid Arthritis

## One-Sentence Summary

Elexacaftor is a CFTR corrector used in the triple combination TRIKAFTA for cystic fibrosis. The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but this rests on **1 loosely related, non-interventional trial** and **0 publications**. The prediction is essentially model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cystic fibrosis (inferred from the drug class and trial context; the licence records list no indication text) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 98.11% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Elexacaftor is known to be a CFTR corrector: it helps misfolded CFTR protein reach the cell surface. It is marketed as part of the TRIKAFTA combination.

No credible link to rheumatoid arthritis has been identified. The high graph score (0.981) is a prediction only, and the score alone is not evidence. Rheumatoid arthritis is an autoimmune joint disease, and nothing in the retrieved data connects CFTR correction to it. The only linked trial studies neutrophil function in cystic fibrosis patients, not in rheumatoid arthritis. A neutrophil-related hypothesis is conceivable, but nothing here supports it.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04970225](https://clinicaltrials.gov/study/NCT04970225) | N/A | Completed | 47 | Observational study of blood neutrophil function and phenotype in cystic fibrosis. It looked at the effects of chronic *Pseudomonas aeruginosa* infection, CFTR modulator treatment and acute exacerbation. It enrolled no rheumatoid arthritis patients and did not test elexacaftor for this indication. |

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2542285 | TRIKAFTA |
| 2526670 | TRIKAFTA |
| 2542277 | TRIKAFTA |
| 2517140 | TRIKAFTA |

Dosage form and approved indication text are not included in the licence records.

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. The one linked trial is a non-interventional study in cystic fibrosis and does not address rheumatoid arthritis. There is no literature and no plausible mechanistic link. The other nine predictions for this drug (ALS, leprosy, pulmonary hypertension and others) are also at L4–L5 and on Hold. For pulmonary hypertension, the only evidence is indirect, from CF studies.

**To proceed, the following is needed:**
- Health Canada product monograph warnings and contraindications, which currently block safety screening
- Mechanism of action data and a plausible pathway linking CFTR correction to rheumatoid arthritis
- Preclinical or in vitro evidence in an arthritis model
- Any interventional study of elexacaftor-containing therapy in rheumatoid arthritis patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

