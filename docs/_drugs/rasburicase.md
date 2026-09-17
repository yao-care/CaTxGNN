---
layout: default
title: Rasburicase
parent: Model Prediction Only (L5)
nav_order: 670
evidence_level: L5
indication_count: 10
---

# Rasburicase
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

# Rasburicase: From Tumor Lysis Syndrome-Associated Hyperuricemia to Renal Hypouricemia

## One-Sentence Summary

Rasburicase (DrugBank DB00049) is a recombinant urate oxidase internationally used to manage hyperuricemia associated with tumor lysis syndrome in cancer chemotherapy patients — though this original indication is not documented in the current Taiwan regulatory dataset, as the drug is not marketed there. The TxGNN model's top prediction is **Renal Hypouricemia**, but the evidence pack's own mechanistic analysis flags this specific prediction as pharmacologically implausible (the disease involves *too little* uric acid, while rasburicase further lowers it) and likely a knowledge-graph embedding artifact rather than a genuine signal. No clinical trials or literature currently support any of the model's top 10 predicted indications.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Taiwan regulatory data (drug not marketed); internationally approved for hyperuricemia associated with tumor lysis syndrome in haematologic malignancies |
| Predicted New Indication | Renal Hypouricemia (rank 1) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on known pharmacology, rasburicase is a recombinant form of urate oxidase, an enzyme that catalyzes the oxidation of uric acid to allantoin, a more soluble compound that is readily excreted renally. It is used to lower elevated uric acid levels, most notably in the supportive management of tumor lysis syndrome during cancer chemotherapy.

The rank-1 prediction, **renal hypouricemia**, is a disorder characterized by pathologically *low* serum uric acid, typically caused by defective uric acid transporters (e.g., SLC22A12/URAT1). This is directionally opposite to rasburicase's pharmacology, which further reduces uric acid levels. The evidence pack's own `repurposing_rationale` explicitly identifies this mismatch and attributes the high TxGNN score to node-embedding similarity in the knowledge graph rather than a causal biological relationship — this prediction should be treated with skepticism rather than as a genuine repurposing lead.

A more mechanistically coherent (though still evidence-free) candidate appears at rank 2: **hypoxanthine-guanine phosphoribosyltransferase (HPRT) partial deficiency** (Kelley-Seegmiller syndrome), a purine salvage disorder that causes uric acid *overproduction* and consequent hyperuricemia/gout/nephrolithiasis. Since rasburicase's established mechanism directly reduces uric acid burden, this direction is biologically plausible, but it remains supported only by model prediction with zero clinical trials or publications identified to date.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Rasburicase is not currently marketed in Taiwan under the available regulatory dataset — no drug identification numbers (DINs) or license records are available (0 of 0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications sit at evidence level L5 (model prediction only), with zero supporting clinical trials or literature across 31 source queries. The top-ranked prediction (renal hypouricemia) is flagged by the evidence pack's own mechanistic analysis as directionally implausible and likely a false signal from knowledge-graph embedding similarity, and the drug is not currently marketed in Taiwan (0 DINs).

**To proceed, the following is needed:**
- TFDA/manufacturer label data on warnings and contraindications (DG001, Blocking — currently prevents entry into S1 safety screening)
- Confirmed mechanism of action data from DrugBank API (DG002)
- Targeted literature/trial searches for the more mechanistically plausible rank-2 candidate (HPRT partial deficiency / Kelley-Seegmiller syndrome) rather than the rank-1 candidate
- Independent pharmacological review to confirm or rule out the rank-1 prediction as a knowledge-graph artifact before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

