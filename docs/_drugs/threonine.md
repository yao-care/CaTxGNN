---
layout: default
title: Threonine
parent: Model Prediction Only (L5)
nav_order: 902
evidence_level: L5
indication_count: 1
---

# Threonine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Threonine: From Amino Acid Nutrition to Gastroparesis

## One-Sentence Summary

Threonine is an essential amino acid. In Canada it appears in parenteral nutrition amino acid products such as CLINIMIX and TRAVASOL.
The TxGNN model predicts it may be effective for **gastroparesis**.
This rests on the model score alone: **0 clinical trials** and **1 publication** are retrieved, and that publication does not test threonine.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication text on file (the products are amino acid nutrition products) |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L5 (model prediction only; the single paper is disease pathophysiology and does not test threonine) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and no original indications are recorded for threonine. Based on known information, threonine is an essential amino acid supplied as part of parenteral nutrition formulations. A mechanistic link to gastroparesis is plausible but unproven.

The one retrieved paper (PMID 28627597) studies gastric smooth muscle cell apoptosis and PI3K-AKT-mTOR and AMPK-mTOR signaling in a rat model of diabetic gastroparesis. It describes disease pathophysiology and does not evaluate threonine. mTOR signaling is amino-acid sensitive, which could connect threonine to this pathway. However, threonine is a much less characterized mTORC1 input than leucine or arginine. No evidence shows that threonine supplementation changes gastric smooth muscle signaling, gastric emptying, or symptoms.

The high score (0.993) comes from a knowledge-graph prediction with no drug-specific rationale behind it. Treat it as hypothesis-generating only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28627597](https://pubmed.ncbi.nlm.nih.gov/28627597/) | 2017 | Preclinical (rat model) | Molecular Medicine Reports | Examined dynamic changes in gastric smooth muscle cell apoptosis and in PI3K-AKT-mTOR and AMPK-mTOR signaling in diabetic gastroparesis rats. Threonine was not evaluated. |

---

## Canada Market Information

Dosage form and approved indication text are not recorded for these licenses. Showing 5 of 20.

| DIN | Product Name |
|---------|------|
| 02046709 | CLINIMIX |
| 02013932 | CLINIMIX |
| 02013940 | CLINIMIX |
| 00872296 | TRAVASOL |
| 02013886 | CLINIMIX |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a knowledge-graph score. There are no registered trials, and the single paper does not test threonine. No mechanism of action or original indication data exists to anchor the prediction. The Health Canada safety data gap is also blocking.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking)
- Mechanism of action data from DrugBank
- Direct evidence, preclinical or clinical, that threonine affects gastric motility or gastroparesis outcomes
- Route compatibility assessment: the marketed products are parenteral nutrition formulations, and the route for a gastroparesis use is undefined
- Approved indication text and dosage forms for the Canadian licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

