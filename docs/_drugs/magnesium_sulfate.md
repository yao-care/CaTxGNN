---
layout: default
title: Magnesium Sulfate
parent: Model Prediction Only (L5)
nav_order: 571
evidence_level: L5
indication_count: 9
monitor_inn: "MAGNESIUM SULFATE"
predicted_indications: ["toxemia of pregnancy", "thrombotic disease", "pharyngitis", "nasal cavity disease", "psychotic disorder", "acute laryngopharyngitis", "headache disorder", "trigeminal autonomic cephalalgia", "treatment-refractory schizophrenia"]
last_modified_at: 2026-10-28
description: "Magnesium Sulfate: predicted new indication Toxemia of pregnancy (evidence level L5). Approved use: Not recorded in the local data"
---

# Magnesium Sulfate
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

## Magnesium Sulfate: Toxemia of pregnancy
{: .text-alpha }

## One-Sentence Summary

Magnesium sulfate is a widely used injectable drug. The TxGNN model (deep learning) predicts toxemia of pregnancy as a possible new indication.
The model predicts it may be effective for **toxemia of pregnancy**, which is essentially the same condition as pre-eclampsia. This is therefore closer to confirmation of a known use than to true repurposing.
Roughly **30 clinical trials** and **20 publications** were compiled, including 2 completed Phase 2/3 randomized trials. These trials mainly address dosing and duration rather than whether the drug works.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Toxemia of pregnancy |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 8 of 8) |
| Number of DINs | 8 (valid: 8) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Mechanistically, magnesium is generally described as an NMDA receptor antagonist and calcium channel blocker that promotes cerebral vasodilation, which may lower seizure risk. This is background pharmacology and was not confirmed from a source in the compiled data.

Toxemia of pregnancy is an older term for the pre-eclampsia/eclampsia spectrum. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Because the Canadian license records contain no indication text, this report cannot confirm that pre-eclampsia is an approved Canadian indication.

The trials and reviews in the data focus on optimizing use: low-dose versus standard regimens, postpartum duration, and dosing in obesity. This suggests the drug is already established in clinical practice for this condition. The open questions concern how best to use it, not whether it has any effect.

---

## Clinical Trial Evidence

