---
layout: default
title: Povidone
parent: 僅模型預測 (L5)
nav_order: 441
evidence_level: L5
indication_count: 1
---

# Povidone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Povidone: From Pharmaceutical Excipient to Congenital Ichthyosiform Erythroderma

## One-Sentence Summary

Povidone (PVP) is a synthetic polymer used almost exclusively as a pharmaceutical excipient (binder, film-former, suspending/solubilizing agent) and does not carry an approved therapeutic indication of its own. The TxGNN model predicts a possible association with **Congenital Ichthyosiform Erythroderma**, a rare inherited skin-barrier disorder, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the underlying mechanistic rationale itself flags the signal as a likely knowledge-graph artifact rather than a genuine pharmacological link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — povidone is a pharmaceutical excipient with no approved therapeutic indication of its own |
| Predicted New Indication | Congenital Ichthyosiform Erythroderma |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L5 (model prediction only; no clinical trials or literature) |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for povidone is not available. This is consistent with what is otherwise known about the substance: povidone is not developed or regulated as an active pharmaceutical ingredient with its own indication. It is an inert, high-molecular-weight polyvinylpyrrolidone polymer used across many drug products as a tablet binder, film-forming agent, and suspending/solubilizing vehicle. It has no established receptor target, enzyme inhibition profile, or systemic pharmacological activity.

Congenital Ichthyosiform Erythroderma is a rare, genetically inherited disorder of skin barrier formation and lipid metabolism (commonly linked to genes such as *ABCA12*, *TGM1*, and *NIPAL4*). Its pathophysiology is entirely unrelated to any known excipient function — there is no structural, receptor, or metabolic pathway overlap between an inert polymer excipient and the lipid/keratinization defects that drive this disease.

Taken together, the repurposing rationale itself concludes there is **no plausible mechanistic link**. The high TxGNN score (99.11%) most likely reflects a co-occurrence confound in the knowledge graph — povidone frequently appears as a vehicle/base ingredient in topical dermatological formulations, which places it near many skin-disease nodes without any causal pharmacological relationship. This prediction should be treated as a likely false positive rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Canada Market Information

Povidone (as a standalone active ingredient) currently holds no Health Canada market authorizations — 0 DINs are on record, and market status is **Not Marketed**.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Regulatory label warnings/contraindications data for this candidate is currently missing and is flagged as a Blocking data gap, meaning it cannot yet proceed to formal safety screening — see Next Steps below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a numerically high TxGNN score, this candidate has zero supporting clinical trials or literature (Evidence Level L5), and the mechanistic rationale explicitly identifies the prediction as a probable knowledge-graph artifact — povidone is an inert excipient with no plausible biological pathway connecting it to a genetic skin-barrier disorder. There is currently no basis to advance this candidate beyond initial screening.

**To proceed, the following is needed:**
- Resolve **DG001 (Blocking)**: obtain official regulatory label warnings/contraindications before this candidate can enter Stage S1 safety review
- Resolve **DG002 (High)**: obtain verified mechanism-of-action data via the DrugBank API to properly assess mechanistic plausibility
- Independent orthogonal evidence (e.g., in vitro or case-level data) demonstrating a genuine mechanistic link, given the current rationale suggests this is a false-positive knowledge-graph association
- Re-evaluation only if new clinical or literature evidence emerges; otherwise this candidate should remain deprioritized
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

