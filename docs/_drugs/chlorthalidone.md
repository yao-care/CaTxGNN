---
layout: default
title: Chlorthalidone
parent: Model Prediction Only (L5)
nav_order: 185
evidence_level: L5
indication_count: 10
---

# Chlorthalidone
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

# Chlorthalidone: From Hypertension (Thiazide-like Diuretic Use) to Primary Hereditary Glaucoma

## One-Sentence Summary

Chlorthalidone is a marketed thiazide-like diuretic, generally used for hypertension and fluid retention (the dataset lists no approved indication text).
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**, with a very high score of 99.92%.
However, **0 clinical trials** and **0 publications** support this prediction, so it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the dataset (general use: hypertension / edema) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, chlorthalidone is a thiazide-like diuretic. Its efficacy in lowering blood pressure through natriuresis and volume reduction is established. Mechanistically, it has no clear route to primary hereditary glaucoma.

One speculative link is carbonic anhydrase inhibition, which could reduce aqueous humor production and so lower intraocular pressure. No clinical data in this pack support this idea. Primary hereditary glaucoma is largely a structural or developmental disease of the eye's drainage system, so a systemic diuretic is unlikely to be relevant. A very high TxGNN score alone is not enough to justify further investment here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2523809 | JAMP CHLORTHALIDONE |
| 360279 | APO-CHLORTHALIDONE |
| 2523817 | JAMP CHLORTHALIDONE |
| 2523795 | JAMP CHLORTHALIDONE |
| 2248763 | AA-ATENIDONE |

Showing 5 of 8 authorizations. Dosage form and approved indication text are not available in the dataset.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the model score. There are no trials or publications, the mechanistic link is speculative, and the disease is structural, so a systemic diuretic is an unlikely fit. Established IOP-lowering agents already exist.

**Other predictions in the pack (for context):**
- All ten predicted indications remain at Hold or "Research Question".
- The strongest is **chronic pulmonary heart disease** (score 99.82%, L3). Its only direct evidence is a 1967 clinical report of chlorthalidone in congestive heart failure due to chronic cor pulmonale. Use would be symptomatic decongestion only.
- Hypertension-related predictions (malignant hypertensive renal disease, malignant renovascular hypertension) are plausible in principle but have no supporting evidence. They are typically emergencies managed with parenteral therapy.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (this blocks safety screening)
- Mechanism of action data from DrugBank
- Approved indication text for the Canadian licenses
- Any preclinical or clinical evidence linking chlorthalidone to glaucoma, such as IOP effects
- Confirmation of the design and findings of the 1967 cor pulmonale report, if that indication is pursued

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

