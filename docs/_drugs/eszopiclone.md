---
layout: default
title: Eszopiclone
parent: 僅模型預測 (L5)
nav_order: 269
evidence_level: L5
indication_count: 0
---

# Eszopiclone
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

# Eszopiclone: Sedative-Hypnotic Agent — Insufficient Data for Repurposing Evaluation

## One-Sentence Summary

Eszopiclone (DrugBank DB00402) is a non-benzodiazepine sedative-hypnotic known for its use in insomnia treatment.
The current Evidence Pack contains **no TxGNN-predicted new indications** for this compound, and the drug is **not marketed in Taiwan**.
Evaluation cannot advance beyond the preliminary stage due to multiple blocking data gaps, including absent regulatory records, missing mechanism of action data, and no safety information on file.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in current Evidence Pack |
| Predicted New Indication | None — no TxGNN predictions available |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A (no predictions to evaluate) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Taiwan Regulatory Information

Eszopiclone currently holds **zero drug licenses (licenses)** in Taiwan and has no documented marketing history in this jurisdiction. No dosage form records, brand name registrations, or approved indication texts are available.

> This drug is not authorized for use in Taiwan. Any repurposing evaluation would need to account for a full regulatory pathway from scratch.

---

## Safety Considerations

All safety data fields in the current Evidence Pack are absent. No key warnings, contraindications, or drug interaction records were retrieved.

> Please refer to the originating country's package insert (e.g., FDA-approved Lunesta® labeling) for safety information, including CNS depression warnings, complex sleep behavior risk, and dependence potential.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Eszopiclone is critically incomplete — there are no TxGNN repurposing predictions, no Taiwan regulatory records, no mechanism of action data, and no safety information. There is no repurposing candidate to evaluate at this time.

**To proceed, the following is needed:**

- **Re-run TxGNN prediction pipeline** for DB00402 (Eszopiclone) — the `predicted_indications` array is empty, suggesting the prediction step was not completed or the drug was not matched in the knowledge graph
- **Verify DrugBank mapping** — confirm that DB00402 is correctly linked to the KG node and that `run_kg_prediction.py` processed it without silent failure
- **Retrieve MOA data** from DrugBank API (DG002: High severity) — eszopiclone acts as a positive allosteric modulator of GABA-A receptors; this should be fetchable and is essential for mechanistic plausibility analysis
- **Taiwan market assessment** — confirm whether eszopiclone is intentionally absent from Taiwan (Health Canada / TFDA) or whether a data retrieval error occurred; note that eszopiclone *is* approved in the US (Lunesta) and several other markets
- **Safety data retrieval** — download and parse the originating country's package insert to populate key warnings and contraindications (DG001: Blocking severity)
- **Re-issue Evidence Pack** after above gaps are resolved before proceeding to full repurposing report
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

