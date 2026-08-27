---
layout: default
title: Hydroquinone
parent: 僅模型預測 (L5)
nav_order: 386
evidence_level: L5
indication_count: 4
---

# Hydroquinone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

Using the report structure provided directly in your prompt (this is a document-generation task from a supplied Evidence Pack, not a coding/skill-triggering task, so no additional skill applies here). I read the JSON carefully — noting that `original_indications` and `licenses` are both empty, `original_moa` is a flagged data gap (DG002), and `taiwan_regulatory.market_status` (used here as Canada market status per the field description) is "未上市" (Not Marketed) with 0 DINs — before drafting the report below.

---

# Hydroquinone: From Topical Hyperpigmentation Treatment to Seborrheic Keratosis

## One-Sentence Summary

> Hydroquinone is a well-established topical skin-depigmenting agent, historically used for hyperpigmentation and melasma — a use directly corroborated by the multiple hydroquinone-based melasma trials captured in this evidence pack (see Clinical Trial Evidence under the "exanthem (disease)" candidate). The TxGNN model predicts it may also be effective for **Seborrheic Keratosis**, but this direction is currently supported only by **0 clinical trials** and **2 tangentially related publications**, and a formal approved-indication record for the drug itself is not yet available.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in this dataset (DrugBank/regulatory records empty). Established dermatologic use as a topical tyrosinase-inhibiting depigmenting agent for hyperpigmentation/melasma is corroborated by trial data elsewhere in this pack. |
| Predicted New Indication | Seborrheic Keratosis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L3 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, hydroquinone belongs to the class of topical phenolic skin-depigmenting agents (tyrosinase inhibitors), and its efficacy in treating hyperpigmentation and melasma has been demonstrated across multiple comparator-controlled clinical trials — several of which appear in this evidence pack under a different predicted-indication entry (e.g., NCT00669071, NCT02977507, NCT05969587, all using 4% hydroquinone as the active or reference treatment for melasma). Mechanistically, this depigmenting activity may also be applicable to seborrheic keratosis.

Seborrheic keratosis and melasma/hyperpigmentation are pathophysiologically related in that both present clinically as hyperpigmented epidermal lesions involving keratinocyte and melanocyte abnormalities. A drug that suppresses melanin synthesis (via tyrosinase inhibition) could plausibly lighten the pigmented component of seborrheic keratosis lesions, which is likely the shared-network signal TxGNN picked up on.

That said, this is a mechanistic extrapolation rather than a directly demonstrated effect: no clinical trial in this pack tests hydroquinone specifically against seborrheic keratosis, and the two supporting publications discuss pigmentary disorders and dermatosis papulosa nigra (a seborrheic-keratosis-related condition) only in a general treatment-algorithm/review context, not as a targeted hydroquinone efficacy study.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for hydroquinone in seborrheic keratosis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33046430](https://pubmed.ncbi.nlm.nih.gov/33046430/) | 2021 | Observational study | Journal of Plastic, Reconstructive & Aesthetic Surgery | Prospective observational study proposing a combination treatment algorithm for facial pigmentary disorders in Asian patients; relevant to depigmenting-agent use but not a dedicated seborrheic keratosis trial. |
| [17373158](https://pubmed.ncbi.nlm.nih.gov/17373158/) | 2007 | Review | Journal of Drugs in Dermatology | Reviews treatment options for dermatosis papulosa nigra, histologically related to seborrheic keratosis; discusses removal approaches and procedural safety considerations rather than hydroquinone-specific efficacy data. |

---

## Canada Market Information

Hydroquinone is not currently marketed in Canada under this evidence pack — 0 DINs are on file, and `market_status` is recorded as "Not Marketed." No product licenses are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Key warnings, contraindications, and drug-interaction data for this product are currently unavailable in the source dataset — this is logged as a Blocking data gap (DG001) that prevents a full S1 initial safety assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence for the seborrheic keratosis indication specifically is limited to L3-level, indirect literature (no dedicated clinical trials), and the drug is not currently marketed in Canada (0 DINs).
- A Blocking data gap (DG001: TFDA/Health Canada label warnings and contraindications) prevents this candidate from entering the S1 safety pre-screen at all, regardless of efficacy evidence strength.

**To proceed, the following is needed:**
- Official product label / package insert data (warnings, contraindications) to resolve DG001 before any safety screening can occur
- DrugBank-sourced mechanism of action data (DG002) to substantiate the tyrosinase-inhibition rationale
- Dedicated clinical or preclinical studies directly testing hydroquinone in seborrheic keratosis, rather than relying on adjacent-indication literature
- Confirmation of Canadian market/regulatory pathway status, since the drug currently has no active DIN license on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

