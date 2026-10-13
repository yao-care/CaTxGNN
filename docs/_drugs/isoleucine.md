---
layout: default
title: Isoleucine
parent: Model Prediction Only (L5)
nav_order: 499
evidence_level: L5
indication_count: 1
---

# Isoleucine
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

# Isoleucine: From Parenteral Nutrition Amino Acid Supplementation to Gastroparesis

## One-Sentence Summary

Isoleucine is an essential branched-chain amino acid, marketed in Canada as a component of parenteral nutrition (amino acid infusion) products.
The TxGNN model predicts it may be effective for **gastroparesis**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on computation alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (no approved indication text is recorded for the Canadian licences) |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, isoleucine is a branched-chain amino acid that takes part in protein synthesis, energy metabolism and glucose uptake. It is supplied in Canada as a component of multi-amino-acid parenteral nutrition products, where its role is nutritional support rather than treating a specific disease.

No mechanistic link to gastroparesis can be established from the data compiled for this report. The high TxGNN score (0.993) comes from knowledge-graph embeddings only. Any connection through nutritional status, glycaemic control or enteric smooth-muscle metabolism is speculative. Amino-acid-rich meals can also influence gastric emptying, so the effect in gastroparesis could be neutral or even harmful.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

All 20 licences are valid single-ingredient authorisations. Dosage form and approved indication text are not recorded for them. The five main ones are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02046709 | CLINIMIX | Not recorded | Not recorded |
| 00872296 | TRAVASOL | Not recorded | Not recorded |
| 02510324 | ESSEPNA | Not recorded | Not recorded |
| 02236875 | PRIMENE 10% | Not recorded | Not recorded |
| 02477947 | OLIMEL 7.6% | Not recorded | Not recorded |

Other licensed products include further CLINIMIX and CLINIMIX E strengths, 20% PROSOL, OLIMEL 5.7%, and SMOFKABIVEN (electrolyte free and extra nitrogen electrolyte free).

## Safety Considerations

- **Knowledge-graph contraindication signals** (from TxGNN/PrimeKG drug-disease edges, not label text):
  - Renal: kidney disease, chronic kidney disease, chronic renal failure syndrome, end stage renal failure, acute urate nephropathy, nephrolithiasis, nephrocalcinosis
  - Calcium and phosphorus disorders: hypercalcemia, humoral hypercalcemia of malignancy, sarcoidosis, phosphorus metabolism disease
  - Cardiac: heart disease, cardiovascular disease, ventricular fibrillation, digitalis poisoning
  - Metabolic: phenylketonuria, disorder of phenylalanine metabolism
  - Other: pyoureter

Package insert warnings, contraindications and drug interaction data are not available. Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only a computational score. There are no clinical trials or publications, no mechanism data, and no mechanistic link to gastroparesis. Isoleucine is also used only as part of nutrition products in Canada, and the knowledge graph flags several relevant contraindications (renal and cardiac disease among them).

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank, to assess any link to gastric motility
- Confirmed approved indications and dosage forms for the Canadian licences
- Literature and trial searches on branched-chain amino acids and gastric emptying or gastroparesis
- Route compatibility assessment, since current products are parenteral nutrition formulations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

