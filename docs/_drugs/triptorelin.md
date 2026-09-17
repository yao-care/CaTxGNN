---
layout: default
title: Triptorelin
parent: Model Prediction Only (L5)
nav_order: 806
evidence_level: L5
indication_count: 10
---

# Triptorelin
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

# Triptorelin: From Undocumented Original Indication to Hypertrichosis

## One-Sentence Summary

> This evidence pack does not document triptorelin's original approved indication, and the drug is currently **not marketed in Canada**.
> The TxGNN model predicts a possible association with **Hypertrichosis (disease)**,
> but this is currently supported by **0 clinical trials** and only **1 indirect case report**, with no established mechanistic basis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.9970% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for triptorelin is not available in this evidence pack, and its original approved indication has not been documented in the current dataset — consistent with its "Not Marketed" status in Canada (0 DINs on file).

Based on the single available literature record, the link between triptorelin and hypertrichosis is indirect rather than mechanistic. The one case report describes a transgender woman on testosterone-blocking therapy (including triptorelin and estradiol) who developed generalised hypertrichosis after starting **ciclosporin** — a drug independently well known to cause hypertrichosis. The paper attributes the hair growth to ciclosporin, not to triptorelin; triptorelin's role is incidental to the case rather than causal.

Given this, the TxGNN model's very high prediction score (99.9970%) most likely reflects a knowledge-graph-level association (e.g., shared patient context, comorbid drug exposure, or hormonal-axis proximity in the graph) rather than a validated pharmacological mechanism connecting a GnRH agonist to hair growth. No independent mechanistic rationale for triptorelin inducing or treating hypertrichosis is present in the evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41822646](https://pubmed.ncbi.nlm.nih.gov/41822646/) | 2026 | Case Report | Cureus | Describes ciclosporin-induced generalised hypertrichosis in a transgender woman on testosterone-blocking therapy (estradiol + triptorelin); hypertrichosis is attributed to ciclosporin, with triptorelin present only as a concurrent medication, not the causal agent. |

## Canada Market Information

Triptorelin is currently **not marketed in Canada** — no Drug Identification Numbers (DINs) are on file (total licenses: 0).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence for triptorelin in hypertrichosis consists of a single case report that does not causally implicate triptorelin, with zero supporting clinical trials and no mechanistic hypothesis — this meets only L5 (model prediction only). Additionally, two blocking/high-severity data gaps (TFDA/label warnings and MOA) prevent even a baseline safety assessment.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official product labeling / warnings and contraindications before any safety evaluation can proceed
- Resolve DG002 (High): obtain mechanism of action data from DrugBank to assess biological plausibility
- Documentation of triptorelin's original approved indication(s), since the current evidence pack has none on record
- Additional independent literature or preclinical data specifically implicating GnRH agonism (not concurrent ciclosporin use) in hair growth modulation, before this candidate can move beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

