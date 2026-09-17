---
layout: default
title: Romidepsin
parent: Model Prediction Only (L5)
nav_order: 692
evidence_level: L5
indication_count: 10
---

# Romidepsin
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

# Romidepsin: From Unspecified Original Indication to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

Romidepsin's original approved indication could not be determined from this evidence pack — the drug is not currently marketed in Canada and no indication text was retrieved. The TxGNN model predicts potential efficacy for **Dermatofibrosarcoma Protuberans**, but this is currently supported by **0 clinical trials** and only **2 tangential publications**, neither of which tested romidepsin directly.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (data gap; drug not marketed in Canada) |
| Predicted New Indication | Dermatofibrosarcoma Protuberans |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data for romidepsin is not available in this evidence pack, and no original approved indication could be retrieved — the drug is not currently marketed in Canada.

Evidence annotations embedded in the predicted-indication rationale characterize romidepsin as a histone deacetylase (HDAC) inhibitor, and a clinical trial summary elsewhere in this same evidence pack (NCT00112463) describes it as a chemotherapy agent that "works ... by killing tumor cells or stopping them from dividing." The rationale hypothesizes that HDAC inhibition could theoretically affect fibroblastic tumor cell proliferation, which is biologically plausible given that dermatofibrosarcoma protuberans is a fibroblastic/mesenchymal neoplasm. However, no literature or trial in this evidence pack has directly tested romidepsin against this specific tumor type — the two related PMIDs are patient-derived cell-line establishment papers, not drug-testing studies.

Notably, this evidence pack also contains a **considerably better-supported** candidate that ranks lower by TxGNN score: **liposarcoma (rank 9)**, backed by a completed Phase 2 trial of romidepsin in metastatic/unresectable soft tissue sarcoma (NCT00112463, n=40) and preclinical data showing HDAC2 inhibition reduces MDM2 expression in dedifferentiated liposarcoma. The HDAC-inhibitor mechanism appears more clinically actionable for that indication than for the top-ranked dermatofibrosarcoma protuberans prediction discussed here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37490236](https://pubmed.ncbi.nlm.nih.gov/37490236/) | 2023 | Preclinical (cell line establishment) | Human Cell | Establishment of NCC-DFSP4-C1 cell line from a DFSP patient with fibrosarcomatous transformation; does not test romidepsin |
| [30411273](https://pubmed.ncbi.nlm.nih.gov/30411273/) | 2019 | Preclinical (cell line establishment) | In Vitro Cell Dev Biol Anim | Establishment of NCC-DFSP1-C1/DFSP2-C1 patient-derived cell lines; does not test romidepsin |

## Canada Market Information

Romidepsin is currently **not marketed in Canada** — no DIN records are available in this evidence pack (0 licenses on file).

## Cytotoxicity

Romidepsin is classified as antineoplastic based on evidence-pack trial descriptions (chemotherapy agent tested across multiple sarcoma indications).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — Histone deacetylase (HDAC) inhibitor |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Cytotoxic drug handling precautions likely apply given antineoplastic/chemotherapy classification; confirm per institutional cytotoxic handling protocol |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (dermatofibrosarcoma protuberans) is supported only by a TxGNN model score, with zero clinical trials and no literature that directly tests romidepsin — this meets the L5/S0 threshold in the evidence pack's own scoring, which is below the bar for advancing.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (currently a Blocking data gap — DG001)
- Original MOA and approved indication data (DG002)
- Direct preclinical or clinical evidence testing romidepsin specifically in dermatofibrosarcoma protuberans or related fibroblastic neoplasms
- Consider redirecting evaluation effort toward **liposarcoma (rank 9)**, which already has a completed Phase 2 trial and preclinical mechanistic support and warrants its own dedicated assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

