---
layout: default
title: Duloxetine
parent: Model Prediction Only (L5)
nav_order: 308
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
monitor_inn: "DULOXETINE"
predicted_indications: ["benign paroxysmal torticollis of infancy", "agoraphobia", "obsessive-compulsive disorder", "schizoid personality disorder", "schizotypal personality disorder", "histrionic personality disorder (disease)", "paranoid personality disorder", "Ohdo syndrome and variants", "ligneous conjunctivitis", "blepharophimosis - intellectual disability syndrome, Ohdo type"]
description: "Duloxetine: predicted new indication Benign paroxysmal torticollis of infancy (evidence level L5). Approved use: Not recorded in the local data"
---

# Duloxetine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Duloxetine: Benign paroxysmal torticollis of infancy
{: .text-alpha }

## One-Sentence Summary

Duloxetine is a serotonin-norepinephrine reuptake inhibitor (SNRI), originally used for depressive disorders, anxiety disorders, fibromyalgia, myofascial pain and female stress incontinence.
The TxGNN model's top-ranked prediction is benign paroxysmal torticollis of infancy, but it has no supporting evidence. The best-supported prediction in the list is **Obsessive-Compulsive Disorder (OCD)**, with **3 clinical trials** (1 directly relevant) and **20 publications**, including one double-blind controlled trial.
This report covers OCD as the lead candidate, and the other top predictions are summarised briefly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Benign paroxysmal torticollis of infancy |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses on record: at least 20) |
| Number of DINs | at least 20 |
| Recommended Decision | Proceed with Guardrails (research question stage; not a treatment recommendation) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, duloxetine is an SNRI. It blocks reuptake of both serotonin and norepinephrine, and it is established in depression and generalized anxiety disorder.

Serotonin reuptake inhibition is the core mechanism of OCD drug treatment, and SSRIs and clomipramine are the standard options. Duloxetine's serotonin transporter inhibition, together with its noradrenergic activity, gives a plausible link between its original anxiety and depression indications and OCD. OCD and anxiety disorders also commonly occur together with depression.

The evidence is modest. It is small, and mostly comes from augmentation or open-label designs. Reviews do not position SNRIs as first-line therapy for OCD. They describe them as an option for patients who do not respond to standard treatment.

