---
layout: default
title: Auranofin
parent: 僅模型預測 (L5)
nav_order: 75
evidence_level: L5
indication_count: 2
---

# Auranofin
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

# Auranofin: From Rheumatoid Arthritis to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Auranofin is an oral gold compound originally approved for the treatment of rheumatoid arthritis.
The TxGNN model predicts it may be effective for **colobomatous microphthalmia-rhizomelic dysplasia syndrome**,
however there are currently **0 clinical trials** and **0 publications** supporting this direction — this prediction is based entirely on model inference.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rheumatoid arthritis |
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known information, Auranofin is an organogold compound whose pharmacological activity is thought to involve inhibition of thioredoxin reductase (TrxR), suppression of NF-κB-mediated inflammation, and modulation of mitochondrial oxidative stress pathways. These effects underpin its efficacy in rheumatoid arthritis.

Colobomatous microphthalmia-rhizomelic dysplasia syndrome is a highly rare congenital genetic disorder characterised by ocular defects (coloboma, microphthalmia) combined with limb-skeletal abnormalities (rhizomelic dysplasia). Its pathogenesis is driven by mutations in developmental genes such as *PAX2*, *CHD7*, *GDF3*, and *ALDH1A3* — none of which are known to interact meaningfully with Auranofin's anti-inflammatory or redox-regulatory mechanisms.

There is no plausible mechanistic bridge between Auranofin's known biology and the gene-level developmental defects that define this syndrome. The high TxGNN score most likely reflects network proximity artefacts within the knowledge graph — rare disease nodes that cluster near well-connected drug nodes without representing genuine biological relationships. This prediction should be treated as a computational signal requiring substantial mechanistic validation before any further consideration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Auranofin is currently not approved or marketed in Canada. No Drug Identification Numbers (DINs) are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction carries no supporting clinical or preclinical evidence (Evidence Level L5), and the mechanistic rationale explicitly identifies the high TxGNN score as likely arising from knowledge graph network artefacts rather than true biological relevance. Auranofin's known mechanisms — TrxR inhibition, NF-κB suppression, and mitochondrial redox modulation — have no established connection to the genetic developmental pathways disrupted in colobomatous microphthalmia-rhizomelic dysplasia syndrome.

**To proceed, the following would be needed:**

- Identification of a credible mechanistic hypothesis linking Auranofin's pharmacology to *PAX2*, *CHD7*, *GDF3*, or *ALDH1A3* pathway biology
- Any published preclinical or in vitro evidence (cell/animal models) connecting gold compounds or TrxR inhibition to ocular or skeletal developmental outcomes
- Formal MOA data from DrugBank to rule out any indirect mechanistic connections not yet captured
- Safety profile documentation (package insert warnings, contraindications, DDI data) before any further evaluation
- Regulatory status clarification for Canada should this ever advance beyond the exploratory stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

