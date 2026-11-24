---
layout: default
title: Dexlansoprazole
parent: Model Prediction Only (L5)
nav_order: 269
evidence_level: L5
indication_count: 4
monitor_inn: "DEXLANSOPRAZOLE"
predicted_indications: ["gastroduodenitis", "duodenal obstruction", "achlorhydria", "leather-bottle stomach"]
last_modified_at: 2026-11-24
description: "Dexlansoprazole: predicted new indication gastroduodenitis (evidence level L5). In Canada: 4 DINs (4 marketed)"
---

# Dexlansoprazole
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

## Dexlansoprazole: proton pump inhibitor → gastroduodenitis
{: .text-alpha }

## One-Sentence Summary

Dexlansoprazole is an acid-suppressing drug (proton pump inhibitor) that is currently marketed in Canada.
The TxGNN model predicts it may be effective for **gastroduodenitis**, but this rests on a prediction score alone, with **0 clinical trials** and **0 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | gastroduodenitis |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 4 of 4) |
| Number of DINs | 4 (marketed: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for dexlansoprazole: "Dexlansoprazole belongs to a class of antisecretory compounds, the substituted benzimidazoles, that suppress gastric acid secretion by specific inhibition of the (H +, K + )-ATPase at the secretory surface of the gastric parietal cell. Because this enzyme is regarded as the acid (proton) pump within the parietal cell, dexlansoprazole has been characterized as a gastric proton-pump inhibitor, in that it blocks the final step of acid production." ([DailyMed: Dexlansoprazole Delayed Release (dexlansoprazole) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=55c550b4-eb8b-4e69-9c09-fa5125a52e65), label version 2026-11-04; accessed 2026-11-19.) Dexlansoprazole belongs to the proton pump inhibitor class, which reduces stomach acid production.

Gastroduodenitis is inflammation of the stomach and duodenal lining. Because acid can aggravate mucosal inflammation, suppressing acid may relieve symptoms of acid-related inflammation. This is a plausible but unconfirmed link: no clinical trials or publications were found that study this disease directly, so the prediction is not yet backed by actual evidence.

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02354950 | DEXILANT | DEXLANSOPRAZOLE | Marketed |
| 02354969 | DEXILANT | DEXLANSOPRAZOLE | Marketed |
| 02528991 | APO-DEXLANSOPRAZOLE | DEXLANSOPRAZOLE | Marketed |
| 02529025 | APO-DEXLANSOPRAZOLE | DEXLANSOPRAZOLE | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

All four single-ingredient licences are currently valid.

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the data compiled for this report. Examples:
  - **Major**: acalabrutinib, atazanavir
  - **Moderate**: furosemide, hydrochlorothiazide, amphotericin B, amikacin, gefitinib, bosutinib, fosamprenavir, foscarnet, fostamatinib, bumetanide, ampicillin, amphetamine
  - **Minor**: acetylsalicylic acid, axitinib, brivaracetam, cyanocobalamin

Please refer to the package insert for other safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (0.9998), but there are no clinical trials or publications that study gastroduodenitis directly, so the evidence level is L5. Acid suppression offers a plausible mechanism, but it has not been tested for this condition.

**To proceed, the following is needed:**
- Clinical or literature evidence that directly studies dexlansoprazole in gastroduodenitis
- Detailed mechanism of action data
- Package insert warnings and contraindications from Health Canada
- Review of the major interactions (acalabrutinib, atazanavir) for the intended patient population

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not currently available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Dexlansoprazole Delayed Release (dexlansoprazole) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=55c550b4-eb8b-4e69-9c09-fa5125a52e65) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

