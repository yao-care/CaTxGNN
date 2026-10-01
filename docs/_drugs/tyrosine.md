---
layout: default
title: Tyrosine
parent: Model Prediction Only (L5)
nav_order: 949
evidence_level: L5
indication_count: 10
---

# Tyrosine
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

# Tyrosine: From Parenteral Nutrition Component to Cauda Equina Syndrome

## One-Sentence Summary

Tyrosine is an amino acid used in parenteral nutrition products on the Canadian market (for example CLINIMIX and TRAVASOL). The TxGNN model predicts it may be effective for **cauda equina syndrome**, but there are **0 clinical trials** and **1 publication**, and that publication is a case report that does not test tyrosine as a treatment. The prediction is currently a model output only, and the recommended decision is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence records. The licensed products (CLINIMIX, TRAVASOL) are amino acid parenteral nutrition products. |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tyrosine is a nutritional amino acid and part of amino acid solutions, with a role as a building block for protein. Beyond that, no therapeutic mechanism has been established for cauda equina syndrome.

Cauda equina syndrome is compression of the lumbosacral nerve roots, and its treatment is urgent surgical decompression. Tyrosine is a precursor of catecholamines (dopamine, norepinephrine), thyroid hormones and melanin. None of these pathways has a recognised role in treating nerve root compression, so no credible mechanistic link can be drawn.

The high score (0.998) is a graph-based prediction with no clinical support. The only retrieved publication is a case report of clear cell sarcoma arising from the S1 nerve root, which was mistaken for a benign schwannoma. It is about a tumour, not about tyrosine therapy or cauda equina syndrome. Its link to tyrosine is indirect at best, through melanin biosynthesis, and that is not therapeutic evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17341045](https://pubmed.ncbi.nlm.nih.gov/17341045/) | 2006 | Case report | Neurosurgical Focus | Clear cell sarcoma arising from the S1 nerve root, previously diagnosed as psammomatous melanotic schwannoma. It does not test tyrosine as an intervention. |

---

## Canada Market Information

The Canadian records list 20 licences in total. Dosage form, manufacturer and approved indication text are not provided for the five main authorisations below.

| DIN | Product Name |
|---------|------|
| 2046709 | CLINIMIX |
| 2013932 | CLINIMIX |
| 2013940 | CLINIMIX |
| 872296 | TRAVASOL |
| 2013886 | CLINIMIX |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-drug interaction records were found for tyrosine in the data sources queried.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials, and the single publication is an unrelated case report. No mechanism connects tyrosine to cauda equina syndrome, so this should not advance to safety screening or further investment.

**To proceed, the following is needed:**
- A plausible biological hypothesis for tyrosine in nerve root compression or injury, supported by preclinical data
- Mechanism of action data for tyrosine (for example from DrugBank)
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Confirmation of the original approved indication from Canadian product monographs
- Evaluation of the other nine predicted indications, whose evidence is also weak. The highest are postural orthostatic tachycardia syndrome and hyperthyroxinemia (L4, indirect evidence only). For hyperthyroxinemia, supplementing a thyroid hormone precursor raises a safety concern.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

