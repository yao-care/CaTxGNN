---
layout: default
title: Losartan
parent: Model Prediction Only (L5)
nav_order: 561
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-13
description: "Losartan: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension, diabetic nephropathy"
---

# Losartan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Losartan: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Losartan is an angiotensin II receptor blocker originally used to treat hypertension and diabetic nephropathy.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but there are currently **0 clinical trials** and only **1 publication** (a 2019 animal model study) supporting this direction, so the evidence is at the model-prediction stage.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, diabetic nephropathy (the Canadian licence records contain no indication text) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, losartan is an angiotensin II type 1 (AT1) receptor blocker. Its efficacy in hypertension and diabetic nephropathy is established, and mechanistically it may be applicable to malignant hypertensive renal disease.

Malignant hypertensive kidney injury is closely tied to over-activation of the renin-angiotensin system. A 2019 rat study of malignant hypertensive nephrosclerosis implicated angiotensin II and NF-κB signalling in the pathology. Blocking the AT1 receptor is therefore biologically plausible.

However, this link rests on a single animal study. No human data or clinical trials exist for this specific indication, so the prediction should be treated as a hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30809002](https://pubmed.ncbi.nlm.nih.gov/30809002/) | 2019 | Preclinical animal model | Hypertension Research | In a rat model of malignant hypertensive nephrosclerosis, angiotensin II and the NF-κB system played a pathogenic role in kidney injury |

## Canada Market Information

Losartan has 20 valid single-ingredient authorisations in Canada, with no cancelled licences. The records compiled for this report do not include dosage form or approved indication text. The first five are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02403323 | AURO-LOSARTAN | Not listed | Not listed |
| 02182815 | COZAAR | Not listed | Not listed |
| 02309750 | PMS-LOSARTAN | Not listed | Not listed |
| 02403358 | AURO-LOSARTAN | Not listed | Not listed |
| 02388804 | LOSARTAN | Not listed | Not listed |

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these are graph-derived associations, not package insert text): pancreatitis, liver disease, gallbladder disease, systemic lupus erythematosus, potassium deficiency, diabetes mellitus, diabetic ketoacidosis, hypotensive disorder, hyperparathyroidism, hepatic coma and encephalopathy, neonatal jaundice, anuria, gout, hypercalcaemia, nephrocalcinosis, renal artery obstruction and impaired renal function. Several of these reflect contraindications of related drug classes, so they should be verified against the Canadian label.
- **Drug Interactions** (100 interactions identified, 20 shown in the data compiled):
  - **Major:** potassium citrate and potassium bicarbonate (risk of hyperkalaemia).
  - **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), insulins (aspart, glargine, isophane), acetylsalicylic acid, morphine, bupropion, aprepitant, dronabinol, picosulfuric acid and polyethylene glycol with electrolytes.
- Caution is warranted in renal artery stenosis, where ARBs can precipitate acute kidney injury. This is particularly relevant to malignant hypertension with renal involvement.

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.73%), and the mechanism is biologically plausible. However, the only supporting evidence is one animal study, with no clinical trials or human data. Losartan is already widely marketed and its general safety profile is well known, but this does not substitute for evidence in this indication.

**To proceed, the following is needed:**
- Human clinical or observational data on ARBs in malignant hypertensive renal disease
- Mechanism of action data (MOA)
- Health Canada package insert warnings and contraindications, including approved indication text, dosage forms and manufacturers
- A safety plan for renal function and potassium monitoring, given the renal artery and hyperkalaemia risks

---

### Other Predicted Indications (for reference)

| Rank | Predicted Indication | Score | Evidence Level | Recommendation | Note |
|---|---|---|---|---|---|
| 2 | Malignant renovascular hypertension | 99.73% | L4 | Hold | One case report (Takayasu's arteritis, enalapril plus losartan) and a rat methods chapter; no controlled human data |
| 3 | Pulmonary hypertension owing to lung disease and/or hypoxia | 99.71% | L4 | Hold | Indirect and mixed evidence; losartan abolished intermittent-hypoxia oxidative stress in a small human study but did not affect altitude diuresis or mountain sickness; many retrieved papers are off-topic |
| 4 | Pulmonary hypertension with unclear multifactorial mechanism | 99.71% | L5 | Hold | Prediction only |
| 5 | Braddock syndrome | 99.61% | L5 | Hold | Prediction only |
| 6 | Prinzmetal angina | 99.45% | L5 | Hold | Prediction only; calcium channel blockers and nitrates are the mainstay |
| 7 | Autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome | 99.39% | L5 | Hold | Prediction only |
| 8 | Brain small vessel disease 1 with or without ocular anomalies | 99.37% | L4 | Research Question | Indirect evidence (TREAT-SVDs trial of blood-pressure-lowering agents, ARB reviews in Marfan syndrome, mouse studies); no trial matched to this disease |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

