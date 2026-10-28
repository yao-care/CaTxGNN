---
layout: default
title: Metoprolol
parent: Model Prediction Only (L5)
nav_order: 609
evidence_level: L5
indication_count: 6
monitor_inn: "Metoprolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease", "trichotillomania"]
last_modified_at: 2026-10-23
description: "Metoprolol: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension"
---

# Metoprolol
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

## Metoprolol: From Hypertension to Malignant Hypertensive Renal Disease
{: .text-alpha }

## One-Sentence Summary

Metoprolol is a beta-1 selective blocker that is marketed in Canada and is used for hypertension, acute coronary syndrome and myocardial infarction.
The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**, but **no clinical trials and no publications** specific to this disease were found, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (a relation recorded in the knowledge graph; the Canadian licence records compiled for this report contain no indication text) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses on record: at least 20) |
| Number of DINs | at least 20 |
| Number of approvals | At least 20 single-ingredient licences (the list may be partial) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Metoprolol is generally understood as a beta-1 selective blocker. Blocking beta-1 receptors lowers heart rate and blood pressure and reduces renin release, which could plausibly matter in hypertension-related kidney injury.

The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It is not evidence of efficacy in this disease.

There is also a practical limit. Malignant hypertension is an emergency, usually managed with titratable intravenous agents, so oral metoprolol is unlikely to be a primary therapy. No study of metoprolol in this condition was found.

## Other Predictions Reviewed

For completeness, the other predicted indications in the data are summarised below. None of them has a direct study of this drug in the predicted disease.

| Predicted Disease | Score | Evidence Level | Comment |
|------|------|------|------|
| Pulmonary hypertension, unclear multifactorial mechanism | 0.9991 | L5 | No studies. Beta-blockers are generally not recommended in pulmonary arterial hypertension, so there is a potential safety concern. |
| Pulmonary hypertension owing to lung disease and/or hypoxia | 0.9991 | L5 | The retrieved publications are mostly unrelated (intoxication, arrhythmia, animal studies). Beta-blockade in hypoxic lung disease raises safety questions. |
| Braddock syndrome | 0.9989 | L5 | No studies and no mechanistic rationale. |
| Chronic pulmonary heart disease | 0.9940 | L5 | The trials and papers address COPD with heart failure, not this disease itself (see below). |
| Trichotillomania | 0.9905 | L5 | No studies and no mechanistic rationale. |

For chronic pulmonary heart disease, the available studies concern beta-blocker safety in COPD combined with cardiac disease, not treatment of the pulmonary heart disease itself. These studies address related conditions rather than the predicted disease, so the evidence level is L5. The research question is worth noting, but it is not direct evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered for malignant hypertensive renal disease.

## Literature Evidence

Currently no related literature available for malignant hypertensive renal disease.

## Canada Market Information

At least 20 single-ingredient metoprolol licences are valid (the list may be partial). The licence records compiled for this report do not include dosage form or approved indication text. The first five are shown.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02350408 | METOPROLOL | Not listed | Not listed |
| 02315327 | RIVA-METOPROLOL-L | Not listed | Not listed |
| 00648027 | PRO-METOPROLOL-L | Not listed | Not listed |
| 02230803 | PMS-METOPROLOL-L | Not listed | Not listed |
| 00842656 | TEVA-METOPROLOL | Not listed | Not listed |

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** The knowledge graph lists many conditions as contraindicated or of concern with metoprolol. They include diabetes mellitus and diabetic ketoacidosis, liver disease and hepatic encephalopathy, pancreatitis, gallbladder disease, myasthenia gravis, systemic lupus erythematosus, psoriasis, gout, hypotensive disorder, pheochromocytoma, anxiety and mood disorders, and several electrolyte and parathyroid disorders. These are model-graph relations and should be checked against the product monograph.
- **Drug Interactions:** 100 interactions were found in the interaction database. Those shown are mostly Moderate, including epinephrine, bupropion, cimetidine, morphine, canagliflozin, dapagliflozin, chlorpropamide, and several corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone). Acetylsalicylic acid and magnesium oxide are Minor.
- **Class concern:** Beta-blockade in pulmonary hypertension and hypoxic lung disease raises safety questions (see above).

Package insert warnings and contraindications were not available, so please refer to the Health Canada product monograph.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score, but no trial or publication studies metoprolol in malignant hypertensive renal disease (evidence level L5). The clinical setting favours intravenous, titratable therapy, and the label-based safety review has not been done.

**To proceed, the following is needed:**
- Health Canada product monograph warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Any clinical or observational evidence of metoprolol in hypertensive renal injury
- Clinical review of whether an oral beta-blocker has any role in this emergency setting
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

