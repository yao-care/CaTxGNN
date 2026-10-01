---
layout: default
title: Metformin
parent: Model Prediction Only (L5)
nav_order: 590
evidence_level: L5
indication_count: 5
---

# Metformin
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

# Metformin: From Type 2 Diabetes to Focal Stiff Limb Syndrome

## One-Sentence Summary

Metformin is a widely marketed oral glucose-lowering drug. The Evidence Pack does not include its licensed indication text, so type 2 diabetes is stated from general knowledge.
The TxGNN model predicts it may be effective for **focal stiff limb syndrome**, but **no clinical trials and no publications** currently support this direction. The prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes (general knowledge; licence indication text not provided) |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, metformin is a long-established biguanide, and its efficacy in glucose control is well proven. Mechanistically, it may be applicable to focal stiff limb syndrome only through indirect routes.

Focal stiff limb syndrome is a focal variant of stiff person syndrome, a rare autoimmune-associated neurological disorder. One speculative link is metformin's AMPK-mediated anti-inflammatory and immunomodulatory effects. No neurological mechanism for metformin is established, and the provided data support no direct link.

The high score (0.994) is a model output only. Classic stiff person syndrome received an identical score (0.9945), which suggests the two share graph neighbours rather than having independent supporting evidence. Treat the score as a hypothesis-generating signal, not as validation.

**Other predictions in the pack (all L5, all Hold):**

| Predicted Indication | Score | Comment |
|------|------|------|
| Classic stiff person syndrome | 99.45% | Weak, indirect immunomodulation rationale |
| Opsismodysplasia | 99.40% | Possible PI3K/insulin pathway overlap via INPPL1; paediatric feasibility concerns |
| Thiamine-responsive dysfunction syndrome | 99.40% | Direction of effect uncertain; metformin and thiamine transport need safety review |
| Drug-induced localized lipodystrophy | 99.06% | Most biologically plausible (insulin-sparing effect), but unvalidated |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Five of the 20 authorizations are listed. Dosage form and approved indication text were not provided.

| DIN | Product Name |
|---------|------|
| 2514486 | METFORMIN TABLETS |
| 2385341 | METFORMIN FC |
| 2550512 | MAR-METFORMIN XR |
| 2558793 | METFORMIN ER |
| 2550504 | MAR-METFORMIN XR |

---

## Safety Considerations

Please refer to the package insert for safety information. No interaction records were found for this drug in the queried source.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no trials, no literature, and no established mechanism. The identical scores for the two stiff person syndrome entries point to shared graph structure rather than independent evidence.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data for metformin
- A systematic literature search on metformin in stiff person syndrome and related autoimmune neurological disorders
- Confirmation of the licensed indication text for the Canadian products
- Route and formulation compatibility assessment

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

