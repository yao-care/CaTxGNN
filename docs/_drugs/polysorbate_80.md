---
layout: default
title: Polysorbate 80
parent: Model Prediction Only (L5)
nav_order: 744
evidence_level: L5
indication_count: 1
---

# Polysorbate 80
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

# Polysorbate 80: From Pharmaceutical Excipient to Congenital Ichthyosiform Erythroderma

## One-Sentence Summary

Polysorbate 80 is a non-ionic surfactant and emulsifier, used in Canada as an ingredient in a marketed eye-care product, and it has no established treatment indication of its own.
The TxGNN model predicts it may be effective for **congenital ichthyosiform erythroderma**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | None specified in the available label data (excipient use) |
| Predicted New Indication | Congenital ichthyosiform erythroderma |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Polysorbate 80 is a pharmaceutical excipient with no established pharmacological activity of its own, so there is no proven efficacy in an original indication to extend to a new one.

Congenital ichthyosiform erythroderma is a genetic keratinization and skin-barrier disorder, for example involving TGM1, ALOX12B or ALOXE3 variants. In theory, a surfactant might alter stratum corneum hydration or help deliver topical agents. This is speculative and has no supporting data. Surfactants can also irritate skin and impair barrier function, which could worsen a barrier-deficient condition.

The very high TxGNN score most likely reflects knowledge-graph connectivity for a widely used excipient node rather than a true therapeutic signal. The prediction should be treated as a weak, unverified hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2399148 | REFRESH OPTIVE ADVANCED |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical, literature or mechanistic support (Evidence Level L5). The score likely reflects knowledge-graph connectivity for a common excipient. The surfactant's possible skin-irritating effect on an already impaired skin barrier is a plausible concern.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data, for example from DrugBank
- A literature and trial search for surfactant or excipient use in ichthyosis or related skin-barrier disorders
- Route compatibility assessment, since the only Canadian product identified appears to be an eye-care product, not a dermatological one
- Evidence of any real therapeutic effect separate from its role as a formulation excipient
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

