---
layout: default
title: Nortriptyline
parent: High Evidence (L1-L2)
nav_order: 669
evidence_level: L2
indication_count: 2
last_modified_at: 2026-10-13
description: "Nortriptyline: predicted new indication Attention deficit hyperactivity disorder (evidence level L2). Approved use: Anxiety disorder, neurotic disorder, dysthymic disorder"
---

# Nortriptyline
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **2** 
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

# Nortriptyline: From Anxiety Disorder to Attention Deficit Hyperactivity Disorder

## One-Sentence Summary

Nortriptyline is a tricyclic antidepressant whose original indications in the knowledge base include anxiety disorder, neurotic disorder and dysthymic disorder.
The TxGNN model predicts it may be effective for **attention deficit hyperactivity disorder (ADHD)**,
with **no registered clinical trials** but **16 publications** (including one randomized controlled trial and one Cochrane systematic review) currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anxiety disorder, neurotic disorder, dysthymic disorder (from the knowledge graph; the Canadian licence records contain no indication text) |
| Predicted New Indication | Attention deficit hyperactivity disorder |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L2 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, nortriptyline is a tricyclic antidepressant that mainly inhibits norepinephrine reuptake, with weaker serotonin reuptake inhibition. This mechanism is inferred from general knowledge, not from the supplied record.

Enhancing noradrenergic signalling in prefrontal circuits is a recognised approach in ADHD treatment, comparable to atomoxetine. One PET study in the literature also reports that nortriptyline is a norepinephrine-transporter-selective tricyclic agent, which supports a plausible biological link.

The original indications (anxiety and mood-related disorders) and ADHD are both neuropsychiatric conditions in which monoamine modulation plays a role. The high TxGNN score is a computational prediction. It supports prioritisation but does not prove efficacy.

A second predicted entry, **ADHD, inattentive type** (score 99.33%), follows the same mechanistic rationale. It has no specific supporting evidence, so it is treated as a subset of the main ADHD prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11052409](https://pubmed.ncbi.nlm.nih.gov/11052409/) | 2000 | RCT | J Child Adolesc Psychopharmacol | Controlled study of nortriptyline's efficacy and tolerability in children and adolescents with ADHD |
| [22700161](https://pubmed.ncbi.nlm.nih.gov/22700161/) | 2012 | RCT | Pediatr Nephrol | Randomized double-blind trial of nortriptyline for enuresis in children with ADHD |
| [25238582](https://pubmed.ncbi.nlm.nih.gov/25238582/) | 2014 | Systematic review | Cochrane Database Syst Rev | Review of tricyclic antidepressants as second-line ADHD treatment in children and adolescents |
| [15064003](https://pubmed.ncbi.nlm.nih.gov/15064003/) | 2004 | Review | Psychiatr Clin North Am | Nonstimulant treatments for adult ADHD; nortriptyline and desipramine are established alternatives but limited by a narrow therapeutic index and cardiovascular toxicity |
| [12270803](https://pubmed.ncbi.nlm.nih.gov/12270803/) | 2002 | Review | Adolesc Med | Overview of ADHD drugs in adolescents, including nortriptyline among the tricyclics |
| [22303520](https://pubmed.ncbi.nlm.nih.gov/22303520/) | 2012 | Guideline | Ann Clin Psychiatry | CANMAT recommendations for mood disorders with comorbid ADHD |
| [8428873](https://pubmed.ncbi.nlm.nih.gov/8428873/) | 1993 | Cohort/Open-label | J Am Acad Child Adolesc Psychiatry | Nortriptyline in children with ADHD and tic disorder or Tourette's syndrome |
| [8444763](https://pubmed.ncbi.nlm.nih.gov/8444763/) | 1993 | Chart review | J Am Acad Child Adolesc Psychiatry | Chart review of 58 cases of nortriptyline treatment for ADHD |
| [8444754](https://pubmed.ncbi.nlm.nih.gov/8444754/) | 1993 | Retrospective study | J Am Acad Child Adolesc Psychiatry | Serum levels and ECG effects of nortriptyline in children and adolescents |
| [4075308](https://pubmed.ncbi.nlm.nih.gov/4075308/) | 1985 | Clinical study | Clin Neuropharmacol | Early report of nortriptyline in attention deficit disorder |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00015237 | AVENTYL | Not listed | Not listed |
| 00015229 | AVENTYL | Not listed | Not listed |

## Safety Considerations

- **Contraindications (knowledge graph associations, not label text)**: The drug-disease contraindication links include long QT syndrome (including familial), torsades de pointes, heart conduction disease, sudden cardiac arrest, myocardial infarction and coronary thrombosis, stroke and other cerebrovascular disorders, liver failure, kidney failure and uremia, epilepsy, manic bipolar disorder, open-angle glaucoma and glaucoma, benign prostatic hyperplasia, substance abuse/dependence, hyperthyroidism (including Graves disease and thyrotoxicosis), and hemoglobinopathy.
- **Drug Interactions**: 100 interactions were found in total. Of the 20 reviewed, the **Major** interactions are:
  - Epinephrine
  - Bupropion
  - Lorcaserin
  - Potassium citrate
  - Dolasetron

  Moderate interactions include anticholinergics (atropine, hyoscyamine, glycopyrronium, dicyclomine), loperamide, morphine, famotidine and cimetidine, clarithromycin, chlorpropamide, and others.
- **Cardiovascular concern in ADHD use**: The literature notes that tricyclics have a narrow therapeutic index and potential cardiovascular toxicity, and one retrospective study examined ECG effects in children and adolescents.

Package insert warnings were not available for this report. Please refer to the Health Canada package insert for the full warnings.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Published evidence includes a controlled study, a Cochrane review and several clinical series supporting nortriptyline in ADHD, with a plausible noradrenergic mechanism. However, there are no registered clinical trials, and the cardiovascular and interaction risks are significant. The inattentive-type prediction has no specific evidence, so it should be held.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmed mechanism of action data from DrugBank
- A careful review of the RCT and Cochrane review findings to confirm effect size and tolerability
- A cardiovascular (ECG) and drug-interaction monitoring plan, especially for children and adolescents
- Confirmation of the approved indications and dosage forms of the two AVENTYL DINs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

