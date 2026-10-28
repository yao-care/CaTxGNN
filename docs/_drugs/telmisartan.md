---
layout: default
title: Telmisartan
parent: Model Prediction Only (L5)
nav_order: 885
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Telmisartan: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Hypertension"
monitor_inn: "TELMISARTAN"
predicted_indications: ["Prinzmetal angina", "brain stem infarction", "ABri amyloidosis", "cerebral artery occlusion", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "intracerebral hemorrhage", "Braddock syndrome"]
---

# Telmisartan
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

## Telmisartan: From Hypertension to Prinzmetal Angina
{: .text-alpha }

## One-Sentence Summary

Telmisartan is an angiotensin receptor blocker originally used to treat hypertension and to reduce stroke and cerebral infarction risk.
The TxGNN model predicts it may be effective for **Prinzmetal angina** (top-ranked prediction, score 0.9998), but **no clinical trials or publications** currently support this specific prediction.
Among the other top-10 predictions, the best-supported is **intracerebral hemorrhage** (a Phase 3 combination-therapy trial and a 2026 NEJM publication), followed by **cerebral artery occlusion** (mainly preclinical evidence).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension; stroke and cerebral infarction risk reduction (approved indication text is not available in the Canadian license records) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | Marketed (valid licenses on record: at least 20) |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, telmisartan blocks the angiotensin II type 1 (AT1) receptor and is also a partial PPAR-gamma agonist. These actions could plausibly improve endothelial function and reduce vasospasm, which is relevant to Prinzmetal (vasospastic) angina.

This link is a hypothesis only. No trials or literature were found for Prinzmetal angina, so the prediction rests on the model score and mechanistic plausibility.

Other predictions in the top 10 show different levels of support:

- **Intracerebral hemorrhage (score 0.9993, L2):** Blood pressure lowering is the main mechanism for preventing recurrent hemorrhage. Telmisartan is a component of the low-dose triple-pill strategy tested in TRIDENT. Its independent contribution cannot be separated from the combination.
- **Cerebral artery occlusion (score 0.9995, L2 with caveats):** Rodent ischemia models show reduced infarct volume, oxidative stress and inflammation. Direct clinical evidence in acute occlusion is lacking.
- **Brain stem infarction, malignant renovascular hypertension and malignant hypertensive renal disease:** These are largely restatements of, or subtypes of, existing indications, with no condition-specific evidence.
- **Pulmonary hypertension (two entries) and the rare conditions ABri amyloidosis and Braddock syndrome:** Evidence is absent or only indirect.

---

## Clinical Trial Evidence

No clinical trials are registered for Prinzmetal angina (the top-ranked prediction).

