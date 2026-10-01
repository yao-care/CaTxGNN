---
layout: default
title: Buprenorphine
parent: Model Prediction Only (L5)
nav_order: 133
evidence_level: L5
indication_count: 6
---

# Buprenorphine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Buprenorphine: From Opioid Use Disorder and Pain to Acute Intermittent Porphyria

## One-Sentence Summary

Buprenorphine is a partial mu-opioid agonist and kappa antagonist, marketed in Canada as BUTRANS and SUBLOCADE products. The TxGNN model predicts it may be effective for **acute intermittent porphyria**, but there are **0 clinical trials** and only **1 publication** (a 1993 anesthesia case report), so the high score is most likely a graph-proximity artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the record (approved indication text is empty). Product names (BUTRANS, SUBLOCADE) suggest pain and opioid dependence products |
| Predicted New Indication | Acute intermittent porphyria |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 (the record lists L4, but the only paper is an anesthesia case report that does not test treatment, so this is effectively model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 18 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Buprenorphine is a mu-opioid partial agonist and kappa antagonist. Its efficacy in its original uses (pain and opioid dependence) is established, but that record contains no link to porphyria.

**No plausible therapeutic mechanism connects buprenorphine to acute intermittent porphyria.** Porphyria is a heme-biosynthesis disorder, and opioid receptor activity does not address that pathway. The high TxGNN score most likely reflects proximity in the knowledge graph, not a real biological rationale.

The only retrieved paper concerns anesthetic management of a porphyria patient. It addresses which drugs can be given safely during surgery, not treatment of the disease. Whether buprenorphine is safe in porphyria is a separate question that this report cannot settle.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8301837](https://pubmed.ncbi.nlm.nih.gov/8301837/) | 1993 | Case report | Masui (Japanese J Anesthesiology) | Anesthetic management of a 40-year-old woman with suspected acute intermittent porphyria undergoing gynecologic cancer surgery. It concerns perioperative drug choice, not treatment of the disease. |

---

## Canada Market Information

18 licenses are recorded in total. Five are shown below. Dosage form and approved indication text are not available in the record.

| DIN | Product Name |
|---------|------|
| 02341212 | BUTRANS 10 |
| 02341220 | BUTRANS 20 |
| 02450771 | BUTRANS 15 |
| 02341174 | BUTRANS 5 |
| 02483092 | SUBLOCADE |

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction records were retrieved. Porphyria safety of buprenorphine should be checked in the label separately.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials and no mechanistic rationale. The only literature is an unrelated anesthesia case report, so the prediction rests on model score alone.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Approved indication text for the Canadian licenses
- Evidence that buprenorphine has a disease-relevant effect in acute intermittent porphyria, plus a separate assessment of its porphyria safety

**Other predicted indications (all on Hold):** lingual-facial-buccal dyskinesia (10 of 19 papers supplied, none testing buprenorphine as treatment, no trials), chronic tic disorder (1 observational comorbidity paper, no trials), continuous spikes and waves during sleep, benign shuddering attacks, and extrapyramidal and movement disease (prediction only, with no trials or literature). Benign shuddering attacks and extrapyramidal and movement disease share an identical score, which suggests a shared graph-based signal, not independent evidence.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

