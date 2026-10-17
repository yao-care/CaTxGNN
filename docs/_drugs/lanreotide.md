---
layout: default
title: Lanreotide
parent: Model Prediction Only (L5)
nav_order: 523
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Lanreotide: predicted new indication Hypertrichosis (evidence level L5). Approved use: Acromegaly"
monitor_inn: "LANREOTIDE"
predicted_indications: ["hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "Ambras type hypertrichosis universalis congenita"]
---

# Lanreotide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Lanreotide: From Acromegaly to Hypertrichosis

## One-Sentence Summary

Lanreotide is a somatostatin analogue originally used to treat acromegaly, hyperpituitarism and pituitary gigantism.
The TxGNN model predicts it may be effective for **Hypertrichosis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acromegaly (also hyperpituitarism and pituitary gigantism, based on the knowledge graph) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, lanreotide is a somatostatin analogue that acts mainly through somatostatin receptors SSTR2 and SSTR5 to suppress growth hormone (GH) and IGF-1 secretion. Its efficacy in acromegaly is established.

The link to hypertrichosis is weak. Hypertrichosis is not a recognized GH/IGF-1-driven condition. Acromegaly can cause excess hair growth as a secondary feature, but that is an indirect association and not evidence that lanreotide would benefit hypertrichosis. The high TxGNN score is a graph-based computational prediction and is probably driven by similarity to other related phenotypes. No trial or literature record supports it.

Other top-ranked predictions are also unsupported by any trial or publication, and none has a plausible mechanistic rationale:
- Malformation syndrome with odontal and/or periodontal component (99.96%)
- Syndrome with a Dandy-Walker malformation as major feature (99.96%)
- Isolated genetic hair shaft abnormality (99.96%)
- Ambras type hypertrichosis universalis congenita (99.96%)

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02555867 | MYTOLAC | Not specified | Not specified |
| 02283395 | SOMATULINE AUTOGEL | Not specified | Not specified |
| 02283417 | SOMATULINE AUTOGEL | Not specified | Not specified |
| 02555883 | MYTOLAC | Not specified | Not specified |
| 02283409 | SOMATULINE AUTOGEL | Not specified | Not specified |

A sixth authorization (DIN 02555875, MYTOLAC) is also valid. All six are single-ingredient products and none is cancelled.

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

- **Conditions flagged in the knowledge graph (not label text)**: The knowledge graph links lanreotide to the following conditions as potential contraindications or cautions: hypertension and hypertensive disorder, liver disease, gallbladder disease, cholelithiasis, cholecystolithiasis, choledocholithiasis, hyperglycemia, hypoglycemia, hypothyroidism (including myxedema and congenital hypothyroidism), and impaired renal function. These should be verified against the official label.
- **Drug Interactions**: 100 interactions were identified, and the 20 shown are all rated Moderate. They are mainly glucose-lowering agents, which is consistent with lanreotide's effects on blood glucose.
  - Antidiabetic agents: acarbose, metformin, pioglitazone, glimepiride, chlorpropamide
  - DPP-4 inhibitors: alogliptin, linagliptin
  - SGLT2 inhibitors: canagliflozin, dapagliflozin, empagliflozin
  - GLP-1 receptor agonists: albiglutide, dulaglutide, semaglutide
  - Insulins: aspart, degludec, detemir, glargine, glulisine, isophane human, regular human

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting clinical trials or publications (Evidence Level L5). No plausible mechanistic link to hypertrichosis has been identified. In addition, package insert safety data are missing, which blocks progression to safety screening.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, obtained by downloading and parsing the label
- Mechanism of action data, for example from DrugBank
- A literature and trial search for any link between somatostatin analogues and hypertrichosis or hair growth
- Route and formulation compatibility assessment for the predicted indication
- A review of the metabolic and gallbladder risks, particularly for glucose-lowering drug combinations, if development is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

