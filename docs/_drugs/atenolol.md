---
layout: default
title: Atenolol
parent: 僅模型預測 (L5)
nav_order: 71
evidence_level: L5
indication_count: 9
---

# Atenolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Atenolol: From Hypertension to Posteroinferior Myocardial Infarction

---

## One-Sentence Summary

Atenolol is a well-established cardioselective β1-adrenergic receptor blocker, globally recognized for treating hypertension and angina pectoris, though no Health Canada DIN record was found in the current dataset.
The TxGNN model predicts it may be effective for **Posteroinferior Myocardial Infarction**, with **0 clinical trials** and **1 publication** currently supporting this specific direction.
The mechanistic rationale is scientifically plausible, but direct subtype-specific clinical evidence is very sparse, placing this prediction at an early exploratory stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not on record in Canada dataset; atenolol is globally indicated for hypertension and angina pectoris |
| Predicted New Indication | Posteroinferior Myocardial Infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Canada Market Status | Not marketed (0 DINs on record) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, atenolol is a selective β1-adrenergic receptor blocker. By occupying cardiac β1 receptors, it reduces heart rate, myocardial contractility, and oxygen consumption — the core mechanisms that limit ischemic myocardial injury and suppress post-infarction sympathetic overstimulation.

Posteroinferior myocardial infarction typically results from occlusion of the right coronary artery or the circumflex branch, leading to ischemia of the inferior and posterior left ventricular wall. In this context, β1 blockade theoretically reduces heart rate and myocardial oxygen demand, limits infarct extension, and lowers the risk of ventricular arrhythmias and remodelling — all well-established benefits of beta-blockers in the broader post-MI population. The high TxGNN score likely reflects the strong graph topology connection between atenolol and myocardial infarction nodes in the knowledge graph.

However, posteroinferior MI carries a specific risk: right coronary artery occlusion frequently damages the sinoatrial and atrioventricular nodes, resulting in sinus bradycardia and AV conduction block. This makes the use of any beta-blocker in this MI subtype more complex than in anterior MI. While the general mechanistic support is strong, direct clinical evidence confirming that atenolol is effective and safe specifically in the posteroinferior subtype is essentially absent — the only identified publication dates to 1985 and was not powered to confirm this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for posteroinferior myocardial infarction.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [3901170](https://pubmed.ncbi.nlm.nih.gov/3901170/) | 1985 | Single-blind Randomized Cross-over | La Revue de médecine interne | Compared anti-ischemic activity of atenolol (200 mg) vs. diltiazem (240 mg) in 23 post-MI patients undergoing rehabilitation 4 weeks after limited posteroinferior or anterior MI with residual ischemia; computerized bicycle ergometer analysis (Case-Marquette system) |

---

## Canada Market Information

No Health Canada Drug Identification Numbers (DINs) are recorded for atenolol in the current dataset.

> **Note:** This likely reflects a data gap rather than true non-availability. Atenolol is a long-established generic drug that has historically been available in Canada. A direct review of the Health Canada Drug Product Database (HCDPD) is strongly recommended to reconcile this discrepancy before any regulatory or formulary assessment proceeds.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key warnings, contraindications, and drug interaction data were not retrieved in this Evidence Pack. As a beta-blocker, atenolol carries well-known class-level risks including bradycardia, AV block, bronchospasm (particularly relevant in patients with COPD or asthma), and rebound hypertension on abrupt withdrawal. These are especially pertinent given the posteroinferior MI context, where AV conduction disturbances are common. Formal safety data retrieval from the Health Canada product monograph or equivalent source is required before clinical evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While a plausible mechanistic basis exists for beta-blocker use in myocardial infarction broadly, direct clinical evidence for atenolol specifically in the posteroinferior MI subtype is limited to a single small cross-over study from 1985. The evidence level (L4) and the absence of any registered clinical trial for this specific indication preclude advancement without further investigation, particularly given the heightened AV block risk unique to this MI territory.

**To proceed, the following is needed:**
- Retrieve and confirm Canada DIN records via the Health Canada Drug Product Database
- Obtain full MOA data from DrugBank (DrugBank ID: DB00335)
- Extract safety data (key warnings, contraindications, drug interactions) from Health Canada product monograph or package insert
- Conduct a broader literature search for beta-blocker evidence stratified by MI territory (inferior/posterior subtype) to assess indirect class-level support
- Evaluate the AV conduction risk profile in posteroinferior MI before any prospective trial design is considered
- Consider whether a broader cardiac indication (e.g., post-MI left ventricular dysfunction, general secondary prevention) would represent a more evidence-supported entry point for atenolol repurposing in Canada

---

*This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

