---
layout: default
title: Acetazolamide
parent: Model Prediction Only (L5)
nav_order: 18
evidence_level: L5
indication_count: 10
monitor_inn: "ACETAZOLAMIDE"
predicted_indications: ["exercise-induced malignant hyperthermia", "hypertrophic cardiomyopathy", "congenital myopathy with excess of thin filaments", "hypertrophic cardiomyopathy due to intensive athletic training", "distal myopathy, Tateyama type", "cirrhotic cardiomyopathy", "cardiomyopathy", "intestinal obstruction", "glycogen storage disease due to acid maltase deficiency, late-onset", "myopathic intestinal pseudoobstruction"]
last_modified_at: 2026-11-24
description: "Acetazolamide: predicted new indication exercise-induced malignant hyperthermia (evidence level L5). In Canada: 3 DINs (2 marketed, 1 dormant)"
---

# Acetazolamide
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

## Acetazolamide: Carbonic anhydrase inhibitor → exercise-induced malignant hyperthermia
{: .text-alpha }

## One-Sentence Summary

Acetazolamide is a carbonic anhydrase inhibitor that is marketed in Canada.
The TxGNN model predicts it may be effective for **exercise-induced malignant hyperthermia**, with a score of 0.9995.
There are **no clinical trials** and **no publications** that directly study this disease, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | exercise-induced malignant hyperthermia |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 2 of 3; dormant: 1) |
| Number of DINs | 3 (marketed: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for acetazolamide: "Acetazolamide is a potent carbonic anhydrase inhibitor, effective in the control of fluid secretion (e.g., some types of glaucoma), in the treatment of certain convulsive disorders (e.g., epilepsy), and in the promotion of diuresis in instances of abnormal fluid retention (e.g., cardiac edema). Acetazolamide is not a mercurial diuretic." ([DailyMed: acetazolamide prescribing information, Chartwell RX, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e8e48a25-5f6c-4b5a-a5f2-ee87aabea33b), label version 2026-11-10; accessed 2026-11-19.) Acetazolamide belongs to the carbonic anhydrase inhibitor class, which alters acid-base balance and ion handling in tissues.

A possible link to exercise-induced malignant hyperthermia, a disorder of muscle physiology, is that these effects might influence muscle ion handling. This idea is speculative. Nothing in the data compiled for this report supports it, and the score of 0.9995 is a model output only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 00545015 | ACETAZOLAMIDE | ACETAZOLAMIDE | Marketed |
| 02537893 | ACETAZOLAMIDE FOR INJECTION USP | ACETAZOLAMIDE (ACETAZOLAMIDE SODIUM) | Marketed |
| 02358328 | ACETAZOLAMIDE FOR INJECTION, USP | ACETAZOLAMIDE (ACETAZOLAMIDE SODIUM) | Dormant |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

The approved indication text is not recorded in the local data. All three licences are currently valid single-ingredient products.

## Safety Considerations

- **Drug Interactions** (100 interactions were found; examples shown):
  - Major: acetylsalicylic acid, cisapride
  - Moderate: antidiabetic agents (e.g. acarbose, acetohexamide, canagliflozin, dapagliflozin, dulaglutide), corticosteroids (e.g. dexamethasone, betamethasone, beclomethasone), amphotericin B formulations, and laxatives (bisacodyl, castor oil)
  - Minor: doxycycline

Other safety information should be taken from the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no trials, no literature and no identifiable mechanism. The evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data for acetazolamide
- Preclinical or mechanistic studies linking carbonic anhydrase inhibition to exercise-induced malignant hyperthermia
- Warnings and contraindications from the Health Canada package insert, to complete the safety screening

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not currently available for acetazolamide" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: acetazolamide prescribing information, Chartwell RX, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e8e48a25-5f6c-4b5a-a5f2-ee87aabea33b) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

