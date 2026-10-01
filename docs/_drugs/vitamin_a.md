---
layout: default
title: Vitamin A
parent: Model Prediction Only (L5)
nav_order: 973
evidence_level: L5
indication_count: 10
---

# Vitamin A
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

# Vitamin A: From Nutritional Supplementation (Multivitamin Products) to Congenital Prothrombin Deficiency

## One-Sentence Summary

Vitamin A is marketed in Canada as a component of multivitamin products (MULTI 1000, MULTI 12, MULTI-12/K1 PEDIATRIC). The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, with a very high score of 99.97%. Five retrieved clinical trials and **no publications** support this prediction, and none of the trials tests Vitamin A, so this is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license records (marketed in multivitamin products) |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Vitamin A is a fat-soluble vitamin supplied in multivitamin products. Its role in nutritional supplementation is established, but a mechanistic link to congenital prothrombin deficiency has not been shown.

The biology does not support the prediction well. Prothrombin (factor II) synthesis depends on vitamin K-dependent gamma-carboxylation, not on Vitamin A. Congenital prothrombin deficiency is an inherited coagulation disorder, so there is no obvious pathway through which Vitamin A would correct it. The 99.97% score reflects graph-based association, probably through shared vitamin and coagulation-related nodes in the knowledge graph. It is not clinical or literature evidence, so it should be treated as a hypothesis only.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04384341](https://clinicaltrials.gov/study/NCT04384341) | N/A | Recruiting | 480 | Observational study of bone loss in haemophilia (factor VIII/IX deficiency). No Vitamin A intervention and not about prothrombin. |
| [NCT03534752](https://clinicaltrials.gov/study/NCT03534752) | N/A | Completed | 220 | Retrospective descriptive study of adults with inborn errors of metabolism in French-speaking Switzerland. No Vitamin A intervention. |
| [NCT00168077](https://clinicaltrials.gov/study/NCT00168077) | Phase 3 | Completed | 40 | Beriplex P/N (prothrombin complex concentrate) for acquired deficiency of factors II, VII, IX and X due to oral anticoagulation. Relevant to prothrombin, but does not test Vitamin A. |
| [NCT00562783](https://clinicaltrials.gov/study/NCT00562783) | Phase 2 | Completed | 90 | Randomized controlled study of Vitalliver in decompensated cirrhosis. No Vitamin A intervention or prothrombin-deficiency population is evident, and manual verification is needed. |
| [NCT02392767](https://clinicaltrials.gov/study/NCT02392767) | N/A | Completed | 25 | Dietary supplement (L-arginine, Pycnogenol, vitamin K2, B vitamins) on endothelial function in hypertension. Unrelated population. |

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 586315 | MULTI 1000 |
| 2100606 | MULTI 12 |
| 2242529 | MULTI-12/K1 PEDIATRIC |

Dosage form and approved indication text are not recorded for these licenses.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the model score. None of the retrieved trials tests Vitamin A, there is no supporting literature, and the known biology (vitamin K-dependent prothrombin synthesis) points away from Vitamin A. The evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data for Vitamin A, plus any evidence linking retinoid signaling to prothrombin synthesis or coagulation
- Health Canada package insert warnings and contraindications, which are currently missing
- Targeted literature and trial searches for Vitamin A in congenital coagulation factor deficiencies
- Manual verification of NCT00562783 (Vitalliver), whose intervention is unclear
- A review of other predicted indications for this drug. For example, "perinatal disease" has an L2 signal from Cochrane reviews of Vitamin A in very low birth weight infants (bronchopulmonary dysplasia), and "injury" and "radiation or chemically induced disorder" also have more supporting evidence than this indication.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

