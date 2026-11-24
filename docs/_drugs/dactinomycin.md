---
layout: default
title: Dactinomycin
parent: Model Prediction Only (L5)
nav_order: 242
evidence_level: L5
indication_count: 4
monitor_inn: "DACTINOMYCIN"
predicted_indications: ["relapsing-remitting multiple sclerosis", "liver sarcoma", "upper aerodigestive tract neoplasm", "head and neck cancer"]
last_modified_at: 2026-11-24
description: "Dactinomycin: predicted new indication Relapsing-remitting multiple sclerosis (evidence level L5). In Canada: 1 DIN (1 marketed)"
---

# Dactinomycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Dactinomycin: cytotoxic DNA-intercalating antineoplastic → relapsing-remitting multiple sclerosis
{: .text-alpha }

## One-Sentence Summary

Dactinomycin is a cytotoxic antineoplastic that intercalates into DNA and inhibits transcription. The TxGNN model predicts it may be effective for **relapsing-remitting multiple sclerosis**, with a score of 0.9958. **No clinical trials and no publications** directly study this disease, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Relapsing-remitting multiple sclerosis |
| TxGNN Prediction Score | 0.9958 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 1 of 1) |
| Number of DINs | 1 (marketed: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for dactinomycin: "Dactinomycin is a cytotoxic actinomycin that binds DNA and inhibits RNA synthesis. The cytotoxic activity of dactinomycin has been demonstrated in animal models of different human cancers." ([DailyMed: dactinomycin prescribing information, Eugia US LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5da55538-2602-4704-a9da-603c9f7ff7dc), label version 2024-06-18; accessed 2026-11-19.) Dactinomycin is generally known as a transcription-inhibiting DNA intercalator with cytotoxic and myelosuppressive effects.

A rationale for immunomodulation in a relapsing autoimmune demyelinating disease is speculative at best. Many approved disease-modifying therapies already exist for this condition, and dactinomycin's toxicity profile makes it a poor fit by comparison. The high score is therefore likely a model artifact rather than a validated signal, and it should not be read as evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 00213071 | COSMEGEN | DACTINOMYCIN | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (DNA-intercalating antibiotic class) |
| Myelosuppression Risk | High. Bone marrow suppression is expected, and the drug interaction and contraindication data point to blood-count risks |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Conditions flagged as contraindication-related:** liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, anemia, leukopenia, aplastic anemia, varicella zoster infection and herpes zoster, hepatic vein thrombosis and Budd-Chiari syndrome. These are relation-level signals and are not label text.
- **Drug Interactions:** 100 interactions were found. Major-level ones include deferiprone and samarium (153Sm) lexidronam. Moderate-level ones include palifermin, strontium chloride Sr-89, fostamatinib, mercaptopurine, roflumilast and chloramphenicol.

Please also refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The score is very high, but no trial or publication studies dactinomycin in relapsing-remitting multiple sclerosis. Its cytotoxic, myelosuppressive profile is a poor match for a chronic autoimmune disease with many approved alternatives.

**To proceed, the following is needed:**
- Mechanistic data showing a plausible immunomodulatory action in demyelinating disease
- Preclinical studies in a relevant model of multiple sclerosis
- Package insert warnings and contraindications from Health Canada
- A risk-benefit comparison against approved disease-modifying therapies

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: dactinomycin prescribing information, Eugia US LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5da55538-2602-4704-a9da-603c9f7ff7dc) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

