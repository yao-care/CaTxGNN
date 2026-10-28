---
layout: default
title: Glatiramer
parent: Model Prediction Only (L5)
nav_order: 432
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Glatiramer: predicted new indication Hemoglobinopathy (evidence level L5). Approved use: Not available in the Canadian license data (glatiramer is generally u…"
monitor_inn: "Glatiramer"
predicted_indications: ["hemoglobinopathy"]
---

# Glatiramer
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Glatiramer: From Multiple Sclerosis to Hemoglobinopathy
{: .text-alpha }

## One-Sentence Summary

Glatiramer is an immunomodulating drug marketed in Canada (as COPAXONE and related products), and its original approved indication text is not available in the data compiled for this report. The TxGNN model predicts it may be effective for **hemoglobinopathy**, but there are **0 clinical trials** and only **1 loosely related publication** (a case report on natalizumab discontinuation in multiple sclerosis), so the prediction rests almost entirely on the model's score. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the Canadian license data (glatiramer is generally used in multiple sclerosis, based on the literature retrieved) |
| Predicted New Indication | Hemoglobinopathy |
| TxGNN Prediction Score | 0.9903 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 4 of 4) |
| Number of DINs | 4 (valid: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacological knowledge, glatiramer is an immunomodulator, a random amino acid copolymer that shifts T-cell responses toward Th2/regulatory phenotypes and competes with myelin antigens for MHC presentation. This is the basis of its use in multiple sclerosis.

For hemoglobinopathy, however, **no credible mechanistic link was identified**. Hemoglobinopathies are inherited disorders of globin chain synthesis or structure and are not primarily immune-mediated. The only linked paper discusses immune disorders after natalizumab discontinuation in a patient with MS who also had beta thalassemia; it does not address treating hemoglobinopathy. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence; it has no clinical support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28372806](https://pubmed.ncbi.nlm.nih.gov/28372806/) | 2017 | Review/Commentary (case report) | Revue neurologique | Describes multiple immune disorders after natalizumab discontinuation in a woman with MS and a history of beta thalassemia; it does not evaluate glatiramer as a treatment for hemoglobinopathy |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02245619 | COPAXONE | Not specified | Not specified |
| 02456915 | COPAXONE | Not specified | Not specified |
| 02460661 | GLATECT | Not specified | Not specified |
| 02541440 | GLATIRAMER ACETATE INJECTION | Not specified | Not specified |

## Safety Considerations

- **Drug Interactions**: One interaction is on record. **Natalizumab** is flagged as a **Major** interaction (DDInter).

Please refer to the package insert for other safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5). There are no registered trials, the single linked paper is not about treating hemoglobinopathy, and no mechanistic rationale connects an immunomodulator to disorders of globin synthesis. The same pattern holds for the other top-ranked predictions: most have no supporting data, and the breast carcinoma literature addresses cancer risk in MS patients rather than anti-tumour efficacy.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, to allow a proper mechanistic-link analysis
- Approved indication text, dosage forms and route information for the Canadian licenses
- Preclinical or mechanistic evidence that glatiramer has any effect in hemoglobinopathy
- A review of the Major interaction with natalizumab before any use alongside it
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

