---
layout: default
title: Lifitegrast
parent: Model Prediction Only (L5)
nav_order: 544
evidence_level: L5
indication_count: 6
---

# Lifitegrast
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

# Lifitegrast: From Dry Eye Disease to Penile Fibromatosis

## One-Sentence Summary

Lifitegrast (marketed in Canada as XIIDRA) is an LFA-1 antagonist, generally known as a treatment for dry eye disease.
The TxGNN model predicts it may be effective for **penile fibromatosis** (Peyronie's disease), but **no clinical trials and no publications** currently support this prediction.
It rests on a model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license record (Xiidra is generally known as a dry eye disease treatment) |
| Predicted New Indication | Penile fibromatosis |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Based on known information, lifitegrast blocks the interaction between LFA-1 and ICAM-1, which limits T-cell adhesion and inflammation on the ocular surface. Its efficacy in dry eye disease has been established, but it is unclear whether this mechanism applies to penile fibromatosis.

The prediction is weakly supported. Peyronie's disease is a fibrotic condition driven mainly by myofibroblast activity and TGF-beta/TNF signaling, and no direct role for LFA-1 antagonism has been documented. The high score likely reflects proximity in the knowledge graph to other fibrotic or inflammatory conditions. Related predictions (palmar fibromatosis, Ledderhose disease, infantile digital fibromatosis) are probably redundant with this one. A topical ophthalmic product is also a poor fit for a penile condition.

A better-supported prediction in the same output is **diabetic retinopathy** (score 99.03%, evidence level L4). Leukocyte adhesion and leukostasis through LFA-1/ICAM-1 plausibly contribute to retinal capillary damage. Support there is still indirect:
- One completed Phase 1/2 dry eye trial (NCT04030962) whose relevance to diabetic retinopathy is unverified.
- A Phase 1b safety study of topical SAR 1118, the former name of lifitegrast (PMID 22538219).
- A proteomics/genetic association study (PMID 41158172).
- Retinal penetration from a topical eye drop remains unresolved.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2471027 | XIIDRA | Not specified in record | Not specified in record |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The penile fibromatosis prediction has no trials, no literature and no plausible mechanistic link (evidence level L5). It is best treated as a model artifact rather than an actionable repurposing candidate.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmed mechanism of action data from DrugBank
- Preclinical evidence linking LFA-1/ICAM-1 blockade to fibroblast or myofibroblast activity in fibromatosis
- Consideration of a route of administration suited to the target tissue
- Manual review of NCT04030962 and a retinal-penetration assessment, if the diabetic retinopathy direction is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

