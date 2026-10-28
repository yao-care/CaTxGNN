---
layout: default
title: Human Immunoglobulin G
parent: Model Prediction Only (L5)
nav_order: 452
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Human Immunoglobulin G: predicted new indication Severe nonproliferative diabetic retinopathy (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Human immunoglobulin G"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "drug-induced osteoporosis"]
---

# Human Immunoglobulin G
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Human Immunoglobulin G: From Immunoglobulin Therapy to Severe Nonproliferative Diabetic Retinopathy
{: .text-alpha }

## One-Sentence Summary

Human immunoglobulin G (IgG) is a plasma-derived antibody product marketed in Canada under 16 valid licences. The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, but **no clinical trials and no publications** currently support this prediction. It is a computational prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (no approved indication text was recorded for the licences) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | Marketed (valid licenses: 16 of 16) |
| Number of DINs | 16 (valid: 16) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general knowledge, human IgG products act through immunomodulation, Fc receptor blockade and complement inhibition, and are used as replacement or immunomodulatory therapy. A speculative link to diabetic retinopathy would be modulation of inflammation or autoimmunity in the diabetic retina, but nothing in the data compiled for this report supports it.

The high score (0.9975) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The model also predicts closely related conditions, including diabetic retinopathy (0.9963) and drug-induced osteoporosis (0.9937). These scores are near-identical, which suggests a shared signal learned by the model rather than independent evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Dosage form, manufacturer and approved indication text were not recorded for these licences. The first five of the 16 valid authorizations are listed:

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02279444 | GAMMAGARD LIQUID | Not recorded | Not recorded |
| 02461692 | CUVITRU | Not recorded | Not recorded |
| 02277921 | IGIVNEX | Not recorded | Not recorded |
| 02498251 | HIZENTRA | Not recorded | Not recorded |
| 02247724 | GAMUNEX | Not recorded | Not recorded |

The remaining licences cover additional HIZENTRA, GAMASTAN, PRIVIGEN, GAMMAGARD S/D and HYQVIA products.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN model (deep learning) score, with no clinical trials, no literature and no established mechanism linking IgG to retinal disease. Safety data from the package insert are also missing, so the candidate cannot move past initial screening.

**To proceed, the following is needed:**
- Download and review the Health Canada package insert for warnings and contraindications
- Obtain mechanism of action data (for example from DrugBank) and assess any link to diabetic retinal inflammation
- Run a systematic search of PubMed and trial registries for IgG in diabetic retinopathy
- Confirm the original approved indications and the available routes of administration (intravenous or subcutaneous) against what a retinal indication would require
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

