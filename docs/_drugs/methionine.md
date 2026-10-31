---
layout: default
title: Methionine
parent: Model Prediction Only (L5)
nav_order: 598
evidence_level: L5
indication_count: 10
monitor_inn: "Methionine"
predicted_indications: ["acne (disease)", "severe nonproliferative diabetic retinopathy", "diabetes mellitus type 2 associated cataract", "nuclear senile cataract", "craniostenosis cataract", "immature cataract", "cortical cataract", "mature cataract", "tetanic cataract", "diabetic cataract"]
last_modified_at: 2026-10-31
description: "Methionine: predicted new indication Acne (disease) (evidence level L5). Approved use: Not available"
---

# Methionine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Methionine: From Parenteral Nutrition Amino Acid Component to Acne (Disease)
{: .text-alpha }

## One-Sentence Summary

Methionine is an essential amino acid that appears in Canada as an ingredient in parenteral nutrition amino acid products (for example CLINIMIX and TRAVASOL).
The TxGNN model predicts it may be useful for **acne (disease)**, but there are **no registered clinical trials** and only **2 indirect publications** (a cohort study and a case report), and neither tests methionine as a treatment.
This prediction is best viewed as a model-generated hypothesis rather than an evidence-supported treatment direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the Canadian licence records compiled for this report contain no indication text) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses on record: at least 20) |
| Number of DINs | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for methionine are not available in the data compiled for this report. Based on known information, methionine is a sulfur-containing essential amino acid and a precursor in the methionine and homocysteine cycle. It is supplied in Canada within amino acid solutions for parenteral nutrition.

The link to acne is weak. The two retrieved papers are indirect. One reports raised plasma homocysteine (a methionine-cycle metabolite) in patients taking isotretinoin for cystic acne. That is a drug-associated biochemical change, not a therapeutic effect. The other is a neonatal case report of an MTHFR mutation, with neonatal acne among many features, and it is not relevant to treating acne. Because methionine supplementation could raise homocysteine, the available signal points more toward a possible safety concern than a benefit.

Because no cited study directly examines methionine for acne, the evidence level is L5 (model prediction only).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11277950](https://pubmed.ncbi.nlm.nih.gov/11277950/) | 2001 | Cohort | International Journal of Dermatology | Plasma homocysteine was elevated in patients on isotretinoin for cystic acne; a drug-related biochemical change, not a methionine treatment study |
| [39357918](https://pubmed.ncbi.nlm.nih.gov/39357918/) | 2024 | Case report | BMJ Case Reports | Neonate with a novel MTHFR mutation, encephalopathy, hair loss and marfanoid features (neonatal acne among the skin findings); not related to acne therapy |

## Canada Market Information

Methionine is marketed in Canada, with at least 20 valid licences in the records compiled (the list may be partial). None of the records includes indication text, dosage form or manufacturer. Main products listed:

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02046709 | CLINIMIX | Not recorded | Not recorded |
| 02013932 | CLINIMIX | Not recorded | Not recorded |
| 00872296 | TRAVASOL | Not recorded | Not recorded |
| 02510324 | ESSEPNA | Not recorded | Not recorded |
| 02236875 | PRIMENE 10% | Not recorded | Not recorded |

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** The TxGNN knowledge graph records contraindication relations between methionine and conditions including hypertension, kidney disease (chronic kidney disease, end-stage renal failure), diabetes mellitus and diabetic ketoacidosis, hypercalcemia, heart disease and cardiovascular disease, hyperlipidemia, nephrolithiasis, phenylketonuria and other disorders of phenylalanine metabolism, digitalis poisoning, ventricular fibrillation, sarcoidosis and nephrocalcinosis. These come from the graph and have not been confirmed against Canadian label text.
- **Drug Interactions (5 recorded):**
  - Moderate: activated charcoal
  - Minor: ephedrine, pseudoephedrine, mexiletine, flecainide
- **Homocysteine:** The retrieved literature links elevated homocysteine with vascular and ocular disease, so methionine supplementation for a non-nutritional purpose would need careful safety consideration.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but it is not backed by any clinical trial or any study of methionine in acne. The only retrieved papers are indirect and, if anything, suggest a homocysteine-related safety concern.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada
- Mechanism-of-action data for methionine
- Direct preclinical or clinical evidence that methionine affects acne
- Assessment of homocysteine-related risk with supplementation
- Confirmation of the Canadian approved indications and dosage forms, since the licence records contain no indication text

---

### Other Predicted Indications (for reference)

Other predictions are mostly eye conditions. All are on Hold except diabetic cataract, which is flagged as a research question.

| Predicted Indication | Evidence Level | Note |
|------|------|------|
| Diabetic cataract | L4 | Most mechanistically coherent. Preclinical studies of methionine sulfoxide reductase B1 (lens cell protection against high-glucose and peroxynitrite damage) concern the repair enzyme, not methionine supplementation. No clinical trials. |
| Nuclear senile cataract, cortical cataract, mature cataract | L4 | Indirect literature on lens protein oxidation and models only; no methionine intervention data |
| Severe nonproliferative diabetic retinopathy, type 2 diabetes-associated cataract, craniostenosis cataract, immature cataract, tetanic cataract | L5 | Prediction only, no trials or literature |

Note: the L4 levels above come from the data compiled for this report, but the cited studies address related lens mechanisms rather than methionine treatment of these diseases directly, so they should be read cautiously.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

