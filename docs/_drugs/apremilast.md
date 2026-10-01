---
layout: default
title: Apremilast
parent: Model Prediction Only (L5)
nav_order: 67
evidence_level: L5
indication_count: 10
---

# Apremilast
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

# Apremilast: From Psoriatic Arthritis and Psoriasis to Migraine Disorder

## One-Sentence Summary

Apremilast is an oral PDE4 inhibitor marketed for inflammatory conditions such as psoriatic arthritis and psoriasis.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so it is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Psoriatic arthritis and psoriasis (from published literature; the Health Canada indication text is not available in this dataset) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 98.66% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in DrugBank for this drug. Apremilast is generally known as a PDE4 inhibitor. It raises intracellular cAMP and lowers pro-inflammatory cytokines such as TNF-alpha, IL-17 and IL-23. This is why it works in immune-mediated conditions such as psoriatic arthritis and psoriasis.

A link to migraine would have to run through neuroinflammation or cAMP-dependent trigeminovascular signaling. This is speculative, and no study in the evidence pack tests it. The score most likely reflects proximity in the knowledge graph rather than a drug-specific mechanism.

There is also a signal against benefit. Headache is a commonly reported adverse event of apremilast, so the prediction is hard to justify without direct clinical data.

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
| 2434334 | OTEZLA |
| 2521733 | PMS-APREMILAST |
| 2528959 | JAMP APREMILAST |
| 2529092 | SANDOZ APREMILAST |
| 2538180 | APO-APREMILAST |

Five of the 11 authorizations are listed above. The original brand and several generics are on the market.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The migraine prediction rests on a model score alone. It has no trials or literature, its mechanistic link is speculative, and headache is a known adverse event of apremilast. It does not justify further investment at this stage.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, to complete safety screening
- Mechanism of action data from DrugBank, to test a PDE4-to-migraine link
- Any preclinical or clinical signal for apremilast in migraine or trigeminovascular models
- A separate review of the **rheumatoid arthritis** prediction (rank 3, TxGNN score 98.09%). It has the strongest support among the ten predictions, at Evidence Level L2, with Phase 2 randomized trials (for example [NCT01285310](https://clinicaltrials.gov/study/NCT01285310), [PMID 25779750](https://pubmed.ncbi.nlm.nih.gov/25779750/)). Its Phase 2 effect sizes should be checked before deciding whether further study is justified.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

