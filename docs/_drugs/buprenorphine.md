---
layout: default
title: Buprenorphine
parent: Moderate Evidence (L3-L4)
nav_order: 135
evidence_level: L4
indication_count: 6
last_modified_at: 2026-10-13
description: "Buprenorphine: predicted new indication Acute intermittent porphyria (evidence level L4). Approved use: Opioid dependence, substance abuse/dependence, morphine dependence"
monitor_inn: "BUPRENORPHINE"
predicted_indications: ["acute intermittent porphyria", "lingual-facial-buccal dyskinesia", "chronic tic disorder", "continuous spikes and waves during sleep", "benign shuddering attacks", "extrapyramidal and movement disease"]
---

# Buprenorphine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **6** 
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

## Buprenorphine: From Opioid Dependence to Acute Intermittent Porphyria
{: .text-alpha }

## One-Sentence Summary

Buprenorphine is an opioid medicine originally used to treat opioid dependence (including morphine dependence) and substance abuse/dependence.
The TxGNN model predicts it may be effective for **acute intermittent porphyria**, but there are **no registered clinical trials** and only **1 publication** (a 1993 case report about anaesthetic management, not treatment of the disease).
This is a model prediction with very weak supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Opioid dependence, substance abuse/dependence, morphine dependence |
| Predicted New Indication | Acute intermittent porphyria |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 18 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, buprenorphine is an opioid used in the treatment of opioid dependence, and its efficacy in that setting is established. Whether it is mechanistically applicable to acute intermittent porphyria is not supported by the data compiled for this report.

The only publication found is a 1993 case report on anaesthetic management of a patient who had porphyria. It describes which drugs were chosen around surgery, not treatment of the disease itself. No credible mechanistic link between buprenorphine and correcting the disease was identified. The high model score (0.994) reflects a graph-based prediction rather than clinical support. Buprenorphine's safety in porphyria (porphyrinogenic potential) would need its own evaluation, and it is not a therapeutic indication.

Other predicted indications are even less supported:

| Predicted Indication | TxGNN Score | Evidence Level | Evidence Summary |
|------|------|------|------|
| Lingual-facial-buccal dyskinesia | 99.32% | L4 | 15 publications, none treating the condition in humans (dementia agitation, animal pharmacology, case reports). Only an indirect link via mu-opioid/5-HT2A interactions |
| Chronic tic disorder | 99.13% | L5 | No trials or literature |
| Continuous spikes and waves during sleep | 99.05% | L5 | No trials or literature. Opioids may lower seizure threshold |
| Benign shuddering attacks | 99.03% | L5 | No trials or literature. Benign, self-limiting condition |
| Extrapyramidal and movement disease | 99.03% | L5 | No trials or literature. Broad category sharing a score with the row above, suggesting graph propagation |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8301837](https://pubmed.ncbi.nlm.nih.gov/8301837/) | 1993 | Case report | Masui (Japanese Journal of Anesthesiology) | Anaesthetic management of a 40-year-old woman with suspected acute intermittent porphyria undergoing gynaecological cancer surgery; perioperative care only, not disease treatment |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02341212 | BUTRANS 10 | Not specified | Not specified |
| 02341220 | BUTRANS 20 | Not specified | Not specified |
| 02450771 | BUTRANS 15 | Not specified | Not specified |
| 02341174 | BUTRANS 5 | Not specified | Not specified |
| 02483092 | SUBLOCADE | Not specified | Not specified |

All 18 licences are valid single-ingredient authorisations (also including SUBOXONE and generic buprenorphine/naloxone products).

---

## Safety Considerations

- **Disease-level cautions (from the knowledge graph, not label text)**: The knowledge graph links buprenorphine to contraindication or caution in several conditions, including:
  - Respiratory: chronic obstructive pulmonary disease, respiratory failure
  - Cardiac/autonomic: long QT syndrome, torsades de pointes, orthostatic hypotension
  - Liver: liver disease, chronic hepatitis B and C
  - Gastrointestinal: paralytic ileus, intestinal obstruction
  - Endocrine: adrenocortical insufficiency, hypothyroidism
  - Other: benign prostatic hyperplasia, intracranial hypertension, drug dependence/substance-related disorders
- **Drug Interactions**: 100 interactions were found. Examples of **Major** interactions include alvimopan, bupropion, morphine, cisapride and dolasetron. Many **Moderate** interactions were also found (for example famotidine, loperamide, atropine, dexamethasone, clarithromycin).

For label-based warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. The single publication is a perioperative case report and does not show efficacy, and no clinical trials exist. Safety in porphyria is itself an open question.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- A dedicated assessment of buprenorphine's porphyrinogenic risk
- Any mechanistic or clinical studies of opioids in acute intermittent porphyria, which currently do not exist in the data reviewed
- Approved indication text and dosage forms for the Canadian licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

