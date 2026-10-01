---
layout: default
title: Romidepsin
parent: Model Prediction Only (L5)
nav_order: 814
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

# Romidepsin: From Its Licensed Use to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

Romidepsin is marketed in Canada as ISTODAX, but the Health Canada record provided does not state its approved indication.
The TxGNN model predicts it may be effective for **dermatofibrosarcoma protuberans (DFSP)**, but **0 clinical trials** and only **2 publications** relate to this prediction, and both publications are cell line establishment papers with no romidepsin data.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Health Canada data provided |
| Predicted New Indication | Dermatofibrosarcoma protuberans |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in DrugBank for this record. The Evidence Pack describes romidepsin as a class I histone deacetylase (HDAC) inhibitor. HDAC inhibitors alter gene expression and can slow tumor growth, which is why they are studied in several cancers.

DFSP is a low-grade skin sarcoma driven by a COL1A1-PDGFB gene fusion that keeps the PDGFB growth signal switched on. The prediction comes from the knowledge graph only. No source provided shows a direct link between HDAC inhibition and the COL1A1-PDGFB mechanism. No romidepsin sensitivity data in DFSP cells is included either.

The score is very high, but the other nine predicted indications score nearly the same (99.29% to 99.67%), so the score does not show that DFSP is a stronger candidate than the others.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37490236](https://pubmed.ncbi.nlm.nih.gov/37490236/) | 2023 | Preclinical (cell line) | Human Cell | Establishes NCC-DFSP4-C1, a cell line from a DFSP with fibrosarcomatous transformation, which has a poorer prognosis than classic DFSP |
| [30411273](https://pubmed.ncbi.nlm.nih.gov/30411273/) | 2019 | Preclinical (cell line) | In Vitro Cell Dev Biol Anim | Establishes two patient-derived DFSP cell lines (NCC-DFSP1-C1, NCC-DFSP2-C1) with the COL1A1-PDGFB translocation |

Both papers build research models. Neither reports romidepsin activity, so they could serve as future test systems but are not evidence of efficacy.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2414295 | ISTODAX |

Dosage form, manufacturer and approved indication text are not available in the data provided.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted epigenetic therapy (class I HDAC inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions; follow local cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The DFSP prediction rests on the model score alone (L5). There are no trials, and the only two papers are cell line establishment reports without romidepsin data. Safety and mechanism data are also missing.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications. This is currently a blocking gap for safety screening.
- Detailed mechanism of action data from DrugBank.
- Laboratory testing of romidepsin in the published DFSP cell lines (NCC-DFSP1-C1, NCC-DFSP2-C1, NCC-DFSP4-C1) to see whether the prediction holds.

**Related lead:** Among the ten predicted indications, only **liposarcoma** (rank 9, score 99.31%) has trials and mechanistic literature. These are a completed Phase 2 study in soft tissue sarcoma (NCT00112463, n=40), a completed Phase 1 azacitidine plus romidepsin study (NCT01537744, n=18), and a preclinical paper on HDAC2 inhibition and MDM2 in dedifferentiated liposarcoma (PMID 31620242). No outcome data is provided for either trial, so liposarcoma may be a more practical place to start. The first step would be to review the NCT00112463 results for a liposarcoma subgroup.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

