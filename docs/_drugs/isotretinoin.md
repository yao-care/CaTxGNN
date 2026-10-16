---
layout: default
title: Isotretinoin
parent: Model Prediction Only (L5)
nav_order: 504
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Isotretinoin: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertensive disorder / hypertension"
---

# Isotretinoin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Isotretinoin: From Hypertensive Disorder to Malignant Renovascular Hypertension

## One-Sentence Summary

Isotretinoin is listed in the data compiled for this report with an original indication of hypertensive disorder (hypertension). This annotation is unusual, because isotretinoin is generally known as a retinoid for severe acne. The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder / hypertension (from the knowledge graph; the Canadian licence records contain no indication text) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 12 |
| Recommended Decision | Hold |

A second prediction, **malignant hypertensive renal disease**, has the same score (99.01%) and the same lack of supporting evidence.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Isotretinoin is a retinoid, and retinoids act mainly through RAR/RXR-mediated gene regulation. Any effect on renovascular hypertension would therefore be speculative. Possible routes include modulation of renin-angiotensin signaling or vascular remodeling, but nothing in the data compiled for this report supports them.

The original indication recorded here (hypertensive disorder) conflicts with isotretinoin's well-known use in severe acne. The input annotation may be wrong, so the link between the "original" and the predicted indication should not be taken at face value. The two predictions have identical scores, which suggests the two disease terms are closely related in the knowledge graph. This is a graph-based similarity, not clinical evidence.

For malignant hypertensive renal disease, a hypothetical rationale would involve retinoid effects on renal injury or fibrosis pathways. This is also unsupported by the available data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02396998 | EPURIS | Not specified | Not specified |
| 02257955 | CLARUS | Not specified | Not specified |
| 02257963 | CLARUS | Not specified | Not specified |
| 02539071 | ABSORICA LD | Not specified | Not specified |
| 00582344 | ACCUTANE | Not specified | Not specified |

Showing 5 of 12 valid single-ingredient licences (EPURIS, CLARUS, ABSORICA LD, ACCUTANE). None are cancelled.

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text):** The knowledge graph links isotretinoin to contraindications in many conditions. Those most relevant to the proposed use include:
  - kidney disease and liver disease
  - hypotensive disorder
  - diabetes mellitus and diabetic ketoacidosis
  - pancreatitis and gallbladder disease
  - inflammatory bowel disease
  - osteoporosis
  - psychotic, anxiety and other mental disorders
  - angioedema (several forms)
  - neutropenia and agranulocytosis
  - systemic lupus erythematosus
  - potassium deficiency
- **Drug interactions:** 98 interactions are recorded in total. The main ones are:
  - **Major:** doxycycline, minocycline, tetracycline, vitamin A
  - **Moderate:** corticosteroids (betamethasone, budesonide, dexamethasone, hydrocortisone, prednisolone, prednisone, triamcinolone), warfarin, dicoumarol, ethanol, naltrexone, nitisinone, fostamatinib, ivacaftor, lumacaftor, abametapir (topical)
- **Class concerns:** Retinoids are known to cause teratogenicity, hyperlipidaemia and hepatotoxicity. These matter for a cardiovascular and renal population, which is often on multiple medicines.

Please refer to the Health Canada package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high model score (99.01%), with no clinical trials, no literature and no mechanism data. The original indication is also doubtful. The safety profile, including many kidney and liver contraindication signals and numerous interactions, adds caution for patients with severe hypertension and renal involvement.

**To proceed, the following is needed:**
- Verification of the original indication annotation, which conflicts with isotretinoin's known use
- Mechanism of action data (for example from DrugBank)
- Health Canada package insert warnings and contraindications, which are required before safety screening can proceed
- A targeted literature and trial search on retinoids in renovascular hypertension and hypertensive renal disease
- Preclinical or mechanistic evidence for a plausible link to blood pressure or renal injury pathways
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

