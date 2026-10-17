---
layout: default
title: Calcitriol
parent: Model Prediction Only (L5)
nav_order: 148
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
description: "Calcitriol: predicted new indication Obsolete vitamin D deficiency (evidence level L5). Approved use: Hypercalcemia, nephrocalcinosis, phosphorus metabolism disease…"
monitor_inn: "CALCITRIOL"
predicted_indications: ["obsolete vitamin D deficiency", "renal tubular acidosis", "acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "Dahlberg-Borer-Newcomer syndrome", "hereditary hypophosphatemic rickets"]
---

# Calcitriol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Calcitriol: From Hypercalcemia and Mineral Metabolism Disorders to Vitamin D Deficiency (Obsolete Term)

## One-Sentence Summary

Calcitriol is the active form of vitamin D. It is used for calcium and phosphate disorders such as hypoparathyroidism, hypophosphatemia and renal osteodystrophy.
The TxGNN model predicts it may be effective for **"obsolete vitamin D deficiency"**, a disease term that has been retired from the ontology. The prediction has **0 clinical trials** and **0 publications** behind it, so it is supported by the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, hypophosphatemia, hypoparathyroidism, renal osteodystrophy (from the knowledge graph; no approved indication text is available for the Canadian licences) |
| Predicted New Indication | Obsolete vitamin D deficiency |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Calcitriol is the hormonally active form of vitamin D, and it is already used in disorders of calcium and phosphate balance. A biological link to vitamin D deficiency is therefore plausible, and the very high TxGNN score probably reflects this closeness.

The practical case is weak, though. Nutritional vitamin D deficiency is normally treated with native vitamin D (cholecalciferol or ergocalciferol), not calcitriol. The disease term is also flagged as obsolete, which makes the prediction hard to map onto a defined clinical use. No trials or publications were retrieved to support it.

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
| 00481823 | ROCALTROL |
| 02485710 | TARO-CALCITRIOL |
| 02485729 | TARO-CALCITRIOL |
| 02431645 | CALCITRIOL-ODAN |
| 00481815 | ROCALTROL |

Three more authorizations are also valid: CALCITRIOL-ODAN (02431637), CALCITRIOL INJECTION USP (02399334) and SILKIS (02338572). All 8 are single-ingredient products.

---

## Safety Considerations

Package insert warnings and contraindications were not available for this report, so please refer to the package insert for label-based safety information.

- **Disease-level contraindication signals (knowledge graph, not label text)**: kidney disease, pyoureter, sarcoidosis, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, nephrolithiasis (including SLC26A1-related susceptibility), acute urate nephropathy, hyperphosphatemia, hypervitaminosis, arteriosclerosis obliterans.
- **Drug interactions**: 100 interactions were recorded. The three listed as Major are:
  - Cholecalciferol
  - Calcifediol
  - Burosumab

  Moderate-level interactions include:
  - Thiazide diuretics (hydrochlorothiazide, chlorothiazide, chlorthalidone and others)
  - Barbiturates and anticonvulsants (amobarbital, butalbital, carbamazepine, fosphenytoin)
  - Bile acid sequestrants (cholestyramine, colesevelam, colestipol)
  - Digoxin and digitoxin
  - Aluminum hydroxide
  - Topical calcipotriol

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone. The target term is obsolete, no trials or literature support it, and native vitamin D is the usual treatment for nutritional deficiency.

**To proceed, the following is needed:**
- Clarification of which current disease term replaces "obsolete vitamin D deficiency", and whether a calcitriol-specific clinical need exists.
- Detailed mechanism of action data.
- Package insert warnings and contraindications from Health Canada.

**Note on other predictions from this analysis:** The same analysis ranked **hereditary hypophosphatemic rickets** as a candidate with much stronger support. It is rated L2 and "Proceed with Guardrails", with two registered trials (NCT03748966 and NCT03820518) and reviews describing calcitriol plus phosphate as conventional therapy. Any follow-up should look at this indication first. It would need monitoring of serum and urinary calcium, nephrocalcinosis and PTH, and burosumab is an established alternative.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

