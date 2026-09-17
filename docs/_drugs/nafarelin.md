---
layout: default
title: Nafarelin
parent: Model Prediction Only (L5)
nav_order: 539
evidence_level: L5
indication_count: 10
---

# Nafarelin
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

# Nafarelin: From GnRH Agonist Therapy to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Nafarelin (DB00666) is a GnRH agonist whose established pharmacology (referenced within this evidence pack's rationale annotations) supports endometriosis-related pain management and central precocious puberty. The TxGNN model's top-ranked prediction is **Ambras Type Hypertrichosis Universalis Congenita**, with a **99.87% prediction score**, but currently **0 clinical trials** and **0 publications** support this direction — the accompanying rationale explicitly flags this as likely knowledge-graph embedding noise rather than a genuine biological signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from regulatory license data (drug not marketed); pharmacologically known as a GnRH agonist used for endometriosis-related pain and central precocious puberty |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed (Not Marketed) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is flagged as a data gap in this evidence pack. Based on annotations embedded in the repurposing rationale, nafarelin is a GnRH agonist that, with continuous dosing, desensitizes the pituitary and suppresses LH/FSH secretion — the mechanism underlying its known use in hormone-dependent conditions.

Ambras type hypertrichosis universalis congenita, however, is a rare congenital disorder linked to chromosome 8 rearrangements affecting hair follicle development. There is no established biological pathway connecting hypothalamic-pituitary-gonadal axis suppression to this condition's pathophysiology.

The rationale accompanying this prediction states directly: *"先天性全身多毛症為罕見遺傳性疾病，與 GnRH 促效劑之下視丘-垂體-性腺軸抑制機轉無生物學關聯，TxGNN 高分推測為圖譜嵌入噪音"* — i.e., this high score is assessed as a graph-embedding artifact rather than a mechanistically grounded signal. This prediction should not be interpreted as a promising repurposing candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Nafarelin currently holds no Canadian market authorization (0 DINs on file; market status: Not marketed / Not Marketed). No licensed product records are available to summarize.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This top-ranked TxGNN prediction has zero supporting clinical trials or literature, and the mechanistic rationale itself identifies it as likely model noise rather than a biologically plausible signal. There is no basis to advance this specific indication.

**To proceed, the following is needed:**
- Confirmed mechanism of action data from DrugBank (currently a data gap, High severity)
- Health Canada / TFDA label warnings and contraindications (currently a Blocking data gap, required before any safety review)
- If repurposing signal is still of interest, evaluate other candidates in this evidence pack with stronger support instead — notably rank 7 ("physiological sexual disorder," L3 evidence, one comparative clinical trial on nafarelin in endometriosis-related pain) and rank 9 (central precocious puberty, L1 evidence — though this appears to be an already-approved indication rather than a new repurposing candidate, and the 0 trials/0 literature shown for it reflects a data collection gap, not absence of real-world evidence)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

