---
layout: default
title: Fosinopril
parent: Model Prediction Only (L5)
nav_order: 414
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Fosinopril: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertension (hypertensive disorder)"
monitor_inn: "Fosinopril"
predicted_indications: ["malignant hypertensive renal disease"]
---

# Fosinopril
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

# Fosinopril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Fosinopril is an ACE inhibitor originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
but there are currently **0 clinical trials** and **0 directly relevant publications** supporting this direction, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder); the Canadian licence records contain no approved indication text |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Based on known information, fosinopril belongs to the ACE inhibitor class. These drugs lower angiotensin II and therefore blood pressure, and its efficacy in hypertension is established.

Renovascular hypertension depends heavily on the renin-angiotensin system, so blocking this pathway is mechanistically plausible. The high TxGNN score most likely reflects the close similarity between this disease and the approved hypertension indication, not new clinical evidence.

There is an important safety caveat. ACE inhibitors can precipitate acute renal failure in patients with bilateral renal artery stenosis or stenosis in a solitary kidney. This is a major concern for this particular predicted indication.

The other predictions follow the same pattern:
- **Malignant hypertensive renal disease** (99.87%): a plausible extension of the hypertension indication, since blocking the renin-angiotensin system may lower blood pressure and pressure inside the kidney's filtering units. No supporting studies were found.
- **Pulmonary hypertension** (two predictions, 99.87%): ACE inhibitors have not shown reliable benefit here, and systemic vasodilators may worsen oxygenation. The prediction appears to be driven by shared network features.
- **Braddock syndrome** (99.81%): no clear mechanistic rationale could be identified.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

For the top prediction (malignant renovascular hypertension), no related literature is available.

The only publications retrieved were for the third-ranked prediction, pulmonary hypertension owing to lung disease and/or hypoxia. Neither supports efficacy:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9923037](https://pubmed.ncbi.nlm.nih.gov/9923037/) | 1998 | Case report | Revue des maladies respiratoires | Two patients taking enalapril or fosinopril for hypertension developed hypoxic eosinophilic pneumonia with sub-acute respiratory failure. This is a safety signal, not efficacy evidence. |
| [31105790](https://pubmed.ncbi.nlm.nih.gov/31105790/) | 2019 | Preclinical/Bioinformatics | Experimental and Therapeutic Medicine | Gene-expression analysis in mouse mesangial cells in a diabetic nephropathy context. It is unrelated to pulmonary hypertension. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02247803 | TEVA-FOSINOPRIL | Not specified | Not specified |
| 02266008 | APO-FOSINOPRIL | Not specified | Not specified |
| 02459396 | FOSINOPRIL | Not specified | Not specified |
| 02266016 | APO-FOSINOPRIL | Not specified | Not specified |
| 02247802 | TEVA-FOSINOPRIL | Not specified | Not specified |

All 6 licences are valid single-ingredient products with none cancelled. The table shows the first 5.

---

## Safety Considerations

- **Disease-level contraindication signals** (from the knowledge graph, not from label text):
  - Kidney disease and liver disease
  - Pancreatitis and gallbladder disease
  - Angioedema, including hereditary, acquired and RAAS-blocker-induced forms
  - Systemic lupus erythematosus and other connective tissue disease
  - Diabetes mellitus and diabetic ketoacidosis
  - Potassium deficiency and hyperparathyroidism
  - Neutropenia and agranulocytosis
  - Aortic stenosis and aortic valve disease
  - Hypotensive disorder
  - Hepatic coma and hepatic encephalopathy
  - Bone disease
- **Drug Interactions** (100 interactions recorded; examples shown):
  - **Major**: potassium bicarbonate and potassium citrate, which carry a risk of raised potassium.
  - **Moderate**: corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), aspirin, and glucose-lowering drugs (metformin, alogliptin, saxagliptin, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide). Others include bupropion, morphine, dronabinol, and bowel-preparation products.
- **Specific to the predicted indication**: ACE inhibitors may cause acute renal failure in bilateral renal artery stenosis or stenosis in a solitary kidney. Renal function and potassium monitoring would be required.

The package insert warnings and contraindications were not available. Please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the model score, with no clinical trials and no supporting literature (Evidence Level L5). The renal safety risk specific to renovascular disease is substantial, and the package insert safety information has not yet been reviewed.

**To proceed, the following is needed:**
- The Health Canada package insert, to complete warnings and contraindications review (this currently blocks safety screening)
- Mechanism of action data (for example from DrugBank)
- A targeted literature search on ACE inhibitors in renovascular and malignant hypertension, including renal safety in renal artery stenosis
- An assessment of whether the existing approved hypertension indication already covers severe or malignant forms
- A review of the biological plausibility of the lower-ranked predictions (pulmonary hypertension and Braddock syndrome) before any research question is framed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

