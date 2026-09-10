---
layout: default
title: Leflunomide
parent: 僅模型預測 (L5)
nav_order: 452
evidence_level: L5
indication_count: 2
---

# Leflunomide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Leflunomide: From Rheumatoid Arthritis to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Leflunomide is a DHODH-inhibiting immunomodulator conventionally used to treat rheumatoid arthritis. The TxGNN model predicts potential efficacy for **Brachydactyly-Syndactyly Syndrome**, a congenital limb malformation disorder, but this prediction is currently supported by **zero clinical trials** and **zero publications** — the mechanism of action does not plausibly connect to the target disease's developmental biology.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file for Canada (drug not marketed); clinically used for rheumatoid arthritis |
| Predicted New Indication | Brachydactyly-Syndactyly Syndrome |
| TxGNN Prediction Score | 99.93% (rank 1959 among all candidates) |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Leflunomide is a DHODH (dihydroorotate dehydrogenase) inhibitor that blocks de novo pyrimidine synthesis, producing an antiproliferative and immunomodulatory effect used clinically to manage rheumatoid arthritis.

Brachydactyly-syndactyly syndrome is a congenital limb malformation disorder (shortened digits fused together) arising from dysregulation of embryonic limb-patterning pathways (e.g., HOX, BMP, SHH signaling), not from inflammation or immune dysfunction. There is no established mechanistic link between pyrimidine-synthesis inhibition/lymphocyte suppression and limb morphogenesis pathways.

Given the complete absence of clinical trials or literature connecting these two entities, the high TxGNN score most likely reflects sparse graph connectivity around this rare-disease node (an artifact of embedding distance in a data-poor region of the knowledge graph) rather than genuine biological plausibility. Notably, the rank-2 candidate (colobomatous microphthalmia-rhizomelic dysplasia syndrome, score 99.93%) shows the identical pattern — another rare congenital developmental syndrome with no trial or literature support — reinforcing that this is likely a systematic artifact rather than an isolated signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Leflunomide currently holds no Health Canada Drug Identification Numbers (DINs); market status is not marketed in Canada, so no product/dosage-form information is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction sits at evidence level L5/decision stage S0 with no clinical, trial, or literature support, and the proposed mechanism (pyrimidine-synthesis inhibition/immunomodulation) has no known connection to the congenital limb-malformation pathophysiology of the target disease. The drug is also not marketed in Canada, so there is no regulatory pathway currently open.

**To proceed, the following is needed:**
- Confirmed drug label / official MOA documentation (currently a data gap)
- Health Canada or TFDA safety labeling (warnings, contraindications) to clear the S1 safety gate
- A mechanistic plausibility review by clinical genetics/developmental biology expertise before any preclinical or clinical follow-up is considered
- Re-evaluation if new literature, case reports, or trials emerge linking DHODH-pathway modulation to limb-patterning disorders
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

