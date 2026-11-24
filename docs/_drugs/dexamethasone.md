---
layout: default
title: Dexamethasone
parent: Model Prediction Only (L5)
nav_order: 268
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "DEXAMETHASONE"
predicted_indications: ["alopecia mucinosa", "telogen effluvium", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions", "alopecia universalis onychodystrophy vitiligo", "prolapse of lacrimal gland"]
description: "Dexamethasone: predicted new indication Alopecia mucinosa (evidence level L5). In Canada: at least 20 DINs"
---

# Dexamethasone
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

## Dexamethasone: Alopecia mucinosa
{: .text-alpha }

## One-Sentence Summary

Dexamethasone is a glucocorticoid with anti-inflammatory and immunosuppressive activity, marketed in Canada in many single-ingredient products.
The TxGNN model predicts it may be effective for **alopecia mucinosa**, but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Alopecia mucinosa |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs on record: at least 20) |
| Number of DINs | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for dexamethasone: "Dexamethasone is a corticosteroid with anti-inflammatory effects and low mineralocorticoid activity. The precise mechanism of action in multiple myeloma is unknown. Dexamethasone induces apoptosis of multiple myeloma cells." ([DailyMed: Hemady (dexamethasone) prescribing information, Edenbridge Pharmaceuticals LLC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6b9cf32c-6d60-4853-bbfd-2304ffc2c129), label version 2026-01-09; accessed 2026-11-19.) Dexamethasone is a corticosteroid, and glucocorticoids are generally used to dampen inflammatory and immune responses.

The high model score (0.9999) appears to reflect a shared hair-loss (alopecia) phenotype and proximity to related hair disorders in the model's network. Any anti-inflammatory rationale for alopecia mucinosa is speculative, because no trials or literature were found that study this disease with dexamethasone. The prediction should therefore be regarded as a hypothesis only.

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 00042560 | MAXIDEX | DEXAMETHASONE | Marketed |
| 00042579 | MAXIDEX | DEXAMETHASONE | Marketed |
| 00664227 | DEXAMETHASONE SODIUM PHOSPHATE INJ USP 4MG/ML | DEXAMETHASONE PHOSPHATE (DEXAMETHASONE SODIUM PHOSPHATE) | Marketed |
| 00778915 | TOBRADEX | DEXAMETHASONE; TOBRAMYCIN | Marketed |
| 00874582 | DEXAMETHASONE SOD PHOSPH INJ 10MG/ML USP | DEXAMETHASONE (DEXAMETHASONE SODIUM PHOSPHATE) | Marketed |
| 01946897 | PMS-DEXAMETHASONE ELIXIR | DEXAMETHASONE | Marketed |
| 01964070 | PMS-DEXAMETHASONE | DEXAMETHASONE | Marketed |
| 01964976 | PMS-DEXAMETHASONE | DEXAMETHASONE | Marketed |
| 01977547 | DEXAMETHASONE SODIUM PHOSPHATE INJECTION, USP | DEXAMETHASONE PHOSPHATE (DEXAMETHASONE SODIUM PHOSPHATE) | Marketed |
| 02023865 | DEXAMETHASONE | DEXAMETHASONE SODIUM PHOSPHATE | Marketed |
| 02204266 | DEXAMETHASONE-OMEGA | DEXAMETHASONE PHOSPHATE (DEXAMETHASONE SODIUM PHOSPHATE) | Marketed |
| 02204274 | DEXAMETHASONE-OMEGA | DEXAMETHASONE PHOSPHATE (DEXAMETHASONE SODIUM PHOSPHATE) | Marketed |
| 02250055 | APO-DEXAMETHASONE | DEXAMETHASONE | Marketed |
| 02261081 | APO-DEXAMETHASONE | DEXAMETHASONE | Marketed |
| 02279363 | PMS-DEXAMETHASONE | DEXAMETHASONE | Marketed |
| 02363445 | OZURDEX | DEXAMETHASONE | Marketed |
| 02387743 | DEXAMETHASONE OMEGA UNIDOSE | DEXAMETHASONE PHOSPHATE (DEXAMETHASONE SODIUM PHOSPHATE) | Marketed |
| 02506882 | SANDOZ CIPROFLOXACIN / DEXAMETHASONE | CIPROFLOXACIN (CIPROFLOXACIN HYDROCHLORIDE); DEXAMETHASONE | Marketed |
| 02528584 | ODAN-DEXAMETHASONE ELIXIR | DEXAMETHASONE | Marketed |
| 02543745 | LEVODEXA | DEXAMETHASONE (DEXAMETHASONE SODIUM PHOSPHATE); LEVOFLOXACIN (LEVOFLOXACIN HEMIHYDRATE) | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

The data contain only part of the DINs for this ingredient; the list may be incomplete.

<!-- licenses:end -->

All listed licences are valid single-ingredient products.

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 interacting drugs. Major-level interactions include **fentanyl** and **adalimumab**. Moderate-level interactions include zidovudine, paclitaxel, abemaciclib, isotretinoin, acalabrutinib, acarbose, acebutolol, codeine, dihydrocodeine, acetazolamide, ketorolac, nifedipine and ibuprofen.

Please refer to the package insert for other safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone. No clinical trial or publication directly studies dexamethasone in alopecia mucinosa, so the evidence level is L5.

**To proceed, the following is needed:**
- Published case reports, case series or trials of corticosteroids in alopecia mucinosa
- Detailed mechanism of action data
- Package insert warnings and contraindications for the relevant formulation
- Assessment of the route of administration (topical, intralesional or systemic) suitable for the skin condition

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available for this drug" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Hemady (dexamethasone) prescribing information, Edenbridge Pharmaceuticals LLC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6b9cf32c-6d60-4853-bbfd-2304ffc2c129) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

