---
layout: default
title: Mogamulizumab
parent: Model Prediction Only (L5)
nav_order: 628
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-28
description: "Mogamulizumab: predicted new indication Prostatic urethra urothelial carcinoma (evidence level L5). Approved use: Mycosis fungoides and variants"
monitor_inn: "Mogamulizumab"
predicted_indications: ["prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant", "renal pelvis papillary urothelial carcinoma", "human herpesvirus 8-related tumor", "ectomesenchymoma", "malignant cutaneous granular cell skin tumor"]
---

# Mogamulizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Mogamulizumab: From Cutaneous T-Cell Lymphoma to Prostatic Urethra Urothelial Carcinoma
{: .text-alpha }

## One-Sentence Summary

Mogamulizumab was originally used to treat cutaneous T-cell lymphomas, including mycosis fungoides and related variants.
The TxGNN model predicts it may be effective for **prostatic urethra urothelial carcinoma**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mycosis fungoides and variants; primary cutaneous T-cell lymphoma (approved indication text for the Canadian licence is not available) |
| Predicted New Indication | Prostatic urethra urothelial carcinoma |
| TxGNN Prediction Score | 0.9944 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, mogamulizumab is an anti-CCR4 monoclonal antibody. It is understood to work through antibody-dependent cellular cytotoxicity, depleting CCR4-positive cells, including effector regulatory T cells (Tregs).

The possible link to urothelial carcinoma is that Treg depletion in the tumour microenvironment could enhance anti-tumour immunity. This is a hypothesis only. Whether urothelial tumours express CCR4 or contain a CCR4+ Treg-rich environment has not been established in the available data.

Other urothelial subtypes also score highly (for example, renal pelvis papillary urothelial carcinoma at 0.9937 and bladder sarcomatoid variant at 0.9940). This pattern suggests a model cluster effect rather than independent evidence. The score is a computational prediction, not clinical evidence.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02527715 | POTELIGEO | Not listed | Not listed |

---

## Safety Considerations

**Drug Interactions**: 83 interactions were identified in the interaction screening. Examples of the main ones:
- **Major**: deferiprone, samarium (153Sm) lexidronam, adalimumab, baricitinib
- **Moderate**: strontium chloride Sr-89, roflumilast, chloramphenicol, zidovudine, alefacept, alemtuzumab, anakinra, azathioprine, canakinumab, anthrax vaccine, tetanus toxoid vaccine
- **Minor**: zinc salts (sulfate, acetate, gluconate, chloride)

Many of the listed interactions involve immunosuppressants or vaccines, so concurrent immune-modulating therapy would need careful review.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score. No clinical trials or publications exist for this indication, and the mechanistic link is hypothetical.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (a blocking gap for safety screening)
- Confirmed mechanism of action data (for example, from DrugBank)
- Preclinical evidence of CCR4 expression and CCR4+ Treg infiltration in urothelial tumours
- Any early-phase trial or literature evidence in urothelial carcinoma
- Approved indication text and dosage form for the Canadian licence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

