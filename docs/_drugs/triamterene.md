---
layout: default
title: Triamterene
parent: Moderate Evidence (L3-L4)
nav_order: 800
evidence_level: L4
indication_count: 6
---

# Triamterene
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **6** 
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

# Triamterene: From Potassium-Sparing Diuretic Therapy to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Triamterene is a collecting-duct ENaC-inhibiting, potassium-sparing diuretic; the evidence pack contains no on-file original indication or licensed product, as the drug is currently **not marketed in Canada**. The TxGNN model predicts a possible role in **Malignant Hypertensive Renal Disease**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only signal at the earliest screening stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available on file (no DIN-licensed products; drug not marketed in Canada) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.89% (rank 2755) |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data (DrugBank MOA field) is not currently available for this candidate. Based on the mechanistic notes accompanying the prediction, triamterene is a collecting-duct epithelial sodium channel (ENaC) inhibitor and functions as a potassium-sparing diuretic — a class with an established, if adjunctive, role in blood pressure and fluid management.

The predicted indication, malignant hypertensive renal disease, is pathophysiologically driven by vascular endothelial injury and marked activation of the renin-angiotensin-aldosterone system (RAAS), not by sodium/volume overload alone. A potassium-sparing diuretic does not address this core disease mechanism, and the model's own rationale flags this as an indirect, class-level inference rather than a disease-specific mechanistic fit. No direct clinical or preclinical data linking triamterene to this indication were found.

It is also worth noting that co-administration with RAAS-modifying agents (ACEi/ARB), which are typically central to managing this condition, carries a recognized hyperkalemia risk with potassium-sparing diuretics — a safety consideration that would need explicit evaluation if this direction were pursued further.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Canada Market Information

Triamterene currently has no DIN-licensed products on file in Canada (`total_licenses = 0`, market status: Not Marketed). No approved indication text is therefore available for this candidate.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug interaction data are not currently available in the evidence pack for this candidate; a DDI query returned no results.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate sits at decision stage S0 with L4 evidence — a mechanism-only inference with zero supporting clinical trials or literature, no confirmed MOA data, and no Canadian market presence to anchor a safety profile. There is currently no basis to advance beyond exploratory screening.

**To proceed, the following is needed:**
- Confirmed mechanism of action (DrugBank API query, per data gap DG002)
- Health Canada / product monograph warnings and contraindications (per data gap DG001, currently blocking safety review)
- Disease-specific preclinical or clinical evidence connecting triamterene to malignant hypertensive renal disease (current literature is absent)
- Hyperkalemia risk assessment for likely co-administration with RAAS-modifying agents in this patient population

**Note:** Among the six candidates in this evidence pack, *chronic pulmonary heart disease* (rank 6) shows a comparatively stronger signal — it has reached decision stage S1 ("Research Question") with actual supporting literature on triamterene-containing diuretic combinations in chronic heart failure/cor pulmonale, whereas the top-ranked candidate here has none. That direction may warrant separate follow-up evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

