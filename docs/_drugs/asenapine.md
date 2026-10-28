---
layout: default
title: Asenapine
parent: Model Prediction Only (L5)
nav_order: 74
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Asenapine: predicted new indication Retinal dystrophy with or without extraocular anomalies (evidence level L5). Approved use: Manic bipolar affective disorder, bipolar disorder, schizophrenia"
monitor_inn: "ASENAPINE"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "congenital disorder of glycosylation with defective fucosylation", "hydranencephaly (disease)", "syndromic myopia", "myopia X-linked", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "myopia 26, X-linked, female-limited", "atypical glycine encephalopathy", "major affective disorder"]
---

# Asenapine
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

## Asenapine: From Bipolar Disorder and Schizophrenia to Retinal Dystrophy with or without Extraocular Anomalies (Top TxGNN Prediction)
{: .text-alpha }

## One-Sentence Summary

Asenapine is an atypical antipsychotic originally used for manic bipolar disorder and schizophrenia.
The TxGNN model's top-ranked prediction is **retinal dystrophy with or without extraocular anomalies**, but there are **no clinical trials and no publications** supporting it, so it is a computational prediction only.
The only prediction with literature support is **major affective disorder** (rank 10), which largely overlaps with asenapine's existing approved use and is not a true repurposing finding (**20 publications**, no registered clinical trials).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Manic bipolar affective disorder, bipolar disorder, schizophrenia |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies (rank 1) |
| TxGNN Prediction Score | 0.9977 |
| Evidence Level | L5 (for the top prediction) |
| Canada Market Status | Marketed (valid licenses: 2 of 2) |
| Number of DINs | 2 (valid: 2) |
| Recommended Decision | Hold |

Note: The Canadian licence data compiled for this report contain no approved-indication text, so the original indication comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Among the other predictions, only **major affective disorder** (rank 10, score 0.9957) has literature support (evidence level L1, **Proceed with Guardrails**). It is an established use rather than a new one.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, asenapine is a serotonin, dopamine, adrenergic and histamine receptor antagonist. Its efficacy in bipolar mania and schizophrenia is established.

**Top prediction (retinal dystrophy):** No mechanistic link to inherited retinal degeneration could be identified. The high score is a computational result and is not supported by any trial or publication.

**Other top-ten predictions:** None shows a plausible mechanism.
- Congenital disorder of glycosylation, hydranencephaly, polymicrogyria, Charcot-Marie-Tooth type 1G and atypical glycine encephalopathy are structural, metabolic or inherited conditions that receptor antagonism is not expected to modify.
- The myopia entries (syndromic myopia, X-linked myopia, myopia 26) are only loosely connected through dopamine signalling in eye growth. Asenapine is a dopamine antagonist, and no evidence supports this use.

**Major affective disorder (rank 10):** This is the one prediction with a clear rationale. It includes bipolar disorder and mania, which are asenapine's approved uses. Blockade of dopamine D2 and serotonin 5-HT2A receptors, together with effects on other monoaminergic receptors, is the accepted basis for its antimanic effect. It is a confirmation of an existing indication, not a new discovery.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The following publications relate to rank 10 (major affective disorder). No literature is available for the other nine predictions.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23719049](https://pubmed.ncbi.nlm.nih.gov/23719049/) | 2013 | Meta-analysis of RCTs | Int Clin Psychopharmacol | Four randomized trials analysed for efficacy and tolerability of asenapine in acute mania of bipolar I disorder |
| [20420486](https://pubmed.ncbi.nlm.nih.gov/20420486/) | 2010 | Review | Expert Rev Neurother | Pharmacology and efficacy in manic and mixed states; higher 5-HT2A than D2 affinity, with distinct monoamine, histamine and muscarinic receptor effects |
| [28741044](https://pubmed.ncbi.nlm.nih.gov/28741044/) | 2017 | Open-label RCT | CNS Drugs | Asenapine compared with olanzapine in borderline personality disorder |
| [26891297](https://pubmed.ncbi.nlm.nih.gov/26891297/) | 2016 | Systematic review / meta-analysis | Int J Mol Sci | Atypical antipsychotics in acute bipolar depression with mixed features; evidence described as scarce and equivocal |
| [37815563](https://pubmed.ncbi.nlm.nih.gov/37815563/) | 2023 | Review | JAMA | Diagnosis and treatment of bipolar disorder |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Review | Acta Psychiatr Scand | Evidence-based treatment options for bipolar mania |
| [29170943](https://pubmed.ncbi.nlm.nih.gov/29170943/) | 2018 | Review | Paediatr Drugs | Asenapine in paediatric bipolar I disorder or schizophrenia; approved in the US for manic or mixed episodes at ages 10–17 |
| [20135021](https://pubmed.ncbi.nlm.nih.gov/20135021/) | 2009 | Review | Drugs Today (Barc) | Asenapine maleate as a new drug for schizophrenia and bipolar mania |
| [28005435](https://pubmed.ncbi.nlm.nih.gov/28005435/) | 2017 | Review | Expert Rev Neurother | Whether any second-generation antipsychotic is weight neutral in bipolar disorder |
| [35141987](https://pubmed.ncbi.nlm.nih.gov/35141987/) | 2022 | Case report | Psychogeriatrics | Adding asenapine to escitalopram in major depressive disorder with psychotic features |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02374803 | SAPHRIS | Not specified | Not specified in the data compiled |
| 02374811 | SAPHRIS | Not specified | Not specified in the data compiled |

---

## Safety Considerations

**Contraindication-related conditions (from the TxGNN knowledge graph, not label text):**
Asenapine is linked to the following groups of conditions.
- **Cardiovascular:** long QT syndrome, familial long QT syndrome, torsades de pointes, myocardial infarction, myocardial ischemia, coronary artery disease, orthostatic hypotension, postural orthostatic tachycardia syndrome
- **Cerebrovascular:** stroke, cerebral infarction, cerebrovascular disorder
- **Metabolic:** diabetes mellitus, hyperglycemia, diabetic ketoacidosis, obesity, potassium deficiency
- **Blood:** neutropenia, agranulocytosis, leukopenia, severe congenital neutropenia, cyclic hematopoiesis, hemoglobinopathy
- **Other:** liver failure, epilepsy, neuroleptic malignant syndrome, multiple system atrophy

**Drug interactions:** 100 interactions are recorded. Examples of the **Major** interactions listed are:
- Bupropion
- Morphine
- Cisapride

Moderate interactions include:
- Antidiabetic agents (acarbose, metformin, pioglitazone, alogliptin, albiglutide, canagliflozin, acetohexamide, chlorpropamide)
- Anticholinergics (atropine, hyoscyamine)
- Famotidine and cimetidine
- Clarithromycin
- Epinephrine
- Loperamide
- Bisacodyl and castor oil

**Literature-noted effects:** Somnolence, metabolic effects and weight gain are discussed in the reviews.

Please refer to the package insert for the official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, retinal dystrophy, and for predictions 1–9 in general)

**Rationale:**
- The top predictions have only a computational score, with no mechanistic link, clinical trials or publications.
- Major affective disorder (rank 10) is supported at L1/S3 (**Proceed with Guardrails**), but it is an existing labeled use rather than a repurposing opportunity.

**To proceed, the following is needed:**
- Mechanism of action data
- Health Canada package insert warnings and contraindications, which block safety screening
- For major affective disorder: registered clinical trial (NCT) verification, and confirmation of the approved indication text for the Canadian DINs
- For depressive and other affective subtypes beyond mania: supporting trial evidence
- A safety monitoring plan covering QT, metabolic, haematological and interaction risks
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

