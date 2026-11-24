---
layout: default
title: Romidepsin
parent: Model Prediction Only (L5)
nav_order: 821
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "ROMIDEPSIN"
predicted_indications: ["dermatofibrosarcoma protuberans", "fibroblastic neoplasm", "kidney fibrosarcoma", "heart fibrosarcoma", "conventional fibrosarcoma", "familial rhabdoid tumor", "low grade fibromyxoid sarcoma", "liver fibrosarcoma", "liposarcoma", "uterine corpus perivascular epithelioid cell tumor"]
description: "Romidepsin: predicted new indication Dermatofibrosarcoma protuberans (evidence level L5). In Canada: 1 DIN (1 marketed)"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Romidepsin: Dermatofibrosarcoma protuberans
{: .text-alpha }

## One-Sentence Summary

Romidepsin is a drug originally used to treat T-cell lymphomas, including primary cutaneous T-cell lymphoma and peripheral T-cell lymphoma.
The TxGNN model predicts it may be effective for **dermatofibrosarcoma protuberans (DFSP)**, but there are **0 clinical trials** and only **2 publications** (both patient-derived cell line reports that do not test romidepsin), so the prediction rests almost entirely on the computational model.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Dermatofibrosarcoma protuberans |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 1 of 1) |
| Number of DINs | 1 (marketed: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for romidepsin: "Romidepsin is a histone deacetylase (HDAC) inhibitor. HDACs catalyze the removal of acetyl groups from acetylated lysine residues in histones, resulting in the modulation of gene expression. HDACs also deacetylate non-histone proteins, such as transcription factors." ([DailyMed: romidepsin prescribing information, Amneal Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=61894b77-f29c-4a81-ad85-bd3a698233a4), label version 2025-09-04; accessed 2026-11-19.) Based on known information, romidepsin is a class I histone deacetylase (HDAC) inhibitor. Its efficacy in T-cell lymphoma has been established, and by changing gene expression through epigenetic regulation it may in principle be applicable to other tumours.

DFSP is a low-grade skin sarcoma driven by a COL1A1–PDGFB fusion gene. It is quite different from T-cell lymphoma in cell type and biology. The link is only a computational prediction (high TxGNN score). No direct drug-disease connection has been demonstrated. The two retrieved papers describe the establishment of patient-derived DFSP cell lines, which are useful as future test models but do not test romidepsin.

For context, the same prediction list also includes liposarcoma, where a preclinical study suggests HDAC2 inhibition lowers MDM2 expression in dedifferentiated liposarcoma. That is a separate indication and does not support DFSP.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for dermatofibrosarcoma protuberans.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37490236](https://pubmed.ncbi.nlm.nih.gov/37490236/) | 2023 | Preclinical (cell line) | Human Cell | Establishment of NCC-DFSP4-C1, a cell line from DFSP with fibrosarcomatous transformation; no romidepsin testing reported |
| [30411273](https://pubmed.ncbi.nlm.nih.gov/30411273/) | 2019 | Preclinical (cell line) | In Vitro Cell Dev Biol Anim | Establishment of two DFSP cell lines (NCC-DFSP1-C1, NCC-DFSP2-C1) carrying the COL1A1-PDGFB translocation; no romidepsin testing reported |

---

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02414295 | ISTODAX | ROMIDEPSIN | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted epigenetic therapy (HDAC inhibitor), used as an antineoplastic agent |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with differential, liver and renal function, electrolytes (especially potassium), ECG |
| Handling Protection | Follow institutional cytotoxic drug handling regulations |

---

## Safety Considerations

- **Disease-related cautions (knowledge graph, not label text)**: The TxGNN knowledge graph lists the following conditions as contraindication-related: long QT syndrome (including familial), heart conduction disease, sudden cardiac arrest, potassium deficiency, thrombocytopenia, neutropenia, agranulocytosis, leukopenia, lymphopenia, anaemia (including macrocytic), liver disease, gallbladder disease, chronic kidney disease, chronic renal failure and end-stage renal failure. These should be verified against the Canadian product monograph.
- **Drug Interactions**: 100 interactions were found. Examples shown include:
  - **Major**: dolasetron
  - **Moderate**: ondansetron, palonosetron, clarithromycin, levofloxacin, miconazole, dexamethasone, famotidine, loperamide, rolapitant, eliglustat, and several laxatives or bowel-preparation agents (bisacodyl, picosulfuric acid, polyethylene glycol, lactulose, lactitol, sodium sulfate, castor oil)
  - **Minor**: metronidazole

  Many of these involve QT-prolonging or electrolyte-altering drugs, which is consistent with the cardiac and potassium cautions above.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (0.9992), but it is not backed by any clinical trial or any study testing romidepsin in DFSP. The two retrieved papers are cell line establishment reports. The evidence is model prediction only (L5).

**To proceed, the following is needed:**
- Preclinical testing of romidepsin in the available DFSP patient-derived cell lines, with attention to the COL1A1–PDGFB pathway
- Mechanism of action data (MOA), for example from DrugBank
- Health Canada package insert warnings and contraindications, which are required before safety screening
- A cardiac (QT) and haematological safety plan for any future study, given the interaction and contraindication signals
- A comparison with other predicted indications such as liposarcoma, where a Phase 2 soft tissue sarcoma trial (NCT00112463) and a mechanistic preclinical study already exist

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: romidepsin prescribing information, Amneal Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=61894b77-f29c-4a81-ad85-bd3a698233a4) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

