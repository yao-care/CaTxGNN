---
layout: default
title: Threonine
parent: Model Prediction Only (L5)
nav_order: 909
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Threonine: predicted new indication Gastroparesis (evidence level L5). Approved use: Not stated in the licence records compiled for this report (products…"
monitor_inn: "THREONINE"
predicted_indications: ["gastroparesis (disease)"]
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

# Threonine: From Parenteral Nutrition Amino Acid Supplementation to Gastroparesis

## One-Sentence Summary

Threonine is an essential amino acid used as a component of parenteral nutrition (intravenous feeding) products in Canada.
The TxGNN model predicts it may be effective for **gastroparesis**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so it is a computational prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records compiled for this report (products are amino acid parenteral nutrition formulations) |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, threonine is an essential amino acid that the body cannot make itself. It is used in protein synthesis and in the production of mucins, the main components of the protective intestinal mucus layer. It is supplied in Canada as a component of multi-amino-acid parenteral nutrition products (for example CLINIMIX, TRAVASOL, PRIMENE, OLIMEL and SMOFKABIVEN).

The link between this nutritional role and gastroparesis (delayed stomach emptying) is not established by the data compiled for this report. Gastroparesis is generally driven by problems such as loss of pacemaker cells in the stomach, damage to enteric nerves, or vagal and diabetic autonomic dysfunction. Any role for threonine in these processes would be speculative. The only support at present is the high TxGNN score of 99.32%, which comes from knowledge-graph pattern matching rather than direct biological or clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Threonine is marketed in Canada with 20 valid single-ingredient authorisations. Dosage form, manufacturer and approved indication text were not available in the licence records. The main authorisations are:

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02046709 | CLINIMIX | Not available | Not available |
| 02013932 | CLINIMIX | Not available | Not available |
| 00872296 | TRAVASOL | Not available | Not available |
| 02236875 | PRIMENE 10% | Not available | Not available |
| 02477947 | OLIMEL 7.6% | Not available | Not available |

The remaining 15 authorisations include further CLINIMIX and CLINIMIX E strengths, 20% PROSOL, ESSEPNA, OLIMEL 5.7%, and SMOFKABIVEN (electrolyte free and extra nitrogen electrolyte free).

---

## Safety Considerations

- **Disease-related contraindication signals (knowledge graph, not label text)**: The TxGNN knowledge graph links threonine to contraindication for **phenylketonuria** and **disorders of phenylalanine metabolism**. These signals come from computational data and should be checked against the official product labelling.
- **Drug Interactions**: No interactions were found in the queried data.

Please refer to the package insert for full warnings and contraindications, as label-based safety data was not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high model score (Evidence Level L5). There are no clinical trials, no publications, and no established mechanistic link between threonine and gastroparesis. Label safety information is also missing, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (download and review the product monographs)
- Mechanism of action data (for example from DrugBank)
- A literature and trial search for threonine and gastric motility or gastroparesis, including preclinical studies
- Assessment of route compatibility: the Canadian products are parenteral nutrition formulations, and whether a route suitable for gastroparesis exists is undetermined
- Approved indication text and dosage forms for the Canadian authorisations, to define the original indication clearly
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

