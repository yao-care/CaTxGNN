---
layout: default
title: Raloxifene
parent: Model Prediction Only (L5)
nav_order: 789
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-13
description: "Raloxifene: predicted new indication Duodenal ulcer (evidence level L5). Approved use: Postmenopausal osteoporosis / osteoporosis"
---

# Raloxifene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Raloxifene: From Postmenopausal Osteoporosis to Duodenal Ulcer

## One-Sentence Summary

Raloxifene is a selective estrogen receptor modulator (SERM) originally used to treat postmenopausal osteoporosis.
The TxGNN model predicts it may be effective for **duodenal ulcer**, but this is a model-based prediction only,
with **0 clinical trials** and **0 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Postmenopausal osteoporosis / osteoporosis |
| Predicted New Indication | Duodenal ulcer |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, raloxifene is a selective estrogen receptor modulator (SERM) that acts on bone, lipid metabolism and breast/uterine tissue. Its efficacy in postmenopausal osteoporosis is established.

For duodenal ulcer, no clear mechanistic link has been identified. Duodenal ulcer is driven mainly by *H. pylori* infection, NSAID use and acid hypersecretion, and no recognized estrogen-receptor pathway connects raloxifene to these processes. The very high TxGNN score (99.72%) is a graph-based prediction and is not backed by any clinical trial or publication in the data compiled for this report.

Other predictions from the same model were also reviewed, and all share the same limitation (L5, no supporting studies):

| Predicted Indication | TxGNN Score | Comment |
|------|------|------|
| Hypoalphalipoproteinemia | 99.65% | Indirect plausibility: raloxifene lowers LDL cholesterol, but its effect on HDL is small and inconsistent. Low HDL is often genetic. |
| Duodenal obstruction | 99.64% | No mechanistic rationale; this is usually a structural condition treated surgically or endoscopically. The score likely reflects graph proximity to other duodenal terms. |
| Duodenogastric reflux | 99.59% | No known prokinetic, bile-binding or mucosal-protective action. Raloxifene's adverse-effect profile offers no offsetting rationale. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02358840 | ACT RALOXIFENE | – | – |
| 02540681 | JAMP RALOXIFENE | – | – |
| 02279215 | APO-RALOXIFENE | – | – |

All three are valid single-ingredient authorizations. Dosage form and approved-indication text are not available in the compiled data.

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: hypertensive disorder, hypertension, liver disease, gallbladder disease, atrial fibrillation, hypertriglyceridemia, thrombophlebitis, coronary artery disease, stroke disorder, cerebrovascular disorder, susceptibility to ischemic stroke, cerebral infarction, pulmonary embolism, retinal artery occlusion, thrombophilia, impaired renal function, transient ischemic attack, vertebrobasilar insufficiency, antiphospholipid syndrome. Many of these relate to thromboembolic and cardiovascular risk.
- **Drug Interactions**: The interaction screen returned 100 potentially interacting drugs, none with a severity rating. Examples include calcitriol, pantoprazole, omeprazole, lansoprazole, glimepiride, metformin, simvastatin, doxycycline, tetracycline, morphine and vancomycin. Because severity is unclassified, clinical significance cannot be judged from this data.

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for duodenal ulcer rests only on a graph-based model score. There is no clinical trial or literature evidence, and no plausible mechanistic link to raloxifene's SERM pharmacology. The known thromboembolic and cardiovascular risks argue against advancing without a clear rationale.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) from DrugBank, to enable a proper mechanistic-link analysis
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- A targeted literature search on raloxifene in peptic or duodenal ulcer disease, and on HDL effects if hypoalphalipoproteinemia is to be considered
- Dosage form and approved-indication details for the three Canadian DINs
- Severity classification of the drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

