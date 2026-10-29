---
layout: default
title: Memantine
parent: Model Prediction Only (L5)
nav_order: 583
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-30
description: "Memantine: predicted new indication Pulmonary hypertension (evidence level L5). Approved use: Not specified in the data compiled for this report"
monitor_inn: "Memantine"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "kyphoscoliotic heart disease", "migraine with brainstem aura"]
---

# Memantine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Memantine: From Its Original Indication to Pulmonary Hypertension
{: .text-alpha }

## One-Sentence Summary

Memantine is a single-ingredient drug that is currently marketed in Canada, although the data compiled for this report do not list its approved indication.
The TxGNN model predicts it may be effective for **pulmonary hypertension**, but this is a model prediction only.
There are **0 clinical trials** and **2 publications**, and neither publication studies memantine in this disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the data compiled for this report |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 0.9954 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 9 of 10) |
| Number of DINs | 10 (valid: 9) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Memantine is generally described as a non-competitive NMDA receptor antagonist. Under that mechanism, the glutamate/NMDA receptor pathway is the plausible link to pulmonary hypertension.

One preclinical publication notes that the glutamate/NMDA receptor axis has been implicated in acute lung injury, pulmonary arterial hypertension and diabetes. This suggests NMDA receptors in the pulmonary vasculature as a possible target. The link is plausible but unproven. No study in the compiled data tests memantine itself in pulmonary hypertension.

The other publication concerns MN-08, a nitrate derivative of memantine under development for pulmonary arterial hypertension. It is a Phase 1 safety and pharmacokinetic study in healthy volunteers. It shows that the memantine scaffold is being explored for this disease, but it is a different compound and says nothing about the efficacy of memantine.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33500723](https://pubmed.ncbi.nlm.nih.gov/33500723/) | 2021 | Preclinical/Mechanistic | Theranostics | Activation of NMDA receptors regulates insulin sensitivity and lipid metabolism. The introduction notes that the glutamate/NMDA receptor axis has been implicated in pulmonary arterial hypertension, but the study itself focuses on metabolism. |
| [41739394](https://pubmed.ncbi.nlm.nih.gov/41739394/) | 2026 | Phase 1 PK/Safety (different compound) | Clinical Drug Investigation | Single and multiple ascending doses of MN-08, a nitrate derivative of memantine under development for pulmonary arterial hypertension, were studied in healthy Chinese volunteers for safety, tolerability and pharmacokinetics. |

There are currently no registered clinical trials of memantine for pulmonary hypertension.

---

## Canada Market Information

Ten valid single-ingredient licenses are listed (none cancelled). The five main ones are below. The data compiled for this report do not include dosage forms or approved indication text for these products.

| DIN | Product Name |
|---------|------|
| 02260638 | EBIXA |
| 02324067 | ACT MEMANTINE |
| 02375532 | SANDOZ MEMANTINE FCT |
| 02366487 | APO-MEMANTINE |
| 02348950 | RIVA-MEMANTINE |

---

## Safety Considerations

- **Contraindication signals from the knowledge graph:** The TxGNN knowledge graph links memantine to liver disease, gallbladder disease and impaired renal function. These come from drug-disease contraindication edges, not from package insert text, and should be verified against the label.
- **Drug Interactions:** The data record 100 interactions in total. The main ones are listed below.
  - **Moderate:** anticholinergic and antimuscarinic agents, including hyoscyamine, atropine, glycopyrronium, clidinium, dicyclomine, methscopolamine, propantheline, scopolamine, trospium and mepenzolate.
  - **Minor:** ranitidine, metformin, cimetidine and potassium citrate.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (0.9954), but the evidence is model prediction only (L5). There are no clinical trials, and neither retrieved publication evaluates memantine in pulmonary hypertension. The only disease-specific lead is a different compound (MN-08).

By comparison, another predicted indication for memantine, **migraine disorder**, has a completed Phase 3 trial (NCT04698525, n=33, versus sodium valproate) and several reviews and meta-analyses. It may be a better candidate for follow-up, although the evidence there is also described as limited.

**To proceed, the following is needed:**
- Preclinical or clinical studies of memantine itself in pulmonary hypertension, such as animal models of pulmonary vascular disease
- Mechanism of action data for memantine
- Health Canada package insert warnings and contraindications, including the approved indication text for each license
- Review of the knowledge-graph contraindication signals (liver, gallbladder and renal impairment) against the label
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

