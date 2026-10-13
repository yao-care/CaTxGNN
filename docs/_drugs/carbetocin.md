---
layout: default
title: Carbetocin
parent: Model Prediction Only (L5)
nav_order: 157
evidence_level: L5
indication_count: 2
---

# Carbetocin
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

# Carbetocin: From Prader-Willi Syndrome to Isotretinoin-like Syndrome

## One-Sentence Summary

Carbetocin is a long-acting oxytocin receptor agonist. In Canada it is marketed to prevent postpartum haemorrhage due to uterine atony. The data compiled for this report also list Prader-Willi syndrome and Noonan syndrome as indications in the knowledge graph.
The TxGNN model predicts it may be effective for **isotretinoin-like syndrome**, but there are **0 clinical trials** and **0 publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prader-Willi syndrome, Noonan syndrome (knowledge graph indications; no approved indication text is available for the Canadian licenses) |
| Predicted New Indication | Isotretinoin-like syndrome |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Carbetocin is a long-acting oxytocin receptor (OXTR) agonist. Detailed mechanism of action data is not currently available in the compiled data, but the pharmacology data confirm that its target is the oxytocin receptor. Its established clinical use is preventing postpartum haemorrhage due to uterine atony. An intranasal formulation (LV-101) has been in development for hyperphagia in Prader-Willi syndrome.

Isotretinoin-like syndrome is a congenital malformation condition resembling retinoic-acid embryopathy. The available data show no plausible mechanistic link between oxytocin receptor agonism and treating this condition. The high score (0.991) is most likely a computational artefact. It may reflect network proximity in the knowledge graph to the original indications (Prader-Willi and Noonan syndromes, both developmental syndromes), but this cannot be verified from the data compiled here. The prediction should be treated as a hypothesis only.

A second prediction, Goodman syndrome (score 99.06%), has the same limitations: no trials, no publications, and no verifiable mechanistic rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02489244 | CARBETOCIN INJECTION | Not specified | Not specified |
| 02496526 | DURATOCIN | Not specified | Not specified |

## Safety Considerations

Please refer to the package insert for safety information.

The pharmacology data list one entry: carbetocin acts on the oxytocin receptor (OXTR) in humans. This is a target interaction, not a drug-drug interaction with a specific co-administered medicine.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational score, with no clinical trials, no literature, and no plausible mechanistic link to isotretinoin-like syndrome. Package insert safety data are also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (download and parse the product monograph)
- Detailed mechanism of action data (e.g. from DrugBank)
- A mechanistic rationale connecting oxytocin receptor agonism to isotretinoin-like syndrome, supported by preclinical or literature evidence
- Route and formulation compatibility assessment (the Canadian products' dosage forms and approved indications are not specified)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

