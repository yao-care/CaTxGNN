---
layout: default
title: Terazosin
parent: 僅模型預測 (L5)
nav_order: 761
evidence_level: L5
indication_count: 10
---

# Terazosin
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

# Terazosin: From Hypertension/BPH to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

> Terazosin is an alpha-1 adrenergic antagonist historically used to treat **hypertension and benign prostatic hyperplasia (BPH)**.
> The TxGNN model's top-ranked prediction is **Hypotrichosis Simplex of the Scalp**,
> but this specific prediction currently has **0 clinical trials** and **0 publications** supporting it — the signal is model-output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension / Benign Prostatic Hyperplasia (inferred from drug class — alpha-1 adrenergic antagonist; no Canadian license record available, see below) |
| Predicted New Indication | Hypotrichosis Simplex of the Scalp |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for terazosin is not available in this Evidence Pack. Based on the pharmacological class referenced throughout this pack's own rationale notes, terazosin is a selective **alpha-1 adrenergic receptor antagonist**, used clinically for blood pressure control and BPH via smooth-muscle relaxation.

For the top-ranked prediction — hypotrichosis simplex of the scalp — the proposed mechanistic link is that alpha-1 receptors are expressed in hair follicles, so alpha-1 blockade could theoretically influence follicular blood flow or piloerector muscle tone. However, this link is **purely speculative** and not supported by any trial or publication in the pack.

More importantly, this same Evidence Pack flags a significant internal inconsistency: within the top 10 TxGNN candidates, terazosin scores highly for **both** hypotrichosis (hair loss/thinning, ranks 1–3) **and** hypertrichosis (excess hair growth, rank 8) — two opposite phenotypes. This pattern is explicitly noted in the pack as suggestive of a **knowledge-graph node-linkage artifact** rather than a genuine biological signal, and substantially weakens confidence in the top-ranked prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Terazosin is currently **not marketed in Canada** under this Evidence Pack — 0 DINs are on record, and no product license or approved-indication text is available for comparison against the predicted indication.

---

## Safety Considerations

Please refer to the package insert for safety information.

Note: this Evidence Pack has a flagged **Blocking** data gap (DG001 — TFDA/product labeling warnings and contraindications) that currently prevents this candidate from entering safety pre-screening (S1), and a **High**-severity gap (DG002 — mechanism of action), which limits confidence in any mechanistic rationale offered above.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (hypotrichosis simplex of the scalp) has zero clinical trial or literature support, is rated L5 (model prediction only), and its mechanistic rationale is undermined by the model's simultaneous, contradictory prediction of the opposite phenotype (hypertrichosis) — consistent with a likely knowledge-graph artifact rather than a real signal.

**To proceed, the following is needed:**
- Product labeling / contraindication data (TFDA or Canadian equivalent) — currently a **Blocking** gap preventing safety pre-screening
- Confirmed mechanism of action (MOA) data from DrugBank or equivalent source
- Independent, disease-specific evidence (trials or mechanistic studies) directly addressing follicular alpha-1 receptor biology, rather than reliance on TxGNN score alone
- Resolution of the conflicting hypotrichosis/hypertrichosis signal before this candidate is reconsidered

---

## Appendix: Other Candidate Indications in This Evidence Pack

This is a multi-indication candidate pack; two lower-ranked (by TxGNN score) predictions reached **S1 / Research Question** status with actual — though old and limited — clinical evidence, and may warrant separate evaluation rather than being screened out along with the top-ranked candidate:

| Rank | Disease | TxGNN Score | Evidence Level | Key Evidence |
|------|---------|-------------|-----------------|--------------|
| 5 | Migraine disorder | 99.92% | L3 | Small open-label trial (PMID [7911406](https://pubmed.ncbi.nlm.nih.gov/7911406/), 1994, n=46) and a case-series commentary (PMID [9074296](https://pubmed.ncbi.nlm.nih.gov/9074296/), 1997) on alpha-1 blockers for migraine prophylaxis; no follow-up large-scale trials since. |
| 7 | Raynaud disease | 99.83% | L3 | Small clinical study (PMID [9273472](https://pubmed.ncbi.nlm.nih.gov/9273472/), 1997) reporting reduced vasospastic attack frequency/severity with terazosin; mechanistically plausible via alpha-1-mediated vasoconstriction blockade. |

Both remain constrained by the same Blocking (TFDA labeling) and High (MOA) data gaps noted above, and evidence is decades old with no modern confirmatory trials.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

