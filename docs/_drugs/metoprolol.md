---
layout: default
title: Metoprolol
parent: Model Prediction Only (L5)
nav_order: 604
evidence_level: L5
indication_count: 10
---

# Metoprolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Metoprolol: From Beta-Blocker Therapy to Malignant Renovascular Hypertension

## One-Sentence Summary

Metoprolol is a beta-blocker marketed in Canada under many brand and generic products. The supplied data does not list its labelled indications.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**.
However, there are **0 clinical trials** and only **2 publications**, and neither publication studies metoprolol in this condition, so the prediction rests almost entirely on the model score.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, metoprolol is a beta-1 selective blocker. Its use in cardiovascular conditions is well established, and mechanistically it may be applicable to hypertensive disease.

The most plausible link is that beta-1 blockade lowers renin release. Renin drives blood pressure elevation in renovascular hypertension. This is a reasonable hypothesis but remains unverified. No trial or study in the evidence pack tests it, and the supplied data does not include metoprolol's approved indications. It is also unclear whether this counts as true repurposing, since metoprolol is already used for hypertension.

Two other predictions for this drug have more supporting evidence than this one (both rated L3): chronic pulmonary heart disease and septal myocardial infarction. They are worth reviewing before this one.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15231398](https://pubmed.ncbi.nlm.nih.gov/15231398/) | 2004 | Other (case report) | Survey of Ophthalmology | A 26-year-old woman had hypertensive optic neuropathy caused by renal artery stenosis due to Takayasu's arteritis. Metoprolol is not evaluated. |
| [1988765](https://pubmed.ncbi.nlm.nih.gov/1988765/) | 1991 | Diagnostic study | Medicine | Chromogranin A had good sensitivity (83%) and specificity (96%) for diagnosing pheochromocytoma in the differential diagnosis of hypertension. Metoprolol is not evaluated. |

Neither paper provides evidence for metoprolol treating malignant renovascular hypertension.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2350408 | METOPROLOL |
| 2315327 | RIVA-METOPROLOL-L |
| 648027 | PRO-METOPROLOL-L |
| 2230803 | PMS-METOPROLOL-L |
| 842656 | TEVA-METOPROLOL |

Dosage form and approved indication text were not provided for these products. The list shows 5 of the 20 authorizations.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a model-only prediction (L5) with no registered trials and no relevant literature. The 2 retrieved papers concern other conditions. The mechanistic link (renin suppression) is plausible but untested.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Metoprolol's labelled indications, to confirm whether this is true repurposing or overlaps with existing hypertension use
- Mechanism of action data from DrugBank
- Targeted searches for metoprolol or beta-blockers in renovascular or malignant hypertension
- Consider prioritizing the better-supported predictions (chronic pulmonary heart disease, septal myocardial infarction)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

