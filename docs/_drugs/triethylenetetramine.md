---
layout: default
title: Triethylenetetramine
parent: Model Prediction Only (L5)
nav_order: 937
evidence_level: L5
indication_count: 10
---

# Triethylenetetramine
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

# Triethylenetetramine: From Copper Chelation to Anaplastic Thyroid Carcinoma

## One-Sentence Summary

Triethylenetetramine (trientine) is generally known as a copper-chelating drug. The supplied data does not state its approved indication.
The TxGNN model predicts it may be effective for **thyroid gland undifferentiated (anaplastic) carcinoma**, but **0 clinical trials** and **0 publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied data (general pharmacology: copper overload, e.g. Wilson's disease) |
| Predicted New Indication | Thyroid gland undifferentiated (anaplastic) carcinoma |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, trientine is a copper chelator, its role in copper-overload disease is well established, and mechanistically it may be applicable to some copper-dependent processes. Copper-dependent signaling and angiogenesis have been proposed as targets in some cancers, but the link to anaplastic thyroid carcinoma is speculative. The TxGNN score reflects knowledge-graph proximity, not clinical evidence.

The other top predictions fall into two groups:

- **Idiopathic copper-associated cirrhosis (rank 6)** is the most biologically coherent prediction. Hepatic copper accumulation is its defining feature, which fits copper chelation. It is flagged as a **Research Question**, but no trials or literature were supplied.
- **Other liver and vascular entities and rare renal cell carcinoma subtypes** (hepatopulmonary syndrome, portal hypertension-related conditions, hepatic porphyria and others) have no clear mechanistic rationale. Several share exactly the same score (0.9977 or 0.9878), which suggests a shared graph-neighborhood artifact rather than a disease-specific signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2515067 | WAYMADE-TRIENTINE |
| 2504855 | MAR-TRIENTINE |

Dosage form, manufacturer, and approved indication text were not provided for either authorization.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no supporting trials or literature (L5), and the mechanistic link to anaplastic thyroid carcinoma is speculative. Safety information and mechanism data are also missing, so the candidate cannot move past initial screening.

**To proceed, the following is needed:**
- Health Canada product monograph (warnings, contraindications, approved indication) for the two DINs. This blocks safety screening.
- Mechanism of action data, for example from DrugBank
- A targeted literature and trial search on trientine or copper chelation in anaplastic thyroid carcinoma
- Consider prioritizing idiopathic copper-associated cirrhosis for a focused evidence review, since it has the strongest mechanistic rationale

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

