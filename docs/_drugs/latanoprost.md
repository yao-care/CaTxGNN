---
layout: default
title: Latanoprost
parent: Model Prediction Only (L5)
nav_order: 523
evidence_level: L5
indication_count: 10
---

# Latanoprost
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

# Latanoprost: From Glaucoma and Ocular Hypertension to Primary Hereditary Glaucoma

## One-Sentence Summary

Latanoprost is a topical prostaglandin F2-alpha analogue, used in eye care to lower intraocular pressure. The TxGNN model predicts it may be effective for **primary hereditary glaucoma**, with **1 clinical trial** and **0 publications** currently supporting this direction. The top prediction may be an on-label or near-label overlap rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied licence data (general knowledge: glaucoma and ocular hypertension) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 (provisional; RCT design and population not confirmed) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 17 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. From general pharmacology, latanoprost is an FP receptor agonist that lowers intraocular pressure by increasing uveoscleral outflow. This is a direct mechanistic fit for glaucoma.

The main caveat is that latanoprost is already marketed for glaucoma and ocular hypertension. The prediction may therefore be an on-label or near-label overlap rather than a new use. Efficacy in the hereditary or congenital subtype is less established, because trabecular outflow anatomy is often abnormal in these patients. The one supporting trial is in refractory pediatric glaucoma, which is closer to this subtype.

Other predictions from the model:
- **Hair disorders** (hypotrichosis simplex of the scalp, congenital hypotrichosis milia): plausible but indirect. Prostaglandin F2-alpha analogues prolong the anagen phase, and eyelash hypertrichosis is a known class effect. No trial or literature was supplied, and scalp dosing and formulation are unestablished.
- **Vascular, lymphatic and thoracic outlet conditions** (visceral calciphylaxis, thoracic outlet syndromes, angiodysplasia of stomach, blue toe syndrome, lymphangiectasis): no credible pharmacological link. Their high scores most likely reflect knowledge-graph neighbourhood artifacts.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | Completed | 37 | Latanoprost and dorzolamide for ocular pressure lowering in primary pediatric glaucoma refractory to surgery. Safety also assessed. Results not supplied. |

The registry title is truncated. Whether the population is hereditary/congenital, whether the study was randomized, and whether latanoprost was the prostaglandin analogue tested are not confirmed. The small sample limits inference.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

17 authorizations are listed. Dosage form and approved indication text were not supplied for the five shown here.

| DIN | Product Name |
|---------|------|
| 2456230 | MONOPROST |
| 2513285 | M-LATANOPROST |
| 2341085 | RIVA-LATANOPROST |
| 2373041 | MYLAN-LATANOPROST |
| 2534835 | AG-LATANOPROST |

---

## Safety Considerations

No drug interactions were found in the queried data. Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supported prediction (hereditary glaucoma) rests on one small Phase 2 trial with an unconfirmed design. It may also duplicate the existing labelled use. The remaining predictions have no clinical evidence, and most lack a credible mechanism.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text for the Canadian licences, to establish whether hereditary glaucoma is already covered
- Full NCT01527682 record and results: population, randomization, comparator, and whether latanoprost was the agent tested
- Mechanism-of-action data from DrugBank
- Published literature on latanoprost in hereditary or congenital glaucoma
- For the hair-related predictions: clinical evidence and a scalp formulation and dosing rationale

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

