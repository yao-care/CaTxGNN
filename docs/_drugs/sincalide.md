---
layout: default
title: Sincalide
parent: Model Prediction Only (L5)
nav_order: 851
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Sincalide: predicted new indication Malignant catarrh (evidence level L5). Approved use: Not stated in the Health Canada license data compiled for this report…"
monitor_inn: "Sincalide"
predicted_indications: ["malignant catarrh", "infectious bovine rhinotracheitis", "cytomegalovirus infection", "thrombotic disease", "hyperthyroidism", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "hyperthyroxinemia", "homozygous familial hypercholesterolemia", "Prinzmetal angina", "amenorrhea (disease)"]
---

# Sincalide
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

## Sincalide: From Gallbladder and Pancreatic Diagnostic Use to Malignant Catarrh
{: .text-alpha }

## One-Sentence Summary

Sincalide is a synthetic C-terminal octapeptide of cholecystokinin (CCK) that stimulates gallbladder contraction and pancreatic secretion, and it is used as a diagnostic agent.
The TxGNN model predicts it may be effective for **malignant catarrh**, but there are **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on computation alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Health Canada license data compiled for this report (the drug's known pharmacology is gallbladder and pancreatic function diagnostics) |
| Predicted New Indication | Malignant catarrh |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, sincalide is a synthetic CCK octapeptide that acts on CCK receptors in the gastrointestinal tract to stimulate gallbladder contraction and pancreatic secretion.

No mechanistic link to the predicted indication has been identified. Malignant catarrh (malignant catarrhal fever) is a viral disease of ruminants, and no CCK-receptor-mediated pathway is known to bear on its pathogenesis. The prediction is purely computational, with no supporting trial or literature data.

The same pattern holds for the other top-ranked predictions, which include infectious bovine rhinotracheitis, cytomegalovirus infection, thrombotic disease, hyperthyroidism, resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta, hyperthyroxinemia, homozygous familial hypercholesterolemia, Prinzmetal angina and amenorrhea. All of them have an L5 evidence level, no clinical trials, no literature and no plausible mechanism. The high scores likely reflect knowledge-graph connectivity rather than pharmacological relevance.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02228602 | KINEVAC | Not listed | Not listed |
| 02494361 | SINCALIDE FOR INJECTION | Not listed | Not listed |

## Safety Considerations

Please refer to the package insert for safety information.

No drug-drug interaction records were found for sincalide, and the knowledge graph lists no contraindicated diseases.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trial or literature support (L5, model prediction only), and no plausible mechanism links CCK-receptor agonism to a veterinary viral disease. Package insert safety data is also missing, which blocks progression to safety screening.

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications and approved indications) downloaded and parsed
- Mechanism of action data (for example from DrugBank)
- A credible biological rationale for the predicted indication, and confirmation that the disease is relevant to human medicine
- Any preclinical or clinical evidence supporting the prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

