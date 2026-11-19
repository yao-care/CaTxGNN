---
layout: default
title: Anakinra
parent: Model Prediction Only (L5)
nav_order: 59
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-05
monitor_inn: "Anakinra"
predicted_indications: ["extracutaneous mastocytoma", "hepatic infarction", "aggressive systemic mastocytosis", "hepatic veno-occlusive disease", "peliosis hepatis", "oligoarticular juvenile idiopathic arthritis with anti-nuclear antibodies", "oligoarticular juvenile idiopathic arthritis without anti-nuclear antibodies", "pyogenic autoinflammatory syndrome", "unclassified autoinflammatory syndrome"]
description: "Anakinra: predicted new indication Extracutaneous mastocytoma (evidence level L5). In Canada: 1 DIN (1 marketed)"
---

# Anakinra
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Anakinra: Extracutaneous mastocytoma
{: .text-alpha }

## One-Sentence Summary

Anakinra is a recombinant interleukin-1 (IL-1) receptor antagonist that is marketed in Canada.
The TxGNN model predicts it may be effective for **extracutaneous mastocytoma**, with a score of 0.9993.
There are currently **no clinical trials and no publications** supporting this specific prediction, so it remains a model-only hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Extracutaneous mastocytoma |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 1 of 1) |
| Number of DINs | 1 (marketed: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for anakinra: "KINERET blocks the biologic activity of IL-1 alpha and beta by competitively inhibiting IL-1 binding to the interleukin-1 type I receptor (IL-1RI), which is expressed in a wide variety of tissues and organs. IL-1 production is induced in response to inflammatory stimuli and mediates various physiologic responses including inflammatory and immunological responses." ([DailyMed: Kineret (anakinra) prescribing information, Swedish Orphan Biovitrum AB (publ)](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d9d74915-6606-4570-9c52-c4001d3177de), label version 2026-04-03; accessed 2026-11-19.) Based on general knowledge, anakinra blocks IL-1 signalling, a pathway central to many inflammatory conditions.

A speculative link is that IL-1 signalling may contribute to inflammation driven by mast cells. However, nothing in the data compiled for this report supports this link. No trials or publications address extracutaneous mastocytoma, and the similarity to the drug's established uses has not been assessed. The prediction should therefore be treated as a hypothesis for further investigation, not as a finding.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02245913 | KINERET | Not specified | Not specified |

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 recorded interactions. The listed examples include:
  - **Major**: deferiprone.
  - **Moderate**: corticosteroids (hydrocortisone, betamethasone, budesonide, dexamethasone, prednisolone, prednisone, triamcinolone), simvastatin, apixaban, rivaroxaban, dicoumarol, and radiopharmaceutical or radiolabelled antibody agents (ibritumomab tiuxetan, iobenguane I-131, tositumomab).
  - **Minor**: zinc salts (acetate, gluconate, sulfate).

Please also refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (0.9993), but no clinical trial or publication studies anakinra in extracutaneous mastocytoma. This places the evidence at L5, model prediction only, which is not enough to justify moving forward.

**To proceed, the following is needed:**
- Preclinical or mechanistic data showing a role for IL-1 signalling in this disease
- Published case reports or early-phase studies of IL-1 blockade in mast cell neoplasms
- Mechanism-of-action data for anakinra
- Review of the Health Canada package insert for warnings and contraindications
- A safety plan that takes the interaction findings into account, particularly the major interaction with deferiprone

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for anakinra are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Kineret (anakinra) prescribing information, Swedish Orphan Biovitrum AB (publ)](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d9d74915-6606-4570-9c52-c4001d3177de) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

