---
layout: default
title: Ocrelizumab
parent: Model Prediction Only (L5)
nav_order: 668
evidence_level: L5
indication_count: 10
---

# Ocrelizumab
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

# Ocrelizumab: From Multiple Sclerosis to HER2 Positive Breast Carcinoma

## One-Sentence Summary

Ocrelizumab is an anti-CD20 antibody that depletes B cells, and it is approved for multiple sclerosis.
The TxGNN model predicts it may be effective for **HER2 positive breast carcinoma**, but there are currently **0 clinical trials** and **0 relevant publications** supporting this direction. This is a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple sclerosis (the Canadian licence record contains no indication text) |
| Predicted New Indication | HER2 positive breast carcinoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, ocrelizumab is an anti-CD20 antibody that depletes B cells, and its efficacy in multiple sclerosis is established.

The link to the new indication is weak. HER2-positive breast cancer cells do not express CD20, and HER2 is not a target of this drug. The only conceivable connection is indirect and speculative, through B cells that infiltrate the tumour. The very high score (99.89%) reflects proximity in the knowledge graph, not clinical or literature support.

The other top predictions are also breast carcinoma subtypes (normal breast-like, progesterone-receptor positive, luminal A or B, progesterone-receptor negative) and several benign or rare tumours (tongue, hypopharynx, buccal mucosa, jugular foramen schwannoma, cervical neuroblastoma). None has a plausible CD20-dependent mechanism or any supporting trial or literature evidence. They appear to be knowledge-graph artifacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

The "luminal A or B" prediction (rank 4) returned 19 publications, but they are keyword false positives. The letter "B" matched B-cell biology, hepatitis B vaccines and HLA-B genetics. None concerns ocrelizumab or breast cancer, so they are not counted as evidence.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2467224 | OCREVUS |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the TxGNN model score. There is no clinical trial, no relevant literature, and no plausible mechanism, because the tumour cells do not express the drug's target (CD20). Risk-benefit cannot be assessed without safety data.

**To proceed, the following is needed:**
- Health Canada product monograph (warnings and contraindications), which is required before any safety screening
- Detailed mechanism of action data (MOA) from DrugBank
- Preclinical or clinical evidence on B-cell or CD20-related biology in breast cancer, including tumour-infiltrating B cells
- Approved indication text and dosage form details for the Canadian licence
- Route compatibility assessment for the proposed indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

