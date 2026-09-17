---
layout: default
title: Lapatinib
parent: Model Prediction Only (L5)
nav_order: 444
evidence_level: L5
indication_count: 1
---

# Lapatinib
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

# Lapatinib: From HER2+ Breast Cancer to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

Lapatinib is a dual EGFR/HER2 tyrosine kinase inhibitor originally used for HER2-positive breast cancer. The TxGNN model predicts it may be effective for **Dermatofibrosarcoma Protuberans (DFSP)**, but currently **no clinical trials** and **no published literature** support this specific pairing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2+ Breast Cancer (noted in evidence rationale; formal MOA/indication fields are a data gap) |
| Predicted New Indication | Dermatofibrosarcoma Protuberans |
| TxGNN Prediction Score | 99.30% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (data gap). Based on the information that is available, Lapatinib is known as a dual EGFR/HER2 tyrosine kinase inhibitor, and its efficacy in HER2-positive breast cancer is well established.

DFSP, however, is driven by a distinct mechanism: the COL1A1-PDGFB fusion gene causes PDGFB overexpression, which activates PDGFR-β signaling. The clinically validated targeted therapy for DFSP is imatinib, a PDGFR inhibitor — not an EGFR/HER2 inhibitor. Lapatinib does not directly inhibit PDGFR-β, so its known pharmacology does not overlap meaningfully with the established driver mechanism of DFSP.

The high TxGNN score (99.30%) most likely reflects the knowledge graph's broad clustering of tyrosine kinase inhibitors as a drug class, rather than target-specific mechanistic evidence linking lapatinib to DFSP. Combined with the complete absence of clinical trials or literature, and the drug currently having no marketing authorization in Canada, the mechanistic case for this prediction is weak.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Canada Market Information

Lapatinib currently has no marketing authorization (DIN) in Canada (market status: not marketed), so no license records are available to summarize.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (dual EGFR/HER2 tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN model score (Evidence Level L5), with zero clinical trials or literature, a mechanistic pathway (EGFR/HER2) that does not clearly overlap with the established DFSP driver (PDGFR-β), and no current Canadian market authorization for the drug.

**To proceed, the following is needed:**
- TFDA/Health Canada label warnings and contraindications (currently a Blocking data gap, DG001)
- Confirmed mechanism of action data for lapatinib (High-priority data gap, DG002)
- Preclinical or case-level evidence specifically linking EGFR/HER2 inhibition to DFSP biology
- Ongoing monitoring for new clinical trials or publications on this drug-disease pair
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

