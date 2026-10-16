---
layout: default
title: Cobicistat
parent: Model Prediction Only (L5)
nav_order: 219
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Cobicistat: predicted new indication Simian immunodeficiency virus infection (evidence level L5). Approved use: HIV infection / AIDS"
---

# Cobicistat
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Cobicistat: From HIV Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Cobicistat is a pharmacokinetic booster (a CYP3A inhibitor) originally used in HIV infection and AIDS treatment regimens.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus infection**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infection / AIDS |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, cobicistat is a CYP3A inhibitor used as a pharmacokinetic booster. It has no intrinsic antiviral activity. It raises blood levels of co-administered antiretrovirals that are CYP3A substrates. Its role in HIV treatment is therefore supportive, not directly antiviral.

Simian immunodeficiency virus (SIV) is a lentivirus closely related to HIV, so a conceptual link to the approved HIV indication exists. The high score (99.92%) most likely reflects how close SIV and HIV sit in the knowledge graph, not an independent pharmacological signal. Any benefit would depend on pairing cobicistat with a suitable antiretroviral, and SIV is mainly a veterinary or preclinical-model indication rather than a human therapeutic target.

Two other predictions were also generated:
- **Feline acquired immunodeficiency syndrome** (score 99.92%): This has the same score as SIV, which suggests a shared graph-neighbourhood artifact. It is veterinary, and any use would need species-specific pharmacokinetic validation.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (score 99.91%): No plausible link to CYP3A inhibition is evident. The score is likely a model artifact for a rare disease with sparse graph connectivity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02426501 | PREZCOBIX | Not specified | Not specified |
| 02473720 | SYMTUZA | Not specified | Not specified |
| 02449498 | GENVOYA | Not specified | Not specified |
| 02397137 | STRIBILD | Not specified | Not specified |

All four authorizations are currently valid.

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 interactions in total. This is a large burden, consistent with strong CYP3A inhibition. The first 20 listed include:
  - **Major**: loperamide, triamcinolone, cisapride, budesonide
  - **Moderate**: hydrocortisone, betamethasone, dexamethasone (including nasal and ophthalmic forms), aprepitant, clotrimazole, clarithromycin, metoclopramide, repaglinide, fenfluramine, dexfenfluramine, prednisolone (ophthalmic), budesonide (nasal), hydrocortisone (ophthalmic)
  - **Minor**: prucalopride

  The large interaction burden is an added concern for any new population, especially pediatric or neurological patients.

Please refer to the package insert for other safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score, with no clinical trials or publications. Cobicistat has no antiviral activity of its own, and the top two predicted indications are veterinary or preclinical-model diseases outside the scope of human repurposing. The third prediction has no biological rationale.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (a blocking gap for safety screening)
- Detailed mechanism of action data
- Independent mechanistic or preclinical evidence for any predicted indication
- For SIV or feline indications, species-specific pharmacokinetic validation and a defined co-administered antiretroviral
- A review of the high-scoring rare neurodevelopmental prediction for biological plausibility before any further work
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

