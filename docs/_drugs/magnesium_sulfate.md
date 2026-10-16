---
layout: default
title: Magnesium Sulfate
parent: Model Prediction Only (L5)
nav_order: 571
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Magnesium Sulfate: predicted new indication Preeclampsia/eclampsia (evidence level L5). Approved use: Constipation"
---

# Magnesium Sulfate
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

# Magnesium Sulfate: From Constipation and Pre-eclampsia to Preeclampsia/Eclampsia (Indication Confirmation)

## One-Sentence Summary

Magnesium sulfate is an established medicine used for constipation and for preventing seizures in pre-eclampsia. The TxGNN model's top prediction is **preeclampsia/eclampsia**, which is already an original indication rather than a true new use. The evidence is deep, with **29 clinical trials** and **20 publications** listed for this prediction. The more genuinely new directions are **headache disorder** (including acute migraine) and **postoperative sore throat (pharyngitis)**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Constipation; severe, mild and unspecified pre-eclampsia (the Canadian licence records carry no indication text) |
| Predicted New Indication | Preeclampsia/eclampsia (rank 1; already an original indication) |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L1 (for the top prediction) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Proceed with Guardrails |

For true repurposing, the most promising predictions are headache disorder (score 99.36%, L1, Proceed with Guardrails) and pharyngitis (score 99.61%, L2, Proceed with Guardrails). The sections below focus on the top-ranked prediction, as requested by the standard format, and note these alternatives where relevant.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, magnesium acts as an NMDA receptor antagonist and a calcium channel blocker, and it promotes cerebral vasodilation. These actions are thought to underlie its anticonvulsant effect and its ability to prevent eclamptic seizures.

The top prediction (preeclampsia/eclampsia) and the second (toxemia of pregnancy, an older term for the same condition) match the drug's existing pre-eclampsia indications. They show the model recovers known uses well, but they are not repurposing discoveries. The more novel signals come from the same mechanisms:

- **Headache/migraine:** Low magnesium has been linked to migraine, and NMDA antagonism may reduce neuronal excitability.
- **Postoperative sore throat:** Topical routes (gargle, nebulization, spray) may reduce peripheral nociception.

---

## Clinical Trial Evidence

