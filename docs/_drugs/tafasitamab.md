---
layout: default
title: Tafasitamab
parent: Model Prediction Only (L5)
nav_order: 872
evidence_level: L5
indication_count: 10
---

# Tafasitamab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Tafasitamab: From Diffuse Large B-Cell Lymphoma to Drug-Induced Osteoporosis

## One-Sentence Summary

Tafasitamab (brand name MINJUVI) is an anti-CD19 antibody used to treat B-cell lymphoma.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**,
but **0 clinical trials** and **0 publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diffuse large B-cell lymphoma (inferred from a published case report; no indication text is recorded in the Canadian license data) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 98.71% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the record. Tafasitamab is an anti-CD19 monoclonal antibody. Its known activity is depleting B cells through antibody-dependent cellular cytotoxicity (ADCC) and phagocytosis (ADCP).

We found no plausible link between B-cell depletion and bone remodeling, so the prediction is **not mechanistically supported**. The high score (0.987) most likely reflects proximity in the TxGNN knowledge graph rather than biology.

The other top-ranked predictions show the same pattern:
- **Diabetic retinopathy (including severe non-proliferative)**: no established role for CD19-directed therapy. The two entries are parent and child terms, so they are not independent evidence.
- **HER2-positive, progesterone-receptor positive and negative, luminal A/B, and normal breast-like breast carcinoma**: CD19 is not expressed on breast carcinoma cells, so direct antitumour activity is not expected. Several of these entries share an identical score, which suggests duplicated graph signals.
- **Psoriasis**: the disease is mainly driven by T cells and the IL-23/IL-17 pathway, so the case for CD19 targeting is weak.

The 19 publications retrieved for the "breast tumor luminal A or B" prediction (10 shown) are keyword false positives. They cover B cells, hepatitis B vaccines and HLA-B alleles, and say nothing about tafasitamab or breast tumours. They should not be counted as evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

Among the lower-ranked predictions, the only relevant paper is a 2023 case report (PMID [37701883](https://pubmed.ncbi.nlm.nih.gov/37701883/), JAAD Case Reports). It describes pityriasis lichenoides chronica in a patient receiving tafasitamab plus lenalidomide for diffuse large B-cell lymphoma. This is anecdotal and cannot separate the drug effect from lenalidomide or the lymphoma. It is a possible adverse-event signal, not evidence of benefit.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2518627 | MINJUVI |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-CD19 monoclonal antibody) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is based only on a model score, with no clinical trials or supporting literature. No biological link between CD19-directed B-cell depletion and bone remodeling has been identified. Every other top-ranked prediction has the same weakness.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which block safety screening
- Detailed mechanism of action data (MOA), for example from the DrugBank API
- Original approved indication text for the Canadian license
- Preclinical or observational evidence linking B-cell or CD19 biology to bone loss
- A review of the pityriasis lichenoides case as a possible safety signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

