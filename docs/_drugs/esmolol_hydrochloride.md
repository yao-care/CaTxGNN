---
layout: default
title: Esmolol Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 265
evidence_level: L5
indication_count: 0
---

# Esmolol Hydrochloride
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

# Esmolol Hydrochloride: Repurposing Evaluation Incomplete — Critical Data Gaps

## One-Sentence Summary

Esmolol Hydrochloride is a short-acting cardioselective beta-1 adrenoreceptor blocker primarily indicated for acute supraventricular tachyarrhythmias and perioperative haemodynamic control.
The TxGNN model did not generate any repurposing predictions for this drug in this Evidence Pack cycle, as key inputs — including DrugBank ID and regulatory indication records — were not resolved.
No clinical trial or literature evidence was retrieved; a full repurposing evaluation cannot be completed at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in this Evidence Pack |
| Predicted New Indication | No prediction generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — Prediction pipeline did not produce output |
| Canada / Taiwan Market Status | Not marketed (0 licenses found) |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

The TxGNN pipeline requires a resolved DrugBank ID to anchor a drug node in the knowledge graph and compute drug–disease association scores. For this Evidence Pack, `drugbank_id` was returned as `null`, which means Esmolol Hydrochloride could not be linked to the graph — and therefore no candidate disease predictions were produced.

In addition, the regulatory data query returned zero active licences and no approved indication text. Without at least one mapped indication, the pipeline's disease-similarity and co-indication enrichment steps cannot run.

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Esmolol is an ultra-short-acting IV beta-1 selective blocker (plasma half-life ≈ 9 minutes, ester-hydrolysis metabolism) with established efficacy in supraventricular tachycardia, atrial fibrillation/flutter rate control, and perioperative hypertension. Potential repurposing hypotheses — such as its use in sepsis-related tachycardia, thyroid storm, or stress cardiomyopathy — exist in the literature, but cannot be scored or ranked until the pipeline inputs are corrected.

---

## Safety Considerations

Safety data was not retrieved in this Evidence Pack. Please refer to the package insert for safety warnings and contraindications before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction pipeline produced no output because the DrugBank ID was unresolved and regulatory licence records were absent, making it impossible to compute repurposing scores or assess evidence level.

**To proceed, the following is needed:**

- **Resolve DrugBank ID**: Query the DrugBank API with the INN "esmolol" or salt form "esmolol hydrochloride" and populate `drugbank_id` in the Evidence Pack
- **Retrieve regulatory data**: Check Health Canada's Drug Product Database (DPD) or TFDA licence registry for active or historic DIN/licence records for esmolol formulations (e.g., Brevibloc®)
- **Populate original indication**: Extract at least one approved indication text to enable disease-mapping and co-indication enrichment
- **Retrieve MOA data**: Query DrugBank API for pharmacodynamics, targets, and mechanism of action fields
- **Retrieve safety data**: Download and parse the package insert PDF from Health Canada or TFDA for warnings, contraindications, and black-box alerts
- **Re-run TxGNN prediction pipeline** with corrected inputs to generate drug–disease repurposing candidates
- **Re-collect evidence**: After predictions are generated, run ClinicalTrials.gov and PubMed collectors against the top-ranked disease candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

