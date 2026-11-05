---
layout: default
title: Icatibant
parent: Model Prediction Only (L5)
nav_order: 465
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-05
monitor_inn: "ICATIBANT"
predicted_indications: ["serpinopathy with toxic serpin polymerization", "pseudo-von Willebrand disease", "primary release disorder of platelets", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "Glanzmann thrombasthenia"]
description: "Icatibant: predicted new indication Serpinopathy with toxic serpin polymerization (evidence level L5). Approved use: Not recorded in the local data"
---

# Icatibant
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Icatibant: Serpinopathy with toxic serpin polymerization
{: .text-alpha }

## One-Sentence Summary

Icatibant is a bradykinin receptor antagonist that is marketed in Canada.
The TxGNN model predicts it may be relevant for **serpinopathy with toxic serpin polymerization**, with a score of 0.9999.
There are currently **no clinical trials and no publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Serpinopathy with toxic serpin polymerization |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 2 of 2) |
| Number of DINs | 2 (marketed: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. From pharmacology data, icatibant is a peptide that acts on the bradykinin B2 receptor (and is also listed against the B1 receptor), blocking bradykinin signalling.

The model's high score most likely reflects shared biology around SERPING1 (C1 inhibitor) and serpin disorders. However, toxic serpin polymerization is a protein-misfolding problem, not a bradykinin-driven process. A B2 receptor antagonist has no clear mechanism to address it. The prediction should be treated as a hypothesis from network-level similarity only, and no mechanistic rationale has been established.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02425696 | FIRAZYR | Not specified | Not specified |
| 02547562 | ICATIBANT INJECTION | Not specified | Not specified |

Both licences are single-ingredient products and both are currently valid.

## Safety Considerations

- **Drug Interactions**: 10 moderate-level interactions were identified, all with ACE inhibitors: benazepril, captopril, enalapril, perindopril, trandolapril, moexipril, lisinopril, quinapril, ramipril and fosinopril.

Please refer to the package insert for further safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The score is very high, but there are no trials or publications, and no plausible mechanism links bradykinin B2 blockade to serpin polymerization. The prediction is not supported beyond the model output.

**To proceed, the following is needed:**
- A mechanistic hypothesis explaining how B2 receptor antagonism could affect toxic serpin polymerization
- Preclinical data in relevant disease models
- Package insert warnings and contraindications from Health Canada
- Confirmed mechanism-of-action data

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

