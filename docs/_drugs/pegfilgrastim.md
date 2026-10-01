---
layout: default
title: Pegfilgrastim
parent: Model Prediction Only (L5)
nav_order: 707
evidence_level: L5
indication_count: 2
---

# Pegfilgrastim
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

# Pegfilgrastim: From an Unrecorded Original Indication to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Pegfilgrastim is a long-acting G-CSF analog marketed in Canada, but the Evidence Pack records no original indication for it.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**.
Currently, **0 clinical trials** and **0 publications** support this direction, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the provided data |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

A second, broader prediction is **diabetic retinopathy** (score 99.73%, also L5, also Hold). The two predictions overlap, so they should not be counted as independent evidence.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and no original indication is recorded. Pegfilgrastim is a long-acting G-CSF analog, but the supplied data cannot confirm a mechanistic link to diabetic retinopathy. The link rests on the TxGNN score (0.999) alone, and the score is a model output, not clinical evidence.

Two opposing hypotheses are plausible, and neither is supported by the supplied trials or literature:
- **Possible benefit:** G-CSF mobilizes bone-marrow-derived progenitor cells, which might support repair of damaged retinal microvasculature.
- **Possible harm:** G-CSF-driven neutrophil expansion and activation could worsen retinal inflammation and capillary leukostasis.

Until the mechanism is clarified and independent evidence is found, this prediction remains an unverified hypothesis.

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
| 2529343 | LAPELGA |
| 2249790 | NEULASTA |
| 2484153 | FULPHILA |
| 2497395 | ZIEXTENZO |
| 2474565 | LAPELGA |

Dosage form and approved indication text are not available for these authorizations. Five of the eight authorizations are listed.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no supporting trials or literature, so it sits at evidence level L5. The mechanism could plausibly help or harm the retina, and the Health Canada safety data needed for screening are missing.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action and original indication data (for example, from DrugBank)
- A targeted literature and trial search for G-CSF or pegfilgrastim in diabetic retinopathy, including any evidence of retinal harm
- Preclinical or mechanistic evidence to decide between the benefit and harm hypotheses
- Assessment of route compatibility (systemic G-CSF versus ocular delivery), which is still pending

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

