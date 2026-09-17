---
layout: default
title: Tolvaptan
parent: Model Prediction Only (L5)
nav_order: 783
evidence_level: L5
indication_count: 10
---

# Tolvaptan
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

# Tolvaptan: From ADPKD (V2 Receptor Antagonism) to Polycystic Kidney Disease 3

## One-Sentence Summary

> Tolvaptan is a selective vasopressin V2 receptor antagonist whose established mechanism underlies its use in autosomal dominant polycystic kidney disease (ADPKD, PKD1/PKD2), though this detail is not directly recorded in the evidence pack (original indication/MOA fields are data gaps).
> The TxGNN model's top prediction for this drug is **Polycystic Kidney Disease 3 (with or without polycystic liver disease)**, a rarer genetic subtype outside the drug's established population,
> with **no clinical trials and no literature** currently registered to support this specific prediction — it is a model-score-only (L5) signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (data gap); mechanistic rationale references ADPKD/PKD1-PKD2 as the drug's established treatment context |
| Predicted New Indication | Polycystic Kidney Disease 3 (with or without polycystic liver disease) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available as a structured field (original_moa is a data gap). Based on the mechanistic rationale accompanying this prediction, tolvaptan is a selective vasopressin V2 receptor antagonist that lowers intracellular cAMP in renal tubular epithelial cells, thereby inhibiting cyst epithelial proliferation and fluid secretion — a pathway that is the established therapeutic mechanism for autosomal dominant polycystic kidney disease (ADPKD, driven by PKD1/PKD2 mutations).

The top-ranked prediction, PKD3, is a rarer polycystic kidney disease subtype. While it shares the "polycystic kidney" phenotype with ADPKD, it is not confirmed to share the same PKD1/PKD2-driven cAMP signaling defect that tolvaptan targets. The rationale explicitly frames this as a mechanistic extrapolation ("可類推但非同一遺傳基因/族群") rather than a validated pathway match, and no trial or literature evidence in the evidence pack corroborates efficacy in PKD3 specifically.

It is also worth noting that this evidence pack contains 9 additional TxGNN-predicted indications beyond PKD3 (ranks 2–10, scores 99.95–99.98%), several of which the model's own rationale flags as having weak or no biological plausibility relative to tolvaptan's V2 receptor mechanism (e.g., hypertrichosis, thoracic malformation, odontal malformation syndrome, Dandy-Walker malformation) — these are assessed as likely knowledge-graph embedding artifacts rather than genuine mechanistic signals. Only ciliopathy-related renal entries (PKD3, Joubert syndrome with renal defect, nephronophthisis-spastic quadriparesis syndrome) have any plausible tubular/cAMP-related rationale, and even these lack supporting evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Canada Market Information

Tolvaptan is currently **not marketed** in Canada under this evidence pack (0 DINs, no license records available).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported only by a TxGNN model score (L5) with no clinical trials or literature evidence for PKD3 specifically, and the target population is a distinct, rarer genetic subtype from tolvaptan's established ADPKD context. The drug is also not currently marketed in Canada.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) and original indication documentation (currently a data gap)
- Regulatory label warnings and contraindications (currently a data gap)
- Genetic/mechanistic evidence confirming PKD3 shares the PKD1/PKD2 cAMP-driven cystogenesis pathway that tolvaptan targets
- Preclinical or case-level evidence specific to PKD3 before advancing beyond S0
- Canada market entry assessment, since the drug currently holds no DIN
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

