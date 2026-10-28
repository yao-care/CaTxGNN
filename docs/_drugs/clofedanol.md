---
layout: default
title: Clofedanol
parent: Model Prediction Only (L5)
nav_order: 212
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Clofedanol: predicted new indication Nasal cavity disease (evidence level L4). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold…"
monitor_inn: "Clofedanol"
predicted_indications: ["nasal cavity disease", "allergic urticaria", "papillary conjunctivitis", "cold urticaria", "faucial diphtheria", "cervical disc degenerative disorder"]
---

# Clofedanol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Clofedanol: From Allergic and Upper Respiratory Tract Conditions to Nasal Cavity Disease
{: .text-alpha }

## One-Sentence Summary

Clofedanol was originally used for upper respiratory conditions such as allergic rhinitis, vasomotor rhinitis, pharyngitis and the common cold.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction is largely a restatement of existing indications and rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, rhinitis, nasopharyngitis (the Canadian licence has no indication text on file) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, clofedanol is generally described as a centrally acting cough suppressant with antihistaminic and anticholinergic properties. This description is not confirmed by the data compiled for this report, so it should be treated as unverified.

Nasal cavity disease is a broad category that includes rhinitis, which is already among clofedanol's original indications (allergic rhinitis, vasomotor rhinitis and rhinitis). The high score therefore mostly reflects overlap with existing uses rather than a genuinely new therapeutic direction. The score is a computational prediction, not clinical evidence.

Other predictions from the model are weaker. Allergic urticaria (0.9997), papillary conjunctivitis (0.9984) and cold urticaria (0.9978) would depend on an antihistamine-like effect that has not been confirmed. Faucial diphtheria (0.9933) and cervical disc degenerative disorder (0.9929) have no credible mechanistic link, and their scores come from the TxGNN model (deep learning) and probably reflect similarities the model learned between related diseases, not biological evidence. Diphtheria is a toxin-mediated bacterial infection that needs antitoxin and antibiotics. The cold urticaria score may also be inflated by the name similarity to "common cold".

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 01966294 | ULONE | Not specified | Not specified |

## Safety Considerations

- **Contraindication signals from the knowledge graph** (these are graph-based associations, not label text): hypertension, coronary artery disease, myocardial infarction, ventricular tachycardia, atrioventricular block, diabetes mellitus and diabetic ketoacidosis, hyperthyroidism (Graves disease, thyrotoxicosis), angle-closure glaucoma and ocular hypertension, benign prostatic hyperplasia and bladder neck obstruction, peptic ulcer disease, pancreatitis, acidosis (including lactic acidosis), and hemoglobinopathy.
- **Drug Interactions**: The interaction screening returned 100 interactions in total; the first 20 are listed in the data compiled for this report, all rated Moderate. They include central nervous system depressant and sedative combinations such as:
  - Opioids: morphine, codeine, dihydrocodeine, fentanyl, alfentanil, tramadol, opium, diphenoxylate and difenoxin.
  - Antihistamines: chlorpheniramine, promethazine, cetirizine and phenyltoloxamine.
  - Cannabinoids: dronabinol and nabilone.
  - Other agents: alprazolam, ethanol, metoclopramide, sibutramine and dichloralphenazone.

  Additive sedation is the likely concern, but the mechanism details were not included in the data.

The Canadian package insert warnings and contraindications were not available, so please refer to the package insert for authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for nasal cavity disease overlaps with clofedanol's existing rhinitis indications and has no supporting trials or literature, so it is not a distinct repurposing signal. The other predicted indications are either speculative or implausible.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently a blocking gap for safety screening
- Confirmed mechanism of action data (for example from DrugBank)
- Approved indication text, dosage form and manufacturer for DIN 01966294
- Clinical trial and literature searches for any indication that is genuinely new, such as allergic urticaria
- Route and formulation compatibility assessment for any non-respiratory target, such as ocular use
- Deprioritising faucial diphtheria and cervical disc degenerative disorder, which have no credible mechanistic link
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

