---
layout: default
title: Sorafenib
parent: Model Prediction Only (L5)
nav_order: 863
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Sorafenib: predicted new indication Liposarcoma (evidence level L5). Approved use: Hepatocellular carcinoma, renal cell carcinoma, thyroid carcinoma"
monitor_inn: "SORAFENIB"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "female breast carcinoma", "renal pelvis carcinoma", "vulva sarcoma", "dermatofibrosarcoma protuberans"]
---

# Sorafenib
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

# Sorafenib: From Hepatocellular Carcinoma to Liposarcoma

## One-Sentence Summary

Sorafenib is a multikinase inhibitor originally used to treat hepatocellular carcinoma, renal cell carcinoma and thyroid carcinoma.
The TxGNN model predicts it may be effective for **liposarcoma**, but the supporting evidence is limited to **1 clinical trial** (a Phase 2 study in mixed soft tissue sarcomas) and **8 publications**, most of which are reviews or preclinical studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hepatocellular carcinoma, renal cell carcinoma, thyroid carcinoma (the Health Canada licence record has no indication text) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L2 (one completed Phase 2 trial, single-arm, mixed sarcoma population) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold (pursue as a research question only) |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the compiled data. Based on known information, sorafenib is a multikinase inhibitor that blocks RAF/MEK/ERK signaling and the receptors VEGFR, PDGFR and KIT. Its efficacy in hepatocellular and renal cell carcinoma is established, and these pathways drive tumour growth and blood vessel formation.

Angiogenesis and MAPK signaling are plausible drivers in soft tissue sarcomas. Preclinical work in malignant peripheral nerve sheath tumour cells and dedifferentiated liposarcoma cell lines shows that sorafenib inhibits growth and MAPK signaling. This supports the biological rationale.

The clinical signal, however, comes from a mixed soft tissue sarcoma population and is not specific to liposarcoma. The prediction should be treated as a hypothesis to test, not a confirmed benefit.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | Completed | 51 | Single-arm study of sorafenib in advanced soft tissue sarcomas; liposarcoma is only a subset of the population |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | Phase 2 trial (SWOG S0505) | Cancer | Sorafenib, a multitargeted kinase inhibitor, tested in advanced soft tissue sarcomas with limited treatment options |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | Phase 1 trial | Ann Surg Oncol | Neoadjuvant conformal radiotherapy plus sorafenib in locally advanced extremity soft tissue sarcoma |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Ann Oncol | Treatment of soft tissue sarcomas is increasingly driven by histological subtype |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magy Onkol | Histology-based medical treatment of soft tissue sarcomas |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review (PDOX models) | Front Oncol | Patient-derived xenograft models used to identify combination therapies in sarcoma (focus on palbociclib) |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | Preclinical | Mol Cancer Ther | Sorafenib inhibits growth and MAPK signaling in MPNST and dedifferentiated liposarcoma cell lines |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | Preclinical xenograft | Am J Pathol | New dedifferentiated liposarcoma xenograft models show PTEN down-regulation and response to PI3K pathway inhibition |
| [25075796](https://pubmed.ncbi.nlm.nih.gov/25075796/) | 2014 | Case report | Anti-cancer Drugs | Trabectedin response in synovial sarcoma (not sorafenib; low relevance) |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02284227 | NEXAVAR | Not listed | Not listed |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multikinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (the knowledge graph links sorafenib to thrombocytopenia, neutropenia and anaemia as contraindication-related conditions) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; consider blood counts, liver function and blood pressure given the conditions listed below |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: hypertension, liver failure, thrombocytopenia, neutropenia, agranulocytosis, blood coagulation disease, acute coronary syndrome, coronary artery disease, myocardial infarction, myocardial ischaemia, anaemia, hypophosphataemia, pancreatitis, anxiety and neurotic disorders. These need confirmation against the Health Canada label.
- **Drug Interactions**: 100 interactions were identified in total. Examples of the interactions listed:
  - **Major**: dolasetron
  - **Moderate**: famotidine, loperamide, dexamethasone, clarithromycin, levofloxacin, palonosetron, naltrexone, and several laxatives and bowel-preparation agents (bisacodyl, lactulose, lactitol, sodium sulfate, polyethylene glycol)
  - **Minor**: dapagliflozin, naloxegol, metronidazole

---

## Conclusion and Next Steps

**Decision: Hold (research question only)**

**Rationale:**
The TxGNN score is very high (99.82%), but the clinical evidence is one single-arm Phase 2 trial in mixed soft tissue sarcomas plus reviews and preclinical work. It does not show a liposarcoma-specific benefit. Sorafenib is already marketed in Canada, which lowers the access barrier, but the Health Canada label warnings and contraindications have not yet been reviewed.

**To proceed, the following is needed:**
- The results and liposarcoma subgroup data from the completed Phase 2 trials (NCT00217620 and SWOG S0505)
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data (MOA)
- A drug interaction management plan, especially for the major interaction with dolasetron
- Comparison against established liposarcoma options such as trabectedin
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

