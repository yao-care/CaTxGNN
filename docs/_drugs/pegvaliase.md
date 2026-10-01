---
layout: default
title: Pegvaliase
parent: Model Prediction Only (L5)
nav_order: 709
evidence_level: L5
indication_count: 10
---

# Pegvaliase
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

# Pegvaliase: From Phenylketonuria to Diabetic Retinopathy

## One-Sentence Summary

Pegvaliase is a PEGylated phenylalanine ammonia lyase, marketed in Canada as PALYNZIQ and approved for phenylketonuria (PKU).
The TxGNN model predicts it may be effective for **diabetic retinopathy** (score 99.2%), but **no clinical trials and no publications** currently support this direction. It is a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Phenylketonuria (taken from the prediction rationale, because the license records contain no indication text) |
| Predicted New Indication | Diabetic retinopathy |
| TxGNN Prediction Score | 99.17% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Pegvaliase is a PEGylated enzyme that breaks down phenylalanine, and its efficacy in PKU is the basis of its approval. No established mechanism connects it to diabetic retinopathy.

Any link would be speculative. One hypothesis is that changes in phenylalanine metabolism affect retinal vascular or metabolic stress. The prediction rests on the graph score alone, with no supporting trials or literature.

The other nine top predictions are also weak:
- **Severe nonproliferative diabetic retinopathy** is a sub-stage of the same disease, so it is not independent evidence.
- **Seven cataract subtypes** (nuclear senile, cortical, mature, tetanic, immature, craniostenosis, and type 2 diabetes-associated) have identical or near-identical scores of about 0.990. This points to a shared graph-neighborhood artifact rather than disease-specific signals.
- **Diabetic cataract** involves polyol pathway and osmotic lens injury, which pegvaliase's enzyme activity does not obviously address.

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
| 2526263 | PALYNZIQ |
| 2526247 | PALYNZIQ |
| 2526255 | PALYNZIQ |

Dosage form and approved indication text are not recorded for these licenses.

---

## Safety Considerations

Please refer to the package insert for safety information.

The prediction rationale notes that pegvaliase is a biologic with immunogenicity and anaphylaxis risk (a boxed warning). Any ocular benefit would have to be weighed against this risk.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predicted indications are Evidence Level L5, supported only by graph scores. There are no trials or publications, and no plausible mechanism has been demonstrated. The anaphylaxis risk of this biologic raises the bar for any new use.

**To proceed, the following is needed:**
- Mechanism of action data, to assess whether phenylalanine metabolism plausibly relates to retinal or lens disease
- Health Canada package insert warnings and contraindications
- Dosage form and approved indication text for the three licenses
- Preclinical or literature evidence for diabetic retinopathy, such as retinal models of phenylalanine metabolism
- Route compatibility and similarity-to-original-indication assessments (both still pending)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

