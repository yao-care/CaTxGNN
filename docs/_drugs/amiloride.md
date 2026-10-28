---
layout: default
title: Amiloride
parent: Model Prediction Only (L5)
nav_order: 50
evidence_level: L5
indication_count: 5
monitor_inn: "Amiloride"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-10-28
description: "Amiloride: predicted new indication malignant hypertensive renal disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Amiloride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Amiloride: potassium-sparing diuretic (ENaC blocker) → malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Amiloride is a potassium-sparing diuretic marketed in Canada. The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**. The data compiled for this report contain **no clinical trials and no publications** on this indication, so the prediction is not yet supported by direct evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9982 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 2 of 2) |
| Number of DINs | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Amiloride is generally known to block the epithelial sodium channel (ENaC) in the distal nephron. This reduces sodium reabsorption and potassium loss. That kidney-level sodium handling is the most plausible link to a blood-pressure-related kidney condition.

The link is weak for this indication. Malignant hypertension with kidney involvement needs rapid, controlled blood pressure reduction, and amiloride is not a typical choice for that. Impaired kidney function also raises the risk of hyperkalaemia with a potassium-sparing agent, which is a significant safety concern. The high score is best read as a computational association, not as evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Two valid single-ingredient licences are on record. Approved indication text, dosage form and manufacturer are not recorded in the local data.

| DIN | Product Name |
|---------|------|
| 02249510 | MIDAMOR |
| 00784400 | AA-AMILZIDE |

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the interaction database. The examples listed here are rated Moderate:
  - Metformin
  - Corticosteroids (hydrocortisone, betamethasone, dexamethasone, budesonide)
  - SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin)
  - Exenatide
  - Bupropion
  - Several laxatives (bisacodyl, castor oil, lactulose, lactitol)

  Minor examples include doxycycline, amoxicillin and cimetidine.
- **Hyperkalaemia in renal impairment**: Potassium retention is a particular concern in patients with reduced kidney function, which is directly relevant to this predicted indication.

Package insert warnings and contraindications are not available in the data compiled for this report. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting trials or publications, so the evidence level is L5. The mechanism is only loosely plausible, and the hyperkalaemia risk in kidney disease is a major safety barrier.

**To proceed, the following is needed:**
- Mechanistic and preclinical data directly addressing malignant hypertensive renal disease
- Retrieval and review of the Health Canada package insert (warnings and contraindications)
- Detailed mechanism of action data
- A potassium and renal-function safety assessment for patients with kidney impairment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

