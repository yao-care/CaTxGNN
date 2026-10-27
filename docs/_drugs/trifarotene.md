---
layout: default
title: Trifarotene
parent: Model Prediction Only (L5)
nav_order: 945
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Trifarotene: predicted new indication Zinc, elevated plasma (evidence level L5). Approved use: Acne (acne vulgaris)"
monitor_inn: "Trifarotene"
predicted_indications: ["zinc, elevated plasma", "pyogenic arthritis-pyoderma gangrenosum-acne syndrome", "demodicidosis of sebaceous gland", "spondyloarthropathy, susceptibility to", "malaria", "Zollinger-Ellison syndrome", "Ehlers-Danlos syndrome", "Beare-Stevenson cutis gyrata syndrome", "isolated congenital adermatoglyphia", "malignant atrophic papulosis"]
---

# Trifarotene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Trifarotene: From Acne to Elevated Plasma Zinc
{: .text-alpha }

## One-Sentence Summary

Trifarotene is a topical retinoid originally used to treat acne.
The TxGNN model predicts it may be effective for **elevated plasma zinc**, but this is a graph-based prediction only, with **0 clinical trials** and **0 publications** supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne (acne vulgaris) |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Trifarotene is a selective retinoic acid receptor gamma (RARγ) agonist. The data compiled for this report also list activity at RARα and RARβ. It is applied to the skin as a 0.005% cream. Its high metabolic instability suggests limited systemic exposure. Detailed mechanism-of-action data are not otherwise available in the compiled data.

Its acne use makes mechanistic sense: retinoids normalise keratinocyte differentiation in the hair follicle. No plausible mechanistic link to elevated plasma zinc was identified, and a topical agent with minimal systemic exposure is an unlikely way to change a blood mineral level. The prediction should be regarded as a statistical output of the knowledge graph, not a mechanistically supported hypothesis.

Other predicted indications were also reviewed. All have only model-prediction support (L5) and no clinical trials or publications. The most biologically coherent one is **pyogenic arthritis-pyoderma gangrenosum-acne (PAPA) syndrome** (score 99.32%), because it includes severe acne. However, its autoinflammatory drivers (PSTPIP1 mutations, IL-1 pathway) are not targeted by RARγ agonism. Several others, such as malaria, Zollinger-Ellison syndrome and Degos disease, have no credible mechanistic rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the predicted indication.

(Trifarotene itself completed Phase 3 trials in acne vulgaris, including the long-term safety study [NCT02189629](https://clinicaltrials.gov/study/NCT02189629). These relate to the original indication, not the predicted one.)

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02494175 | AKLIEF | Not specified | Not specified |

---

## Safety Considerations

- **Drug Interactions**: No drug-drug interactions are listed in the compiled data. The three entries returned are pharmacological target bindings, not interactions: trifarotene binds retinoic acid receptors α, β and γ (RARA, RARB, RARG).
- **Systemic exposure**: Trifarotene is highly metabolically unstable, so systemic exposure is expected to be limited when used topically.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a graph-based score alone, with no clinical trials, no literature and no plausible mechanistic link. A topical, minimally absorbed agent is poorly suited to altering plasma zinc levels.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data
- A biological rationale connecting RAR agonism to zinc homeostasis, plus preclinical or observational evidence
- Consideration of alternative candidates closer to the original indication (e.g., the acne component of PAPA syndrome), which would still require clinical evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

