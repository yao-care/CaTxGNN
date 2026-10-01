---
layout: default
title: Varenicline
parent: Model Prediction Only (L5)
nav_order: 960
evidence_level: L5
indication_count: 10
---

# Varenicline
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

# Varenicline: From Smoking Cessation to Migraine Disorder

## One-Sentence Summary

Varenicline is a nicotinic receptor partial agonist, used as a smoking cessation aid and marketed in Canada under 11 licenses.
The TxGNN model predicts it may be effective for **migraine disorder**, but **no clinical trials** and **no relevant publications** support this direction.
This is a model-only prediction, and headache is a known adverse effect of the drug.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Smoking cessation (based on the published literature; the license records contain no indication text) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. From the evidence reviewed, varenicline is a partial agonist at α4β2 nicotinic acetylcholine receptors, with activity at α7 receptors. Its efficacy in smoking cessation is established.

A link to migraine is speculative. One theoretical angle is cholinergic modulation of cortical spreading depression. However, headache is a labeled adverse effect of varenicline, so the direction of effect may be opposite to a therapeutic one.

The score is very high (99.92%), but it is not backed by any supporting clinical evidence. A related prediction, migraine with brainstem aura, is a subtype of the same condition and likely reflects the same graph neighborhood, so it is not independent support. Other top predictions, such as the hair-loss cluster, glaucoma and pulmonary hypertension, also have no supporting clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19585710](https://pubmed.ncbi.nlm.nih.gov/19585710/) | 2009 | Case report | Therapie | Cardiac arrest in a patient taking varenicline. This is a safety report and does not address migraine. |

No publication retrieved tests varenicline as a migraine treatment.

---

## Canada Market Information

Dosage form and approved indication text are not available in the license records.

| DIN | Product Name |
|---------|------|
| 2542978 | NRA-VARENICLINE |
| 2554445 | AURO-VARENICLINE |
| 2546957 | MINT-VARENICLINE |
| 2419882 | APO-VARENICLINE |
| 2554453 | AURO-VARENICLINE |

Five of the 11 licenses are shown.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

Headache is a labeled adverse effect of varenicline, which is directly relevant to a migraine indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (Evidence Level L5). No trials or relevant literature support efficacy in migraine, and the known headache adverse effect points toward a possible safety signal rather than benefit.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Detailed mechanism of action data (MOA), for example from DrugBank
- Preclinical or clinical evidence of varenicline benefit in migraine, as opposed to headache reported as an adverse event
- Original indication text from the Canadian license records, to document the approved use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

