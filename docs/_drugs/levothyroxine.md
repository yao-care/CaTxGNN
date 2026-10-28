---
layout: default
title: Levothyroxine
parent: Model Prediction Only (L5)
nav_order: 547
evidence_level: L5
indication_count: 4
monitor_inn: "Levothyroxine"
predicted_indications: ["renal hypodysplasia/aplasia", "bilateral renal agenesis", "Potter sequence", "Carney complex"]
last_modified_at: 2026-10-23
description: "Levothyroxine: predicted new indication Renal hypodysplasia/aplasia (evidence level L5). Approved use: Hypothyroidism"
---

# Levothyroxine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Levothyroxine: From Hypothyroidism to Renal Hypodysplasia/Aplasia
{: .text-alpha }

## One-Sentence Summary

Levothyroxine is a synthetic thyroid hormone used for hypothyroidism and several thyroid-related conditions.
The TxGNN model predicts it may be effective for **renal hypodysplasia/aplasia**, but the prediction is supported by **0 clinical trials** and **0 publications**.
It is a model-only prediction and should be treated with caution.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypothyroidism (relation recorded in the knowledge graph; the Canadian licence records compiled for this report contain no indication text) |
| Predicted New Indication | Renal hypodysplasia/aplasia |
| TxGNN Prediction Score | 0.9967 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses on record: at least 20) |
| Number of DINs | at least 20 |
| Number of approvals | At least 20 licences (single-ingredient products); the list may be partial |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Levothyroxine is a synthetic form of the thyroid hormone thyroxine. It is used for hypothyroidism, myxedema, goitre, Hashimoto thyroiditis and several thyroid cancers. These uses are not confirmed here by label text.

Thyroid hormone plays a role in kidney development and maturation, so a biological link is conceivable. However, renal hypodysplasia/aplasia is a structural congenital malformation that arises in utero. Postnatal levothyroxine is unlikely to reverse it.

The very high score (0.9967) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence or a demonstrated therapeutic effect. Because mechanism data is missing, this reasoning cannot be validated.

Other predictions in the same list (bilateral renal agenesis, Potter sequence, Carney complex) also have no supporting studies. Bilateral renal agenesis and Potter sequence are likely artifacts of the same renal-anomaly cluster. Carney complex may be linked through thyroid-related nodes, but any use would be adjunctive for thyroid lesions and would not treat the underlying disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

At least 20 valid single-ingredient licences were found; the list may be partial. The records compiled for this report do not include dosage form or approved indication text. Five examples are shown.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02550792 | APO-LEVOTHYROXINE | Not listed | Not listed |
| 02461714 | LEVOTHYROXINE SODIUM FOR INJECTION | Not listed (injection by product name) | Not listed |
| 02172119 | SYNTHROID | Not listed | Not listed |
| 02499924 | LEVOTHYROXINE SODIUM INJECTION | Not listed (injection by product name) | Not listed |
| 02213214 | ELTROXIN | Not listed | Not listed |

---

## Safety Considerations

- **Knowledge-graph contraindication relations** (not label text): hypertension, pituitary hormone deficiencies and hypogonadotropic hypogonadism (including Kallmann syndrome and Sheehan syndrome), osteoporosis and postmenopausal osteoporosis, diabetes mellitus and diabetic ketoacidosis, coronary artery disease, myocardial infarction, and thymus gland disease.
- **Drug Interactions**: 100 interactions were found. The 20 reviewed are mostly Moderate, with one Minor (cimetidine). Main groups:
  - Antidiabetic agents: acarbose, metformin, pioglitazone, alogliptin, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide, albiglutide, dulaglutide
  - Acid suppressants: omeprazole, rabeprazole, dexlansoprazole, cimetidine
  - Minerals and antacids: calcium phosphate, calcium acetate, magnesium oxide
  - Sympathomimetics: epinephrine, isometheptene, diethylpropion
- TSH suppression at higher doses carries cardiac and bone risks, which matters for the Carney complex prediction.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN model (deep learning) score, with no clinical trials or publications for renal hypodysplasia/aplasia. The condition is a structural malformation that thyroid hormone is unlikely to correct, so the high score is probably an artifact.

**To proceed, the following is needed:**
- Any clinical or preclinical evidence directly studying levothyroxine in renal hypodysplasia/aplasia
- Mechanism of action data and a clear mechanistic rationale for renal development
- Health Canada package insert warnings and contraindications
- Indication text, dosage form and route information for the Canadian licences
- Safety analysis for the target population (fetal, neonatal or paediatric) before any further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

