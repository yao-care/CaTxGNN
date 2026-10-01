---
layout: default
title: Tranylcypromine
parent: Model Prediction Only (L5)
nav_order: 924
evidence_level: L5
indication_count: 10
---

# Tranylcypromine
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

# Tranylcypromine: From Depression to Benign Paroxysmal Torticollis of Infancy

## One-Sentence Summary

Tranylcypromine is a monoamine oxidase inhibitor (MAOI) antidepressant. The Canadian licence data in the pack do not list an indication, but the literature describes its use in major depressive disorder.
The TxGNN model predicts it may be effective for **benign paroxysmal torticollis of infancy**, but **0 clinical trials** and **0 publications** support this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Depression (not stated in the Canadian licence data; taken from the literature, which describes use in major depressive disorder) |
| Predicted New Indication | Benign paroxysmal torticollis of infancy |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The mechanistic link for this prediction is weak. Tranylcypromine irreversibly and non-selectively inhibits monoamine oxidase (MAO-A and MAO-B), which raises serotonin, norepinephrine and dopamine levels. This is the basis of its antidepressant effect. Detailed mechanism-of-action data were not available in the pack.

Benign paroxysmal torticollis of infancy is a self-limiting condition in young children. It is usually linked to channelopathy genes such as *CACNA1A*. MAO inhibition has no established relevance to this biology, and the high TxGNN score (0.997) reflects a graph-based association only. Tranylcypromine is also not suited to use in infants, which further weakens the case for repurposing.

Treat this prediction as a model output without mechanistic or clinical support.

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
| 1919598 | PARNATE |
| 2542188 | M-TRANYLCYPROMINE |

The pack gives no dosage form or approved indication text for either product.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical or literature evidence (L5), and the mechanistic link is not supported. The target condition is a self-limiting paediatric disorder, and tranylcypromine is not suited to infant use.

**To proceed, the following is needed:**
- Any preclinical or clinical data linking MAO inhibition to this condition
- Health Canada package insert warnings and contraindications, since safety screening cannot proceed without them
- Detailed mechanism-of-action data from DrugBank
- A paediatric safety assessment

**Note on other predictions for this drug:**
Other predicted indications have more support. Dysthymic disorder, agoraphobia and neurotic disorder are at L4 (Research Question). Melancholia (L3) and neurotic depression (L2) are at Proceed with Guardrails, but both overlap with tranylcypromine's existing depression use and are not true repurposing. These are better starting points for further evaluation.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

