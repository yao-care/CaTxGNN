---
layout: default
title: Ketamine
parent: Model Prediction Only (L5)
nav_order: 510
evidence_level: L5
indication_count: 1
---

# Ketamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Ketamine: From an Approved Anaesthetic/Analgesic Use to Headache Disorder

## One-Sentence Summary

Ketamine is an injectable drug with seven valid single-ingredient licences in Canada, but the data compiled for this report do not include the approved indication text.
The TxGNN model predicts it may be effective for **headache disorder**,
with **9 clinical trials** and **20 publications** compiled, including a completed Phase 3 trial and a Phase 3 trial still recruiting.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (Health Canada licence records contain no indication text) |
| Predicted New Indication | Headache disorder |
| TxGNN Prediction Score | 99.33% |
| Evidence Level | L1 (see note below) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 7 |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* Only one Phase 3 trial (THINK, NCT03081416) is confirmed as completed, and the other Phase 3 trial is still recruiting. Strictly under the L1 rule (≥2 completed Phase 3 RCTs), a more conservative grading of L2 would be defensible. The L1 grade is retained from the scoring data compiled for this report.

## Why is This Prediction Reasonable?

Ketamine is an NMDA receptor antagonist. Glutamate signalling and central sensitisation are implicated in migraine, cluster headache and other chronic headache disorders, including cortical spreading depression and trigeminovascular pain transmission. Blocking NMDA receptors may reduce central sensitisation and pain amplification, which gives a plausible biological basis for use in acute or refractory headache.

Detailed mechanism-of-action data were not available in the compiled records, so this reasoning rests on ketamine's well-known pharmacology rather than on a curated mechanism entry. Ketamine's analgesic effects at sub-dissociative doses further support the biological plausibility. The high TxGNN score (0.99) is consistent with this link.

