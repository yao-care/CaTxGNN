---
layout: default
title: Vancomycin
parent: Model Prediction Only (L5)
nav_order: 958
evidence_level: L5
indication_count: 10
---

# Vancomycin
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

# Vancomycin: From Gram-Positive Bacterial Infections to Diffuse Scleroderma

## One-Sentence Summary

Vancomycin is a glycopeptide antibiotic used against Gram-positive bacterial infections. The Canadian license records supplied here do not state an indication.
The TxGNN model predicts it may be effective for **diffuse scleroderma**, but there are **0 clinical trials** and only **1 unrelated case report** behind this prediction. The high score is most likely a knowledge-graph artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied license records. Vancomycin is generally a glycopeptide antibiotic for Gram-positive infections |
| Predicted New Indication | Diffuse scleroderma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

It is not, based on the available data. Detailed mechanism of action data is not available in the Evidence Pack. Vancomycin is known to inhibit cell wall synthesis in Gram-positive bacteria.

Diffuse scleroderma is an autoimmune, fibrotic disease with no known antibacterial target. No plausible mechanistic link could be identified between the drug's antibacterial action and this condition.

The score of 0.999 reflects a computational association in the knowledge graph. It is not supported by biological or clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Case report | The American Journal of Case Reports | A 56-year-old man with a diffuse exfoliative rash, sepsis and eosinophilia, evaluated for erythroderma. The paper is not about scleroderma and does not show a vancomycin benefit for it. |

---

## Canada Market Information

Vancomycin has 20 licenses in Canada. The supplied records do not include dosage form or approved indication text. Five main authorizations are listed below.

| DIN | Product Name |
|---------|------|
| 02407752 | JAMP VANCOMYCIN |
| 02394626 | VANCOMYCIN HYDROCHLORIDE FOR INJECTION, USP |
| 02406543 | VANCOMYCIN HYDROCHLORIDE FOR INJECTION, USP |
| 02139243 | VANCOMYCIN HYDROCHLORIDE FOR INJECTION, USP |
| 02533006 | VANCOMYCIN HYDROCHLORIDE FOR INJECTION, USP |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found for this drug in the Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no mechanistic support, no clinical trials, and only one unrelated case report (L5). Vancomycin has no known target in an autoimmune fibrotic disease, so this prediction should not be pursued.

**To proceed, the following is needed:**
- Direct preclinical or clinical evidence linking vancomycin to scleroderma pathology, with no such evidence currently available
- Mechanism of action data and Health Canada package insert warnings and contraindications

**Other predictions for this drug:** Most of the other nine predictions have no plausible link either. The exception is **streptococcal pneumonia** (rank 9, score 99.60%, L4), which is biologically plausible because *S. pneumoniae* is Gram-positive and vancomycin is active against it. This is better viewed as an extension of its existing antibacterial spectrum than as true repurposing, and no efficacy trial exists in the supplied data. If this drug is pursued further, that indication is the one to evaluate.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

