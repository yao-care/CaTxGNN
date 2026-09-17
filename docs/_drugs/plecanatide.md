---
layout: default
title: Plecanatide
parent: Model Prediction Only (L5)
nav_order: 627
evidence_level: L5
indication_count: 10
---

# Plecanatide
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

# Plecanatide: From Unrecorded Original Indication to Hypertrichosis

## One-Sentence Summary

Plecanatide's original approved indication and detailed mechanism of action are not available in the current data pack (marked as data gaps), and the drug is not currently marketed in Canada. The TxGNN model predicts a possible signal for **Hypertrichosis (disease)** with a near-maximal score, but there are **0 clinical trials** and **0 publications** supporting this specific pairing, and the model's own mechanistic rationale flags the result as a likely statistical false positive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indications on record for this drug) |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for this drug is not available in the current record (`original_moa` is marked as a data gap). However, the model's own rationale notes that plecanatide acts as a locally-restricted agonist of guanylate cyclase-C (GC-C) receptors on the apical surface of intestinal epithelial cells, with minimal systemic absorption — meaning its pharmacological activity is expected to stay largely confined to the gut lumen.

Hypertrichosis (excessive hair growth) is governed by hair follicle growth-cycle regulation, a physiological system with no established connection to intestinal GC-C/cGMP signaling. No shared receptor, pathway, or tissue overlap links the two. This absence of a plausible biological bridge is consistent with what the model's rationale itself concludes: the prediction is likely a statistical artifact of the knowledge-graph embedding space rather than a genuine pharmacological hypothesis.

This concern is reinforced by the wider pattern in this prediction batch: multiple top-ranked candidates for the same drug (ranks 1, 2, and 4) are all hair/hair-follicle-related phenotypes with near-identical, extremely high scores despite zero supporting evidence. This clustering behavior — several unrelated but phenotypically similar diseases all scoring near 1.0 — is more indicative of embedding-space proximity than of a specific, drug-grounded signal, especially given that the drug's own original indication and MOA are undocumented, leaving the model without a real anchor for this drug.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Canada Market Information

Plecanatide currently holds no drug identification numbers (DINs) in Canada and is not marketed (`market_status`: Not marketed / Not Marketed). No licensed products are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a near-maximal TxGNN score, this prediction has no clinical trial or literature support (L5 evidence), and the mechanistic pathway proposed by the model does not plausibly connect the drug's known intestinal-restricted GC-C activity to hair growth regulation. The pattern of multiple unrelated hair-related diseases scoring near-identically in this same batch further suggests an embedding artifact rather than a genuine signal.

**To proceed, the following is needed:**
- Original approved indication(s) and verified mechanism of action for the drug (currently data gaps, DG002)
- TFDA/Health Canada label warnings and contraindications (currently a blocking data gap, DG001)
- Independent pharmacological or preclinical rationale connecting GC-C agonism to hair follicle biology, if this candidate is to be pursued further
- Re-screening of this drug's full prediction list for candidates with actual mechanistic plausibility and/or drug-specific clinical/literature evidence, since none of the top 10 ranked predictions in this batch currently meet that bar
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

