---
layout: default
title: Tafasitamab
parent: Model Prediction Only (L5)
nav_order: 879
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Tafasitamab: predicted new indication Drug-induced osteoporosis (evidence level L5). Approved use: Relapsed or refractory diffuse large B-cell lymphoma"
monitor_inn: "Tafasitamab"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "HER2 positive breast carcinoma", "psoriasis", "progesterone-receptor positive breast cancer", "normal breast-like subtype of breast carcinoma", "breast tumor luminal A or B", "progesterone-receptor negative breast cancer", "pityriasis lichenoides"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Tafasitamab: From Diffuse Large B-Cell Lymphoma to Drug-Induced Osteoporosis

## One-Sentence Summary

Tafasitamab is a CD19-targeting monoclonal antibody that is marketed in Canada as MINJUVI and is used in diffuse large B-cell lymphoma (DLBCL), as shown in the literature compiled for this report.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**, but there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relapsed or refractory diffuse large B-cell lymphoma (from the literature; the Canadian license record has no indication text) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 98.71% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. From the published literature, tafasitamab is an Fc-modified, humanized anti-CD19 monoclonal antibody. It depletes B cells and is used with lenalidomide in relapsed or refractory DLBCL.

No mechanistic link has been identified between CD19 targeting and drug-induced bone loss. The high TxGNN score is a graph-based association. No clinical trials or publications support it, and the review of the data found no biological rationale connecting B-cell depletion to osteoporosis.

The other top predictions (diabetic retinopathy, several breast cancer subtypes, psoriasis) likewise have no supporting evidence. Treat this prediction as a hypothesis for screening, not as a development candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for drug-induced osteoporosis.

---

## Literature Evidence

Currently no related literature available for drug-induced osteoporosis.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02518627 | MINJUVI | Not specified | Not specified in the license record |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-CD19 monoclonal antibody), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions (complete blood count is generally advised for B-cell-directed therapy) |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

**Drug Interactions**: The interaction query returned 41 interactions in total. The first 20 records are available, of which the following are rated **Major**:
- Deferiprone
- Samarium (153Sm) lexidronam
- Adalimumab
- Baricitinib
- Certolizumab pegol
- Cladribine
- Leflunomide
- Natalizumab

Many of the remaining records are rated Moderate. They include strontium chloride Sr-89, roflumilast, chloramphenicol, alefacept, alemtuzumab, anakinra, azathioprine, canakinumab, dimethyl fumarate, niraparib and ocrelizumab. Most of these are immunosuppressive or myelosuppressive agents, so combined use may add to infection or blood-count risk.

**Other safety signal**: A published case report describes pityriasis lichenoides chronica in a patient taking tafasitamab plus lenalidomide. Lenalidomide is a confounder, but the case may be relevant for skin-event monitoring.

For warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (evidence level L5), with no clinical trials, no publications and no identified mechanistic link between CD19 B-cell depletion and drug-induced osteoporosis. The immunosuppressive profile and the extensive interaction list also add caution.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data (for example from DrugBank)
- A plausible biological rationale linking B-cell or CD19 biology to bone loss, supported by preclinical or mechanistic studies
- Original indication text for the Canadian license
- Reassessment of the other predicted indications; none has supporting evidence so far
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

