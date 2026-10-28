---
layout: default
title: Paliperidone
parent: Model Prediction Only (L5)
nav_order: 700
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
monitor_inn: "PALIPERIDONE"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "myopia X-linked", "syndromic myopia", "hydranencephaly (disease)", "congenital disorder of glycosylation with defective fucosylation", "myopia 26, X-linked, female-limited", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "atypical glycine encephalopathy"]
description: "Paliperidone: predicted new indication Retinal dystrophy with or without extraocular anomalies (evidence level L5). Approved use: Not recorded in the local data"
---

# Paliperidone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Paliperidone: Retinal dystrophy with or without extraocular anomalies
{: .text-alpha }

## One-Sentence Summary

Paliperidone is an antipsychotic originally used to treat schizophrenia and related psychotic disorders.
The TxGNN model predicts it may be effective for **retinal dystrophy (with or without extraocular anomalies)**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 11 of 11) |
| Number of DINs | 11 (valid: 11) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, paliperidone is a dopamine D2 and serotonin 5-HT2A receptor antagonist. Its efficacy in schizophrenia is established.

A mechanistic link to inherited retinal degeneration is hard to find. No established pathway connects D2/5-HT2A antagonism to the genetic and degenerative processes behind retinal dystrophies. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The same applies to the other top-ranked predictions, including several myopia subtypes, hydranencephaly, a glycosylation disorder and a hereditary neuropathy. None has any trial or literature support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Paliperidone has 11 valid single-ingredient authorizations in Canada, with no cancelled licences. The records compiled for this report contain no dosage form or approved-indication text. The first five are:

| DIN | Product Name |
|---------|------|
| 02300273 | INVEGA |
| 02300303 | INVEGA |
| 02300281 | INVEGA |
| 02354241 | INVEGA SUSTENNA |
| 02455994 | INVEGA TRINZA |

The remaining DINs belong to the same INVEGA, INVEGA SUSTENNA and INVEGA TRINZA product families.

---

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**: Conditions flagged include:
  - Cardiovascular and rhythm conditions: long QT syndrome (including familial), torsades de pointes, orthostatic hypotension, postural orthostatic tachycardia syndrome, hypotensive disorder, myocardial infarction and coronary thrombosis.
  - Neurological conditions: epilepsy, multiple system atrophy, basal ganglia disease, focal hand dystonia and blepharospasm.
  - Metabolic conditions: diabetes mellitus, diabetic ketoacidosis, hyperglycemia, hyperlipidemia (including familial), obesity disorder and potassium deficiency disease.
  - Haematological conditions: neutropenia, agranulocytosis and hemoglobinopathy.
  - Other conditions: Crohn disease, inflammatory bowel disease, female breast carcinoma and impaired renal function.
- **Drug Interactions**: The interaction query returned 100 records. The 20 reviewed here include two **Major** interactions:
  - Bupropion
  - Morphine

  The rest are **Moderate**:
  - Antidiabetic agents (acarbose, metformin, pioglitazone, alogliptin, albiglutide, canagliflozin, chlorpropamide)
  - Anticholinergic or gastrointestinal agents (atropine, hyoscyamine, glycopyrronium, loperamide, bisacodyl)
  - Other agents (famotidine, epinephrine, hydrocortisone, amphotericin B and its lipid complex, lorcaserin)

Please refer to the Canadian package insert for the official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The retinal dystrophy prediction has a very high model score but no clinical trials, no literature and no plausible mechanistic link (Evidence Level L5).

**To proceed, the following is needed:**
- Mechanism of action data and a documented biological rationale linking paliperidone to retinal pathways
- Preclinical evidence (for example, retinal cell or animal model studies) to move beyond model-only support
- Health Canada package insert warnings and contraindications, to complete the safety screening
- Review of the other high-scoring predictions to decide whether any warrants separate investigation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

