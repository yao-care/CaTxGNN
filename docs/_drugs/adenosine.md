---
layout: default
title: Adenosine
parent: Model Prediction Only (L5)
nav_order: 27
evidence_level: L5
indication_count: 1
monitor_inn: "ADENOSINE"
predicted_indications: ["obsolete bundle branch block"]
last_modified_at: 2026-10-28
description: "Adenosine: predicted new indication obsolete bundle branch block (evidence level L5). Approved use: Not recorded in the local data"
---

# Adenosine
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

## Adenosine: adenosine receptor agonist (antiarrhythmic) → obsolete bundle branch block
{: .text-alpha }

## One-Sentence Summary

Adenosine is an injectable drug that acts on adenosine receptors and slows conduction through the heart's atrioventricular node.
The TxGNN model predicts it may be effective for **obsolete bundle branch block**, but **no clinical trials and no publications** currently support this direction.
The term "obsolete" marks a deprecated disease label, so this prediction may be an artifact of the disease ontology rather than a genuine therapeutic signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | obsolete bundle branch block |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 3 of 3) |
| Number of DINs | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. In general, adenosine is known to slow conduction through the atrioventricular (AV) node and is used diagnostically and therapeutically in rhythm disturbances involving rapid heart rates.

The model gives this prediction a very high score (0.9994), but the score reflects a computational pattern only. No clinical trial or publication was found that studies adenosine in bundle branch block. Because the disease term is flagged as obsolete, the prediction may reflect a deprecated ontology entry. No direct therapeutic rationale is evident, and a drug that slows cardiac conduction could even worsen conduction disturbances. The mechanistic link is therefore weak and should not be treated as support for use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02457474 | ADENOSINE INJECTION | Injection | Not recorded in local data |
| 02457482 | ADENOSINE INJECTION | Injection | Not recorded in local data |
| 02267659 | ADENOSINE INJECTION | Injection | Not recorded in local data |

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the interaction screening. Examples of those rated Major: cisapride, dolasetron and papaverine. Examples rated Moderate: famotidine, clarithromycin, granisetron, levofloxacin, ondansetron and palonosetron. Several of these (cisapride, dolasetron, granisetron, ondansetron, palonosetron, clarithromycin, levofloxacin) are agents that can affect cardiac rhythm, which deserves particular attention in a conduction-disorder setting.
- Please also refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no supporting trials or publications, and the disease term is obsolete. Adenosine's effect on cardiac conduction raises a plausible safety concern rather than a benefit in bundle branch block.

**To proceed, the following is needed:**
- Confirmation of whether the disease term maps to a current, clinically meaningful condition
- A clear mechanistic rationale and preclinical or clinical evidence in the relevant condition
- Package insert warnings and contraindications from Health Canada for safety screening
- Mechanism of action data for adenosine
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

