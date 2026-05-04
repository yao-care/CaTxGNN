---
layout: default
title: Menotropins
parent: 僅模型預測 (L5)
nav_order: 301
evidence_level: L5
indication_count: 10
---

# Menotropins
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

# Menotropins: From Infertility to Peptic Esophagitis

## One-Sentence Summary

Menotropins is a combination gonadotropin preparation (FSH + LH), primarily used in reproductive medicine to treat infertility and hypogonadotropic hypogonadism by stimulating gonadal hormone production.
The TxGNN model predicts it may have potential in **Peptic Esophagitis** with a score of **98.44%**, yet **no clinical trials** and **no supporting publications** currently exist for this indication.
The overall prediction landscape for Menotropins shows a striking clustering of esophageal and cardiac conduction disorders across all top 10 results, strongly suggesting a knowledge-graph artefact rather than genuine biological signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Infertility / Hypogonadotropic Hypogonadism (no approved indication on record in Canada) |
| Predicted New Indication | Peptic Esophagitis |
| TxGNN Prediction Score | 98.44% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on known pharmacology, Menotropins is a purified preparation of human menopausal gonadotropins containing both follicle-stimulating hormone (FSH) and luteinizing hormone (LH). It acts on FSH and LH receptors in the gonads to stimulate follicular development and estrogen/progesterone synthesis in women, and testosterone production and spermatogenesis in men. Its therapeutic use is tightly confined to the reproductive axis.

Peptic esophagitis is driven by acid-mediated mucosal damage to the esophageal lining — typically from gastroesophageal reflux, H. pylori infection, or chemical injury. There is no established pharmacological pathway connecting FSH/LH receptor signalling to gastric acid regulation, lower esophageal sphincter tone, or esophageal mucosal defence mechanisms. The evidence pack's own mechanistic analysis concludes that "no known mechanistic link connects gonadotropins to esophageal mucosal acid injury or gastric acid secretion," and that the high TxGNN score likely reflects knowledge-graph noise rather than a true biological relationship.

A notable pattern across the top 10 predictions is that four of the highest-ranked indications involve esophageal pathology (peptic esophagitis, esophageal disease, non-syndromic esophageal malformation, esophageal ulcer), and four involve cardiac conduction abnormalities (His bundle tachycardia, sinoatrial block, progressive familial heart block, sinoatrial node disease). This systematic clustering is inconsistent with the narrow reproductive-axis pharmacology of Menotropins and is more consistent with high-connectivity node bias in the knowledge graph than with genuine repurposing potential.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top predicted indication (peptic esophagitis).

> **Note:** One tangentially related case series was identified for the rank-4 prediction (Raynaud Disease):
>
> | PMID | Year | Type | Journal | Key Findings |
> |------|------|------|---------|-------------|
> | [3117594](https://pubmed.ncbi.nlm.nih.gov/3117594/) | 1987 | Case Series | Fertility and Sterility | Two infertile women on bromocriptine (5–7.5 mg/day) developed cold-induced digital vasospasm (Raynaud's phenomenon). Reports a potential adverse effect of bromocriptine — not a therapeutic effect of Menotropins. |
>
> This publication describes a side effect of a co-administered dopamine agonist (bromocriptine), not a therapeutic effect of Menotropins, and does not support repurposing.

---

## Canada Market Information

Menotropins is not currently marketed in Canada. No Drug Identification Numbers (DINs) are registered, and no approved product monographs are available through Health Canada's drug database.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data (key warnings, contraindications, and drug-drug interactions) were not retrievable in this evidence pack. Full safety review requires downloading and parsing the product monograph from the relevant regulatory authority before any further evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Every top-10 prediction for Menotropins carries an L5 evidence rating with zero clinical trial or literature support, and the predicted conditions — esophageal disorders and cardiac conduction abnormalities — have no established mechanistic connection to FSH/LH pharmacology. The systematic clustering pattern across predictions is a strong indicator of knowledge-graph structural bias rather than actionable repurposing signal.

**To proceed, the following is needed:**
- Retrieve the complete drug monograph / package insert to establish a baseline safety profile before any S1 safety screening can occur
- Query DrugBank (DB00032) for full mechanism of action data to enable rigorous plausibility assessment
- Investigate whether the esophageal and cardiac node clustering in TxGNN reflects a systematic upstream model bias (high node connectivity artefact) that should be corrected in the knowledge graph before further candidate generation
- If continued evaluation is desired, deprioritise all 10 current candidates and re-run prediction with bias-corrected graph or alternative scoring thresholds
- Consider whether Menotropins' known reproductive pharmacology could instead be evaluated against endocrine or reproductive disease indications not currently appearing in the top predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

