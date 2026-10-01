---
layout: default
title: Hyaluronidase
parent: Model Prediction Only (L5)
nav_order: 449
evidence_level: L5
indication_count: 10
---

# Hyaluronidase
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

# Hyaluronidase: From an Unspecified Original Indication to Esotropia

## One-Sentence Summary

Hyaluronidase is an enzyme marketed in Canada as a component of HyQvia products. The dataset does not record its original approved indication.
The TxGNN model predicts it may be effective for **esotropia**, but **0 clinical trials** and **0 publications** currently support this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available data |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.89% (model rank 2789) |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Hyaluronidase is an enzyme that breaks down hyaluronan, and the dataset does not link that action to esotropia, a condition of eye misalignment.

The dataset identifies no plausible mechanism for this indication, and no original indication is recorded to compare against. The 99.89% score is a model output only. With no trials or publications, the prediction cannot be considered mechanistically supported.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2524368 | HYQVIA |
| 2524384 | HYQVIA |
| 2524392 | HYQVIA |
| 2524376 | HYQVIA |
| 2524406 | HYQVIA |

Dosage form and approved indication text are not available for these authorizations.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found. A 2024 review (PMID 37145319) notes that allergic reactions to hyaluronidase injection occur and are often misdiagnosed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The esotropia prediction has a high model score but no trials, no literature and no identifiable mechanism (Evidence Level L5). It should not be advanced on this basis.

**Other candidates:** The same Evidence Pack contains a better-supported prediction, **diabetic retinopathy**, which is worth evaluating instead. It has two completed Phase 3 trials of intravitreal ovine hyaluronidase for severe vitreous hemorrhage (NCT00198510, n=750; NCT00198497, n=510), one small Phase 2 trial, and reviews on enzymatic vitreolysis. Efficacy results are not in the dataset, and it should be treated as a research question rather than a confirmed use.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocks safety screening)
- Mechanism of action data (from DrugBank)
- Original approved indication, dosage forms and routes for the Canadian products
- Any clinical or mechanistic evidence linking hyaluronidase to esotropia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

