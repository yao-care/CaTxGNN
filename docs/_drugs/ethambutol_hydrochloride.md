---
layout: default
title: Ethambutol Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 272
evidence_level: L5
indication_count: 0
---

# Ethambutol Hydrochloride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Ethambutol Hydrochloride: Drug Repurposing Evaluation Report

## One-Sentence Summary

Ethambutol Hydrochloride is a first-line antimycobacterial agent used in the treatment of active tuberculosis. The current Evidence Pack **contains no TxGNN-predicted new indications** for this drug — the model output is absent and essential data fields (DrugBank ID, MOA, safety warnings) have not been populated. This report reflects the current data state and recommends a **Hold** pending resolution of upstream data gaps.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not populated in Evidence Pack |
| Predicted New Indication | No predictions available |
| TxGNN Prediction Score | — |
| Evidence Level | Not determinable |
| Canada Market Status | Not marketed (per Evidence Pack) |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Ethambutol Hydrochloride is currently in an incomplete state — `predicted_indications` is empty and all drug-level data fields (DrugBank ID, MOA, original indications, safety warnings) are unpopulated. Without a TxGNN prediction output and baseline drug data, no repurposing evaluation can be conducted.

**To proceed, the following is needed:**

- **Re-run TxGNN pipeline** for Ethambutol Hydrochloride to generate predicted indication candidates with scores
- **Resolve DrugBank mapping** — the query log shows a successful DrugBank lookup (`result_count: 1`) but `drugbank_id` is null; investigate the mapping failure and re-populate `original_moa`, `original_indications`, and DrugBank categories
- **Verify Canada market status** — Health Canada DIN records should be re-queried; Ethambutol HCl is a well-established antimycobacterial agent and the "Not marketed" status warrants confirmation
- **Obtain package insert safety data** — retrieve Health Canada product monograph to populate `key_warnings` and `contraindications` (currently blocking the S1 safety screening step per DG001)
- **Re-generate Evidence Pack** after above gaps are resolved before proceeding to full repurposing evaluation

---

> ⚠️ **Data Status Notice**
>
> This report could not be fully evaluated due to critical upstream data gaps (DG001: Safety warnings — Blocking; DG002: MOA — High severity). The DrugBank query on 2026-03-25 returned 1 result but was not integrated into the Evidence Pack. Remediation should be prioritised before this candidate re-enters the evaluation pipeline.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

