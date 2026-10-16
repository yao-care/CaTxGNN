---
layout: default
title: Human Immunoglobulin G
parent: Model Prediction Only (L5)
nav_order: 452
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Human Immunoglobulin G: predicted new indication Severe nonproliferative diabetic retinopathy (evidence level L5). Approved use: Not available in the data compiled for this report"
---

# Human Immunoglobulin G
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

# Human Immunoglobulin G: From Immunoglobulin Therapy to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Human immunoglobulin G (IgG) is a plasma-derived antibody product marketed in Canada under 16 valid licences. The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, but **no clinical trials and no publications** currently support this prediction. It is a computational prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (no approved indication text was recorded for the licences) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 16 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general knowledge, human IgG products act through immunomodulation, Fc receptor blockade and complement inhibition, and are used as replacement or immunomodulatory therapy. A speculative link to diabetic retinopathy would be modulation of inflammation or autoimmunity in the diabetic retina, but nothing in the data compiled for this report supports it.

The high score (0.9975) reflects a knowledge-graph pattern, not demonstrated biology. The model also predicts closely related conditions, including diabetic retinopathy (99.63%), several cataract types (97.6%–98.9%) and drug-induced osteoporosis (99.37%). Many of these share identical or near-identical scores, which suggests a shared network-derived signal rather than independent evidence. For cataracts in particular, lens protein oxidation and osmotic stress have no evident connection to IgG's known immunological actions.

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
The prediction rests only on a knowledge-graph score, with no clinical trials, no literature and no established mechanism linking IgG to retinal disease. Safety data from the package insert are also missing, so the candidate cannot move past initial screening.

**To proceed, the following is needed:**
- Download and review the Health Canada package insert for warnings and contraindications
- Obtain mechanism of action data (for example from DrugBank) and assess any link to diabetic retinal inflammation
- Run a systematic search of PubMed and trial registries for IgG in diabetic retinopathy
- Confirm the original approved indications and the available routes of administration (intravenous or subcutaneous) against what a retinal indication would require
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

