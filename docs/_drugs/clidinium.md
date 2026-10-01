---
layout: default
title: Clidinium
parent: Model Prediction Only (L5)
nav_order: 203
evidence_level: L5
indication_count: 10
---

# Clidinium
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

# Clidinium: From Antimuscarinic Antispasmodic (Indication Not Recorded) to Cauda Equina Syndrome

## One-Sentence Summary

Clidinium is a peripherally acting antimuscarinic (anticholinergic) drug, marketed in Canada as LIBRAX, but its original approved indication is not recorded in the data provided.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**, but **no clinical trials and no publications** support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the data provided |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Clidinium is understood to be a peripherally acting muscarinic antagonist, but the mechanism field could not be confirmed.

The link to cauda equina syndrome is weak. This condition is a compressive neurological emergency that needs surgical decompression. An antimuscarinic could at most relieve bladder symptoms and would not treat the underlying compression. The high score (rank 1831 in the model output) reflects graph-based association, not clinical support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 115630 | LIBRAX |

## Safety Considerations

Please refer to the package insert for safety information. No interaction records were found in the data provided.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no trials, no literature, and a mechanistic rationale that is unconvincing for a condition requiring surgical treatment. Health Canada label data are also missing, so safety screening cannot start.

**To proceed, the following is needed:**
- Health Canada product monograph (indication, warnings, contraindications)
- Confirmed mechanism of action from DrugBank
- Evidence of any clinical rationale for cauda equina syndrome; without it, this candidate should not advance

**Other candidates in the same prediction set:**
- **Peptic ulcer disease** is the best-supported candidate, with 7 papers (evidence level L3). Most are 1960s–80s studies of clidinium combined with chlordiazepoxide. The most recent is a 2016 paper on adding clidinium-C to PPI-based triple therapy for *H. pylori*. It probably overlaps with the combination product's existing use, so it is closer to on-label adjunct use than true repurposing. Confirm the label status and study designs before reprioritising.
- **Obsolete neurogenic bladder** has a plausible antimuscarinic mechanism but no clidinium-specific evidence. Its ontology term is flagged as obsolete, so review the mapping first.
- **Myasthenia-related terms** (ranks 5–8) and the **receptor-activity grouping term** (rank 9) look like graph-adjacency artifacts, with no mechanistic rationale.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

