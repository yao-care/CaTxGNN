---
layout: default
title: Verapamil
parent: Model Prediction Only (L5)
nav_order: 971
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
description: "Verapamil: predicted new indication Obsolete bundle branch block (evidence level L5). Approved use: Hypertension, atrial fibrillation, acute coronary syndrome…"
---

# Verapamil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Verapamil: From Hypertension to Obsolete Bundle Branch Block

## One-Sentence Summary

Verapamil is a calcium channel blocker, originally used to treat hypertension, atrial fibrillation, angina and ventricular arrhythmias.
The TxGNN model predicts it may be effective for **obsolete bundle branch block**, but there are **no clinical trials and no publications** supporting this prediction.
This is a model-only prediction and should be treated with caution.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, atrial fibrillation, acute coronary syndrome, Prinzmetal angina, ventricular tachycardia (the approved indication text for Canadian licences is not available) |
| Predicted New Indication | Obsolete bundle branch block |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, verapamil is an L-type calcium channel blocker. Its efficacy in hypertension and in supraventricular and ventricular arrhythmias is established, and it slows conduction through the atrioventricular (AV) node.

Mechanistically, however, the prediction is hard to justify. Bundle branch block is a conduction defect in the His-Purkinje system. Slowing conduction would not be expected to treat it and could make conduction disease worse. The high score (0.996) appears to reflect network-based similarity in the knowledge graph rather than a biological rationale. The disease term is also flagged as obsolete, so the prediction has doubtful clinical meaning.

Other predictions in the list are shown below for context. All are also at the hypothesis stage:

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Malignant hypertensive renal disease | 99.27% | L5 | Overlaps with the approved antihypertensive class effect; no supporting studies |
| 3 | Malignant renovascular hypertension | 99.27% | L5 | The two retrieved papers do not evaluate verapamil as a treatment |
| 4 | Pulmonary hypertension with unclear multifactorial mechanism | 99.26% | L5 | Not a standard agent; negative inotropy is a risk in right heart failure |
| 5 | Pulmonary hypertension owing to lung disease and/or hypoxia | 99.26% | L4 | Preclinical and mechanistic support only; calcium channel blockers are generally not recommended here |
| 6 | Braddock syndrome | 99.15% | L5 | No mechanistic rationale evident |
| 7 | Periodic paralysis with transient compartment-like syndrome | 99.08% | L5 | Channelopathy, so biologically conceivable, but a hypothesis only |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for obsolete bundle branch block.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00782483 | AA-VERAP | Not specified | Not specified |
| 00782491 | AA-VERAP | Not specified | Not specified |
| 02166739 | VERAPAMIL HYDROCHLORIDE INJECTION USP | Injection (by product name) | Not specified |
| 01907123 | ISOPTIN SR | Sustained-release (by product name) | Not specified |
| 02210347 | MYLAN-VERAPAMIL SR | Sustained-release (by product name) | Not specified |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (model-derived relationships, not package insert text). The most clinically relevant for this prediction are:
  - Cardiac conduction and function: atrioventricular block, heart failure, hypotensive disorder, ventricular tachycardia (including catecholaminergic and incessant infant forms), hypertrophic cardiomyopathy, aortic stenosis and related aortic valve disease
  - Neuromuscular: myasthenia gravis and neuromuscular junction disease
  - Organ function: kidney disease, liver disease, gallbladder disease, renal artery obstruction
  - Haematological and other: neutropenia, agranulocytosis, angioedema (several types, including hereditary), connective tissue, bone and cartilage disease
- **Drug Interactions**: 100 interactions were found. The first 20 returned include:
  - **Major**: loperamide
  - **Moderate**: hydrocortisone, metformin, bupropion, aprepitant, triamcinolone, acetylsalicylic acid, dexamethasone, betamethasone, budesonide (including nasal), cimetidine, clarithromycin, canagliflozin, and several calcium salts (phosphate, acetate, carbonate, chloride, citrate)
  - **Minor**: morphine

Please refer to the package insert for the official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction is supported by a model score only, with no trials or literature. Verapamil's pharmacology (slowing conduction) runs against treating a conduction block, and atrioventricular block is among the knowledge-graph contraindications. The disease term is also obsolete.
- Among the other predictions, pulmonary hypertension owing to lung disease and/or hypoxia has the most mechanistic and preclinical support (L4), but it is not clinical evidence, and calcium channel blockers are generally not recommended there.

**To proceed, the following is needed:**
- Review of the Health Canada package insert for warnings, contraindications and approved indications. This is a blocking gap for safety screening.
- Mechanism of action data from DrugBank.
- Clarification of the obsolete disease term and mapping to a current diagnosis.
- Expert cardiology review of whether any clinical rationale exists.
- If pursuing another prediction, a targeted literature search and clinical evidence specific to verapamil.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

