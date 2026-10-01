---
layout: default
title: Octinoxate
parent: Model Prediction Only (L5)
nav_order: 669
evidence_level: L5
indication_count: 10
---

# Octinoxate
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

# Octinoxate: From Sun Protection (UV Filter) to Osteoarthritis

## One-Sentence Summary

Octinoxate is a topical UVB-filter cinnamate ester, found in sunscreen and cosmetic products marketed in Canada.
The TxGNN model predicts it may be effective for **osteoarthritis**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian licence records; used as a UVB sunscreen filter in topical products |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 98.93% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Octinoxate is a topical UVB-filter cinnamate ester with low systemic exposure. Its established role is photoprotection of the skin, and no pathway to cartilage or joint inflammation has been established.

The high TxGNN score reflects a knowledge-graph prediction only. The other top predictions are mostly skeletal or joint conditions (osteoarthritis susceptibility, rheumatoid arthritis, pseudoachondroplasia, gout, brachyolmia and others), which suggests the model is picking up a shared graph neighbourhood rather than a pharmacological link. A small-molecule UV filter has no plausible way to modify genetic susceptibility or rare monogenic skeletal dysplasias.

The one prediction with a conceptual angle is hepatic porphyria, where photoprotection might ease skin photosensitivity symptoms. Even that would be symptomatic rather than disease-modifying. Octinoxate absorbs mainly UVB, whereas porphyrin photosensitivity is driven largely by visible light, so protection would be limited.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2457458 | LISE WATIER CC CREME FPS 25 SPF | Not listed | Not listed |
| 2387018 | TRUE MATCH LUMI | Not listed | Not listed |
| 2404842 | ANTI-AGING COMPLEX EYE TREATMENT BROAD SPECTRUM SPF 15 | Not listed | Not listed |
| 2306441 | FLAWLESS EFFECT LIQUID FOUNDATION BROAD SPECTRUM SPF 15 | Not listed | Not listed |
| 2355302 | PREVAGE ANTI-AGING EYE CREAM SPF 15 | Not listed | Not listed |

Five of the 20 authorisations are shown. All are topical cosmetic or sun-protection products.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. No clinical trials or publications support it, and no mechanism links a topical UVB filter to osteoarthritis or any other predicted condition. The product is also a low-systemic-exposure topical agent, so route compatibility with joint disease is unresolved.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) to test any biological link to cartilage or joint inflammation
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Route and exposure compatibility assessment, since current products are topical with minimal systemic absorption
- Preclinical or published evidence for at least one predicted indication before reconsidering
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

