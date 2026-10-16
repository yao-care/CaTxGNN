---
layout: default
title: Ramipril
parent: Model Prediction Only (L5)
nav_order: 792
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ramipril: predicted new indication Pulmonary hypertension with unclear multifactorial mechanism (evidence level L5). Approved use: Hypertension"
monitor_inn: "RAMIPRIL"
predicted_indications: ["pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant renovascular hypertension", "malignant hypertensive renal disease", "Braddock syndrome", "brain stem infarction", "Prinzmetal angina", "intracerebral hemorrhage", "ABri amyloidosis", "cerebral artery occlusion"]
---

# Ramipril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Ramipril: From Hypertension to Pulmonary Hypertension (Multifactorial / Unclear Mechanism)

## One-Sentence Summary

Ramipril is an ACE inhibitor originally used for hypertension and for reducing stroke and cerebrovascular risk.
The TxGNN model predicts it may be effective for **pulmonary hypertension with unclear multifactorial mechanism**,
but **no clinical trials and no publications** specific to this indication are currently available, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension; stroke and cerebrovascular disorders (the Health Canada licence records contain no indication text, so this comes from the knowledge-graph indication list) |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the compiled data. Based on known pharmacology, ramipril inhibits angiotensin-converting enzyme (ACE) and lowers angiotensin II, a molecule that constricts blood vessels and promotes vascular remodeling.

Systemic hypertension and pulmonary hypertension are both disorders of vascular tone and vessel-wall remodeling. Because the renin-angiotensin system may influence the pulmonary circulation as well, ACE inhibition could plausibly affect pulmonary vascular pressure. This link is hypothetical for the predicted indication: no trials or publications were found for it.

Indirect support exists for a closely related condition, **pulmonary hypertension owing to lung disease and/or hypoxia** (the second-ranked prediction, same score of 99.93%). A 1996 rat study (PMID 9200213) found that ramipril attenuated the effects of chronic hypoxia on pulmonary blood vessels. This is animal data only and does not establish benefit in humans.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked predicted indication.

For context, the closely related second-ranked prediction (pulmonary hypertension owing to lung disease and/or hypoxia) has one relevant preclinical paper:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9200213](https://pubmed.ncbi.nlm.nih.gov/9200213/) | 1996 | Preclinical (animal) | Physiological Research | In rats exposed to chronic hypoxia, ramipril (10 mg/kg daily) lowered baseline pulmonary perfusion pressure and attenuated hypoxia-induced changes in pulmonary vessels |

The other papers retrieved for that indication concern myocardial infarction, renal capillaries, cardiac remodeling or radiation necrosis, and are not relevant to pulmonary hypertension.

## Canada Market Information

Ramipril is marketed in Canada with 20 valid single-ingredient licences and no cancelled licences. Dosage form and approved indication text are not available in the compiled data. Five of the licences are listed below.

| DIN | Product Name |
|---------|------|
| 02221853 | ALTACE |
| 02251531 | APO-RAMIPRIL |
| 02331128 | JAMP-RAMIPRIL |
| 02310546 | TARO-RAMIPRIL |
| 02469073 | PHARMA-RAMIPRIL |

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (model-derived, not label text): kidney disease, liver disease, gallbladder disease, systemic lupus erythematosus, neutropenia and agranulocytosis, hereditary angioedema, hypotensive disorder, connective tissue disease (including scleroderma and systemic sclerosis), bone and cartilage disease, and renal artery obstruction.
- **Drug interactions**: 100 interactions were identified in total. Two are rated **Major**: potassium citrate and potassium bicarbonate (a risk of raised potassium is the usual concern with ACE inhibitors). The others in the retrieved list are rated Moderate, including corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), acetylsalicylic acid, morphine, bupropion, and several diabetes drugs (metformin, glimepiride, chlorpropamide, alogliptin, and SGLT2 inhibitors canagliflozin, dapagliflozin and empagliflozin).
- Package insert warnings and contraindications were not available. Please refer to the package insert for authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (99.93%), but the evidence is model-only (L5): no clinical trials or literature support this specific indication. The nearest support is a single animal study in hypoxic pulmonary hypertension. Because ramipril lowers blood pressure, its safety in pulmonary hypertension patients is also unestablished.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- A structured literature search for ACE inhibitors in human pulmonary hypertension, and a check of registries for any trials
- Further preclinical or small exploratory clinical evidence, particularly in hypoxia-related pulmonary hypertension
- A blood-pressure and renal safety assessment for this patient population

**Other predicted indications (for reference):**

| Rank | Predicted Indication | Score | Evidence Level | Note |
|------|------|------|------|------|
| 2 | Pulmonary hypertension owing to lung disease and/or hypoxia | 99.93% | L4 | Indirect animal support (PMID 9200213) |
| 3 | Malignant renovascular hypertension | 99.93% | L5 | Renal safety concern in bilateral renal artery stenosis |
| 4 | Malignant hypertensive renal disease | 99.93% | L5 | Close to the existing hypertension indication |
| 5 | Braddock syndrome | 99.91% | L5 | No mechanistic rationale found |
| 6 | Brain stem infarction | 99.89% | L5 | Plausible given existing stroke-risk use |
| 7 | Prinzmetal angina | 99.83% | L5 | The one retrieved paper does not evaluate ramipril |
| 8 | Intracerebral haemorrhage | 99.82% | L4 | Indirect animal data only; acute-setting safety unestablished |
| 9 | ABri amyloidosis | 99.79% | L5 | No mechanistic rationale found |
| 10 | Cerebral artery occlusion | 99.74% | L4 | One small human cerebral blood flow study (PMID 8797135) and mixed animal results; marked "Research Question" |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

