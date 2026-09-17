---
layout: default
title: Propranolol
parent: Model Prediction Only (L5)
nav_order: 654
evidence_level: L5
indication_count: 6
---

# Propranolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Propranolol: From Cardiovascular Indications to Distal Myopathy, Tateyama Type

## One-Sentence Summary

Propranolol is a non-selective beta-adrenergic blocker with long-established cardiovascular indications (this evidence pack contains no Canadian license or approved-indication text, as the drug is not currently marketed in Canada). The TxGNN model's top-ranked prediction for this drug is **Distal Myopathy, Tateyama Type**, a rare hereditary muscle disease, but this prediction is currently supported by **0 clinical trials** and **0 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — Health Canada shows no license for propranolol; original indication data was not provided in this evidence pack |
| Predicted New Indication | Distal myopathy, Tateyama type |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed (Not Marketed) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap — DrugBank MOA lookup still pending). Propranolol is a non-selective β1/β2-adrenergic receptor antagonist, but without a confirmed MOA record in this pack, no formal statement can be made about how that mechanism connects to the predicted indication.

Distal myopathy, Tateyama type is a rare, autosomal-dominant hereditary muscle disorder linked to structural muscle-fiber genes, not to adrenergic signaling pathways. The repurposing rationale explicitly notes there is **no known pathophysiological link** between β-adrenergic blockade and this disease.

The TxGNN score of 99.40% reflects knowledge-graph embedding similarity rather than any validated mechanistic or empirical relationship. In the absence of any supporting trials, literature, or biological rationale, this prediction should be treated as a hypothesis-generation artifact rather than a credible repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Canada Market Information

Propranolol has no active Health Canada drug licenses on file in this evidence pack (`total_licenses: 0`, market status: Not marketed / Not Marketed). No DIN-level product or indication data is available.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are not yet available for this drug — DG001, TFDA label warnings/contraindications, is flagged as a Blocking data gap.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by TxGNN embedding similarity (Evidence Level L5, Decision Stage S0) with no clinical trials, no literature, and no established mechanistic connection between propranolol's β-blockade and this rare hereditary myopathy. There is insufficient evidence to advance this candidate.

**To proceed, the following is needed:**
- Mechanism-of-action data for propranolol (DG002 — High severity)
- TFDA/Health Canada label warnings and contraindications (DG001 — Blocking severity, required before any safety pre-screen)
- Preclinical or genetic/pathophysiology evidence linking adrenergic signaling to Tateyama-type distal myopathy
- Reassessment of Canadian market status, since propranolol currently has no active license in this dataset

**Note:** This same evidence pack contains a much better-supported candidate for propranolol — **cardiomyopathy** (rank 6, Evidence Level L2, Decision Stage S2, "Proceed with Guardrails"), backed by 3 clinical trials and 20 publications, including RCT-level evidence in hypertrophic cardiomyopathy. If the goal is to identify a viable repurposing pathway for propranolol rather than evaluate the single top TxGNN-ranked hit, that candidate warrants a separate, dedicated evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

