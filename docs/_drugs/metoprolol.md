---
layout: default
title: Metoprolol
parent: Model Prediction Only (L5)
nav_order: 609
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Metoprolol: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertension, acute coronary syndrome, myocardial infarction"
monitor_inn: "Metoprolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "trichotillomania"]
---

# Metoprolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Metoprolol: From Hypertension and Myocardial Infarction to Malignant Renovascular Hypertension

## One-Sentence Summary

Metoprolol is a beta-1 selective blocker originally used for hypertension, acute coronary syndrome and myocardial infarction.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, but **no clinical trials** and only **1 publication** (a diagnostic study unrelated to metoprolol therapy) support this specific prediction.
Among the other predictions, **chronic pulmonary heart disease** has the most supporting evidence (4 clinical trials and 20 publications), though much of it points to safety concerns rather than benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, acute coronary syndrome, myocardial infarction (approved indication text is not available in the Canadian licence records) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, metoprolol is a beta-1 selective blocker that lowers heart rate, cardiac output and renin release. Its efficacy in hypertension and myocardial infarction is established.

Renin release is relevant to renovascular hypertension, so a mechanistic link is plausible. The high TxGNN score appears to reflect the disease's proximity to the approved hypertension indication in the knowledge graph rather than disease-specific evidence. The only linked paper (PMID 1988765) is a diagnostic study of chromogranin A in pheochromocytoma and does not address metoprolol treatment. Malignant hypertension is also usually managed with other first-line agents.

### Other Predictions in the Data

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Malignant hypertensive renal disease | 99.91% | L5 | No trials or literature; extrapolation from hypertension |
| 3 | Pulmonary hypertension, unclear multifactorial mechanism | 99.91% | L5 | No supporting data; beta-blockers are approached cautiously in pulmonary arterial hypertension |
| 4 | Pulmonary hypertension owing to lung disease/hypoxia | 99.91% | L4 | Literature mostly unrelated; no direct evidence |
| 5 | Braddock syndrome | 99.89% | L5 | Purely computational |
| 6–8 | Posterolateral, posteroinferior and septal myocardial infarction | 99.84%–99.80% | L4 | Subtypes of an already approved indication; not distinct repurposing opportunities |
| 9 | Chronic pulmonary heart disease | 99.40% | L3 | Mostly safety and tolerability data in COPD; see below |
| 10 | Trichotillomania | 99.05% | L5 | Purely computational |

---

## Clinical Trial Evidence

For the top-ranked prediction (malignant renovascular hypertension), no related clinical trials are currently registered.

