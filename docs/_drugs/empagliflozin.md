---
layout: default
title: Empagliflozin
parent: 僅模型預測 (L5)
nav_order: 277
evidence_level: L5
indication_count: 3
---

# Empagliflozin
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

The data-report skill governs CLI output — not applicable here since the Evidence Pack was provided directly. Proceeding with the evaluation report.

---

# Empagliflozin: From Type 2 Diabetes to Classic Stiff Person Syndrome

## One-Sentence Summary

Empagliflozin is a selective SGLT2 (sodium-glucose cotransporter-2) inhibitor approved globally for type 2 diabetes mellitus, heart failure, and chronic kidney disease, though it currently holds no registered product in Taiwan.
The TxGNN model predicts it may be effective for **Classic Stiff Person Syndrome**,
however, with **0 clinical trials** and **0 publications** currently supporting this direction, the evidence base consists of model prediction only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan; globally approved for type 2 diabetes mellitus, heart failure, chronic kidney disease |
| Predicted New Indication | Classic Stiff Person Syndrome |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Empagliflozin is a selective inhibitor of sodium-glucose cotransporter-2 (SGLT2) in the renal proximal tubule, which promotes urinary glucose excretion and reduces plasma glucose independently of insulin. Its downstream effects include ketone body elevation (particularly β-hydroxybutyrate), reduced inflammation via NF-κB inhibition, and lower circulating levels of IL-6 and TNF-α.

Classic Stiff Person Syndrome (SPS) is a rare autoimmune neurological disorder driven by GAD65 antibodies that attack GABAergic inhibitory neurons, resulting in progressive axial rigidity and episodic painful spasms. The theoretical link proposed by the TxGNN knowledge graph is indirect: elevated β-hydroxybutyrate from SGLT2 inhibition may confer neuroprotective and HDAC inhibitory effects that could support GABA neurotransmission, while the anti-inflammatory profile of Empagliflozin might attenuate the neuroinflammatory component of SPS.

However, these proposed mechanisms do not address the core autoimmune pathology (anti-GAD65 antibody-mediated destruction of GABAergic neurons), making the mechanistic link highly speculative. The identical TxGNN scores for Classic SPS and Focal Stiff Limb Syndrome (both 0.9906) further indicate that these predictions share the same knowledge graph node cluster rather than representing independent, disease-specific signals. No preclinical cell, animal, or clinical studies have been conducted to support this hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Empagliflozin in classic stiff person syndrome, focal stiff limb syndrome, or opsismodysplasia.

---

## Literature Evidence

Currently no related literature available for Empagliflozin in the predicted indications.

---

## Taiwan Market Information

Empagliflozin is not currently registered or marketed in Taiwan. No approved licenses or DIN records exist in the Taiwan regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three predicted indications (Classic Stiff Person Syndrome, Focal Stiff Limb Syndrome, Opsismodysplasia) are at evidence level L5 — model prediction only — with no supporting clinical trials, observational studies, or published literature, and the proposed mechanistic links are highly indirect and do not address the core disease pathophysiology of any predicted indication.

**To proceed, the following is needed:**
- Resolve Blocking data gap DG001: obtain TFDA package insert warnings and contraindications before any safety evaluation can begin
- Resolve High-severity data gap DG002: retrieve confirmed MOA data from DrugBank to enable proper mechanistic plausibility assessment
- Commission a systematic literature review of SGLT2 inhibitors in autoimmune neurological diseases as a minimum prerequisite for SPS hypothesis generation
- Conduct preclinical studies (GAD65-antibody animal models) before any clinical development consideration for the SPS indications
- Consider evaluating Empagliflozin's established indications (T2DM, heart failure, CKD) as scientifically better-grounded repurposing candidates if the goal is near-term clinical translation, rather than pursuing these KG-predicted rare disease associations at L5 evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

