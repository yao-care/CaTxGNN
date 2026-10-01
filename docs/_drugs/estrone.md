---
layout: default
title: Estrone
parent: Model Prediction Only (L5)
nav_order: 354
evidence_level: L5
indication_count: 2
---

# Estrone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Estrone: From an Unspecified Original Indication to Elevated Plasma Zinc

## One-Sentence Summary

Estrone is an estrogen marketed in Canada as a vaginal cream, but its original approved indication is not recorded in the available data.
The TxGNN model predicts it may be related to **elevated plasma zinc**, but there are **0 clinical trials** and only **2 loosely related publications** behind this prediction.
This is a model-only signal with no direct supporting evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in the Canadian licence record |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 (the pack labels it L4, but the retrieved papers do not test estrone for this condition, so prediction-only is the more accurate level) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Estrone is an estrogen product, and its licensed Canadian form is a vaginal cream. Without a documented original indication or mechanism, the link to the predicted indication cannot be assessed.

No direct mechanistic link is established. The score of 0.998 comes from graph-based prediction only. The two retrieved papers concern hormonal status and micronutrient markers, and neither examines estrone as a treatment for elevated plasma zinc. Elevated plasma zinc is also a laboratory finding, not a well-defined disease target, which makes a therapeutic hypothesis hard to frame.

A second prediction, **pyogenic arthritis-pyoderma gangrenosum-acne (PAPA) syndrome**, scored 99.30%. It has no trials or literature at all (L5). PAPA is a rare autoinflammatory disorder, and no rationale connects estrone to its pathway.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [807594](https://pubmed.ncbi.nlm.nih.gov/807594/) | 1975 | Cohort | J Clin Endocrinol Metab | In 28 men with severe protein-calorie malnutrition, hypogonadism and low testosterone recovered with refeeding. It does not study estrone or zinc treatment. |
| [12081830](https://pubmed.ncbi.nlm.nih.gov/12081830/) | 2002 | Unverified (likely intervention study) | Am J Clin Nutr | Examines iron indexes and antioxidant status in perimenopausal women given soy protein. It does not study estrone or plasma zinc. |

Both papers are indirect and neither supports the predicted indication.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 727369 | ESTRAGYN VAGINAL CREAM | Vaginal cream (inferred from product name) | Not provided |

## Safety Considerations

Please refer to the package insert for safety information. No interaction records were found for this drug in the queried data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-model score. No clinical trials exist, and the two retrieved papers do not test estrone for this condition. Because the original indication, mechanism and safety data are missing, the candidate cannot progress to safety screening.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap)
- The original approved indication and mechanism of action (for example from DrugBank)
- A plausible biological rationale linking estrone to plasma zinc regulation, and confirmation that elevated plasma zinc is a clinically meaningful target
- Targeted literature searches for direct evidence, and review of the two retrieved papers' relevance
- Confirmation of route compatibility, since the only marketed form is a vaginal cream

*This report is for research reference only and is not medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

