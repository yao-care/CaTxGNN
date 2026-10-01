---
layout: default
title: Rosuvastatin
parent: Model Prediction Only (L5)
nav_order: 818
evidence_level: L5
indication_count: 10
---

# Rosuvastatin
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

# Rosuvastatin: From Hyperlipidemia to Cholesterol-Ester Transfer Protein Deficiency

## One-Sentence Summary

Rosuvastatin is a statin (HMG-CoA reductase inhibitor) used to lower cholesterol in dyslipidemia.
The TxGNN model predicts it may be effective for **cholesterol-ester transfer protein (CETP) deficiency**,
but currently **0 clinical trials** and only **2 publications** (both case reports on related lipid disorders) touch on this direction, so the evidence is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperlipidemia / dyslipidemia (general statin use; the Canadian license records do not include indication text) |
| Predicted New Indication | Cholesterol-ester transfer protein deficiency |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L4 (indirect literature only; no study tests rosuvastatin in this condition) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, rosuvastatin inhibits HMG-CoA reductase, which lowers hepatic cholesterol synthesis, raises LDL receptor activity and lowers LDL cholesterol. Its efficacy in hyperlipidemia is well established.

CETP deficiency is also a lipid disorder, which may be why the model links the two. However, the mechanisms do not line up well. CETP deficiency mainly **raises HDL cholesterol** and is not a primary LDL-lowering target. Statins' LDL-lowering action therefore does not directly address the core abnormality.

The only two papers retrieved concern **other** rare lipid disorders (complete apoA-I deficiency and hepatic lipase deficiency). They do not test rosuvastatin in CETP deficiency. The high model score reflects a knowledge-graph association rather than demonstrated clinical benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21122686](https://pubmed.ncbi.nlm.nih.gov/21122686/) | 2010 | Case report / Review | J Clin Lipidol | Complete apoA-I deficiency in an Iraqi Mandaean family caused by a new APOA1 nonsense mutation. The two homozygotes presented very differently. Not about rosuvastatin or CETP deficiency. |
| [22798447](https://pubmed.ncbi.nlm.nih.gov/22798447/) | 2010 | Case report | BMJ Case Rep | Hepatic lipase deficiency in a young Middle-Eastern-Arabic male, with premature atherosclerosis despite high HDL-C. Reports CETP activity and mass in this setting. Not a treatment study. |

---

## Canada Market Information

Rosuvastatin has 20 licensed products in Canada. The first 5 are shown below. Dosage form and approved-indication text are not recorded in the supplied data.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02378531 | PMS-ROSUVASTATIN | Not listed | Not listed |
| 02413108 | MAR-ROSUVASTATIN | Not listed | Not listed |
| 02378566 | PMS-ROSUVASTATIN | Not listed | Not listed |
| 02536625 | NRA-ROSUVASTATIN TABLETS | Not listed | Not listed |
| 02337975 | APO-ROSUVASTATIN | Not listed | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information.

The drug-interaction query returned no records. This should be treated as missing data, not as evidence that no interactions exist.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no registered trials, and the two retrieved papers are case reports on different lipid disorders. The mechanism (LDL lowering) also does not match CETP deficiency, which mainly raises HDL.

**To proceed, the following is needed:**
- Clinical or case-series data on rosuvastatin (or any statin) in genetically confirmed CETP deficiency
- Evidence that LDL lowering gives a meaningful clinical benefit in this condition
- Health Canada product monograph warnings and contraindications
- Approved-indication text for the Canadian licenses, to confirm the original indication
- A complete drug-interaction review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

