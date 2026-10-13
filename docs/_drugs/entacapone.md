---
layout: default
title: Entacapone
parent: Model Prediction Only (L5)
nav_order: 331
evidence_level: L5
indication_count: 10
---

# Entacapone
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

# Entacapone: From Parkinson Disease to PLA2G6-Associated Neurodegeneration

## One-Sentence Summary

Entacapone is a COMT inhibitor originally used to treat Parkinson disease and related parkinsonian syndromes.
The TxGNN model predicts it may be effective for **PLA2G6-associated neurodegeneration**,
but **no clinical trials and no publications** currently support this specific prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease (the Canadian licence records contain no indication text, so this comes from the knowledge-graph indication list) |
| Predicted New Indication | PLA2G6-associated neurodegeneration |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on what is known, entacapone is a catechol-O-methyltransferase (COMT) inhibitor used alongside levodopa. By slowing levodopa breakdown, it prolongs the levodopa effect in Parkinson disease.

PLA2G6-associated neurodegeneration includes dystonia-parkinsonism presentations. This overlaps with the motor features of Parkinson disease, so symptomatic dopaminergic modulation is plausible. However, entacapone only extends the action of levodopa. It does not address the underlying lipid-metabolism and neurodegenerative pathology of this disease. The high score may partly reflect the closeness of the disease to parkinsonism in the knowledge graph rather than independent biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered for PLA2G6-associated neurodegeneration.

## Literature Evidence

Currently no related literature available for PLA2G6-associated neurodegeneration.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02535939 | MINT-ENTACAPONE | Not listed | Not listed |
| 02375559 | TEVA-ENTACAPONE | Not listed | Not listed |
| 02380005 | SANDOZ ENTACAPONE | Not listed | Not listed |
| 02305968 | STALEVO | Not listed | Not listed |
| 02337835 | STALEVO | Not listed | Not listed |

Eight valid single-ingredient licences are on record in total; the five above are shown. No licences have been cancelled.

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text):** The graph links entacapone to contraindications in several groups.
  - Neurological and autonomic: multiple system atrophy, orthostatic hypotension, postural orthostatic tachycardia syndrome, drug-induced dyskinesia, epilepsy.
  - Psychiatric: psychotic disorders, schizoaffective disorder, anxiety disorder, mental disorder.
  - Organ disease: liver disease, kidney disease, gallbladder disease, peptic ulcer disease.
  - Eye: open-angle and angle-closure glaucoma.
  - Cardiovascular: myocardial infarction, coronary thrombosis, sudden cardiac arrest, heart conduction disease.
  - Other: diabetes mellitus, diabetic ketoacidosis, melanoma, hemoglobinopathy, diarrheal disease.
- **Drug Interactions:** 82 interactions were identified in total. The ones reviewed are mostly moderate-level.
  - Moderate: epinephrine (including ophthalmic and topical forms), morphine (including liposomal), dronabinol, opium, nabilone, metoclopramide, iron.
  - Severity not classified: pantoprazole, omeprazole, lansoprazole, doxycycline, metformin, atropine, lactulose, prednisone, simvastatin, potassium chloride.
- **Context:** Liver safety would be a particular concern in a fragile paediatric population, where this condition often presents.

Please refer to the package insert for official warnings and contraindications, as label text was not available.

## Other Predicted Indications Reviewed

| Rank | Predicted Indication | Score | Evidence Level | Note |
|---|---|---|---|---|
| 1 | PLA2G6-associated neurodegeneration | 99.76% | L5 | Dystonia-parkinsonism overlap; no trials or literature |
| 2 | Rasmussen subacute encephalitis | 99.73% | L5 | Immune-mediated; no clear mechanistic link |
| 3 | Myelitis | 99.63% | L5 | No known mechanistic link |
| 4 | Paralysis agitans, juvenile, of Hunt | 99.60% | L5 | Close to the original indication, but possibly an ontology-proximity effect |
| 5 | Transaldolase deficiency | 99.43% | L5 | Metabolic disorder; no plausible link |
| 6 | Lethal infantile mitochondrial myopathy | 99.28% | L5 | No mechanism; hepatic safety concern |
| 7 | Lewy body dementia | 99.25% | L4 | Shared alpha-synuclein and dopaminergic pathology; preclinical studies only |
| 8 | Fructose-1,6-bisphosphatase deficiency | 99.22% | L5 | No mechanistic link |
| 9 | Polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | 99.06% | L5 | Structural developmental defect |
| 10 | Progressive supranuclear palsy-corticobasal syndrome | 99.04% | L5 | Tauopathies respond poorly to levodopa-based therapy |

Two lower-ranked predictions have a small amount of related material:

- **Lewy body dementia:** [NCT04246437](https://clinicaltrials.gov/study/NCT04246437) is a Phase 1 [18F]F-DOPA imaging study in autonomic failure. It is a diagnostic study that does not test entacapone, so relevance is tangential. Two preclinical papers are on record: [39259788](https://pubmed.ncbi.nlm.nih.gov/39259788/) (2024, Science Advances, iPSC organoid model) and [23913715](https://pubmed.ncbi.nlm.nih.gov/23913715/) (2013, J Neurosci Res, in vitro work on antiparkinsonian agents and oligomer formation).
- **Progressive supranuclear palsy-corticobasal syndrome:** [NCT02994719](https://clinicaltrials.gov/study/NCT02994719) is an observational gait analysis study with no entacapone intervention.

Neither provides direct evidence of efficacy.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The PLA2G6-associated neurodegeneration prediction has a high model score but no supporting trials or literature (Evidence Level L5). Entacapone would at most offer symptomatic benefit, and its safety profile has not been reviewed against this population.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, which are currently missing and block safety screening
- Detailed mechanism-of-action data for entacapone
- Literature or case-level evidence of entacapone, or levodopa combinations, used in PLA2G6-associated dystonia-parkinsonism
- A safety assessment for paediatric and hepatic risk in this population
- A closer look at the Lewy body dementia direction, which has the most plausible biological link among the ten predictions, as a possible research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

