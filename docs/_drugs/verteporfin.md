---
layout: default
title: Verteporfin
parent: Model Prediction Only (L5)
nav_order: 825
evidence_level: L5
indication_count: 1
---

# Verteporfin
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

# Verteporfin: From Macular Degeneration to Mitochondrial Oxidative Phosphorylation Disorder

## One-Sentence Summary

> Verteporfin is a photosensitizing agent established for photodynamic therapy in age-related macular degeneration, and separately known as a YAP/TAZ transcriptional co-activator inhibitor.
> The TxGNN model predicts it may be relevant to **mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-score-only signal with no verifiable mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Age-related macular degeneration (photodynamic therapy) — based on known clinical use; no formal license record exists since the drug is not marketed in Canada |
| Predicted New Indication | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 99.49% (rank 9418) |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (original_moa: Data Gap) in the structured record. Based on known information, verteporfin acts as a photosensitizer used in photodynamic therapy for macular degeneration, and separately has been characterized as an inhibitor of the YAP/TAZ transcriptional co-activators.

Neither of these known mechanisms provides an established biological pathway connecting verteporfin to nuclear-DNA-related defects in mitochondrial oxidative phosphorylation. The evidence pack's own repurposing rationale states explicitly that there is **no verifiable mechanistic link**: no literature supports a direct regulatory effect of verteporfin on the oxidative phosphorylation pathway in this disease context.

This prediction should therefore be treated as a pure knowledge-graph association score from TxGNN, without biological plausibility support at this stage. It is not reasonable to advance this candidate on mechanistic grounds alone.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Canada Market Information

Verteporfin is not currently marketed in Canada under this evidence pack (0 licenses, market status: Not marketed/Not marketed). No DIN or product record is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and drug-interaction data are currently marked as data gaps in this evidence pack — including a Blocking-severity gap for regulatory warning/contraindication labeling — and cannot be summarized here.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN association score (L5, decision stage S0) with zero clinical trials, zero literature, and no verifiable mechanistic link between verteporfin's known pharmacology and the predicted indication. A Blocking-severity data gap (regulatory warnings/contraindications) also prevents safety pre-screening (S1).

**To proceed, the following is needed:**
- TFDA/Health Canada label data (warnings, contraindications) to clear the Blocking data gap
- Confirmed mechanism of action (MOA) data via DrugBank API to enable mechanistic-relevance analysis
- Independent literature or preclinical search specifically on verteporfin and mitochondrial oxidative phosphorylation pathways, since none currently exists
- Re-evaluation of route compatibility (currently "pending") given verteporfin is normally administered via IV infusion for photodynamic therapy, which may not suit a metabolic/mitochondrial disorder indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

