---
layout: default
title: Finasteride
parent: Model Prediction Only (L5)
nav_order: 385
evidence_level: L5
indication_count: 6
---

# Finasteride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Finasteride: From Established Androgen-Dependent Uses to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Finasteride is a 5-alpha reductase inhibitor. The Evidence Pack does not list its approved indications, but its known hair-related use is in androgen-dependent conditions such as male pattern hair loss.
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.
The mechanistic assessment suggests the prediction is unlikely to hold.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Evidence Pack (all Canadian license entries have empty indication text) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the database. Based on general pharmacology, finasteride inhibits type II/III 5-alpha reductase and lowers scalp and serum dihydrotestosterone (DHT). This is why it is used in androgen-dependent hair and prostate conditions.

The link to the predicted indication is weak. Ambras syndrome is a congenital condition associated with genomic rearrangements at 8q22 that alter TRPS1 regulation. It is not androgen-dependent, so lowering DHT is unlikely to reverse it. The high graph score probably reflects shared hair-related nodes in the knowledge graph rather than a real biological connection.

Overall, the mechanistic plausibility is low, and the score should be read as a model artifact until evidence shows otherwise.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Health Canada lists 20 licenses in total. Dosage form, manufacturer and indication text are not recorded for the entries below.

| DIN | Product Name |
|---------|------|
| 2339471 | SANDOZ FINASTERIDE A |
| 2389878 | MINT-FINASTERIDE |
| 2348500 | TEVA-FINASTERIDE |
| 2374404 | AG-FINASTERIDE |
| 2322579 | SANDOZ FINASTERIDE |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5). The proposed indication is a congenital, non-androgen-dependent condition, so finasteride's DHT-lowering mechanism offers no clear basis for benefit.

The other predictions for this drug are no stronger:
- **Hypertrichosis (rank 2):** Evidence is indirect (L4). The one registered trial (NCT04293822, Phase 4, n=60) studies topical cetirizine versus minoxidil in androgenetic alopecia, not finasteride. The four retrieved reviews cover hair disorders in general and do not show finasteride efficacy in hypertrichosis. Androgen-dependent hirsutism is the more plausible neighbouring target and would need to be separated from true hypertrichosis.
- **Periodontal/dental malformation syndrome (rank 3):** The retrieved literature is general periodontitis material that never mentions finasteride, and no mechanistic link was found.
- **Dandy-Walker syndrome, isolated genetic hair shaft abnormality and familial isolated trichomegaly (ranks 4–6):** Prediction only, with no plausible biological rationale.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data from DrugBank
- Approved indication text for the Canadian licenses, to confirm the original indication
- For any follow-up, a drug-specific literature search for finasteride in hirsutism, which is a better-founded question than the top-ranked prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

