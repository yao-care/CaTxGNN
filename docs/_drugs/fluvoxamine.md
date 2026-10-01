---
layout: default
title: Fluvoxamine
parent: Model Prediction Only (L5)
nav_order: 404
evidence_level: L5
indication_count: 10
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

# Fluvoxamine: From SSRI Use (Original Indication Not Recorded) to Schizoid Personality Disorder

## One-Sentence Summary

Fluvoxamine is a selective serotonin reuptake inhibitor (SSRI). The supplied data does not record its original approved indication.
The TxGNN model predicts it may be effective for **schizoid personality disorder**, but there are **0 clinical trials** and only **1 publication**, a cross-sectional comorbidity study rather than a treatment study.
The score is a knowledge-graph prediction only, so this is a low-evidence candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the supplied Health Canada records |
| Predicted New Indication | Schizoid personality disorder |
| TxGNN Prediction Score | 99.997% (rank 136) |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source MOA field. Based on known information, fluvoxamine is an SSRI and a sigma-1 receptor agonist. Its serotonergic effects are established in anxiety, obsessive-compulsive and depressive disorders.

No treatment-relevant link to schizoid personality disorder is documented. The only retrieved paper studied personality disorders and traits in body dysmorphic disorder. It describes which conditions occur together, not how patients respond to fluvoxamine. Its authors note that schizoid traits have been postulated in that population. Twenty-six of its 148 participants took part in a fluvoxamine treatment study, but the paper does not report treatment outcomes for schizoid personality disorder.

The TxGNN score of 99.997% is also identical for several personality disorders (schizoid, schizotypal, histrionic and paranoid). It is saturated and does not discriminate between them, so it should not be read as evidence specific to this disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10929788](https://pubmed.ncbi.nlm.nih.gov/10929788/) | 2000 | Cross-sectional | Comprehensive Psychiatry | Assessed personality disorders and traits in 148 people with body dysmorphic disorder, 26 of whom were in a fluvoxamine treatment study. Describes comorbidity, not drug response. |

---

## Canada Market Information

Six licenses are on record; five are listed below. Dosage form and approved-indication text were not provided.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1919369 | LUVOX | — | — |
| 1919342 | LUVOX | — | — |
| 2255537 | TEVA-FLUVOXAMINE | — | — |
| 2231330 | APO-FLUVOXAMINE | — | — |
| 2255529 | TEVA-FLUVOXAMINE | — | — |

---

## Safety Considerations

Please refer to the package insert for safety information.

The drug-interaction query returned no results. This should not be read as "no interactions", because fluvoxamine is known to inhibit CYP1A2 and CYP2C19 and needs a formal interaction review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone. There are no registered trials and no treatment data for schizoid personality disorder, and the score does not distinguish this disease from related personality disorders. Other fluvoxamine candidates in this pack have stronger support (anxiety disorder, endogenous depression and agoraphobia are all L2), though these may already be labeled uses rather than true repurposing.

**To proceed, the following is needed:**
- The Health Canada package insert (approved indications, warnings, contraindications), which currently blocks safety screening
- Detailed mechanism-of-action data from DrugBank
- Any controlled or open-label study of fluvoxamine in schizoid personality disorder
- A full drug-interaction review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

