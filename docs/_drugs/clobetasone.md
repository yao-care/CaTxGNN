---
layout: default
title: Clobetasone
parent: Model Prediction Only (L5)
nav_order: 210
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Clobetasone: predicted new indication Primary cutaneous T-cell lymphoma (evidence level L5). Approved use: Not stated in the Canadian license record (the single product is mark…"
monitor_inn: "Clobetasone"
predicted_indications: ["primary cutaneous T-cell lymphoma", "Sezary syndrome", "primary cutaneous B-cell lymphoma", "granulomatous slack skin disease", "Crohn's colitis", "adrenocortical insufficiency", "primary cutaneous T-cell non-Hodgkin lymphoma", "nephrotic syndrome", "cystic teratoma", "spinal cord dermoid cyst"]
---

# Clobetasone
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

## Clobetasone: From Topical Corticosteroid Use to Primary Cutaneous T-Cell Lymphoma
{: .text-alpha }

## One-Sentence Summary

Clobetasone is a moderate-potency topical corticosteroid, marketed in Canada in a medicated cream for eczema care.
The TxGNN model predicts it may be useful for **primary cutaneous T-cell lymphoma**, with a very high score.
However, **no clinical trials and no publications** were found in the data compiled for this report, so the prediction rests on model output and class-level reasoning only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license record (the single product is marketed as an eczema-care medicated cream) |
| Predicted New Indication | Primary cutaneous T-cell lymphoma |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for this drug. Based on known information, clobetasone is a topical corticosteroid. Drugs in this class act through the glucocorticoid receptor to produce anti-inflammatory and immunosuppressive effects.

Topical corticosteroids are used as skin-directed therapy in early-stage mycosis fungoides, the most common subtype of cutaneous T-cell lymphoma (CTCL). This gives a plausible symptom-control link between clobetasone and CTCL. Primary cutaneous T-cell non-Hodgkin lymphoma (rank 7) overlaps largely with this prediction and carries the same rationale.

Important caveats apply. There is no clobetasone-specific trial or publication in the compiled data, and the TxGNN score is a computational prediction only. Other predictions with high scores are weaker:
- **Sezary syndrome:** a leukemic, systemic CTCL variant that needs systemic therapy, so a topical steroid is unlikely to be disease-modifying.
- **Primary cutaneous B-cell lymphoma and granulomatous slack skin disease:** these look like class-level or disease-group associations without supporting data.
- **Crohn's colitis, adrenocortical insufficiency, nephrotic syndrome:** these reflect the glucocorticoid class. Clobetasone is a topical dermatological product, not suited to gastrointestinal delivery, systemic replacement or systemic exposure.
- **Cystic teratoma and spinal cord dermoid cyst:** no plausible mechanism; the scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

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
| 02214415 | Spectro Eczemacare Medicated Cream | Not specified | Not specified |

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction records were found for clobetasone, and the knowledge graph lists no contraindicated diseases. Note that this reflects a lack of data, not proof of safety. As a general class consideration noted in the data, extensive topical use can suppress the HPA axis.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but the evidence level is L5: there are no clinical trials or publications. The most plausible indication, early-stage CTCL (mycosis fungoides) as skin-directed therapy, is a research question rather than an evidence-backed option. The product's own indication and safety label data are also missing.

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications and approved indication) for the licensed product
- Mechanism of action data for clobetasone
- A literature and trial search focused on topical corticosteroids in early-stage mycosis fungoides and CTCL
- Route and formulation compatibility assessment (topical use versus the disease's required route)
- Safety assessment for extensive or long-term topical use, including HPA-axis suppression
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

