---
layout: default
title: Soybean Oil
parent: Model Prediction Only (L5)
nav_order: 860
evidence_level: L5
indication_count: 1
---

# Soybean Oil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Soybean Oil: From Parenteral Nutrition Lipid Source to Amenorrhea

## One-Sentence Summary

Soybean oil is the lipid component of several intravenous lipid emulsion and parenteral nutrition products marketed in Canada. The supplied data does not state a formal approved indication.
The TxGNN model predicts it may be effective for **amenorrhea**, but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the supplied data (the marketed products are lipid emulsions, which suggests a nutritional use) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 13 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, soybean oil is a source of polyunsaturated fatty acids, mainly linoleic acid. It is used in lipid emulsions and combination parenteral nutrition products. Its efficacy in any specific original indication cannot be confirmed from the supplied data.

One speculative link is that fatty acids may influence steroid hormone synthesis or correct energy deficiency, which underlies functional hypothalamic amenorrhea. This reasoning is not supported by any study in the supplied data.

The isoflavones usually cited for soy phytoestrogen effects are found mainly in soy protein, not in the refined oil. The very high score is therefore more likely a knowledge-graph artifact, such as connections through hub nodes or nutrient and lipid-related nodes, than a real therapeutic signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

13 licenses are on record. The five main ones are listed below. Dosage form and approved indication text were not provided for these products.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2065673 | INTRALIPID 20% | Not specified | Not specified |
| 2344327 | CLINOLEIC 20% | Not specified | Not specified |
| 2396963 | SMOFLIPID 20% | Not specified | Not specified |
| 2352540 | OLIMEL 5.7% | Not specified | Not specified |
| 2477947 | OLIMEL 7.6% | Not specified | Not specified |

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high model score. There are no clinical trials or publications, and the mechanism and original indication are unverified. The mechanistic link is speculative and may be a knowledge-graph artifact.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data from DrugBank
- Approved indication text and dosage forms for the Canadian products
- A literature and trial search on lipid or fatty acid intake and amenorrhea, particularly functional hypothalamic amenorrhea
- Route compatibility assessment, since the available products appear to be intravenous nutrition formulations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

