---
layout: default
title: Asenapine
parent: Model Prediction Only (L5)
nav_order: 74
evidence_level: L5
indication_count: 10
---

# Asenapine
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

# Asenapine: From Schizophrenia and Bipolar I Mania to Retinal Dystrophy

## One-Sentence Summary

Asenapine is an atypical antipsychotic used for schizophrenia and manic or mixed episodes of bipolar I disorder.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**, but this is a **graph-based prediction only**, with **0 clinical trials** and **no relevant publications** supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

The Canadian license records in the Evidence Pack do not include approved indication text. The original indications above come from the literature in the pack.

---

## Why is This Prediction Reasonable?

Currently, the mechanism-of-action record for this drug is incomplete. Asenapine is known as a D2/5-HT2A/5-HT2C/5-HT7 antagonist with broad monoaminergic activity, and it also has α2 antagonism. This profile fits its use in schizophrenia and bipolar mania.

**The prediction is weak.** No established mechanistic link connects this receptor profile to inherited retinal degeneration. The high score (0.998) comes only from patterns in the knowledge graph. Antipsychotic ocular effects, such as lens or retinal toxicity, point toward risk rather than benefit.

The other top-ranked predictions have similar problems. Most are monogenic or structural congenital disorders, such as X-linked myopia, hydranencephaly and glycosylation disorders. Receptor antagonism is not a plausible disease-modifying mechanism for these, and none has any clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The 15 retrieved papers are general ophthalmology background articles on orbital, extraocular muscle and congenital eye conditions. **None studies asenapine, and none tests any drug for retinal dystrophy.** They show that the search matched on disease terms only, not that the drug works. The 10 listed below are ranked by study type (reviews before case reports).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Semin Ultrasound CT MR | Orbital infections, mostly secondary to sinusitis. No drug relevance. |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Doc Ophthalmol | Wagner-Stickler syndrome complex: vitreoretinal degeneration with extraocular manifestations. No treatment data. |
| [19064847](https://pubmed.ncbi.nlm.nih.gov/19064847/) | 2008 | Review | Arch Ophthalmol | Clinical features and outcomes of orbital arteriovenous malformations. |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Semin Neurol | Approach to evaluating diplopia. |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klin Monbl Augenheilkd | Congenital ptosis, its forms and examination. |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan J Ophthalmol | Congenital anomalies of lens shape. |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatr Radiol | Imaging features of pediatric ocular pathologies. |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case report | Am J Ophthalmol | Two patients with unilateral cryptophthalmia. |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Case report | Optom Vis Sci | Synergistic divergence in congenital fibrosis of the extraocular muscles. |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case report | J Neuroophthalmol | Isolated congenital trochlear-oculomotor synkinesis in a child. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2374803 | SAPHRIS |
| 2374811 | SAPHRIS |

Dosage form, manufacturer and approved indication text are not available in the current data.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the data. Ocular effects of antipsychotics are a theoretical concern for any use in retinal disease.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no relevant literature and no plausible mechanism. Antipsychotic ocular effects suggest possible harm rather than benefit in a retinal disorder.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking asenapine pharmacology to retinal degeneration, supported by preclinical data
- Health Canada package insert warnings and contraindications
- Complete mechanism-of-action data from DrugBank
- Approved indication text for the Canadian licenses, to confirm the original indication

**Note:** The tenth-ranked prediction, major affective disorder, has Phase 3 RCT support (L1). However, it is largely an existing approved use in bipolar I mania, not true repurposing, and it does not cover unipolar depression. It should be checked against the label before it is treated as a new indication.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

