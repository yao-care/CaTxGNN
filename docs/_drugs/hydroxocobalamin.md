---
layout: default
title: Hydroxocobalamin
parent: 僅模型預測 (L5)
nav_order: 387
evidence_level: L5
indication_count: 2
---

# Hydroxocobalamin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Hydroxocobalamin: From Cyanide Poisoning to Esophageal Varices without Bleeding

## One-Sentence Summary

Hydroxocobalamin is the pharmaceutical form of vitamin B12, established clinically as a cyanide poisoning antidote and for treatment of B12 deficiency; it is not currently marketed in Canada.
The TxGNN model predicts potential effectiveness for **Esophageal Varices without Bleeding** (and, at an almost identical score, the related **Esophageal Varices with Bleeding**),
but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a research hypothesis only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cyanide poisoning (antidote); Vitamin B12 deficiency |
| Predicted New Indication | Esophageal Varices without Bleeding |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap). Based on known pharmacological information, hydroxocobalamin is a vitamin B12 analog whose established clinical uses are as a cyanide poisoning antidote and for vitamin B12 deficiency — it is not currently approved for any hepatic or gastrointestinal indication.

The proposed mechanistic link to esophageal varices comes from a separate, well-documented pharmacological property of hydroxocobalamin: potent scavenging of nitric oxide (NO). This property has previously been investigated as an adjunct therapy for vasodilatory shock (e.g., septic shock). Because portal hypertension in cirrhosis is driven substantially by NO-mediated splanchnic vasodilation, NO scavenging offers a theoretical route by which hydroxocobalamin could reduce portal venous inflow and pressure — a mechanism analogous in logic (though not in target) to established splanchnic vasoconstrictors such as vasopressin or terlipressin used in variceal bleeding.

This connection is indirect and inferential rather than an established pharmacological indication, and it is currently unsupported by any registered clinical trial or published literature. The TxGNN score of 99.23% reflects the strength of association within the knowledge graph only and should not be interpreted as clinical efficacy evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Hydroxocobalamin currently has no marketing authorization in Canada (0 DINs; market status: Not Marketed). No product/DIN data is available for this evaluation.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Regulatory warnings/contraindications data (TFDA/Health Canada label) is currently a Blocking data gap (DG001) — this must be resolved before any safety pre-assessment (S1) can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5, model-prediction-only signal with zero supporting clinical trials or publications, and a Blocking data gap on regulatory safety information (warnings/contraindications) prevents even an initial safety assessment. The drug is also not currently marketed in Canada.

**To proceed, the following is needed:**
- Official label warnings and contraindications (resolve DG001, Blocking) to enable a S1 safety pre-assessment
- Confirmed mechanism of action documentation (resolve DG002)
- Preclinical or clinical evidence directly evaluating hydroxocobalamin, or NO-scavenging agents generally, in portal hypertension / esophageal varices
- Clarification of a regulatory pathway (e.g., special access) given the drug currently has no Canadian market authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

