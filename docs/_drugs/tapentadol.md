---
layout: default
title: Tapentadol
parent: 僅模型預測 (L5)
nav_order: 748
evidence_level: L5
indication_count: 3
---

# Tapentadol
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

# Tapentadol: From Pain Management to Migraine Disorder

## One-Sentence Summary

> Tapentadol is a μ-opioid receptor agonist / noradrenaline reuptake inhibitor (MOR-NRI) established in pain management, though detailed original-indication and MOA data are not present in the current dataset.
> The TxGNN model predicts it may be effective for **Migraine Disorder**,
> with **0 clinical trials** and **2 tangentially related publications** currently identified — neither of which discusses tapentadol directly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in dataset (general pharmacological knowledge: pain management) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 (model prediction only, no direct supporting studies) |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured dataset. Based on known pharmacology, tapentadol is a μ-opioid receptor agonist combined with a noradrenaline reuptake inhibitor (MOR-NRI). In theory, this dual analgesic mechanism could be extended to acute migraine pain — which is the basis for the TxGNN association score of 0.9967.

However, this score is a pure knowledge-graph prediction. The two literature records retrieved for this pairing discuss **dipyrone (metamizole)** and **sumatriptan plus naproxen** for migraine treatment — neither paper mentions tapentadol. These appear to be disease-keyword matches rather than direct evidence for this drug.

More importantly, international headache guidelines (AHS/AAN) explicitly **do not recommend opioids as first-line acute migraine therapy**, given inferior efficacy versus triptans/NSAIDs and the well-documented risk of medication-overuse headache (MOH). In this case, the mechanistic rationale should be read as a **negative signal** rather than support for repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27096578](https://pubmed.ncbi.nlm.nih.gov/27096578/) | 2016 | Review | Cochrane Database of Systematic Reviews | Evaluates dipyrone (metamizole), not tapentadol, for postoperative/migraine pain; indirect keyword match only |
| [27096438](https://pubmed.ncbi.nlm.nih.gov/27096438/) | 2016 | Review | Cochrane Database of Systematic Reviews | Evaluates sumatriptan plus naproxen for acute migraine; does not reference tapentadol or opioid mechanisms |

---

## Canada Market Information

Tapentadol currently holds **no active Health Canada market authorization** in this dataset (0 DINs, market status: Not Marketed). No product licenses are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The migraine association rests solely on a TxGNN knowledge-graph score with no direct clinical trial or literature evidence for tapentadol in this indication. Retrieved literature discusses unrelated drugs, and established headache-society guidance treats opioid-based therapy as a negative signal for acute migraine, not a supporting rationale.

**To proceed, the following is needed:**
- Confirmed original indication and DrugBank MOA data (currently flagged as Blocking/High data gaps)
- Health Canada regulatory status and safety labeling (warnings, contraindications, DDI)
- Direct tapentadol-specific clinical or preclinical evidence in migraine before advancing past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

