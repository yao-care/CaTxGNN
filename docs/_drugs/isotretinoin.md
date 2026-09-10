---
layout: default
title: Isotretinoin
parent: 僅模型預測 (L5)
nav_order: 426
evidence_level: L5
indication_count: 2
---

# Isotretinoin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Isotretinoin: Original Indication Unavailable → Predicted New Indication: Malignant Renovascular Hypertension

## One-Sentence Summary

Isotretinoin's original approved indication and mechanism of action are not available in the current Evidence Pack (data gap, remediation pending via DrugBank API query). The TxGNN model predicts potential relevance to **Malignant Renovascular Hypertension** (and a near-duplicate signal, Malignant Hypertensive Renal Disease), but this is based **purely on knowledge-graph embedding similarity, with zero supporting clinical trials or literature**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no licenses or indication data in Evidence Pack) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for isotretinoin in this Evidence Pack ([Data Gap] DG002, High severity, pending DrugBank API remediation). No original indication data was returned either, so no pharmacological or clinical relationship between the original use and the predicted indication can be established at this time.

Based on the model's own rationale output, there is **no known mechanistic link** between isotretinoin (a retinoid) and malignant renovascular hypertension — the prediction shows no connection to renin-angiotensin pathways or renal vasculature pathophysiology. Notably, isotretinoin's known safety signal (potential elevation of triglycerides and lipid metabolism effects) runs **counter to**, rather than in support of, this indication direction. The TxGNN score of 99.01% reflects graph-embedding similarity only and does not constitute mechanistic or clinical evidence.

A second, near-identical candidate — **Malignant Hypertensive Renal Disease** (same score, adjacent KG rank) — appears to be a redundant signal from a neighboring graph node rather than an independent finding, and carries the same lack of mechanistic support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Isotretinoin currently has no authorized products in Canada (0 DINs; market status: Not Marketed).

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not currently available; a TFDA label warnings/contraindications gap is flagged as Blocking [DG001], pending PDF label parsing.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on TxGNN embedding similarity (L5, no clinical or literature support), and the model's own mechanistic rationale finds no biological link — with a known safety signal pointing the opposite direction. Combined with the absence of Canadian market presence and missing MOA/label data, there is no basis to advance this candidate.

**To proceed, the following is needed:**
- Isotretinoin mechanism of action data (DrugBank API query, DG002)
- TFDA/product label warnings and contraindications (Blocking gap DG001)
- Any preclinical or mechanistic literature specifically linking retinoids to renal vascular/hypertensive pathology
- Clarification on whether the two predicted indications (malignant renovascular hypertension vs. malignant hypertensive renal disease) should be treated as one signal or two
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

