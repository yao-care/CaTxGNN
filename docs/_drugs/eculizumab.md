---
layout: default
title: Eculizumab
parent: Model Prediction Only (L5)
nav_order: 310
evidence_level: L5
indication_count: 10
---

# Eculizumab
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

# Eculizumab: From Complement-Mediated Diseases to Cyclic Hematopoiesis

## One-Sentence Summary

Eculizumab is a complement C5 inhibitor, marketed in Canada as SOLIRIS. The literature retrieved for this pack describes it in complement-mediated diseases such as paroxysmal nocturnal hemoglobinuria (PNH) and atypical hemolytic uremic syndrome (aHUS). The TxGNN model predicts it may be effective for **cyclic hematopoiesis** (cyclic neutropenia), but **no clinical trials and no publications** currently support this prediction, so it is a model output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license record (retrieved literature describes PNH, aHUS and myasthenia gravis) |
| Predicted New Indication | Cyclic hematopoiesis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source record. Eculizumab is known as a C5 complement inhibitor that blocks terminal complement activation. Its efficacy is established in diseases driven by uncontrolled complement activity.

Cyclic hematopoiesis (cyclic neutropenia) is a rare disorder of neutrophil production linked to ELANE variants. No established link exists between terminal complement activation and this disease. The score of 99.97% most likely reflects proximity in the knowledge graph rather than a demonstrated biological mechanism.

The other top-ranked predictions show the same pattern. Most are congenital neutropenia or related disorders of neutrophil production (JAGN1, CXCR2 and CSF3R deficiency, X-linked and severe congenital neutropenia, adult idiopathic neutropenia). All are prediction-only (L5) and have no supporting trials. This suggests the model is clustering a group of neutropenia-related diseases around the drug rather than identifying a complement-driven mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2322285 | SOLIRIS |

The dosage form and approved indication text are not available in the license record.

---

## Safety Considerations

Please refer to the package insert for safety information.

Complement inhibition can raise the risk of serious infection, including meningococcal infection. Patients with neutropenia already have impaired infection defences, so any use in this setting would need a careful risk-benefit assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials or publications for cyclic hematopoiesis. There is no plausible link between C5 blockade and neutrophil cycling, and added infection risk in neutropenic patients makes the risk-benefit unfavorable without supporting evidence.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text and dosage form for the Canadian license
- Detailed mechanism of action data, and a mechanistic rationale connecting complement C5 inhibition to neutrophil cycling
- Preclinical or clinical evidence specific to cyclic hematopoiesis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

