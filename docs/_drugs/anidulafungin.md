---
layout: default
title: Anidulafungin
parent: 僅模型預測 (L5)
nav_order: 57
evidence_level: L5
indication_count: 10
---

# Anidulafungin
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

# Anidulafungin: From Invasive Candidiasis to Impetigo

## One-Sentence Summary

Anidulafungin is an echinocandin-class antifungal used intravenously to treat invasive candidiasis and esophageal candidiasis. The TxGNN model ranks **Impetigo** as its top predicted new indication with a score of **98.85%**; however, this prediction carries significant mechanistic concerns. Currently **no clinical trials** and **no supporting publications** exist to validate this repurposing direction, placing it at the lowest evidence tier (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication on record in Canada |
| Predicted New Indication | Impetigo |
| TxGNN Prediction Score | 98.85% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. From established pharmacology, Anidulafungin belongs to the echinocandin class and works by non-competitively inhibiting β-1,3-D-glucan synthase — an enzyme essential for building the fungal cell wall. This enzyme is entirely absent in bacteria and human cells, making Anidulafungin exquisitely selective for fungi.

Impetigo, however, is a superficial bacterial skin infection caused primarily by *Staphylococcus aureus* and/or *Streptococcus pyogenes*. Because Anidulafungin's sole mechanism of action targets a fungal-specific enzyme, it has no known antibacterial activity and cannot reasonably be expected to exert therapeutic benefit against the bacterial pathogens responsible for impetigo.

The high TxGNN score (98.85%) is therefore likely a **network proximity artifact**: in the knowledge graph, nodes representing skin infections cluster together, causing high prediction scores to propagate across both fungal and bacterial skin disease nodes without reflecting true biological activity. This is a case where the model's numerical output should be interpreted with caution, not taken at face value as evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Anidulafungin has no approved Drug Identification Numbers (DINs) in Canada and is currently not marketed in this jurisdiction. No licensing data is available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's top-ranked prediction of impetigo for Anidulafungin is mechanistically implausible — Anidulafungin specifically targets the fungal enzyme β-1,3-D-glucan synthase, which is absent in bacteria, while impetigo is an exclusively bacterial skin infection caused by *S. aureus* and *S. pyogenes*. The high prediction score most likely reflects a knowledge-graph network clustering effect rather than a genuine biological signal. With zero supporting clinical trials, zero publications (L5 evidence), and a fundamental mechanism mismatch, there is no scientific basis to advance this repurposing direction at this time. Notably, all 10 predicted indications in this Evidence Pack are similarly rated L5 / Hold, and the mechanistic rationale recorded for each consistently identifies incompatibility with Anidulafungin's antifungal mechanism of action.

**To proceed, any future evaluation will require:**
- Identification of a plausible mechanistic link between Anidulafungin and any proposed new indication (currently absent for all 10 predictions)
- Retrieval of the full Taiwan/Canada package insert to complete the safety profile — key warnings and contraindications are currently missing (Data Gap DG001, blocking severity)
- Mechanism of action data from DrugBank (Data Gap DG002) to enable proper mechanistic plausibility scoring
- A review of whether any of the predicted indications involve a fungal pathogen or a pathway where echinocandin activity is scientifically conceivable — for example, invasive fungal co-infections in immunocompromised settings — as these would represent more mechanistically coherent targets for further exploration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

