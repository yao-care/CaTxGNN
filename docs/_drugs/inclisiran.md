---
layout: default
title: Inclisiran
parent: Model Prediction Only (L5)
nav_order: 476
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Inclisiran: predicted new indication Potassium deficiency disease (evidence level L5). Approved use: Not available in the compiled data"
monitor_inn: "Inclisiran"
predicted_indications: ["potassium deficiency disease", "esophageal disease", "atypical coarctation of aorta", "migraine disorder", "non-syndromic esophageal malformation", "migraine with brainstem aura", "aortic malformation", "esophageal ulcer", "Raynaud disease"]
---

# Inclisiran
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Inclisiran: From an Unspecified Original Indication to Potassium Deficiency Disease
{: .text-alpha }

## One-Sentence Summary

Inclisiran is a small interfering RNA (siRNA) marketed in Canada as LEQVIO. Its approved indication text was not available in the data compiled for this report, although its known pharmacology is LDL-cholesterol lowering.
The TxGNN model predicts it may be effective for **potassium deficiency disease**, but **no clinical trials and no publications** currently support this prediction, so it should be treated as a computational hypothesis only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (the Canadian licence record has no indication text) |
| Predicted New Indication | Potassium deficiency disease |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on general knowledge, inclisiran is an siRNA that silences hepatic PCSK9 expression. This increases LDL-receptor recycling and lowers LDL-C.

Review of the prediction finds **no plausible mechanistic link** between PCSK9 silencing and potassium homeostasis. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No trial or literature data back it up.

The other top-ranked predictions show the same pattern. These include esophageal disease, migraine disorders, atypical coarctation of the aorta, Raynaud disease and others. None has a clear mechanistic rationale, and none has supporting evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for potassium deficiency disease.

For context, two Phase 3 inclisiran trials appeared under a lower-ranked prediction (aortic malformation). They are pediatric familial hypercholesterolemia studies, and the link to that prediction is likely a matching artifact:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06597019](https://clinicaltrials.gov/study/NCT06597019) | Phase 3 | Recruiting | 60 | Safety, tolerability and efficacy of inclisiran vs placebo, then open-label, in children aged 6 to <12 years with heterozygous familial hypercholesterolemia |
| [NCT06597006](https://clinicaltrials.gov/study/NCT06597006) | Phase 3 | Recruiting | 9 | Same design in children aged 2 to <12 years with homozygous familial hypercholesterolemia |

These trials do not support the potassium deficiency prediction.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02518376 | LEQVIO | Not available | Not available |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the compiled data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no trials, no literature and no plausible mechanistic link between PCSK9 silencing and potassium homeostasis. The evidence level is L5 (model prediction only). Safety screening cannot proceed because Canadian package insert data are missing.

**To proceed, the following is needed:**
- The Health Canada package insert, including approved indication, warnings and contraindications
- Mechanism of action data from DrugBank
- A credible biological rationale linking PCSK9 silencing to potassium deficiency, followed by supporting preclinical or clinical data
- Consideration of whether other candidates are better supported, such as lipid- or vascular-related conditions, although the current data show no evidence for any of the top 10 predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

