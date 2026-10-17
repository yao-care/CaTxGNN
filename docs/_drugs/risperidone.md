---
layout: default
title: Risperidone
parent: Model Prediction Only (L5)
nav_order: 815
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Risperidone: predicted new indication Gaze palsy, familial horizontal, with progressive scoliosis (evidence level L5). Approved use: Schizophrenia"
monitor_inn: "RISPERIDONE"
predicted_indications: ["gaze palsy, familial horizontal, with progressive scoliosis", "asperger syndrome, susceptibility to", "amelocerebrohypohidrotic syndrome", "Phelan-McDermid syndrome", "trichotillomania"]
---

# Risperidone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Risperidone: From Schizophrenia and Bipolar Disorder to Familial Horizontal Gaze Palsy with Progressive Scoliosis

## One-Sentence Summary

Risperidone is an antipsychotic originally used for schizophrenia, bipolar disorder and autism-spectrum-related conditions.
The TxGNN model predicts it may be effective for **familial horizontal gaze palsy with progressive scoliosis**, a rare genetic disorder.
Currently there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia; bipolar disorder (including mania); autism spectrum disorder (from the knowledge graph, because the Canadian licence records contain no indication text) |
| Predicted New Indication | Gaze palsy, familial horizontal, with progressive scoliosis |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, risperidone is an atypical antipsychotic that blocks dopamine D2 and serotonin 5-HT2A receptors. Its efficacy in schizophrenia and bipolar mania is well established.

**The predicted link is weak.** Familial horizontal gaze palsy with progressive scoliosis is a rare genetic disorder of axon guidance, linked to the ROBO3 gene. It does not involve dopaminergic or serotonergic pathology that D2/5-HT2A antagonism would plausibly address. The very high score (99.76%) therefore looks like an artifact of the knowledge-graph structure rather than a pharmacologically grounded signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Risperidone has 20 valid single-ingredient authorizations in Canada and no cancelled ones. Dosage form and approved-indication text are not available in the compiled records. The first five are listed below.

| DIN | Product Name |
|---------|------|
| 02264218 | TEVA-RISPERIDONE |
| 02255758 | RISPERDAL CONSTA |
| 02356910 | RISPERIDONE |
| 02371804 | MAR-RISPERIDONE |
| 02283565 | RIVA-RISPERIDONE |

---

## Safety Considerations

Package insert warnings and contraindications were not available for this report. Please refer to the Health Canada package insert for authoritative safety information.

- **Knowledge-graph contraindication signals** (not label text): the graph links risperidone to contraindications in several groups.
  - Cardiovascular: heart disease, myocardial infarction, stroke, heart conduction disease, sudden cardiac arrest, orthostatic or hypotensive disorders.
  - Metabolic: diabetes mellitus, diabetic ketoacidosis, hyperglycaemia, hyperlipidaemia, obesity.
  - Haematological: neutropenia, agranulocytosis.
  - Other: epilepsy, liver disease or failure, gallbladder disease, female breast carcinoma.
- **Drug Interactions**: 100 interacting drugs were recorded. The two **Major** interactions in the retrieved list are **bupropion** and **morphine**. Many others are Moderate, including metformin, acarbose, alogliptin, canagliflozin, epinephrine, hydrocortisone, atropine, loperamide and famotidine.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications and no plausible mechanistic link. The target condition is a rare axon-guidance disorder unrelated to risperidone's pharmacology. The knowledge-graph contraindication signals (for example epilepsy and cardiovascular disease) add caution in a population that may include patients with seizures.

**To proceed, the following is needed:**
- Mechanistic evidence connecting risperidone to ROBO3-related pathology (none identified)
- Any preclinical or clinical data in this condition
- Complete mechanism of action data and the Health Canada package insert warnings and contraindications

**Note on other predictions for this drug:** the compiled data contain a better-supported candidate, **major affective disorder** (TxGNN score 99.11%). It has two completed Phase 3 trials of adjunctive risperidone in treatment-resistant depression (NCT00095134, n=630; NCT00044681, n=258) and several meta-analyses. It is rated L1 with a "Proceed with Guardrails" recommendation. That candidate partly overlaps with the existing bipolar indication, and it would need monitoring of metabolic effects, prolactin, extrapyramidal symptoms and somnolence. It is worth a separate evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

