---
layout: default
title: Paliperidone
parent: Model Prediction Only (L5)
nav_order: 700
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Paliperidone: predicted new indication Retinal dystrophy with or without extraocular anomalies (evidence level L5). Approved use: Schizophrenia, schizoaffective disorder, schizophreniform disorder…"
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

# Paliperidone: From Schizophrenia to Retinal Dystrophy

## One-Sentence Summary

Paliperidone is an antipsychotic originally used to treat schizophrenia and related psychotic disorders.
The TxGNN model predicts it may be effective for **retinal dystrophy (with or without extraocular anomalies)**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia, schizoaffective disorder, schizophreniform disorder, psychotic disorder (from the knowledge graph; the Canadian licence records contain no indication text) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, paliperidone is a dopamine D2 and serotonin 5-HT2A receptor antagonist. Its efficacy in schizophrenia is established.

A mechanistic link to inherited retinal degeneration is hard to find. No established pathway connects D2/5-HT2A antagonism to the genetic and degenerative processes behind retinal dystrophies. The high score is most likely a graph-based artifact of the knowledge graph rather than a biologically grounded signal.

The same applies to the other top-ranked predictions, including several myopia subtypes, hydranencephaly, a glycosylation disorder and a hereditary neuropathy. None has any trial or literature support. The only prediction with any supporting studies is treatment-refractory schizophrenia. That is a sub-population of the original indication, not a true repurposing target, and the three Phase 4 trials found do not show paliperidone-specific efficacy there.

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
The retinal dystrophy prediction has a very high model score but no clinical trials, no literature and no plausible mechanistic link (Evidence Level L5). The only prediction with supporting studies is treatment-refractory schizophrenia, which is not a new indication.

**To proceed, the following is needed:**
- Mechanism of action data and a documented biological rationale linking paliperidone to retinal pathways
- Preclinical evidence (for example, retinal cell or animal model studies) to move beyond model-only support
- Health Canada package insert warnings and contraindications, to complete the safety screening
- Review of the other high-scoring predictions to decide whether any warrants separate investigation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

