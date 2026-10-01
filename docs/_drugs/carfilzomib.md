---
layout: default
title: Carfilzomib
parent: Model Prediction Only (L5)
nav_order: 158
evidence_level: L5
indication_count: 5
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

# Carfilzomib: From Multiple Myeloma to Melanoma (Lead Prediction: CMM7)

## One-Sentence Summary

Carfilzomib is an irreversible proteasome inhibitor, marketed in Canada as KYPROLIS. It is known as a myeloma drug, although the Canadian licence records here contain no indication text.
The TxGNN model predicts it may be effective for **CMM7** and four other melanoma-type conditions, each scoring above 99%.
Evidence is thin: **0 clinical trials** for any prediction and **5 preclinical or computational publications**, all under the general "melanoma" prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence data. The literature describes carfilzomib as a frontline anti-myeloma drug (multiple myeloma) |
| Predicted New Indication | CMM7 (a melanoma-related condition) |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L5 for CMM7 (model prediction only); L4 for the general "melanoma" prediction |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

**All predictions returned (all melanoma-related):**

| Rank | Predicted Indication | Score | Evidence Level | Recommendation |
|------|------|------|------|------|
| 1 | CMM7 | 99.37% | L5 | Hold |
| 2 | Pediatric leptomeningeal melanoma | 99.30% | L5 | Hold |
| 3 | Epithelioid cell uveal melanoma | 99.23% | L5 | Hold |
| 4 | Vulvar melanoma | 99.19% | L5 | Hold |
| 5 | Melanoma | 99.03% | L4 | Research Question |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the record. Carfilzomib is an irreversible inhibitor of the 20S proteasome. Its efficacy in myeloma is well known. Mechanistically, blocking proteasome-dependent survival pathways could also matter in melanoma.

The only direct support is a 2021 cell-line study in murine B16-F1 melanoma cells. It reported that carfilzomib combined with bortezomib increased apoptosis, with caspase activation. This is preclinical and indirect. It does not show benefit in humans.

For the specific predictions, the link is weaker:
- **CMM7:** no CMM7-specific mechanism is supported by the data.
- **Pediatric leptomeningeal melanoma:** CNS penetration is uncertain, and paediatric safety and pharmacokinetics cannot be assessed.
- **Epithelioid cell uveal melanoma:** uveal melanoma is biologically different from cutaneous melanoma, so cutaneous preclinical data cannot be assumed to transfer.
- **Vulvar melanoma:** the link rests on the shared melanoma ontology, with no mucosal-melanoma data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered, for CMM7 or for any of the other four predictions.

---

## Literature Evidence

Nothing was retrieved for CMM7. The five publications below were retrieved for the general **melanoma** prediction (rank 5).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | In vitro (murine cell line) | Biology | Carfilzomib plus bortezomib induced apoptosis in B16-F1 melanoma cells, with activation of caspases 3, 8, 9 and 12 |
| [36134605](https://pubmed.ncbi.nlm.nih.gov/36134605/) | 2023 | Computational | J Biomol Struct Dyn | Docking and dynamics screening of clinical drugs against cancer kinase targets across ten cancer types, including melanoma. The direct link to carfilzomib is unclear from the available text |
| [31540997](https://pubmed.ncbi.nlm.nih.gov/31540997/) | 2019 | Preclinical mechanistic | Mol Cancer Res | The AIRAP-like gene (ZFAND2A) regulates cell survival in human melanoma via the E3 ligase cIAP2. The direct link to carfilzomib is unclear from the available text |
| [29581547](https://pubmed.ncbi.nlm.nih.gov/29581547/) | 2018 | Preclinical mechanistic | Leukemia | BET-targeting PROTACs, which degrade BET proteins via the proteasome, were active in multiple myeloma models. Melanoma relevance is indirect |
| [27016342](https://pubmed.ncbi.nlm.nih.gov/27016342/) | 2016 | Preclinical mechanistic | Matrix Biol | Bortezomib and carfilzomib activated NF-κB and raised heparanase expression in tumour cells, which is associated with a more aggressive phenotype. This is a possible resistance or safety signal |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2459949 | KYPROLIS |
| 2451034 | KYPROLIS |
| 2459930 | KYPROLIS |

Dosage form and approved indication text are not recorded for these licences.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (proteasome inhibitor), used as an anticancer agent |

Please refer to the package insert warnings and precautions for myelosuppression risk, emetogenicity, monitoring items and handling protection.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the dataset.

One preclinical signal is worth noting (PMID 27016342): proteasome inhibitors upregulated heparanase through NF-κB, which is linked to a more aggressive tumour phenotype.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top four predictions are model signals only (L5), with no trials or literature. The general melanoma prediction has only preclinical or computational support (L4) and no human efficacy or safety data.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data from DrugBank
- Approved indication text and dosage forms for the three KYPROLIS DINs
- Melanoma-specific preclinical work, in vivo where possible, testing carfilzomib alone rather than only in combination with bortezomib
- Clarification of what "CMM7" refers to, and a subtype-specific rationale for the uveal, vulvar and paediatric leptomeningeal predictions
- Route-of-administration compatibility assessment, including CNS penetration for the leptomeningeal setting

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

