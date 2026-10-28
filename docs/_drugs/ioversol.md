---
layout: default
title: Ioversol
parent: Model Prediction Only (L5)
nav_order: 492
evidence_level: L5
indication_count: 9
monitor_inn: "Ioversol"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis", "brachyolmia", "hemoglobinopathy", "brachyolmia-amelogenesis imperfecta syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "myosclerosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "alopecia"]
last_modified_at: 2026-10-28
description: "Ioversol: predicted new indication Osteoarthritis (evidence level L5). Approved use: Not available"
---

# Ioversol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Ioversol: From an Iodinated Contrast Agent (No Labelled Indication on File) to Osteoarthritis
{: .text-alpha }

## One-Sentence Summary

Ioversol is an iodinated contrast agent marketed in Canada under the brand name OPTIRAY, but the data compiled for this report contain no approved-indication text for it.
The TxGNN model predicts it may be effective for **osteoarthritis**, but **no clinical trials** and **no publication that studies ioversol itself in this disease** support the prediction.
The one linked paper studies an embolization procedure with a different agent, so this is essentially a computational prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no indication text in the Canadian licence records) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 0.9963 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 2 of 2) |
| Number of DINs | 2 (valid: 2) |
| Number of approvals | 2 (both single-ingredient products) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Ioversol is an iodinated contrast agent, a class used to enhance imaging rather than to treat disease. It has no known pharmacological anti-osteoarthritis activity.

The only linked publication (PMID 38102013, the LipioJoint-1 trial) studied genicular artery embolization for knee osteoarthritis using an ethiodized oil emulsion (Lipiodol). That paper does not study ioversol as a treatment. Contrast agents such as ioversol may be used incidentally to guide angiography during such procedures, so the link is procedural and indirect.

The high TxGNN score is a computational prediction without a supporting mechanism. It should not be read as evidence of efficacy.

Because no cited study directly examines ioversol in osteoarthritis, the evidence level is L5. The earlier internal label of L4 is not supported.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38102013](https://pubmed.ncbi.nlm.nih.gov/38102013/) | 2024 | Single-arm clinical trial | Diagnostic and Interventional Imaging | Evaluated safety and efficacy of transient genicular artery embolization using an ethiodized oil emulsion for knee osteoarthritis. Ioversol was not the studied agent. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 01900854 | OPTIRAY 320 | Not listed | Not listed |
| 02035626 | OPTIRAY 320 (ULTRAJECT) | Not listed | Not listed |

Both records are single-ingredient products with valid status.

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 records; the main ones are listed below. Most are rated Major.
  - **Major**: metformin, amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms), mesalazine, balsalazide, olsalazine, sulfasalazine, vancomycin, kanamycin, neomycin, streptomycin and polymyxin B
  - **Moderate**: mannitol
  - **Unknown severity**: atropine, famotidine, acetylsalicylic acid, morphine, omeprazole

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. The only linked study used a different agent (ethiodized oil) in an embolization procedure, and ioversol has no known anti-osteoarthritis mechanism.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications and approved indication text, which are currently missing and block safety screening
- Mechanism of action data from DrugBank
- Any study that directly tests ioversol in osteoarthritis, or a plausible mechanistic rationale
- A review of the many Major-level drug interactions before any new use is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

