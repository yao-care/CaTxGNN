---
layout: default
title: Rasagiline
parent: Model Prediction Only (L5)
nav_order: 797
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Rasagiline: predicted new indication PLA2G6-associated neurodegeneration (evidence level L5). Approved use: Parkinson disease (and related parkinsonian syndromes). The Canadian…"
monitor_inn: "RASAGILINE"
predicted_indications: ["PLA2G6-associated neurodegeneration", "Rasmussen subacute encephalitis", "myelitis", "paralysis agitans, juvenile, of Hunt", "transaldolase deficiency", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis"]
---

# Rasagiline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Rasagiline: From Parkinson Disease to PLA2G6-Associated Neurodegeneration
{: .text-alpha }

## One-Sentence Summary

Rasagiline is a drug originally used to treat Parkinson disease and related parkinsonian syndromes.
The TxGNN model predicts it may be effective for **PLA2G6-associated neurodegeneration (PLAN)**, with a very high model score.
However, **no clinical trials and no publications** were found in the data compiled for this report, so the prediction rests on computation alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease (and related parkinsonian syndromes). The Canadian licence records do not include indication text. |
| Predicted New Indication | PLA2G6-associated neurodegeneration |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Rasagiline is generally known as a MAO-B inhibitor, which raises dopaminergic tone. This is the basis of its use in Parkinson disease, and this general knowledge is not drawn from the compiled data.

PLAN includes infantile neuroaxonal dystrophy and PLA2G6-related dystonia-parkinsonism (PARK14). The parkinsonian features of PARK14 overlap with rasagiline's established indication, so a symptomatic dopaminergic benefit is plausible. Rasagiline has also been proposed to have neuroprotective and anti-apoptotic properties in preclinical models.

There are important limits. PLAN is driven by defects in lipid metabolism and membrane remodelling, with iron accumulation. No direct link between MAO-B inhibition and this underlying pathology has been established. The score of 0.997 is a computational prediction only.

Other top-ranked predictions are also unsupported by trials or literature:

| Rank | Predicted Indication | Score | Comment |
|------|------|------|------|
| 2 | Rasmussen subacute encephalitis | 99.56% | Only a speculative neuroprotection link; no evidence that MAO-B inhibition affects T-cell-mediated cortical damage |
| 3 | Myelitis | 99.32% | Heterogeneous causes; no established mechanism |
| 4 | Paralysis agitans, juvenile, of Hunt | 99.25% | Historical term for juvenile parkinsonism; likely scores high because it sits close to existing indications in the ontology, not because it is a novel finding |
| 5 | Transaldolase deficiency | 99.19% | No plausible mechanistic link; liver involvement is a caution because rasagiline is metabolised in the liver |
| 6 | Polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | 99.01% | Structural developmental malformation; no plausible effect |

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
| 02491982 | JAMP RASAGILINE | Not specified | Not specified |
| 02284650 | AZILECT | Not specified | Not specified |
| 02284642 | AZILECT | Not specified | Not specified |
| 02418436 | TEVA-RASAGILINE | Not specified | Not specified |
| 02418444 | TEVA-RASAGILINE | Not specified | Not specified |

Eight valid single-ingredient licences are on record (showing the first 5). None are cancelled.

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (not label text, so these need verification against the package insert): hypertension and hypertensive disorder, multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, drug-induced dyskinesia, epilepsy, bipolar disorder, major affective disorder, liver disease, gallbladder disease, melanoma, pheochromocytoma and related adrenal or paraganglioma tumours, and several cancers (duodenum, small intestine, heart, adrenal gland).
- **Drug interactions:** 100 interactions were found in total. The first 20 retrieved include two **Major** interactions, with **bupropion** and **morphine**. The rest are Moderate, including epinephrine, cimetidine, phentermine, diethylpropion, dronabinol, diphenoxylate, difenoxin, obeticholic acid, chlorpropamide, glimepiride, and multiple insulin products (aspart, degludec, detemir, glargine, glulisine, human isophane, human regular, and inhaled rapid-acting).
- **Relevance to the predicted indication:** transaldolase deficiency involves liver dysfunction, but that is a different predicted indication from the top one. For PLAN, the available data do not show specific safety information.

Package insert warnings and contraindications were not available, so please refer to the package insert for the complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are no clinical trials or publications for PLAN. The mechanistic link is only plausible for the parkinsonian features, and not for the underlying lipid-metabolism and iron-accumulation pathology. Safety review also cannot proceed because the label warnings are missing.

**To proceed, the following is needed:**
- Obtain Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Obtain mechanism-of-action data from DrugBank
- Search for case reports, natural-history data, and preclinical studies of MAO-B inhibitors in PLAN or PARK14
- Compare PLAN with the original indications to determine whether any benefit would be symptomatic only (for example, parkinsonian features) or disease-modifying
- Assess route and formulation compatibility, and the suitability of rasagiline for paediatric patients, since dosage form and route data are currently missing
- Review the interaction with the major-level drugs (bupropion, morphine) and the knowledge-graph contraindications for a target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

