---
layout: default
title: Alfacalcidol
parent: Model Prediction Only (L5)
nav_order: 31
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Alfacalcidol: predicted new indication Familial isolated hypoparathyroidism due to impaired PTH secretion (evidence level L5). Approved use: Hyperparathyroidism, osteitis fibrosa, hypoparathyroidism…"
monitor_inn: "ALFACALCIDOL"
predicted_indications: ["Dahlberg-Borer-Newcomer syndrome", "craniofacial conodysplasia", "acromesomelic dysplasia, Campailla Martinelli type", "renal tubular acidosis"]
---

# Alfacalcidol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Alfacalcidol: From Hyperparathyroidism to Familial Isolated Hypoparathyroidism

## One-Sentence Summary

Alfacalcidol is an active vitamin D analog, originally used for hyperparathyroidism, osteitis fibrosa, hypoparathyroidism and renal osteodystrophy.
The TxGNN model predicts it may be effective for **familial isolated hypoparathyroidism due to impaired PTH secretion**.
Currently there are **no clinical trials** and **no publications** supporting this specific prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperparathyroidism, osteitis fibrosa, hypoparathyroidism, renal osteodystrophy (the Health Canada licence records compiled for this report contain no indication text) |
| Predicted New Indication | Familial isolated hypoparathyroidism due to impaired PTH secretion |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, alfacalcidol is a 1-alpha-hydroxylated vitamin D analog. It bypasses renal 1-alpha-hydroxylase and does not need PTH stimulation to become active.

That makes it biologically plausible for states where PTH is lacking. Hypoparathyroidism is already among its original indications, and the familial isolated form is a genetic subtype of the same condition. The high score (0.996) therefore most likely reflects closeness to the existing indication rather than a genuinely new repurposing opportunity.

No trials or publications were found for this specific subtype, so the support is prediction-only.

### Other Predicted Indications (for reference)

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Dahlberg-Borer-Newcomer syndrome | 99.60% | L4 | Historical name associated with Fanconi-Bickel syndrome. Alfacalcidol could plausibly help with the bone disease, but this would be symptomatic management. Most retrieved publications are off-target, and the one on-condition paper concerns a different drug (empagliflozin). Hold. |
| 3 | Craniofacial conodysplasia | 99.55% | L5 | No mechanistic rationale evident. No evidence. Hold. |
| 4 | Acromesomelic dysplasia, Campailla Martinelli type | 99.53% | L5 | Linked to growth-plate signalling rather than the vitamin D/PTH axis. No evidence. Hold. |
| 5 | Renal tubular acidosis | 99.27% | L4 | Mechanistically plausible as an adjunct for osteomalacia and rickets. Evidence is five case reports. Flagged as a research question. |

## Clinical Trial Evidence

Currently no related clinical trials registered for the predicted indication.

## Literature Evidence

Currently no related literature available for the predicted indication (familial isolated hypoparathyroidism).

For reference, the publications retrieved for the fifth-ranked prediction, renal tubular acidosis, are all case reports:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22740247](https://pubmed.ncbi.nlm.nih.gov/22740247/) | 2013 | Case report | Mod Rheumatol | Osteomalacia from renal tubular acidosis in Sjögren's syndrome. Treated with sodium bicarbonate, risedronate, alfacalcidol and prednisolone; bone density normalised by 24 months. |
| [11518137](https://pubmed.ncbi.nlm.nih.gov/11518137/) | 2001 | Case report | Intern Med | Rapid osteomalacia improvement in a patient with Sjögren's syndrome, rheumatoid arthritis and type 1 RTA. Alkali supplement and an alfacalcidol-containing regimen. |
| [33398781](https://pubmed.ncbi.nlm.nih.gov/33398781/) | 2021 | Case report | CEN Case Rep | Osteomalacia from atypical RTA with vitamin D deficiency, in a patient previously on active vitamin D. |
| [28509074](https://pubmed.ncbi.nlm.nih.gov/28509074/) | 2012 | Case report/Review | CEN Case Rep | Osteomalacia secondary to distal RTA due to Sjögren's syndrome, with literature review. |
| [36412607](https://pubmed.ncbi.nlm.nih.gov/36412607/) | 2023 | Case report | Kidney Blood Press Res | Severe hypophosphataemia, renal Fanconi syndrome and distal RTA related to zoledronic acid. |

These reports describe improvement with regimens that also included alkali and phosphate, so they do not isolate alfacalcidol's contribution.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02533324 | SANDOZ ALFACALCIDOL | Not listed | Not listed |
| 02240329 | ONE-ALPHA | Not listed | Not listed |
| 00474525 | ONE-ALPHA | Not listed | Not listed |
| 00474517 | ONE-ALPHA | Not listed | Not listed |
| 02242502 | ONE-ALPHA | Not listed | Not listed |

A sixth licence (DIN 02533316, SANDOZ ALFACALCIDOL) is also valid. All six are single-ingredient products.

## Safety Considerations

Please refer to the package insert for safety information.

Mechanism-based note: for the renal tubular acidosis prediction, hypercalciuria and nephrocalcinosis risk call for calcium and renal monitoring.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is essentially a genetic subtype of an existing indication (hypoparathyroidism). It has no trials or literature specific to it, so the evidence level is L5 and it adds little new repurposing value. Among the alternatives, renal tubular acidosis is the most promising (L4, case reports only) but needs stronger evidence.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Approved indication text, dosage forms and manufacturer details for the Canadian licences
- Clinical evidence specific to the familial isolated form of hypoparathyroidism, or a decision to treat it as covered by the existing hypoparathyroidism indication
- For renal tubular acidosis: controlled or larger observational studies that isolate alfacalcidol's effect, plus a calcium and renal monitoring plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

