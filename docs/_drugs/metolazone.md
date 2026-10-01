---
layout: default
title: Metolazone
parent: Model Prediction Only (L5)
nav_order: 603
evidence_level: L5
indication_count: 5
---

# Metolazone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Metolazone: From Diuretic Therapy to Malignant Renovascular Hypertension

## One-Sentence Summary

Metolazone is a thiazide-like diuretic marketed in Canada as ZAROXOLYN, though its approved indication text is not recorded in the available data.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, but **no clinical trials and no relevant publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the available licence data |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Based on general pharmacology, metolazone is a thiazide-like diuretic that inhibits the Na-Cl cotransporter in the distal convoluted tubule. This produces sodium and water loss and lowers blood pressure, so a link to hypertensive disease is plausible.

The fit for this specific indication is weak. Renovascular hypertension is driven mainly by renin-angiotensin system activation. Malignant hypertension is an emergency that is usually managed with parenteral agents, not an oral diuretic. The high score (99.84%) is a graph-based prediction and should not be read as evidence of efficacy.

The second-ranked prediction, malignant hypertensive renal disease, has an identical score, so the two predictions are probably not independent. Volume reduction could plausibly help renal haemodynamics, and metolazone is used in practice for diuretic-resistant oedema with reduced renal function. Thiazide efficacy falls at low GFR, though metolazone is a relative exception. This remains inference only.

The remaining predictions are pulmonary hypertension (two entries) and Braddock syndrome. For pulmonary hypertension, a diuretic may relieve right-heart congestion as symptomatic support but has no known effect on pulmonary vascular remodelling. For Braddock syndrome, no mechanistic link to metolazone is established. The score there likely reflects network proximity through hypertension-related nodes. All three are marked Hold.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

Note: the literature retrieved for the pulmonary hypertension (lung disease/hypoxia) prediction consists of general hypoxia-biology papers on neurodegeneration, cancer, keloid and multiple sclerosis. None mention metolazone or pulmonary hypertension treatment, so they were not counted as supporting evidence.

## Canada Market Information

| Licence Number | Product Name |
|---------|------|
| 888400 | ZAROXOLYN |

Dosage form, manufacturer and approved indication text are not recorded for this licence.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a model score (L5). There are no trials or relevant publications, and the mechanistic rationale is weak for a condition driven by renin-angiotensin activation and typically treated with parenteral agents.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- The original approved indication text for the ZAROXOLYN licence
- Targeted literature searches on metolazone in renovascular or malignant hypertension and hypertensive renal disease
- Route compatibility assessment (oral diuretic vs. the parenteral therapy usually needed in malignant hypertension)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

