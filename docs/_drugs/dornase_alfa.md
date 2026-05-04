---
layout: default
title: Dornase Alfa
parent: 僅模型預測 (L5)
nav_order: 238
evidence_level: L5
indication_count: 10
---

# Dornase Alfa
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

# Dornase alfa: From Cystic Fibrosis to Paroxysmal Hemicrania

## One-Sentence Summary

Dornase alfa (Pulmozyme) is a recombinant human DNase I enzyme, clinically established internationally for cystic fibrosis by degrading extracellular DNA in airway secretions to reduce mucus viscosity.
The TxGNN model predicts it may have activity against **Paroxysmal Hemicrania**, a rare trigeminal autonomic headache disorder.
However, **0 clinical trials** and **0 publications** currently support this direction, and the prediction score of 50% is shared identically across all 10 top-ranked indications — strongly suggesting a model artifact rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current dataset (drug not registered in Canada; internationally approved for cystic fibrosis) |
| Predicted New Indication | Paroxysmal Hemicrania |
| TxGNN Prediction Score | 50.00% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not captured in this evidence pack. Based on established scientific knowledge, Dornase alfa is a recombinant human deoxyribonuclease I (DNase I) enzyme that selectively cleaves extracellular DNA. It is approved in multiple jurisdictions (FDA, EMA, and others) under the brand name Pulmozyme for cystic fibrosis, where neutrophil-derived extracellular DNA contributes to the abnormal mucus viscosity that obstructs the airways; enzymatic degradation of this DNA reduces sputum viscosity and improves pulmonary function.

Paroxysmal hemicrania is a trigeminal autonomic cephalalgia (TAC) subtype, characterised by severe, strictly unilateral orbital or temporal pain attacks accompanied by ipsilateral cranial autonomic features. The underlying pathophysiology involves activation of the hypothalamic–trigeminal vascular axis and neuroimmune signalling — not extracellular DNA accumulation. The theoretical bridge proposed by the TxGNN model is highly indirect: cGAS-STING and TLR9 DNA-sensing pathways are emerging areas of neuroinflammation research, and DNase I could theoretically dampen this signal. However, this multi-step hypothetical connection has zero supporting preclinical or clinical literature to date.

A critical red flag in this evidence pack is the observation that all 10 top-ranked predicted indications — spanning histiocytoses, trigeminal headache disorders, glaucoma, and benign oral tumours — carry the identical TxGNN score of exactly 0.5. This strongly suggests these predictions reflect graph-topological proximity within the disease ontology node clusters (e.g., the histiocytosis node group) rather than any biologically specific drug–disease interaction. This pattern is a known characteristic of systematic graph-network output rather than mechanistically grounded repurposing signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Dornase alfa has no registered products in Canada per this dataset (0 DINs, not marketed). The drug is commercially available internationally as Pulmozyme (Genentech/Roche) for cystic fibrosis but does not appear in the Canada regulatory dataset captured here.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for Dornase alfa in paroxysmal hemicrania is supported by zero clinical trials and zero publications, carries an undifferentiated score of 0.5 shared identically across 10 biologically unrelated indications, and lacks any plausible mechanistic pathway connecting DNase I activity to trigeminal autonomic headache pathophysiology; this combination of factors indicates a model noise artifact that does not warrant forward investment at this time.

**To proceed, the following is needed:**
- Retrieve the full approved prescribing information (package insert) for Pulmozyme to document the confirmed original indication, contraindications, and key warnings
- Obtain mechanism of action and pharmacology data from DrugBank (DB00003) to enable proper mechanistic reasoning
- Conduct a dedicated literature search for DNase I, extracellular DNA, NETs (neutrophil extracellular traps), and cGAS-STING involvement specifically in trigeminal autonomic cephalalgias or neuroinflammation models
- Cross-validate TxGNN scores against alternative computational repurposing models (e.g., DRKG, OpenTargets) to determine whether the paroxysmal hemicrania signal is model-specific noise or reproducible across platforms
- If neuroinflammation rationale is to be pursued, prioritise indications with a stronger established extracellular DNA or NET component (e.g., SLE, ANCA-associated vasculitis) over headache disorders where biological plausibility is substantially weaker
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

