---
layout: default
title: Nusinersen
parent: 僅模型預測 (L5)
nav_order: 566
evidence_level: L5
indication_count: 10
---

# Nusinersen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Nusinersen: From Spinal Muscular Atrophy to Neoplasm of Immature B and T Cells

## One-Sentence Summary

Nusinersen is an antisense oligonucleotide whose only publicly documented approved use is spinal muscular atrophy (SMA); this information is **not captured in the current evidence pack**, since the original indication and mechanism-of-action fields are both flagged as data gaps. The TxGNN model's top-ranked new indication, **Neoplasm of Immature B and T Cells**, carries a prediction score of only **50%** — a value at the model's baseline, meaning it does not reflect a distinguishable signal — and is supported by **zero clinical trials and zero publications**. Across all 10 top-ranked candidates in this pack, every score is identically 0.5 and every recommendation is **Hold**, indicating this candidate set does not currently support any repurposing hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (no Health Canada license records; publicly known indication is Spinal Muscular Atrophy, unverified here) |
| Predicted New Indication | Neoplasm of immature B and T cells |
| TxGNN Prediction Score | 50.00% (baseline value — not a differentiated signal) |
| Evidence Level | L5 |
| Canada Market Status | Not marketed (未上市) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Nusinersen in this evidence pack (data gap DG002, severity High). Based on general public knowledge, Nusinersen is a 2'-MOE-modified antisense oligonucleotide that modulates SMN2 pre-mRNA splicing to increase functional SMN protein, and it is administered intrathecally for spinal muscular atrophy — a mechanism specific to motor neuron biology with no established link to lymphoid or myeloid oncogenesis.

For this specific candidate, "neoplasm of immature B and T cells," there is no mechanistic rationale, no clinical trial, and no literature evidence of any kind — the evidence base is entirely empty. A TxGNN score of exactly 0.5 corresponds to the model's baseline/near-random output, not a meaningfully elevated prediction, so no biological plausibility argument can be constructed from the data provided.

It is also worth noting that all 10 top-ranked predictions in this pack share the identical 0.5 score. Two of the other candidates (myeloid/lymphoid neoplasms with JAK2/PDGFRA/PDGFRB/FGFR1 abnormalities; neoplasm of mature T-cells or NK-cells) returned 20 PubMed hits each, but per the rationale notes these are disease-biology review articles retrieved via keyword co-occurrence (e.g., JAK2 inhibitors, NK-cell immunology) — none mention Nusinersen or antisense oligonucleotides, so they do not constitute drug-specific evidence. The remaining candidates, including the top-ranked one, have no evidence at all.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Canada Market Information

Nusinersen is not currently marketed in Canada (0 licenses/DINs on record), so no product-level market table is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug interaction data are all flagged as data gaps in this evidence pack — including a Blocking-severity gap for TFDA label warnings/contraindications, DG001 — so no drug-specific safety statements can be made at this time.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication has a TxGNN score at model baseline (0.5), zero supporting clinical trials, and zero supporting literature. Across the entire top-10 candidate list, every score is identical and equally uninformative, and no mechanistic hypothesis can be built due to missing MOA data. There is no evidentiary basis to advance this candidate beyond a screening-stage hold.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain and parse the TFDA/Health Canada product label for warnings and contraindications
- Resolve DG002 (High): retrieve confirmed mechanism-of-action data from DrugBank
- Re-run or re-rank the TxGNN prediction, since a uniform 0.5 score across the top 10 candidates suggests these results are near the model's noise floor rather than genuine high-confidence predictions — higher-scoring candidates elsewhere in the ranked output should be evaluated instead
- If pursuing candidates with literature hits (rank 2, rank 7), have a domain expert confirm whether the retrieved articles reflect genuine drug-disease relevance or are keyword-driven false positives, as currently assessed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

