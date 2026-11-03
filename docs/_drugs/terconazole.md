---
layout: default
title: Terconazole
parent: Model Prediction Only (L5)
nav_order: 898
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-03
monitor_inn: "TERCONAZOLE"
predicted_indications: ["trichomonal vulvovaginitis", "vulvitis", "postmenopausal atrophic vaginitis", "herpetic vulvovaginitis", "ulceration of vulva", "vulvar neoplasm", "vaginal discharge", "bacterial vaginosis"]
description: "Terconazole: predicted new indication Trichomonal vulvovaginitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Terconazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Terconazole: Trichomonal vulvovaginitis
{: .text-alpha }

## One-Sentence Summary

Terconazole is a topical triazole antifungal that is currently marketed in Canada.
The TxGNN model predicts it may be effective for **trichomonal vulvovaginitis** (score 0.9986), but **no clinical trials** and **no studies that directly examine this condition** were found, so the prediction remains model-only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Trichomonal vulvovaginitis |
| TxGNN Prediction Score | 0.9986 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Based on known pharmacology, terconazole is a triazole antifungal. It inhibits fungal lanosterol 14-alpha-demethylase (CYP51), which blocks ergosterol synthesis in the fungal cell membrane.

This mechanism does not carry over well to trichomonal infection. *Trichomonas vaginalis* is a protozoan, and it lacks ergosterol-dependent membrane biology comparable to fungi. No plausible mechanistic link to terconazole was identified. The very high TxGNN score most likely reflects the drug's closeness to other genital-tract infection conditions in the model's network, not a true pharmacological effect. Standard therapy for this infection is a nitroimidazole (metronidazole or tinidazole).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10546257](https://pubmed.ncbi.nlm.nih.gov/10546257/) | 1999 | Review | The Nurse Practitioner | General overview of lower genital tract infections of bacterial, fungal and protozoal origin, including symptoms and management. It does not report terconazole data for trichomonal infection. |
| [6617296](https://pubmed.ncbi.nlm.nih.gov/6617296/) | 1983 | Review | Chemotherapy | Describes terconazole as a broad-spectrum triazole antifungal with strong in vitro activity against yeasts and filamentous fungi. It reports no activity against protozoa. |

Neither publication directly studies terconazole in trichomonal vulvovaginitis.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02247651 | TARO-TERCONAZOLE | Not specified | Not specified in the compiled data |

Terconazole has one valid single-ingredient licence in Canada, and the drug is marketed.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. No clinical trials or direct studies support it, and the drug's antifungal mechanism offers no plausible action against a protozoal pathogen. Established nitroimidazole therapy already exists for this infection.

**To proceed, the following is needed:**
- In vitro data showing any activity of terconazole against *Trichomonas vaginalis*
- Detailed mechanism-of-action data
- Package insert warnings and contraindications from Health Canada, which are needed for safety screening
- Preclinical or early clinical evidence directly addressing this condition before any further consideration

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

