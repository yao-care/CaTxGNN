---
layout: default
title: Quetiapine
parent: Model Prediction Only (L5)
nav_order: 779
evidence_level: L5
indication_count: 10
---

# Quetiapine
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

# Quetiapine: From Antipsychotic Use to Retinal Dystrophy

## One-Sentence Summary

Quetiapine is an atypical antipsychotic that is already marketed in Canada. The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**, but there are **0 clinical trials** and **0 relevant publications** supporting this. The 15 retrieved papers are about congenital eye anomalies and never mention quetiapine, so this prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian licence records provided (quetiapine is generally known as an atypical antipsychotic) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Quetiapine acts mainly through 5-HT2A and D2 receptor antagonism, with additional H1 and alpha-1 activity. None of these actions is known to affect inherited retinal degeneration.

The reviewed rationale found **no credible mechanistic link** between quetiapine and retinal dystrophy. The retrieved literature appears to be keyword-matched noise. The score of 0.996 reflects a graph-based pattern in the knowledge graph, not biological or clinical evidence. This prediction should not be treated as a real repurposing lead.

**Worth noting:** among the other top-10 predictions, **trichotillomania** (rank 8, score 99.38%) is the only one with a plausible link. It is a body-focused repetitive behaviour disorder on the obsessive-compulsive spectrum. Seven publications address it, two of them directly about quetiapine, but all are case reports or narrative reviews, and one case report describes obsessive-compulsive symptoms emerging on quetiapine. It is graded L4 and flagged as a Research Question, and it deserves more attention than the rank 1 prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the 15 retrieved papers mentions quetiapine. The 10 shown below are all about congenital or orbital eye conditions and are not evidence for this prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Seminars in Ultrasound, CT, and MR | Orbital infections, mostly sinusitis-related; imaging and clinical features |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Seminars in Neurology | Systematic approach to evaluating diplopia |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klin Monbl Augenheilkd | Congenital ptosis and associated eye findings |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | Congenital anomalies of lens shape |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Documenta Ophthalmologica | Wagner-Stickler syndrome complex (vitreoretinal degeneration with extraocular features) |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Imaging of pediatric ocular pathologies |
| [19064847](https://pubmed.ncbi.nlm.nih.gov/19064847/) | 2008 | Review | Archives of Ophthalmology | Orbital arteriovenous malformations: features and outcomes |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case report | American Journal of Ophthalmology | Two cases of unilateral cryptophthalmia |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case report | Journal of Neuro-Ophthalmology | Congenital trochlear-oculomotor synkinesis in a 6-year-old |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Case report | Optometry and Vision Science | Synergistic divergence in congenital fibrosis of the extraocular muscles |

## Canada Market Information

Showing 5 of 20 authorizations. Dosage form and indication text are not available in the records provided.

| DIN | Product Name |
|---------|------|
| 02296594 | PMS-QUETIAPINE |
| 02244107 | SEROQUEL |
| 02317893 | QUETIAPINE |
| 02321513 | SEROQUEL XR |
| 02317370 | PRO-QUETIAPINE |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials, no relevant literature and no plausible mechanism, so it rests on the model score alone (L5). The 15 retrieved papers are keyword noise and should not be read as support.

**To proceed, the following is needed:**
- Any mechanistic or preclinical rationale linking quetiapine pharmacology to retinal degeneration. Without it, this candidate should not advance.
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening.
- Detailed mechanism of action data from DrugBank.
- Redirect effort to **trichotillomania** (rank 8). That would need a controlled study that monitors metabolic and sedative adverse effects and the risk of treatment-emergent obsessive-compulsive symptoms.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

