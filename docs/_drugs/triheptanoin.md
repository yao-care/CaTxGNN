---
layout: default
title: Triheptanoin
parent: Model Prediction Only (L5)
nav_order: 804
evidence_level: L5
indication_count: 10
---

# Triheptanoin
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

# Triheptanoin: From Undocumented Original Indication to Craniostenosis Cataract

## One-Sentence Summary

> Triheptanoin's original approved indication is not documented in the current evidence pack, and Canadian market status is "not marketed" with zero licenses on file.
> The TxGNN model predicts a possible link to **Craniostenosis Cataract**, with a prediction score of **99.98%**,
> but **0 clinical trials** and **0 publications** currently support this direction — this is a pure computational prediction (L5) with no independent verification.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (no Canadian license data, no `original_indications` on file) |
| Predicted New Indication | Craniostenosis cataract |
| TxGNN Prediction Score | 99.98% (rank 930 among all disease predictions) |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa: [Data Gap]`). Based on the evidence pack's own repurposing rationale, triheptanoin is an odd-chain medium-chain triglyceride that acts on the mitochondrial fatty acid oxidation / anaplerosis pathway. No known biological connection has been established between this pathway and crystalline lens protein pathology in craniostenosis-associated cataract.

Because there is no `original_indications` data on file and market status in Canada is "not marketed," there is no reference indication against which to assess mechanistic plausibility or therapeutic-area proximity. The rationale text accompanying this candidate explicitly states: *"無已知機轉關聯...原始 MOA 資料缺失，無法建立合理假說"* (no known mechanistic link; with MOA data missing, no plausible hypothesis can be constructed).

A further concern is the pattern across the top 10 predictions: 9 of the top 10 are different cataract subtypes (craniostenosis cataract, diabetes mellitus type 2 associated cataract, mature cataract, immature cataract, tetanic cataract, diabetic cataract, cortical cataract, nuclear senile cataract, senile cataract) with nearly identical scores (0.99968–0.99975) and consecutive-adjacent ranks (930–1017). The single outlier, antithrombin deficiency type 2 (rank 1097), shares no plausible mechanistic connection with the others either. This pattern — near-identical scores clustered on one disease category, plus a mechanistically unrelated outlier — is consistent with an embedding clustering artifact in the TxGNN model rather than a biologically specific signal, as the evidence pack itself flags for the diabetes-associated cataract candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Triheptanoin is not currently marketed in Canada, and no Drug Identification Numbers (DINs) are on file in the evidence pack. No license or approved-indication data is available for extraction.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no clinical trial or literature support (L5, decision stage S0), no established mechanistic link, and the top-ranked predictions show a pattern consistent with a model embedding artifact rather than a specific biological signal. Combined with the absence of Canadian market presence, original indication data, and MOA data, there is currently no basis to advance this candidate beyond model output.

**To proceed, the following is needed:**
- Drug-level MOA data (DrugBank API query, per DG002)
- Regulatory safety data — warnings, contraindications, DDI (per DG001, currently Blocking)
- Documented original/approved indication(s) for this drug in any jurisdiction, to establish a reference point for mechanistic plausibility
- Independent confirmation that the top predictions are not an embedding-clustering artifact (e.g., re-run with perturbation analysis or compare against a disease-diverse control set)
- If pursued, targeted literature/preclinical search specifically on fatty acid oxidation pathways in lens/crystallin biology
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

