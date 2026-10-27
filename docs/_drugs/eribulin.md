---
layout: default
title: Eribulin
parent: Model Prediction Only (L5)
nav_order: 344
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Eribulin: predicted new indication Fibroblastic neoplasm (evidence level L5). Approved use: Liposarcoma"
monitor_inn: "Eribulin"
predicted_indications: ["autosomal recessive familial Mediterranean fever", "dermatofibrosarcoma protuberans", "pleural mesothelioma", "malignant peritoneal mesothelioma", "ovarian myxoid liposarcoma", "pleural adenomatoid tumor", "pleural biphasic mesothelioma", "fibroblastic neoplasm", "pleural epithelioid mesothelioma", "heart fibrosarcoma"]
---

# Eribulin
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

## Eribulin: From Liposarcoma to Fibroblastic Neoplasm
{: .text-alpha }

## One-Sentence Summary

Eribulin is a microtubule-targeting chemotherapy originally used for liposarcoma.
The TxGNN model predicts it may be effective for **fibroblastic neoplasm** (the best-supported of the top 10 predictions, which is why it is reported here rather than the rank-1 prediction), with **1 completed Phase 2 clinical trial** and **8 publications** (mostly preclinical) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Liposarcoma (the Health Canada licence records compiled for this report contain no indication text) |
| Predicted New Indication | Fibroblastic neoplasm (TxGNN rank 8 of 10; rank 1 is autosomal recessive familial Mediterranean fever, which has no supporting evidence) |
| TxGNN Prediction Score | 99.36% (rank 8 candidate) |
| Evidence Level | L2 (one completed Phase 2 trial, small and without reported results) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold (research question: further evidence needed) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, eribulin is a microtubule dynamics inhibitor (an antimitotic cytotoxic agent). Its efficacy in liposarcoma has been established, and it has activity in other soft tissue sarcomas.

Fibroblastic neoplasms include solitary fibrous tumour (SFT), fibrosarcoma and myxofibrosarcoma. These are mesenchymal tumours closely related to liposarcoma, so a class-level rationale exists for an anti-tubulin agent.

Supporting signals:
- A completed Phase 2 study (ERASING) tested eribulin directly in advanced SFT.
- Preclinical work in HT1080 fibrosarcoma cells shows sensitivity to eribulin, along with acquired resistance. Recombinant methioninase partly reversed that resistance in cells and in nude mice.
- Patient-derived SFT xenograft work suggested potential effectiveness of eribulin or trabectedin.

Other predictions in the top 10 are weaker. Several (pleural, peritoneal and other mesotheliomas, adenomatoid tumour, heart fibrosarcoma) have no trials or literature. Dermatofibrosarcoma protuberans has only an indirect general sarcoma review. Ovarian myxoid liposarcoma largely reflects the existing liposarcoma indication. The familial Mediterranean fever prediction has no apparent mechanistic basis for a cytotoxic drug.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03840772](https://clinicaltrials.gov/study/NCT03840772) | Phase 2 | Completed | 16 | ERASING: Italian Sarcoma Group Phase II study of eribulin in advanced solitary fibrous tumour. Results were not available in the data compiled. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38136399](https://pubmed.ncbi.nlm.nih.gov/38136399/) | 2023 | Review | Cancers | Diagnosis and treatment of extrameningeal solitary fibrous tumours; NAB2-STAT6 fusion is a common feature. |
| [28284173](https://pubmed.ncbi.nlm.nih.gov/28284173/) | 2017 | Preclinical (xenograft) | Eur J Cancer | Patient-derived SFT xenografts predicted high sensitivity to doxorubicin/dacarbazine, and suggested trabectedin or eribulin may be effective. |
| [38423656](https://pubmed.ncbi.nlm.nih.gov/38423656/) | 2024 | Preclinical (in vitro) | Anticancer Res | Recombinant methioninase and eribulin act synergistically against fibrosarcoma cells but not normal fibroblasts. |
| [39197933](https://pubmed.ncbi.nlm.nih.gov/39197933/) | 2024 | Preclinical (in vitro) | Anticancer Res | Methioninase increased eribulin efficacy 16-fold in highly eribulin-resistant HT1080 fibrosarcoma cells. |
| [40295012](https://pubmed.ncbi.nlm.nih.gov/40295012/) | 2025 | Preclinical | In Vivo | Super-eribulin-resistant HT1080 cells became more malignant, but were arrested by methionine restriction plus eribulin in nude mice. |
| [39625530](https://pubmed.ncbi.nlm.nih.gov/39625530/) | 2024 | Preclinical (cell line) | Hum Cell | Establishment of the SMU-MFS myxofibrosarcoma cell line, a model for developing new therapies. |
| [34383271](https://pubmed.ncbi.nlm.nih.gov/34383271/) | 2021 | Preclinical (cell line) | Hum Cell | Establishment of the NCC-MFS4-C1 myxofibrosarcoma cell line; myxofibrosarcoma is described as refractory to chemotherapy. |
| [35906852](https://pubmed.ncbi.nlm.nih.gov/35906852/) | 2023 | Case report | Genes Chromosomes Cancer | Response to entrectinib in an MPNST with an NTRK3 fusion; only indirectly relevant to eribulin. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02377438 | HALAVEN | Not listed | Not listed |
| 02539136 | NAT-ERIBULIN | Not listed | Not listed |
| 02545950 | ERIBULIN MESYLATE INJECTION | Not listed | Not listed |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (microtubule dynamics inhibitor, antimitotic) |
| Myelosuppression Risk | High. Neutropenia and thrombocytopenia appear among the knowledge-graph contraindications; agranulocytosis is also listed |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with differential, electrolytes (including potassium), ECG (QT interval), and neurological assessment for peripheral neuropathy |
| Handling Protection | Follow institutional cytotoxic drug handling regulations |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text): long QT syndrome (including familial), thrombocytopenia, potassium deficiency, neutropenia, agranulocytosis, peripheral nervous system disease, peripheral neuropathy, and constipation disorder.
- **Drug Interactions**: 100 interactions were identified in total. Major-level examples are **dolasetron** and **cisapride** (consistent with additive QT-prolongation risk). Moderate-level examples include ondansetron, palonosetron, clarithromycin, levofloxacin, metronidazole, tinidazole, rosuvastatin, simvastatin, famotidine, loperamide, and several laxatives and bowel-preparation agents (bisacodyl, picosulfuric acid, polyethylene glycol, lactulose, lactitol, castor oil, sodium sulfate).

Package insert warnings and contraindications were not available, so please refer to the Canadian product monograph for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold** (research question)

**Rationale:**
Eribulin has a plausible class-level link to fibroblastic neoplasms, and one completed Phase 2 trial in SFT exists. However, that trial is small (n=16) with no results available, and the remaining literature is mostly preclinical. The other nine top predictions have no or only indirect evidence.

**To proceed, the following is needed:**
- Results of the ERASING trial (NCT03840772), including response rate and progression-free survival
- Confirmation in larger or comparative studies in SFT, fibrosarcoma and myxofibrosarcoma
- Health Canada product monograph warnings, contraindications and approved indication text (currently missing, and blocking safety screening)
- Mechanism of action data from DrugBank
- A safety plan covering QT prolongation, myelosuppression and peripheral neuropathy, and review of the major interactions (dolasetron, cisapride)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

