---
layout: default
title: Patisiran
parent: Model Prediction Only (L5)
nav_order: 704
evidence_level: L5
indication_count: 10
---

# Patisiran
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

# Patisiran: From hATTR Amyloidosis Polyneuropathy to Dermatitis

## One-Sentence Summary

Patisiran (ONPATTRO) is a liver-directed siRNA therapy. Based on general background knowledge, it is used for polyneuropathy of hereditary transthyretin-mediated (hATTR) amyloidosis, but the Evidence Pack does not list an approved indication.
The TxGNN model predicts it may be effective for **dermatitis**, but there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Evidence Pack (background knowledge: hATTR amyloidosis polyneuropathy) |
| Predicted New Indication | Dermatitis |
| TxGNN Prediction Score | 90.65% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on general background knowledge (not from the input data), patisiran is a lipid-nanoparticle siRNA that silences hepatic transthyretin (TTR) production. It is approved for hATTR amyloidosis polyneuropathy.

No mechanistic link between TTR silencing and inflammatory skin disease is supported by the available data, and no TTR-related pathway is evident in dermatitis. The score of 90.65% is a computational signal only. It most likely reflects proximity in the knowledge graph rather than established biology.

The other top-ranked predictions (for example hydroa vacciniforme, amyopathic dermatomyositis, acne keloid, and mastocytosis subtypes) show the same pattern. All have scores of about 0.85 to 0.91, no trials, no publications, and no supported mechanistic link. This clustering suggests a systematic model artifact rather than a genuine repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2489252 | ONPATTRO |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for patisiran.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical, literature, or mechanistic support (Evidence Level L5, decision stage S0). No plausible biological link exists between hepatic TTR silencing and dermatitis, so there is currently no basis to advance it.

**To proceed, the following is needed:**
- Mechanism of action data (DrugBank) and a documented rationale linking TTR silencing to skin inflammation
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- The approved indication text and dosage form for DIN 2489252
- Any preclinical or clinical signal for dermatitis (trials, case reports, or mechanistic studies)
- Route compatibility assessment (patisiran is given by intravenous infusion, and no route data are available for the predicted indication)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

