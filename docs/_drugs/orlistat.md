---
layout: default
title: Orlistat
parent: Model Prediction Only (L5)
nav_order: 681
evidence_level: L5
indication_count: 1
---

# Orlistat
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Orlistat: From Obesity Management to Hypervitaminosis

## One-Sentence Summary

Orlistat is a lipase inhibitor that reduces dietary fat absorption. It is marketed in Canada as XENICAL, and the pack does not record its approved indication. The TxGNN model predicts it may be effective for **hypervitaminosis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Evidence Pack (orlistat is generally known as an anti-obesity agent) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for orlistat is not available in the Evidence Pack. The available pharmacology is limited to this: orlistat inhibits gastric and pancreatic lipases and reduces dietary fat absorption by roughly 30%. The same effect lowers absorption of the fat-soluble vitamins (A, D, E and K), and vitamin deficiency is a labeled adverse effect.

This gives a possible, but indirect, link to hypervitaminosis. In theory, reduced fat absorption could limit intake-driven excess of fat-soluble vitamins such as A or D. It would not apply to water-soluble vitamins. No mechanistic or clinical data in the Evidence Pack support this idea.

The original indications are also empty in the input. The high TxGNN score (0.994) therefore cannot be cross-checked against known pharmacology and should be read as a model prediction only. A reduction in vitamin absorption that is a safety concern in routine use is the very property this prediction would rely on, which makes the rationale speculative.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2240325 | XENICAL | — | — |

---

## Safety Considerations

Please refer to the package insert for safety information.

The pack lists no recorded drug interactions. Its only safety-related pharmacology note is that orlistat lowers absorption of fat-soluble vitamins (A, D, E, K), and vitamin deficiency is a labeled adverse effect.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a model prediction (Evidence Level L5), with no registered trials and no literature. The proposed mechanism is indirect and speculative, and the pack lacks both the original indication and the mechanism-of-action data needed to validate the score.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (download and parse the PDF). This blocks safety screening.
- Mechanism of action and original indication data from DrugBank (DB01083).
- A targeted literature and trial search on orlistat and fat-soluble vitamin excess.
- Evidence that any benefit outweighs the known risk of vitamin deficiency.
- Approved indication text and dosage form for the XENICAL DIN.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