The following trials are relevant to the better-supported predictions (cerebral artery occlusion and intracerebral hemorrhage):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Phase 3 | Completed | 1671 | TRIDENT: low-dose triple-pill BP-lowering strategy for secondary prevention after intracerebral hemorrhage. The effect is of the combination, not telmisartan alone. |
| [NCT01075698](https://clinicaltrials.gov/study/NCT01075698) | Phase 4 | Completed | 1228 | Open-label PROBE study of telmisartan vs ordinary therapy in high-risk hypertensive patients, assessing biomarkers and cardiovascular events. Results not shown. |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | NA | Terminated | 4 | TRIDENT MRI sub-study. Too small to inform efficacy. |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Terminated | 1 | TRIDENT cognitive sub-study. No usable efficacy data. |

---

## Literature Evidence

No literature is available for Prinzmetal angina. The table below covers the better-supported predictions (cerebral artery occlusion and intracerebral hemorrhage).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42019018](https://pubmed.ncbi.nlm.nih.gov/42019018/) | 2026 | RCT (combination therapy) | N Engl J Med | Three low-dose antihypertensives in a single pill after intracerebral hemorrhage. Appears to be the main TRIDENT report. Outcomes are not shown in the data compiled. |
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | Trial design | Int J Stroke | TRIDENT rationale, design and progress. |
| [24636673](https://pubmed.ncbi.nlm.nih.gov/24636673/) | 2014 | Post-hoc RCT analysis | Int J Stroke | Ischemic and hemorrhagic recurrence rates by race-ethnic group in the PRoFESS secondary stroke prevention trial. |
| [17538008](https://pubmed.ncbi.nlm.nih.gov/17538008/) | 2007 | Preclinical | J Pharmacol Exp Ther | AT1 blockade with telmisartan reduced apoptosis, inflammation and oxidative stress in rats with intracerebral hemorrhage. |
| [19604102](https://pubmed.ncbi.nlm.nih.gov/19604102/) | 2009 | Preclinical | J Neurotrauma | Telmisartan reduced cerebral infarct volume and peri-infarct cPLA2 in rat MCAO. |
| [21901125](https://pubmed.ncbi.nlm.nih.gov/21901125/) | 2011 | Preclinical | PLoS One | Telmisartan, ramipril and their combination in rat stroke prevention and neuroprotection models. |
| [24650592](https://pubmed.ncbi.nlm.nih.gov/24650592/) | 2014 | Preclinical | Pharmacol Biochem Behav | Non-hypotensive telmisartan plus nimodipine showed synergistic neuroprotection in cerebral ischemia. |
| [20498620](https://pubmed.ncbi.nlm.nih.gov/20498620/) | 2010 | Preclinical | J Hypertens | Low-dose telmisartan prevented ischemic brain damage via PPAR-gamma activation in diabetic mice. |
| [27078703](https://pubmed.ncbi.nlm.nih.gov/27078703/) | 2016 | Preclinical | Neurol Res | Telmisartan reduced oxidative stress and subarachnoid haemorrhage-induced cerebral vasospasm. |
| [41341617](https://pubmed.ncbi.nlm.nih.gov/41341617/) | 2025 | Preclinical | Toxicol Rep | Telmisartan attenuated cerebral ischemia-reperfusion neurotoxicity via Nrf2/HO-1 modulation. |

---

## Canada Market Information

Telmisartan has 20 valid single-ingredient authorizations in Canada. Dosage form and approved indication text are not available in the records compiled. The first five are listed below.

| DIN | Product Name |
|---------|------|
| 02240770 | MICARDIS 80MG TAB |
| 02484544 | AG-TELMISARTAN |
| 02320177 | TEVA-TELMISARTAN |
| 02320185 | TEVA-TELMISARTAN |
| 02375966 | SANDOZ TELMISARTAN |

---

## Safety Considerations

- **Disease-related cautions (from the knowledge graph, not label text):** Telmisartan is flagged as contraindicated or to be used with caution in conditions including liver failure, kidney disease, anuria, renal artery obstruction, hypotensive disorder, potassium deficiency, diabetes mellitus and diabetic ketoacidosis, gout, hypercalcemia, systemic lupus erythematosus, pancreatitis, gallbladder disease, and cholestasis.
- **Drug Interactions:** 100 interactions were identified. Major interactions include **potassium citrate** and **potassium bicarbonate** (risk of hyperkalaemia). Moderate interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), insulin and exenatide, acetylsalicylic acid, morphine, bupropion, dronabinol, and bowel-preparation agents.
- **Renovascular disease:** ARBs can cause acute renal function decline in bilateral renal artery stenosis. This is relevant to the malignant renovascular hypertension prediction.

Please refer to the package insert for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, Prinzmetal angina, rests on a model score and mechanistic plausibility alone (L5), with no trials or literature. Telmisartan is already widely marketed in Canada, so access is not a barrier. The more promising direction is secondary prevention after intracerebral hemorrhage (Phase 3 TRIDENT trial, completed). That trial tests a three-drug combination, so telmisartan's own contribution is unknown.

**To proceed, the following is needed:**
- A literature and trial search specific to telmisartan in vasospastic (Prinzmetal) angina
- The TRIDENT primary results (PMID 42019018), plus analysis of telmisartan's contribution within the triple pill
- Mechanism of action data (MOA) in the data set
- Health Canada package insert warnings and contraindications, to complete the safety screening
- Renal and potassium safety monitoring plans for any new-indication population
- Approved indication text and dosage forms for the Canadian DINs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

