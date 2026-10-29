---
layout: default
title: Calcitriol
parent: Model Prediction Only (L5)
nav_order: 148
evidence_level: L5
indication_count: 5
monitor_inn: "CALCITRIOL"
predicted_indications: ["obsolete vitamin D deficiency", "renal tubular acidosis", "acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "hereditary hypophosphatemic rickets"]
last_modified_at: 2026-10-30
description: "Calcitriol: predicted new indication obsolete vitamin D deficiency (evidence level L5). Approved use: Not recorded in the local data"
---

# Calcitriol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Calcitriol: active vitamin D hormone (vitamin D receptor agonist) → obsolete vitamin D deficiency
{: .text-alpha }

## One-Sentence Summary

Calcitriol is the active hormonal form of vitamin D and is marketed in Canada as a single-ingredient product.
The TxGNN model predicts it may be useful for **obsolete vitamin D deficiency**, with a prediction score of **0.9996**.
There are currently **no clinical trials and no publications** retrieved for this specific prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | obsolete vitamin D deficiency |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 6 of 8) |
| Number of DINs | 8 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Calcitriol is, however, the biologically active form of vitamin D (1,25-dihydroxyvitamin D3). It acts through the vitamin D receptor to regulate calcium and phosphate handling. A biological link to vitamin D deficiency is therefore plausible, and this is likely why the model scores the prediction so highly.

Three points weaken the case:
- The disease term is flagged as **obsolete** in the disease vocabulary, so it may not correspond to a clearly defined current clinical condition.
- Calcitriol is already the activated hormone. Nutritional vitamin D deficiency is generally treated with native vitamin D (cholecalciferol or ergocalciferol) rather than calcitriol.
- No trials or literature were retrieved to show that calcitriol benefits patients with this condition.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Eight single-ingredient licences are currently valid. The main authorizations are listed below. Approved indication text and dosage forms are not recorded in the local data.

| DIN | Product Name |
|---------|------|
| 00481823 | ROCALTROL |
| 00481815 | ROCALTROL |
| 02485710 | TARO-CALCITRIOL |
| 02485729 | TARO-CALCITRIOL |
| 02431645 | CALCITRIOL-ODAN |

## Safety Considerations

- **Drug Interactions** (100 interacting drugs were identified; the main ones are listed):
  - **Major:** cholecalciferol, calcifediol and burosumab. Combining active or native vitamin D forms raises the risk of excess vitamin D effect and hypercalcaemia. Burosumab is a major interaction because it changes phosphate and vitamin D handling.
  - **Moderate:**
    - Thiazide diuretics (hydrochlorothiazide, chlorothiazide, chlorthalidone, bendroflumethiazide, benzthiazide) can raise calcium levels.
    - Enzyme-inducing anticonvulsants and barbiturates (carbamazepine, fosphenytoin, amobarbital, butabarbital, butalbital) can lower vitamin D activity.
    - Bile acid sequestrants (cholestyramine, colesevelam, colestipol) can reduce absorption.
    - Digoxin and digitoxin carry arrhythmia risk if calcium rises.
    - Aluminum hydroxide and topical calcipotriol also interact.

Package insert warnings and contraindications for the Canadian products were not available in the data compiled for this report. Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The score is very high, but the prediction has no supporting trials or publications. The disease term is obsolete, and native vitamin D rather than calcitriol is the usual treatment for nutritional deficiency. This places it at evidence level L5.

**To proceed, the following is needed:**
- Clarification of which current, non-obsolete disease concept this prediction maps to
- Clinical or literature evidence directly studying calcitriol in that condition, including comparison against native vitamin D
- Mechanism-of-action data
- Package insert warnings and contraindications from Health Canada, to support a safety screen (hypercalcaemia and the interactions above)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

