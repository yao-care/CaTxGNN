---
layout: default
title: Levodopa
parent: Model Prediction Only (L5)
nav_order: 543
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
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

## Levodopa: From Parkinson Disease to Rasmussen Subacute Encephalitis
{: .text-alpha }

## One-Sentence Summary

Levodopa is a dopamine precursor originally used to treat Parkinson disease and related parkinsonian disorders.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**,
but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease (and related parkinsonian disorders) |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 0.9906 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs on record: at least 20) |
| Number of DINs | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for levodopa: "Levodopa, the metabolic precursor of dopamine, crosses the blood-brain barrier and presumably is converted to dopamine in the brain. This is thought to be the mechanism whereby levodopa relieves symptoms of Parkinson's disease." ([DailyMed: Inbrija (levodopa) prescribing information, Merz Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=077c0f39-a3a2-4b2b-a184-09131889dcfb), label version 2026-07-20; accessed 2026-11-19.) Based on known information, levodopa is converted to dopamine in the brain and replaces the dopamine lost in Parkinson disease and related parkinsonian disorders. In Canada it is marketed mainly in combination with carbidopa.

Rasmussen encephalitis is a rare, chronic, unilateral neuroinflammatory disease, most likely driven by T-cell-mediated cytotoxicity. It causes progressive hemispheric atrophy, intractable focal epilepsy, hemiparesis and cognitive decline. No direct mechanistic link to levodopa has been established. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, such as movement-disorder or basal ganglia phenotypes, or features resembling hemiparkinsonism-hemiatrophy syndrome, which is among levodopa's listed original indications.

Dopaminergic replacement is not known to modify the immune-mediated disease process. At most, levodopa might play a role in symptomatic treatment of rare secondary parkinsonian or dystonic features, not in treating the underlying disease. The high score should therefore be read as a hypothesis, not as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Levodopa has 20 valid single-ingredient authorizations in Canada and none cancelled. Dosage form and approved indication text were not available in the data compiled for this report.

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 00386464 | PROLOPA CAP 100-25 | BENSERAZIDE (BENSERAZIDE HYDROCHLORIDE); LEVODOPA | Marketed |
| 00386472 | PROLOPA CAP 200-50 | BENSERAZIDE (BENSERAZIDE HYDROCHLORIDE); LEVODOPA | Marketed |
| 02195941 | APO-LEVOCARB | CARBIDOPA; LEVODOPA | Marketed |
| 02195968 | APO-LEVOCARB | CARBIDOPA; LEVODOPA | Marketed |
| 02244495 | TEVA-LEVOCARBIDOPA | CARBIDOPA; LEVODOPA | Marketed |
| 02244496 | TEVA-LEVOCARBIDOPA | CARBIDOPA; LEVODOPA | Marketed |
| 02245211 | AA-LEVOCARB CR | CARBIDOPA; LEVODOPA | Marketed |
| 02272873 | AA-LEVOCARB CR | CARBIDOPA; LEVODOPA | Marketed |
| 02292165 | DUODOPA | CARBIDOPA (CARBIDOPA MONOHYDRATE); LEVODOPA | Marketed |
| 02457954 | MINT-LEVOCARB | CARBIDOPA; LEVODOPA | Marketed |
| 02457962 | MINT-LEVOCARB | CARBIDOPA; LEVODOPA | Marketed |
| 02531593 | AURO-LEVOCARB | CARBIDOPA; LEVODOPA | Marketed |
| 02531607 | AURO-LEVOCARB | CARBIDOPA; LEVODOPA | Marketed |
| 02531615 | AURO-LEVOCARB | CARBIDOPA; LEVODOPA | Marketed |
| 02546396 | JAMP LEVOCARB | CARBIDOPA; LEVODOPA | Marketed |
| 02546418 | JAMP LEVOCARB | CARBIDOPA; LEVODOPA | Marketed |
| 02546426 | JAMP LEVOCARB | CARBIDOPA; LEVODOPA | Marketed |
| 02549719 | PMS-LEVODOPA-CARBIDOPA | CARBIDOPA; LEVODOPA | Marketed |
| 02549727 | PMS-LEVODOPA-CARBIDOPA | CARBIDOPA; LEVODOPA | Marketed |
| 02549735 | PMS-LEVODOPA-CARBIDOPA | CARBIDOPA; LEVODOPA | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

The data contain only part of the DINs for this ingredient; the list may be incomplete.

<!-- licenses:end -->

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

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Inbrija (levodopa) prescribing information, Merz Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=077c0f39-a3a2-4b2b-a184-09131889dcfb) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

