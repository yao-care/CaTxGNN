---
layout: default
title: Rasagiline
parent: Model Prediction Only (L5)
nav_order: 790
evidence_level: L5
indication_count: 6
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Rasagiline: From Parkinson's Disease to PLA2G6-Associated Neurodegeneration

## One-Sentence Summary

Rasagiline is a selective MAO-B inhibitor, used for Parkinson's disease and marketed in Canada under 8 DINs.
The TxGNN model predicts it may be useful for **PLA2G6-associated neurodegeneration**, a very rare disorder with parkinsonian features.
This prediction rests on the model score alone: **0 clinical trials** and **0 publications** were found to support it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (not stated in the Canadian license records supplied) |
| Predicted New Indication | PLA2G6-associated neurodegeneration |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Rasagiline is a selective MAO-B inhibitor. By blocking the breakdown of dopamine in the brain, it raises striatal dopamine and eases the motor symptoms of Parkinson's disease. The supplied dataset does not include a formal mechanism-of-action entry, so this description comes from the drug's known pharmacology.

PLA2G6-associated neurodegeneration includes a dystonia-parkinsonism form (PARK14), which shares dopaminergic and parkinsonian features with Parkinson's disease. A symptomatic benefit from boosting dopamine is therefore biologically plausible. The high score probably reflects how close the two diseases sit in the knowledge graph. There is no support here for any disease-modifying effect.

The disease is ultra-rare, and the supplied data show no clinical signal for this use. The other five predictions (Rasmussen encephalitis, myelitis, juvenile parkinsonism of Hunt, transaldolase deficiency, and a polymicrogyria syndrome) also have only model scores behind them. Most have no clear mechanistic link to MAO-B inhibition. Juvenile parkinsonism of Hunt is the exception, since it overlaps with the known Parkinson's disease space.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Five of the 8 authorizations are listed below. The records supplied do not include dosage form or approved indication text.

| DIN | Product Name |
|---------|------|
| 02491982 | JAMP RASAGILINE |
| 02284650 | AZILECT |
| 02284642 | AZILECT |
| 02418436 | TEVA-RASAGILINE |
| 02418444 | TEVA-RASAGILINE |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the data supplied.

One point from the rationale to keep in mind: rasagiline is metabolized in the liver. This matters if it were ever considered for a population with liver involvement.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no supporting trials or literature (L5). The proposed use is also a very rare condition. A symptomatic dopaminergic benefit is plausible, but nothing in the data confirms it.

**To proceed, the following is needed:**
- A targeted literature search on MAO-B inhibitors or dopaminergic therapy in PLA2G6-associated neurodegeneration and PARK14, including case reports
- The Health Canada product monograph, to confirm the approved indication, warnings, contraindications and interactions
- Detailed mechanism-of-action data from DrugBank
- An assessment of safety and dosing for the pediatric and juvenile-onset patients typical of this disease
- Expert review to decide whether a symptomatic-benefit hypothesis justifies further study

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

