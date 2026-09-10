---
layout: default
title: Maraviroc
parent: 僅模型預測 (L5)
nav_order: 487
evidence_level: L5
indication_count: 10
---

# Maraviroc
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

# Maraviroc: From HIV-1 Infection to Multiple Endocrine Neoplasia

## One-Sentence Summary

Maraviroc is a CCR5 antagonist originally used as an HIV-1 entry inhibitor. The TxGNN model's top-ranked prediction points to **Multiple Endocrine Neoplasia (MEN)**, but this is currently supported by **0 clinical trials** and **0 publications** — and the evidence pack's own mechanistic review states there is no known biological link between CCR5/chemokine signaling and MEN pathogenesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (CCR5 antagonist / viral entry inhibitor) |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Maraviroc is not available in this evidence pack (flagged as a Blocking data gap for TFDA/Health Canada labeling and a High-severity gap for MOA). Based on known pharmacology referenced elsewhere in this pack, Maraviroc is a CCR5 antagonist that blocks HIV-1 viral entry into CD4+ cells — its efficacy in HIV-1 infection is well established.

However, for this top-ranked prediction, the model's own rationale states plainly: *"MEN is a hereditary endocrine tumour syndrome driven by RET/MEN1 gene mutations, with no known biological connection to CCR5/chemokine signaling — this is a model score only, with no mechanistic or literature support."* In other words, the high TxGNN score (99.82%) is not corroborated by any plausible mechanistic pathway, clinical trial, or published study.

This is a case where the numerical prediction score is high but the qualitative evidence is essentially absent — a pattern the evidence level (L5) and recommendation (Hold) are designed to flag. It should not be interpreted as a validated repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Canada Market Information

Maraviroc is currently **not marketed** in Canada under this evidence pack (0 DINs on file). No Health Canada product licenses are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (Multiple Endocrine Neoplasia) has a high model score but zero supporting trials, zero literature, and an explicit statement in the rationale that no mechanistic link to CCR5 exists — this does not meet even a preliminary evidence bar.
- Core safety inputs (TFDA/Health Canada label warnings, contraindications, MOA) are marked as data gaps, one of which (label warnings/contraindications) is Blocking and prevents entry into initial safety screening (S1).

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data for Maraviroc (DrugBank API query, per remediation plan DG002)
- Health Canada/TFDA product monograph for warnings and contraindications (per remediation plan DG001)
- Independent mechanistic or preclinical evidence specifically linking CCR5 antagonism to MEN pathogenesis before any further evaluation
- Note: among the 10 predicted indications in this pack, **HER2-positive breast carcinoma** (rank 10, evidence level L4, decision stage S1 "Research Question") shows a more concrete mechanistic rationale — CCL5-CCR5 signaling has been shown to drive trastuzumab resistance via ERK pathway activation — and may warrant a separate, dedicated evaluation rather than being deprioritized purely by TxGNN rank.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

