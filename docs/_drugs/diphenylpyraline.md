---
layout: default
title: Diphenylpyraline
parent: Model Prediction Only (L5)
nav_order: 288
evidence_level: L5
indication_count: 3
---

# Diphenylpyraline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Diphenylpyraline: From an Unrecorded Original Indication to Allergic Urticaria

## One-Sentence Summary

The record does not list an original indication for diphenylpyraline. It is marketed in Canada under 2 licences, but no approved indication text is available.
The TxGNN model predicts it may be effective for **allergic urticaria**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the record |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general drug-class knowledge (not the supplied record), diphenylpyraline is a first-generation H1 antihistamine. H1 receptor blockade is the standard mechanism for symptomatic relief of histamine-mediated conditions such as urticaria, so the top prediction is mechanistically plausible.

This may therefore be an existing class-level use rather than true repurposing. The label and regulatory status in each jurisdiction should be checked before treating it as a new candidate. The TxGNN score (0.996) is a computational prediction only.

The other two predictions are weaker:
- **Acute laryngopharyngitis (99.23%)**: No clear mechanistic link is supported by the data. The condition is mostly infectious or irritant-driven, and the drying effect of anticholinergic antihistamines could be unhelpful.
- **Nasal cavity disease (99.15%)**: H1 antagonism may ease sneezing, rhinorrhea and itching in allergic nasal conditions. The term is too broad to tie to a defined condition.

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
| 299561 | CREO-RECTAL ADULTES/ADULTS | — | — |
| 299596 | CREO-RECTAL ENFANTS/CHILDREN | — | — |

Dosage form and approved indication text are not available for either licence.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trial or literature support (Evidence Level L5, stage S0). The mechanism of action and the Canadian labelled indications are both missing, so it is unclear whether allergic urticaria is a new use or an existing class-level use.

**To proceed, the following is needed:**
- The Health Canada package insert (warnings, contraindications and approved indications), which currently blocks safety screening
- Mechanism of action data from DrugBank
- A search for trials and literature on diphenylpyraline in allergic urticaria
- Confirmation of whether allergic urticaria is already a labelled use in Canada or elsewhere
- A route-of-administration compatibility assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

