---
layout: default
title: Desipramine
parent: Model Prediction Only (L5)
nav_order: 261
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-13
description: "Desipramine: predicted new indication Attention deficit hyperactivity disorder… (evidence level L5). Approved use: Anxiety disorder, neurotic disorder, dysthymic disorder"
monitor_inn: "Desipramine"
predicted_indications: ["attention deficit hyperactivity disorder, inattentive type", "attention deficit-hyperactivity disorder", "specific developmental disorder", "chondromyxoid fibroma", "faciodigitogenital syndrome", "benign paroxysmal torticollis of infancy", "agoraphobia"]
---

# Desipramine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Desipramine: From Anxiety Disorder to Attention Deficit Hyperactivity Disorder, Inattentive Type

## One-Sentence Summary

Desipramine is a tricyclic antidepressant, originally used for anxiety disorder, neurotic disorder and dysthymic disorder.
The TxGNN model predicts it may be effective for **attention deficit hyperactivity disorder, inattentive type** (top-ranked prediction), but **no clinical trials or publications** were found for this exact subtype.
The closely related broader entry, **attention deficit-hyperactivity disorder (ADHD)**, is backed by **13 publications** (including a Cochrane review of tricyclic antidepressants) and no registered trials, and is the more realistic repurposing direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anxiety disorder, neurotic disorder, dysthymic disorder (from the knowledge graph; Canadian licence records contain no indication text) |
| Predicted New Indication | Attention deficit hyperactivity disorder, inattentive type (broader ADHD entry shown below for context) |
| TxGNN Prediction Score | 99.81% (ADHD, broader entry: 99.78%) |
| Evidence Level | L5 for the inattentive subtype; L3 for broader ADHD |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold (inattentive subtype); Proceed with Guardrails is conceivable only for broader ADHD as a research question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, desipramine is a tricyclic antidepressant with strong norepinephrine reuptake inhibition. Enhanced noradrenergic signalling in prefrontal circuits plausibly supports attention, which fits the high TxGNN score.

This is the same mechanism as atomoxetine, an approved non-stimulant ADHD treatment. Anxiety and mood disorders frequently co-occur with ADHD, which also links the original indications to the predicted one.

However, no trials or literature were retrieved for the inattentive subtype itself. The supporting evidence comes from the broader ADHD entry, and the connection to the subtype is inferred rather than demonstrated.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The table below lists the most relevant publications for the broader ADHD entry (none were found for the inattentive subtype).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25238582](https://pubmed.ncbi.nlm.nih.gov/25238582/) | 2014 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Tricyclic antidepressants as second-line treatment for ADHD in children and adolescents |
| [29944175](https://pubmed.ncbi.nlm.nih.gov/29944175/) | 2018 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Pharmacological treatment of ADHD in children with comorbid tic disorders |
| [19625978](https://pubmed.ncbi.nlm.nih.gov/19625978/) | 2009 | Meta-analysis | J Am Acad Child Adolesc Psychiatry | Relative efficacy of medications for ADHD and tics in children with both conditions |
| [30422834](https://pubmed.ncbi.nlm.nih.gov/30422834/) | 2019 | Systematic review | Int Clin Psychopharmacol | Pharmacotherapy for ADHD comorbid with an anxiety disorder |
| [8444765](https://pubmed.ncbi.nlm.nih.gov/8444765/) | 1993 | Clinical study | J Am Acad Child Adolesc Psychiatry | Desipramine in children with ADHD and tic disorder or Tourette's syndrome |
| [9418743](https://pubmed.ncbi.nlm.nih.gov/9418743/) | 1997 | Review | J Clin Psychiatry | Antidepressants are less effective than psychostimulants; desipramine should be avoided in youths and adolescents |
| [16732717](https://pubmed.ncbi.nlm.nih.gov/16732717/) | 2006 | Review | Expert Opin Investig Drugs | Adult ADHD pharmacotherapy; stimulants first-line, atomoxetine also reported effective |
| [17078784](https://pubmed.ncbi.nlm.nih.gov/17078784/) | 2006 | Observational | Expert Rev Neurother | Desipramine and imipramine as nonselective norepinephrine reuptake inhibitors can be effective |
| [8032506](https://pubmed.ncbi.nlm.nih.gov/8032506/) | 1994 | Review | Arch Fam Med | Desipramine a reasonable second choice after methylphenidate |
| [10790990](https://pubmed.ncbi.nlm.nih.gov/10790990/) | 1999 | Review | Evid Rep Technol Assess | Effectiveness and safety of ADHD treatments in children and adults |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02216248 | DESIPRAMINE | Not specified | Not specified |
| 02216256 | DESIPRAMINE | Not specified | Not specified |
| 02216264 | DESIPRAMINE | Not specified | Not specified |
| 02216272 | DESIPRAMINE | Not specified | Not specified |
| 02216280 | DESIPRAMINE | Not specified | Not specified |

---

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text)**: long QT syndrome, familial long QT syndrome, torsades de pointes, sudden cardiac arrest, heart conduction disease, epilepsy, bipolar disorder / major affective disorder, schizophrenia, angle-closure glaucoma / glaucoma, benign prostatic hyperplasia, hyperthyroidism / Graves disease / thyrotoxicosis, liver disease, gallbladder disease, kidney disease, pyoureter, stroke / cerebrovascular disorder / cerebral infarction, and substance abuse/dependence.
- **Drug Interactions**: 100 interactions were recorded. Examples classed as **Major**: epinephrine, bupropion, lorcaserin, potassium citrate, cisapride and dexfenfluramine. Many **Moderate** ones were also found, including anticholinergics (atropine, hyoscyamine, glycopyrronium, clidinium), famotidine, cimetidine, clarithromycin, morphine, loperamide and sulfonylureas (chlorpropamide, acetohexamide).
- **Other concerns from the literature**: reports of cardiovascular events, including sudden death in children treated with desipramine, and a large interaction burden (notably through CYP2D6).

Package insert warnings were not available; please refer to the Health Canada package insert for full safety information.

---

## Other Predicted Indications (for context)

| Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|
| Attention deficit-hyperactivity disorder | 99.78% | L3 | Reviews and a Cochrane review support use as second-line therapy; the best-supported direction |
| Agoraphobia | 99.22% | L3 | Open-label studies and one small placebo-controlled study ([8290663](https://pubmed.ncbi.nlm.nih.gov/8290663/)); overlaps with the original anxiety indications; SSRIs and CBT are first-line |
| Obsessive-compulsive disorder | 99.03% | L3 | Direct comparisons favour clomipramine, fluvoxamine and sertraline over desipramine; weak fit |
| Specific developmental disorder | 99.64% | L5 | Only preclinical papers; speculative |
| Chondromyxoid fibroma, faciodigitogenital syndrome, benign paroxysmal torticollis of infancy | 99.57%, 99.51%, 99.31% | L5 | No mechanistic link or evidence; likely knowledge-graph artifacts |

---

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked inattentive subtype). Broader ADHD can be pursued as a **research question**.

**Rationale:**
- The top prediction has no trials or literature behind it, so it rests on the model score alone (L5).
- For broader ADHD the evidence is mostly reviews of small, older studies, with no registered trials. Cardiovascular safety concerns and a heavy interaction burden further limit use, and stimulants and atomoxetine remain preferred options.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Review of primary trials behind the Cochrane TCA review to confirm study design and effect size, including subtype-specific (inattentive) data
- Cardiovascular risk assessment (ECG monitoring) and CYP2D6 interaction management plan
- Defined clinical niche versus approved ADHD therapies, for example ADHD with comorbid tics or anxiety
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

