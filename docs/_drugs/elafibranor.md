---
layout: default
title: Elafibranor
parent: 僅模型預測 (L5)
nav_order: 253
evidence_level: L5
indication_count: 1
---

# Elafibranor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Elafibranor: From NASH/PBC to Amenorrhea

## One-Sentence Summary

Elafibranor is a dual PPAR-α/δ agonist originally developed for non-alcoholic steatohepatitis (NASH) and primary biliary cholangitis (PBC), receiving FDA approval for PBC in 2024 under the brand name Iqirvo.
The TxGNN model predicts it may be effective for **Amenorrhea**, however, there are currently **no clinical trials** and **no publications** supporting this direction.
At L5 evidence (model prediction only), this candidate is not ready to advance without further biological validation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Non-alcoholic steatohepatitis (NASH) / Primary biliary cholangitis (PBC) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism of action data is not available in the current Evidence Pack. Based on published information, elafibranor is a dual PPAR-α/δ agonist: the PPAR-α component primarily drives fatty acid β-oxidation in the liver, reducing hepatic lipid accumulation; the PPAR-δ component modulates systemic energy metabolism and mitochondrial biogenesis. These properties underlie its approved use in primary biliary cholangitis and its investigational use in NASH.

The proposed mechanistic bridge to amenorrhea is built on a single, highly indirect chain: PPAR-δ activation promotes a positive energy balance → this may theoretically relieve the energy-deficit state that suppresses hypothalamic GnRH pulsatility → restoration of GnRH pulses could re-establish ovulatory cycles in functional hypothalamic amenorrhea (FHA). FHA is indeed driven by chronic energy deficit (e.g., in athletes or patients with eating disorders), so the metabolic angle is not entirely without logic.

However, this pathway has not been tested in any animal model or in vitro system. No published data links elafibranor, or any PPAR-δ agonist, to HPG axis regulation, gonadotropin secretion, or menstrual cycle restoration. The exceptionally high TxGNN score (0.9986) most likely reflects non-specific co-embedding of "energy metabolism dysregulation" nodes that are shared across multiple gynaecological phenotypes in the knowledge graph, rather than a direct pharmacological relationship. This is a hypothesis-generating signal, not a validated biological link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Elafibranor is not currently authorised for sale in Canada. No DINs have been issued and no product monographs are on file. Regulatory submissions would be required before any Canadian use.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN score, the mechanistic connection between a hepatic lipid-metabolism drug and amenorrhea is indirect and entirely unvalidated; with zero supporting clinical trials or publications (L5 evidence), there is insufficient biological justification to invest in clinical development at this stage.

**To proceed, the following is needed:**

- **Preclinical mechanistic validation**: Test whether PPAR-δ activation restores GnRH pulsatility in established rodent models of functional hypothalamic amenorrhea (e.g., energy-restricted or exercise-induced anovulation models)
- **HPG axis literature review**: Conduct a systematic review of PPAR-δ agonism and hypothalamic-pituitary-gonadal axis signalling to assess biological plausibility before any in vivo work
- **MOA data gap resolution**: Retrieve full DrugBank mechanistic profile (DB05187) to identify any secondary targets relevant to reproductive endocrinology
- **Safety and contraindication review**: Obtain and parse the full Iqirvo prescribing information, specifically reproductive-toxicity and endocrine-related warnings, as these are currently unavailable
- **Knowledge graph audit**: Verify whether the TxGNN score reflects a drug-specific signal or a class-level artefact shared across all PPAR agonists, to determine whether this prediction is worth prioritising over competing candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

