---
layout: default
title: Levodopa
parent: Model Prediction Only (L5)
nav_order: 543
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Levodopa: predicted new indication Rasmussen subacute encephalitis (evidence level L5). Approved use: Parkinson disease (and related parkinsonian disorders)"
monitor_inn: "LEVODOPA"
predicted_indications: ["Rasmussen subacute encephalitis"]
---

# Levodopa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Levodopa: From Parkinson Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Levodopa is a dopamine precursor originally used to treat Parkinson disease and related parkinsonian disorders.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**,
but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease (and related parkinsonian disorders) |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, levodopa is converted to dopamine in the brain and replaces the dopamine lost in Parkinson disease and related parkinsonian disorders. In Canada it is marketed mainly in combination with carbidopa.

Rasmussen encephalitis is a rare, chronic, unilateral neuroinflammatory disease, most likely driven by T-cell-mediated cytotoxicity. It causes progressive hemispheric atrophy, intractable focal epilepsy, hemiparesis and cognitive decline. No direct mechanistic link to levodopa has been established. The prediction may arise from shared neighbours in the knowledge graph, such as movement-disorder or basal ganglia phenotypes, or from features resembling hemiparkinsonism-hemiatrophy syndrome, which is among levodopa's listed original indications.

Dopaminergic replacement is not known to modify the immune-mediated disease process. At most, levodopa might play a role in symptomatic treatment of rare secondary parkinsonian or dystonic features, not in treating the underlying disease. The high score should therefore be read as a hypothesis, not as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Levodopa has 20 valid single-ingredient authorizations in Canada and none cancelled. Dosage form and approved indication text were not available in the data compiled for this report. Five main authorizations are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02292165 | DUODOPA | Not available | Not available |
| 00386472 | PROLOPA CAP 200-50 | Not available | Not available |
| 00386464 | PROLOPA CAP 100-25 | Not available | Not available |
| 02195968 | APO-LEVOCARB | Not available | Not available |
| 02244495 | TEVA-LEVOCARBIDOPA | Not available | Not available |

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for full safety information.

**Disease contraindications from the knowledge graph** (derived from drug-disease relationship data, not label text, and to be verified against the label). The graph lists the following conditions:
- Neurological and autonomic: multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, drug-induced dyskinesia, epilepsy
- Psychiatric: anxiety disorder, neurotic disorder, dysthymic disorder, psychotic disorder, schizophreniform disorder, schizoaffective disorder, mental disorder
- Cardiovascular: myocardial infarction, coronary thrombosis, sudden cardiac arrest, heart conduction disease
- Gastrointestinal and hepatobiliary: gastric ulcer, peptic ulcer disease, diarrheal disease, liver disease, gallbladder disease
- Metabolic and renal: diabetes mellitus, diabetic ketoacidosis, kidney disease, pyoureter
- Eye: open-angle glaucoma, angle-closure glaucoma
- Other: melanoma, hemoglobinopathy

Epilepsy is on this list and is a core feature of Rasmussen encephalitis, which deserves particular attention for this predicted indication.

**Drug interactions:** The query returned 100 interactions in total. The 20 retrieved are mostly Moderate or Minor.
- Moderate: epinephrine, ephedrine, bupropion, metronidazole, pyridoxine, iron, metoclopramide, and anticholinergics (atropine, hyoscyamine, methscopolamine, glycopyrronium, clidinium, dicyclomine, mepenzolate)
- Minor: antacids (aluminum hydroxide, calcium carbonate, magaldrate, magnesium carbonate, magnesium hydroxide, magnesium oxide)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a high model prediction score. There are no registered trials or publications, and no plausible mechanism for treating the immune-mediated pathology of Rasmussen encephalitis. The knowledge graph also lists epilepsy as a contraindication, a notable concern for this disease.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (a blocking gap for safety screening)
- Mechanism of action data for levodopa
- A literature review for any reports of levodopa use in Rasmussen encephalitis or hemiparkinsonism-hemiatrophy
- A clear clinical rationale for the target use, such as symptomatic management of secondary parkinsonism, rather than disease modification
- Assessment of seizure risk in this population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

