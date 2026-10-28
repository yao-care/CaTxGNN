---
layout: default
title: Chlorpromazine
parent: Model Prediction Only (L5)
nav_order: 186
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
description: "Chlorpromazine: predicted new indication Retinal dystrophy with or without extraocular anomalies (evidence level L4). Approved use: Schizophrenia, psychotic disorder, manic bipolar affective disorder"
monitor_inn: "CHLORPROMAZINE"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "congenital disorder of glycosylation with defective fucosylation", "myopia X-linked", "syndromic myopia", "hydranencephaly (disease)", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "myopia 26, X-linked, female-limited", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "atypical glycine encephalopathy"]
---

# Chlorpromazine
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

## Chlorpromazine: From Schizophrenia and Other Psychotic Disorders to Retinal Dystrophy with or without Extraocular Anomalies
{: .text-alpha }

## One-Sentence Summary

Chlorpromazine is an antipsychotic originally used for schizophrenia, bipolar mania and other psychotic disorders.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**, but the only supporting item is **1 publication**, a 1967 report of phototoxic *adverse* reactions, and there are **no clinical trials**. This prediction should be regarded as a model output without therapeutic evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia, psychotic disorder, manic bipolar affective disorder (the Canadian licence records contain no indication text) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 3 of 3) |
| Number of DINs | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, chlorpromazine is a long-established antipsychotic (a dopamine D2 receptor antagonist), and its efficacy in schizophrenia and other psychotic disorders is well established.

For the predicted indication, a plausible therapeutic link is hard to find. The only publication is a 1967 report of phototoxic reactions to high-dose chlorpromazine and thioridazine. Chlorpromazine is also known to cause ocular effects, including lens and corneal deposits and pigmentary retinopathy at high doses. These are adverse-effect signals, not evidence of benefit. The high TxGNN score most likely reflects network proximity to retinal-related genes or pathways rather than a real therapeutic effect. The safety signal argues against use in retinal disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [5336672](https://pubmed.ncbi.nlm.nih.gov/5336672/) | 1967 | Case report/Observational | JAMA | Phototoxic reactions induced by high doses of chlorpromazine and thioridazine (an adverse-effect report, not therapeutic evidence) |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00232807 | TEVA-CHLORPROMAZINE | Not listed | Not listed |
| 00232823 | TEVA-CHLORPROMAZINE | Not listed | Not listed |
| 00232831 | TEVA-CHLORPROMAZINE | Not listed | Not listed |

## Safety Considerations

- **Disease-level cautions (from the knowledge graph, not label text):** Chlorpromazine is linked to contraindications in many conditions. The main groups are:
  - Cardiovascular: long QT syndrome (including familial), torsades de pointes, sudden cardiac arrest, heart conduction disease, myocardial infarction, orthostatic hypotension, postural orthostatic tachycardia syndrome
  - Blood: neutropenia, agranulocytosis, leukopenia, thrombocytopenia, anaemia
  - Neurological: epilepsy, basal ganglia disease, multiple system atrophy, focal hand dystonia, blepharospasm
  - Other: liver disease, gallbladder disease, hyperglycaemia, benign prostatic hyperplasia, obesity, substance abuse/dependence, female breast carcinoma
- **Drug Interactions:** The interaction screen returned 100 records. The ones listed below are the first 20 shown, and two are rated Major:
  - Major: bupropion and morphine
  - Moderate (examples): metformin, pioglitazone, epinephrine, hydrocortisone, famotidine, atropine, loperamide, amphotericin B, and several other antidiabetic and anticholinergic drugs
- **Ocular safety:** The available literature points to phototoxicity, and chlorpromazine is known to cause ocular deposits and pigmentary retinopathy at high doses. This is directly relevant to the proposed retinal indication.

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication rests on a model score alone. The only publication reports ocular and photosensitivity harm, and there are no registered trials. No therapeutic mechanism for retinal dystrophy is supported, and the safety signal runs in the opposite direction.

**To proceed, the following is needed:**
- Evidence of a plausible mechanism linking chlorpromazine to retinal dystrophy, and the drug's mechanism of action data
- Preclinical (L4) data showing benefit in retinal disease models
- Official Canadian package insert warnings and contraindications, together with the approved indication text and dosage forms
- An ocular safety assessment, covering retinopathy and phototoxicity

**Other predictions in the list:** The other eight highest-scoring predictions (for example X-linked and syndromic myopia, hydranencephaly, and congenital glycosylation and metabolic disorders) have no trials or literature and no supported mechanism, so they remain at **Hold**. The tenth prediction, early-onset schizophrenia, is an extension of an existing indication to a younger population. It is supported only by observational and pharmacogenetic studies (L3), and newer atypical antipsychotics are generally preferred in this group. It is better treated as a research question than as a repurposing candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

