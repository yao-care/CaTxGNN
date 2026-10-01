---
layout: default
title: Paliperidone
parent: Model Prediction Only (L5)
nav_order: 694
evidence_level: L5
indication_count: 10
---

# Paliperidone
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

# Paliperidone: From Schizophrenia to Retinal Dystrophy (With or Without Extraocular Anomalies)

## One-Sentence Summary

Paliperidone is an atypical antipsychotic used for schizophrenia, and it is marketed in Canada as INVEGA and INVEGA TRINZA.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**, but **0 clinical trials** support this prediction.
The 15 retrieved publications are general ophthalmology papers, and none of them study paliperidone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia (taken from the prediction notes, because the license records contain no indication text) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, paliperidone is a D2/5-HT2A receptor antagonist (the active metabolite of risperidone) with proven efficacy in schizophrenia. Nothing in this pharmacology connects it to inherited retinal degeneration.

Retinal dystrophies are genetically driven degenerative conditions of the retina. Dopamine and serotonin receptor blockade has no known disease-modifying role in them. The very high TxGNN score (99.92%) most likely reflects a knowledge-graph artifact rather than biological support, so the prediction should be treated as a computational signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The publications below were retrieved for the predicted disease area. None involves paliperidone, and none is an RCT. They provide background on the disease only, not evidence for the drug.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Doc Ophthalmol | Wagner-Stickler syndrome complex: vitreoretinal degeneration with myopia, cataract and retinal detachment |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatr Radiol | Imaging and differential diagnosis of pediatric ocular pathologies |
| [19064847](https://pubmed.ncbi.nlm.nih.gov/19064847/) | 2008 | Review | Arch Ophthalmol | Clinical features and management of orbital arteriovenous malformations |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case report | Am J Ophthalmol | Two cases of unilateral cryptophthalmia |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case report | J Neuroophthalmol | Isolated trochlear-oculomotor synkinesis in a 6-year-old boy |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Unclassified | Optom Vis Sci | Synergistic divergence in congenital fibrosis of the extraocular muscles |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Unclassified | Am J Ophthalmol | Pathogenesis and treatment of maculopathy with cavitary optic disc anomalies |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Unclassified | Int J Mol Sci | Optic nerve head and retinal abnormalities in congenital fibrosis of the extraocular muscles |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Unclassified | J Binocul Vis Ocul Motil | Ophthalmoplegia and congenital cranial dysinnervation disorders |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Unclassified | Taiwan J Ophthalmol | Congenital anomalies of lens shape |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2300273 | INVEGA |
| 2300303 | INVEGA |
| 2300281 | INVEGA |
| 2455994 | INVEGA TRINZA |
| 2456001 | INVEGA TRINZA |

Showing 5 of 11 authorizations. Dosage form and approved indication text are not available in the license records.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials, no relevant literature, and no plausible mechanistic link between D2/5-HT2A antagonism and inherited retinal degeneration.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank to support any mechanistic-link analysis
- Health Canada package insert warnings and contraindications for safety screening
- Preclinical evidence in a retinal degeneration model, which would be required before any clinical consideration

**Note on other predictions:** Of the 10 predicted indications, only *treatment-refractory schizophrenia* (rank 10, score 99.80%) has clinical trials. These are four Phase 4 studies, giving Evidence Level L3 and a "Research Question" rating. It falls within the drug's approved use and has no Phase 3 RCT, so it is a better candidate for follow-up than the top-ranked prediction.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

