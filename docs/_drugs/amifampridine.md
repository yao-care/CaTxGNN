---
layout: default
title: Amifampridine
parent: Model Prediction Only (L5)
nav_order: 48
evidence_level: L5
indication_count: 2
monitor_inn: "Amifampridine"
predicted_indications: ["glaucoma", "acute intermittent porphyria"]
last_modified_at: 2026-11-05
description: "Amifampridine: predicted new indication glaucoma (evidence level L5). In Canada: 2 DINs (2 marketed)"
---

# Amifampridine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Amifampridine: voltage-gated potassium channel blocker → glaucoma
{: .text-alpha }

## One-Sentence Summary

Amifampridine is a potassium channel blocker that is marketed in Canada. The TxGNN model predicts it may be relevant to **glaucoma**, but the data compiled for this report contain **no clinical trials and no publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | glaucoma |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 2 of 2) |
| Number of DINs | 2 (marketed: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Amifampridine blocks voltage-gated potassium channels. This prolongs depolarization at the nerve terminal and increases neurotransmitter release at the neuromuscular junction. According to the Mechanism of Action section of the US FDA-approved prescribing information for amifampridine: "The mechanism by which amifampridine exerts its therapeutic effect in LEMS patients has not been fully elucidated. Amifampridine is a broad-spectrum potassium channel blocker." ([DailyMed: Firdapse (amifampridine phosphate) prescribing information, Catalyst Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f015fe60-3128-4a43-8c31-19fc6b5def3f), label version 2026-04-16; accessed 2026-11-19.) This description reflects the general, known pharmacology of the drug class.

No clear link has been established between this mechanism and the pathophysiology of glaucoma, which involves intraocular pressure and loss of retinal ganglion cells. The high TxGNN score is a computational output only. It is not supported by any trial, publication or mechanistic study in the data compiled here. The prediction should be regarded as a hypothesis that requires independent biological justification before any further investment.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02502984 | FIRDAPSE | Not recorded | Not recorded |
| 02503034 | RUZURGI | Not recorded | Not recorded |

## Safety Considerations

- **Drug Interactions**: 68 interacting drugs were identified in the interaction database. Of the 20 listed in the data compiled for this report, one is rated **Major**: bupropion. The rest are rated Moderate, including:
  - Corticosteroids: hydrocortisone, betamethasone, dexamethasone, prednisolone, prednisone
  - Stimulants and anorectics: ephedrine, phentermine, fenfluramine, dexfenfluramine, diethylpropion, mazindol, sibutramine
  - Opioids: morphine (including liposomal) and opium
  - Other: levofloxacin, metoclopramide, dronabinol, polyethylene glycol (3350 with electrolytes)

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The glaucoma prediction has a high model score (0.9971) but no supporting trials, literature or established mechanism, so the evidence level is L5. There is no basis to advance it at this stage.

**To proceed, the following is needed:**
- A plausible mechanistic rationale linking potassium channel blockade to glaucoma pathophysiology
- Preclinical studies that directly address glaucoma
- Detailed mechanism of action data
- Package insert warnings and contraindications from Health Canada, for safety screening
- Assessment of route compatibility, since an ocular indication may require a different formulation or route of administration

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data are not available in the data compiled for this report, so t" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Firdapse (amifampridine phosphate) prescribing information, Catalyst Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f015fe60-3128-4a43-8c31-19fc6b5def3f) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

