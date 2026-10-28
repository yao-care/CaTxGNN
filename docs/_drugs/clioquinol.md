---
layout: default
title: Clioquinol
parent: Model Prediction Only (L5)
nav_order: 207
evidence_level: L5
indication_count: 2
monitor_inn: "CLIOQUINOL"
predicted_indications: ["ectothrix infectious disease", "endothrix infectious disease"]
last_modified_at: 2026-10-23
description: "Clioquinol: predicted new indication Ectothrix infectious disease (evidence level L5). Approved use: Tinea pedis, tinea corporis, tinea infection…"
---

# Clioquinol
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

## Clioquinol: From Tinea Infections to Ectothrix Infectious Disease
{: .text-alpha }

## One-Sentence Summary

Clioquinol is a topical halogenated hydroxyquinoline used in dermatophyte skin infections such as tinea pedis and tinea corporis.
The TxGNN model predicts it may be effective for **ectothrix infectious disease**, a fungal infection of the outer hair shaft.
Currently there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tinea pedis, tinea corporis, tinea infection, dermatophytosis of groin and perianal area (relations recorded in the knowledge graph; no approved indication text is available in the Canadian licence records) |
| Predicted New Indication | Ectothrix infectious disease |
| TxGNN Prediction Score | 0.9926 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 3 of 3) |
| Number of DINs | 3 (valid: 3) |
| Number of approvals | 3 licences (DINs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, clioquinol is a topical halogenated hydroxyquinoline with antifungal and antibacterial activity. A commonly proposed mechanism is metal ion chelation affecting fungal enzymes, but this cannot be confirmed from the data compiled for this report.

Ectothrix infection is a dermatophyte infection in which fungal arthroconidia form on the outside of the hair shaft, typically from *Microsporum* and *Trichophyton* species. The high score (0.9926) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

There is an important limitation. Hair-shaft infections are difficult to treat with topical agents alone because penetration into the hair follicle is poor, and standard care usually relies on systemic antifungals. This weakens the extrapolation from superficial skin infections.

A second prediction, **endothrix infectious disease** (score 0.9919, fungus growing inside the hair shaft), has the same limitations. It also has no supporting trials or literature, and intrahair growth is even harder to reach with topical therapy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00074462 | LOCACORTEN VIOFORM | Not stated | Not stated |
| 00074454 | LOCACORTEN VIOFORM EARDROPS | Not stated | Not stated |
| 00074500 | VIOFORM HYDROCORTISONE | Not stated | Not stated |

All three licences are currently valid and are listed as single-ingredient records.

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

The following are disease relations recorded in the knowledge graph. They are not label text, but they merit review against the official labelling:
- **Contraindication relations in the knowledge graph:** adrenocortical insufficiency, Addison disease, skin atrophy, telangiectasis, capillary disease, hereditary hemorrhagic telangiectasia, peripheral vascular disease, intermittent vascular claudication, peripheral arterial disease.

No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is biologically plausible within the dermatophyte class, but it is supported only by a model score. No clinical trials or publications address ectothrix infection, so the evidence level is L5. Poor topical penetration into the hair shaft further limits confidence.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications and approved indication text (currently blocking for safety screening)
- Mechanism of action data for clioquinol (for example from DrugBank)
- Literature or in vitro data on clioquinol activity against ectothrix and endothrix dermatophytes
- Assessment of whether a topical route can adequately reach infected hair shafts, compared with systemic antifungal standard care
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

