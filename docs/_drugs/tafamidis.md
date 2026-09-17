---
layout: default
title: Tafamidis
parent: Model Prediction Only (L5)
nav_order: 745
evidence_level: L5
indication_count: 10
---

# Tafamidis
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

# Tafamidis: From Transthyretin Amyloid Cardiomyopathy to Primary Release Disorder of Platelets

## One-Sentence Summary

Tafamidis is a transthyretin (TTR) stabilizer used to treat transthyretin amyloid cardiomyopathy (ATTR-CM), a progressive infiltrative heart disease well documented in the literature reviewed here.
The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**,
but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only signal with no biological plausibility identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Transthyretin Amyloid Cardiomyopathy (ATTR-CM) *(inferred from literature evidence; no Canadian label data available)* |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 89.27% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on the literature collected for this drug, Tafamidis binds to transthyretin (TTR) and prevents tetramer dissociation, thereby stabilizing the protein and inhibiting amyloidogenesis — this is well established for ATTR-CM and ATTR-PN (polyneuropathy).

However, for the top-ranked prediction (Primary Release Disorder of Platelets), the model's own rationale explicitly states: **there is no known mechanistic link**. Platelet release disorders involve platelet granule/secretion pathways, which do not intersect with TTR amyloid pathology. This appears to be a knowledge-graph embedding similarity artifact rather than a biologically grounded hypothesis, and it is not supported by any clinical trial or publication in the evidence pack.

For context, lower-ranked candidates in this pack — particularly "primary amyloidosis" (rank 5) and "acquired amyloid peripheral neuropathy" (rank 6) — are mechanistically coherent with Tafamidis's known TTR-stabilizing action and are backed by extensive clinical trial and literature evidence. The rank-1 prediction discussed here, by contrast, should not be interpreted as a credible repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Canada Market Information

Tafamidis is currently **not marketed** in Canada (Health Canada market status: Not marketed / Not marketed), with 0 registered DINs. No product license or approved-indication text is available for extraction.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Health Canada label warnings/contraindications for Tafamidis are a blocking data gap (DG001) — this drug cannot proceed to safety pre-screening (S1) until label data is obtained.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (Primary Release Disorder of Platelets) has a high TxGNN embedding score but zero supporting clinical trials or literature, and the model's own mechanistic rationale states there is no known biological link between TTR stabilization and platelet release physiology. This is an L5 (model-prediction-only) candidate and should not advance without independent mechanistic or preclinical justification.

**To proceed, the following is needed:**
- Health Canada product label (warnings/contraindications) — currently blocking (DG001)
- DrugBank/literature-derived mechanism of action detail (DG002)
- Independent biological plausibility assessment for platelet release disorder, given the model rationale found none
- Consider redirecting repurposing review toward higher-evidence candidates in this pack (e.g., primary amyloidosis, acquired amyloid peripheral neuropathy), which have substantial Phase 2–4 trial and literature support consistent with Tafamidis's established TTR-stabilizing mechanism
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

