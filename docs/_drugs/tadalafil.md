---
layout: default
title: Tadalafil
parent: 僅模型預測 (L5)
nav_order: 744
evidence_level: L5
indication_count: 8
---

# Tadalafil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Tadalafil: From (Indication Not Documented) to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

> Tadalafil (DrugBank DB00820) is a PDE5 inhibitor; this evidence pack does not include a documented original indication or mechanism-of-action text (data gap), though it is publicly known as a treatment for erectile dysfunction, BPH, and pulmonary arterial hypertension.
> The TxGNN model's top prediction is **Ambras Type Hypertrichosis Universalis Congenita** (score 99.98%), but this is currently supported by **0 clinical trials** and **0 publications**, and the model's own generated rationale flags it as a likely knowledge-graph artifact rather than a real mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (`original_indications` is empty) |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available for tadalafil in this evidence pack (Data Gap DG002, High severity). Based on general pharmacological knowledge, tadalafil is a PDE5 inhibitor that increases cGMP-mediated vascular smooth muscle relaxation — the basis of its known use in erectile dysfunction, BPH, and pulmonary arterial hypertension.

However, the model's own `repurposing_rationale` for this top candidate is explicit that **no mechanistic link exists**: Ambras type hypertrichosis universalis congenita is a rare congenital disorder of hair follicle growth regulation (androgen/growth-factor pathways), which does not intersect with the cGMP–PDE5 vascular pathway. The rationale states the 99.98% score is most likely an artifact of knowledge-graph embedding proximity rather than a biologically derived prediction, and there is no supporting clinical trial or literature evidence of any kind.

This pattern is not isolated. Five of the eight predicted indications in this pack (Ambras hypertrichosis, hypertrichosis, odontal/periodontal malformation syndrome, Dandy-Walker–associated syndrome, isolated hair shaft abnormality, familial trichomegaly) carry near-identical very-high scores (>99.6%) with zero clinical or literature support, and each rationale independently concludes there is no plausible PDE5-related mechanism. This suggests a **systematic scoring artifact for tadalafil in this run**, rather than several independent genuine signals. Two candidates outside this pattern deserve separate note: kyphoscoliotic heart disease (rank 7) has a theoretically plausible but unproven link via WHO Group 3 pulmonary hypertension, flagged only as a "Research Question," and migraine with brainstem aura (rank 8) is supported by a single case report describing tadalafil-*induced* migraine aura — a safety signal, not a treatment hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Tadalafil currently has **no marketing authorization (DIN) in Canada** under this evidence pack (`total_licenses: 0`, `licenses: []`, market status: not marketed). No authorized product/indication text is available to summarize.

---

## Safety Considerations

Formal safety data (key warnings, contraindications, drug-interaction database) is not available in this evidence pack — please refer to the Health Canada product monograph for full safety information.

**Supplementary literature signal (not part of the formal safety dataset):** A case report (PMID [17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/), *Cephalalgia*, 2006) describes tadalafil-associated typical migraine aura without headache, consistent with the known cerebral vasodilatory effect of PDE5 inhibition. This is a class-related adverse-effect signal and is unrelated to the predicted indication above, but is worth flagging for any future clinical evaluation of this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication has an extremely high TxGNN score but zero clinical or literature support, and the model-generated rationale itself identifies it as a likely embedding artifact with no plausible biological mechanism. This pattern repeats across the majority of predicted indications for this drug, undermining confidence in this candidate set as a whole.

**To proceed, the following is needed:**
- Documented original indication and label text for tadalafil (currently a Blocking data gap, DG001)
- Verified mechanism of action from DrugBank/product monograph (currently a High-severity data gap, DG002)
- Health Canada regulatory pathway assessment, given the drug is not currently marketed in Canada (0 DINs)
- If the kyphoscoliotic heart disease / Group 3 pulmonary hypertension hypothesis is pursued further, a dedicated safety review of PDE5 inhibitor use in non-Group 1 pulmonary hypertension is required before any research protocol is considered
- Independent scrutiny of TxGNN score calibration for this drug, given the systematic high-score/no-evidence pattern across most candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

