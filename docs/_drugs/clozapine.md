---
layout: default
title: Clozapine
parent: Model Prediction Only (L5)
nav_order: 218
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-03
monitor_inn: "CLOZAPINE"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "trichotillomania", "schizophreniform disorder", "bipolar disorder", "major affective disorder", "attention deficit-hyperactivity disorder", "attention deficit hyperactivity disorder, inattentive type", "Malan overgrowth syndrome"]
description: "Clozapine: predicted new indication Manic bipolar affective disorder (evidence level L5). Approved use: Not recorded in the local data"
---

# Clozapine
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

## Clozapine: Manic bipolar affective disorder
{: .text-alpha }

## One-Sentence Summary

Clozapine is an atypical antipsychotic that is currently marketed in Canada.
The TxGNN model predicts it may be effective for **manic bipolar affective disorder**, particularly treatment-resistant mania.
The data compiled for this report include **1 completed Phase 2 double-blind trial** for this condition and a **systematic review and meta-analysis of clozapine in bipolar disorder**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 17 of 17) |
| Number of DINs | 17 (valid: 17) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Clozapine is known to act on many receptors, including dopamine D2/D4, serotonin 5-HT2A, muscarinic and adrenergic receptors. This broad profile plausibly contributes to antimanic and mood-stabilizing effects.

Some patients with mania do not respond adequately to conventional treatment or cannot tolerate it. The completed Phase 2 trial was designed to test clozapine in this setting. A systematic review and meta-analysis of clozapine in bipolar disorder supports the same direction.

The evidence is still limited. The Phase 2 trial was small (42 participants), and no completed Phase 3 trial of mania specifically is listed. Clozapine's serious safety risks make careful patient selection and monitoring essential.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00029458](https://clinicaltrials.gov/study/NCT00029458) | Phase 2 | Completed | 42 | Double-blind study of clozapine safety and efficacy in the manic phase of bipolar disorder, in patients who do not respond to or cannot tolerate conventional treatment |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32182485](https://pubmed.ncbi.nlm.nih.gov/32182485/) | 2020 | Systematic review/Meta-analysis | J Psychiatr Res | Assesses clinical efficacy of clozapine in bipolar disorder and its adverse-effect profile |
| [25346322](https://pubmed.ncbi.nlm.nih.gov/25346322/) | 2015 | Systematic review | Bipolar Disord | Evaluates efficacy and safety of clozapine in treatment-resistant bipolar disorder |
| [41192460](https://pubmed.ncbi.nlm.nih.gov/41192460/) | 2025 | Cohort/Real-world effectiveness | Lancet Psychiatry | Nationwide and meta-analytic comparison of clozapine effectiveness and safety across psychiatric disorders versus other antipsychotics |
| [33719158](https://pubmed.ncbi.nlm.nih.gov/33719158/) | 2021 | Review | Bipolar Disord | Overview of what is known about clozapine in bipolar disorder and future directions |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Review | Acta Psychiatr Scand | Evidence-based options for managing a manic episode, including mood stabilizer and antipsychotic choice |
| [16432528](https://pubmed.ncbi.nlm.nih.gov/16432528/) | 2006 | Review | Mol Psychiatry | Treatment-resistant bipolar disorder: inadequate response remains common despite many validated treatments |
| [11280956](https://pubmed.ncbi.nlm.nih.gov/11280956/) | 2001 | Review | Bull Menninger Clin | Treatment-resistant bipolar disorder; newer options rest largely on case reports and series |
| [41262335](https://pubmed.ncbi.nlm.nih.gov/41262335/) | 2025 | Model-informed dosing study | Drug Des Devel Ther | Clozapine drug interactions and individualized dosing in bipolar disorder |
| [10682225](https://pubmed.ncbi.nlm.nih.gov/10682225/) | 2000 | Case series | Clin Neuropharmacol | 36 patients given combined ECT and clozapine; 67% benefited and the combination was mostly well tolerated |
| [26407790](https://pubmed.ncbi.nlm.nih.gov/26407790/) | 2015 | Meta-analysis (safety) | World Psychiatry | Prevalence of metabolic syndrome in people with severe mental illness, relevant to metabolic monitoring |

## Canada Market Information

Health Canada records list 17 valid single-ingredient clozapine licences (no cancelled licences). Five are shown below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00894737 | CLOZARIL | Not recorded | Not recorded |
| 00894745 | CLOZARIL | Not recorded | Not recorded |
| 02490668 | CLOZARIL | Not recorded | Not recorded |
| 02490676 | CLOZARIL | Not recorded | Not recorded |
| 02248035 | AA-CLOZAPINE | Not recorded | Not recorded |

## Safety Considerations

- **Drug Interactions**: The interaction screen completed with 100 interacting drugs found. Major-level interactions include:
  - bupropion
  - morphine
  - potassium citrate

  Moderate-level interactions include:
  - antidiabetic agents (metformin, pioglitazone, alogliptin, acarbose, canagliflozin, chlorpropamide, albiglutide)
  - anticholinergic or gut-slowing agents (atropine, hyoscyamine, glycopyrronium, loperamide)
  - acid-suppressing agents (omeprazole, famotidine, cimetidine)
  - epinephrine
  - bisacodyl
  - lorcaserin
- **Literature-noted risks**: The cited publications highlight agranulocytosis and neutropenia (blood-count monitoring), myocarditis and cardiomyopathy, seizures, and metabolic effects such as weight gain and metabolic syndrome.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 double-blind trial and systematic reviews and meta-analyses directly address clozapine in bipolar mania, and the TxGNN score is very high (0.9995). The trial is small and the drug carries serious risks, so any further development needs strict safety conditions.

**To proceed, the following is needed:**
- Results and outcome data from NCT00029458, and confirmation from larger controlled trials in mania
- Health Canada package insert warnings and contraindications (not yet captured)
- Mechanism-of-action data to strengthen the mechanistic rationale
- A safety monitoring plan covering:
  - absolute neutrophil count
  - cardiac monitoring
  - seizure risk
  - metabolic parameters
  - management of the major drug interactions listed above

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

