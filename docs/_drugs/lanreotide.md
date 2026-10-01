---
layout: default
title: Lanreotide
parent: Model Prediction Only (L5)
nav_order: 518
evidence_level: L5
indication_count: 5
---

# Lanreotide
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

# Lanreotide: From Somatostatin Analog Therapy to Hypertrichosis

## One-Sentence Summary

Lanreotide is a somatostatin analog that is marketed in Canada (Somatuline Autogel, Mytolac). The TxGNN model predicts it may be effective for **hypertrichosis**, but this rests on a model score alone: **0 clinical trials** and **0 publications** currently support it.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the input. Lanreotide is a somatostatin analog that suppresses growth hormone (GH) and IGF-1. Hypertrichosis appears in some GH-excess states, so an indirect link is conceivable.

This link is speculative. The score of about 0.9997 is a model output, not clinical evidence. The input documents no direct biological rationale for using lanreotide against hypertrichosis.

Four other predictions have the same problem, and all are also L5 with no clinical trials:

- Malformation syndrome with an odontal/periodontal component. Its 20 retrieved publications are general periodontitis papers that do not mention lanreotide or somatostatin analogs, so the match looks like a keyword artifact.
- Syndrome with a Dandy-Walker malformation as a major feature.
- Isolated genetic hair shaft abnormality.
- Ambras type hypertrichosis universalis congenita. This is an ultra-rare congenital disorder, and the prediction likely reflects graph similarity to other hypertrichosis nodes.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Dosage form and approved indication text are not recorded for these licenses. Five of the six licenses are listed below.

| DIN | Product Name |
|---------|------|
| 2555867 | MYTOLAC |
| 2555883 | MYTOLAC |
| 2283395 | SOMATULINE AUTOGEL |
| 2283409 | SOMATULINE AUTOGEL |
| 2283417 | SOMATULINE AUTOGEL |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction relies solely on a model score. There are no trials or literature for hypertrichosis, and the mechanistic link is speculative. The other four predicted indications are also L5.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank), to assess whether GH/IGF-1 suppression plausibly affects hypertrichosis
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Approved indication and dosage form details for the Canadian licenses
- Targeted literature and trial searches for lanreotide or somatostatin analogs in hypertrichosis, to see whether any real evidence exists
- Route of administration compatibility, which is still pending

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

