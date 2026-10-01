---
layout: default
title: Pantothenic Acid
parent: Model Prediction Only (L5)
nav_order: 699
evidence_level: L5
indication_count: 9
---

# Pantothenic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Pantothenic Acid: From Multivitamin Supplementation to Congenital Prothrombin Deficiency

## One-Sentence Summary

Pantothenic acid (vitamin B5) is marketed in Canada as a component of multivitamin products, including prenatal formulations.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, but this prediction has **1 loosely related clinical trial** and **no publications**, and no plausible biological link was found.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data (the products are multivitamin and prenatal vitamin formulations) |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Pantothenic acid is the precursor of coenzyme A (CoA), which is central to energy and lipid metabolism. It is supplied in multivitamin products to prevent or correct nutritional deficiency.

Congenital prothrombin deficiency is an inherited bleeding disorder caused by a lack of functional prothrombin (factor II). Pantothenic acid has no known role in prothrombin synthesis or in vitamin K-dependent carboxylation, so the original use and the predicted use are not biologically connected.

The high TxGNN score therefore looks like an artifact of the knowledge graph rather than a real biological signal. This prediction should not be treated as a credible repurposing lead.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02392767](https://clinicaltrials.gov/study/NCT02392767) | N/A | Completed | 25 | Randomised, double-blind, placebo-controlled cross-over study of a multi-ingredient supplement (L-arginine, Pycnogenol, vitamin K2, alpha-lipoic acid, vitamins B6, B12 and folic acid) on endothelial function in mild-to-moderate hypertension. It does not involve a coagulation disorder or prothrombin deficiency (relevance grade C). |

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 586315 | MULTI 1000 |
| 2552639 | PREGVIT FOLIC 5 |
| 2535718 | PREGNANCY MULTIVITAMIN |
| 2552620 | PREGVIT |
| 2537478 | PREGNANCY MULTIVITAMIN FOLIC 5 |

Dosage form, manufacturer and approved indication text are not listed in the licence data.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. No mechanism links pantothenic acid to prothrombin deficiency, and the single trial found tests an unrelated multi-ingredient supplement in hypertension. Evidence is at L5.

**To proceed, the following is needed:**
- Health Canada product monograph warnings and contraindications for the marketed products
- Mechanism of action data (for example from DrugBank)
- A clear original-indication statement from the Canadian licence records
- A separate review of the other predicted indications. **Folic acid deficiency anemia** (rank 4) is the most plausible one: it has an L4 mechanistic rationale and a favourable safety profile, but the supporting trials are multi-micronutrient studies that cannot isolate the effect of pantothenic acid. **Uterine inflammatory disease** (rank 5) has only mouse-model evidence.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

