---
layout: default
title: Alanine
parent: Model Prediction Only (L5)
nav_order: 29
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Alanine: predicted new indication Gastroparesis (evidence level L5). Approved use: Not stated in the Health Canada license data compiled for this report…"
---

# Alanine
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

# Alanine: From Parenteral Nutrition Amino Acid Component to Gastroparesis

## One-Sentence Summary

Alanine is a non-essential amino acid used in Canada as an ingredient of parenteral nutrition (intravenous feeding) products.
The TxGNN model predicts it may be useful for **gastroparesis**, but this is a model prediction only: **0 clinical trials** and **3 loosely related publications** (none showing that alanine treats the condition) are currently available.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Health Canada license data compiled for this report (marketed as an amino acid component of parenteral nutrition products) |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, alanine is a non-essential amino acid supplied in intravenous nutrition formulations (such as Clinimix, Travasol, Primene, Olimel and SmofKabiven). Its role there is nutritional and metabolic support, and no mechanism linking it to gastric motility has been documented.

The only plausible link is indirect. Gastroparesis is a common complication of diabetes and is also more frequent in chronic renal failure, and the retrieved literature concerns diabetic and renal-related gastrointestinal or hepatic complications. This is a comorbidity association. It is not evidence that alanine treats gastroparesis or changes gastric emptying. Any therapeutic role, such as nutritional support for patients with gastroparesis, is speculative and unsupported by the data compiled for this report.

The very high TxGNN score (99.37%) reflects knowledge-graph patterns, not experimental or clinical confirmation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10926110](https://pubmed.ncbi.nlm.nih.gov/10926110/) | 2000 | Review | Advances in Renal Replacement Therapy | Reviews gastrointestinal and hepatic disorders in end-stage renal disease and transplant recipients; notes gastroparesis is more common in chronic renal failure. Does not involve alanine. |
| [26315331](https://pubmed.ncbi.nlm.nih.gov/26315331/) | 2016 | Review | Diabetic Medicine | Describes diabetic hepatosclerosis as a possible microvascular complication of diabetes. Not directly related to gastroparesis or alanine. |
| [33763324](https://pubmed.ncbi.nlm.nih.gov/33763324/) | 2021 | Review (case report) | Cureus | Case of glycogen hepatopathy in a type 1 diabetic patient whose history included gastroparesis. Not related to alanine treatment. |

These publications mention gastroparesis only as a co-existing condition. None tests alanine for it.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02046709 | CLINIMIX | Not specified | Not specified |
| 02013932 | CLINIMIX | Not specified | Not specified |
| 02013940 | CLINIMIX | Not specified | Not specified |
| 00872296 | TRAVASOL | Not specified | Not specified |
| 02013886 | CLINIMIX | Not specified | Not specified |

Twenty valid single-ingredient licenses are on record in total; the table shows the first five. Other products include Clinimix E, Essepna, 20% Prosol, Primene 10%, Olimel 5.7% and 7.6%, and SmofKabiven (electrolyte-free and extra-nitrogen versions).

## Safety Considerations

- **Contraindications flagged by the knowledge graph (not label text):** The TxGNN knowledge graph links alanine with contraindication edges for several conditions. These are model-derived associations and should be checked against the product monographs.
  - Kidney conditions: kidney disease, chronic kidney disease, chronic renal failure syndrome, end-stage renal failure, acute urate nephropathy, nephrolithiasis, nephrocalcinosis
  - Calcium and phosphorus disorders: hypercalcemia, humoral hypercalcemia of malignancy, sarcoidosis, phosphorus metabolism disease
  - Cardiac conditions: heart disease, cardiovascular disease, ventricular fibrillation, digitalis poisoning
  - Phenylalanine metabolism disorders: phenylketonuria and related disorders
  - Other: pyoureter

Notably, kidney disease is among the flagged conditions, and gastroparesis in these patients often co-occurs with renal failure, so this overlap deserves attention.

Please refer to the package insert for label warnings and drug interaction information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. There are no registered clinical trials, no mechanistic rationale, and the retrieved literature does not examine alanine for gastroparesis. Product-label safety data are also missing.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism of action data for alanine, for example from DrugBank
- Targeted literature search for amino acid or nutritional interventions in gastroparesis
- Approved indication text, dosage forms and routes for the Canadian products
- Clarification of whether any plausible use (such as parenteral nutritional support in severe gastroparesis) differs from the existing approved use
- Review of the knowledge-graph contraindications, especially renal and cardiac conditions, against the product labels
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

