---
layout: default
title: Raloxifene
parent: Model Prediction Only (L5)
nav_order: 782
evidence_level: L5
indication_count: 4
---

# Raloxifene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Raloxifene: From Osteoporosis to Duodenal Ulcer

## One-Sentence Summary

Raloxifene is a selective estrogen receptor modulator (SERM) approved for osteoporosis and for breast cancer risk reduction.
The TxGNN model predicts it may be effective for **duodenal ulcer**, but this is a knowledge-graph prediction only.
Currently **0 clinical trials** and **0 publications** support it, so the evidence is at the model-prediction level.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis; breast cancer risk reduction (taken from the prediction rationale, as the Canadian license indication text was not supplied) |
| Predicted New Indication | Duodenal ulcer |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Raloxifene is a SERM, and its efficacy in osteoporosis and breast cancer risk reduction is established. Any mechanistic link to duodenal ulcer is speculative. One possible route is estrogen receptor signaling in gastrointestinal mucosa. No established pathway connects SERM activity to ulcer healing or to *H. pylori*-related disease.

The high score (0.997) reflects proximity in the knowledge graph, not biological or clinical evidence. The other top-ranked predictions are even weaker:

- **Hypoalphalipoproteinemia (99.65%)**: Raloxifene modestly lowers LDL-C and fibrinogen, but its effect on HDL-C is generally small or neutral. The rationale is weak.
- **Duodenal obstruction (99.64%)**: This is mainly a mechanical or structural condition, so a hormonal receptor modulator has no plausible therapeutic mechanism. It is likely a graph-proximity artifact.
- **Duodenogastric reflux (99.59%)**: This is a motility and pyloric function disorder, and no known SERM mechanism affects it. The association probably comes from shared graph neighbors with other duodenal diseases.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2358840 | ACT RALOXIFENE |
| 2540681 | JAMP RALOXIFENE |
| 2279215 | APO-RALOXIFENE |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a knowledge-graph score, with no trials or publications, and the biological rationale for duodenal ulcer is weak. The product is marketed in Canada (3 DINs), but no safety data are available to support moving forward.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, for example from DrugBank, to assess any link to gastroduodenal mucosa
- A systematic literature and trial search for raloxifene in duodenal ulcer or other gastroduodenal disease
- Review of whether the lower-ranked predictions (such as hypoalphalipoproteinemia) warrant a lipid-endpoint literature search
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

