---
layout: default
title: Cimetidine
parent: 僅模型預測 (L5)
nav_order: 162
evidence_level: L5
indication_count: 9
---

# Cimetidine
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

# Cimetidine: From Peptic Ulcer Disease to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Cimetidine is a histamine H2-receptor antagonist with a decades-long history of use in peptic ulcer disease and conditions of gastric acid hypersecretion.
The TxGNN model predicts it may be effective for **Smouldering Systemic Mastocytosis (SSM)**, ranking it as the top novel repurposing candidate with a prediction score of **99.80%**.
However, **no clinical trials** and **no publications** were identified specifically supporting this indication, placing the entire evidence base at model-prediction level only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Peptic ulcer disease; gastric acid hypersecretion conditions |
| Predicted New Indication | Smouldering Systemic Mastocytosis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this Evidence Pack. Based on contextual information embedded in the evidence records, cimetidine is a competitive antagonist at the histamine H2 receptor on gastric parietal cells. By blocking H2 receptors, it suppresses histamine-stimulated gastric acid secretion and reduces intragastric acidity — the core pharmacological action underlying its established use in peptic ulcer disease.

In systemic mastocytosis, clonal mast cells accumulate in organs and continuously release histamine in large quantities. This triggers a cascade of H1- and H2-mediated symptoms including gastric acid hypersecretion, abdominal cramping, and diarrhoea. The mechanistic connection is therefore direct and logical: blocking H2 receptors should attenuate the acid hypersecretion component of mast cell mediator release. In clinical practice, combination H1 + H2 blockade is already a cornerstone of mastocytosis symptom management, making cimetidine's mechanistic fit conceptually sound.

Smouldering Systemic Mastocytosis (SSM) sits in the middle of the severity spectrum — higher mast cell burden than indolent mastocytosis, but without end-organ damage meeting the criteria for aggressive disease. Effective symptom control in SSM is therefore clinically meaningful. However, the TxGNN prediction remains at the hypothesis level for this specific subtype: no clinical trials or publications specific to cimetidine in SSM were retrieved. The prediction likely reflects graph-level proximity between the H2-receptor pharmacological node and histamine-driven disease nodes in the knowledge graph, rather than empirically validated efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Cimetidine is not currently marketed in Canada. The regulatory query returned zero active Drug Identification Numbers (DINs) and no licence records. Should a repurposing programme for SSM be pursued, a full regulatory filing from first principles would be required in the Canadian market.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's mechanistic logic is coherent — cimetidine's H2 blockade directly addresses one of the primary pathophysiological drivers of mastocytosis symptoms — but the complete absence of clinical trial and published literature evidence for this specific subtype (SSM) means there is currently no empirical foundation on which to advance a repurposing decision.

**To proceed, the following is needed:**

- **Retrieve the full product monograph / package insert** to complete the safety assessment, including warnings, contraindications, and drug interactions — currently a blocking data gap
- **Confirm the mechanism of action** via DrugBank or an equivalent validated source — required for mechanistic link analysis
- **Targeted literature review** for H2-receptor antagonists (cimetidine, ranitidine, famotidine) in systemic mastocytosis broadly, and SSM specifically, to determine whether existing clinical use already constitutes de facto evidence
- **Guideline review** — confirm whether current mastocytosis management guidelines (e.g., ECNM, NCCN) already recommend H2 blockers as standard of care; if so, this is an established use rather than novel repurposing and the decision framework changes
- **Comparative assessment against lower-ranked predictions**: Predictions at ranks 2–7 (particularly active peptic ulcer disease at L1, gastrojejunal ulcer at L3, and duodenogastric reflux at L3) carry substantially stronger evidence and may represent more actionable repurposing candidates in the near term
- **Market access strategy**: Given zero current Canadian market presence, a parallel regulatory pathway analysis is needed before any development investment is committed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

