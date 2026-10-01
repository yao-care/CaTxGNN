---
layout: default
title: Butamben
parent: Model Prediction Only (L5)
nav_order: 138
evidence_level: L5
indication_count: 10
---

# Butamben
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

# Butamben: From Topical Local Anesthesia to Bronchitis

## One-Sentence Summary

Butamben is a topical ester local anesthetic, marketed in Canada as a component of CETACAINE LIQUID. The TxGNN model predicts it may be effective for **bronchitis**, but this rests on the model score alone: there are **0 clinical trials** and **0 publications** supporting the direction. It is a model-only signal, and the recommendation is to hold.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license record (butamben is a topical local anesthetic) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacology, butamben is a topical ester local anesthetic that blocks voltage-gated sodium channels. Topical airway anesthesia could plausibly suppress the cough reflex.

This link is weak. Suppressing a reflex only relieves a symptom and does not treat bronchitis itself, which is an inflammatory or infectious airway disease. Butamben is also poorly water-soluble and used only topically, which limits any respiratory application. The high TxGNN score (99.79%) most likely reflects proximity in the knowledge graph rather than a demonstrated mechanism.

The nine other predictions for this drug show the same pattern. They include severe nonproliferative diabetic retinopathy, acrodermatitis chronica atrophicans, neonatal dermatomyositis, cauda equina syndrome and diabetic retinopathy. All have scores of 99.1–99.8%, no trials or literature, and no credible mechanistic link. The two diabetic retinopathy entries are related subtypes, so their scores reflect one repeated graph signal, not independent support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2028867 | CETACAINE LIQUID | Not listed | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found for butamben.

The following concern comes from the prediction rationale, not from a package insert. Local anesthetics of the para-aminobenzoate ester class carry risks of methemoglobinemia and hypersensitivity, which would matter in any pediatric use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction is supported only by the TxGNN score (Evidence Level L5). No trials or publications exist, and the plausible mechanism (cough suppression) would relieve a symptom without treating the disease. Butamben's topical-only use and poor water solubility further limit any respiratory application.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence linking butamben to airway inflammation or bronchitis
- An assessment of whether an airway-compatible route or formulation exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