Roughly 30 trials were retrieved. The 10 most relevant are listed below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02317146](https://clinicaltrials.gov/study/NCT02317146) | Phase 2/3 | Completed | 280 | Postpartum magnesium sulfate for 6 vs 24 hours in severe pre-eclampsia after less than 8 hours of pre-delivery treatment |
| [NCT02307201](https://clinicaltrials.gov/study/NCT02307201) | Phase 2/3 | Completed | 1114 | 24 hours vs no postpartum magnesium sulfate in severe pre-eclampsia after at least 8 hours of pre-delivery treatment (multicentre) |
| [NCT03164304](https://clinicaltrials.gov/study/NCT03164304) | Phase 4 | Completed | 222 | 1 g vs 2 g maintenance dose in severe pre-eclampsia |
| [NCT00004399](https://clinicaltrials.gov/study/NCT00004399) | N/A | Completed | 2000 | Nimodipine vs magnesium sulfate for preventing eclamptic seizures in severe pre-eclampsia |
| [NCT04501289](https://clinicaltrials.gov/study/NCT04501289) | N/A | Completed | 114 | Low-dose vs standard Pritchard regimen in severe pre-eclampsia/eclampsia |
| [NCT01408979](https://clinicaltrials.gov/study/NCT01408979) | Phase 4 | Completed | 120 | Short-course postpartum prophylaxis in severe pre-eclampsia |
| [NCT02091401](https://clinicaltrials.gov/study/NCT02091401) | Phase 4 | Completed | 200 | Repeat-bolus regimen (Springfusor pump) vs continuous infusion: serum levels and clinical outcomes |
| [NCT03318211](https://clinicaltrials.gov/study/NCT03318211) | Phase 4 | Unknown | 100 | Continuing vs stopping magnesium sulfate after delivery |
| [NCT02396030](https://clinicaltrials.gov/study/NCT02396030) | Phase 4 | Terminated | 62 | 1 g/h vs 2 g/h maintenance for eclampsia prevention; early termination limits conclusions |
| [NCT06486025](https://clinicaltrials.gov/study/NCT06486025) | Phase 1/2 | Unknown | 100 | Alternate dosing in overweight and obese women with pre-eclampsia |

An ongoing Phase 3 trial, [NCT07220902](https://clinicaltrials.gov/study/NCT07220902) (levetiracetam vs magnesium sulfate, n=1240), has not yet started recruiting.

---

## Literature Evidence

None of the retrieved publications is a randomized trial of magnesium sulfate itself. They are mainly reviews and pharmacokinetic studies.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32980358](https://pubmed.ncbi.nlm.nih.gov/32980358/) | 2022 | Review | Am J Obstet Gynecol | Eclampsia in the 21st century: incidence is far higher in low-resource countries |
| [38669914](https://pubmed.ncbi.nlm.nih.gov/38669914/) | 2024 | Review | Pregnancy Hypertens | Magnesium sulfate is superior to other anticonvulsants for recurrent seizures in eclampsia and is also indicated in pre-eclampsia with severe features |
| [36822712](https://pubmed.ncbi.nlm.nih.gov/36822712/) | 2023 | Review | Obstet Gynecol Clin North Am | IV and IM regimens are effective for seizure prevention; regimens can be tailored for low-resource settings |
| [37467840](https://pubmed.ncbi.nlm.nih.gov/37467840/) | 2023 | Review | Am J Obstet Gynecol | Reduces eclamptic seizure risk; no studies in late postpartum severe hypertension alone |
| [8879973](https://pubmed.ncbi.nlm.nih.gov/8879973/) | 1996 | Review | Drug Saf | Better than diazepam or phenytoin for preventing recurrent seizures in eclampsia |
| [10803454](https://pubmed.ncbi.nlm.nih.gov/10803454/) | 2000 | Review | Clin Pharmacokinet | Pharmacokinetic principles of IV and IM regimens |
| [38872116](https://pubmed.ncbi.nlm.nih.gov/38872116/) | 2024 | Pharmacokinetic study | BMC Pregnancy Childbirth | Population pharmacokinetics and dose optimization in a Chinese pre-eclampsia population |
| [32642964](https://pubmed.ncbi.nlm.nih.gov/32642964/) | 2020 | Pharmacokinetic study | Drugs R D | Population pharmacokinetic model and covariates in pre-eclampsia |

---

## Canada Market Information

Eight Canadian licences are listed, all in valid status. The licence records contain no dosage form or approved-indication text. Four are magnesium sulfate injection products.

| DIN | Product Name |
|---------|------|
| 02139499 | Magnesium Sulfate Injection, USP |
| 02513161 | Magnesium Sulfate Injection, BP 49.3% |
| 02542153 | Magnesium Sulfate in Water for Injection |
| 00392618 | Magnesium Sulfate Injection USP |

The other four licences (TIS-U-SOL Solution and three SmofKabiven products) appear to be multi-component products. They are not used here to describe the single-ingredient drug.

---

## Safety Considerations

- **Contraindications (knowledge-graph relations, not label text):** kidney disease, pyoureter, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, chronic diarrheal disease, appendicitis, atrioventricular block, hyperkalemic periodic paralysis, periodic paralysis, hypoaldosteronism, myotonia congenita, gastroparesis.
- **Drug Interactions:** 92 interactions are recorded. Major-level examples are dolutegravir, amikacin and bictegravir. Moderate-level examples include nifedipine, amlodipine, cisatracurium, ciprofloxacin, doxycycline, tetracycline, alendronic acid, risedronic acid, ibandronate, cholecalciferol, calcitriol, calcifediol and several corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone). Nifedipine is notable because it is commonly used alongside magnesium sulfate in pre-eclampsia care.

Warning and contraindication text from the Canadian package insert is not available. Please refer to the package insert for label safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Directly relevant randomized trials in severe pre-eclampsia support use of the drug, including two completed Phase 2/3 trials (L2). Fewer than two completed Phase 3 trials are present, so L1 is not met.
- The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, and label-level confirmation and mechanism data are missing.

**To proceed, the following is needed:**
- Canadian package insert text (indication, warnings, contraindications) to confirm the labelled use and safety.
- Mechanism-of-action data from a verified source.
- A monitoring plan covering serum magnesium levels, renal function, respiratory status and reflexes, plus review of interacting drugs (especially nifedipine and neuromuscular blockers).
- Dosing guidance for special populations (obesity, renal impairment) based on the ongoing and completed dosing trials.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

