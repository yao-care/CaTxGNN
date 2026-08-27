---
layout: default
title: Mirtazapine
parent: 僅模型預測 (L5)
nav_order: 429
evidence_level: L5
indication_count: 3
---

# Mirtazapine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Mirtazapine: From Depression to Ohdo Syndrome and Variants

## One-Sentence Summary

Mirtazapine is a noradrenergic and specific serotonergic antidepressant (NaSSA), primarily used for the treatment of major depressive disorder.
The TxGNN model predicts it may be effective for **Ohdo Syndrome and Variants**, a rare X-linked neurodevelopmental disorder,
however with **0 clinical trials** and **0 publications** currently supporting this direction, the evidence base is entirely absent.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Major depressive disorder |
| Predicted New Indication | Ohdo Syndrome and Variants |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on known pharmacological information, mirtazapine is a centrally acting presynaptic α2-adrenergic receptor antagonist that also blocks postsynaptic 5-HT2A, 5-HT2C, 5-HT3, and H1 receptors. Its clinical utility in depression arises from enhanced noradrenergic and serotonergic neurotransmission, along with sedating properties mediated via histamine H1 blockade.

Ohdo Syndrome and its variants are X-linked rare neurodevelopmental disorders caused by loss-of-function mutations in transcriptional regulatory genes — primarily *MED12*, *KAT6A*, and *MED13L* — which govern chromatin remodeling and transcription factor activity. The molecular pathology of these disorders (histone acetyltransferase dysfunction, Mediator complex disruption) operates at the epigenetic and transcriptional level, which has no established intersection with mirtazapine's receptor pharmacology targets (α2, 5-HT, H1).

The high TxGNN score (0.9942) in this case most likely reflects a topological clustering effect in the knowledge graph — specifically, mirtazapine's node proximity to the "rare neurodevelopmental disease" cluster — rather than a genuine biological repurposing rationale. This prediction should be interpreted as a model artifact rather than a clinically actionable hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Mirtazapine currently holds no Drug Identification Numbers (DINs) in Canada and is not marketed in this jurisdiction. No license records are available for tabulation.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model produces a high numerical score for mirtazapine → Ohdo Syndrome, but the mechanistic rationale analysis identifies this as a probable knowledge graph topology artifact with no biological plausibility: mirtazapine's receptor-level pharmacology (α2/5-HT/H1 antagonism) has no established connection to the chromatin remodeling and transcription factor pathways that are disrupted in Ohdo Syndrome. With zero supporting clinical trials and zero publications, and the drug not currently marketed in Canada, there is insufficient basis to advance this candidate.

**To proceed, the following is needed:**

- **Mechanistic evidence**: Identification of any credible molecular link between mirtazapine's pharmacological targets and *MED12/KAT6A/MED13L* pathway dysfunction before this candidate can leave L5 status
- **MOA data**: Complete DrugBank API query to obtain full mechanism of action, receptor binding profile, and off-target activity data (resolves DG002)
- **Safety package**: Retrieval and parsing of the Health Canada product monograph or equivalent package insert to populate key warnings and contraindications (resolves DG001)
- **Knowledge graph audit**: Investigate whether the high TxGNN score reflects a genuine signal or a known topological bias for rare neurodevelopmental disease nodes — if a systematic bias is confirmed, this candidate family should be flagged for de-prioritization across the pipeline
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

