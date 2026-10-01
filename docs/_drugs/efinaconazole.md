---
layout: default
title: Efinaconazole
parent: Model Prediction Only (L5)
nav_order: 313
evidence_level: L5
indication_count: 10
---

# Efinaconazole
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

# Efinaconazole: From Onychomycosis to Astigmatism

## One-Sentence Summary

Efinaconazole is a topical triazole antifungal marketed in Canada as JUBLIA, used for onychomycosis (fungal nail infection).
The TxGNN model predicts it may be effective for **astigmatism**, but the score is a flat 50%, and there are **0 clinical trials** and **0 publications** supporting this direction.
This prediction is most likely a knowledge-graph artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Onychomycosis (the Canadian licence record has no indication text; this is taken from the published literature) |
| Predicted New Indication | Astigmatism |
| TxGNN Prediction Score | 50% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the record. The published literature describes efinaconazole as a topical triazole antifungal that inhibits sterol 14α-demethylase, an enzyme in fungal ergosterol synthesis. Its efficacy in onychomycosis is the basis of its approval.

This mechanism does not plausibly extend to astigmatism. Astigmatism is an optical refractive error caused by uneven curvature of the cornea or lens, and it has no known fungal or ergosterol-related component. The score of exactly 0.5 does not discriminate between candidates. It has no trials or literature behind it and should be treated as a model artifact rather than a real signal.

The other nine predictions for this drug share the same flat 0.5 score and also lack any evidence. Atopic dermatitis is the only one with a speculative link, through fungal colonisation of the skin. Even there, the two retrieved papers do not address it: one is an onychomycosis drug review and the other is a conference report. One entry, "tumor suppressor gene on chromosome 11", is a genetic locus label rather than a disease, so it is not a valid indication and should be excluded from review.

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
| 2413388 | JUBLIA |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5) with a non-discriminating score of 50%. It has no supporting trials or literature and no plausible mechanism, since a topical antifungal has no known target in refractive error.

**To proceed, the following is needed:**
- Health Canada package insert (warnings and contraindications) to complete the safety screening
- Confirmation of the approved indication text and dosage form for DIN 2413388
- Any mechanistic or clinical evidence linking efinaconazole to astigmatism; without it, no further investment is recommended
- Exclusion of non-disease entries (e.g., "tumor suppressor gene on chromosome 11") from downstream candidate review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