Up to 10 of the most relevant trials for preeclampsia/eclampsia:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02317146](https://clinicaltrials.gov/study/NCT02317146) | Phase 2/3 | Completed | 280 | Postpartum magnesium sulfate for 6 vs 24 hours in severe preeclampsia |
| [NCT03164304](https://clinicaltrials.gov/study/NCT03164304) | Phase 4 | Completed | 222 | 1 g vs 2 g IV maintenance dose in severe pre-eclampsia |
| [NCT00004399](https://clinicaltrials.gov/study/NCT00004399) | N/A | Completed | 2000 | Nimodipine vs magnesium sulfate for preventing eclamptic seizures |
| [NCT04501289](https://clinicaltrials.gov/study/NCT04501289) | N/A | Completed | 114 | Low-dose vs standard Pritchard regimen |
| [NCT06486025](https://clinicaltrials.gov/study/NCT06486025) | Phase 1/2 | Unknown | 100 | Alternate dosing in overweight and obese women |
| [NCT03318211](https://clinicaltrials.gov/study/NCT03318211) | Phase 4 | Unknown | 100 | Continuing vs stopping magnesium after delivery |
| [NCT02396030](https://clinicaltrials.gov/study/NCT02396030) | Phase 4 | Terminated | 62 | 1 g/h vs 2 g/h maintenance dose for eclampsia prevention |
| [NCT02307201](https://clinicaltrials.gov/study/NCT02307201) | Phase 2/3 | Completed | 1114 | Postpartum magnesium for 24 hours vs none after more than 8 hours of pre-delivery treatment |
| [NCT07220902](https://clinicaltrials.gov/study/NCT07220902) | Phase 3 | Not yet recruiting | 1240 | Levetiracetam vs magnesium sulfate for eclamptic seizure prevention (equivalence design) |
| [NCT02091401](https://clinicaltrials.gov/study/NCT02091401) | Phase 4 | Completed | 200 | Repeat-bolus pump regimen vs continuous IV regimen, with serum magnesium levels |

Most of these trials address dose, duration and delivery method rather than whether magnesium works at all. Its efficacy for this indication is already well established.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9794688](https://pubmed.ncbi.nlm.nih.gov/9794688/) | 1998 | Review | Obstetrics and Gynecology | Efficacy, benefits and risks of magnesium sulfate seizure prophylaxis in preeclampsia and eclampsia |
| [2288560](https://pubmed.ncbi.nlm.nih.gov/2288560/) | 1990 | Review | Am J Obstet Gynecol | Magnesium sulfate described as the ideal anticonvulsant; efficacy and safety documented over 60 years |
| [32980358](https://pubmed.ncbi.nlm.nih.gov/32980358/) | 2022 | Review | Am J Obstet Gynecol | Eclampsia in the 21st century: incidence and outcomes |
| [10803454](https://pubmed.ncbi.nlm.nih.gov/10803454/) | 2000 | Review | Clin Pharmacokinet | Pharmacokinetic principles of magnesium sulfate regimens in eclampsia and pre-eclampsia |
| [38669914](https://pubmed.ncbi.nlm.nih.gov/38669914/) | 2024 | Review | Pregnancy Hypertension | Magnesium sulfate superior to other anticonvulsants for recurrent convulsions; broad indications in preeclampsia |
| [36822712](https://pubmed.ncbi.nlm.nih.gov/36822712/) | 2023 | Review | Obstet Gynecol Clin North Am | Regimens in high-income and low/middle-income countries |
| [8879973](https://pubmed.ncbi.nlm.nih.gov/8879973/) | 1996 | Review | Drug Safety | Magnesium sulfate better than diazepam or phenytoin for preventing recurrent seizures in eclampsia |
| [23282276](https://pubmed.ncbi.nlm.nih.gov/23282276/) | 2012 | Guideline | Rev Med Inst Mex Seguro Soc | Clinical guideline on preeclampsia-eclampsia |
| [38872116](https://pubmed.ncbi.nlm.nih.gov/38872116/) | 2024 | Pharmacokinetic study | BMC Pregnancy Childbirth | Population pharmacokinetics and dose optimization in a Chinese preeclampsia population |
| [17441885](https://pubmed.ncbi.nlm.nih.gov/17441885/) | 2007 | Cohort | J Obstet Gynaecol Res | Ionized and total magnesium levels during therapy in severe preeclampsia-eclampsia |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02139499 | Magnesium Sulfate Injection, USP | Not listed | Not listed |
| 02513161 | Magnesium Sulfate Injection, BP 49.3% | Not listed | Not listed |
| 02542153 | Magnesium Sulfate in Water for Injection | Not listed | Not listed |
| 00392618 | Magnesium Sulfate Injection USP | Not listed | Not listed |
| 00800007 | Tis-U-Sol Solution | Not listed | Not listed |

A total of 8 valid single-ingredient licences exist; the other three are SmofKabiven parenteral nutrition products (DINs 02456206, 02501813, 02440695), which contain magnesium sulfate as a component.

---

## Safety Considerations

- **Disease-level cautions (from the knowledge graph, not label text):** Kidney disease, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, chronic diarrheal disease, appendicitis, atrioventricular block, hyperkalemic periodic paralysis, periodic paralysis, hypoaldosteronism, myotonia congenita, gastroparesis, and pyoureter are flagged as contraindication edges.
- **Drug Interactions:** 92 interactions were identified. Major ones include dolutegravir, amikacin and bictegravir. Moderate ones include nifedipine, amlodipine, cisatracurium, doxycycline, tetracycline, ciprofloxacin, bisphosphonates (alendronic acid, risedronic acid, ibandronate), corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone), and vitamin D analogues (cholecalciferol, calcifediol, calcitriol).
- **Monitoring:** Watch for magnesium toxicity (reflexes, respiratory rate, urine output, serum level), and adjust dosing in renal impairment and obesity.

For label warnings and contraindications, please refer to the package insert, since these were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Preeclampsia/eclampsia is an already-established use of magnesium sulfate, supported by many randomized trials and extensive literature, so the evidence is strong (L1). It is a confirmation of an existing indication rather than a new repurposing opportunity.
- Among genuinely new directions, headache/migraine (a completed Phase 3 placebo-controlled trial, NCT05967442) and postoperative sore throat (a 2026 meta-analysis supporting nebulized magnesium) are the most promising. Both are rated Proceed with Guardrails.
- Trigeminal autonomic cephalalgia and thrombotic disease are Research Questions; psychotic disorder, nasal cavity disease, acute laryngopharyngitis and treatment-refractory schizophrenia should be held for lack of direct evidence.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications, dosage forms and approved indication text (a blocking gap for safety screening).
- Detailed mechanism of action data (MOA).
- Published results of the Phase 3 migraine trial (NCT05967442) to confirm efficacy.
- Larger, multi-centre trials for postoperative sore throat to confirm optimal dose and route; restrict the indication to postoperative or intubation-related sore throat, not infectious pharyngitis.
- A safety monitoring plan covering renal impairment, obesity and the interaction list above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

