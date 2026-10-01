---
layout: default
title: Diazoxide
parent: Model Prediction Only (L5)
nav_order: 275
evidence_level: L5
indication_count: 10
---

# Diazoxide
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

# Diazoxide: From Hyperinsulinemic Hypoglycemia to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Diazoxide is a K-ATP channel opener. The literature describes it as first-line oral therapy for hyperinsulinemic hypoglycemia, and its Canadian license record does not state an indication.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**, but there are **0 clinical trials** and **0 publications** for this specific disease.
The prediction rests on model output alone (Evidence Level L5).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license record; the literature describes hyperinsulinemic hypoglycemia as the established use |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Diazoxide opens K-ATP channels. In pancreatic beta cells this suppresses insulin release, which explains its use in hyperinsulinemic hypoglycemia. Detailed mechanism of action data is not available in the evidence pack. Hypertrichosis is a well-known adverse effect of the drug, so a hair-growth-stimulating effect is plausible. Minoxidil sulfate, which also opens K-ATP channels, has a similar effect.

The link to this specific disease is weak. Hypotrichosis simplex is a monogenic hair-follicle disorder (for example CDSN, APCS, SNRPE variants). No data connect K-ATP opening to these pathways. The high score is a knowledge-graph prediction, not a mechanistic finding.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for this disease.

## Canada Market Information

| License Number | Product Name |
|---------|------|
| 503347 | PROGLYCEM |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no trials, no literature and no mechanistic link, so it is unsupported beyond the model score.

Other candidates in the same prediction list vary in how well they are supported:
- **Alopecia (L4, research question):** the only direct preclinical evidence is topical diazoxide altering hair growth in the stumptailed macaque (PMID 2085505). No human efficacy trials exist.
- **Autosomal dominant hyperinsulinism due to Kir6.2 deficiency (L4, research question):** this is closer to rediscovery of the label use than to true repurposing, and no subtype-specific data are available.
- **Hypertrichosis:** the direction is contradictory. It is a common diazoxide adverse effect, so this association should be excluded or recorded as a safety signal.
- **Remaining candidates (L5):** they have no supporting data. The periodontal results are keyword-matching artifacts.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data from DrugBank
- The approved indication text for the Canadian license
- For the alopecia direction: topical formulation work, human dose-finding, and monitoring of systemic absorption and hypotension
- For the Kir6.2 direction: genotype-response data and labeling status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

