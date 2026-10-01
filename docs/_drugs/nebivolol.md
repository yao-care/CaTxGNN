---
layout: default
title: Nebivolol
parent: Model Prediction Only (L5)
nav_order: 640
evidence_level: L5
indication_count: 5
---

# Nebivolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Nebivolol: From Its Existing Approved Use to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Nebivolol is a beta-blocker already marketed in Canada under 9 licences, but the supplied record does not list its approved indications.
The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**, but this rests on the model score alone, with **0 clinical trials** and **0 publications** retrieved for this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 9 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied record, and no original indications are listed. The following is background pharmacology, not something the supplied data supports. Nebivolol is a beta-1 selective blocker that also promotes endothelial nitric oxide (NO)-mediated vasodilation. Both actions lower blood pressure, and they could plausibly help the renal vasculature in severe hypertension.

The prediction may be an extension of an existing use rather than true repurposing. Nebivolol is already marketed as an antihypertensive, and malignant hypertensive renal disease is a severe form of hypertensive kidney injury.

There is also a practical limit. The malignant (accelerated) phase usually needs rapid, titratable parenteral blood-pressure control, which an oral beta-blocker cannot provide. The same score (99.42%) was given to "malignant renovascular hypertension", which suggests a shared graph path rather than independent support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Nine licences are recorded; the five main ones are listed below. Dosage form and approved-indication text are not provided in the record.

| DIN | Product Name |
|---------|------|
| 2543508 | JAMP NEBIVOLOL |
| 2399016 | BYSTOLIC |
| 2399024 | BYSTOLIC |
| 2548704 | PRZ-NEBIVOLOL |
| 2548720 | PRZ-NEBIVOLOL |

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned no records, so no interaction information is available from this dataset.

Please refer to the package insert for safety information, including warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a model score, with no trials or drug-specific publications. Nebivolol is already an antihypertensive, so this may not be true repurposing. Oral therapy is also poorly suited to the acute management that malignant hypertension typically requires.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Approved indication text for the Canadian licences, to confirm what the drug is already authorised for
- Targeted searches for nebivolol studies in malignant or accelerated hypertension and hypertensive nephropathy
- A decision on whether this question is worth pursuing, given the acute-care setting

**Other predictions for this drug:**
- **Malignant renovascular hypertension:** same score, no evidence retrieved. It faces the same limits as the lead indication.
- **Pulmonary hypertension (hypoxia-related and unclear multifactorial forms):** score 99.39%, Hold. The 20 retrieved papers are keyword matches on "hypoxia" and none concern nebivolol. Beta-blockade in pulmonary hypertension also raises safety questions.
- **Braddock syndrome:** score 99.14%, Hold. No evidence retrieved and no credible mechanistic link from the supplied data.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

