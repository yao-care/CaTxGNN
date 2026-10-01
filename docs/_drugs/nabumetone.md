---
layout: default
title: Nabumetone
parent: Model Prediction Only (L5)
nav_order: 633
evidence_level: L5
indication_count: 10
---

# Nabumetone
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

# Nabumetone: From NSAID Anti-Inflammatory Therapy to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Nabumetone is a non-steroidal anti-inflammatory drug (NSAID) that is currently marketed in Canada.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, but **no clinical trials and no publications** currently support this direction.
The prediction rests on the model score alone, and the mechanistic review found no plausible biological link.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

The pack contains no approved-indication text, so the original indication is not listed.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on the mechanistic review, nabumetone is an NSAID prodrug. Its active metabolite, 6-MNA, preferentially inhibits COX-2 and so reduces prostaglandin synthesis. This gives it anti-inflammatory and analgesic effects.

**The prediction for this disease is not mechanistically supported.** Acromesomelic dysplasia, Hunter-Thompson type, is a genetic skeletal dysplasia in the CDMP1/GDF5 pathway. COX inhibition does not act on that pathway. The high score (99.99%) is a knowledge-graph output only. Nothing in the pack shows nabumetone would change the course of this disease.

The other top-10 predictions are also weak. Most are rare genetic skeletal or developmental disorders, such as brachyolmia, pseudoachondroplasia and WHIM syndrome, where there is no plausible link. Two are more credible because they are related to inflammatory arthritis:
- **Spondyloarthropathy, susceptibility to** (rank 8, score 99.94%): NSAIDs are general first-line symptomatic therapy in spondyloarthritis, and nabumetone shares that class mechanism. The listed entity is a genetic susceptibility term, not a treatable clinical condition. This is the best candidate for a follow-up literature search.
- **Rheumatoid nodulosis** (rank 10, score 99.93%): NSAIDs are used symptomatically in rheumatoid arthritis, but they are not known to modify nodule formation.

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
| 2238639 | NABUMETONE |

Dosage form, manufacturer and approved-indication text were not available for this license.

---

## Safety Considerations

Please refer to the package insert for safety information. The pack has no warnings or contraindications, and the drug-interaction query returned no results.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is at evidence level L5, with no trials, no literature and no plausible mechanistic link to this genetic skeletal dysplasia. A high model score alone does not justify moving forward.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking gap, needed before safety screening)
- Structured mechanism-of-action data (for example, from DrugBank)
- A targeted literature search for nabumetone in spondyloarthritis, the most credible candidate
- Approved-indication and dosage-form data for the Canadian license

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

