---
layout: default
title: Entacapone
parent: Model Prediction Only (L5)
nav_order: 329
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

# Entacapone: From Parkinson's Disease to PLA2G6-Associated Neurodegeneration

## One-Sentence Summary

Entacapone is a COMT inhibitor used as an add-on to levodopa in Parkinson's disease. The TxGNN model predicts it may be effective for **PLA2G6-associated neurodegeneration**, but **no clinical trials and no publications** currently support this specific prediction, so it is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (levodopa adjunct; not stated in the Canadian license records) |
| Predicted New Indication | PLA2G6-associated neurodegeneration |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, entacapone acts by peripheral COMT inhibition, which extends levodopa exposure. Its efficacy as a levodopa adjunct in Parkinson's disease is established.

PLA2G6-associated neurodegeneration can present with dystonia-parkinsonism (PARK14). A COMT inhibitor could therefore plausibly modulate the dopaminergic symptoms of this condition.

The mechanistic link is only partial. The underlying pathology is disordered lipid metabolism and brain iron accumulation, and entacapone does not address either. At best it might offer symptomatic relief, not disease modification. No supporting data were provided for this prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Eight DINs are on record. Five are listed below. The dosage form and approved indication fields are empty in the source data.

| DIN | Product Name |
|---------|------|
| 2535939 | MINT-ENTACAPONE |
| 2375559 | TEVA-ENTACAPONE |
| 2380005 | SANDOZ ENTACAPONE |
| 2305968 | STALEVO |
| 2337835 | STALEVO |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score alone (L5), with no trials or literature. The disease's core pathology (lipid metabolism and iron accumulation) is not targeted by entacapone.

Among the other top-ranked predictions, two are more biologically plausible but still lack therapeutic evidence:
- **Juvenile parkinsonism (Hunt type):** flagged as a Research Question. A literature review of levodopa/COMT inhibitor use in early-onset parkinsonism is a reasonable next step.
- **Lewy body dementia:** L4 evidence with three preclinical or review publications. The only trial is a diagnostic imaging study, not a treatment trial.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A targeted literature search on COMT inhibitors in PLA2G6-associated neurodegeneration and PARK14 dystonia-parkinsonism
- Original indication text from the Canadian license records
- Dosage form and route data, to check route compatibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

