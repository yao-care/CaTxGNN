---
layout: default
title: Tiaprofenic Acid
parent: Model Prediction Only (L5)
nav_order: 905
evidence_level: L5
indication_count: 10
---

# Tiaprofenic Acid
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

# Tiaprofenic Acid: From Anti-Inflammatory (NSAID) Use to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Tiaprofenic acid is a nonsteroidal anti-inflammatory drug (NSAID) that is currently marketed in Canada. The TxGNN model predicts it may be effective for **brachydactyly-syndactyly syndrome**, a congenital limb malformation, but **0 clinical trials** and **0 publications** support this prediction. It is a computational signal only and is not credible on mechanistic grounds.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Tiaprofenic acid belongs to the NSAID class, which acts by inhibiting cyclooxygenase (COX). This is a class-level assumption, not confirmed by the supplied data. The Canadian licence records also contain no approved indication text.

On this basis the prediction is **not credible**. Brachydactyly-syndactyly syndrome is a congenital limb malformation of developmental genetic origin. An NSAID would not be expected to alter a structural developmental defect. The high score (0.9999, model rank 259) is most likely an artifact of the knowledge graph.

The other nine top-ranked predictions show the same pattern. Most are rare genetic skeletal or developmental disorders (such as brachyolmia and pseudoachondroplasia) or thrombophilias (factor 5 excess, heparin cofactor 2 deficiency). None has a plausible link to COX inhibition, and none has any trial or literature support.

The one exception is **spondyloarthropathy, susceptibility to** (rank 6, score 99.99%). NSAIDs are widely used for symptom control in inflammatory spondyloarthropathies. However, this entry is a genetic susceptibility term rather than a treatable clinical condition, and the supplied data contain no evidence for tiaprofenic acid in it. It is flagged as a research question only.

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
| 2179679 | TEVA-TIAPROFENIC ACID |
| 2179687 | TEVA-TIAPROFENIC ACID |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score, with no trials, no literature and no plausible mechanism for a congenital limb malformation. Evidence is at L5, the lowest level.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for any safety screening)
- Mechanism of action data from DrugBank
- A targeted literature search on tiaprofenic acid in spondyloarthritis and ankylosing spondylitis, the only candidate with a plausible class-level rationale
- Confirmation of the approved indications and dosage forms for the two Canadian DINs

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

