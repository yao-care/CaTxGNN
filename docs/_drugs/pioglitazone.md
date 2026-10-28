---
layout: default
title: Pioglitazone
parent: Model Prediction Only (L5)
nav_order: 739
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Pioglitazone: predicted new indication Opsismodysplasia (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "PIOGLITAZONE"
predicted_indications: ["opsismodysplasia", "classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
---

# Pioglitazone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Pioglitazone: From Type 2 Diabetes Mellitus to Opsismodysplasia
{: .text-alpha }

## One-Sentence Summary

Pioglitazone is an insulin-sensitizing drug (a PPAR-gamma agonist) originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **opsismodysplasia**, a rare skeletal dysplasia,
but **no clinical trials and no publications** currently support this prediction. It rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 0.9959 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 13 of 13) |
| Number of DINs | 13 (valid: 13) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, pioglitazone is a thiazolidinedione that activates PPAR-gamma, improving insulin sensitivity and supporting pancreatic beta-cell function. Its efficacy in type 2 diabetes is well established.

Opsismodysplasia is a rare skeletal dysplasia caused by INPPL1 mutations. INPPL1 encodes SHIP2, a phosphoinositide phosphatase that affects insulin/PI3K signaling. Any link to PPAR-gamma agonism is speculative. No clear mechanistic connection was identified, and the high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

**Other predictions reviewed** (all L5, all Hold, with no clinical trials or literature, except as noted):

| Rank | Predicted Indication | Score | Comment |
|------|------|------|------|
| 2 | Classic stiff person syndrome | 0.9950 | Possible immunomodulatory rationale; unproven |
| 3 | Focal stiff limb syndrome | 0.9950 | Same score and rationale as rank 2; likely a shared prediction from the TxGNN model (deep learning) that may reflect similarities the model learned between related diseases, not biological evidence |
| 4 | Thiamine-responsive dysfunction syndrome | 0.9948 | Glycemic overlap only; standard care is thiamine and insulin |
| 5 | Drug-induced localized lipodystrophy | 0.9930 | Adipose biology is relevant, but stopping the offending drug is the usual management |
| 6 | Centrifugal lipodystrophy | 0.9926 | Theoretical rationale only |
| 7 | Pressure-induced localized lipoatrophy | 0.9924 | Mechanical cause; usually resolves when the cause is removed |
| 8 | Idiopathic localized lipodystrophy | 0.9919 | Disease-class similarity only |
| 9 | Pancreatic agenesis | 0.9918 | Unlikely to work alone because pioglitazone needs endogenous insulin; 7 papers retrieved, all about type 2 diabetes |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for opsismodysplasia.

(For the rank 9 prediction, pancreatic agenesis, 7 papers were retrieved, but they concern type 2 diabetes and thiazolidinediones in general rather than the predicted disease. They are indirect at best and do not count as supporting evidence.)

## Canada Market Information

Pioglitazone is marketed in Canada with 13 valid single-ingredient licences (no combination products and no cancelled licences). Dosage form and approved indication text are not available in the compiled data. Five of the licences are listed below.

| DIN | Product Name |
|---------|------|
| 02326485 | MINT-PIOGLITAZONE |
| 02365529 | JAMP PIOGLITAZONE |
| 02339595 | ACH-PIOGLITAZONE |
| 02302888 | TEVA-PIOGLITAZONE |
| 02302977 | APO-PIOGLITAZONE |

## Safety Considerations

**Drug Interactions**: 100 interactions were found in the DDInter database. Most of those listed are Moderate, and some are Minor. Examples include:
- Moderate: abiraterone, acetazolamide, alpelisib, epinephrine, formoterol, hydrochlorothiazide, hydrocortisone, phenylephrine, pseudoephedrine, salbutamol, ethanol
- Minor: nifedipine, ethinylestradiol, lipoic acid, topical corticosteroids

**Conditions flagged in the knowledge graph as contraindications** (derived from graph relationships, not label text):
- Congestive heart failure
- Kidney disease
- Liver disease
- Gallbladder disease
- Adrenocortical insufficiency / Addison disease
- Pituitary hormone deficiencies and hypogonadotropic hypogonadism (including Kallmann syndrome)
- Thymus gland disease
- Infectious disease

Health Canada package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high model score (L5). There are no clinical trials or relevant publications, and no credible mechanistic link between PPAR-gamma agonism and opsismodysplasia. The other top predictions are similarly unsupported. The known safety profile of pioglitazone also raises concerns, notably congestive heart failure.

**To proceed, the following is needed:**
- Mechanistic evidence connecting pioglitazone or PPAR-gamma signaling to INPPL1/SHIP2 biology (preclinical or in vitro studies)
- Detailed mechanism of action data
- Health Canada package insert warnings and contraindications for formal safety screening
- Assessment of route compatibility and similarity to the original indication
- Any case reports or clinical data in the predicted disease, if they exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

