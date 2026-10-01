---
layout: default
title: Aflibercept
parent: Model Prediction Only (L5)
nav_order: 28
evidence_level: L5
indication_count: 10
---

# Aflibercept
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

# Aflibercept: From Retinal Neovascular and Edematous Disease to Esotropia

## One-Sentence Summary

Aflibercept is a VEGF-A/VEGF-B/PlGF trap, marketed in Canada for retinal neovascular and edematous disease (the licence records themselves list no indication text).
The TxGNN model predicts it may be effective for **esotropia**, but there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction is model-only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Retinal neovascular and edematous disease (from the prediction rationale; not stated in the Canadian licence records) |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on known information, aflibercept is a recombinant fusion protein that traps VEGF-A, VEGF-B and placental growth factor (PlGF). This reduces abnormal vessel growth and vascular leakage in the retina, and its efficacy in retinal neovascular and edematous disease is established.

The link to esotropia is weak. Esotropia is an ocular motility and alignment disorder (an inward-turning eye). It is not driven by VEGF-mediated neovascularization or edema. The high score (0.994) most likely reflects "ophthalmic proximity" in the knowledge graph rather than a shared mechanism.

Because the original indication and mechanism data are missing from the record, the prediction cannot be cross-checked, and no mechanistic similarity has been established.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Ten authorizations are on record. The main ones are listed below. Dosage form and approved-indication text are not populated in the source data.

| DIN | Product Name |
|---------|------|
| 2558238 | YESAFILI |
| 2554178 | AFLIVU |
| 2415992 | EYLEA |
| 2535858 | YESAFILI |
| 2505355 | EYLEA |

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried records.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a graph score alone, with no trials or literature, and no VEGF-driven mechanism links aflibercept to esotropia. Other candidates in the same list, such as esophageal varices and rare tumours, are at most research questions and also have no clinical evidence.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action and original indication data, for example from DrugBank
- Preclinical or mechanistic evidence for VEGF/PlGF involvement in esotropia
- A literature and trial search for aflibercept in strabismus or ocular motility disorders

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

