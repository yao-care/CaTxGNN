---
layout: default
title: Givosiran
parent: Model Prediction Only (L5)
nav_order: 431
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Givosiran: predicted new indication Early-onset familial noncirrhotic portal hypertension (evidence level L5). Approved use: Hepatic porphyria"
monitor_inn: "GIVOSIRAN"
predicted_indications: ["early-onset familial noncirrhotic portal hypertension", "primitive portal vein thrombosis", "hepatoportal sclerosis", "idiopathic copper-associated cirrhosis", "hepatopulmonary syndrome", "chronic hepatitis C virus infection", "glycogen storage disease due to hepatic glycogen synthase deficiency", "chronic hepatitis B virus infection", "disorder of phenylalanine metabolism"]
---

# Givosiran
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Givosiran: From Hepatic Porphyria to Early-Onset Familial Noncirrhotic Portal Hypertension
{: .text-alpha }

## One-Sentence Summary

Givosiran is a liver-targeted RNA interference drug, originally used to treat hepatic porphyria.
The TxGNN model predicts it may be effective for **early-onset familial noncirrhotic portal hypertension**, but **no clinical trials and no publications** currently support this prediction, so it is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hepatic porphyria |
| Predicted New Indication | Early-onset familial noncirrhotic portal hypertension |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Givosiran is a GalNAc-conjugated small interfering RNA (siRNA). It is taken up by liver cells and silences the *ALAS1* gene. This lowers the neurotoxic heme intermediates aminolevulinic acid (ALA) and porphobilinogen (PBG), which drive the attacks seen in acute hepatic porphyria.

The data compiled for this report do not establish a mechanistic link between ALAS1 suppression and noncirrhotic portal hypertension. That condition involves vascular and hepatoportal pathology, which heme-synthesis modulation is not known to address. The score of 1.0000 is identical to the scores of several other unrelated liver-vascular diseases (portal vein thrombosis, hepatoportal sclerosis, idiopathic copper-associated cirrhosis, hepatopulmonary syndrome). This suggests the model is picking up a generic "liver-related" association rather than a signal specific to this disease.


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
| 02506343 | GIVLAARI | Not listed | Not listed |

---

## Safety Considerations

**Drug Interactions:** 87 interactions are recorded. The 20 reviewed include one major interaction and the rest moderate.
- **Major:** Eliglustat
- **Moderate (examples):**
  - Aminoglycosides: vancomycin, kanamycin, neomycin, streptomycin
  - Amphotericin B formulations
  - Aminosalicylates: mesalazine, balsalazide, olsalazine, sulfasalazine
  - Other: metoclopramide, naltrexone, exenatide, fenfluramine, alosetron, caffeine

**Liver-related caution:** Transaminase elevations have been seen with givosiran. This would be a concern in a patient with a diseased liver, such as one with portal hypertension or cirrhosis.

For warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no trials or publications, and no plausible mechanism links ALAS1 silencing to noncirrhotic portal hypertension. The identical scores across unrelated diseases point to a non-specific output.

**To proceed, the following is needed:**
- A disease-specific mechanistic hypothesis connecting heme synthesis or ALAS1 to the pathology of portal hypertension
- Preclinical or early clinical evidence in this condition
- Review of the Health Canada package insert for warnings, contraindications, and hepatic safety in patients with liver disease
- Consider redirecting effort to the ALAD porphyria prediction, which has a stronger biological rationale. It would first need evidence that resolves the question of erythroid ALA production.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

