---
layout: default
title: Valsartan
parent: Model Prediction Only (L5)
nav_order: 964
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-05
monitor_inn: "VALSARTAN"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease", "Prinzmetal angina"]
description: "Valsartan: predicted new indication Malignant hypertensive renal disease (evidence level L5). In Canada: at least 20 DINs"
---

# Valsartan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Valsartan: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Valsartan is an angiotensin II type 1 receptor blocker (ARB) that is marketed in Canada.
The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**.
No clinical trials and no studies of valsartan in this disease are available, so the evidence level is **L5** (model prediction only).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs on record: at least 20) |
| Number of DINs | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for valsartan: "Angiotensin II is formed from angiotensin I in a reaction catalyzed by angiotensin-converting enzyme (ACE, kininase II). Angiotensin II is the principal pressor agent of the renin-angiotensin system, with effects that include vasoconstriction, stimulation of synthesis and release of aldosterone, cardiac stimulation, and renal reabsorption of sodium. […] Diovan (valsartan) blocks the vasoconstrictor and aldosterone-secreting effects of angiotensin II by selectively blocking the binding of angiotensin II to the AT 1 receptor in many tissues, such as vascular smooth muscle and the adrenal gland." ([DailyMed: Diovan (valsartan) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5ddba454-f3e6-43c2-a7a6-58365d297213), label version 2026-08-11; accessed 2026-11-19.) Valsartan belongs to the angiotensin receptor blocker class, which blocks the AT1 receptor of the renin-angiotensin-aldosterone system (RAAS). Mechanistically, RAAS blockade lowers blood pressure and may protect the kidney in hypertensive kidney injury, so the prediction is biologically plausible.

However, this link is a hypothesis only. The one publication attached to this prediction (PMID 24368192) tested avosentan, an endothelin receptor antagonist, in a rat model of hypertensive nephropathy. It did not study valsartan or malignant hypertensive renal disease in patients, so it offers only indirect support. No clinical trials are registered.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24368192](https://pubmed.ncbi.nlm.nih.gov/24368192/) | 2014 | Preclinical (different drug: avosentan) | Pharmacological Research | Avosentan protected against hypertensive nephropathy in transgenic rats at doses that did not cause fluid retention; valsartan was not studied. |

## Canada Market Information

At least 20 valid single-ingredient valsartan licences are recorded in the local data; the list may be partial. Dosage form and indication text are not recorded for these licences.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02244782 | DIOVAN 160MG TABLETS | Not listed | Not listed |
| 02244781 | DIOVAN 80MG TABLETS | Not listed | Not listed |
| 02289504 | DIOVAN | Not listed | Not listed |
| 02356643 | TEVA-VALSARTAN | Not listed | Not listed |
| 02356759 | SANDOZ VALSARTAN | Not listed | Not listed |

## Safety Considerations

- **Drug Interactions** (100 interactions found in the interaction database; main ones shown):
  - **Major:** potassium chloride and potassium bicarbonate (risk of raised blood potassium).
  - **Moderate:** insulins and exenatide (effects on blood glucose), hydrocortisone, eluxadoline, and polyethylene glycol with electrolytes.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high and RAAS blockade is mechanistically plausible for hypertensive kidney injury. However, no clinical trial or study of valsartan in malignant hypertensive renal disease exists in the data compiled for this report, so the evidence level is L5.

**To proceed, the following is needed:**
- Clinical or observational studies of valsartan, or other ARBs, in malignant hypertensive renal disease
- Mechanism-of-action data for valsartan
- Warnings and contraindications from the Health Canada package insert
- A safety plan covering potassium monitoring, renal function, and interacting drugs

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Diovan (valsartan) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5ddba454-f3e6-43c2-a7a6-58365d297213) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

