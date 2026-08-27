---
layout: default
title: Hemin
parent: 僅模型預測 (L5)
nav_order: 378
evidence_level: L5
indication_count: 10
---

# Hemin
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

# Hemin: From Acute Porphyria (Heme Replacement Therapy) to Thrombocytopenic Purpura

## One-Sentence Summary

Hemin is a heme-replacement agent known pharmacologically for use in acute hepatic porphyria (no formal original-indication or Canadian regulatory record is on file for this candidate). The TxGNN model's top-ranked prediction for Hemin is **Thrombocytopenic Purpura**, with a very high prediction score (99.79%), but this signal is currently supported by **0 clinical trials** and **0 publications** — it is a pure model-based hypothesis with no direct evidence located to date.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally documented (no Canadian market authorization on file); known pharmacological use is acute hepatic porphyria (heme replacement therapy) |
| Predicted New Indication | Thrombocytopenic Purpura |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The formal mechanism-of-action field for this candidate is flagged as a data gap. Based on known pharmacology of hemin (referenced within this evidence pack's own analysis of related candidates), its established action is to replenish intracellular heme, which feedback-inhibits hepatic ALAS1 (δ-aminolevulinic acid synthase 1) — the rate-limiting enzyme in heme biosynthesis — thereby reducing accumulation of neurotoxic porphyrin precursors in acute porphyria. Hemin also induces heme oxygenase-1 (HO-1), an enzyme with antioxidant, anti-inflammatory, and vascular endothelial-protective properties.

TxGNN's top-ranked hypothesis links Hemin to Thrombocytopenic Purpura, plausibly via HO-1's endothelial-protective effects, since endothelial injury contributes to the pathophysiology of thrombotic microangiopathies such as TTP. However, no clinical trials or literature evidence were retrieved to substantiate this specific link. Importantly, the evidence pack's own mechanistic review flags a significant caution: free heme (hemin) is a known damage-associated molecular pattern (DAMP) that can activate platelets, endothelium, and the coagulation cascade — a pro-thrombotic, pro-inflammatory action that may run counter to, rather than support, treatment of a thrombotic/consumptive platelet disorder like TTP. The mechanistic direction is therefore uncertain and possibly contradictory.

For reference, among the other nine TxGNN-predicted indications for Hemin, only "hemophilia" (rank 2, score 99.72%) has any literature support at all — four PMIDs, of which just one (PMID 19890094, a preclinical FVIII-deficient mouse study) offers indirect mechanistic relevance via HO-1-mediated immune modulation; the remaining three concern a different drug (givosiran) for a different disease (acute hepatic porphyria) and are not directly relevant. This underscores that Hemin's current predicted-indication set is largely unvalidated model output, and the top-ranked TTP signal in particular has no supporting evidence of any kind.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Hemin currently has no Health Canada market authorization on file (0 DINs; market status: Not Marketed). No product-level information is available for this jurisdiction.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (Thrombocytopenic Purpura) is supported only by the TxGNN model score, with zero clinical trials or literature evidence, and the proposed mechanism may plausibly run counter to the therapeutic goal given hemin's known pro-thrombotic/pro-inflammatory DAMP activity.
- The drug is not currently marketed in Canada, and a blocking data gap (missing official warnings/contraindications, DG001) prevents even an initial safety screen (S1).

**To proceed, the following is needed:**
- Official package insert / regulatory warnings and contraindications (resolves blocking gap DG001)
- Confirmed, sourced mechanism-of-action documentation (resolves high-priority gap DG002)
- Preclinical or in vitro evidence specifically testing hemin/HO-1 induction in TTP or thrombotic microangiopathy models
- Drug interaction data (current query returned no results)
- Continued monitoring of the secondary "hemophilia" signal (rank 2, evidence level L4, decision stage S1), which has weak but more concrete mechanistic support and may warrant a dedicated research-question review before this Thrombocytopenic Purpura signal is revisited
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

