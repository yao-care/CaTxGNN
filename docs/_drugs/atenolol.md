---
layout: default
title: Atenolol
parent: Moderate Evidence (L3-L4)
nav_order: 78
evidence_level: L4
indication_count: 9
last_modified_at: 2026-10-13
description: "Atenolol: predicted new indication Posteroinferior myocardial infarction (evidence level L4). Approved use: Hypertension, myocardial infarction"
monitor_inn: "ATENOLOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "chronic pulmonary heart disease"]
---

# Atenolol
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **9** 
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

# Atenolol: From Hypertension and Myocardial Infarction to Posteroinferior Myocardial Infarction

## One-Sentence Summary

Atenolol is a beta-1 selective blocker originally used for hypertension and myocardial infarction.
The TxGNN model predicts it may be effective for **posteroinferior myocardial infarction**, but this is largely a sub-classification of an indication it already covers.
Evidence is thin: **0 clinical trials** and **1 publication** (a small 1985 crossover study) are available for this specific prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, myocardial infarction (approved indication text for the Canadian licences is not available; the original indications come from the knowledge graph) |
| Predicted New Indication | Posteroinferior myocardial infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, atenolol is a beta-1 selective blocker. It lowers heart rate, contractility and myocardial oxygen demand, and its efficacy in hypertension and myocardial infarction is well established.

Posteroinferior myocardial infarction is a location-based subtype of myocardial infarction. The same beta-1 blockade rationale applies to any MI location, so this prediction is better seen as a re-labelling of an existing indication than as true repurposing. This also explains the very high model score.

The other top predictions follow a similar pattern. Posterolateral and septal myocardial infarction are further MI subtypes. Malignant renovascular hypertension and malignant hypertensive renal disease are extensions of the hypertension indication. Pulmonary hypertension and chronic pulmonary heart disease appear to be driven by the shared "hypertension" label. Beta-blockers are not an established therapy there, and negative inotropy may worsen right ventricular function. Braddock syndrome has no identifiable mechanistic basis in the data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3901170](https://pubmed.ncbi.nlm.nih.gov/3901170/) | 1985 | Randomized single-blind crossover trial | La Revue de médecine interne | In 23 patients 4 weeks after a posteroinferior or anterior MI with residual ischaemia, atenolol 200 mg and diltiazem 240 mg were compared for anti-ischaemic activity using computerized exercise testing. Small and indirect. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02266660 | TEVA-ATENOLOL | Not listed | Not listed |
| 02171805 | TEVA-ATENOLOL | Not listed | Not listed |
| 02466465 | ATENOLOL | Not listed | Not listed |
| 02541564 | ATENOLOL | Not listed | Not listed |
| 02277379 | RIVA-ATENOLOL | Not listed | Not listed |

Twenty single-ingredient licences are currently valid, and none are cancelled. Only the first five are shown here.

---

## Safety Considerations

- **Disease contraindication signals from the knowledge graph** (not label text): liver failure, anxiety and neurotic disorders, dysthymic disorder, pancreatitis, systemic lupus erythematosus, asthma (including intrinsic and allergic), potassium deficiency, psoriasis, gout and hyperuricaemia, anuria, hypercalcaemia and nephrocalcinosis, phosphorus metabolism disease, type 1 and type 2 diabetes (including diabetic ketoacidosis), atrioventricular block, Raynaud disease and anaphylaxis.
- **Drug interactions:** 100 interactions were identified. The retrieved list includes moderate-level interactions with epinephrine, hydrocortisone, hyoscyamine, bupropion, triamcinolone, morphine, acetohexamide, atropine, betamethasone, budesonide and several calcium salts. Minor-level interactions include acetylsalicylic acid, aluminum hydroxide and attapulgite.
- **Use in lung disease:** The literature for the pulmonary predictions raises caution about bronchospasm and right ventricular compensation. Atenolol is also renally cleared and needs dose adjustment in renal impairment.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is a sub-classification of an indication atenolol already has, so it offers little new value. The only supporting evidence is one small, old, indirect crossover study. None of the other seven predictions has direct clinical evidence, and the pulmonary hypertension predictions carry safety concerns.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Confirmation of whether the approved Canadian labels already cover myocardial infarction generally, which would make the subtype prediction redundant
- If pursuing a true repurposing direction, direct human evidence for a distinct indication (the pulmonary predictions are not supported)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