An important caveat is that the evidence is heterogeneous across headache subtypes (migraine, cluster, tension-type and chronic daily headache), and the trials use different routes (intravenous, intranasal, oral) and comparators.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03081416](https://clinicaltrials.gov/study/NCT03081416) | Phase 3 | Completed | 80 | THINK trial: intranasal sub-dissociative ketamine vs standard therapy for primary headache in the emergency department (ED); randomised, single-blind, placebo-controlled |
| [NCT05306899](https://clinicaltrials.gov/study/NCT05306899) | Phase 3 | Recruiting | 56 | KetHead: multicentre, placebo-controlled RCT of high-dose IV ketamine infusion for chronic daily headache; no results yet |
| [NCT02657031](https://clinicaltrials.gov/study/NCT02657031) | Phase 4 | Completed | 54 | Low-dose ketamine vs prochlorperazine (Compazine) for headache in the ED; randomised, double-blind, multicentre |
| [NCT04814381](https://clinicaltrials.gov/study/NCT04814381) | Phase 4 | Completed | 93 | Single ketamine infusion combined with magnesium sulfate for refractory chronic cluster headache; combination design confounds attribution to ketamine alone |
| [NCT02697071](https://clinicaltrials.gov/study/NCT02697071) | N/A | Completed | 34 | Randomised, double-blind, placebo-controlled trial of sub-dissociative ketamine for acute migraine-type headache in the ED |
| [NCT03221569](https://clinicaltrials.gov/study/NCT03221569) | Phase 4 | Unknown | 60 | Sub-dissociative ketamine vs ketorolac for acute tension-type headache; status unknown, so reliability is uncertain |
| [NCT04179266](https://clinicaltrials.gov/study/NCT04179266) | Phase 1/2 | Completed | 23 | Proof-of-concept study of intranasal ketamine spray for chronic cluster headache; small and exploratory |
| [NCT04860713](https://clinicaltrials.gov/study/NCT04860713) | Phase 4 | Completed | 5 | Oral ketamine + aspirin vs rimegepant in the ED; only 5 participants and a multi-drug formulation, so very limited value |
| [NCT02403687](https://clinicaltrials.gov/study/NCT02403687) | N/A | Completed | 300 | PACE study: observational study of topical analgesics; not specific to headache, indirect relevance |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Guideline | Headache | American Headache Society 2025 update on parenteral drugs for acute migraine in the ED |
| [34703891](https://pubmed.ncbi.nlm.nih.gov/34703891/) | 2021 | Systematic review | J Dent Anesth Pain Med | Efficacy of ketamine for migraine and other primary headaches vs placebo and active comparators |
| [35356451](https://pubmed.ncbi.nlm.nih.gov/35356451/) | 2022 | Cohort (retrospective) | Front Neurol | IV lidocaine and ketamine infusions for inpatient headache disorders: efficacy, duration and safety |
| [36310189](https://pubmed.ncbi.nlm.nih.gov/36310189/) | 2023 | Systematic review / meta-analysis | J Neurol | Preventive treatments for refractory chronic cluster headache |
| [34919214](https://pubmed.ncbi.nlm.nih.gov/34919214/) | 2022 | Review | Drugs | Drug treatment of cluster headache, covering acute and preventive therapy |
| [39037675](https://pubmed.ncbi.nlm.nih.gov/39037675/) | 2024 | Review | CNS Drugs | Psychotropic drugs, including ketamine, re-emerging as headache medicines |
| [32189074](https://pubmed.ncbi.nlm.nih.gov/32189074/) | 2020 | Review | Curr Neurol Neurosci Rep | ED and inpatient management of headache in adults |
| [32410204](https://pubmed.ncbi.nlm.nih.gov/32410204/) | 2020 | Review | Curr Neurol Neurosci Rep | ED and inpatient management of headache in children and adolescents |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Rev Neurother | Pharmacotherapy update for trigeminal neuralgia; ketamine mentioned as a possible adjuvant |
| [35416105](https://pubmed.ncbi.nlm.nih.gov/35416105/) | 2022 | Review | Expert Opin Drug Saf | Long-term safety of ketamine and esketamine in depression (safety context) |

Several other publications in the compiled set concern ketamine in depression and are not directly relevant to headache.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02550458 | Ketamine Hydrochloride Injection, USP | Injection | Not available |
| 02535645 | Ketamine Injection, BP | Injection | Not available |
| 02246796 | Ketamine Hydrochloride Injection USP | Injection | Not available |
| 00224405 | Ketalar | Injection | Not available |
| 00224391 | Ketalar | Injection | Not available |

Seven licences are valid in total (all single-ingredient); the five above are shown. The dosage form is inferred from the product names, as the licence records do not list it.

## Safety Considerations

- **Disease contraindications (from a knowledge graph, not label text):** The TxGNN knowledge graph links ketamine to contraindication with hypertension and hypertensive disorders, stroke and cerebrovascular disorders, cerebral infarction, myocardial infarction, coronary thrombosis, coronary artery disease and myocardial ischaemia, ocular hypertension, intracranial hypertension and pseudotumor cerebri, respiratory failure, thyrotoxicosis/hyperthyroidism/Graves disease, hemoglobinopathy, delirium, and substance abuse/dependence. These should be confirmed against the Canadian product monograph.
- **Drug interactions:** 100 interactions were found. Moderate-level interactions include:
  - opioids and related drugs (morphine, liposomal morphine, diphenoxylate, opium)
  - cannabinoids (dronabinol, nabilone)
  - metoclopramide
  - sympathomimetics and stimulants (ephedrine, phentermine, sibutramine, fenfluramine, isometheptene, topical epinephrine)

  Interactions with atropine, amphotericin B, famotidine, omeprazole, potassium chloride, ondansetron and ursodeoxycholic acid are listed with an unknown severity level.

The cardiovascular and intracranial-pressure contraindications are particularly relevant for headache patients, who may have vascular risk factors or raised intracranial pressure as a cause of headache.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several randomised trials, including a completed Phase 3 trial (THINK) and a Phase 3 trial in progress (KetHead), directly test ketamine in headache, and the NMDA-antagonist mechanism is biologically plausible. However, the trials are small (5 to 93 participants), cover different headache subtypes and routes, and no results are summarised in the compiled data. The safety data are incomplete.

**To proceed, the following is needed:**
- Health Canada product monograph warnings and contraindications (not available in the compiled data), plus the approved indications and dosage forms for each DIN
- Results from the completed trials (THINK, NCT02657031, NCT02697071, NCT04814381) and the final KetHead results
- Selection of a target headache subtype (acute migraine in the ED, cluster headache or chronic daily headache), with the route and dose
- A cardiovascular, intracranial-pressure and abuse-potential screening plan, along with a review of the opioid, cannabinoid and sympathomimetic interactions
- Detailed mechanism-of-action data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

