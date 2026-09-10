---
layout: default
title: Risdiplam
parent: 僅模型預測 (L5)
nav_order: 685
evidence_level: L5
indication_count: 10
---

# Risdiplam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Risdiplam: From Spinal Muscular Atrophy to Acne

## One-Sentence Summary

> Risdiplam is an SMN2 pre-mRNA splicing modulator used to treat spinal muscular atrophy (SMA).
> The TxGNN model predicts it may be effective for **Acne**,
> but currently **0 clinical trials** and **0 publications** support this direction, and the model's own rationale flags the signal as likely noise.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Spinal Muscular Atrophy (SMA) *(per evidence-pack mechanistic description; no formal Canada license text available)* |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap in this evidence pack). Based on the information that is available, Risdiplam is an **SMN2 pre-mRNA splicing modulator**: it increases functional SMN protein levels and is used to treat spinal muscular atrophy, a neuromuscular disease.

There is no known pharmacological pathway connecting SMN2 splicing modulation to acne pathology, which is driven by sebaceous gland activity, follicular inflammation, and androgen signaling. The evidence pack's own mechanistic assessment explicitly states this link is **not supported**, and attributes the high TxGNN score to sparse, indirect connections between dermatology-related nodes in the knowledge graph rather than a genuine biological signal.

This pattern is not isolated to acne: all 10 top-ranked predictions in this evidence pack (including a cluster of 4 separate melanoma-subtype entries, drug-induced osteoporosis, elevated plasma zinc, and others) carry the same **L5 / Stage S0 / Hold** assessment, with rationale text repeatedly noting the absence of any known mechanistic link. This suggests a systematic embedding-similarity artifact in this candidate set rather than a set of independently credible repurposing signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Canada Market Information

Risdiplam currently has **no licensed products in Canada** (market status: Not Marketed; 0 DINs on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and drug-interaction data are all recorded as Blocking data gaps in this evidence pack — TFDA/Health Canada product-monograph text has not yet been sourced.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction has no clinical trial or literature support (Evidence Level L5, Decision Stage S0), and the repurposing rationale generated alongside the prediction itself identifies no plausible mechanistic connection between SMN2 splicing modulation and acne pathology — indicating the TxGNN score likely reflects knowledge-graph noise rather than a genuine signal. The drug is also not currently marketed in Canada, and safety data (warnings/contraindications) remains a Blocking gap.

**To proceed, the following is needed:**
- Resolve Blocking data gap DG001: source and parse official product-monograph warnings/contraindications before any S1 safety screening
- Resolve High-priority data gap DG002: confirm detailed MOA via DrugBank API
- Independent mechanistic or preclinical evidence specifically linking SMN2 splicing modulation to dermatologic/sebaceous pathways, if this candidate is to advance
- Given the systematic pattern across all 10 predictions in this pack, consider re-evaluating the underlying knowledge-graph embeddings for this drug before pursuing any individual candidate further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

