---
layout: default
title: Zinc Acetate
parent: Model Prediction Only (L5)
nav_order: 984
evidence_level: L5
indication_count: 10
---

# Zinc Acetate
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

# Zinc Acetate: From Topical Itch Relief to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Zinc acetate is marketed in Canada in topical itch and bug-bite relief products. The licence records do not list a formal indication, so this use is inferred from the product names.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, but **0 clinical trials** and **0 publications** currently support this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in licence records; products are marketed for itch and bug-bite relief (inferred from product names) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Zinc acetate is marketed in Canada in topical itch-relief products, and the licence records do not state an approved indication. A mechanistic link to diabetic retinopathy is therefore only theoretical.

The plausible rationale is zinc's role in antioxidant defence, as a cofactor of superoxide dismutase (SOD), and in retinal zinc homeostasis. Oxidative stress and inflammation are central to diabetic retinal damage, so this link is biologically reasonable. No trials or publications were retrieved to support it.

The marketed products are topical skin products. Retinopathy would likely need a different route of administration, and route compatibility has not yet been assessed. The model's score is high, but it reflects a graph-based association, not demonstrated efficacy.

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
| 2246156 | POLYSPORIN ITCH RELIEF |
| 2280868 | BENADRYL BUG BITE RELIEF |
| 2484838 | BENADRYL ITCH STOPPING CREAM |
| 2478072 | CHILDREN'S BENADRYL BUG BITE RELIEF |

Dosage form and approved indication text are not recorded in the source data for these licences.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The lead prediction is supported by model score alone (L5), with no clinical trials or literature. The marketed products are topical, so route compatibility with a retinal indication is also unresolved.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example, from DrugBank)
- A targeted literature and trial search for zinc and diabetic retinopathy
- Route-of-administration assessment (topical products versus a systemic or ocular need)
- Confirmation of the approved indications from the Health Canada licence records

**Other predictions:**
Bronchitis (rank 2, score 99.97%) has slightly more support at L4. It rests on one completed randomized trial of zinc acetate lozenges in the common cold (NCT03309995, n=87). That evidence is indirect and does not address bronchitis, so this prediction is also on Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

