---
layout: default
title: Vilazodone
parent: Model Prediction Only (L5)
nav_order: 975
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Vilazodone: predicted new indication Dysthymic disorder (evidence level L5). Approved use: Major depressive disorder"
monitor_inn: "Vilazodone"
predicted_indications: ["agoraphobia", "benign paroxysmal torticollis of infancy", "Keppen-Lubinsky syndrome", "Ohdo syndrome and variants", "schizotypal personality disorder"]
---

# Vilazodone
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

# Vilazodone: From Major Depressive Disorder to Dysthymic Disorder

## One-Sentence Summary

Vilazodone is an antidepressant originally used for major depressive disorder and related depressive and anxiety conditions.
The TxGNN model predicts it may be effective for **Dysthymic Disorder** (persistent depressive disorder), but **no clinical trials and no publications** specific to this indication were found, so the prediction currently rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major depressive disorder (the Canadian licence records contain no indication text; this is taken from the knowledge-graph indications: unipolar depression, endogenous depression, major depressive disorder, anxiety disorder) |
| Predicted New Indication | Dysthymic disorder |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. The published literature describes vilazodone as a serotonin reuptake inhibitor combined with 5-HT1A receptor partial agonism. It was designed so that the 5-HT1A component may offset the negative feedback that limits the early effect of SSRIs.

Dysthymic disorder is a chronic, milder form of depression that sits close to the approved major depressive disorder indication. Because the underlying serotonergic pathways overlap, it is plausible that the same mechanism helps in chronic depressive symptoms.

The very high score should be read with caution. No trials or literature were found for this indication, so this is a model prediction only.

### Other Predicted Indications (for context)

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Neurotic disorder | 99.75% | L5 | Outdated, non-specific category; no evidence |
| Neurotic depression | 99.72% | L4 | Roughly equivalent to dysthymia; 20 general antidepressant publications, largely indirect |
| Melancholia | 99.72% | L4 | 1 Phase 4 trial in general major depression; indirect |
| Obsessive-compulsive disorder | 99.72% | L4 | Plausible serotonergic link; no vilazodone-specific data (research question only) |
| Agoraphobia | 99.68% | L5 | Plausible link; no evidence |
| Benign paroxysmal torticollis of infancy, Keppen-Lubinsky syndrome, Ohdo syndrome | 99.5–99.6% | L5 | No plausible mechanism; likely graph artifacts |
| Schizotypal personality disorder | 99.51% | L5 | Weak, speculative link |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for dysthymic disorder.

---

## Literature Evidence

Currently no related literature available for dysthymic disorder.

For the closely related "neurotic depression" prediction, the following vilazodone-relevant publications were retrieved. They concern major depression, not dysthymia specifically:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35726313](https://pubmed.ncbi.nlm.nih.gov/35726313/) | 2022 | Review | Neuropsychiatr Dis Treat | Updated review of vilazodone in adult major depression; efficacy supported by four positive short-term (8–10 week) placebo-controlled trials |
| [36253442](https://pubmed.ncbi.nlm.nih.gov/36253442/) | 2023 | Network meta-analysis | Mol Psychiatry | Compares antidepressants in the maintenance phase of adult major depression |
| [37032427](https://pubmed.ncbi.nlm.nih.gov/37032427/) | 2023 | Guideline | Clin Pharmacol Ther | Pharmacogenetic guideline for serotonin reuptake inhibitor antidepressants, including vilazodone |
| [27508501](https://pubmed.ncbi.nlm.nih.gov/27508501/) | 2016 | Review | Psychother Psychosom | Safety and tolerability of newer-generation antidepressants, including vilazodone |
| [31777303](https://pubmed.ncbi.nlm.nih.gov/31777303/) | 2020 | Systematic review | Clin Toxicol | Vilazodone poisoning; possible greater toxicity in overdose |
| [24195711](https://pubmed.ncbi.nlm.nih.gov/24195711/) | 2013 | Review | Expert Opin Drug Discov | Discovery and development of vilazodone as an SSRI plus 5-HT1A partial agonist |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02551810 | APO-VILAZODONE | Not listed | Not listed |
| 02443732 | VIIBRYD | Not listed | Not listed |
| 02443740 | VIIBRYD | Not listed | Not listed |
| 02551837 | APO-VILAZODONE | Not listed | Not listed |
| 02551829 | APO-VILAZODONE | Not listed | Not listed |

A sixth valid single-ingredient licence (VIIBRYD, DIN 02443724) is also held, giving 6 valid licences in total. No licences are cancelled.

---

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: epilepsy, bipolar disorder, major affective disorder, blood coagulation disease, neuroleptic malignant syndrome, inappropriate ADH syndrome, nephrogenic syndrome of inappropriate antidiuresis, and serotonin syndrome.
- **Drug Interactions**: 100 interactions were identified. Those shown below are among the first 20 returned and are not a ranked list of the most severe.
  - **Major**: bupropion, lorcaserin, clarithromycin, diethylpropion, dolasetron, palonosetron, phentermine
  - **Moderate** (examples): acetylsalicylic acid, morphine, dexamethasone, aprepitant, pioglitazone, glimepiride, chlorpropamide, and several insulins
- **Other**: One review notes that vilazodone may raise serotonin concentrations faster than SSRIs, which could mean more severe toxicity in overdose. The predicted indication "benign paroxysmal torticollis of infancy" would involve infants, and vilazodone is not approved for paediatric use.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for dysthymic disorder is biologically plausible because it is close to the approved depression indication, but it is supported by a model score only (L5), with no trials or literature. Package insert safety data is also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking gap)
- Mechanism-of-action data from DrugBank
- A targeted search for trials or studies of vilazodone in dysthymia or persistent depressive disorder
- Clarification of how dysthymia differs from the approved major depressive disorder indication, so the repurposing question is meaningful
- For obsessive-compulsive disorder, a literature review of vilazodone-specific data before treating it as a research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

