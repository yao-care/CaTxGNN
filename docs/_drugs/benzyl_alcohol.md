---
layout: default
title: Benzyl Alcohol
parent: 僅模型預測 (L5)
nav_order: 94
evidence_level: L5
indication_count: 1
---

# Benzyl Alcohol
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

# Benzyl Alcohol: From Pharmaceutical Preservative to Bronchitis

## One-Sentence Summary

Benzyl Alcohol is a compound widely used as an antimicrobial preservative in pharmaceutical formulations (including bacteriostatic saline solutions), with no approved therapeutic indications on record in this dataset.
The TxGNN model predicts a statistical association with **Bronchitis**, with **0 clinical trials** and **4 publications** retrieved — however, critically, the existing literature documents benzyl alcohol as a **cause** of bronchitis when inhaled, not as a treatment for it.
This prediction is assessed as a probable case of reverse causation, and the evidence level is **L5** (model prediction only).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indications on record |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

> ⚠️ **Reverse Causation Warning — This prediction requires critical scrutiny before any further evaluation.**

Benzyl Alcohol is primarily known as an antimicrobial preservative in injectable and inhalable pharmaceutical products, most notably bacteriostatic normal saline. When bacteriostatic saline containing benzyl alcohol is nebulized and inhaled, it is well-documented to act as an irritant to the tracheobronchial mucosa and **induce** bronchitis — not treat it. The causal direction is harm, not benefit.

The TxGNN model likely detected a strong statistical co-occurrence between benzyl alcohol and bronchitis within its knowledge graph. However, this association reflects an **adverse effect relationship** (benzyl alcohol → bronchitis as a drug-induced harm), rather than a therapeutic one. This is a textbook example of reverse causation in computational drug repurposing: the model identified that the two entities frequently appear together in the medical literature, but misattributed the direction of the clinical relationship.

Detailed mechanism of action (MOA) data is not available for this drug in the current dataset. There is no established pharmacological mechanism by which benzyl alcohol would be expected to treat bronchitis, and all retrieved evidence points toward harm rather than benefit. This prediction should not be advanced without first resolving this fundamental causation concern.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [7807035](https://pubmed.ncbi.nlm.nih.gov/7807035/) | 1995 | Clinical Observation / Adverse Event Series | The Journal of Family Practice | Investigated whether nebulized bacteriostatic saline (which contains benzyl alcohol as preservative) is an irritant to the tracheobronchial mucosa in healthy adults — **documents benzyl alcohol as a cause of bronchitis, not a treatment** |
| [2355429](https://pubmed.ncbi.nlm.nih.gov/2355429/) | 1990 | Case Report / Adverse Event Report | JAMA | Case report of bronchitis induced by nebulized bacteriostatic saline; benzyl alcohol preservative implicated as the causative irritant |
| [7775900](https://pubmed.ncbi.nlm.nih.gov/7775900/) | 1995 | Clinical Observation | The Journal of Family Practice | Observational study on nebulized saline and bronchitis; contextually related to benzyl alcohol-containing formulations |
| [36747926](https://pubmed.ncbi.nlm.nih.gov/36747926/) | 2023 | Phytochemical / In-vitro Study | Heliyon | Evaluation of Senna tora bioactive molecules for antioxidant, anti-inflammatory, and antibacterial activity; bronchitis mentioned as a traditional indication — not directly about benzyl alcohol |

> ⚠️ All 4 retrieved publications are Tier 3 evidence. The two most directly relevant studies (PMID 7807035, PMID 2355429) explicitly document benzyl alcohol as a **cause** of bronchitis via inhalation, providing no support for a therapeutic role.

---

## Canada Market Information

Benzyl Alcohol is not currently approved or marketed as a drug product in Canada. There are 0 DINs on record for this substance.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for benzyl alcohol in bronchitis is a statistical artifact driven by reverse causation — benzyl alcohol is documented in the medical literature as an agent that *induces* bronchitis through inhalation of bacteriostatic saline, and there is no plausible therapeutic mechanism, no clinical trial evidence, and no approved indication to support further development in this direction.

**To proceed, the following is needed:**
- Confirm whether TxGNN's knowledge graph contains adverse event edges that may be systematically misinterpreted as therapeutic associations — if so, this is a pipeline-level data quality issue requiring correction
- Conduct a comprehensive DrugBank and primary literature review to determine whether any legitimate therapeutic indication for benzyl alcohol exists (e.g., topical pediculicide use) that could inform a separate, better-grounded repurposing hypothesis
- If no therapeutic mechanism for bronchitis can be identified after targeted review, formally flag this candidate as a reverse-causation artifact and remove it from the active repurposing pipeline
- Obtain MOA data from DrugBank to enable future mechanistic plausibility assessments for other predicted indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

