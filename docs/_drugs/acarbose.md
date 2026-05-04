---
layout: default
title: Acarbose
parent: 僅模型預測 (L5)
nav_order: 15
evidence_level: L5
indication_count: 9
---

# Acarbose
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Acarbose: From Type 2 Diabetes to Focal Stiff Limb Syndrome

## One-Sentence Summary

Acarbose is an alpha-glucosidase inhibitor widely used in the management of type 2 diabetes mellitus, working by slowing carbohydrate absorption in the intestinal brush border.
The TxGNN model predicts it may be effective for **Focal Stiff Limb Syndrome**, however this prediction is currently supported by **no clinical trials** and **no published literature** for this specific indication.
The mechanistic rationale is considered weak, and this prediction most likely reflects a knowledge graph network proximity artifact rather than a direct pharmacological opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus (established global use; no approved indication in Canada) |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not marketed (未上市) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in the current Evidence Pack. Based on established pharmacological knowledge, Acarbose is an alpha-glucosidase inhibitor that competitively blocks intestinal brush-border enzymes — specifically maltase, sucrase, and glucoamylase — thereby slowing the digestion and absorption of complex carbohydrates and blunting postprandial blood glucose excursions. It acts locally within the intestinal lumen and has minimal systemic absorption.

Focal stiff limb syndrome is a rare autoimmune neurological disorder mediated by anti-GAD65 (glutamic acid decarboxylase 65) antibodies. GAD65 is the key enzyme that synthesizes the inhibitory neurotransmitter GABA from glutamate. Crucially, GAD65 is also a major autoantigen in type 1 diabetes mellitus, where it drives immune-mediated destruction of pancreatic beta cells. This shared autoimmune target likely explains why the TxGNN knowledge graph produced a high-scoring network proximity link between Acarbose (a diabetes drug) and GAD65-associated neurological conditions — the two disease categories are co-linked through the GAD65 antigen node.

However, the actual mechanistic connection is very weak. Acarbose acts exclusively in the gut lumen and has no ability to modulate GAD65 autoimmunity, GABA synthesis, spinal inhibitory interneuron function, or the underlying neuroimmunological pathology of focal stiff limb syndrome. There is no published evidence that alpha-glucosidase inhibition provides any benefit in autoimmune neurological disorders. This prediction reflects a **comorbidity association** in the knowledge graph (shared GAD65 autoantigen between T1DM and stiff-person spectrum disorders) rather than a genuine repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is rated L5 — model prediction only — with zero supporting clinical trials or literature for the focal stiff limb syndrome indication. The mechanistic case for Acarbose in this neurological condition is not supported: intestinal alpha-glucosidase inhibition has no plausible direct effect on the GAD65-mediated autoimmune pathology driving focal stiff limb syndrome. Additionally, Acarbose holds no approved DINs in Canada, creating a significant regulatory gap that must be resolved before any clinical development pathway can be considered.

**To proceed, the following is needed:**
- Retrieve complete mechanism of action data for Acarbose (DrugBank API)
- Obtain full Canada safety profile: package insert warnings, contraindications, and drug interaction data
- Conduct a targeted literature search for any preclinical or mechanistic evidence linking alpha-glucosidase inhibition to autoimmune neurological conditions or GABA pathway modulation
- Evaluate whether alternative TxGNN predictions with stronger mechanistic grounding (e.g., **Pancreatic Agenesis**, Rank 9, L4 evidence with 11 supporting literature records) represent a more viable repurposing direction for Acarbose
- If pursuing neurological indications, consider whether the stiff-person spectrum rationale warrants a hypothesis-generating preclinical study proposal

---

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

