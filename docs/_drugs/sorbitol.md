---
layout: default
title: Sorbitol
parent: Model Prediction Only (L5)
nav_order: 864
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Sorbitol: predicted new indication Exercise-induced malignant hyperthermia (evidence level L5). Approved use: Not available"
monitor_inn: "SORBITOL"
predicted_indications: ["exercise-induced malignant hyperthermia"]
---

# Sorbitol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Sorbitol: From an Unspecified Original Indication to Exercise-Induced Malignant Hyperthermia
{: .text-alpha }

## One-Sentence Summary

Sorbitol is a sugar alcohol that is marketed in Canada in irrigation products, and no formal original indication is recorded in the data compiled for this report.
The TxGNN model predicts it may be effective for **exercise-induced malignant hyperthermia**.
This prediction has **0 clinical trials** and **0 publications** behind it, so it rests on the computational score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the Canadian licence records contain no approved indication text) |
| Predicted New Indication | Exercise-induced malignant hyperthermia |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Sorbitol is known as a sugar alcohol used as an osmotic laxative, a sweetener and an irrigating solution. No original therapeutic indication is documented in the data compiled for this report.

Malignant hyperthermia is a disorder of calcium regulation in skeletal muscle, typically linked to RYR1 or CACNA1S variants. It is triggered by volatile anaesthetics or succinylcholine, and the established treatment is dantrolene. No plausible pharmacological link between sorbitol and this pathway has been identified.

The high score most likely reflects knowledge-graph proximity artefacts, such as shared associations with formulation excipients or other polyols. It should not be read as true pharmacological activity. Sorbitol is not a recognised treatment or preventive agent for malignant hyperthermia.

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
| 00498807 | Sorbitol Mannitol Irrigation | Not specified | Not specified |
| 00799963 | Cystosol W 3% Hexitols | Not specified | Not specified |

---

## Safety Considerations

- **Contraindications (knowledge-graph based, not label text)**: The TxGNN knowledge graph lists active peptic ulcer disease as a contraindication.
- **Drug Interactions**: Two interactions were identified.
  - **Tolevamer**: Major
  - **Lamivudine**: Moderate

Package insert warnings and contraindications were not available for this report. Please refer to the Health Canada package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for this prediction is a high model score. There are no clinical trials or publications, no documented mechanism, and no plausible pharmacological link between sorbitol and malignant hyperthermia. Dantrolene is the established treatment, and sorbitol has no recognised role.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence linking sorbitol to calcium regulation or thermoregulation in skeletal muscle
- Route and formulation compatibility assessment, since current Canadian products are irrigation solutions
- Review of whether the prediction is a knowledge-graph artefact before any further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

