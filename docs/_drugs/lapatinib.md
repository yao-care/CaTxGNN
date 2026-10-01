---
layout: default
title: Lapatinib
parent: Model Prediction Only (L5)
nav_order: 520
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

# Lapatinib: From an Unrecorded Original Indication to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

Lapatinib is a dual EGFR/HER2 tyrosine kinase inhibitor marketed in Canada as TYKERB, but no original indication is recorded in the supplied data.
The TxGNN model predicts it may be effective for **dermatofibrosarcoma protuberans (DFSP)**.
This prediction has **0 clinical trials** and **0 publications** behind it, so it rests on a computational score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the supplied data |
| Predicted New Indication | Dermatofibrosarcoma protuberans |
| TxGNN Prediction Score | 99.30% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the curated record. Lapatinib is known to inhibit both EGFR and HER2 tyrosine kinases, but the record has no original indications to check against.

The biological link to DFSP is weak. DFSP is driven mainly by the COL1A1-PDGFB fusion, which activates PDGFRB signaling, and its established targeted therapy is a PDGFR-directed inhibitor (imatinib). The supplied data documents no reason to think DFSP depends on EGFR or HER2.

The high score (0.993) is a computational output from the knowledge graph, not clinical evidence. The relationship remains speculative until someone shows that EGFR/HER2 expression or pathway activity is relevant in DFSP tissue.

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
| 2326442 | TYKERB |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found for this drug in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications (Evidence Level L5). The mechanistic link is also doubtful, because DFSP is a PDGFRB-driven tumour with an established PDGFR-directed therapy and no documented EGFR/HER2 dependence.

**To proceed, the following is needed:**
- The Health Canada package insert (warnings and contraindications), which is a blocking gap for safety screening
- Curated original indications and mechanism of action from DrugBank
- Independent biological validation, such as EGFR/HER2 expression or pathway activity in DFSP tissue
- Preclinical or clinical evidence for lapatinib in DFSP, including a comparison against imatinib
- Assessment of route compatibility and similarity to the original indication (both currently pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

