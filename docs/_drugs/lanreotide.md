---
layout: default
title: Lanreotide
parent: Model Prediction Only (L5)
nav_order: 523
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-24
monitor_inn: "LANREOTIDE"
predicted_indications: ["hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "Ambras type hypertrichosis universalis congenita"]
description: "Lanreotide: predicted new indication Hypertrichosis (disease) (evidence level L5). In Canada: 6 DINs (6 marketed)"
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

## Lanreotide: Hypertrichosis (disease)
{: .text-alpha }

## One-Sentence Summary

Lanreotide is a somatostatin analogue originally used to treat acromegaly, hyperpituitarism and pituitary gigantism.
The TxGNN model predicts it may be effective for **Hypertrichosis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 6 of 6) |
| Number of DINs | 6 (marketed: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for lanreotide: "Lanreotide, the active component of SOMATULINE DEPOT is an octapeptide analog of natural somatostatin. The mechanism of action of lanreotide is believed to be similar to that of natural somatostatin." ([DailyMed: Somatuline Depot (lanreotide acetate) prescribing information, Ipsen Biopharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6e4a41fd-a753-4362-87ee-8cc56ed3660d), label version 2024-10-11; accessed 2026-11-19.) Based on general knowledge, lanreotide is a somatostatin analogue that acts mainly through somatostatin receptors SSTR2 and SSTR5 to suppress growth hormone (GH) and IGF-1 secretion. Its efficacy in acromegaly is established.

The link to hypertrichosis is weak. Hypertrichosis is not a recognized GH/IGF-1-driven condition. Acromegaly can cause excess hair growth as a secondary feature, but that is an indirect association and not evidence that lanreotide would benefit hypertrichosis. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No trial or literature record supports it.

Other top-ranked predictions are also unsupported by any trial or publication, and none has a plausible mechanistic rationale:
- Malformation syndrome with odontal and/or periodontal component (0.9996)
- Syndrome with a Dandy-Walker malformation as major feature (0.9996)
- Isolated genetic hair shaft abnormality (0.9996)
- Ambras type hypertrichosis universalis congenita (0.9996)

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02283395 | SOMATULINE AUTOGEL | LANREOTIDE (LANREOTIDE ACETATE) | Marketed |
| 02283409 | SOMATULINE AUTOGEL | LANREOTIDE (LANREOTIDE ACETATE) | Marketed |
| 02283417 | SOMATULINE AUTOGEL | LANREOTIDE (LANREOTIDE ACETATE) | Marketed |
| 02555867 | MYTOLAC | LANREOTIDE (LANREOTIDE ACETATE) | Marketed |
| 02555875 | MYTOLAC | LANREOTIDE (LANREOTIDE ACETATE) | Marketed |
| 02555883 | MYTOLAC | LANREOTIDE (LANREOTIDE ACETATE) | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

<!-- review:begin ca-lic-20261124b-lanreotide-1 -->

> **Review correction (2026-11-24)**: Originally stated: "A sixth authorization (DIN 02555875, MYTOLAC) is also valid." Removed: it referred to the earlier licence table, which showed only some of the DINs (for example "the sixth", "the remaining …", "shown here"). The table under Canada Market Information is now generated from the Health Canada DPD data and lists every DIN in the data with its current status. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261124b-lanreotide-1 -->

All six are single-ingredient products and none is cancelled.

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

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Somatuline Depot (lanreotide acetate) prescribing information, Ipsen Biopharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6e4a41fd-a753-4362-87ee-8cc56ed3660d) |
| 2026-11-24 | Removed: "A sixth authorization (DIN 02555875, MYTOLAC) is also valid." | Corrected | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

