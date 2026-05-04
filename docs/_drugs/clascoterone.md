---
layout: default
title: Clascoterone
parent: 僅模型預測 (L5)
nav_order: 169
evidence_level: L5
indication_count: 10
---

# Clascoterone
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

# Clascoterone: From Acne Vulgaris to Candidiasis

## One-Sentence Summary

Clascoterone is a topical androgen receptor (AR) antagonist approved in some international markets for acne vulgaris, but with no current Health Canada authorization.
The TxGNN model predicts it may be effective for **Candidiasis**, with **0 clinical trials** and **0 publications** currently supporting this direction.
This is a model-only prediction (L5) with limited mechanistic rationale and a recommendation to **Hold** pending further investigation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acne vulgaris (topical AR antagonist; no Canadian DIN on file) |
| Predicted New Indication | Candidiasis |
| TxGNN Prediction Score | 94.82% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on available contextual information, Clascoterone is a topical androgen receptor (AR) antagonist (cortexolone 17α-propionate). It works by competitively blocking dihydrotestosterone (DHT) binding at AR in sebaceous glands and hair follicles, reducing sebum production and follicular inflammation — the established basis for its acne vulgaris indication in other regulatory jurisdictions.

Candidiasis is a fungal infection caused by *Candida* species and is managed primarily with antifungal agents targeting fungal cell wall or membrane synthesis. There is no direct mechanistic bridge between AR antagonism and antifungal activity. The internal repurposing rationale assessment flags that this TxGNN prediction likely originates from a knowledge graph artifact — the model may have traversed a negative association between topical corticosteroids and skin fungal infections and misread it as a positive repurposing signal, since Clascoterone shares structural features with steroid-class molecules.

The known immunomodulatory effects of topical AR antagonists (local, minimal systemic exposure) do not plausibly support an anti-*Candida* hypothesis. This prediction should be interpreted as a model-generated false positive rather than a biologically grounded repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Clascoterone currently has no Health Canada authorizations and is not marketed in Canada. No DINs are on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The candidiasis prediction carries no mechanistic support — Clascoterone is a topical AR antagonist with no antifungal activity, and the TxGNN signal most likely reflects a knowledge graph traversal artifact rather than a true therapeutic opportunity. The complete absence of clinical trial and published literature evidence further disqualifies this candidate from further development in this direction.

**To proceed, the following is needed:**
- Obtain MOA data from DrugBank (DG002 remediation) to fully characterize AR/GR receptor binding profiles before evaluating any repurposing candidate
- Obtain TFDA/Health Canada package insert warnings and contraindications (DG001 remediation) to complete the safety baseline
- Prioritize mechanistically stronger repurposing candidates from the same prediction set over candidiasis — specifically **atrophoderma vermiculata** (rank 6; plausible AR-driven follicular keratinization mechanism) and **adrenal gland hyperfunction** (rank 9; dual AR/GR antagonism rationale with cortexolone structural basis)
- Any candidiasis indication would require preclinical demonstration of anti-*Candida* activity as a prerequisite before any clinical investment is considered

---

> ⚠️ **Disclaimer**: This report is intended for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

