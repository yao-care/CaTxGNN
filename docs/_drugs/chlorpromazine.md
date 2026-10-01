---
layout: default
title: Chlorpromazine
parent: Model Prediction Only (L5)
nav_order: 184
evidence_level: L5
indication_count: 10
---

# Chlorpromazine
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

# Chlorpromazine: From an Unrecorded Original Indication to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

Chlorpromazine is marketed in Canada as TEVA-CHLORPROMAZINE, but the source data does not record its original indication.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**, with **0 clinical trials** and **15 retrieved publications** (none clearly testing chlorpromazine for this condition).
The prediction rests on model output alone, and the drug's known retinal toxicity is a safety concern for this use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the source data |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Chlorpromazine is a prototypical antipsychotic that blocks dopamine D2 and other receptors. Nothing in the data links that mechanism to retinal dystrophy or to the extraocular anomalies in this disease category.

The 15 retrieved papers are general articles on orbital disease, congenital eye-muscle disorders and congenital eye anomalies. None of them tests chlorpromazine as a treatment. The 0.9995 score most likely reflects similarity between disease entities in the knowledge graph rather than a drug-specific biological signal.

One retrieved paper, a 1968 report on phenothiazine retinopathy, points the other way. Chlorpromazine is a phenothiazine, and it is known to cause pigmentary retinopathy and lens or corneal deposits at high cumulative doses. That makes a retinal indication a poor fit without strong evidence.

Among the other predictions, **early-onset schizophrenia** (rank 10, score 99.47%) is the only one with a clear biological rationale. It may reflect an existing label use in a younger population rather than true repurposing. Its only registered trial is observational and does not test chlorpromazine.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No randomized trials were retrieved. All entries are reviews, case reports or unclassified items, and none reports chlorpromazine efficacy in retinal dystrophy.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [5647013](https://pubmed.ncbi.nlm.nih.gov/5647013/) | 1968 | Not classified | Ophthalmologica | Report on phenothiazine retinopathy. No abstract is available. The title indicates retinal toxicity of the drug class, which is a safety signal rather than support for efficacy. |
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Seminars in Ultrasound, CT, and MR | Orbital infections, most often secondary to sinusitis. Covers clinical signs such as proptosis and visual loss. Not related to retinal dystrophy or to chlorpromazine. |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Seminars in Neurology | Systematic approach to evaluating diplopia from ocular, neurologic or extraocular-muscle causes. Diagnostic overview only. |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klinische Monatsblätter für Augenheilkunde | Congenital ptosis, its associated eye-muscle and vision abnormalities, and examination and therapy. |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | Congenital anomalies of lens size, shape and position, and their associated developmental conditions. |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Documenta Ophthalmologica | Wagner-Stickler syndrome complex: vitreoretinal degeneration with myopia, cataract and retinal detachment. It supports the disease context, not a drug effect. |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Imaging features of pediatric ocular pathologies, including congenital lesions, Coats disease and retinopathy of prematurity. |
| [19064847](https://pubmed.ncbi.nlm.nih.gov/19064847/) | 2008 | Review | Archives of Ophthalmology | Clinical features, management and outcomes in a series of orbital arteriovenous malformations. |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case report | American Journal of Ophthalmology | Two patients with unilateral cryptophthalmia and its variable clinical features. |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case report | Journal of Neuro-Ophthalmology | Isolated congenital trochlear-oculomotor synkinesis in a 6-year-old boy. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 232807 | TEVA-CHLORPROMAZINE |
| 232823 | TEVA-CHLORPROMAZINE |
| 232831 | TEVA-CHLORPROMAZINE |

Dosage form and approved indication text are not recorded in the source data for these licenses.

---

## Safety Considerations

- **Ocular toxicity (from the evidence review)**: Chlorpromazine can cause pigmentary retinopathy and lens or corneal deposits at high cumulative doses. This is directly relevant to any retinal or eye-disease indication.
- **Package insert**: Please refer to the package insert for warnings, contraindications and drug interactions. The interaction query returned no results.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a very high model score. There are no clinical trials, and the retrieved literature does not test chlorpromazine for retinal dystrophy. The drug's known retinal toxicity argues against this use.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from the DrugBank API
- Original indication and approved indication text for the three DINs
- Preclinical or mechanistic evidence linking chlorpromazine to retinal dystrophy pathways, if this indication is to be pursued at all
- A separate review of the early-onset schizophrenia prediction, including pediatric safety, since it is the only prediction with a plausible rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

