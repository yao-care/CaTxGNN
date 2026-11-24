---
layout: default
title: Isotretinoin
parent: Model Prediction Only (L5)
nav_order: 504
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "ISOTRETINOIN"
predicted_indications: ["malignant hypertensive renal disease"]
description: "Isotretinoin: predicted new indication Malignant hypertensive renal disease (evidence level L5). In Canada: 12 DINs (12 marketed)"
---

# Isotretinoin
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

## Isotretinoin: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Isotretinoin is listed in the data compiled for this report with an original indication of hypertensive disorder (hypertension). This annotation is unusual, because isotretinoin is generally known as a retinoid for severe acne. The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9901 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 12 of 12) |
| Number of DINs | 12 (marketed: 12) |
| Recommended Decision | Hold |

A second prediction, **malignant hypertensive renal disease**, has the same score (0.9901) and the same lack of supporting evidence.

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for isotretinoin: "The exact mechanism of action of Zenatane in the treatment of severe recalcitrant nodular acne in nonpregnant patients 12 years of age and older with multiple inflammatory nodules with a diameter of 5 mm or greater who are unresponsive to conventional therapy, including systemic antibiotics is unknown. Isotretinoin, a retinoid, inhibits sebaceous gland function and keratinization." ([DailyMed: Zenatane (isotretinoin) prescribing information, Dr. Reddy's Laboratories Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=27b3cf26-f22e-5b70-1c24-009933b7c6ee), label version 2026-09-20; accessed 2026-11-19.) Isotretinoin is a retinoid, and retinoids act mainly through RAR/RXR-mediated gene regulation. Any effect on renovascular hypertension would therefore be speculative. Possible routes include modulation of renin-angiotensin signaling or vascular remodeling, but nothing in the data compiled for this report supports them.

The original indication recorded here (hypertensive disorder) conflicts with isotretinoin's well-known use in severe acne. The input annotation may be wrong, so the link between the "original" and the predicted indication should not be taken at face value. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

For malignant hypertensive renal disease, a hypothetical rationale would involve retinoid effects on renal injury or fibrosis pathways. This is also unsupported by the available data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 00582344 | ACCUTANE | ISOTRETINOIN | Marketed |
| 00582352 | ACCUTANE | ISOTRETINOIN | Marketed |
| 02257955 | CLARUS | ISOTRETINOIN | Marketed |
| 02257963 | CLARUS | ISOTRETINOIN | Marketed |
| 02396971 | EPURIS | ISOTRETINOIN | Marketed |
| 02396998 | EPURIS | ISOTRETINOIN | Marketed |
| 02397005 | EPURIS | ISOTRETINOIN | Marketed |
| 02397013 | EPURIS | ISOTRETINOIN | Marketed |
| 02539047 | ABSORICA LD | ISOTRETINOIN | Marketed |
| 02539055 | ABSORICA LD | ISOTRETINOIN | Marketed |
| 02539063 | ABSORICA LD | ISOTRETINOIN | Marketed |
| 02539071 | ABSORICA LD | ISOTRETINOIN | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

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
The prediction rests only on a high model score (0.9901), with no clinical trials, no literature and no mechanism data. The original indication is also doubtful. The safety profile, including many kidney and liver contraindication signals and numerous interactions, adds caution for patients with severe hypertension and renal involvement.

**To proceed, the following is needed:**
- Verification of the original indication annotation, which conflicts with isotretinoin's known use
- Mechanism of action data (for example from DrugBank)
- Health Canada package insert warnings and contraindications, which are required before safety screening can proceed
- A targeted literature and trial search on retinoids in renovascular hypertension and hypertensive renal disease
- Preclinical or mechanistic evidence for a plausible link to blood pressure or renal injury pathways

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Zenatane (isotretinoin) prescribing information, Dr. Reddy's Laboratories Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=27b3cf26-f22e-5b70-1c24-009933b7c6ee) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

