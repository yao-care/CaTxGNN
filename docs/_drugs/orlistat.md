---
layout: default
title: Orlistat
parent: Model Prediction Only (L5)
nav_order: 687
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Orlistat: predicted new indication Hypervitaminosis (evidence level L5). Approved use: Obesity disorder"
monitor_inn: "ORLISTAT"
predicted_indications: ["hypervitaminosis"]
---

# Orlistat
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Orlistat: From Obesity to Hypervitaminosis

## One-Sentence Summary

Orlistat was originally used to treat obesity, including monogenic obesity.
The TxGNN model predicts it may be useful for **Hypervitaminosis**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the computational model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obesity disorder; monogenic obesity (the Canadian licence record contains no approved indication text) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, orlistat is a gastric and pancreatic lipase inhibitor that reduces dietary fat absorption by roughly 30%.

Fat-soluble vitamins (A, D, E, K) are absorbed together with dietary fat. In theory, lowering fat absorption could reduce their uptake and so reduce body load in fat-soluble hypervitaminosis, such as vitamin A or D excess.

This link is plausible but weak. It rests on a known adverse effect of orlistat (fat-soluble vitamin malabsorption), not on any demonstrated therapeutic benefit. Hypervitaminosis from excess supplementation is usually managed simply by stopping the supplement, and water-soluble hypervitaminosis would not be affected by this mechanism. The high TxGNN score (0.994) is a computational prediction only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02240325 | XENICAL | Not specified | Not specified |

## Safety Considerations

- **Contraindication-related diseases (from the knowledge graph, not label text)**: liver failure, primary hyperoxaluria, anorexia nervosa, bulimia nervosa, vitamin deficiency disorder, cholestasis, benign recurrent intrahepatic cholestasis, familial intrahepatic cholestasis, drug-induced liver injury. Of note, vitamin deficiency disorder appearing here is consistent with orlistat's effect on fat-soluble vitamin absorption.
- **Drug Interactions**: 100 interactions were recorded. The first 20 listed are mostly Moderate, with a few Minor. Examples:
  - Moderate: abacavir, lamivudine, emtricitabine, atazanavir, acarbose, albiglutide, alogliptin, canagliflozin, metformin, chlorpropamide, amiodarone, cannabidiol, asparaginase (*E. coli* and *Erwinia chrysanthemi*), calaspargase pegol, brentuximab vedotin, clofarabine
  - Minor: cholecalciferol, calcifediol, calcitriol

Please refer to the package insert for label warnings and contraindications, which are not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (L5), with no clinical trials or publications. The proposed mechanism relies on what is normally an adverse effect of orlistat. Standard management of hypervitaminosis (stopping the supplement) is already simple, and orlistat has many drug interactions and liver- and nutrition-related cautions.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- A literature and clinical-trial search on orlistat and fat-soluble vitamin excess (for example, vitamin A or D toxicity)
- Evaluation of whether reduced absorption offers a clinically meaningful benefit over simply stopping the supplement
- Route and formulation compatibility assessment, and the approved indication text and dosage form for the Canadian licence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

