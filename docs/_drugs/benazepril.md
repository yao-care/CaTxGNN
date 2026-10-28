---
layout: default
title: Benazepril
parent: Model Prediction Only (L5)
nav_order: 99
evidence_level: L5
indication_count: 4
monitor_inn: "Benazepril"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
last_modified_at: 2026-10-28
description: "Benazepril: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Benazepril
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

## Benazepril: ACE inhibitor (RAAS blockade) → Malignant hypertensive renal disease (malignant hypertensive renal disease)
{: .text-alpha }

## One-Sentence Summary

Benazepril is an ACE inhibitor that is marketed in Canada as a single-ingredient product.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, with a score of 0.9965.
Currently there are **no clinical trials and no publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease (malignant hypertensive renal disease) |
| TxGNN Prediction Score | 0.9965 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 3 of 3) |
| Number of DINs | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on its drug class, benazepril is an ACE inhibitor, which blocks the renin-angiotensin-aldosterone system (RAAS). This lowers blood pressure and can reduce pressure inside the kidney's filtering units (glomeruli) and protein loss in urine.

Malignant hypertensive renal disease is kidney damage caused by severely elevated, rapidly progressive blood pressure. Because the main driver is high blood pressure acting on the kidney, RAAS blockade is mechanistically plausible. However, this looks more like an extension of blood pressure control than a distinct new repurposing signal. No study in the data compiled for this report directly examines benazepril in this disease, so the high score cannot be confirmed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02290332 | BENAZEPRIL | Not recorded | Not recorded |
| 02273918 | BENAZEPRIL | Not recorded | Not recorded |
| 02290340 | BENAZEPRIL | Not recorded | Not recorded |

All three licences are single-ingredient products and currently valid.

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 records; the 20 shown are all of Moderate level. They are mostly glucose-lowering agents, including insulins (human, aspart, degludec, detemir, glargine, glulisine, lispro), sulfonylureas (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide), alogliptin, dapagliflozin and exenatide. Other listed agents are hydrocortisone and glycerin. Blood glucose should be monitored when combined with these.

For other safety information, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score, but no clinical trial or publication studies benazepril in malignant hypertensive renal disease, so the evidence level is L5. The mechanistic plausibility mostly reflects benazepril's existing blood pressure-lowering role.

**To proceed, the following is needed:**
- Clinical or observational studies of ACE inhibitors, specifically benazepril, in malignant hypertensive renal disease
- Detailed mechanism of action data
- Package insert warnings and contraindications from Health Canada
- Review of renal safety (e.g. kidney function and potassium monitoring) in patients with severe hypertension and kidney injury
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

