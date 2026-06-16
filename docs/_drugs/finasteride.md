---
layout: default
title: Finasteride
parent: 僅模型預測 (L5)
nav_order: 330
evidence_level: L5
indication_count: 6
---

# Finasteride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Finasteride: From Androgenetic Alopecia / BPH to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Finasteride is a well-established 5-alpha reductase inhibitor (5-ARI) used globally for male androgenetic alopecia and benign prostatic hyperplasia (BPH), though no product is formally registered in this market based on available regulatory data.
The TxGNN model predicts it may be effective for **Ambras Type Hypertrichosis Universalis Congenita** — a rare congenital condition of excessive whole-body hair growth — with **no clinical trials** and **no publications** currently supporting this direction.
The mechanistic rationale is fundamentally contradictory: finasteride suppresses DHT-driven hair follicle activity (treating hair *loss*), while Ambras syndrome is a chromosomal structural disorder causing non-androgenic hair *overproduction*.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in this market (globally recognized for: androgenetic alopecia, BPH) |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.994% |
| Evidence Level | L5 — Model prediction only, no supporting studies |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data was not returned by the evidence collection pipeline for this candidate. Based on established pharmacology, finasteride is a competitive inhibitor of 5-alpha reductase type II (and type I at higher doses), the enzyme that converts testosterone to dihydrotestosterone (DHT). By reducing circulating and tissue DHT levels, finasteride slows androgen-driven follicular miniaturization in male pattern hair loss and reduces prostate gland volume in BPH. Its clinical efficacy in these indications is extensively documented and globally recognized.

Ambras Syndrome (hypertrichosis universalis congenita of the Ambras type) is a structurally distinct biological entity caused by a paracentric inversion of chromosome 8q22, leading to dysregulated overexpression of hair growth signalling genes. This mechanism operates entirely outside the androgen/DHT axis: the affected follicles are not DHT-sensitive, and the excessive hair growth is not driven by androgen receptor activity. Lowering DHT via 5-ARI inhibition would have no corrective effect on a chromosomally determined hair phenotype.

The directional mismatch is fundamental: finasteride is specifically designed to *reduce* androgenic hair follicle stimulation (treating hair loss), while Ambras syndrome involves non-androgenic hair *overproduction* secondary to a chromosomal structural defect. The high TxGNN score almost certainly reflects statistical co-occurrence of hair-phenotype nodes in the biomedical knowledge graph rather than a genuine causal pathway. There is no mechanistic hypothesis, no pre-clinical model, no clinical trial, and no publication that supports this repurposing direction.

---

## Clinical Trial Evidence

No clinical trials related to finasteride and Ambras type hypertrichosis universalis congenita are currently registered.

---

## Literature Evidence

No literature related to finasteride and Ambras type hypertrichosis universalis congenita is currently available.

---

## Canada Market Information

No Health Canada–approved products for finasteride are present in the current regulatory dataset (0 DINs returned). This finding may reflect a data pipeline gap rather than the true regulatory status; finasteride is authorized in numerous jurisdictions under brand names including Proscar® (5 mg, BPH) and Propecia® (1 mg, androgenetic alopecia). Clinicians and researchers should independently verify the current status via the Health Canada Drug Product Database before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is a fundamental directional contradiction between finasteride's DHT-suppressing mechanism of action and the chromosomal/genetic aetiology of Ambras syndrome, compounded by a complete absence of clinical trial, pre-clinical, or published literature evidence supporting this repurposing hypothesis.

**To proceed, the following would be needed:**
- Identification of any plausible biological pathway linking 5-alpha reductase inhibition to the paracentric inversion at 8q22 and downstream gene dysregulation in Ambras syndrome
- Pre-clinical studies (in vitro or animal model) demonstrating that finasteride or DHT suppression produces any measurable effect on the Ambras syndrome hair phenotype
- A mechanistic hypothesis that resolves the directional contradiction before any human study is contemplated
- Verification of Health Canada regulatory data through the Drug Product Database to confirm actual DIN and approval status
- Retrieval of full TFDA/Health Canada prescribing information to complete the safety profile (currently blocking)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