The trials below relate to the rank 9 prediction, chronic pulmonary heart disease, which has the strongest evidence base:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06825728](https://clinicaltrials.gov/study/NCT06825728) | Phase 4 | Not yet recruiting | 311 | Metoprolol in heart failure with reduced ejection fraction and COPD; compares doses and examines all-cause death and rehospitalisation |
| [NCT02587351](https://clinicaltrials.gov/study/NCT02587351) | Phase 3 | Terminated | 532 | Randomised, placebo-controlled trial of metoprolol to prevent COPD exacerbations; the literature notes it did not reduce exacerbations and increased those requiring hospitalisation |
| [NCT00384566](https://clinicaltrials.gov/study/NCT00384566) | Phase 4 | Withdrawn | 0 | Carvedilol vs metoprolol respiratory assessment in heart failure; no data |
| [NCT05096884](https://clinicaltrials.gov/study/NCT05096884) | Early Phase 1 | Terminated | 14 | Post-COVID exertional dyspnoea and tachycardia; low relevance |

---

## Literature Evidence

For malignant renovascular hypertension, one publication was found:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1988765](https://pubmed.ncbi.nlm.nih.gov/1988765/) | 1991 | Diagnostic study | Medicine | Chromogranin A for diagnosing pheochromocytoma; not relevant to metoprolol therapy |

For chronic pulmonary heart disease (rank 9), the most relevant publications are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38587241](https://pubmed.ncbi.nlm.nih.gov/38587241/) | 2024 | RCT | N Engl J Med | Beta-blockers after myocardial infarction with preserved ejection fraction |
| [38762800](https://pubmed.ncbi.nlm.nih.gov/38762800/) | 2024 | RCT | JAMA | Bisoprolol in COPD at high risk of exacerbation (BICS); no benefit shown |
| [20413026](https://pubmed.ncbi.nlm.nih.gov/20413026/) | 2010 | Randomised crossover trial | J Am Coll Cardiol | Switching between beta-1 selective and nonselective beta-blockers in heart failure with COPD |
| [32000982](https://pubmed.ncbi.nlm.nih.gov/32000982/) | 2020 | Cohort | Am J Cardiol | Metoprolol vs carvedilol in geriatric patients with heart failure, COPD, diabetes and renal failure |
| [26844454](https://pubmed.ncbi.nlm.nih.gov/26844454/) | 2016 | Cohort | Medicine | Carvedilol, bisoprolol and metoprolol in coexisting heart failure and COPD (Taiwan database) |
| [33784233](https://pubmed.ncbi.nlm.nih.gov/33784233/) | 2021 | Secondary analysis of RCT | Ann Am Thorac Soc | Chronotropic index and COPD exacerbations in BLOCK COPD |
| [38771577](https://pubmed.ncbi.nlm.nih.gov/38771577/) | 2024 | Cohort | JAMA Netw Open | Beta-blocker use in COPD after acute myocardial infarction |
| [32250198](https://pubmed.ncbi.nlm.nih.gov/32250198/) | 2020 | Review | Expert Rev Respir Med | Practical recommendations for beta-blockers in COPD |
| [14520486](https://pubmed.ncbi.nlm.nih.gov/14520486/) | 2003 | Clinical study | Heart Vessels | Metoprolol used safely in coronary artery disease patients with COPD |
| [6851273](https://pubmed.ncbi.nlm.nih.gov/6851273/) | 1983 | Small clinical study | Clin Cardiol | Metoprolol effects on cardiac and pulmonary function in COPD |

---

## Canada Market Information

Metoprolol is marketed in Canada with 20 valid single-ingredient licences and no cancelled licences. Dosage form, manufacturer and approved indication text are not available in the data compiled for this report. The first five licences are listed below.

| DIN | Product Name |
|---------|------|
| 02350408 | METOPROLOL |
| 02315327 | RIVA-METOPROLOL-L |
| 00648027 | PRO-METOPROLOL-L |
| 02230803 | PMS-METOPROLOL-L |
| 00842656 | TEVA-METOPROLOL |

---

## Safety Considerations

Package insert warnings and contraindications are not available in the data compiled for this report. Please refer to the package insert for these.

**Contraindications from the knowledge graph (not label text):** The TxGNN knowledge graph links metoprolol to contraindications in several disease areas, including:
- Diabetes mellitus and diabetic ketoacidosis
- Liver disease, hepatic coma and hepatic encephalopathy
- Pancreatitis and gallbladder disease
- Systemic lupus erythematosus
- Psoriasis
- Myasthenia gravis and neuromuscular junction disease
- Pheochromocytoma
- Hypotensive disorders
- Gout and hyperuricaemia
- Anxiety, neurotic and dysthymic disorders
- Anuria
- Hyperparathyroidism and hypercalcaemia
- Potassium deficiency
- Neonatal jaundice

These are model-derived and should be verified against the label.

**Drug interactions:** The interaction screening completed and returned 100 interactions. The first 20 are shown in the data. Most are Moderate, including epinephrine, corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), bupropion, morphine, atropine, hyoscyamine, glycopyrronium, cimetidine, canagliflozin, dapagliflozin, chlorpropamide and calcium salts. Acetylsalicylic acid and magnesium oxide are Minor.

**Respiratory safety signal:** In the BLOCK COPD trial (NCT02587351), metoprolol did not reduce COPD exacerbations and increased exacerbations requiring hospitalisation. This is relevant for any pulmonary indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (malignant renovascular hypertension) rests on model prediction alone, with no trials and no relevant literature, so it sits at L5. The best-supported alternative, chronic pulmonary heart disease, is mostly tolerability data, and the pivotal trial suggested harm. The myocardial infarction subtypes are already covered by the approved indication and are not distinct repurposing opportunities.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Disease-specific clinical or mechanistic evidence for renovascular or malignant hypertension
- For chronic pulmonary heart disease, results from NCT06825728 and a review of the BLOCK COPD harm signal
- Dosage form and approved indication details for the Canadian licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

