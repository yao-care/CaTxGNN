---
layout: default
title: Fludrocortisone
parent: Model Prediction Only (L5)
nav_order: 391
evidence_level: L5
indication_count: 8
---

# Fludrocortisone
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

# Fludrocortisone: From Mineralocorticoid Replacement to Primary Cutaneous T-Cell Lymphoma

## One-Sentence Summary

Fludrocortisone is a synthetic corticosteroid with mainly mineralocorticoid activity. It is marketed in Canada, but the data compiled for this report do not list an approved indication.
The TxGNN model predicts it may be effective for **primary cutaneous T-cell lymphoma**, but **no clinical trials and no publications** currently support this prediction, so it should be treated as a computational hypothesis only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Primary cutaneous T-cell lymphoma |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, fludrocortisone is a mineralocorticoid with some glucocorticoid activity.

Systemic and topical corticosteroids have a role in managing cutaneous T-cell lymphoma, which is the only plausible link to this prediction. However, fludrocortisone is not an established agent for this disease. The very high TxGNN score is a computational output only. No trials or literature support it, and no specific mechanistic link could be identified from the available data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for primary cutaneous T-cell lymphoma.

For context, the other predicted indications also lack clinical trials. The only one with notable literature is "eye disease" (rank 6, evidence level L4, recommendation: Research Question). The most relevant items are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36161841](https://pubmed.ncbi.nlm.nih.gov/36161841/) | 2022 | Phase 1B study | BMJ Open Ophthalmology | Safety and tolerability of single-dose intravitreal fludrocortisone acetate in geographic atrophy |
| [34509498](https://pubmed.ncbi.nlm.nih.gov/34509498/) | 2021 | Preclinical | Experimental Eye Research | Anti-inflammatory and neuroprotective properties of fludrocortisone in retinal degeneration |
| [11008895](https://pubmed.ncbi.nlm.nih.gov/11008895/) | 1999 | Clinical study | International Ophthalmology | Fludrocortisone for systemic hypotension in primary open-angle glaucoma patients |

The remaining retrieved papers are mostly reviews and case reports on dysautonomia, Parkinson's non-motor symptoms, autoimmune polyglandular syndromes and Sjögren's-related renal tubular acidosis. They provide no direct support for an ocular indication.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02552248 | JAMP FLUDROCORTISONE | Not specified | Not specified |
| 02086026 | FLORINEF | Not specified | Not specified |

## Safety Considerations

**Drug Interactions:** 446 interactions were identified. Examples of those listed:
- **Major:** Bupropion
- **Moderate:** antidiabetic agents (acarbose, pioglitazone, alogliptin, canagliflozin, dapagliflozin, empagliflozin, linagliptin, chlorpropamide, albiglutide, dulaglutide), amphotericin B, aprepitant, acetylsalicylic acid, clarithromycin, bisacodyl, picosulfuric acid, oxandrolone, oxymetholone

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for primary cutaneous T-cell lymphoma rests only on a model score, with no clinical trials, no literature and no supported mechanistic link. The other top predictions (cystic teratoma, dermoid cysts, exostosis and broad orbital categories) are similarly unsupported. The only signal worth following is a preclinical and early clinical one for retinal degeneration (geographic atrophy), which is a separate research question.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data (for example from DrugBank)
- Approved indication text for the two Canadian licences
- For primary cutaneous T-cell lymphoma, preclinical or mechanistic evidence showing a rationale for fludrocortisone over established corticosteroids
- If the ocular direction is pursued, a specific condition (for example geographic atrophy) instead of the broad "eye disease" category, and a route-of-administration assessment, since the early clinical study used intravitreal injection
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

