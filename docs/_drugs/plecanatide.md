---
layout: default
title: Plecanatide
parent: Model Prediction Only (L5)
nav_order: 738
evidence_level: L5
indication_count: 10
---

# Plecanatide
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

# Plecanatide: From Chronic Idiopathic Constipation to Hypertrichosis

## One-Sentence Summary

Plecanatide is a locally acting gut drug (a guanylate cyclase-C agonist) marketed in Canada as TRULANCE. The Evidence Pack does not record its approved indication, so the original use shown here (chronic idiopathic constipation) is general knowledge, not pack data. The TxGNN model predicts it may be effective for **hypertrichosis**, but there are **0 clinical trials** and **0 publications** supporting this direction, so it rests on a graph-based prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Canadian licence data (generally known as chronic idiopathic constipation) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the input. Plecanatide is known to be a guanylate cyclase-C agonist that acts locally in the gut with minimal systemic absorption. It raises intestinal cGMP signalling.

No plausible mechanism connects this action to hair follicle biology. Hypertrichosis is excess hair growth. Because plecanatide is barely absorbed, it is not expected to reach hair follicles in meaningful amounts. The high score (99.998%, model rank 111) is a statistical output of the knowledge graph, not evidence of a real drug-disease link.

The other nine predictions in the pack show the same pattern. They include Ambras-type hypertrichosis, hair shaft abnormalities, a Dandy-Walker malformation syndrome, coronary artery dissection, vascular disease, thoracic outlet syndromes and phaeochromocytoma. All are L5 with no trials, and none has a plausible gut-restricted mechanism. Only the periodontal malformation prediction has literature, and those papers are general periodontitis papers that never mention plecanatide.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2493012 | TRULANCE | — | — |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for plecanatide in the queried source.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical, registry or literature support, and its mechanism is implausible for a gut-restricted drug with minimal systemic absorption. The score alone does not justify further investment.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text, dosage form and manufacturer for the Canadian licence
- Mechanism-of-action data from DrugBank
- At least preclinical or mechanistic evidence linking GC-C/cGMP signalling to hair follicle biology
- Evidence that systemic or topical exposure sufficient for a hair effect is achievable (route compatibility is currently unassessed)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

