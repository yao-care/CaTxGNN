---
layout: default
title: Elosulfase Alfa
parent: Model Prediction Only (L5)
nav_order: 320
evidence_level: L5
indication_count: 9
---

# Elosulfase Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Elosulfase Alfa: From Morquio A Syndrome to Scheie Syndrome

## One-Sentence Summary

Elosulfase alfa is a recombinant enzyme replacement therapy (recombinant GALNS) used for Morquio A syndrome (MPS IVA).
The TxGNN model predicts it may be effective for **Scheie syndrome** (attenuated MPS I), but there are **0 clinical trials** and only **2 publications** (general cohort studies with no efficacy data), so the prediction is unsupported by direct evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Morquio A syndrome (MPS IVA), based on the literature. The Canadian licence record does not state an indication text. |
| Predicted New Indication | Scheie syndrome |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Based on known information, elosulfase alfa is recombinant N-acetylgalactosamine-6-sulfatase (GALNS). It degrades keratan sulfate and chondroitin-6-sulfate, and its efficacy in Morquio A syndrome has been established.

Scheie syndrome is an attenuated form of MPS I caused by deficiency of a different enzyme, alpha-L-iduronidase (IDUA). This leads to accumulation of dermatan sulfate and heparan sulfate. GALNS cannot replace IDUA and does not act on these substrates, so the enzyme has no direct therapeutic link to this disease.

The high graph score most likely reflects the shared mucopolysaccharidosis/lysosomal storage neighbourhood in the knowledge graph rather than a real mechanistic relationship. The prediction should be treated as a model artifact until direct evidence appears.

For context, the same dataset ranks a broader category, "lysosomal storage disease with skeletal involvement" (which includes Morquio A), second. That entry reflects the approved use rather than true repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35005816](https://pubmed.ncbi.nlm.nih.gov/35005816/) | 2022 | Cohort | Human Mutation | Molecular characterization of 302 Iranian MPS patients. It is a diagnostic and genetic study with no treatment data. |
| [18584975](https://pubmed.ncbi.nlm.nih.gov/18584975/) | 2009 | Cohort | Pathologie Biologie | Clinical features and consanguinity in MPS I and IVA patients in Tunisia. It contains no efficacy data for elosulfase alfa. |

Neither paper evaluates elosulfase alfa in Scheie syndrome.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2427184 | VIMIZIM |

Dosage form and approved indication text are not recorded in the licence data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no efficacy publications and no plausible mechanism. GALNS does not act on the substrates that accumulate in Scheie syndrome (IDUA deficiency). The score most likely reflects graph proximity among MPS diseases rather than a real therapeutic link.

**To proceed, the following is needed:**
- Any preclinical or clinical data showing elosulfase alfa activity in IDUA-deficient models or patients (none currently exists)
- Health Canada product monograph warnings and contraindications for a safety review
- The licensed indication text and dosage form from the Canadian licence record
- Detailed mechanism of action data to support a mechanistic analysis

Where MPS I treatment is the goal, enzymes that target IDUA are the mechanistically appropriate approach.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

