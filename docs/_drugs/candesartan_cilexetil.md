---
layout: default
title: Candesartan Cilexetil
parent: Model Prediction Only (L5)
nav_order: 151
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Candesartan Cilexetil: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension / hypertensive disorder"
monitor_inn: "CANDESARTAN CILEXETIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
---

# Candesartan Cilexetil
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

# Candesartan Cilexetil: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Candesartan cilexetil is an angiotensin II receptor blocker originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but **no clinical trials and no publications** currently support this specific prediction, so it remains a model-based research question.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension / hypertensive disorder (the Canadian licence records provide no indication text, so this comes from the knowledge graph) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L4 (indirect, class-level mechanistic reasoning only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known information, candesartan cilexetil is an angiotensin II type 1 receptor blocker (ARB). Its efficacy in hypertension is established, and mechanistically it may be applicable to hypertension-driven kidney disease.

Malignant hypertensive renal disease involves severe, accelerated hypertension with overactivation of the renin-angiotensin-aldosterone system (RAAS). Blocking angiotensin II signalling is therefore biologically plausible. The new indication is essentially an extension of the approved hypertension indication, which makes the prediction coherent.

This support is indirect, though. It rests on class-level reasoning and the model score, not on disease-specific clinical data. A high TxGNN score reflects network-level associations and does not replace clinical evidence.

Other predictions in the same analysis:

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Malignant renovascular hypertension | 99.68% | L4 | Angiotensin II is central to this condition, but ARBs carry a risk of acute renal function decline in bilateral renal artery stenosis or a solitary kidney |
| Pulmonary hypertension owing to lung disease and/or hypoxia | 99.67% | L4 | The two retrieved publications do not directly support it; systemic vasodilators may worsen ventilation-perfusion matching |
| Pulmonary hypertension with unclear multifactorial mechanism | 99.67% | L5 | Model prediction only |
| Braddock syndrome | 99.56% | L5 | No clear mechanistic connection identified |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the leading prediction (malignant hypertensive renal disease).

## Canada Market Information

Candesartan cilexetil has 20 valid single-ingredient licences in Canada and none cancelled. The records provided do not include dosage forms or approved indication text. Five of the licences are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02239092 | ATACAND | Not specified | Not specified |
| 02239090 | ATACAND | Not specified | Not specified |
| 02326957 | SANDOZ CANDESARTAN | Not specified | Not specified |
| 02366320 | TEVA-CANDESARTAN | Not specified | Not specified |
| 02391198 | PMS-CANDESARTAN | Not specified | Not specified |

## Safety Considerations

**Contraindications and cautions suggested by the knowledge graph** (these come from drug-disease relationships, not from label text, and must be checked against the package insert):

- Kidney and circulation: impaired renal function, anuria, renal artery obstruction, hypotensive disorder
- Metabolic: diabetes mellitus, diabetic ketoacidosis, potassium deficiency, hyperuricaemia, gout, hypercalcaemia, phosphorus metabolism disease, nephrocalcinosis
- Liver and digestive: liver disease, hepatic coma, hepatic encephalopathy, pancreatitis, gallbladder disease, neonatal jaundice
- Endocrine and bone: hyperparathyroidism, osteitis fibrosa
- Autoimmune: systemic lupus erythematosus (including paediatric)

**Points specific to the predicted indications:**
- For renovascular hypertension, ARBs can cause acute renal function decline in bilateral renal artery stenosis or a solitary kidney, so careful safety evaluation is needed.
- For pulmonary hypertension due to lung disease or hypoxia, systemic vasodilators may worsen ventilation-perfusion matching.

No drug interaction data were found. Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible as an extension of the approved hypertension indication, with a high model score (99.68%). However, there are no clinical trials or publications for this indication, and the label-based safety information is missing. The evidence supports only a research question at this stage.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Detailed mechanism-of-action data from DrugBank
- A targeted literature and trial search on ARB use in malignant hypertensive nephropathy
- A renal safety plan, particularly for renal artery stenosis and impaired renal function
- Drug interaction data
- Approved indication text and dosage forms for the Canadian licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

