---
layout: default
title: Soybean Oil
parent: 僅模型預測 (L5)
nav_order: 734
evidence_level: L5
indication_count: 1
---

# Soybean Oil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Soybean Oil: From Pharmaceutical Excipient to Amenorrhea

## One-Sentence Summary

Soybean oil (DrugBank DB09422) is not marketed in Canada as a standalone therapeutic product — it functions primarily as a pharmaceutical excipient or parenteral nutrition lipid emulsion component. The TxGNN model predicts a possible association with **Amenorrhea**, but this prediction is currently supported by **no clinical trials and no literature**, and the underlying mechanistic rationale does not identify a plausible biological link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established — soybean oil has no registered therapeutic indication; it is used as an excipient / parenteral nutrition lipid emulsion component |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for soybean oil is not currently available (Data Gap). Based on known information, soybean oil is used pharmaceutically as an excipient and as a lipid source in parenteral nutrition formulations, providing fatty acids and energy substrate and contributing to cell membrane composition. It has no established original therapeutic indication to compare against.

Critically, the model's own repurposing rationale explicitly notes that **no known mechanistic link** exists between soybean oil's pharmacological role (fatty acid/energy source, membrane component) and the hypothalamic-pituitary-ovarian axis pathways that regulate menstruation and estrogen/progesterone secretion, which underlie amenorrhea. The absence of original MOA data further reduces confidence in this association. In short, the high TxGNN score does not appear to be substantiated by a coherent mechanistic hypothesis at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

No Health Canada authorizations (DINs) are currently on file for this product in the evidence pack (total licenses: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score, there is no clinical trial or literature evidence supporting this indication, and the model's own mechanistic rationale finds no plausible biological link between soybean oil's known pharmacology and amenorrhea. This is a pure model prediction (L5) with a data gap on original MOA, which blocks progression to safety evaluation.

**To proceed, the following is needed:**
- Original MOA and any established/off-label indications for soybean oil (via DrugBank API)
- TFDA/Health Canada label warnings and contraindications (currently Blocking data gap, DG001)
- At least preclinical or mechanistic literature establishing a biological rationale for the amenorrhea link before further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

