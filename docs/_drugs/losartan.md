---
layout: default
title: Losartan
parent: Model Prediction Only (L5)
nav_order: 556
evidence_level: L5
indication_count: 8
---

# Losartan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Losartan: From Its Currently Marketed Use to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Losartan is an angiotensin II type 1 (AT1) receptor blocker that is marketed in Canada.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but the evidence is thin: **0 clinical trials** and **1 preclinical publication** (a rat model).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the provided data (licence indication text is empty) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 (preclinical/mechanism studies only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Losartan blocks the angiotensin II type 1 receptor. Detailed mechanism-of-action data is not available in the provided data, so this is the only mechanistic statement supported.

Malignant hypertensive kidney injury is a form of severe hypertension-related renal damage. The one supporting paper suggests that angiotensin II and NF-κB signalling contribute to it in an animal model. Blocking the AT1 receptor is therefore biologically plausible. However, this is a mechanistic fit only. No human efficacy data exists for this indication, and the TxGNN score is a model prediction, not clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30809002](https://pubmed.ncbi.nlm.nih.gov/30809002/) | 2019 | Preclinical animal model | Hypertension Research | In rats, uninephrectomy plus salt overload was used to test whether latent renal dysfunction could be unmasked, giving a model of malignant hypertensive nephrosclerosis. It implicates angiotensin II and NF-κB signalling. The available abstract excerpt does not report losartan treatment results. |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2403323 | AURO-LOSARTAN |
| 2182815 | COZAAR |
| 2309750 | PMS-LOSARTAN |
| 2403358 | AURO-LOSARTAN |
| 2388804 | LOSARTAN |

These are 5 of the 20 authorizations. Dosage form and approved indication text are not available in the provided data.

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the queried source.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is one animal-model paper and a high model score. There are no clinical trials and no human data for this indication. This is a research question, not a candidate for development yet.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text and dosage forms for the Canadian licences
- Detailed mechanism-of-action data from DrugBank
- Preclinical or clinical studies that test losartan directly in malignant hypertensive renal disease
- A review of the other predicted indications (ranks 2–8), which are also at L4/L5 with little or no relevant evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

