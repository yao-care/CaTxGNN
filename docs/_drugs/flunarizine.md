---
layout: default
title: Flunarizine
parent: Model Prediction Only (L5)
nav_order: 393
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Flunarizine: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the Health Canada license record (known main use: migra…"
---

# Flunarizine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Flunarizine: From Migraine Prophylaxis (Marketed) to Migraine Disorder

## One-Sentence Summary

Flunarizine is a calcium channel blocker that is marketed in Canada (one DIN), and its main clinical use is migraine prophylaxis in many countries.
The TxGNN model predicts it may be effective for **migraine disorder**, with a score of 99.1%.
The data compiled for this report include **14 clinical trials** and **20 publications**, but most are small, open-label, not yet recruiting, or of unknown status, and none reports results for flunarizine.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Health Canada license record (known main use: migraine prophylaxis in many countries) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.12% |
| Evidence Level | L1 per the system scoring; a conservative reading is lower, because no completed Phase 3 RCT is listed |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the record compiled for this report. The following relies on general pharmacological knowledge. Flunarizine is a calcium channel blocker with additional H1 antihistaminic and dopamine D2 antagonist activity. The pharmacology data also show that it acts on the T-type calcium channels Cav3.1, Cav3.2 and Cav3.3 (human) and on the D2 receptor (rat).

Blocking neuronal calcium entry is thought to reduce cortical spreading depression and neuronal hyperexcitability, both implicated in migraine. The relevant pharmacology data describe its main use as migraine prophylaxis, and it is not approved by the FDA. A 1991 review states that numerous controlled studies, including double-blind comparisons with placebo and other antimigraine drugs, found it effective for prophylaxis. Other reviews and guidelines list it among first-choice preventive drugs.

The Health Canada license record for the DIN has no indication text, so the "original indication" cannot be confirmed from Canadian data. The prediction therefore mostly reflects an established use abroad rather than a new one in Canada.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07354126](https://clinicaltrials.gov/study/NCT07354126) | N/A | Recruiting | 44 | Flunarizine vs propranolol in children aged 8-15, measured by PedMIDAS; no results |
| [NCT06162819](https://clinicaltrials.gov/study/NCT06162819) | N/A | Unknown | 84 | Flunarizine vs amitriptyline for migraine prophylaxis; no results |
| [NCT02639598](https://clinicaltrials.gov/study/NCT02639598) | Phase 4 | Completed | 62 | Flunarizine 10 mg/day vs topiramate 50 mg/day for chronic migraine prophylaxis |
| [NCT03712917](https://clinicaltrials.gov/study/NCT03712917) | N/A | Completed | 120 | Greater occipital nerve block vs topiramate vs flunarizine in episodic migraine |
| [NCT07655700](https://clinicaltrials.gov/study/NCT07655700) | Phase 4 | Not yet recruiting | 177 | Propranolol, flunarizine, and their combination for prophylaxis; no results |
| [NCT06499116](https://clinicaltrials.gov/study/NCT06499116) | Phase 4 | Not yet recruiting | 460 | Pragmatic comparison of amitriptyline, flunarizine, topiramate and propranolol in primary care |
| [NCT07751497](https://clinicaltrials.gov/study/NCT07751497) | Phase 2 | Not yet recruiting | 400 | Rimegepant vs flunarizine, non-inferiority, in vestibular migraine |
| [NCT00752466](https://clinicaltrials.gov/study/NCT00752466) | Phase 1 | Completed | 75 | Pharmacokinetic interaction of flunarizine with topiramate; no efficacy data |
| [NCT04766762](https://clinicaltrials.gov/study/NCT04766762) | N/A | Unknown | 96 | Acupuncture for migraine without aura; flunarizine is the usual treatment/comparator |
| [NCT07068815](https://clinicaltrials.gov/study/NCT07068815) | Phase 1 | Not yet recruiting | 60 | Fu's subcutaneous needling vs flunarizine in migraine without aura |

The 14 trials in the data include four more that are not listed above: an electro-acupuncture study, two mechanistic pain studies, and an alpha-lipoic acid add-on study. The list also omits a pulsed radiofrequency vs calcium channel blocker study in childhood migraine.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39365169](https://pubmed.ncbi.nlm.nih.gov/39365169/) | 2024 | Systematic review with economic model | Health Technol Assess | Compares effectiveness and cost-effectiveness of preventive drugs for chronic migraine |
| [39388181](https://pubmed.ncbi.nlm.nih.gov/39388181/) | 2024 | Network meta-analysis | JAMA Netw Open | Efficacy and safety of preventive medications in pediatric migraine |
| [42673559](https://pubmed.ncbi.nlm.nih.gov/42673559/) | 2026 | Systematic review | Neurology | AAN/AHS review of pharmacologic migraine prevention in adults |
| [41572863](https://pubmed.ncbi.nlm.nih.gov/41572863/) | 2026 | Review | Dtsch Arztebl Int | Drug and non-drug prophylaxis for frequent or severe migraine |
| [28752512](https://pubmed.ncbi.nlm.nih.gov/28752512/) | 2017 | Practice guideline | Acta Neurol Taiwan | Taiwan Headache Society consensus on preventive migraine treatment |
| [31413170](https://pubmed.ncbi.nlm.nih.gov/31413170/) | 2019 | Practice guideline | Neurology | AAN/AHS update on pediatric migraine prevention |
| [12390610](https://pubmed.ncbi.nlm.nih.gov/12390610/) | 2002 | RCT | Headache | 6-month randomized comparison of acupuncture vs flunarizine in migraine without aura |
| [30428122](https://pubmed.ncbi.nlm.nih.gov/30428122/) | 2019 | Controlled study | Acta Neurol Scand | Flunarizine plus supraorbital neurostimulation vs either alone for prophylaxis |
| [1889980](https://pubmed.ncbi.nlm.nih.gov/1889980/) | 1991 | Review | Headache | Controlled studies, including double-blind ones, found flunarizine effective for prophylaxis |
| [21049704](https://pubmed.ncbi.nlm.nih.gov/21049704/) | 2010 | Review | J Assoc Physicians India | Lists flunarizine among first-choice prophylactic drugs |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02246082 | FLUNARIZINE | Not recorded | Not recorded |

---

## Safety Considerations

- **Known adverse effects (general pharmacological knowledge, not from the Canadian label):** sedation, weight gain, depression, and extrapyramidal symptoms or parkinsonism. Extra caution is warranted in elderly patients and in those with a history of depression.
- **Drug Interactions:** The data list 4 pharmacology interaction entries, all describing targets rather than interacting drugs: D2 receptor, Cav3.1, Cav3.2 and Cav3.3. A Phase 1 study (NCT00752466) examined the pharmacokinetic interaction of flunarizine with topiramate.

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Flunarizine is used for migraine prophylaxis in many countries, and guidelines and reviews support it. The newer trials in the data are mostly small or open-label comparisons without results, and the Canadian license record has no indication or label information.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (the record is currently missing)
- The approved indication text, dosage form and manufacturer for DIN 02246082
- Verified mechanism of action data from DrugBank
- Results from the ongoing head-to-head trials, especially the larger primary-care comparison (NCT06499116)
- A monitoring plan for sedation, depression and extrapyramidal symptoms, especially in elderly patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

