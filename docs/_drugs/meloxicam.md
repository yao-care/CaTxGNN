---
layout: default
title: Meloxicam
parent: Model Prediction Only (L5)
nav_order: 576
evidence_level: L5
indication_count: 10
---

# Meloxicam
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

# Meloxicam: From Conventional NSAID Use to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Meloxicam is a COX-2-preferential non-steroidal anti-inflammatory drug (NSAID) that is marketed in Canada. The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare genetic skeletal disorder. There are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available Canadian licence records |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Meloxicam is an NSAID that preferentially inhibits COX-2, which reduces prostaglandin-mediated inflammation and pain. Its usefulness for inflammatory and painful joint conditions is well known.

The predicted disease is a monogenic skeletal dysplasia caused by disruption of the CDMP1/GDF5 growth-factor pathway. Meloxicam has no known action on this pathway. At most, it might give symptomatic pain relief. The high TxGNN score likely reflects network-level associations in the knowledge graph, not a demonstrated biological link.

The other top-10 predictions are also mostly rare genetic skeletal or developmental syndromes with no plausible COX-inhibition link. Two are more credible:

- **Rheumatoid factor-positive polyarticular juvenile idiopathic arthritis (rank 8):** NSAIDs give direct symptomatic relief in JIA, and one indirect literature item exists (see below).
- **Spondyloarthropathy, susceptibility to (rank 6):** NSAIDs are first-line therapy for spondyloarthritis symptoms. This entry is a genetic-susceptibility label, so any assessment should target clinical axial SpA or ankylosing spondylitis instead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top-ranked prediction.

For context, the only literature item in the whole evidence pack concerns the rank 8 prediction (JIA). It is a 2014 Phase 4 registry study of celecoxib versus nonselective NSAIDs in JIA ([PMID 25057265](https://pubmed.ncbi.nlm.nih.gov/25057265/), *Pediatric Rheumatology Online Journal*). It is a cohort study. It is unconfirmed whether meloxicam was studied or whether the study was specific to RF-positive disease.

---

## Canada Market Information

Five of the 10 authorizations are listed below. Dosage form, manufacturer and approved-indication text are not recorded for these entries.

| DIN | Product Name |
|---------|------|
| 2353148 | MELOXICAM |
| 2258315 | TEVA-MELOXICAM |
| 2390884 | AURO-MELOXICAM |
| 2353156 | MELOXICAM |
| 2258323 | TEVA-MELOXICAM |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no trials or publications, and there is no plausible mechanistic link between COX inhibition and the GDF5 pathway disorder. Any benefit would be at most symptomatic pain relief.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Approved indication text and dosage forms for the Canadian licences
- Detailed mechanism of action data
- If the aim is symptomatic use in rheumatic conditions, redirect the assessment to better-supported candidates such as JIA (confirm whether meloxicam was studied and whether the label covers JIA) or clinical axial spondyloarthritis or ankylosing spondylitis

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

