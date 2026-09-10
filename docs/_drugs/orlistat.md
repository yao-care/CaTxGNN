---
layout: default
title: Orlistat
parent: 僅模型預測 (L5)
nav_order: 582
evidence_level: L5
indication_count: 1
---

# Orlistat
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

# Orlistat: From Obesity (Weight Management) to Hypervitaminosis

## One-Sentence Summary

Orlistat is a gastrointestinal lipase inhibitor originally used for obesity/weight management by blocking dietary fat absorption. The TxGNN model predicts it may be effective for **Hypervitaminosis** (excess fat-soluble vitamins), but this prediction is currently supported by **zero clinical trials** and **zero publications** — it is a pure model-derived hypothesis with no direct evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obesity / weight management (pancreatic and gastric lipase inhibitor) — not officially confirmed by Canadian regulatory data, as the drug is not currently marketed there |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.42% (rank 10,329) |
| Evidence Level | L5 |
| Canada Market Status | 未上市 (Not marketed) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the drug record itself. Based on known pharmacology, orlistat is a gastrointestinal (pancreatic and gastric) lipase inhibitor: it blocks hydrolysis of dietary triglycerides, reducing intestinal fat absorption. Its efficacy in obesity/weight management is well established. A known consequence of this mechanism is reduced absorption of fat-soluble vitamins (A, D, E, K), which is normally listed as a **side effect** rather than a therapeutic goal.

The TxGNN model's high score (0.994) for hypervitaminosis appears to reflect this same "fat/lipid-soluble substance absorption inhibition" pathway, but with the logic reversed: if orlistat reduces fat absorption, it might also reduce excess absorption of fat-soluble vitamins in cases of vitamin overdose (hypervitaminosis A/D/E/K).

This is a mechanistically plausible but highly speculative extrapolation — it reframes a known adverse effect as a potential therapeutic effect, which is the opposite direction from how the mechanism is normally used clinically. No direct pharmacological, preclinical, or clinical evidence currently supports this reframing as an actual treatment strategy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Orlistat is not currently marketed in Canada (0 DIN, 0 licenses on record). No product/dosage form/approved-indication data is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is model-only (L5), with no supporting clinical trials, literature, or preclinical data, and it relies on a reversed-direction extrapolation of a known side effect rather than an established pharmacological rationale. Combined with the drug's unmarketed status in Canada and missing safety/MOA data, there is currently no basis to advance beyond exploratory screening (decision stage S0).

**To proceed, the following is needed:**
- Confirmed original MOA and indication data from DrugBank/regulatory sources (currently flagged as a Blocking data gap)
- TFDA/Health Canada label warnings and contraindications (currently a Blocking data gap)
- Preclinical or mechanistic studies specifically testing lipase inhibition as a treatment for vitamin overdose
- Any case reports or pharmacokinetic studies on orlistat's effect on fat-soluble vitamin toxicity clearance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

