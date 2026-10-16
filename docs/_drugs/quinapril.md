---
layout: default
title: Quinapril
parent: Model Prediction Only (L5)
nav_order: 787
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Quinapril: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension (hypertensive disorder)"
monitor_inn: "QUINAPRIL"
predicted_indications: ["malignant hypertensive renal disease", "malignant renovascular hypertension", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
---

# Quinapril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Quinapril: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Quinapril is an ACE inhibitor originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but currently there are **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on model prediction alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 14 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, quinapril belongs to the ACE inhibitor class. Its efficacy in hypertension is established, and mechanistically it may be applicable to malignant hypertensive renal disease.

Malignant hypertensive renal disease (hypertensive nephrosclerosis with severe hypertension) involves activation of the renin-angiotensin-aldosterone system (RAAS), so blocking ACE is mechanistically plausible. However, this prediction is largely an extension of the already approved hypertension indication rather than a distinct repurposing opportunity.

The other predicted indications are weaker or less specific:
- **Malignant renovascular hypertension** (score 99.86%): RAAS activation from renal hypoperfusion makes ACE inhibition coherent, but caution is needed in bilateral renal artery stenosis, where ACE inhibitors can precipitate acute renal failure. No trials or literature are available.
- **Pulmonary hypertension, unclear multifactorial mechanism** (99.85%): Angiotensin II contributes to pulmonary vascular remodeling, but the heterogeneous causes weaken any specific link. Systemic vasodilators can also cause hypotension or worsen ventilation-perfusion matching.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (99.85%): This is the only prediction with literature, which consists of preclinical animal studies (L4).
- **Braddock syndrome** (99.79%): No clear mechanistic rationale; the high score likely reflects graph-based associations rather than biological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction (or for any of the other four predicted indications).

---

## Literature Evidence

Currently no related literature available for the top-ranked prediction.

For reference, the only literature found among the predictions relates to rank 4, pulmonary hypertension owing to lung disease and/or hypoxia:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8873672](https://pubmed.ncbi.nlm.nih.gov/8873672/) | 1996 | Preclinical (animal study) | Circulation | Inhibiting tissue ACE with quinapril reduced hypoxic pulmonary hypertension and pulmonary vascular remodeling |
| [8720418](https://pubmed.ncbi.nlm.nih.gov/8720418/) | 1996 | Preclinical (animal study, cardiac) | J Cardiovasc Pharmacol | Quinapril preserved left ventricular function and energy metabolism in rats after myocardial infarction; only tangentially relevant to pulmonary disease |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02517477 | JAMP QUINAPRIL | Not specified | Not specified |
| 02340585 | PMS-QUINAPRIL | Not specified | Not specified |
| 02517450 | JAMP QUINAPRIL | Not specified | Not specified |
| 02517469 | JAMP QUINAPRIL | Not specified | Not specified |
| 02340577 | PMS-QUINAPRIL | Not specified | Not specified |

These are 5 of 14 valid single-ingredient authorizations. The remainder include quinapril/hydrochlorothiazide products (APO-QUINAPRIL/HCTZ, AURO-QUINAPRIL HCTZ, JAMP QUINAPRIL / HCTZ).

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (not taken from label text): kidney disease, angioedema (including hereditary, acquired and RAAS-blocker-induced forms), pancreatitis, liver disease, hepatic coma/encephalopathy, gallbladder disease, systemic lupus erythematosus, diabetes mellitus and diabetic ketoacidosis, potassium deficiency, hypotensive disorder, anuria, neutropenia/agranulocytosis, gout, hyperparathyroidism, and connective tissue, bone and cartilage diseases.
- **Drug Interactions**: 100 interactions were identified in total. The one rated **Major** among those listed is **potassium citrate**, which raises hyperkalaemia concern with ACE inhibitors. Others listed are Moderate, for example metformin, acetylsalicylic acid, corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), SGLT2 inhibitors (canagliflozin, dapagliflozin), doxycycline, tetracycline, bupropion, morphine and chlorpropamide.
- For renovascular indications, caution is needed in bilateral renal artery stenosis because of the risk of acute renal failure.

Official package insert warnings were not available, so please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (99.86%), with no clinical trials or literature. The mechanism is plausible, but it mostly overlaps with quinapril's existing hypertension indication, so it offers limited new repurposing value.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A literature and trial search for ACE inhibitors in malignant hypertensive nephrosclerosis and renovascular hypertension
- Review of the renal safety profile (renal artery stenosis, hyperkalaemia, acute kidney injury) in the target population
- Authorization details for the DINs (dosage form and approved indication text)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

