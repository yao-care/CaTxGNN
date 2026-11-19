---
layout: default
title: Darunavir
parent: Model Prediction Only (L5)
nav_order: 251
evidence_level: L5
indication_count: 4
monitor_inn: "DARUNAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
last_modified_at: 2026-11-05
description: "Darunavir: predicted new indication feline acquired immunodeficiency syndrome (evidence level L5). In Canada: 8 DINs (7 marketed, 1 dormant)"
---

# Darunavir
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

## Darunavir: HIV protease inhibitor → feline acquired immunodeficiency syndrome
{: .text-alpha }

## One-Sentence Summary

Darunavir is an HIV-1 protease inhibitor.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, a veterinary indication, with a score of 0.9997.
There are currently **no clinical trials** and **no publications** directly studying this disease, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 7 of 8; dormant: 1) |
| Number of DINs | 8 (marketed: 7) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for darunavir: "Darunavir is an HIV-1 antiviral drug. […] Darunavir is an inhibitor of the HIV-1 protease. It selectively inhibits the cleavage of HIV-1 encoded Gag-Pol polyproteins in infected cells, thereby preventing the formation of mature virus particles." ([DailyMed: Prezista (darunavir) prescribing information, Janssen Products LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=814301f9-c990-46a5-b481-2879a521a16f), label version 2025-08-29; accessed 2026-11-19.) Darunavir is known as an HIV-1 protease inhibitor, which blocks the viral enzyme needed to mature new virus particles.

Feline immunodeficiency virus (FIV) is a lentivirus related to HIV-1, so a mechanistic rationale exists in principle. However, FIV protease differs from HIV-1 protease in substrate specificity and inhibitor sensitivity. Published work suggests HIV-1 protease inhibitors have reduced activity against FIV protease.

The high score reflects a model prediction only. No trials or literature support it. This is also a veterinary indication, which falls outside the scope of human drug repurposing.

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
| 02486121 | AURO-DARUNAVIR | Not recorded | Not recorded |
| 02487241 | APO-DARUNAVIR | Not recorded | Not recorded |
| 02486148 | AURO-DARUNAVIR | Not recorded | Not recorded |
| 02487268 | APO-DARUNAVIR | Not recorded | Not recorded |
| 02521350 | DARUNAVIR | Not recorded | Not recorded |

The list shows 5 of the 8 valid licences.

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were found. Examples from the list include the following.
  - **Major**: cisapride.
  - **Moderate**: antidiabetic drugs (acarbose, metformin, pioglitazone, alogliptin, canagliflozin, dapagliflozin, saxagliptin, chlorpropamide), corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), clarithromycin and aprepitant.
- Darunavir is typically boosted with ritonavir or cobicistat and has strong CYP3A4-related interaction potential.

For warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications, and FIV protease is likely less sensitive to HIV-1 protease inhibitors. The indication is veterinary, so it is not a human repurposing opportunity.

**To proceed, the following is needed:**
- Laboratory data on darunavir activity against FIV protease
- Veterinary-specific efficacy and safety studies in cats
- Mechanism of action data and package insert safety information

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not currently available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Prezista (darunavir) prescribing information, Janssen Products LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=814301f9-c990-46a5-b481-2879a521a16f) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

