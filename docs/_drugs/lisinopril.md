---
layout: default
title: Lisinopril
parent: Model Prediction Only (L5)
nav_order: 547
evidence_level: L5
indication_count: 10
---

# Lisinopril
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

# Lisinopril: From ACE Inhibitor Therapy to Posteroinferior Myocardial Infarction

## One-Sentence Summary

Lisinopril is an ACE inhibitor that is marketed in Canada. The record does not list an approved indication.
The TxGNN model predicts it may be effective for **posteroinferior myocardial infarction**,
but **0 clinical trials** and **0 publications** currently support this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the record (Canadian licence entries have no indication text) |
| Predicted New Indication | Posteroinferior myocardial infarction |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Lisinopril is an ACE inhibitor, and blocking the renin-angiotensin-aldosterone system (RAAS) is known to reduce adverse remodelling after a heart attack. Mechanistically, it may therefore apply to myocardial infarction.

Two cautions apply to this prediction:
- The score (99.90%) is identical to that of posterolateral myocardial infarction. This suggests the model is reflecting a shared parent-disease signal, not evidence specific to the posteroinferior subtype.
- There are no trials or publications for this subtype, so the prediction has no independent support.

**Other candidates in the same report.** Among the 10 predictions, the best-supported one is **chronic pulmonary heart disease** (rank 9, score 99.68%, provisional L3). It has two lisinopril-specific clinical publications (details below). Septal myocardial infarction (L4) has one indirect case report.

## Clinical Trial Evidence

Currently no related clinical trials registered for posteroinferior myocardial infarction.

## Literature Evidence

Currently no related literature available for posteroinferior myocardial infarction.

**For reference, the closest lisinopril-specific literature is under other predicted indications:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17047621](https://pubmed.ncbi.nlm.nih.gov/17047621/) | 2006 | Clinical study (design unverified) | Kardiologiia | In heart failure with ischemic heart disease and COPD, lisinopril 10 mg/day was reported to attenuate pulmonary hypertension and improve right ventricular function (chronic pulmonary heart disease) |
| [14524095](https://pubmed.ncbi.nlm.nih.gov/14524095/) | 2003 | Clinical study (design unverified) | Probl Tuberk Bolezn Legk | Lisinopril in patients with chronic cor pulmonale; no abstract available |
| [39018146](https://pubmed.ncbi.nlm.nih.gov/39018146/) | 2024 | Case report | JPMA | An ACE inhibitor plus coenzyme Q10 was used adjunctively in a patient with ventricular septal rupture after late-onset MI. It is not septal-MI specific and does not isolate lisinopril |

The 20 publications reported for "pulmonary hypertension owing to lung disease and/or hypoxia" are general hypoxia papers, such as brain aging and cancer metabolism. They do not involve lisinopril and should not be counted as evidence.

## Canada Market Information

Dosage form and approved indication text are empty in the source record, so only DIN and product name are shown. Five of the 20 authorizations are listed.

| DIN | Product Name |
|---------|------|
| 02049333 | ZESTRIL |
| 02386232 | LISINOPRIL |
| 02394499 | AURO-LISINOPRIL |
| 02394480 | AURO-LISINOPRIL |
| 02386240 | LISINOPRIL |

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction data were found in the record.

Prediction-specific concerns noted in the record:
- ACE inhibitors can precipitate acute renal failure in bilateral renal artery stenosis or a solitary kidney (relevant to the renovascular hypertension prediction).
- Renal function and hyperkalaemia risk need careful handling in malignant hypertensive renal disease.
- A published case report describes severe bradycardia and hypotension with concomitant tizanidine and lisinopril ([PMID 20852161](https://pubmed.ncbi.nlm.nih.gov/20852161/)).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication rests on a model score alone (L5). It has no trials or literature, and the identical score for a sibling subtype suggests a shared-parent artefact. Safety documentation is also missing, which blocks progression to safety screening.

**To proceed, the following is needed:**
- The Health Canada package insert (warnings, contraindications, approved indications, dosage forms)
- Mechanism of action data from DrugBank
- Evidence for MI at the parent-disease level, and confirmation of whether the subtype-level prediction adds anything
- Abstract-level review of the two lisinopril publications on chronic pulmonary heart disease to confirm design, sample size and outcomes, since the provisional L3 could fall to L4
- Route and dosage form compatibility assessment for the new indication

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

