---
layout: default
title: Carfilzomib
parent: Model Prediction Only (L5)
nav_order: 160
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Carfilzomib: predicted new indication Melanoma (evidence level L5). Approved use: Plasma cell myeloma"
monitor_inn: "CARFILZOMIB"
predicted_indications: ["CMM7", "pediatric leptomeningeal melanoma", "epithelioid cell uveal melanoma", "vulvar melanoma (disease)", "melanoma"]
---

# Carfilzomib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Carfilzomib: From Plasma Cell Myeloma to Melanoma

## One-Sentence Summary

Carfilzomib is a proteasome-inhibitor-class drug originally used to treat plasma cell myeloma.
The TxGNN model predicts it may be effective for **Melanoma**, but no clinical trials are registered for this direction.
The evidence consists of only **4 publications**, all preclinical or computational, so this is best treated as a research question.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Plasma cell myeloma (from the knowledge graph; the Canadian licence records contain no indication text) |
| Predicted New Indication | Melanoma (rank 1 in the model output is CMM7, a melanoma-related entity; melanoma itself is ranked 5th and is the only prediction with any supporting literature, so it is the focus of this report) |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L4 (preclinical only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

Other melanoma-related predictions (CMM7, pediatric leptomeningeal melanoma, epithelioid cell uveal melanoma, vulvar melanoma) scored 99.2–99.4%, but all are model predictions only (L5), with no trials or publications.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, carfilzomib belongs to the proteasome inhibitor class and its efficacy in plasma cell myeloma is established. Mechanistically, it may be applicable to melanoma through proteotoxic stress and induction of cell death.

The only directly relevant finding is a 2021 laboratory study in which carfilzomib combined with bortezomib increased apoptosis (programmed cell death) in B16-F1 mouse melanoma cells. This is consistent with the idea that blocking protein degradation can push tumour cells toward death. However, it was tested in mouse cells in a dish, in combination with another proteasome inhibitor. It says little about carfilzomib alone or about effects in patients.

The other three publications are indirectly relevant at best: a computational docking screen, a melanoma cell-survival gene study, and a study on heparanase expression after myeloma drugs. Their link to carfilzomib in melanoma is unconfirmed. The prediction should be regarded as a hypothesis, not as evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | In vitro preclinical study | Biology | Carfilzomib plus bortezomib increased apoptosis and caspase activation in B16-F1 mouse melanoma cells |
| [36134605](https://pubmed.ncbi.nlm.nih.gov/36134605/) | 2023 | In silico docking/simulation | J Biomol Struct Dyn | Drug repurposing screen of clinical drugs against cancer kinase targets across ten cancer types, including melanoma |
| [31540997](https://pubmed.ncbi.nlm.nih.gov/31540997/) | 2019 | Preclinical/mechanistic | Mol Cancer Res | The AIRAPL gene regulates cell survival in human melanoma via cIAP2; relevance to carfilzomib unclear |
| [27016342](https://pubmed.ncbi.nlm.nih.gov/27016342/) | 2016 | Preclinical/mechanistic | Matrix Biol | Bortezomib and carfilzomib raised heparanase expression via NF-κB, linked to a more aggressive tumour phenotype; relevance to melanoma unclear |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02459949 | KYPROLIS | Not listed | Not listed |
| 02451034 | KYPROLIS | Not listed | Not listed |
| 02459930 | KYPROLIS | Not listed | Not listed |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (proteasome inhibitor), used as an anticancer agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; at minimum, complete blood count and liver and renal function are generally monitored for anticancer agents |
| Handling Protection | Follow institutional hazardous/cytotoxic drug handling regulations; please refer to the package insert |

## Safety Considerations

**Drug Interactions**: The interaction screen returned 100 interacting drugs. The 20 entries reviewed here include the following.
- **Major**: oxandrolone, oxymetholone, stanozolol, deferiprone, samarium (153Sm) lexidronam, aminocaproic acid, avatrombopag, antihemophilic factor (recombinant), von Willebrand factor, human C1-esterase inhibitor, recombinant factor VIIa, factor X, conestat alfa
- **Moderate**: metronidazole, tinidazole, naltrexone, rosuvastatin, simvastatin, palifermin, strontium chloride Sr-89

Warnings and contraindications from the Canadian package insert are not available in the data compiled for this report. Please refer to the package insert for these.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The melanoma prediction is supported only by laboratory and computational studies, with no clinical trials and no human efficacy or safety data. The one directly relevant study used mouse cells and a drug combination. The Canadian package insert warnings are also missing, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Obtain and review the Health Canada package insert (warnings and contraindications), which is currently a blocking gap
- Supplement the mechanism of action data
- Preclinical studies of carfilzomib alone in human melanoma models, including the specific subtypes (uveal, mucosal/vulvar, leptomeningeal) predicted by the model
- Review of melanoma literature and trial registries to check whether proteasome inhibitors have shown clinical activity in melanoma
- For pediatric or leptomeningeal use, assessment of CNS penetration and pediatric safety data
- Review of the major drug interactions listed above for any planned combination regimen
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

