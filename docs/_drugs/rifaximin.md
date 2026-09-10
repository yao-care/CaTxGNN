---
layout: default
title: Rifaximin
parent: 僅模型預測 (L5)
nav_order: 678
evidence_level: L5
indication_count: 6
---

# Rifaximin
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

# Rifaximin: From Non-Absorbable Gut Antibiotic to Oral Candidiasis

## One-Sentence Summary

Rifaximin is an oral, non-absorbable antibiotic (original indication data not available in this evidence pack). The TxGNN model's top-ranked prediction is **Oral Candidiasis**, but the only supporting publication currently on file actually reports that rifaximin use *increases* the risk of drug-resistant Candida infection rather than treating it — so this signal should be read as a caution flag, not a therapeutic lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no license/indication data on file; original MOA also missing) |
| Predicted New Indication | Oral Candidiasis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L4 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on the literature retrieved for this candidate, rifaximin is described as "an oral and non-absorbable antibiotic," meaning it acts locally within the gut lumen rather than systemically — a property that would not obviously extend to an oral mucosal fungal infection like oral candidiasis.

More importantly, the single piece of literature evidence behind this prediction points in the opposite direction from what a repurposing signal would need. The cohort study (PMID 34180023) found that rifaximin use in allogeneic hematopoietic stem cell transplant recipients was associated with an *increased* incidence of micafungin-resistant Candida infections, consistent with rifaximin disrupting normal gut/mucosal microbial balance rather than treating candidiasis. The TxGNN model's high score (99.75%) likely reflects a strong graph-embedding relationship between rifaximin and candidiasis, but the model does not appear to distinguish the direction of that relationship (causing/favoring infection vs. treating it). This mismatch between a high prediction score and adverse-direction evidence is itself an important finding, not just a data gap.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Cohort | Annals of Hematology | Rifaximin use was associated with (favoured) micafungin-resistant Candida spp. infections in allogeneic HSCT recipients — an adverse association, not a therapeutic one |

---

## Canada Market Information

Rifaximin is not currently marketed in Canada; no DIN records are on file for this evidence pack (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA label warnings/contraindications are flagged as a **blocking data gap (DG001)** — this must be resolved before any safety-based go decision can be made.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Oral Candidiasis) carries only Evidence Level L4, with zero clinical trials and a single cohort study whose finding actually contradicts a therapeutic role for rifaximin in candidiasis. Combined with a blocking gap on TFDA safety labeling and missing mechanism-of-action data, there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (blocking gap DG001)
- Confirmed mechanism of action (DG002) to evaluate biological plausibility
- Independent literature or trial evidence clarifying whether rifaximin is protective or causative for candidiasis before any further evaluation
- Re-review of lower-ranked candidates (all currently L5, no evidence) only if new data emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

