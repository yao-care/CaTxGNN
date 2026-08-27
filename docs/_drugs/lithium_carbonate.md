---
layout: default
title: Lithium Carbonate
parent: 僅模型預測 (L5)
nav_order: 393
evidence_level: L5
indication_count: 10
---

# Lithium Carbonate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Lithium Carbonate: From Bipolar Disorder to Pseudoachondroplasia

## One-Sentence Summary

Lithium carbonate is a long-established mood stabilizer used for bipolar disorder (mania), acting in part through inhibition of GSK-3β and downstream Wnt/β-catenin signaling. The TxGNN model predicts it may be effective for **Pseudoachondroplasia**, a rare skeletal dysplasia, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack itself flags the mechanistic rationale as speculative.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bipolar disorder (mood stabilizer) — based on established pharmacological knowledge; no Health Canada license/indication text was available in this dataset |
| Predicted New Indication | Pseudoachondroplasia |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, drug-specific mechanism-of-action data was not available in this evidence pack (flagged as a High-severity data gap requiring DrugBank verification). Based on general pharmacological knowledge, lithium carbonate is a mood-stabilizing agent whose efficacy in bipolar disorder is well established; one of its known cellular effects is inhibition of glycogen synthase kinase-3β (GSK-3β), which activates the Wnt/β-catenin signaling pathway — a pathway also involved in chondrocyte differentiation and cartilage development.

This is the theoretical bridge TxGNN appears to be drawing on: bipolar disorder (a neuropsychiatric target of lithium) and pseudoachondroplasia (a skeletal dysplasia) are not obviously related clinically, but Wnt/β-catenin signaling touches both neuronal and skeletal biology, which may explain why the model assigns a very high similarity score (rank 825 out of the full candidate list).

However, the evidence pack's own mechanistic assessment is candid that this link is weak: pseudoachondroplasia is caused primarily by mutations in the *COMP* gene, leading to misfolded cartilage oligomeric matrix protein accumulating in the endoplasmic reticulum and triggering chondrocyte apoptosis — a **structural protein-folding disorder**, not a signaling-pathway disorder. Lithium's GSK-3β/Wnt activity has no established role in correcting protein misfolding or ER stress of this type. As a result, this prediction should be treated as a high-scoring but mechanistically unproven hypothesis rather than a validated repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Lithium carbonate is currently listed as **not marketed** in this dataset, with 0 registered DINs and no license records. No Health Canada authorization or indication text is available for extraction.

---

## Safety Considerations

Detailed prescribing information — including key warnings, contraindications, and drug interaction data — was not available for lithium carbonate in this evidence pack. Please refer to the package insert for safety information before any clinical consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns pseudoachondroplasia a very high similarity score (99.98%), the evidence pack itself identifies the mechanistic rationale as speculative — pseudoachondroplasia is a structural protein-misfolding disease, not a signaling-pathway disorder that lithium's known GSK-3β/Wnt activity would be expected to address. With zero clinical trials, zero publications, and evidence level L5 (model prediction only), there is currently no empirical basis to support this specific indication.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data for lithium carbonate from DrugBank (currently a data gap)
- TFDA/Health Canada prescribing information (warnings, contraindications, DDI) — currently a blocking data gap for any safety assessment
- Preclinical evidence evaluating whether Wnt/β-catenin modulation has any measurable effect on COMP-related chondrocyte apoptosis
- Consideration of other candidates in this same prediction set with comparatively stronger mechanistic plausibility, which may warrant prioritization over pseudoachondroplasia:
  - **WHIM syndrome** (rank 9) — lithium has well-documented, long-observed neutrophil-mobilizing effects (historically used for chemotherapy-induced neutropenia), which map more directly onto WHIM's CXCR4-driven neutrophil retention defect (myelokathexis) than the pseudoachondroplasia link does
  - **Brachyolmia-amelogenesis imperfecta syndrome** (rank 6) — supported by one review-level publication ([PMID 31888683](https://pubmed.ncbi.nlm.nih.gov/31888683/)) and a biologically coherent rationale involving Wnt-pathway roles in both cartilage and enamel mineralization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

