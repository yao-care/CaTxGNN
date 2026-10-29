---
layout: default
title: Labetalol
parent: Model Prediction Only (L5)
nav_order: 515
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-30
monitor_inn: "Labetalol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism"]
description: "Labetalol: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Labetalol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Labetalol: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Labetalol is a combined alpha-1 and non-selective beta-adrenergic blocker, originally used to treat hypertension and hypertensive disorders.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but there are currently **no clinical trials** and **no publications specific to this condition**, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9908 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 10 of 11) |
| Number of DINs | 11 (valid: 10) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, labetalol is a combined alpha-1 and non-selective beta-adrenergic blocker. Its efficacy in hypertension is established, and mechanistically it may be applicable to malignant hypertensive renal disease.

Malignant hypertensive renal disease is kidney damage caused by severely elevated blood pressure. Lowering blood pressure is therefore a plausible way to help. Labetalol is already used for severe hypertension and hypertensive emergencies.

This is essentially an extension of the original indication rather than a true repurposing. The high score (0.9908) is a computational prediction only, and no study specific to the renal condition was found.

Other predictions from the model were also reviewed:
- **Pulmonary hypertension (two predictions, score 0.9908)**: these are probably driven by the shared word "hypertension". Labetalol is not a pulmonary vasodilator, and non-selective beta-blockade may cause bronchoconstriction in patients with lung disease. The retrieved literature concerns systemic hypertension (such as preeclampsia) or unrelated topics, and gives no direct support. These predictions are not recommended for advancement.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature is available for the top predicted indication (malignant hypertensive renal disease).


| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7242419](https://pubmed.ncbi.nlm.nih.gov/7242419/) | 1981 | Case report | Med J Aust | A young man with malignant hypertension after hallucinogenic drug use had vasculitis that responded to prednisone. Minoxidil and labetalol were used for initial blood pressure control. This does not demonstrate labetalol efficacy for the condition. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02231689 | LABETALOL HYDROCHLORIDE INJECTION USP | Not specified | Not specified |
| 02243539 | APO-LABETALOL | Not specified | Not specified |
| 02489406 | RIVA-LABETALOL | Not specified | Not specified |
| 02541505 | LABETALOL HYDROCHLORIDE INJECTION USP | Not specified | Not specified |
| 02106272 | TRANDATE | Not specified | Not specified |

Eleven valid single-ingredient licences are listed in total. The five above are shown as the main ones.

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (not taken from the product label): these include liver failure, liver disease, hepatic encephalopathy, kidney disease, anuria, diabetes mellitus, diabetic ketoacidosis, atrioventricular block, pulmonary emphysema, bronchial disease, hypotensive disorder, pancreatitis, gout, systemic lupus erythematosus, and others.
- **Drug Interactions**: 100 interactions were identified. Examples:
  - **Major**: epinephrine, dolasetron
  - **Moderate**: corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), morphine, anticholinergics (atropine, hyoscyamine, dicyclomine, methscopolamine), SGLT2 inhibitors (canagliflozin, dapagliflozin), chlorpropamide, cimetidine, calcium salts
  - **Minor**: acetylsalicylic acid, magnesium oxide
- **Other safety concern**: non-selective beta-blockade may cause bronchospasm, which matters for the pulmonary hypertension predictions.

Please also refer to the Health Canada package insert for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The evidence level is L5: there are no trials or specific literature for the predicted indication. The indication also largely overlaps with labetalol's existing hypertension use, so it adds little as a true repurposing opportunity. The pulmonary hypertension predictions carry a safety concern and no supporting evidence.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example, from DrugBank)
- Clinical or observational evidence of labetalol use in malignant hypertensive nephrosclerosis or renal outcomes
- Approved indication text and dosage forms for the Canadian licences, to confirm how the new indication relates to existing labelling
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

