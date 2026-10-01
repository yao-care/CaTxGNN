---
layout: default
title: Fostamatinib
parent: Model Prediction Only (L5)
nav_order: 413
evidence_level: L5
indication_count: 10
---

# Fostamatinib
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

# Fostamatinib: From Chronic Immune Thrombocytopenia to Autosomal Thrombocytopenia with Normal Platelets

## One-Sentence Summary

Fostamatinib is a SYK inhibitor marketed as TAVALISSE and approved for chronic immune thrombocytopenia (ITP).
The TxGNN model predicts it may be effective for **autosomal thrombocytopenia with normal platelets**, a hereditary platelet disorder.
This prediction currently has **0 clinical trials** and **0 publications** behind it, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic immune thrombocytopenia (from the mechanism notes; the license records carry no indication text) |
| Predicted New Indication | Autosomal thrombocytopenia with normal platelets |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Based on known information, fostamatinib's active metabolite R406 inhibits spleen tyrosine kinase (SYK). In chronic ITP this reduces Fc-receptor-mediated destruction of platelets by immune cells. Its efficacy in ITP is established, and it may be applicable to other low-platelet conditions.

The link to the predicted indication is weak. Autosomal thrombocytopenia with normal platelets is hereditary, so immune-mediated platelet destruction, the process fostamatinib blocks, may not drive it. Whether the drug could help depends on the specific genetic cause, which has not been established. The rationale is therefore inferred from the ITP setting and the model score, not from disease-specific data. It could not be checked against the product label because the original indication and mechanism fields were missing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2508052 | TAVALISSE |
| 2508060 | TAVALISSE |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical or literature support (L5). Its mechanistic fit is uncertain, because most hereditary thrombocytopenias are caused by production defects rather than immune platelet destruction. The other nine model predictions are also weak. Several are ranked highly but have no plausible SYK-related mechanism, such as esophageal malformation, biotin metabolic disease, filariasis and vitamin deficiency. The glaucoma results are only general kinase-inhibitor reviews. Esophageal disease has only two cell-based cancer studies.

**To proceed, the following is needed:**
- The genetic cause of the target disease, and whether platelet loss involves any SYK- or Fc-receptor-driven component
- Mechanism of action data for fostamatinib, and confirmation of its original indication from the Health Canada label
- Health Canada package insert warnings and contraindications, needed before any safety screening
- A targeted search for disease-specific preclinical or case evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

