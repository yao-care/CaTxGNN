---
layout: default
title: Ivacaftor
parent: Moderate Evidence (L3-L4)
nav_order: 502
evidence_level: L4
indication_count: 10
---

# Ivacaftor
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Ivacaftor: From Cystic Fibrosis to Rheumatoid Arthritis

## One-Sentence Summary

Ivacaftor is a CFTR potentiator marketed in Canada as KALYDECO, and it is used in cystic fibrosis.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**,
but only **1 clinical trial** (observational, indirect) and **1 publication** (preclinical mouse study) touch on this direction. Neither tests ivacaftor in rheumatoid arthritis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cystic fibrosis (inferred from ivacaftor's CFTR potentiator role; the Canadian license records provide no indication text) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 96.97% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 15 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ivacaftor is a CFTR potentiator, its use in cystic fibrosis is established, and mechanistically it may be applicable to inflammatory disease through indirect routes.

In cystic fibrosis, CFTR dysfunction has been linked to altered neutrophil function and heightened inflammation. This offers a hypothetical, indirect route to inflammatory conditions such as rheumatoid arthritis. No RA-specific mechanism or data support the link. The high TxGNN score is a graph-based prediction, not clinical evidence.

Other top-ranked predictions for this drug (HIV infection, leprosy, cytomegalovirus infection, and several rare congenital syndromes) have no supporting studies and no plausible mechanism. Two of them, simian immunodeficiency virus infection and feline AIDS, are non-human diseases and likely graph-similarity artifacts. Rheumatoid arthritis is the only prediction with any related evidence, and that evidence is weak.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04970225](https://clinicaltrials.gov/study/NCT04970225) | NA (observational) | Completed | 47 | Analyzes function and phenotype of blood neutrophils in cystic fibrosis patients, including the effect of CFTR modulator treatment. It does not enroll RA patients and does not test ivacaftor for RA (relevance grade C, indirect context only). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28634110](https://pubmed.ncbi.nlm.nih.gov/28634110/) | 2017 | Preclinical (mouse) | Gastroenterology | In mouse models of Sjögren's syndrome and autoimmune pancreatitis, restoring CFTR activity in ducts rescued acinar cell function and reduced inflammation in pancreatic and salivary glands. It is autoimmune-related but not RA-specific. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2442620 | KALYDECO |
| 2397412 | KALYDECO |
| 2519364 | KALYDECO |
| 2442612 | KALYDECO |
| 2543451 | KALYDECO |

Dosage form, manufacturer and approved indication text are not available in the current records. Five of the 15 DINs are listed.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score, one indirect observational trial and one preclinical mouse study. No study tests ivacaftor in rheumatoid arthritis, and no RA-specific mechanism has been identified.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Detailed mechanism of action data from DrugBank
- Evidence linking CFTR potentiation to RA pathophysiology, for example synovial or neutrophil-related preclinical data
- Confirmation of the approved indication text from the Canadian license records

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

