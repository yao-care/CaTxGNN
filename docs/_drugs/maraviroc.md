---
layout: default
title: Maraviroc
parent: Model Prediction Only (L5)
nav_order: 568
evidence_level: L5
indication_count: 10
---

# Maraviroc
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

# Maraviroc: From HIV-1 Infection to Multiple Endocrine Neoplasia

## One-Sentence Summary

Maraviroc is a CCR5 antagonist marketed in Canada as CELSENTRI, and is generally used to treat HIV-1 infection.
The TxGNN model predicts it may be effective for **multiple endocrine neoplasia (MEN)**, but this is a graph-based prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (from general drug knowledge; the Canadian license records provided contain no indication text) |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Based on known information, maraviroc blocks the CCR5 chemokine receptor, and its efficacy in HIV-1 infection is established.

For multiple endocrine neoplasia, no link to CCR5 antagonism has been identified. MEN is driven by MEN1 or RET gene alterations, which are not part of the CCR5 pathway. The high score comes from the knowledge-graph model alone. No trials, literature, or mechanistic studies support it.

The prediction should therefore be treated as a hypothesis-generating signal, not a repurposing lead. Other candidates on the list have somewhat more support. The most notable is **HER2-positive breast carcinoma**, where preclinical work links autocrine CCL5 to trastuzumab resistance. That would fit a CCL5-CCR5 rationale, but it is preclinical only and has no clinical trials.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2299852 | CELSENTRI |
| 2299844 | CELSENTRI |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no supporting trials or literature, and no plausible mechanism linking CCR5 blockade to MEN pathogenesis. Evidence is at L5 (model prediction only).

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data for maraviroc
- Any preclinical or mechanistic evidence connecting CCR5/chemokine signaling to MEN1- or RET-driven disease
- Consideration of higher-evidence candidates first, such as HER2-positive breast carcinoma (L4, marked "Research Question")

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

