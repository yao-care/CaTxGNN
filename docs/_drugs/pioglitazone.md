---
layout: default
title: Pioglitazone
parent: Model Prediction Only (L5)
nav_order: 732
evidence_level: L5
indication_count: 9
---

# Pioglitazone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Pioglitazone: From Type 2 Diabetes to Opsismodysplasia

## One-Sentence Summary

Pioglitazone is a PPAR-gamma agonist (insulin sensitizer) used for type 2 diabetes. The license records do not state this indication, so it is inferred from the retrieved literature.
The TxGNN model predicts it may be effective for **opsismodysplasia**, a rare skeletal dysplasia, with a very high score.
However, **0 clinical trials** and **0 publications** support this prediction, so it is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (inferred from literature; not stated in the license records) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 13 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Based on known information, pioglitazone is a thiazolidinedione that activates PPAR-gamma, and its efficacy in improving insulin sensitivity in type 2 diabetes is well documented.

Opsismodysplasia is a rare skeletal dysplasia linked to INPPL1, a gene involved in phosphoinositide signaling and growth plate development. No clear mechanistic link to PPAR-gamma agonism or insulin sensitization has been identified. The high TxGNN score is a graph-based association with no supporting trials or literature, so it should be treated as a hypothesis only.

Other predictions for this drug have a more plausible biological rationale. These are the localized lipodystrophies (drug-induced, centrifugal, pressure-induced and idiopathic), since PPAR-gamma regulates fat cell differentiation. They are flagged as research questions, but they also have no supporting clinical evidence in the retrieved data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

Only the pancreatic agenesis prediction (rank 9) returned articles. These are 9 general reviews and one RCT on type 2 diabetes, insulin resistance and PPAR agonists, and none address opsismodysplasia.

---

## Canada Market Information

Showing 5 of 13 authorizations.

| DIN | Product Name |
|---------|------|
| 2326485 | MINT-PIOGLITAZONE |
| 2326477 | MINT-PIOGLITAZONE |
| 2365529 | JAMP PIOGLITAZONE |
| 2339595 | ACH-PIOGLITAZONE |
| 2339587 | ACH-PIOGLITAZONE |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score (L5), with no trials, no literature and no plausible mechanism linking PPAR-gamma agonism to opsismodysplasia. The drug is widely marketed in Canada, but that does not support this new use.

**To proceed, the following is needed:**
- Mechanism of action data for pioglitazone
- Health Canada product monograph warnings and contraindications, to allow a safety screen
- A targeted literature review on opsismodysplasia and INPPL1/phosphoinositide signaling in relation to PPAR-gamma
- Consideration of the localized lipodystrophy candidates as a better-grounded research direction, taking into account pioglitazone's weight gain and fluid retention effects
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

