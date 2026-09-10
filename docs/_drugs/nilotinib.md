---
layout: default
title: Nilotinib
parent: 僅模型預測 (L5)
nav_order: 548
evidence_level: L5
indication_count: 1
---

# Nilotinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Nilotinib: From Chronic Myeloid Leukemia to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

Nilotinib is a second-generation tyrosine kinase inhibitor originally developed for Philadelphia chromosome-positive chronic myeloid leukemia (BCR-ABL-driven disease). The TxGNN model predicts it may be effective for **Dermatofibrosarcoma Protuberans (DFSP)**, a PDGFRB-driven sarcoma, but this direction is currently supported by only **0 clinical trials** and **1 publication** (a mechanistic review) — evidence is still at the preclinical/rationale stage.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Myeloid Leukemia (BCR-ABL-positive) — based on known drug class; not present in the supplied regulatory dataset |
| Predicted New Indication | Dermatofibrosarcoma Protuberans |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap). Based on well-established pharmacology, nilotinib is a second-generation tyrosine kinase inhibitor whose target spectrum covers BCR-ABL, PDGFR (α/β), and c-KIT — the same target class as imatinib, which is already approved for DFSP.

DFSP is driven almost exclusively by the COL1A1-PDGFB fusion gene, which causes constitutive activation of PDGFRB signaling. Because nilotinib directly inhibits PDGFRB, the mechanistic rationale for repurposing is biologically plausible: it mirrors the established imatinib-DFSP relationship and could theoretically serve as an alternative in imatinib-resistant or -intolerant cases.

This mechanistic overlap is the primary basis for the prediction score. However, it remains a target-class inference rather than direct clinical or in-vivo evidence for DFSP, which is why the evidence level is capped at L4 (mechanism-only).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Review | Pharmacological Research | Reviews small-molecule PDGFR inhibitors (including nilotinib's target class) in neoplastic disease, describing PDGF/PDGFR signaling biology relevant to PDGFRB-driven tumors such as DFSP; does not report direct DFSP clinical data |

## Canada Market Information

Nilotinib is currently **not marketed** in Canada (0 licenses/DINs on file), so no product-level table is available.

## Cytotoxicity

Nilotinib is an antineoplastic targeted therapy (tyrosine kinase inhibitor class), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is currently limited to a single mechanistic review article with no supporting clinical trials, and the drug is not yet marketed in Canada. The prediction rests on target-class analogy to imatinib rather than direct evidence in DFSP, which is insufficient to advance beyond the initial screening stage (S0).

**To proceed, the following is needed:**
- Confirmed original-indication and MOA data (currently a High-severity data gap)
- TFDA/product monograph safety warnings and contraindications (currently a Blocking data gap)
- Preclinical or case-level evidence specific to DFSP (not just PDGFR-class rationale)
- Initiation of clinical trial activity, or at minimum case reports, in PDGFRB-driven sarcomas
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

