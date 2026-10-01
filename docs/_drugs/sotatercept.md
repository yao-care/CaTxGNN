---
layout: default
title: Sotatercept
parent: Model Prediction Only (L5)
nav_order: 859
evidence_level: L5
indication_count: 10
---

# Sotatercept
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

# Sotatercept: Predicted Repurposing to Acute Lymphoblastic Leukemia (Original Indication Not Recorded)

## One-Sentence Summary

Sotatercept is marketed in Canada under the brand name WINREVAIR, but the Evidence Pack does not record its original indication.
The TxGNN model predicts it may be effective for **acute lymphoblastic leukemia**, but **no clinical trials and no publications** currently support this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Acute lymphoblastic leukemia |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. The analysis notes describe sotatercept as an activin signaling ligand trap (ActRIIA-Fc). It modulates TGF-beta superfamily signaling and erythropoiesis. No direct link to the biology of acute lymphoblastic leukemia has been established, and the high score may reflect proximity in the knowledge graph rather than disease-specific biology.

The other top-ranked predictions are also model output only, with no trials or literature:
- **Diabetic eye disease** (severe nonproliferative diabetic retinopathy, diabetic retinopathy, diabetic cataract): the three predictions overlap and are not independent evidence. Activin/TGF-beta signaling may play a role in retinal vascular remodeling, but this is a hypothesis. The vascular adverse effects of sotatercept (telangiectasia, bleeding) would need preclinical evaluation for the retina.
- **Urothelial carcinoma cluster** (transitional cell carcinoma and three rarer variants): the rationale is generic TGF-beta superfamily involvement in epithelial tumors.
- **HER2 positive breast carcinoma:** this pathway can be pro- or anti-tumorigenic, so the prediction is a safety concern as well as an evidence gap.
- **Drug-induced osteoporosis** (rank 4, flagged "Research Question"): this is the mechanistically most coherent prediction. Activin inhibition is biologically linked to increased bone formation. It has not been verified against supporting data, and a targeted literature review is the logical next step.

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
| 2551306 | WINREVAIR |
| 2551314 | WINREVAIR |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score (99.78%) but is evidence level L5, with no trials, no literature, and no established mechanistic link to acute lymphoblastic leukemia. Safety information is also missing, so the candidate cannot proceed to safety screening.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking gap)
- Drug mechanism of action and original approved indication, for example from DrugBank
- A targeted literature review, starting with drug-induced osteoporosis, the most mechanistically coherent prediction
- Preclinical evidence for any oncology or ocular indication, given the context-dependent role of TGF-beta signaling and the vascular adverse effects
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

