---
layout: default
title: Sodium Zirconium Cyclosilicate
parent: 僅模型預測 (L5)
nav_order: 727
evidence_level: L5
indication_count: 10
---

# Sodium Zirconium Cyclosilicate
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

Using the report format from the task instructions above (this is the applicable "skill" for this request — a domain-specific report generation template supplied directly in the system prompt).

# Sodium Zirconium Cyclosilicate: From Hyperkalemia to Breast Fibrocystic Disease

## One-Sentence Summary

> Sodium zirconium cyclosilicate (SZC) is a non-absorbed potassium-binding polymer used to treat hyperkalemia by exchanging cations in the gastrointestinal tract. TxGNN's top prediction points to **Breast Fibrocystic Disease**, but this candidate has **no supporting clinical trials and no supporting literature**, and the model's own generated rationale flags it as a likely knowledge-graph artifact rather than a genuine mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperkalemia (drug's known/approved use referenced in evidence rationale; not confirmable from Canadian regulatory data, as the drug is unlicensed in Canada) |
| Predicted New Indication | Breast Fibrocystic Disease |
| TxGNN Prediction Score | 93.41% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available (Data Gap). Based on the information present in the evidence pack, SZC is a non-absorbed cation-exchange polymer that binds potassium locally in the gastrointestinal lumen and is not systemically absorbed. It has no known interaction with hormonal (estrogen/progesterone) regulatory pathways relevant to breast fibrocystic disease.

Unlike typical repurposing candidates in this report series, the evidence pack's own mechanistic rationale for this candidate explicitly argues **against** biological plausibility: it states the high TxGNN score is "suspected to reflect graph clustering of breast-related disease nodes rather than a genuine biological association" (疑為知識圖譜中乳房相關疾病節點群聚造成的高分假象). This pattern is reinforced by ranks 2–8, which are all breast-related conditions (fibrocystic disease, benign mammary dysplasia, blunt duct adenosis, apocrine adenosis, fat necrosis, breast abscess, lactation disease, breast adenosis) with descending but closely clustered scores (93.4%–90.5%) — consistent with an embedding-space artifact rather than 10 independent pharmacological signals.

Given the absence of MOA confirmation, the absence of any trial or literature evidence, and the model-generated rationale actively disputing plausibility, this candidate should not be treated as a credible repurposing lead at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Sodium zirconium cyclosilicate is currently not marketed in Canada under this evidence pack (`market_status: 未上市`, `total_licenses: 0`). No DIN records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: Key warnings, contraindications, and drug–drug interaction data are all marked as Data Gaps in this evidence pack. This is flagged as a **Blocking** gap (DG001 — TFDA label warnings/contraindications), meaning the candidate cannot proceed to the S1 safety pre-screen until this is resolved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- All 10 predicted indications are L5 (model prediction only), with zero clinical trials and zero literature support across the board.
- The evidence pack's own mechanistic rationale for the top-ranked candidate explicitly questions its validity, attributing the score to likely knowledge-graph clustering among breast-related disease nodes rather than a real pharmacological link.
- A Blocking data gap (missing TFDA label safety data) prevents this candidate from entering the S1 safety pre-screen regardless of indication strength.
- The drug is not currently marketed in Canada (0 DINs), which also limits near-term actionability.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official product label warnings/contraindications before any safety pre-screen
- Resolve DG002 (High): obtain confirmed MOA data via DrugBank API
- Independent methodological review of the TxGNN ontology/embedding space to confirm whether ranks 1–8 (all breast-related conditions) represent a systematic node-clustering artifact
- If pursuing further, deprioritize the breast-related cluster (ranks 1–8) and instead scrutinize ranks 9–10 (heparin cofactor 2 deficiency, antithrombin deficiency type 2) separately — though these also currently lack any mechanistic, trial, or literature support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

