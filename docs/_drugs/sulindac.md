---
layout: default
title: Sulindac
parent: Model Prediction Only (L5)
nav_order: 740
evidence_level: L5
indication_count: 10
---

# Sulindac
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

# Sulindac: From NSAID (Anti-inflammatory) Use to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

> Sulindac is generally known as an NSAID acting through COX-1/2 inhibition, but no confirmed original indication or regulatory label data is present in this evidence pack (the drug is currently not marketed in Canada). The TxGNN model predicts potential activity against **Acromesomelic Dysplasia, Hunter-Thompson Type**, a rare skeletal dysplasia, but this prediction is currently supported by **0 clinical trials** and **0 publications** — the evidence pack itself flags this as a likely knowledge-graph artifact rather than a biologically grounded signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no `original_indications` or license data on file; Sulindac is generically classified as an NSAID (COX-1/2 inhibitor) based on mechanistic notes elsewhere in this pack |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.92% (rank 2174) |
| Evidence Level | L5 — model prediction only, no clinical or literature support |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap requiring a DrugBank API lookup). Based on the informal mechanistic notes attached to this candidate, Sulindac is understood to act as an NSAID via COX-1/2 inhibition and possibly through Wnt/APC pathway modulation — the latter is the basis for its known off-label use in familial adenomatous polyposis, not for skeletal dysplasias.

Acromesomelic Dysplasia, Hunter-Thompson Type is a rare autosomal recessive skeletal disorder caused by defects in the NPR2/GDF5 signaling pathway, which governs endochondral bone growth. This pathway has no established interaction with COX-mediated prostaglandin signaling or Wnt/APC regulation. The evidence pack's own rationale explicitly states there is **no clear mechanistic relationship** between Sulindac's known pharmacology and this disease, and attributes the very high TxGNN score to likely **noise from a sparse knowledge-graph node** (a rare disease with few connected edges), rather than a genuine biological signal.

Given the absence of any mechanistic, preclinical, clinical, or literature support, this prediction should be treated as exploratory/hypothesis-generating only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Sulindac has **0 active Canadian licenses (DINs)** on file — market status is "Not Marketed." No product-level authorization data is available to report.

---

## Safety Considerations

Please refer to the package insert for safety information.

Note: Regulatory safety data (warnings, contraindications, drug interactions) could not be retrieved for this drug — this is flagged in the evidence pack as a **Blocking** data gap (DG001), meaning this candidate cannot currently pass the S1 safety pre-screening stage regardless of prediction score.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5 (model prediction only), with zero supporting clinical trials or publications, and the drug's own mechanistic rationale explicitly questions the biological plausibility of this link, attributing the score to sparse-graph noise. Additionally, a Blocking data gap on safety/labeling information prevents this candidate from advancing past the S0/S1 stage.

**To proceed, the following is needed:**
- Mechanism of action data via DrugBank API query (DG002)
- Health Canada / TFDA product monograph for warnings and contraindications (DG001, Blocking)
- Independent literature or preclinical evidence linking NPR2/GDF5 signaling to COX-1/2 or Wnt/APC pathways
- Re-evaluation of TxGNN score reliability for this sparse-node disease target before further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

