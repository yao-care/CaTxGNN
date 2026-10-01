---
layout: default
title: Lurasidone
parent: Model Prediction Only (L5)
nav_order: 561
evidence_level: L5
indication_count: 10
---

# Lurasidone
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

# Lurasidone: From Atypical Antipsychotic to Manic Bipolar Affective Disorder

## One-Sentence Summary

Lurasidone is an atypical antipsychotic marketed in Canada under the brand name LATUDA and several generics.
The TxGNN model predicts it may be effective for **manic bipolar affective disorder**, with **15 registered clinical trials** and **20 publications** on bipolar disorder in the evidence pack.
Most of that evidence covers bipolar I depression and maintenance treatment, not acute mania.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 (see caveat in the conclusion) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source data. The reasoning below is based on general pharmacology. Lurasidone is an atypical antipsychotic. It antagonises D2, 5-HT2A and 5-HT7 receptors and is a partial agonist at 5-HT1A. This receptor profile is plausibly relevant to stabilising mood episodes in bipolar disorder.

The strongest direct evidence is for **bipolar I depression**, which the pack describes as an established use. Phase 3 placebo-controlled trials exist in adults and in children and adolescents. There is also a large Phase 3 study of lurasidone added to lithium or divalproex for preventing recurrence (965 participants). Lurasidone therefore already has a substantial evidence base in bipolar disorder, which makes the model's link to the bipolar spectrum credible.

