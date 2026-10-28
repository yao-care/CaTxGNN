---
layout: default
title: Fostamatinib
parent: Model Prediction Only (L5)
nav_order: 416
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Fostamatinib: predicted new indication Autosomal thrombocytopenia with normal platelets (evidence level L5). Approved use: Thrombocytopenia due to immune destruction"
monitor_inn: "Fostamatinib"
predicted_indications: ["autosomal thrombocytopenia with normal platelets", "non-syndromic esophageal malformation"]
---

# Fostamatinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Fostamatinib: From Immune Thrombocytopenia to Autosomal Thrombocytopenia with Normal Platelets
{: .text-alpha }

## One-Sentence Summary

Fostamatinib is a SYK inhibitor originally used to treat thrombocytopenia caused by immune destruction of platelets.
The TxGNN model predicts it may be effective for **autosomal thrombocytopenia with normal platelets**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on computational similarity alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Thrombocytopenia due to immune destruction |
| Predicted New Indication | Autosomal thrombocytopenia with normal platelets |
| TxGNN Prediction Score | 0.9945 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 2 of 2) |
| Number of DINs | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, fostamatinib is a SYK (spleen tyrosine kinase) inhibitor, acting through its active metabolite R406. It is approved for chronic immune thrombocytopenia, where it reduces Fc receptor-mediated platelet destruction.

The predicted indication is an inherited thrombocytopenia, so the link to the approved indication is based on disease-category similarity (both are low platelet count conditions). However, most inherited thrombocytopenias are caused by defective platelet production rather than immune destruction. A SYK inhibitor is therefore not expected to address the underlying cause.

The high TxGNN score is a computational prediction. No trials or publications support it, so this should be treated as a research question rather than an actionable lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for this predicted indication.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02508052 | TAVALISSE | Not specified | Not specified |
| 02508060 | TAVALISSE | Not specified | Not specified |

---

## Safety Considerations

**Drug Interactions**: The interaction screening returned 100 potential interactions. The most notable are:
- **Major**: Clarithromycin
- **Moderate** (examples): proton pump inhibitors (omeprazole, rabeprazole, dexlansoprazole), cimetidine, corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), aprepitant, morphine, loperamide, pioglitazone, empagliflozin, alosetron, alvimopan, dolasetron, dronabinol, eliglustat

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or literature (evidence level L5). Most inherited thrombocytopenias involve impaired platelet production, not immune destruction, so the SYK-inhibition rationale is weak.

**To proceed, the following is needed:**
- Confirmation that the specific condition has an immune-mediated or SYK-dependent component
- Mechanism of action data and package insert warnings and contraindications from Health Canada
- Preclinical or case-level evidence of platelet benefit in inherited thrombocytopenia
- Approved indication text and dosage forms for the Canadian DINs

---

### Note on Other Predicted Indications

The other prediction, non-syndromic esophageal malformation (score 0.9905), also has no clinical trials and only L5 evidence. It has no identifiable mechanistic rationale and is likely a TxGNN model (deep learning) artifact.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

