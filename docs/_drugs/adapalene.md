---
layout: default
title: Adapalene
parent: 僅模型預測 (L5)
nav_order: 25
evidence_level: L5
indication_count: 1
---

# Adapalene
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

# Adapalene: From Acne Treatment to Zinc, Elevated Plasma

## One-Sentence Summary

Adapalene is a third-generation topical retinoid, widely used in dermatology for acne vulgaris treatment through selective binding to nuclear retinoic acid receptors (RAR-β and RAR-γ).
The TxGNN model predicts it may be effective for **Zinc, Elevated Plasma (hyperzincaemia)**,
however this prediction is currently supported by **zero clinical trials** and **zero publications** — making it a model-only hypothesis with no empirical backing.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acne vulgaris (topical retinoid) |
| Predicted New Indication | Zinc, Elevated Plasma |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| Market Status | Not Marketed |
| Number of Registered Products | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the structured dataset. Based on known pharmacological information, adapalene is a third-generation synthetic retinoid that selectively binds RAR-β and RAR-γ nuclear receptors, regulating gene expression to exert anti-inflammatory and keratinocyte-normalising effects. It is primarily approved for topical treatment of acne vulgaris.

The mechanistic rationale proposed by TxGNN for this prediction rests on an indirect biochemical pathway: retinoids such as adapalene can induce metallothionein (MT) gene expression, and MT is the primary intracellular zinc-binding protein. In theory, increased MT expression could redistribute or facilitate clearance of plasma zinc. Additionally, RAR nuclear receptors themselves depend on zinc finger structural domains for activity, meaning that abnormal zinc metabolism could in principle disrupt RAR signalling in a bidirectional relationship.

However, these mechanistic steps are multiple degrees removed from a direct therapeutic effect. There is currently **no clinical evidence** that adapalene lowers plasma zinc concentrations, and no recognised treatment pathway exists for using retinoids in hyperzincaemia. The high TxGNN score (0.995) most likely reflects knowledge graph proximity between the nodes *retinoid → metallothionein → zinc* rather than a true therapeutic association. This prediction should be treated with significant scepticism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Market Information

This drug is currently **not marketed** and has no registered products or product authorisations on file. No DIN (Drug Identification Number) or equivalent regulatory submissions are recorded in the dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported exclusively by a knowledge graph model (evidence level L5) with no clinical trials, no published literature, and no plausible direct therapeutic mechanism linking adapalene to the management of elevated plasma zinc. The mechanistic connection is speculative and multi-step, and the indication itself ("zinc, elevated plasma") is a laboratory finding rather than a standalone disease entity with established treatment protocols.

**To revisit this decision, the following would be needed:**

- **Preclinical evidence**: In vitro or animal studies demonstrating that adapalene or any retinoid meaningfully reduces plasma zinc levels (would upgrade to L4).
- **Mechanistic clarification**: Quantitative data on MT induction by adapalene and its downstream effect on plasma zinc homeostasis.
- **MOA data**: Full DrugBank mechanism-of-action data to better assess target pathway overlap.
- **Clinical context review**: Determine whether "zinc, elevated plasma" represents a primary condition (e.g., zinc toxicity, dietary overload) or a secondary biomarker — this would define whether a drug intervention is even conceptually appropriate.
- **Safety profile**: Retrieve full package insert warnings and contraindications before any translational planning.

> ⚠️ **Research Use Only**: This report is generated for research reference purposes and does not constitute medical advice. All drug repurposing candidates require clinical validation before any application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