The manic pole is less well supported. None of the trials in the pack tests lurasidone for acute mania. The one mania-specific study, an open-label paediatric trial (NCT01932541), was withdrawn with 0 participants. The very high TxGNN score is consistent with efficacy in the manic phase but does not prove it.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01358357](https://clinicaltrials.gov/study/NCT01358357) | Phase 3 | Completed | 965 | Randomized, double-blind, placebo-controlled study of lurasidone added to lithium or divalproex for preventing recurrence in bipolar I disorder. This is the largest direct RCT. |
| [NCT01986101](https://clinicaltrials.gov/study/NCT01986101) | Phase 3 | Completed | 525 | Randomized, double-blind, placebo-controlled study of lurasidone (SM-13496) in bipolar I depression |
| [NCT02046369](https://clinicaltrials.gov/study/NCT02046369) | Phase 3 | Completed | 350 | 6-week placebo-controlled study of flexibly dosed lurasidone in children and adolescents with bipolar I depression |
| [NCT01986114](https://clinicaltrials.gov/study/NCT01986114) | Phase 3 | Completed | 495 | Long-term efficacy and safety study of lurasidone (SM-13496) in bipolar I disorder |
| [NCT01575561](https://clinicaltrials.gov/study/NCT01575561) | Phase 3 | Completed | 377 | 12-week open-label extension of lurasidone added to lithium or divalproex. Supports long-term safety and tolerability but is uncontrolled. |
| [NCT02731612](https://clinicaltrials.gov/study/NCT02731612) | Phase 3 | Completed | 100 | 6-week placebo-controlled study of adjunctive lurasidone for cognition in euthymic bipolar patients (ELICE-BD) |
| [NCT02147379](https://clinicaltrials.gov/study/NCT02147379) | Phase 3 | Completed | 53 | Open-label randomized study of lurasidone versus treatment as usual for cognition in euthymic bipolar I patients |
| [NCT04383691](https://clinicaltrials.gov/study/NCT04383691) | Phase 3 | Terminated | 124 | 6-week placebo-controlled study in bipolar I depression. It was terminated early, which limits interpretation. |
| [NCT01932541](https://clinicaltrials.gov/study/NCT01932541) | Phase 4 | Withdrawn | 0 | Open-label study of Latuda for mania in children and adolescents aged 6–17. It was withdrawn with no participants, so it yields no data. |
| [NCT06433635](https://clinicaltrials.gov/study/NCT06433635) | Phase 4 | Active, not recruiting | 2726 | Pragmatic sequential randomized trial in bipolar depression comparing cariprazine, quetiapine, lurasidone and aripiprazole/escitalopram |

---

## Literature Evidence

None of the retrieved publications is a randomized trial. They are systematic reviews, meta-analyses, guidelines and narrative reviews. The abstracts in the pack are mostly truncated, so the findings below reflect scope only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [39557452](https://pubmed.ncbi.nlm.nih.gov/39557452/) | 2024 | Systematic review / dose-response meta-analysis | BMJ Ment Health | Examines the dose-response relationship of lurasidone in bipolar depression for efficacy, acceptability and metabolic/endocrine effects |
| [37595997](https://pubmed.ncbi.nlm.nih.gov/37595997/) | 2023 | Network meta-analysis | Lancet Psychiatry | Compares the efficacy and tolerability of drug treatments for acute bipolar depression in adults |
| [38487836](https://pubmed.ncbi.nlm.nih.gov/38487836/) | 2024 | Network meta-analysis | Eur Psychiatry | Compares five FDA-approved atypical antipsychotics, including lurasidone, in bipolar depression (16 RCTs, 7,234 patients) |
| [29536616](https://pubmed.ncbi.nlm.nih.gov/29536616/) | 2018 | Clinical practice guideline | Bipolar Disord | CANMAT/ISBD 2018 guidelines for managing bipolar disorder |
| [34599629](https://pubmed.ncbi.nlm.nih.gov/34599629/) | 2021 | Clinical practice guideline | Bipolar Disord | CANMAT/ISBD recommendations for bipolar disorder with mixed presentations |
| [33177610](https://pubmed.ncbi.nlm.nih.gov/33177610/) | 2021 | Systematic review / network meta-analysis | Mol Psychiatry | Compares mood stabilisers and antipsychotics for maintenance-phase bipolar disorder |
| [37815563](https://pubmed.ncbi.nlm.nih.gov/37815563/) | 2023 | Review | JAMA | Overview of the diagnosis and treatment of bipolar disorder |
| [38618207](https://pubmed.ncbi.nlm.nih.gov/38618207/) | 2024 | Network meta-analysis | EClinicalMedicine | Ranks the metabolic effects of antipsychotics and mood stabilisers in bipolar disorder |
| [36472471](https://pubmed.ncbi.nlm.nih.gov/36472471/) | 2022 | Review / treatment algorithm | J Child Adolesc Psychopharmacol | Psychopharmacological treatment algorithms for manic/mixed and depressive episodes in paediatric bipolar disorder |
| [24170243](https://pubmed.ncbi.nlm.nih.gov/24170243/) | 2014 | Commentary | Am J Psychiatry | "Lurasidone and bipolar disorder." No abstract is available |

---

## Canada Market Information

The pack lists 20 authorisations in total. It does not include dosage form, manufacturer or approved indication text for any of them. The five main entries are:

| DIN | Product Name |
|---------|------|
| 2413361 | LATUDA |
| 2522349 | NRA-LURASIDONE |
| 2504529 | TARO-LURASIDONE |
| 2514028 | AURO-LURASIDONE |
| 2505894 | PMS-LURASIDONE |

---

## Safety Considerations

Please refer to the package insert for safety information.

The pack does not include Health Canada warnings, contraindications or drug interaction data (the DDI query returned no results). For context, it contains literature on antipsychotic-related weight gain and metabolic effects (PMIDs 31952459 and 38618207) and two long-term open-label safety studies of lurasidone (NCT01914393 and NCT01575561).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several completed Phase 3 randomized trials support lurasidone in bipolar I disorder, and it is already established for bipolar I depression. That evidence does not cover acute mania, and the only mania-specific trial was withdrawn. The L1 rating therefore reflects bipolar disorder broadly, and manic-phase efficacy remains unproven.

The other nine predicted indications are L5 model predictions with no plausible mechanism and little or no supporting literature, so they are on **Hold**.

**To proceed, the following is needed:**
- The Health Canada package insert warnings, contraindications and drug interactions. This is a blocking gap for safety screening.
- Detailed mechanism-of-action data from DrugBank.
- Confirmation of the episode polarity and outcomes of the bipolar trials, especially NCT01358357, NCT02731612 and the truncated-title studies.
- Evidence specific to acute mania, such as a dedicated RCT or a subgroup analysis.
- The approved indication text and dosage forms for the Canadian licences.
- A metabolic monitoring plan.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

