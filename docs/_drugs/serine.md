---
layout: default
title: Serine
parent: Model Prediction Only (L5)
nav_order: 845
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Serine: predicted new indication Familial visceral myopathy (evidence level L5). Approved use: Open-angle glaucoma"
monitor_inn: "Serine"
predicted_indications: ["familial visceral myopathy", "intestinal obstruction", "myopathic intestinal pseudoobstruction", "unclassified intestinal pseudoobstruction", "neuronal intestinal dysplasia, type B", "intestinal pseudoobstruction, neuronal, chronic idiopathic, X-linked", "exercise-induced malignant hyperthermia", "aqueous misdirection"]
---

# Serine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Serine: From Open-Angle Glaucoma and Pulmonary Tuberculosis to Familial Visceral Myopathy
{: .text-alpha }

## One-Sentence Summary

Serine is a proteinogenic amino acid. In the knowledge graph it is linked to open-angle glaucoma and pulmonary tuberculosis, and in Canada it is marketed as a component of parenteral nutrition products.
The TxGNN model predicts it may be effective for **familial visceral myopathy**, but there are **0 clinical trials** and **0 publications** supporting this prediction.
This is a model prediction only, and the data compiled for this report do not support a mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma; pulmonary tuberculosis (from the knowledge graph; no approved indication text is available in the Canadian licence records) |
| Predicted New Indication | Familial visceral myopathy |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, serine is a proteinogenic amino acid that is supplied as a nutritional component in parenteral nutrition amino acid solutions. Its link to the original indications (open-angle glaucoma and pulmonary tuberculosis) comes from knowledge-graph edges rather than from label text, and the source has not been verified.

Familial visceral myopathy is a rare genetic disorder of gut smooth muscle, typically associated with defects in genes such as ACTG2. The data compiled for this report show no mechanistic connection between serine and these defects. The very high TxGNN score (99.99%) most likely reflects the drug's position in the knowledge graph rather than biological evidence, and the prediction is probably a knowledge-graph artifact.

Several other top predictions show the same pattern. Myopathic and unclassified intestinal pseudo-obstruction have identical scores, as do traumatic glaucoma and aqueous misdirection. This suggests shared graph neighbourhoods rather than independent evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for familial visceral myopathy.

For context, the second-ranked prediction (intestinal obstruction) and the sixth-ranked prediction (angle-closure glaucoma) returned publications. These appear to be keyword matches only. They concern Peutz-Jeghers syndrome, which is caused by variants in the serine/threonine kinase STK11, and the serine protease PRSS56 in angle-closure glaucoma. None evaluates serine as a therapy.

---

## Canada Market Information

Serine is marketed in Canada through 20 valid single-ingredient licences, mainly parenteral nutrition products. Dosage form and approved indication text are not available in the compiled data. The first five licences are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00872296 | TRAVASOL | Not available | Not available |
| 02498448 | CLINIMIX | Not available | Not available |
| 02498456 | CLINIMIX | Not available | Not available |
| 02498464 | CLINIMIX | Not available | Not available |
| 02510324 | ESSEPNA | Not available | Not available |

---

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report, and no drug interaction records were found. Please refer to the package insert for safety information.

The knowledge graph does list contraindication links to the following conditions. These come from graph edges, not from label text, and should be verified against the product monograph:

- **Renal:** kidney disease, chronic kidney disease, chronic renal failure syndrome, end stage renal failure, nephrolithiasis, nephrocalcinosis, acute urate nephropathy
- **Metabolic:** diabetes mellitus, diabetic ketoacidosis, hypercalcemia, humoral hypercalcemia of malignancy, phosphorus metabolism disease
- **Cardiovascular:** heart disease, cardiovascular disease, ventricular fibrillation, digitalis poisoning
- **Neuropsychiatric:** epilepsy, anxiety disorder, neurotic disorder, dysthymic disorder, psychotic disorder, schizophreniform disorder, schizoaffective disorder, mental disorder, substance abuse/dependence
- **Other:** sarcoidosis, vitamin B12 deficiency, megaloblastic anemia

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no clinical trials or relevant publications, and no plausible mechanism links serine to familial visceral myopathy. The literature found for other predicted indications consists of keyword matches on "serine" rather than evidence of therapeutic benefit.

**To proceed, the following is needed:**
- Mechanism of action data, and evidence of a biological link between serine and visceral smooth muscle disease
- Preclinical studies (for example, disease models of ACTG2-related myopathy) showing any effect of serine
- Health Canada package insert warnings and contraindications, so that safety screening can begin
- Verification of the original indications (open-angle glaucoma, pulmonary tuberculosis), which currently come from the knowledge graph only
- Dosage form and approved indication details for the Canadian licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

