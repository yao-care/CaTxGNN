---
layout: default
title: Sincalide
parent: Model Prediction Only (L5)
nav_order: 844
evidence_level: L5
indication_count: 10
---

# Sincalide
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

# Sincalide: From Gallbladder and Pancreatic Function Diagnosis to Malignant Catarrh

## One-Sentence Summary

Sincalide is a cholecystokinin (CCK) receptor agonist used as a diagnostic agent for gallbladder and pancreatic function.
The TxGNN model predicts it may be effective for **malignant catarrh**, a veterinary herpesvirus disease of cattle, but there are **0 clinical trials** and **0 publications** supporting this. The prediction is most likely a knowledge-graph artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license records. The Evidence Pack describes sincalide as a diagnostic CCK agonist for gallbladder and pancreatic function |
| Predicted New Indication | Malignant catarrh |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Sincalide is a CCK receptor agonist that acts on gallbladder contraction and bile release, and it is used diagnostically for gallbladder and pancreatic function.

No identifiable mechanistic link to malignant catarrh was found. Malignant catarrh is a herpesvirus disease of cattle, and no CCK-receptor pathway is known to be relevant to it. The prediction is therefore not considered biologically plausible.

The same score (99.96%) was assigned to infectious bovine rhinotracheitis, another bovine herpesvirus disease. This suggests both predictions come from the same graph neighborhood rather than from a real signal. The other top-ranked predictions are also unsupported:

- **Cytomegalovirus infection:** one retrieved paper covers basic CCK signaling in rat pancreatic cells and is unrelated to the virus.
- **Hyperthyroidism and related thyroid conditions:** retrieved papers show that thyroid status alters the response to CCK. They do not show that CCK-8 treats thyroid disease.
- **Thrombotic disease, homozygous familial hypercholesterolemia, Prinzmetal angina and amenorrhea:** no evidence was found.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for malignant catarrh.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2228602 | KINEVAC |
| 2494361 | SINCALIDE FOR INJECTION |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or publications for this indication, and no plausible mechanism links CCK receptor agonism to a bovine herpesvirus disease. The same pattern appears across all ten predictions, which have no clinical trial support and at most indirect preclinical evidence.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Mechanism of action data, for example from DrugBank
- Confirmation of whether veterinary disease terms such as malignant catarrh should be excluded from human drug repurposing predictions
- Review of the highest-scoring predictions with human relevance, such as cytomegalovirus infection and thyroid-related conditions, once direct evidence is available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

