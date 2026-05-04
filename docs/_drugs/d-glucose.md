---
layout: default
title: D-Glucose
parent: 僅模型預測 (L5)
nav_order: 191
evidence_level: L5
indication_count: 10
---

# D-Glucose
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

# D-glucose: From Energy Supplementation to Non-Syndromic Esophageal Malformation

## One-Sentence Summary

D-glucose (dextrose) is the body's primary monosaccharide energy substrate, widely used in clinical settings for hypoglycemia management and parenteral nutritional support, with no formal approved indication recorded in this regulatory dataset.
The TxGNN model predicts it may be effective for **Non-Syndromic Esophageal Malformation** with a prediction score of **84.11%**,
however **no clinical trials** and **no publications** currently support this repurposing direction, placing the prediction at the lowest evidence tier (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not formally registered (clinically used for hypoglycemia treatment and parenteral nutrition) |
| Predicted New Indication | Non-Syndromic Esophageal Malformation |
| TxGNN Prediction Score | 84.11% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, D-glucose is the universal monosaccharide energy currency of cellular metabolism. It fuels glycolysis, the TCA cycle, oxidative phosphorylation, and multiple biosynthetic pathways across virtually all cell types. In clinical practice, it is administered intravenously to correct hypoglycaemia and serves as the primary carbohydrate source in parenteral nutrition formulations.

Non-syndromic esophageal malformation encompasses structural congenital anomalies of the esophagus — most commonly esophageal atresia (with or without tracheoesophageal fistula) — arising from disrupted foregut morphogenesis during embryogenesis. These are fundamentally structural, developmental defects with no established pharmacological target that would be amenable to D-glucose intervention. The causal biology lies in transcription factor dysregulation (e.g., *SOX2*, *FOXA2*) and signalling pathway errors during organogenesis, not in postnatal energy metabolism.

The evidence pack's mechanistic rationale explicitly flags this prediction as probable model noise: the TxGNN model's high score (0.841) most likely reflects the ubiquity of glucose metabolic nodes in the knowledge graph, generating broad but non-specific associations. The current evidence pack contains zero supporting clinical trials and zero supporting publications for this indication. No plausible causal pathway exists by which exogenous D-glucose administration would correct or treat a structural esophageal developmental defect.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is zero clinical or preclinical evidence supporting D-glucose as a therapeutic agent for non-syndromic esophageal malformation, and no mechanistically plausible pathway has been identified. This TxGNN prediction most likely represents a false-positive signal arising from the model's broad, non-specific representation of glucose metabolism nodes within the knowledge graph rather than a genuine drug-disease relationship.

**To proceed, the following is needed:**
- Establish a biologically plausible mechanistic hypothesis linking D-glucose to esophageal malformation pathogenesis (e.g., through glucose-dependent developmental signalling or epigenetic regulation of foregut patterning genes)
- Conduct preclinical studies (in vitro organoid or animal model) to empirically test any proposed mechanism before human translation
- Obtain the full safety profile and package insert data, which are currently unavailable and constitute a blocking data gap
- Consult developmental biologists and pediatric gastroenterologists to evaluate whether glucose signalling plays any meaningful role in foregut morphogenesis
- Consider re-running TxGNN with structural anomaly-specific graph constraints to reduce noise-driven predictions for metabolically ubiquitous substrates like D-glucose
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

