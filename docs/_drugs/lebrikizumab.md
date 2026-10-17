---
layout: default
title: Lebrikizumab
parent: Model Prediction Only (L5)
nav_order: 530
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Lebrikizumab: predicted new indication Severe nonproliferative diabetic retinopathy (evidence level L5). Approved use: Atopic dermatitis"
monitor_inn: "Lebrikizumab"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "drug-induced osteoporosis", "diabetic retinopathy", "primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "neonatal dermatomyositis", "psoriasis", "HER2 positive breast carcinoma"]
---

# Lebrikizumab
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

# Lebrikizumab: From Atopic Dermatitis to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Lebrikizumab is an anti-IL-13 monoclonal antibody, marketed in Canada as EBGLYSS and developed for moderate-to-severe atopic dermatitis.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**.
This is a computational prediction only: there are **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic dermatitis (inferred from the drug's clinical program; the licence indication text was not populated in the data compiled for this report) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 97.94% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Lebrikizumab binds IL-13 and prevents formation of the IL-13Rα1/IL-4Rα signalling complex. This dampens type 2 inflammation, the central driver of atopic dermatitis. Detailed mechanism-of-action data were not available in the compiled data, so this description comes from the drug class and the literature on its original indication.

A link to diabetic retinopathy is possible in theory, for example if type 2 inflammation contributes to retinal inflammation. However, this is speculation. The compiled data contain no trial, publication or mechanistic study connecting IL-13 blockade to diabetic retinopathy. The high score reflects the model's pattern matching in its knowledge graph, not demonstrated biology. The original and predicted indications (a skin disease and a microvascular eye complication of diabetes) are also quite different, and no similarity analysis was available.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02549131 | EBGLYSS |
| 02549123 | EBGLYSS |

Both authorisations are valid single-ingredient products. Dosage form and approved-indication text were not available in the compiled data.

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials, no literature and no established mechanistic link to diabetic retinopathy. Safety data from the label are also missing, so the candidate cannot move beyond the initial screening stage.

**To proceed, the following is needed:**
- Preclinical or mechanistic evidence for IL-13 involvement in diabetic retinopathy (for example, IL-13 expression in diabetic retinal tissue or animal models)
- Health Canada product monograph warnings and contraindications
- Mechanism-of-action data from DrugBank
- Assessment of route compatibility, since ocular disease may need a different delivery approach than subcutaneous injection

**Note on other predictions:** Of the other predictions for this drug, only "dermatitis" (rank 5) has substantial evidence, including multiple Phase 3 trials and randomised publications. It maps to atopic dermatitis, which is the drug's existing use, so it is not a true repurposing finding. The psoriasis prediction (rank 9) is weakly supported: the IL-13 mechanism is a poor fit, and one case report describes lebrikizumab-induced psoriasis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

