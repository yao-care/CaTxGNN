---
layout: default
title: Lisinopril
parent: 僅模型預測 (L5)
nav_order: 392
evidence_level: L5
indication_count: 10
---

# Lisinopril
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

Using the report as directly specified by the user's detailed prompt template (no additional skill applies — this is a self-contained report-authoring task with its own complete formatting spec already provided).

# Lisinopril: From Hypertension to Posteroinferior Myocardial Infarction

## One-Sentence Summary

Lisinopril is a long-established ACE inhibitor whose core approved use is hypertension (and, in many jurisdictions, heart failure/post-MI cardioprotection). The TxGNN model predicts it may be effective for **Posteroinferior Myocardial Infarction**, but this specific top-ranked prediction currently has **0 clinical trials** and **0 publications** directly supporting it — the signal rests on the knowledge-graph score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (well-established ACE-inhibitor indication; not captured as a structured field in this evidence pack) |
| Predicted New Indication | Posteroinferior Myocardial Infarction |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Canada Market Status | 未上市 (Not marketed) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on known pharmacology, lisinopril is an angiotensin-converting enzyme (ACE) inhibitor — a drug class whose efficacy in hypertension, heart failure, and post-myocardial-infarction ventricular remodeling is well established in cardiology practice. ACE inhibition reduces afterload, lowers angiotensin II-driven vasoconstriction, and limits adverse cardiac remodeling, which is the pharmacological basis commonly cited for ACE-inhibitor use across the broader ischemic/hypertensive cardiovascular disease spectrum.

Posteroinferior myocardial infarction is an anatomical subtype of MI, so a mechanistic connection to an ACE inhibitor's known post-MI remodeling benefit is plausible in principle. However, the evidence pack contains no clinical trials, literature, or ICTRP records specifically tying lisinopril to this exact anatomical MI subtype — the `repurposing_rationale` fields for this candidate are unpopulated ("pending"), so this connection has not yet been formally substantiated.

Notably, other predictions in this same evidence pack for lisinopril are better supported by drug-specific literature: rank 4 ("pulmonary hypertension owing to lung disease and/or hypoxia") and rank 9 ("chronic pulmonary heart disease") both surface publications specifically studying lisinopril in cor pulmonale and pulmonary hypertension (e.g., PMID 17047621, PMID 14524095), plus 5 related clinical trial records for rank 9. These may represent more actionable near-term repurposing signals than the top-ranked candidate discussed here, and are worth flagging for parallel evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Lisinopril is currently **not marketed** in Canada per this dataset (0 DINs / licenses on file). No product listings are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** A Blocking-severity data gap (DG001) has been identified — Health Canada/TFDA label warnings and contraindications have not yet been retrieved. Per the evidence pack, this **prevents the candidate from entering the S1 safety pre-assessment stage** until resolved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (posteroinferior myocardial infarction) has no supporting clinical trials or literature — evidence level L5, model prediction only.
- A Blocking data gap (DG001, missing label warnings/contraindications) explicitly prevents safety pre-assessment (S1) from proceeding.
- The drug is not currently marketed in Canada (0 DINs), so the regulatory pathway for this candidate is unclear.

**To proceed, the following is needed:**
- Retrieve the official Health Canada product monograph / TFDA label to resolve the Blocking safety data gap (DG001)
- Obtain DrugBank mechanism-of-action detail to resolve the High-severity MOA gap (DG002)
- Run targeted literature/trial searches specifically for "posteroinferior myocardial infarction" + lisinopril, since none currently exist
- Consider evaluating the better-evidenced related candidates in this same pack (chronic pulmonary heart disease / pulmonary hypertension due to hypoxia, which already have lisinopril-specific literature and trial records) as alternative, more mature repurposing leads
- Clarify current Canadian regulatory/market status given the 0-license finding
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

