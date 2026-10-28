---
layout: default
title: L-Lysine
parent: Model Prediction Only (L5)
nav_order: 514
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "L-Lysine: predicted new indication gastroparesis (disease) (evidence level L5). Approved use: Not specified in the available licence data (the products are amino a…"
monitor_inn: "L-LYSINE"
predicted_indications: ["gastroparesis (disease)", "congenital prothrombin deficiency", "obsolete vitamin D deficiency"]
---

# L-Lysine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## L-Lysine: From Parenteral Nutrition Amino Acid Component to gastroparesis (disease)
{: .text-alpha }

## One-Sentence Summary

L-lysine is an essential amino acid used in Canada as a component of parenteral nutrition (amino acid infusion) products.
The TxGNN model predicts it may be relevant for **gastroparesis**, but there are **0 clinical trials** and only **1 loosely related publication** (a preclinical stem-cell study that does not involve L-lysine), so this is essentially a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available licence data (the products are amino acid / parenteral nutrition formulations) |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 0.9977 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses on record: at least 20) |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, L-lysine is an essential amino acid that the body uses for protein synthesis, calcium absorption, and carnitine production. In Canada it is marketed only within amino acid and parenteral nutrition products.

The data compiled for this report show no established link between these functions and gastric motility or gastric emptying. Gastroparesis involves loss of interstitial cells of Cajal and enteric neurons, which is not a process L-lysine is known to address. The high score (0.9977) is a computational prediction and is not backed by clinical or mechanistic data.

The other two predictions are also weak:
- **Congenital prothrombin deficiency** (score 0.9913): a genetic coagulation disorder that dietary lysine would not be expected to correct. Lysine analogues such as tranexamic acid act as antifibrinolytics, but that does not extend to L-lysine itself.
- **Vitamin D deficiency** (score 0.9902): the disease term is obsolete in the ontology, and L-lysine's modest effect on calcium handling does not replace vitamin D.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29414870](https://pubmed.ncbi.nlm.nih.gov/29414870/) | 2018 | Preclinical | Bioengineering (Basel) | Mesenchymal stem cells delivered from gelatin-alginate hydrogels to the stomach lumen as a potential gastroparesis therapy. The study does not test L-lysine. |

## Canada Market Information

All 20 licences are valid single-ingredient products. Dosage form and approved indication text are not available in the data compiled for this report. The five shown are the first five listed.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02046709 | CLINIMIX | Not available | Not available |
| 02013932 | CLINIMIX | Not available | Not available |
| 02013940 | CLINIMIX | Not available | Not available |
| 00872296 | TRAVASOL | Not available | Not available |
| 02013886 | CLINIMIX | Not available | Not available |

Other marketed products include CLINIMIX E, PRIMENE 10%, OLIMEL, SMOFKABIVEN, 20% PROSOL, and ESSEPNA.

## Safety Considerations

- **Disease associations from the knowledge graph (not label text):** The TxGNN knowledge graph links L-lysine to contraindication relationships with several conditions. These should be verified against the product labelling:
  - Kidney: kidney disease, chronic kidney disease, chronic renal failure, end-stage renal failure, acute urate nephropathy, nephrolithiasis, nephrocalcinosis
  - Calcium and phosphorus: hypercalcemia, humoral hypercalcemia of malignancy, sarcoidosis, phosphorus metabolism disease
  - Cardiac: heart disease, cardiovascular disease, digitalis poisoning, ventricular fibrillation
  - Metabolic: phenylketonuria and other disorders of phenylalanine metabolism
- **Drug interactions:** No interaction records were found.

Please refer to the package insert for authoritative warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (TxGNN model, deep learning; gastroparesis 0.9977), which may reflect similarities the model learned between related diseases, not biological evidence. There are no clinical trials, the only publication is an unrelated preclinical study, and no mechanistic link to gastroparesis is supported. Kidney, cardiac, and calcium-related conditions are also flagged as potential concerns.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank to assess any link to gastric motility
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text and dosage forms for the Canadian products
- Targeted literature search for L-lysine and gastric emptying or gastroparesis
- Route compatibility assessment, since current products are parenteral nutrition formulations
- Mapping the obsolete vitamin D deficiency term to a current ontology term if that prediction is to be pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