**Other predictions in the top 10:**
- **Agoraphobia (rank 2, L3):** Duloxetine has open-label and case-level support in panic disorder and generalized anxiety disorder, which gives indirect support. No agoraphobia-specific trial exists.
- **Benign paroxysmal torticollis of infancy, schizoid, schizotypal, histrionic and paranoid personality disorders, Ohdo syndrome and variants, ligneous conjunctivitis, and Ohdo-type blepharophimosis (ranks 1 and 4–10, L5):** These are prediction-only. No trials or literature were found, and no plausible mechanistic link was identified. The high scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Hold.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00464698](https://clinicaltrials.gov/study/NCT00464698) | Phase 4 | Completed | 20 | Duloxetine for the treatment of OCD. Directly relevant, but small and likely open-label |
| [NCT01404871](https://clinicaltrials.gov/study/NCT01404871) | N/A | Completed | 26 | Predicting medication response in OCD. Participants randomised to clomipramine or escitalopram; those who had already tried them could take duloxetine instead |
| [NCT02476136](https://clinicaltrials.gov/study/NCT02476136) | N/A | Unknown | 8800 | Individual patient data meta-analysis of initial severity and antidepressant efficacy in anxiety disorders. Not specific to duloxetine or OCD |

For agoraphobia, the only registered trial found (NCT05930912, psychiatric orders in psychoanalytic treatment of ASD, n=1) is not relevant to duloxetine.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27811556](https://pubmed.ncbi.nlm.nih.gov/27811556/) | 2016 | RCT (double-blind) | J Clin Psychopharmacol | Duloxetine augmentation in resistant OCD |
| [25637377](https://pubmed.ncbi.nlm.nih.gov/25637377/) | 2015 | Open-label study | Int J Neuropsychopharmacol | Efficacy of duloxetine for OCD |
| [31749717](https://pubmed.ncbi.nlm.nih.gov/31749717/) | 2019 | Systematic review | Front Psychiatry | Duloxetine in psychiatric disorders beyond major depression and generalized anxiety disorder |
| [16669725](https://pubmed.ncbi.nlm.nih.gov/16669725/) | 2006 | Review | J Clin Psychiatry | Critical review of SNRIs (venlafaxine, clomipramine) in OCD |
| [24766145](https://pubmed.ncbi.nlm.nih.gov/24766145/) | 2014 | Review | Expert Opin Pharmacother | Review of double-blind studies of serotonergic antidepressants in OCD |
| [21779536](https://pubmed.ncbi.nlm.nih.gov/21779536/) | 2011 | Review | Innov Clin Neurosci | Discusses SNRIs as pharmacological alternatives for OCD |
| [28477500](https://pubmed.ncbi.nlm.nih.gov/28477500/) | 2017 | Meta-analysis | J Affect Disord | OCD has a reduced placebo and antidepressant response compared with other anxiety disorders |
| [18208931](https://pubmed.ncbi.nlm.nih.gov/18208931/) | 2008 | Case series | J Psychopharmacol | Switching from serotonin reuptake inhibitors to duloxetine in resistant OCD |
| [39735048](https://pubmed.ncbi.nlm.nih.gov/39735048/) | 2024 | Case report | Cureus | Supratherapeutic duloxetine plus CBT in severe treatment-resistant OCD with comorbid depression |
| [19483491](https://pubmed.ncbi.nlm.nih.gov/19483491/) | 2009 | Case report | Clin Neuropharmacol | High-dose duloxetine in treatment-resistant OCD with sustained full remission |

For agoraphobia, the supporting literature is indirect: an open-label study in panic disorder ([19228176](https://pubmed.ncbi.nlm.nih.gov/19228176/), 2009) and a case report of panic disorder with gastric pain ([24294001](https://pubmed.ncbi.nlm.nih.gov/24294001/), 2013).

---

## Canada Market Information

Duloxetine has 20 valid single-ingredient licences in Canada and none cancelled. Dosage form and approved indication text are not available for these licences. The first five are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02457202 | TARO-DULOXETINE | – | – |
| 02456753 | TEVA-DULOXETINE | – | – |
| 02436647 | AURO-DULOXETINE | – | – |
| 02473208 | M-DULOXETINE | – | – |
| 02507765 | BIO-DULOXETINE | – | – |

---

## Safety Considerations

The following comes from knowledge-graph contraindication links and an interaction database. It is not package insert text, and warnings and contraindications from the label are not available.

- **Contraindication-linked conditions (knowledge graph):**
  - Cardiovascular and blood pressure: hypertension, orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy
  - Neuropsychiatric: epilepsy, bipolar disorder and major affective disorder, substance abuse/dependence
  - Hepatic and metabolic: liver disease, cirrhosis, fatty liver, hepatitis, gallbladder disease, hyperglycemia
  - Haematological and ocular: blood coagulation disease, angle-closure glaucoma
  - Other: serotonin syndrome, neuroleptic malignant syndrome, SIADH and nephrogenic syndrome of inappropriate antidiuresis
- **Drug interactions:** 100 interactions were recorded; the 20 retrieved include these major ones:
  - Bupropion
  - Lorcaserin
  - Diethylpropion
  - Dolasetron
  - Dexfenfluramine

  Most of these involve serotonergic or sympathomimetic effects. Moderate interactions include epinephrine, morphine, acetylsalicylic acid and cimetidine. Several acid-suppressing drugs (famotidine, ranitidine, rabeprazole) are minor.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for OCD only; Hold for the other predictions, with agoraphobia kept as a research question)

**Rationale:**
- OCD has a plausible mechanism, a double-blind augmentation trial, an open-label study, a completed Phase 4 trial and multiple case reports. The trials are small, mostly open-label or augmentation designs, and reviews do not treat SNRIs as first-line for OCD. Evidence therefore supports further research, not a treatment recommendation.
- The seven prediction-only candidates have no supporting evidence and should be held.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications. This is a blocking gap, so safety screening cannot proceed without it.
- Mechanism of action data from DrugBank
- Results from NCT00464698 and a critical appraisal of PMID 27811556, including its sample size and design
- A larger randomised, controlled trial of duloxetine in OCD, ideally against first-line SSRIs
- A safety monitoring plan covering the serotonergic drug interactions and the listed contraindicated conditions, especially bipolar disorder, liver disease and hypertension
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

