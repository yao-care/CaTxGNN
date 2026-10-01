---
layout: default
title: Evinacumab
parent: Model Prediction Only (L5)
nav_order: 368
evidence_level: L5
indication_count: 10
---

# Evinacumab
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

# Evinacumab: From Lipid Lowering to Diabetic Cataract

## One-Sentence Summary

Evinacumab is an ANGPTL3 inhibitor that lowers LDL-C and triglycerides, and it is marketed in Canada as EVKEEZA.
The TxGNN model predicts it may be effective for **diabetic cataract**, but **no clinical trials and no publications** currently support this prediction.
It is a model-only signal, and the evidence is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence record (drug is a lipid-lowering ANGPTL3 inhibitor) |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 98.52% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on the supplied analysis, evinacumab is an ANGPTL3 inhibitor that lowers LDL-C and triglycerides. No direct link to lens pathology is documented.

The score of 98.52% comes from the knowledge graph alone. Any link to diabetic cataract would be speculative, for example through the metabolic or vascular effects of diabetes. Several other cataract subtypes (tetanic, mature, craniostenosis, immature, and type 2 diabetes-associated cataract) share an identical score of 98.45%. This suggests a shared graph-neighbourhood artifact rather than an indication-specific finding.

A more plausible lead is **diabetic retinopathy** (score 98.22%, rank 10 among the predictions). ANGPTL3 is evinacumab's direct target, and one 2026 preclinical study (PMID 41555340) reports that an ANGPTL3-integrin α5 axis drives retinal vascular leakage in diabetic retinopathy. This gives a target-specific rationale, rated L4 and labelled a "Research Question". It has no clinical trials or human efficacy data. Whether a large systemically given antibody reaches the retina at effective levels is also unaddressed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for diabetic cataract.

The only related publication in the evidence pack concerns the neighbouring prediction, diabetic retinopathy:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41555340](https://pubmed.ncbi.nlm.nih.gov/41555340/) | 2026 | Preclinical/mechanistic (inferred from title only) | J Transl Med | ANGPTL3-integrin α5 axis drives retinal vascular leakage in diabetic retinopathy |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2541769 | EVKEEZA |

Dosage form and approved indication text are not provided in the licence record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for diabetic cataract rests only on a knowledge-graph score, with no trials, no literature and no plausible mechanism. The identical scores across cataract subtypes point to a graph artifact. Diabetic retinopathy is the only related direction with a target-based rationale, and it is still preclinical.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Confirmed mechanism of action data from DrugBank, and the original approved indication from the licence record
- Review of the full text of PMID 41555340, since it was classified from the title only
- Evidence that ANGPTL3 inhibition affects lens pathology, or a decision to redirect the effort to diabetic retinopathy
- Ocular exposure and long-term ocular safety data for evinacumab, which is a large systemic antibody
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

