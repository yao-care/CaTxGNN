---
layout: default
title: Mirtazapine
parent: Model Prediction Only (L5)
nav_order: 621
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Mirtazapine: predicted new indication Ohdo syndrome and variants (evidence level L5). Approved use: Unipolar depression, endogenous depression, major depressive disorder…"
monitor_inn: "MIRTAZAPINE"
predicted_indications: ["Ohdo syndrome and variants", "blepharophimosis - intellectual disability syndrome, Ohdo type", "benign paroxysmal torticollis of infancy"]
---

# Mirtazapine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Mirtazapine: From Major Depressive Disorder to Ohdo Syndrome and Variants
{: .text-alpha }

## One-Sentence Summary

Mirtazapine is an antidepressant originally used for depressive disorders (unipolar depression, endogenous depression, major depressive disorder) and anxiety disorder.
The TxGNN model predicts it may be effective for **Ohdo syndrome and variants**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the computational model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Unipolar depression, endogenous depression, major depressive disorder, anxiety disorder (from the knowledge graph; no approved indication text is available for the Canadian licences) |
| Predicted New Indication | Ohdo syndrome and variants |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, mirtazapine is an antidepressant that is generally described as acting through alpha-2 adrenergic, 5-HT2/5-HT3 and H1 receptor antagonism. Its efficacy in depressive disorders is established, but the data compiled for this report do not confirm this mechanism.

Ohdo syndrome (including KAT6B-related variants) is a rare genetic disorder of chromatin regulation, marked by intellectual disability and craniofacial features. No biological pathway connecting mirtazapine's receptor targets to the cause of this condition can be established from the available evidence. At most, any benefit would be symptomatic (for example sleep, appetite, mood or behaviour) and not disease-modifying.

The very high TxGNN score (99.42%) is a purely computational output and is not backed by any clinical or published evidence. It should be treated as a hypothesis only.

### Other Predicted Indications

| Rank | Predicted Indication | TxGNN Score | Trials / Publications | Comment |
|------|------|------|------|------|
| 2 | Blepharophimosis – intellectual disability syndrome, Ohdo type | 99.11% | 0 / 0 | Likely the same or a closely related disease node as rank 1, so the two predictions are probably not independent evidence. |
| 3 | Benign paroxysmal torticollis of infancy | 99.11% | 0 / 0 | Considered a migraine-spectrum condition, so a speculative serotonergic or antihistaminergic link is conceivable. The condition is self-limiting in infancy, a sedating antidepressant has an unfavourable risk-benefit profile at that age, and no paediatric safety data are available. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Mirtazapine has 20 valid single-ingredient licences in Canada (no combination products, none cancelled). Dosage form and approved indication text are not available in the data compiled for this report. Five main authorizations are listed below.

| DIN | Product Name |
|---------|------|
| 02248542 | REMERON RD |
| 02248543 | REMERON RD |
| 02248544 | REMERON RD |
| 02286629 | APO-MIRTAZAPINE |
| 02256126 | MYLAN-MIRTAZAPINE |

Other marketed products include AURO-MIRTAZAPINE (and OD), SANDOZ MIRTAZAPINE, PRO-MIRTAZAPINE, NRA-MIRTAZAPINE, TEVA-MIRTAZAPINE and generic MIRTAZAPINE.

---

## Safety Considerations

**Contraindication-related conditions (from the knowledge graph, not label text):**
Multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, hypotensive disorder, epilepsy, manic bipolar affective disorder, liver disease, gallbladder disease, impaired renal function, neutropenia, agranulocytosis, hypertriglyceridemia, obesity disorder, monogenic obesity, stroke and cerebrovascular disorder, cerebral infarction, ischemic stroke susceptibility, myocardial infarction, coronary thrombosis, hemoglobinopathy, serotonin syndrome, and drug-induced akathisia.

**Drug Interactions:** The interaction search returned 100 records in total; 20 are shown in the data compiled for this report. 

- **Major:** Bupropion, Lorcaserin, Dolasetron, Palonosetron
- **Moderate (examples):** Famotidine, Cimetidine, Clarithromycin, Levofloxacin, Morphine, Dexamethasone, Aprepitant, Loperamide, Dronabinol, Nabilone, Eliglustat, Obeticholic acid, and several bowel-preparation laxatives (bisacodyl, picosulfuric acid, sodium sulfate, polyethylene glycol with electrolytes)

Please refer to the package insert for official warnings and contraindications, as these were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is based only on a model score, with no clinical trials, no publications and no supported mechanistic link to Ohdo syndrome. The knowledge graph also lists several contraindicated conditions, and the lack of package insert data blocks safety screening.

**To proceed, the following is needed:**
- Mechanism of action data for mirtazapine (DrugBank), and a biological rationale connecting it to Ohdo syndrome
- Health Canada package insert warnings and contraindications
- Preclinical or clinical evidence, such as case reports or symptom-focused studies, in Ohdo syndrome
- Review of the three predictions for independence, since ranks 1 and 2 likely refer to the same condition
- Dosage form and approved indication details for the Canadian licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

