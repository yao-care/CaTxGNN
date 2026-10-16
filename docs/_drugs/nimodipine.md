---
layout: default
title: Nimodipine
parent: Model Prediction Only (L5)
nav_order: 652
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Nimodipine: predicted new indication Homozygous familial hypercholesterolemia (evidence level L5). Approved use: Subarachnoid hemorrhage (including acquired aneurysmal subarachnoid h…"
monitor_inn: "NIMODIPINE"
predicted_indications: ["homozygous familial hypercholesterolemia", "nephrogenic syndrome of inappropriate antidiuresis"]
---

# Nimodipine
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

# Nimodipine: From Subarachnoid Hemorrhage to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Nimodipine is a calcium channel blocker originally used to treat **subarachnoid hemorrhage**, including aneurysmal subarachnoid hemorrhage.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia**,
but **no clinical trials and no publications** currently support this direction. The prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Subarachnoid hemorrhage (including acquired aneurysmal subarachnoid hemorrhage) |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, nimodipine is a dihydropyridine L-type calcium channel blocker with preferential activity on cerebral blood vessels. Its benefit in subarachnoid hemorrhage is established.

The link to the predicted indication is weak. Homozygous familial hypercholesterolemia is caused by defects in the LDL receptor pathway (LDLR, APOB, PCSK9, LDLRAP1). Nimodipine does not act on this pathway. Some calcium channel blockers have shown modest anti-atherosclerotic effects in preclinical models, but these do not correct the underlying LDL-receptor deficiency.

The high score (0.993) most likely reflects network-level associations, such as shared cardiovascular or lipid-related nodes in the knowledge graph. It does not reflect a validated biological mechanism.

A second prediction, **nephrogenic syndrome of inappropriate antidiuresis** (score 99.05%), has the same problem. That condition is driven by gain-of-function variants in the vasopressin V2 receptor. No known pathway lets nimodipine counteract this signaling. Nimodipine's blood-pressure-lowering effect and the risk of low sodium in neurocritical care settings would call for caution. This prediction also has no clinical or literature support and is also rated L5 / Hold.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02325926 | NIMOTOP | Not specified | Not specified |

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: liver disease, gallbladder disease, hypotensive disorder. These come from drug-disease relationships in the TxGNN knowledge graph and must be confirmed against the official product label.
- **Drug Interactions**: 100 interactions were identified in total. Representative examples are listed below.
  - **Major**: clarithromycin, dolasetron
  - **Moderate**: bupropion, aprepitant, morphine, acetylsalicylic acid, cimetidine, miconazole, canagliflozin, dapagliflozin, empagliflozin, magnesium sulfate, kanamycin, neomycin, dronabinol, nabilone, and several calcium salts (calcium carbonate, calcium chloride, calcium acetate, calcium phosphate)

Official warnings and contraindications from the Health Canada product monograph were not available. Please refer to the package insert for complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trial or literature support (evidence level L5). Its mechanistic basis is also weak: nimodipine does not act on the LDL-receptor pathway that causes homozygous familial hypercholesterolemia. The high model score alone is not enough to justify moving forward.

**To proceed, the following is needed:**
- Mechanism of action data for nimodipine, to allow a proper mechanistic assessment
- Preclinical or mechanistic evidence that nimodipine affects LDL metabolism or the LDL-receptor pathway
- A literature and trial search specific to calcium channel blockers in familial hypercholesterolemia
- The Health Canada product monograph (warnings, contraindications, approved indication, dosage form), which is required for any safety screening
- A review of the hypotension and drug-interaction profile (especially CYP3A4 inhibitors such as clarithromycin) for the target patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

