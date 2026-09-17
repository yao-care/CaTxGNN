---
layout: default
title: Lactulose
parent: Model Prediction Only (L5)
nav_order: 438
evidence_level: L5
indication_count: 8
---

# Lactulose
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Lactulose: From Constipation/Hepatic Encephalopathy to Acute Urate Nephropathy

## One-Sentence Summary

Lactulose (DrugBank DB00581) is a synthetic disaccharide osmotic agent generically used for constipation and hepatic encephalopathy; detailed original-indication and mechanism-of-action data are not present in this evidence pack. The TxGNN model's top-ranked prediction is **Acute Urate Nephropathy** (score 99.89%), but this candidate currently has **zero supporting clinical trials and zero supporting literature**, making it a purely model-driven, unvalidated hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (Lactulose is generically classified as an osmotic laxative used for constipation and hepatic encephalopathy) |
| Predicted New Indication | Acute Urate Nephropathy |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed (Not marketed) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this evidence pack (flagged as a High-severity data gap, DG002). Based on generally known pharmacology, Lactulose is a non-absorbable synthetic disaccharide; in the colon it is fermented by bacteria into short-chain fatty acids, producing an osmotic laxative effect (used for constipation) and lowering luminal pH to trap ammonia as ammonium (used for hepatic encephalopathy).

For the top-ranked candidate, **acute urate nephropathy**, the model itself reports no mechanistic bridge: the disease is caused by acute uric-acid crystal precipitation in renal tubules (typically from tumour lysis syndrome), a pathophysiology unrelated to colonic osmotic/ammonia-trapping activity. The evidence pack's own repurposing rationale states this is a "purely data-driven prediction with no supporting mechanistic hypothesis" — there is no plausible pharmacological link identified between Lactulose's known actions and urate nephropathy.

Given the absence of both mechanistic rationale and empirical evidence, this prediction should be treated as low-confidence and exploratory only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/regulatory label warnings and contraindications are flagged as a Blocking-severity data gap (DG001) in this evidence pack, which prevents progression to the S1 safety pre-assessment stage.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (acute urate nephropathy) has a high model confidence score but no clinical trial or literature support, and no plausible mechanistic link — it does not meet even preliminary evidence thresholds for further investment (L5, decision stage S0).

**To proceed, the following is needed:**
- Regulatory label data (warnings/contraindications) — currently a Blocking data gap
- DrugBank/mechanism-of-action data — currently a High-severity data gap
- Original indication documentation from a verified regulatory source
- Consider reprioritizing evaluation toward other candidates in this same evidence pack with materially stronger support — notably **obstructive jaundice** (rank 3, L3/S2, includes a completed Phase 4 trial and a 1991 RCT on lactulose preventing postoperative renal dysfunction), which has a coherent mechanistic story (reduced endotoxemia via gut barrier protection) largely absent here
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

