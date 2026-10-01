---
layout: default
title: Acetazolamide
parent: Model Prediction Only (L5)
nav_order: 18
evidence_level: L5
indication_count: 10
---

# Acetazolamide
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

# Acetazolamide: From a Carbonic Anhydrase Inhibitor to Exercise-Induced Malignant Hyperthermia

## One-Sentence Summary

Acetazolamide is a carbonic anhydrase inhibitor that is marketed in Canada, but the Evidence Pack does not record its approved indication.
The TxGNN model predicts it may be effective for **exercise-induced malignant hyperthermia**, with a very high score.
No clinical trials or publications currently support this specific prediction, so it rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Exercise-induced malignant hyperthermia |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Acetazolamide is known as a carbonic anhydrase inhibitor. Any link to exercise-induced malignant hyperthermia is therefore speculative.

One possible connection is that acetazolamide is used in muscle channelopathies such as periodic paralysis. Both conditions involve dysregulated muscle ion and pH handling.

The score of 99.95% (model rank 1,448) is not clinical evidence. It probably reflects proximity to other muscle disorders in the knowledge graph. The relationship to the original indication could not be assessed because no approved indication text was available.

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
| 2537893 | ACETAZOLAMIDE FOR INJECTION USP |
| 545015 | ACETAZOLAMIDE |
| 2358328 | ACETAZOLAMIDE FOR INJECTION, USP |

Two of the three products are injectable formulations.

---

## Safety Considerations

Please refer to the package insert for safety information.

Literature retrieved for other predicted indications (not for this one) reports these adverse events:
- Non-cardiogenic pulmonary edema after intravenous acetazolamide (case report)
- Acetazolamide-induced adynamic ileus (case report)

These are single case reports, so they show possible signals rather than established risk rates.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials, no literature and no established mechanism, so it stays at the model-only stage (L5, S0). The high score alone is not enough to justify moving forward.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which currently block safety screening
- Mechanism of action data (e.g., from DrugBank) to test the ion and pH handling hypothesis
- A targeted literature search for acetazolamide in exercise-induced malignant hyperthermia and related muscle ion-channel disorders
- Approved indication text for the three Canadian DINs, to define the original indication and route compatibility

**Other candidates from the same run:**
- Cardiomyopathy (rank 7) has the most supporting evidence of the ten predictions (L4).
  - It has three recruiting Phase 4 or NA trials in acute heart failure. These involve acetazolamide or diuretic strategies, and none has reported results.
  - The link to cardiomyopathy is indirect.
  - It is worth considering as a research question rather than a clinical recommendation.
- Intestinal obstruction (rank 8) and myopathic intestinal pseudoobstruction (rank 10) have literature suggesting possible harm from acetazolamide, so they should not be prioritized.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

