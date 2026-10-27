---
layout: default
title: Bimekizumab
parent: Model Prediction Only (L5)
nav_order: 116
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Bimekizumab: predicted new indication Diabetic cataract (evidence level L5). Approved use: Not available in the compiled data"
monitor_inn: "Bimekizumab"
predicted_indications: ["diabetic cataract", "immature cataract", "craniostenosis cataract", "tetanic cataract", "mature cataract", "diabetes mellitus type 2 associated cataract", "nuclear senile cataract", "cortical cataract", "senile cataract", "antithrombin deficiency type 2"]
---

# Bimekizumab
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

## Bimekizumab: From an Approved Immune-Mediated Indication to Diabetic Cataract
{: .text-alpha }

## One-Sentence Summary

Bimekizumab is a humanized monoclonal antibody that neutralizes IL-17A and IL-17F. It is marketed in Canada under the brand name BIMZELX, but the compiled data do not include its approved indication text.
The TxGNN model predicts it may be effective for **diabetic cataract**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on a knowledge-graph score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (the Health Canada license entries contain no indication text) |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 98.23% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, bimekizumab is a monoclonal antibody that dual-neutralizes IL-17A and IL-17F, cytokines involved in inflammatory signaling.

No established link between IL-17 blockade and lens opacification was identified. A speculative pathway is that chronic low-grade inflammation and oxidative stress in diabetes may involve IL-17 signaling, but no trial or publication supports this. Diabetic cataract is mainly driven by hyperglycemia, the polyol pathway, and oxidative stress.

A systemic biologic is also a poor fit for a lens condition. The high score reflects a graph-based inference only and should not be read as clinical support.

The other top-ranked predictions are mostly other cataract types (immature, mature, senile, nuclear, cortical, tetanic, craniostenosis-associated, and type 2 diabetes-associated cataract), plus type 2 antithrombin deficiency. All are L5 with no trials or literature, and none has a plausible IL-17A/F mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02553627 | BIMZELX | Not specified | Not specified |
| 02525275 | BIMZELX | Not specified | Not specified |
| 02525267 | BIMZELX | Not specified | Not specified |
| 02553619 | BIMZELX | Not specified | Not specified |

All four licenses are valid single-ingredient products.

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug-interaction records were found in the data compiled for this report. For a biologic immunomodulator, infection-related risks would need particular weighing in a diabetic population.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature, and no plausible mechanism linking IL-17A/F neutralization to lens opacification. A systemic immunomodulatory biologic is also poorly suited to a degenerative or metabolic lens condition.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (a blocking gap for safety screening)
- Approved indication text and dosage forms for each DIN
- Mechanism of action data from DrugBank
- Preclinical or mechanistic evidence linking IL-17 signaling to diabetic lens pathology
- Assessment of route compatibility, since a systemic biologic is unlikely to suit an ocular target
- Safety evaluation of infection risk in a diabetic population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

