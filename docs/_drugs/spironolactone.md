---
layout: default
title: Spironolactone
parent: 僅模型預測 (L5)
nav_order: 735
evidence_level: L5
indication_count: 2
---

# Spironolactone
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

# Spironolactone: From Unrecorded Original Indication to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Spironolactone (DrugBank DB00421) currently has no original indication or mechanism-of-action (MOA) data available in this Evidence Pack, and it is not marketed in Canada. The TxGNN model predicts potential efficacy for **Hypotrichosis Simplex of the Scalp**, but this prediction is supported only by model score (L5) — **no clinical trials or literature** currently back this direction, and the model's own rationale flags the mechanistic link as weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no Canada license data on file) |
| Predicted New Indication | Hypotrichosis Simplex of the Scalp |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for spironolactone is not available in this Evidence Pack (flagged as a High-severity data gap). No original indication records were found either, since the drug has no Canadian market authorization.

The repurposing rationale supplied with this candidate does note that spironolactone has a known anti-androgen mechanism (androgen receptor blockade, inhibition of testosterone/DHT synthesis), which has biological plausibility for androgen-driven hair loss such as androgenetic alopecia. However, **hypotrichosis simplex of the scalp is an autosomal-dominant congenital condition** caused by mutations in hair-follicle structural/keratin genes (e.g., CDH3, KRT71), and is **not driven by the androgen pathway**. The evidence pack's own assessment concludes that the high TxGNN score likely reflects semantic proximity between "hair loss / hair growth" concepts in the knowledge graph rather than a genuine mechanistic connection to this specific genetic disorder — the mechanistic link is therefore assessed as weak.

A second, related candidate (congenital hypotrichosis milia, rank 2, score 99.04%) shows the same pattern: a rare ectodermal-dysplasia-type congenital condition with no known relationship to spironolactone's diuretic/anti-androgen activity, again likely reflecting graph-level term association rather than biological plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Spironolactone is not currently marketed in Canada under this Evidence Pack's data — no DIN records are on file (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: TFDA/product-label warnings and contraindications are recorded as a **Blocking** data gap in this Evidence Pack — this drug cannot proceed to safety pre-screening (S1) until label warnings/contraindications are sourced and reviewed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predicted indications are L5 (model-score-only) with no clinical trial or literature support, and the model's own mechanistic rationale rates the biological link as weak for these rare congenital conditions. Combined with a Blocking-severity gap in TFDA safety labeling, this candidate does not currently meet the bar to advance past S0.

**To proceed, the following is needed:**
- TFDA (or equivalent) product label — warnings, contraindications, DDI data (Blocking gap, DG001)
- Confirmed original indication(s) and mechanism of action from DrugBank (High-priority gap, DG002)
- Independent literature or preclinical evidence specifically linking anti-androgen/mineralocorticoid-antagonist activity to keratin-gene-mediated congenital hypotrichosis, before this candidate can be re-scored above L5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

