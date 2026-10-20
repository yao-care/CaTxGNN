---
layout: default
title: Olanzapine
parent: Model Prediction Only (L5)
nav_order: 679
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Olanzapine: predicted new indication Benign paroxysmal torticollis of infancy (evidence level L5). Approved use: Bipolar disorder, manic bipolar affective disorder…"
monitor_inn: "OLANZAPINE"
predicted_indications: ["benign paroxysmal torticollis of infancy", "agoraphobia", "dysthymic disorder"]
---

# Olanzapine
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

# Olanzapine: From Bipolar Disorder and Schizophrenia to Benign Paroxysmal Torticollis of Infancy

## One-Sentence Summary

Olanzapine is an atypical antipsychotic originally used for schizophrenia, bipolar disorder, depression and anxiety disorders.
The TxGNN model predicts it may be effective for **benign paroxysmal torticollis of infancy**, but **no clinical trials and no publications** currently support this specific prediction.
The next two predictions, agoraphobia and dysthymic disorder, have limited indirect literature (6 and 5 publications respectively) and no registered trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bipolar disorder, manic bipolar affective disorder, unipolar depression, endogenous depression, major depressive disorder, anxiety disorder, schizophrenia (the Canadian licence records contain no indication text) |
| Predicted New Indication | Benign paroxysmal torticollis of infancy |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, olanzapine is an antipsychotic whose efficacy in schizophrenia and bipolar disorder is established. Its pharmacology is generally attributed to dopamine and serotonin receptor antagonism, but this could not be verified from the data compiled for this report.

Benign paroxysmal torticollis of infancy is a rare, self-limiting pediatric episodic disorder. It is related to the migraine spectrum and to CACNA1A channelopathies. No established mechanistic link to olanzapine's receptor pharmacology was identified. The high score is probably driven by network proximity to related neurological or movement phenotypes in the knowledge graph rather than a true pharmacological rationale.

Because the condition is benign and resolves on its own in infants, the risk-benefit balance for an antipsychotic with metabolic and sedative adverse effects is unfavourable.

### Other Predicted Indications Reviewed

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Agoraphobia | 99.47% | L3 | Research question. Plausible link through panic disorder and anxiety, supported only by small uncontrolled studies. |
| 3 | Dysthymic disorder | 99.28% | L3 | Research question. Overlaps with olanzapine's depression indications, but evidence is indirect. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for benign paroxysmal torticollis of infancy. No registered trials were found for agoraphobia or dysthymic disorder either.

---

## Literature Evidence

No related literature is currently available for benign paroxysmal torticollis of infancy.

For reference, the literature found for the two next-ranked predictions is shown below.

