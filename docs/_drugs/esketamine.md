---
layout: default
title: Esketamine
parent: Model Prediction Only (L5)
nav_order: 349
evidence_level: L5
indication_count: 2
---

# Esketamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Esketamine: From Its Currently Marketed Use to Agoraphobia

## One-Sentence Summary

Esketamine is marketed in Canada as SPRAVATO, but the original approved indication is not recorded in the available data.
The TxGNN model predicts it may be effective for **agoraphobia**, but there are currently **0 clinical trials** and **1 general review article** behind this prediction, so it is essentially a model-only hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Agoraphobia |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 (model prediction; the single review is general and not specific to esketamine) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Esketamine is generally characterized as an NMDA receptor antagonist that enhances glutamatergic signaling. This is plausibly, though only indirectly, relevant to anxiety and fear-related brain circuitry, which is the most likely basis for the model's prediction.

The score is very high (99.57%), but it comes from a graph-based prediction alone. No trial for agoraphobia or panic disorder is available. The one supporting publication is a general review of anxiety-disorder drug treatments. It surveys current and emerging options and is not direct evidence for esketamine in agoraphobia. The relationship between the original indication and agoraphobia therefore cannot be assessed until the approved indication text is retrieved.

**Second-ranked prediction:** TxGNN also ranks *benign paroxysmal torticollis of infancy* (score 99.49%). It has no trials or literature and no plausible mechanistic link, and it is a self-limiting pediatric condition. Pediatric safety of esketamine has not been established, so the benefit-risk balance is unfavorable. It is not pursued further here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33424664](https://pubmed.ncbi.nlm.nih.gov/33424664/) | 2020 | Review | Frontiers in Psychiatry | Summarizes approved and off-label drug treatments for panic disorder, generalized anxiety disorder and social anxiety disorder. Notes that few novel drugs are under investigation for anxiety disorders. It is a general overview and does not test esketamine in agoraphobia. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2499290 | SPRAVATO |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. No clinical trials exist for agoraphobia, and the only literature is a general anxiety-disorder review. Key drug-level data (mechanism of action, Canadian package insert) are also missing, so the case is a research question rather than an actionable repurposing candidate.

**To proceed, the following is needed:**
- The Health Canada package insert (warnings, contraindications, approved indication), which blocks any safety screening
- Detailed mechanism of action data from DrugBank
- Targeted searches for esketamine or ketamine studies in agoraphobia, panic disorder and related anxiety disorders
- An assessment of route compatibility and of the original-to-new indication relationship once the approved indication is known
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

