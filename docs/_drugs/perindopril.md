---
layout: default
title: Perindopril
parent: Model Prediction Only (L5)
nav_order: 723
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-31
monitor_inn: "perindopril"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
description: "Perindopril: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Perindopril
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

## Perindopril: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Perindopril is an ACE inhibitor originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but **no clinical trials** and only **1 indirectly related publication** currently support this direction, so the prediction remains a computational hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9977 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses on record: at least 20) |
| Number of DINs | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, perindopril is an angiotensin-converting enzyme (ACE) inhibitor. It blocks the formation of angiotensin II, which lowers blood pressure and reduces pressure inside the kidney's filtering units (intraglomerular pressure).

Malignant hypertension with kidney injury is strongly driven by activation of the renin-angiotensin system (RAS). Perindopril's mechanism therefore overlaps with its approved hypertension use, and the prediction is biologically plausible.

However, the only publication retrieved concerns solitary kidney function after nephrectomy for renal cancer. It does not study perindopril in malignant hypertensive kidney disease. The high TxGNN score is a computational prediction, not clinical evidence.

Other predicted indications are weaker still:
- **Malignant renovascular hypertension:** mechanistically plausible, but no trials or literature were found. ACE inhibitors also carry a known risk of acute kidney injury in bilateral renal artery stenosis or a solitary stenotic kidney.
- **Pulmonary hypertension (lung disease/hypoxia):** only animal studies, such as perindopril with amlodipine in hypoxic rats, offer indirect support. No human efficacy data were found.
- **Pulmonary hypertension with unclear multifactorial mechanism and Braddock syndrome:** no trials or literature; these are predictions from the TxGNN model (deep learning) only, and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36382821](https://pubmed.ncbi.nlm.nih.gov/36382821/) | 2022 | Other (indirect) | Urologiia (Moscow) | Functional state of a solitary kidney after nephrectomy for renal cancer; does not address perindopril in malignant hypertensive nephropathy |

---

## Canada Market Information

Perindopril has 20 valid single-ingredient authorisations in Canada, with no cancelled licences. Dosage form and approved indication text were not available in the data compiled for this report. Main products:

| DIN | Product Name |
|---------|------|
| 02479885 | PERINDOPRIL ERBUMINE |
| 02474824 | MAR-PERINDOPRIL |
| 02555697 | NB-PERINDOPRIL |
| 02465000 | TEVA-PERINDOPRIL |
| 02470241 | SANDOZ PERINDOPRIL ERBUMINE |

---

## Safety Considerations

- **Disease contraindications (knowledge-graph data, not label text):** kidney disease, liver disease, gallbladder disease, angioedema (including acquired, hereditary, and RAAS-blocker-induced forms), neutropenia, agranulocytosis, hypotensive disorder, connective tissue disease, bone and cartilage disease, renal artery obstruction, and pyoureter. Renal artery obstruction and kidney disease are especially relevant to the predicted renal indications.
- **Drug interactions:** 213 interactions were recorded. Major-level ones include **potassium citrate** and **potassium bicarbonate** (risk of raised potassium). Moderate-level ones include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), antidiabetic agents (metformin, alogliptin, saxagliptin, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide), acetylsalicylic acid, morphine, bupropion, and dronabinol.
- **Case reports:** ACE inhibitor-triggered angioedema, including airway-threatening cases, appeared in the retrieved literature as a safety signal.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (0.9977), and the ACE-inhibition mechanism is plausible for hypertension-related kidney injury. However, there are no clinical trials, and the single publication retrieved is not relevant to perindopril. The evidence is limited to model prediction and indirect reasoning. The kidney-related safety concerns also need careful assessment.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- A targeted literature search on ACE inhibitors in malignant hypertensive nephropathy
- Renal safety assessment, including renal artery stenosis and kidney function monitoring
- Indication text and dosage forms for the Canadian authorisations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