**Agoraphobia (rank 2)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16415705](https://pubmed.ncbi.nlm.nih.gov/16415705/) | 2006 | Open-label trial | J Clin Psychopharmacol | 12-week trial of olanzapine 5 mg/day added to an SSRI in 31 patients with SSRI-resistant panic disorder, with or without agoraphobia |
| [26635099](https://pubmed.ncbi.nlm.nih.gov/26635099/) | 2016 | Systematic review | Expert Opin Pharmacother | Treatment-resistant panic disorder: about one-third of patients remain symptomatic after treatment |
| [40946318](https://pubmed.ncbi.nlm.nih.gov/40946318/) | 2026 | Systematic review | Psychother Psychosom | Pharmacological, psychotherapeutic and neurostimulatory options for treatment-resistant anxiety disorders |
| [25012437](https://pubmed.ncbi.nlm.nih.gov/25012437/) | 2014 | Cohort | J Affect Disord | Impact of comorbid anxiety disorders, including agoraphobia, on 24-month outcomes in bipolar I disorder |
| [10739446](https://pubmed.ncbi.nlm.nih.gov/10739446/) | 2000 | Letter | Am J Psychiatry | Olanzapine and panic attacks |
| [15470803](https://pubmed.ncbi.nlm.nih.gov/15470803/) | 2004 | Case report | Pharmacopsychiatry | Remission of panic disorder after olanzapine plus paroxetine |

**Dysthymic disorder (rank 3)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21154393](https://pubmed.ncbi.nlm.nih.gov/21154393/) | 2010 | Systematic review | Cochrane Database Syst Rev | Second-generation antipsychotics as add-on treatment for major depressive disorder and dysthymia |
| [10578457](https://pubmed.ncbi.nlm.nih.gov/10578457/) | 1999 | Open-label study | Biol Psychiatry | Olanzapine safety and efficacy in borderline personality disorder with comorbid dysthymia |
| [22938165](https://pubmed.ncbi.nlm.nih.gov/22938165/) | 2012 | Review | Bipolar Disord | Evidence-based options for treatment-resistant bipolar disorder |
| [11920152](https://pubmed.ncbi.nlm.nih.gov/11920152/) | 2002 | Review | Mol Psychiatry | Substituted benzamides in dysthymia (a different drug class) |
| [34727399](https://pubmed.ncbi.nlm.nih.gov/34727399/) | 2021 | Systematic review | Hum Psychopharmacol | Amisulpride for depressive symptoms (a different drug) |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02229285 | ZYPREXA | Not specified | Not specified |
| 02243086 | ZYPREXA ZYDIS | Not specified | Not specified |
| 02303175 | PMS-OLANZAPINE | Not specified | Not specified |
| 02276739 | TEVA-OLANZAPINE | Not specified | Not specified |
| 02281791 | APO-OLANZAPINE | Not specified | Not specified |

There are 20 valid single-ingredient licences in total, including brand, generic and orally disintegrating tablet (ODT) products.

---

## Safety Considerations

- **Disease-level contraindications (knowledge graph):** These come from drug-disease relationships in the knowledge graph, not from package insert text. They include:
  - Metabolic conditions: diabetes mellitus, diabetic ketoacidosis, hyperglycaemia, hyperlipidaemia, hypertriglyceridaemia, obesity
  - Liver conditions: liver failure, liver disease, cirrhosis, gallbladder disease
  - Blood conditions: neutropenia, agranulocytosis, blood coagulation disease
  - Cardiovascular and cerebrovascular conditions: orthostatic hypotension, hypotensive disorder, myocardial infarction, stroke, cerebral infarction, cerebrovascular disorder, coronary thrombosis
  - Other: epilepsy, benign prostatic hyperplasia, female breast carcinoma, multiple system atrophy, postural orthostatic tachycardia syndrome
- **Drug Interactions:** 100 interactions were recorded. Major-level examples include **bupropion, morphine and potassium citrate**. Moderate-level examples include metformin, acarbose, alogliptin, canagliflozin, dapagliflozin, chlorpropamide, famotidine, epinephrine, clarithromycin, and several anticholinergic agents (atropine, hyoscyamine, glycopyrronium).
- **Rationale-level concerns:** Metabolic risk (weight gain, metabolic syndrome) and sedation are particular concerns for long-term use in a benign or chronic lower-severity condition.

The package insert warnings and contraindications from Health Canada were not available, so please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.54%), but there are no trials or publications for benign paroxysmal torticollis of infancy, and no plausible mechanistic link. The condition is self-limiting in infants, and olanzapine's metabolic and sedative risks make the risk-benefit balance unfavourable. Agoraphobia and dysthymic disorder are better-supported research questions (L3), but both rely on small, uncontrolled or indirect evidence.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which currently block safety screening
- Mechanism of action data for olanzapine
- For agoraphobia: a controlled trial of olanzapine augmentation in panic disorder with agoraphobia, compared against first-line SSRIs and CBT
- For dysthymic disorder: a dysthymia-specific randomised trial of olanzapine, with long-term metabolic monitoring
- For the top-ranked prediction: expert review to determine whether any biological rationale exists, given the CACNA1A channelopathy and migraine-spectrum background
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

