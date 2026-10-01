---
layout: default
title: Mecasermin
parent: Model Prediction Only (L5)
nav_order: 570
evidence_level: L5
indication_count: 5
---

# Mecasermin
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

# Mecasermin: From Severe Primary IGF-1 Deficiency to Monosomy X

## One-Sentence Summary

Mecasermin (recombinant human IGF-1, marketed in Canada as INCRELEX) is used for severe primary IGF-1 deficiency, a growth-related condition.
The TxGNN model predicts it may be effective for **monosomy X (Turner syndrome)**, but this is currently a **model prediction only**, with **0 clinical trials** and **0 publications** supplied as support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Severe primary IGF-1 deficiency (from the candidate's mechanistic rationale; the Canadian licence record supplied has no indication text) |
| Predicted New Indication | Monosomy X |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, mecasermin is recombinant human IGF-1 and acts on the growth axis. Its efficacy in IGF-1 deficiency-related growth failure is established, and mechanistically it may be applicable to short stature in monosomy X.

Monosomy X (Turner syndrome) is characterized by short stature, which is why the model links it to a growth-axis drug. However, the link is indirect. Turner short stature is usually managed through the growth hormone (GH) pathway, not by IGF-1 replacement. Without MOA data, the high score (99.59%) cannot be cross-checked against a mechanism. No trials or literature were supplied, so the prediction stands on the model alone.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| Licence Number | Product Name |
|---------|------|
| 2509733 | INCRELEX |

Dosage form, manufacturer, and approved indication text are not available in the supplied record.

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the queried database.

Please refer to the package insert for warnings and contraindications. General concerns for IGF-1 therapy noted in the candidate analysis include hypoglycemia, fluid and tissue growth effects, and a theoretical neoplasia risk.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. No trials or literature exist in the supplied evidence, the mechanistic link is indirect, and the standard approach for Turner short stature is the GH pathway.

**To proceed, the following is needed:**
- Mechanism of action data (DrugBank) to cross-check the model score
- Health Canada package insert warnings and contraindications
- A targeted literature and trial registry search for mecasermin or IGF-1 in Turner syndrome
- Approved indication text and dosage form for the Canadian licence

**Other candidates:** Among the other four predictions, "growth hormone insensitivity syndrome with immune dysregulation 2, autosomal dominant" (score 99.06%) is the most mechanistically coherent. Growth hormone insensitivity causes low IGF-1 despite normal or high GH, and mecasermin directly replaces IGF-1. It is flagged as a Research Question and would need its own literature and registry search before any staging. The remaining candidates are on Hold: Wolman disease has no clear mechanistic connection, and the two esophageal varices entries look like duplicates with a weak, indirect rationale.

---

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

