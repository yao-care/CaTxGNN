---
layout: default
title: Eculizumab
parent: 僅模型預測 (L5)
nav_order: 248
evidence_level: L5
indication_count: 10
---

# Eculizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Eculizumab: From Complement-Mediated Rare Diseases to Cyclic Hematopoiesis

## One-Sentence Summary

Eculizumab is a humanized monoclonal antibody that blocks complement protein C5, with established use in complement-driven rare diseases such as paroxysmal nocturnal hemoglobinuria (PNH) and atypical hemolytic uremic syndrome (aHUS); however, no Canadian regulatory record is available in this Evidence Pack.
The TxGNN model predicts it may be effective for **Cyclic Hematopoiesis**, placing it at rank 1 among all predicted new indications with a score of **99.97%**.
Despite the high model confidence, **no clinical trials and no supporting literature** have been identified for this specific drug–disease pair, yielding an evidence level of **L5** (model prediction only).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no Canadian DIN on file) |
| Predicted New Indication | Cyclic Hematopoiesis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known published information, Eculizumab (Soliris®) is a complement C5 inhibitor that prevents cleavage of C5 into the pro-inflammatory anaphylatoxin C5a and the membrane attack complex initiator C5b-9. By halting the terminal complement cascade, it has proven efficacy in diseases where uncontrolled complement activation is the primary driver of tissue injury — most notably PNH and atypical HUS, as reflected in the indirect literature found for related indications in this pack (e.g., PMID 25237200, 19179329, 39543505).

Cyclic hematopoiesis (cyclic neutropenia) is caused predominantly by autosomal dominant mutations in the *ELANE* gene encoding neutrophil elastase, or less commonly *HAX1*, resulting in approximately 21-day oscillations in circulating neutrophil counts due to periodic accelerated apoptosis of myeloid progenitor cells in the bone marrow. The underlying disease mechanism is intrinsic to the granulopoietic compartment — driven by proteotoxic stress and endoplasmic reticulum dysfunction — and is largely independent of the terminal complement pathway.

The mechanistic link between C5 inhibition and cyclic hematopoiesis is therefore highly speculative. While complement-driven inflammation could theoretically amplify bone marrow damage during neutrophil nadir periods, there is no established evidence that C5a or the membrane attack complex drives the oscillatory granulopoiesis cycle itself. The TxGNN model's high ranking most likely reflects graph-level proximity in the knowledge graph (e.g., shared rare hematological disease nodes) rather than a direct and actionable biological mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Eculizumab in cyclic hematopoiesis.

---

## Literature Evidence

Currently no related literature available for Eculizumab in cyclic hematopoiesis.

---

## Canada Market Information

Eculizumab currently has no Drug Identification Numbers (DINs) on file and is not marketed in Canada per the data available in this Evidence Pack. No approved indication text can be extracted.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns an extremely high prediction score (99.97%), this confidence is entirely unsupported by clinical or preclinical evidence — no trials, no literature, and no mechanistic studies link complement C5 inhibition to the ELANE/HAX1-driven oscillatory granulopoiesis that defines cyclic hematopoiesis. A high model score in the absence of any biological plausibility warrants a full stop pending further investigation.

**To proceed, the following is needed:**
- Preclinical mechanistic studies demonstrating that complement pathway activation (specifically C5a or C5b-9) contributes to cyclic bone marrow progenitor apoptosis in ELANE-mutant or HAX1-mutant animal models
- Molecular data linking the terminal complement cascade to oscillatory granulopoiesis rather than downstream inflammatory amplification
- Complete MOA documentation for Eculizumab (currently a Data Gap), including receptor binding profile and downstream pathway effects
- Full safety profile including key warnings, contraindications, and drug–drug interactions (all currently Data Gap)
- Assessment of the Canadian rare disease/orphan drug regulatory pathway for any potential future application
- Clarification of whether Eculizumab's established pharmacological bridging (complement-mediated hematologic damage in PNH/aHUS) offers any transferable rationale to bone marrow failure phenotypes — even if indirect

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

