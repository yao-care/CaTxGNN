---
layout: default
title: Carvedilol
parent: Model Prediction Only (L5)
nav_order: 161
evidence_level: L5
indication_count: 4
monitor_inn: "CARVEDILOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
last_modified_at: 2026-11-24
description: "Carvedilol: predicted new indication malignant hypertensive renal disease (evidence level L5). In Canada: at least 20 DINs"
---

# Carvedilol
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

## Carvedilol: non-selective beta-blocker with alpha-1 blocking activity → malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Carvedilol is a beta-blocker that also blocks alpha-1 adrenergic receptors and has antioxidant properties, and it is currently marketed in Canada.
The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**.
**No clinical trials and no publications** on this disease were found in the data compiled for this report, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9955 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs on record: at least 18; dormant: 2) |
| Number of DINs | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for carvedilol: "COREG is a racemic mixture in which nonselective β-adrenoreceptor blocking activity is present in the S(-) enantiomer and α1-adrenergic blocking activity is present in both R(+) and S(-) enantiomers at equal potency. COREG has no intrinsic sympathomimetic activity." ([DailyMed: Coreg (carvedilol) prescribing information, Waylis Therapeutics LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=07c619c6-4a0c-445e-94fa-664a54f68a39), label version 2026-07-31; accessed 2026-11-19.) Based on general pharmacology, carvedilol lowers blood pressure by blocking beta and alpha-1 adrenergic receptors. It also has antioxidant activity, which could in theory help protect the kidney from the injury caused by severely raised blood pressure.

The link to malignant hypertensive renal disease is therefore plausible only at a theoretical level. Malignant hypertension with kidney involvement is an acute emergency that is usually managed with intravenously administered agents. An oral beta-blocker is not a typical first-line choice. No study in the compiled data examines carvedilol in this condition, and the score of 0.9955 is a model output, not clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Health Canada records show 20 valid single-ingredient carvedilol licences, with none cancelled. The records may be partial. Dosage form and indication text are not recorded for these entries.

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02245914 | PMS-CARVEDILOL | CARVEDILOL | Marketed |
| 02245916 | PMS-CARVEDILOL | CARVEDILOL | Marketed |
| 02248752 | CARVEDILOL | CARVEDILOL | Marketed |
| 02248753 | CARVEDILOL | CARVEDILOL | Marketed |
| 02248754 | CARVEDILOL | CARVEDILOL | Marketed |
| 02252309 | TEVA-CARVEDILOL | CARVEDILOL | Marketed |
| 02252317 | TEVA-CARVEDILOL | CARVEDILOL | Marketed |
| 02252325 | TEVA-CARVEDILOL | CARVEDILOL | Marketed |
| 02252333 | TEVA-CARVEDILOL | CARVEDILOL | Marketed |
| 02324504 | CARVEDILOL | CARVEDILOL | Marketed |
| 02324520 | CARVEDILOL | CARVEDILOL | Marketed |
| 02364948 | CARVEDILOL | CARVEDILOL | Marketed |
| 02364956 | CARVEDILOL | CARVEDILOL | Marketed |
| 02368900 | JAMP-CARVEDILOL | CARVEDILOL | Marketed |
| 02368919 | JAMP-CARVEDILOL | CARVEDILOL | Marketed |
| 02368927 | JAMP-CARVEDILOL | CARVEDILOL | Marketed |
| 02418509 | AURO-CARVEDILOL | CARVEDILOL | Marketed |
| 02418517 | AURO-CARVEDILOL | CARVEDILOL | Marketed |
| 02247933 | APO-CARVEDILOL | CARVEDILOL | Dormant |
| 02247935 | APO-CARVEDILOL | CARVEDILOL | Dormant |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

The data contain only part of the DINs for this ingredient; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for these.

- **Drug Interactions**: The interaction screen was completed and returned 100 interacting drugs. The first 20 were reviewed.
  - **Major**: epinephrine.
  - **Moderate**, among others:
    - corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide);
    - anticholinergics (atropine, hyoscyamine);
    - morphine;
    - bupropion;
    - lorcaserin;
    - canagliflozin;
    - acetohexamide;
    - calcium salts.
  - **Minor**, among others: acetylsalicylic acid, aluminum hydroxide, attapulgite.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting clinical trial or publication for this disease, so the evidence level is L5. Malignant hypertensive renal disease is an acute condition usually treated with other agents, and no data show a benefit from carvedilol.

**To proceed, the following is needed:**
- Mechanism-of-action data for carvedilol
- Package insert warnings and contraindications from Health Canada
- A literature review and any clinical or preclinical studies of carvedilol in hypertensive kidney injury
- Clinical input on whether an oral beta-blocker has a role in this acute setting

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for carvedilol is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Coreg (carvedilol) prescribing information, Waylis Therapeutics LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=07c619c6-4a0c-445e-94fa-664a54f68a39) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

