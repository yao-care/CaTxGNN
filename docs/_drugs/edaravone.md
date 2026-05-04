---
layout: default
title: Edaravone
parent: 僅模型預測 (L5)
nav_order: 249
evidence_level: L5
indication_count: 2
---

# Edaravone
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

# EDARAVONE: From ALS / Acute Ischemic Stroke to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Edaravone (Radicava®/Radicut®) is a potent free radical scavenger approved for amyotrophic lateral sclerosis (ALS) in the United States and for acute ischemic stroke in Japan, acting through antioxidative neuroprotection.
The TxGNN model predicts it may be effective for **Heparin Cofactor 2 Deficiency**, a rare inherited thrombophilia,
with **0 clinical trials** and **0 publications** currently supporting this direction — this is a pure model-level prediction with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALS (Radicava®, US FDA 2017); Acute ischemic stroke (Radicut®, Japan PMDA) |
| Predicted New Indication | Heparin Cofactor 2 Deficiency |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established public knowledge, Edaravone is a small-molecule free radical scavenger that neutralises hydroxyl radicals (•OH) and peroxyl radicals, inhibits lipid peroxidation, and reduces oxidative stress-mediated endothelial and neuronal injury. This mechanism underpins its approved uses in ALS (delaying functional decline) and acute ischemic stroke (limiting infarct expansion).

Heparin cofactor 2 (HCII) deficiency is a rare hereditary thrombophilia in which reduced HCII activity — a serine protease inhibitor that inactivates thrombin in the presence of dermatan sulfate or heparin — creates a pro-thrombotic state. The mechanistic link between Edaravone and HCII deficiency is **indirect and highly speculative**. Scientific literature has shown that reactive oxygen species (ROS) can amplify coagulation by oxidatively modifying fibrinogen, promoting platelet aggregation, and enhancing procoagulant phospholipid membrane exposure. In theory, by reducing ROS-mediated endothelial injury and platelet activation, Edaravone could partially attenuate the thrombotic tendency caused by HCII deficiency. Importantly, however, Edaravone has no direct effect on HCII protein expression, thrombin-inhibitory capacity, or the dermatan sulfate/heparin cofactor pathway.

The repurposing rationale analysis rates mechanistic confidence as **low**: the full proposed chain (free radical scavenging → reduced ROS-mediated platelet activation → partial alleviation of thrombotic tendency in HCII deficiency) has not been validated in any animal model or cell-based system. This prediction is best treated as a hypothesis-generating signal rather than an actionable repurposing candidate at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Edaravone currently holds no approved DINs in Canada and is not marketed in the Canadian market.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Safety data (key warnings, contraindications, drug interactions) was not available in this Evidence Pack. For prescribing information, refer to the Radicava® (edaravone) US label or the Radicut® Japan label as reference documents until a formal Canadian monograph is obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a pure TxGNN model prediction (Evidence Level L5) with zero supporting clinical trials, zero published literature, and a mechanistic link rated as **low-confidence** and entirely unvalidated in experimental systems relevant to HCII deficiency. Edaravone is not marketed in Canada, and no formal safety profile for this indication was evaluable.

**To proceed, the following is needed:**

- **Preclinical validation:** Cell-based or animal model studies of HCII deficiency to test whether antioxidant intervention reduces thrombin generation or thrombotic events
- **Mechanistic data (MOA):** Retrieve full DrugBank entry (DB12243) to confirm mechanism and pharmacological targets
- **Safety review:** Obtain Radicava® (US) or Radicut® (Japan) package insert to extract warnings, contraindications, and DDI profile before any further evaluation
- **Literature sweep:** Targeted PubMed search on Edaravone + coagulation / thrombosis / oxidative stress to assess indirect mechanistic evidence
- **Disease epidemiology:** Assess HCII deficiency prevalence and unmet clinical need to determine whether a repurposing investment is justified given disease rarity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

