---
layout: default
title: Oxybutynin
parent: Model Prediction Only (L5)
nav_order: 695
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
monitor_inn: "Oxybutynin"
predicted_indications: ["restless legs syndrome", "gastroduodenitis", "peptic ulcer disease"]
description: "Oxybutynin: predicted new indication Restless legs syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Oxybutynin
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

## Oxybutynin: Restless legs syndrome
{: .text-alpha }

## One-Sentence Summary

Oxybutynin is an antimuscarinic drug originally used to treat overactive bladder and related bladder-control disorders.
The TxGNN model predicts it may be effective for **restless legs syndrome**,
but there are currently **no registered clinical trials** and **no publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Restless legs syndrome |
| TxGNN Prediction Score | 0.9974 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 6 of 6) |
| Number of DINs | 6 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, oxybutynin is a muscarinic receptor antagonist (anticholinergic), and its efficacy in overactive bladder is established.

The data compiled for this report do not establish a mechanistic link to restless legs syndrome. The very high model score (0.9974) comes from the TxGNN model (deep learning) and is a prediction only; it may reflect similarities the model learned between related diseases, not biological evidence. Anticholinergics are not a recognized treatment for restless legs syndrome, and their central effects could even worsen sleep or symptoms. This prediction should therefore be regarded as a weak, hypothesis-level signal.

Two other predictions were also generated: gastroduodenitis (score 0.9962) and peptic ulcer disease (score 0.9931). Antimuscarinic activity could theoretically reduce gastric secretion and motility. However, anticholinergics have been made obsolete by modern acid-suppressive therapy for these conditions, and oxybutynin has been linked to reflux esophagitis. Neither is stronger than the lead prediction in terms of clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for restless legs syndrome.

For reference, the literature retrieved for the third-ranked prediction (peptic ulcer disease) is listed below. It is indirect and old, and does not support the lead prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2360335](https://pubmed.ncbi.nlm.nih.gov/2360335/) | 1990 | Case report | DICP: the Annals of Pharmacotherapy | Oxybutynin-induced reflux esophagitis, probably from reduced lower esophageal sphincter tone caused by its anticholinergic action |
| [14173506](https://pubmed.ncbi.nlm.nih.gov/14173506/) | 1964 | Clinical evaluation (historical, likely uncontrolled) | Current Therapeutic Research | Evaluation of oxybutynin chloride in gastrointestinal disease; design and outcomes cannot be confirmed |
| [4380481](https://pubmed.ncbi.nlm.nih.gov/4380481/) | 1965 | Pharmacology review/preclinical | Archives Internationales de Pharmacodynamie et de Thérapie | Describes oxybutynin as a musculotropic antispasmodic with moderate anticholinergic action |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02240549 | PMS-OXYBUTYNIN | Not listed | Not listed |
| 02299364 | RIVA-OXYBUTYNIN | Not listed | Not listed |
| 02240550 | PMS-OXYBUTYNIN | Not listed | Not listed |
| 02223376 | PMS-OXYBUTYNIN | Not listed | Not listed |
| 02163543 | APO-OXYBUTYNIN | Not listed | Not listed |

One further authorisation (02230394, TEVA-OXYBUTYNIN) is also valid. All 6 licences are single-ingredient products with valid status.

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (not label text, so they must be confirmed against the package insert): conditions that commonly rule out anticholinergics include
  - Eye, neuromuscular and urinary: angle-closure glaucoma, myasthenia gravis, bladder neck obstruction, benign prostatic hyperplasia
  - Gastrointestinal: paralytic ileus, intestinal obstruction, toxic megacolon, ulcerative colitis and inflammatory bowel disease, gastroesophageal reflux disease and esophagitis, hiatus hernia
  - Cardiovascular, metabolic and organ disease: hyperthyroidism, coronary artery disease, heart conduction disease, hypertension, kidney disease, liver disease
- **Drug Interactions**: 100 interactions were found. Major-level interactions include **potassium citrate** and **potassium chloride**. Moderate-level interactions are mostly with other anticholinergic or antimuscarinic agents (e.g., hyoscyamine, atropine, glycopyrronium, trospium, dicyclomine, propantheline), opioids (morphine, opium), and loperamide, aprepitant, eluxadoline, metoclopramide and pramlintide.
- **Safety signal for upper GI use**: a published case report links oxybutynin to reflux esophagitis.

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for restless legs syndrome has a high model score but no clinical trials, no literature and no established mechanism, and anticholinergics are not a recognized therapy for it. The alternative predictions (gastroduodenitis, peptic ulcer disease) have only old, indirect evidence and a relevant GI safety signal.

**To proceed, the following is needed:**
- Mechanism of action data, to test whether any biologically plausible link to restless legs syndrome exists
- Package insert warnings and contraindications from Health Canada, which are currently missing
- Preclinical or observational evidence for oxybutynin in restless legs syndrome, including whether anticholinergic exposure worsens symptoms
- Dosage form, route and approved indication details for the Canadian licences
- A review of the interaction burden and the anticholinergic safety profile in the likely target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

