---
layout: default
title: Brinzolamide
parent: Model Prediction Only (L5)
nav_order: 124
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Brinzolamide: predicted new indication Primary hereditary glaucoma (evidence level L5). Approved use: Open-angle glaucoma, ocular hypertension"
---

# Brinzolamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Brinzolamide: From Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Brinzolamide is a carbonic anhydrase inhibitor originally used to treat open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**,
but currently **no clinical trials or publications** support this direction, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma, ocular hypertension |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, brinzolamide is a carbonic anhydrase II inhibitor. It lowers intraocular pressure (IOP) by reducing aqueous humor secretion.

Raised IOP is the main modifiable driver of optic nerve damage in glaucoma, including hereditary forms such as primary congenital glaucoma and juvenile open-angle glaucoma. A pressure-lowering mechanism is therefore plausibly relevant.

The very high score likely reflects how close primary hereditary glaucoma sits to the approved indications in the knowledge graph. It may be partly a re-labeling of the existing glaucoma indication rather than a truly novel repurposing signal. Congenital forms often involve structural angle abnormalities that respond poorly to medication, so efficacy cannot be assumed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02238873 | AZOPT | Not specified | Not specified |
| 02435411 | SIMBRINZA | Not specified | Not specified |
| 02331624 | AZARGA | Not specified | Not specified |

## Safety Considerations

- **Drug Interactions**: 32 potential interactions were identified in the interaction screening, but none has a severity level assigned. Examples include:
  - Proton pump inhibitors: pantoprazole, omeprazole, lansoprazole
  - Corticosteroids: prednisone, prednisolone, dexamethasone, triamcinolone
  - Anticoagulants and antiplatelets: warfarin, clopidogrel
  - Statins: simvastatin, rosuvastatin
  - Others: potassium chloride, pioglitazone, metoclopramide, famotidine, ranitidine

Systemic carbonic anhydrase inhibitor exposure raises safety concerns in children, which matters for the congenital and pediatric forms of hereditary glaucoma.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no clinical trials or publications behind it (Evidence Level L5). The indication may largely overlap with the already-approved glaucoma space. Package insert safety information is also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap)
- Mechanism of action data from DrugBank
- A literature and trial search for brinzolamide in primary hereditary glaucoma, including pediatric and congenital subtypes
- Approved indication text and dosage forms for the three Canadian products
- Pediatric safety assessment for carbonic anhydrase inhibitor exposure
- Severity grading for the identified drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

