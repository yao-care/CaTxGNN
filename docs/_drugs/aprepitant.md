---
layout: default
title: Aprepitant
parent: Model Prediction Only (L5)
nav_order: 68
evidence_level: L5
indication_count: 10
---

# Aprepitant
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

# Aprepitant: From an Approved Antiemetic Product to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Aprepitant is marketed in Canada under the EMEND brand. The approved indication text was not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis**.
No clinical trials and no relevant publications currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Aprepitant is known to be a substance P/NK1 receptor antagonist. Its approved indication text could not be retrieved, so its established use cannot be compared directly with the predicted indication.

Nephrogenic syndrome of inappropriate antidiuresis is caused by gain-of-function of the vasopressin V2 receptor. No established link exists between NK1 blockade and this pathway. NK1 signaling may modulate central fluid and osmoregulation, but this is speculative.

The high TxGNN score is therefore not backed by mechanistic or clinical support at this time. The prediction should be treated as a computational hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02298813 | EMEND TRI-PACK | Not listed | Not listed |
| 02298805 | EMEND | Not listed | Not listed |
| 02298791 | EMEND | Not listed | Not listed |

## Safety Considerations

- **Knowledge-graph contraindication signal**: The TxGNN knowledge graph links aprepitant to a contraindication with liver failure. This comes from graph data, not from product label text.
- **Drug Interactions**: 100 interactions were identified, and the first 20 returned are summarized here.
  - **Major**: fentanyl, alfentanil, acalabrutinib
  - **Moderate** (examples): paclitaxel, abemaciclib, rabeprazole, nifedipine, ibuprofen, levonorgestrel, hydrocortisone, albendazole, fluvoxamine, fosamprenavir, fosphenytoin, fostamatinib, gefitinib, lidocaine, dihydrocodeine, abametapir (topical)
  - **Minor**: dolutegravir

  Interaction levels come from the DDInter database. Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting clinical trials or relevant literature, and no plausible mechanistic link to the vasopressin V2 receptor pathway. The evidence level is L5. Package insert safety data and approved indication text are also missing.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indications from Health Canada
- Mechanism of action data from DrugBank, and an analysis of any link between NK1 signaling and renal water handling
- Preclinical or mechanistic studies testing NK1 antagonism in models of nephrogenic syndrome of inappropriate antidiuresis
- A review of the liver failure contraindication signal and the major drug interactions before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

