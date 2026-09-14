---
layout: default
title: Teriparatide
parent: 僅模型預測 (L5)
nav_order: 764
evidence_level: L5
indication_count: 10
---

# Teriparatide
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

# Teriparatide: From Osteoporosis to Duodenal Ulcer

## One-Sentence Summary

> Teriparatide (DrugBank DB06285) is a recombinant PTH(1-34) analog generally known for osteoporosis / fracture-risk-reduction therapy, though this evidence pack contains no confirmed original-indication or MOA data.
> The TxGNN model's top prediction is **Duodenal Ulcer**, but **0 clinical trials** and **0 publications** currently support this specific pairing, and the model's own rationale flags it as biologically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis / fracture-risk reduction (general drug knowledge — not confirmed by Canadian licensing data, as the drug is not marketed here) |
| Predicted New Indication | Duodenal Ulcer (disease) |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Teriparatide is broadly known as a recombinant fragment of human parathyroid hormone (PTH 1-34), acting on the PTH1 receptor to stimulate osteoblast activity and bone formation — this context is provided from general drug knowledge only, not from any Canadian regulatory source, since the product currently has no market presence or DIN in Canada.

The top-ranked prediction, duodenal ulcer, is a gastrointestinal mucosal disease with no established pharmacological connection to PTH signaling or bone metabolism. The evidence pack's own rationale is explicit on this point: there is no known mechanism supporting a PTH analog's efficacy against duodenal ulcer, and the high TxGNN score likely reflects statistical co-occurrence of calcium-homeostasis or gastrointestinal-related genes within the knowledge graph rather than genuine biological plausibility.

No clinical trials or literature support this specific drug–disease pairing. This is a pure knowledge-graph signal (Evidence Level L5) and would require substantial mechanistic and preclinical validation before any further consideration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Teriparatide is currently **not marketed in Canada** — there are 0 DINs on record in this evidence pack, so no authorization table can be generated.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/Health Canada label warnings and contraindications are flagged as a **Blocking** data gap (DG001) — this must be resolved before any safety-stage [S1] review can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (duodenal ulcer) has no clinical trial or literature support, and the model's own rationale states there is no known biological plausibility — Evidence Level L5.
- The drug is not marketed in Canada (0 DINs), and mechanism-of-action and safety-label data are both flagged as data gaps, one of which (DG001) is **Blocking**.

**To proceed, the following is needed:**
- Health Canada / manufacturer product monograph — warnings, contraindications (Blocking, DG001)
- DrugBank or literature-sourced mechanism of action (High priority, DG002)
- Preclinical or mechanistic rationale specifically linking PTH signaling to duodenal ulcer pathophysiology before this candidate can advance past S0

---

**Additional Note:** Among the 10 candidates in this pack, rank #8 — *pregnancy and lactation-associated osteoporosis* — has substantially stronger real-world support than the top-ranked pairing: 2 registered clinical trials and 19 publications, several specifically evaluating teriparatide's clinical use and bone-density outcomes in this population (e.g., PMID 34132853, 35903718, 39156353). This is consistent with known off-label teriparatide use for PLO and may warrant a separate, dedicated evaluation rather than being treated as a low-ranked TxGNN signal.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

