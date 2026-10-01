---
layout: default
title: Tildrakizumab
parent: Model Prediction Only (L5)
nav_order: 907
evidence_level: L5
indication_count: 4
---

# Tildrakizumab
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

# Tildrakizumab: From Plaque Psoriasis to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Tildrakizumab is marketed in Canada as ILUMYA. The Canadian license records provided do not list its approved indication, but it is generally known as an anti-IL-23 antibody used for plaque psoriasis.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. This is a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the license data provided (generally known: plaque psoriasis) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the dataset. From general knowledge, tildrakizumab is a monoclonal antibody that blocks the p19 subunit of IL-23. Its efficacy in its original indication is established, and mechanistically it might be relevant to the new indication.

The hypothesized link is that IL-23/Th17-driven inflammation may contribute to inflammation of the retinal microvasculature in diabetic eye disease. This link is indirect. No trial or publication in the provided data supports it, and a high graph score alone is not clinical evidence. Systemic IL-23 blockade has no established ocular rationale, and ocular safety and the route of administration have not been examined.

TxGNN also ranked three other conditions for this drug, all with the same L5 evidence level and no trials or literature:

| Rank | Predicted Disease | TxGNN Score | Comment |
|------|------|------|------|
| 2 | Diabetic retinopathy | 99.53% | Same IL-23/IL-17 inflammation hypothesis as the top prediction |
| 3 | Diabetic cataract | 99.21% | No plausible direct mechanism; the score likely reflects network proximity to other diabetic complications |
| 4 | Drug-induced osteoporosis | 99.20% | Loose indirect rationale through IL-23/IL-17 effects on bone remodeling, but the direction of effect is unclear |

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
| 2558904 | ILUMYA |
| 2516098 | ILUMYA |

The dosage form, manufacturer and approved indication text are not available in the records provided.

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction records were found for tildrakizumab in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no literature and an indirect mechanistic hypothesis. Safety information for the Canadian product has not been reviewed, so the candidate cannot yet move past the initial screening stage.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank, to support a mechanistic-link analysis
- The approved indication text for the two Canadian DINs
- Preclinical or clinical evidence for IL-23 pathway involvement in diabetic retinal disease
- An assessment of route of administration and ocular safety for a systemic IL-23 blocker in this setting

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

