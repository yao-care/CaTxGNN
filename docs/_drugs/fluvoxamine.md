---
layout: default
title: Fluvoxamine
parent: Model Prediction Only (L5)
nav_order: 407
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Fluvoxamine: predicted new indication Schizoid personality disorder (evidence level L5). Approved use: Social phobia, phobic disorder, obsessive-compulsive disorder"
monitor_inn: "Fluvoxamine"
predicted_indications: ["schizoid personality disorder", "schizotypal personality disorder", "histrionic personality disorder (disease)", "paranoid personality disorder", "anxiety disorder", "agoraphobia", "benign paroxysmal torticollis of infancy", "dependent personality disorder", "narcissistic personality disorder", "endogenous depression"]
---

# Fluvoxamine
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

# Fluvoxamine: From Social Phobia and Obsessive-Compulsive Disorder to Schizoid Personality Disorder

## One-Sentence Summary

Fluvoxamine is a selective serotonin reuptake inhibitor (SSRI) originally used for social phobia and obsessive-compulsive disorder (OCD).
The TxGNN model predicts it may be effective for **schizoid personality disorder**, but **no clinical trials** and only **1 publication** are linked to this prediction, and that publication is not a treatment study.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Social phobia, phobic disorder, obsessive-compulsive disorder |
| Predicted New Indication | Schizoid personality disorder |
| TxGNN Prediction Score | 99.997% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Fluvoxamine is an SSRI, and serotonin reuptake inhibition is the established basis for its use in anxiety-spectrum conditions such as social phobia and OCD. Mechanistically, serotonergic modulation might influence some traits seen in personality disorders, such as social withdrawal and detachment.

The relationship between the original and new indications is weak. Social phobia and OCD are anxiety-spectrum disorders with documented responses to SSRIs. Schizoid personality disorder is a long-standing pattern of detachment and restricted emotional expression, and no data compiled here show that fluvoxamine treats it. The very high model score (99.997%) is purely computational. The same score was assigned to several other personality disorders (schizotypal, histrionic, paranoid), which suggests the model is picking up a general class-level pattern rather than a disorder-specific signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10929788](https://pubmed.ncbi.nlm.nih.gov/10929788/) | 2000 | Cohort | Comprehensive Psychiatry | Assessed personality disorders and traits in 148 people with body dysmorphic disorder, 26 of whom took part in a fluvoxamine treatment study. It examined how common schizoid and other personality traits are in this group and did not test fluvoxamine as a treatment for schizoid personality disorder. |

---

## Canada Market Information

Fluvoxamine has 6 valid single-ingredient authorizations in Canada. The data compiled for this report do not include dosage form or approved-indication text for these products.

| DIN | Product Name | Status |
|---------|------|------|
| 01919369 | LUVOX | Valid |
| 01919342 | LUVOX | Valid |
| 02255537 | TEVA-FLUVOXAMINE | Valid |
| 02231330 | APO-FLUVOXAMINE | Valid |
| 02255529 | TEVA-FLUVOXAMINE | Valid |

---

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the Health Canada package insert for these.

- **Conditions flagged as contraindication-related (drug-disease knowledge graph, not label text)**: epilepsy, bipolar disorder, major affective disorder, liver disease, gallbladder disease, blood coagulation disease, neuroleptic malignant syndrome, inappropriate ADH syndrome, nephrogenic syndrome of inappropriate antidiuresis, and serotonin syndrome.
- **Drug Interactions**: 100 interactions were identified. The ones flagged as **Major** include:
  - Alosetron
  - Diethylpropion
  - Dolasetron
  - Bupropion

  Examples of **Moderate** interactions include:
  - Acetylsalicylic acid
  - Clarithromycin
  - Morphine
  - Pioglitazone
  - Aprepitant
  - Several corticosteroids (hydrocortisone, dexamethasone, budesonide, betamethasone, triamcinolone)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. No clinical trials exist, and the single linked paper is an observational study that does not test fluvoxamine for this disorder. There is also no disorder-specific mechanistic rationale.

**To proceed, the following is needed:**
- Any direct clinical evidence (case series, pilot trials) of fluvoxamine in schizoid personality disorder
- Detailed mechanism of action data and a disorder-specific rationale
- Package insert warnings and contraindications from Health Canada
- A co-medication screening plan, given the large number of drug interactions

**Note on other predictions for this drug:** The same analysis ranked several other candidates with considerably stronger support: anxiety disorder, agoraphobia, and endogenous depression. For anxiety disorder, completed Phase 3 trials and network meta-analyses exist, though much of that evidence overlaps with already-labeled indications. For agoraphobia, placebo-controlled RCTs in panic disorder with agoraphobia exist. For endogenous depression, a Phase 2 trial of fluvoxamine in melancholia (NCT04160377, status unknown) is registered. These are better candidates for further evaluation than schizoid personality disorder.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

