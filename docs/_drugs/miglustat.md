---
layout: default
title: Miglustat
parent: Model Prediction Only (L5)
nav_order: 612
evidence_level: L5
indication_count: 10
---

# Miglustat
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

# Miglustat: From Gaucher Disease to Autosomal Ichthyosis Syndrome with Fatal Disease Course

## One-Sentence Summary

Miglustat is an oral glucosylceramide synthase inhibitor, launched for type 1 Gaucher disease (per the supplied literature; the Canadian licence records list no indication text).
The TxGNN model predicts it may be effective for **autosomal ichthyosis syndrome with fatal disease course**,
but currently **0 clinical trials** and **0 publications** support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 1 Gaucher disease (from literature, not from the licence records) |
| Predicted New Indication | Autosomal ichthyosis syndrome with fatal disease course |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Based on known information, miglustat inhibits glucosylceramide synthase, the first step of glycosphingolipid synthesis. This "substrate reduction" approach lowers the amount of lipid that accumulates in storage disorders such as Gaucher disease.

The link to the predicted disease is speculative. Some ichthyoses involve defects in epidermal ceramide and lipid metabolism, so altering the glycosphingolipid pool could conceivably matter. However, the specific disease is not well defined in the data, and no study shows that suppressing this pathway would help. The high score (99.83%) is best read as a model output that still needs biological validation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2456257 | SANDOZ MIGLUSTAT |
| 2556812 | OPFOLDA |
| 2250519 | ZAVESCA |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for this disease has a high model score but no trials, no literature and only a speculative mechanism, so it stays at L5 (model prediction only).

Note that the pack ranks this disease first only by TxGNN score. The only candidate with real supporting evidence is **Tay-Sachs disease** (rank 7, score 99.75%). It has 5 registered trials (for example NCT00672022, NCT00418847), 20 publications including a randomized controlled study in late-onset disease (PMID 19346952) and a systematic review (PMID 37209042). Those trials are small, mostly pharmacokinetic and safety studies, and the pack notes that clinical benefit on neurological outcomes is not clear. Consider re-running this report with Tay-Sachs as the primary indication.

**To proceed, the following is needed:**
- Clarify which disease "autosomal ichthyosis syndrome with fatal disease course" refers to, then search for supporting preclinical or clinical data
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text for the three Canadian licences
- Detailed mechanism of action data from DrugBank
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

