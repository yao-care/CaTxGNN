---
layout: default
title: Ibuprofen
parent: Model Prediction Only (L5)
nav_order: 458
evidence_level: L5
indication_count: 7
---

# Ibuprofen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Ibuprofen: From Pain and Inflammation (NSAID) to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ibuprofen is a widely marketed non-steroidal anti-inflammatory drug (NSAID), generally used for pain and inflammation.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare skeletal disorder.
Currently there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the license data (general NSAID use: pain and inflammation) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for ibuprofen is not available in the input. Ibuprofen is known as a non-selective COX inhibitor, and its use in pain and inflammation is well established. Based on the data provided, however, no supported mechanistic link to the predicted disease could be identified.

Acromesomelic dysplasia, Hunter-Thompson type is a rare skeletal dysplasia. It has been reported as linked to loss-of-function of CDMP1/GDF5, a growth factor in the BMP pathway. Ibuprofen has no known action on this pathway. The very high TxGNN score (0.997, model rank 5,670) is a graph-based association only. It is not independent pharmacological evidence.

The other top-ranked predictions show the same pattern. They are mostly rare skeletal or developmental disorders (brachyolmia, pseudoachondroplasia, brachydactyly-syndactyly syndrome and others), and none has supporting trials or literature.

- **Pseudoachondroplasia:** A theoretical anti-inflammatory rationale exists, because COMP mutations cause chondrocyte stress and inflammatory signaling. Any use would be standard symptomatic care for joint pain, not a repurposing signal.
- **Myosclerosis:** The link is weak and speculative. An NSAID might relieve symptoms, but there is no evidence of disease modification.
- **Developmental syndromes:** NSAID use in a developmental context also raises safety questions that would need separate evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Ibuprofen has 20 authorizations in Canada. Dosage form and approved indication text are not available in the supplied data. Five main products are listed below.

| DIN | Product Name |
|---------|------|
| 2242632 | MOTRIN 300MG |
| 2376598 | IBUPROFEN LIQUID GEL CAPSULES |
| 441643 | APO-IBUPROFEN |
| 2248231 | ADVIL EXTRA STRENGTH LIQUI-GELS |
| 2374226 | MUSCLE & JOINT |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no clinical trials, no literature and no plausible COX-inhibition-dependent mechanism for this rare skeletal dysplasia. Ibuprofen's original mechanism and safety data are also missing, so the evaluation cannot progress to safety screening.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking gap for safety screening)
- Detailed mechanism of action data (for example, from DrugBank)
- Any preclinical or clinical evidence linking ibuprofen to GDF5/BMP-pathway or skeletal dysplasia biology
- Confirmation of the approved indications and dosage forms for the Canadian DINs
- A separate safety assessment of NSAID use in developmental or paediatric rare-disease populations

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

