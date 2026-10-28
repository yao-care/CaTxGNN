---
layout: default
title: Acebutolol
parent: Model Prediction Only (L5)
nav_order: 16
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Acebutolol: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension / hypertensive disorder"
monitor_inn: "ACEBUTOLOL"
predicted_indications: ["malignant hypertensive renal disease"]
---

# Acebutolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Acebutolol: From Hypertension to Malignant Hypertensive Renal Disease
{: .text-alpha }

## One-Sentence Summary

Acebutolol is a beta-blocker originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease** (and the related **malignant renovascular hypertension**), but this is a model prediction only, with **0 clinical trials** and **1 indirect publication** (from 1975) supporting the direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension / hypertensive disorder (the Health Canada licence records contain no indication text) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9910 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 6 of 6) |
| Number of DINs | 6 (valid: 6) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, acebutolol is a cardioselective beta-1 blocker with intrinsic sympathomimetic activity. Its efficacy in hypertension is established, and mechanistically it may be applicable to hypertensive renal disease.

Beta-1 blockade reduces renin release from the kidney and lowers blood pressure. Both effects are plausibly relevant to hypertension-related kidney damage and to renovascular hypertension, which is largely driven by activation of the renin-angiotensin system.

However, the high score (0.9910) most likely reflects the close semantic similarity between these conditions and the approved hypertension indication. It should not be read as independent evidence of benefit. Malignant hypertension is a hypertensive emergency, usually managed with parenteral agents and therapy targeting the renin-angiotensin system, so oral acebutolol would not be a standard choice.

A second predicted indication, **malignant renovascular hypertension**, has the same score (0.9910) and the same limitations.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Only one publication was found, and it relates to the second predicted indication (malignant renovascular hypertension). No literature was found for malignant hypertensive renal disease.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [768911](https://pubmed.ncbi.nlm.nih.gov/768911/) | 1975 | Clinical study (open, uncontrolled) | La Nouvelle presse medicale | In 50 hypertensive patients treated for one year with acebutolol alone or combined with other antihypertensives, results were good or moderate in 74% and treatment failed in 26%. The drug was well tolerated. This is indirect evidence for general arterial hypertension, not specifically for malignant renovascular hypertension. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02204525 | TEVA-ACEBUTOLOL | Not specified | Not specified |
| 02147629 | APO-ACEBUTOLOL | Not specified | Not specified |
| 02204517 | TEVA-ACEBUTOLOL | Not specified | Not specified |
| 02204533 | TEVA-ACEBUTOLOL | Not specified | Not specified |
| 02147610 | APO-ACEBUTOLOL | Not specified | Not specified |

Six valid single-ingredient licences are held in total. Only the first five are listed here; the sixth is APO-ACEBUTOLOL (DIN 02147602). No cancelled licences.

---

## Safety Considerations

Contraindications drawn from the knowledge graph (not from label text) cover the following disease areas:

- **Cardiovascular**: atrioventricular block, sick sinus syndrome, peripheral vascular disease (including intermittent claudication and peripheral arterial disease)
- **Respiratory**: asthma (intrinsic and allergic), pulmonary emphysema
- **Endocrine and metabolic**: diabetes mellitus, diabetic ketoacidosis, phaeochromocytoma and related adrenal or paraganglionic tumours
- **Neuromuscular**: myasthenia gravis and neuromuscular junction disease
- **Organ disease**: kidney disease, liver disease, gallbladder disease
- **Skin**: psoriasis and parapsoriasis
- **Psychiatric**: anxiety disorder, neurotic disorder, dysthymic disorder
- **Other**: pyoureter, and cancers of the duodenum, small intestine, heart and adrenal gland

Kidney disease appears in this list, which is directly relevant to a renal indication and needs careful review.

**Drug Interactions**: 100 interactions were identified; the first 20 retrieved are summarised here.
- **Moderate**: acetohexamide, chlorpropamide, canagliflozin, dapagliflozin (antidiabetic agents), atropine, clidinium, betamethasone, budesonide, bupropion, cimetidine, and calcium salts (acetate, carbonate, citrate, glubionate, gluconate, lactate, phosphate)
- **Minor**: aluminium hydroxide, acetylsalicylic acid, attapulgite

For package-insert warnings and contraindications, please refer to the product monograph, as this information is not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone. No clinical trials exist, and the only publication is a 1975 uncontrolled study of general hypertension. Malignant hypertensive renal disease is an emergency normally treated with other agents, and kidney disease appears among the graph-derived contraindications.

**To proceed, the following is needed:**
- Package-insert warnings and contraindications from Health Canada (a blocking gap for safety screening)
- Mechanism of action data (for example, from DrugBank)
- Targeted literature review on beta-blockers in malignant hypertension and hypertensive nephropathy
- Assessment of whether acebutolol offers any advantage over current standard therapy
- Review of renal-safety implications, given that kidney disease appears among the contraindications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

