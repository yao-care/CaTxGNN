---
layout: default
title: Desonide
parent: Model Prediction Only (L5)
nav_order: 263
evidence_level: L5
indication_count: 10
---

# Desonide
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

# Desonide: From Topical Corticosteroid Therapy to Polyp of Vocal Cord

## One-Sentence Summary

Desonide is a low-potency topical corticosteroid. The licence data provided do not state its approved indication.
The TxGNN model predicts it may be effective for **polyp of vocal cord**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so it is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data (desonide is a low-potency topical corticosteroid) |
| Predicted New Indication | Polyp of vocal cord |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Desonide is a low-potency topical corticosteroid. Its glucocorticoid anti-inflammatory action could plausibly relate to inflammatory, polyp-like lesions, but this link is speculative.

Several practical problems weaken the prediction:

- **Delivery route:** Desonide's cream and ointment formulations are designed for skin. They are not suited to reach the vocal cord.
- **Graph-based score:** The score likely reflects graph-neighbourhood similarity across polyp-type diseases rather than a drug-specific signal.

The other top-ranked predictions show the same pattern. All ten are polyp or polyp-like lesions with scores of about 99.90–99.91%:

- middle ear polyp
- external auditory canal polyp
- frontal sinus polyp
- ureter polyp
- vulva polyp
- fibroepithelial polyp
- neoplastic polyp
- epulis
- uterine polyp

Each has no clinical trial or literature evidence. The external auditory canal and vulva are the most anatomically accessible sites for a topical product, but this is still only a hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2229323 | PDP-DESONIDE |
| 2229315 | PDP-DESONIDE |

Dosage form, manufacturer and approved indication text were not provided for these two authorizations.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for desonide.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no supporting trials or publications (L5). Topical skin formulations are also poorly matched to most predicted sites, such as the vocal cord, middle ear, sinus, ureter and uterus.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Detailed mechanism of action data (MOA), for example from DrugBank
- The approved indication text and dosage forms for the two DINs
- A route-compatibility assessment for each predicted site
- Any preclinical or clinical evidence of corticosteroid effect on the predicted lesion types, for example corticosteroid use in sinonasal polyposis, and whether it can be extended to desonide

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

