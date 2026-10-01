---
layout: default
title: Brodalumab
parent: Model Prediction Only (L5)
nav_order: 124
evidence_level: L5
indication_count: 10
---

# Brodalumab
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

# Brodalumab: From Plaque Psoriasis to Strongyloidiasis

## One-Sentence Summary

Brodalumab (Canadian brand SILIQ) is an IL-17 receptor A (IL-17RA) antagonist, originally used for immune-mediated skin disease (plaque psoriasis).
The TxGNN model predicts it may be effective for **strongyloidiasis**, a parasitic worm infection, with a high score of 99.84%.
However, there are **0 clinical trials** and **0 publications** supporting this prediction, so it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Plaque psoriasis (general drug knowledge; the Canadian licence record contains no indication text) |
| Predicted New Indication | Strongyloidiasis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, brodalumab blocks the IL-17 receptor A, which dampens IL-17-driven inflammation in immune-mediated diseases.

On the available data, this prediction is **not mechanistically convincing**. Strongyloidiasis is an infection, and IL-17 signalling helps defend barrier sites such as skin and gut. Blocking IL-17RA is therefore more likely to raise infection risk than to treat an infection. The high TxGNN score most likely reflects knowledge-graph patterns rather than a real therapeutic link.

No similarity analysis between the original and predicted indications has been completed. No route-of-administration compatibility analysis has been completed either.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2473623 | SILIQ |

Dosage form and approved indication text are not recorded in the licence data.

## Safety Considerations

- **Drug Interactions**: The interaction query returned no records (0 found). This is not evidence that there are no interactions.
- **Boxed warning noted in the Evidence Pack**: Suicidal ideation and behaviour. This would need particular attention in any new patient population.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials or literature behind it, and the IL-17 host-defence role points toward increased rather than decreased infection risk. The Evidence Pack supports no plausible therapeutic rationale for strongyloidiasis.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence linking IL-17RA blockade to strongyloidiasis; without it, further investment is not justified

**Note:** Among the other predictions, "eye disease" (rank 2) has slightly more supporting material, though only an unrelated observational trial and one review. The term is too broad to define an indication. Narrower IL-17-related ocular inflammation such as uveitis or scleritis may be a more useful research question.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

