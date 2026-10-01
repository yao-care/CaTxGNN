---
layout: default
title: Carbetocin
parent: Model Prediction Only (L5)
nav_order: 155
evidence_level: L5
indication_count: 2
---

# Carbetocin
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

# Carbetocin: From Postpartum Hemorrhage to Isotretinoin-like Syndrome

## One-Sentence Summary

Carbetocin is a long-acting oxytocin receptor agonist used as a uterotonic to prevent or treat postpartum hemorrhage.
The TxGNN model predicts it may be effective for **isotretinoin-like syndrome**, but there are **0 clinical trials** and **0 publications** supporting this, so the prediction is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Postpartum hemorrhage (uterotonic use; the Canadian licence records list no indication text) |
| Predicted New Indication | Isotretinoin-like syndrome |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Carbetocin is a synthetic, long-acting analogue of oxytocin. It acts as an oxytocin receptor agonist and causes uterine contraction, which is why it is used in postpartum hemorrhage.

The predicted condition, isotretinoin-like syndrome, is a congenital malformation phenotype linked to disruption of the retinoid pathway. A peptide uterotonic has no evident plausible action on this pathway or on the developmental processes involved. No mechanistic link has been established between the original and predicted indications.

The high TxGNN score (99.15%) reflects graph-based association only and is likely a knowledge-graph artifact. A second prediction, Goodman syndrome (score 99.06%), has the same problem. It is a rare congenital craniofacial and limb malformation disorder that is developmental and genetic in nature, with no supporting trials or literature. Neither prediction should be treated as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2489244 | CARBETOCIN INJECTION |
| 2496526 | DURATOCIN |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no literature, and no plausible mechanism linking an oxytocin receptor agonist to a congenital retinoid-pathway malformation phenotype. The evidence level is L5, so there is no basis to advance.

**To proceed, the following is needed:**
- A documented mechanistic hypothesis linking oxytocin receptor agonism to isotretinoin-like syndrome
- Mechanism of action data from DrugBank
- Preclinical or clinical evidence for the predicted indication
- Health Canada package insert warnings and contraindications
- Approved indication text and dosage forms for the two Canadian licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

