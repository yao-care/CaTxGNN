---
layout: default
title: Regorafenib
parent: High Evidence (L1-L2)
nav_order: 800
evidence_level: L2
indication_count: 8
last_modified_at: 2026-11-04
monitor_inn: "Regorafenib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "clear cell renal carcinoma", "unclassified renal cell carcinoma", "renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions", "renal cell carcinoma associated with neuroblastoma", "childhood kidney cell carcinoma", "vulva sarcoma"]
description: "Regorafenib: predicted new indication Liposarcoma (evidence level L2). Approved use: Not recorded in the local data"
---

# Regorafenib
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **8** 
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

## Regorafenib: Liposarcoma
{: .text-alpha }

## One-Sentence Summary

Regorafenib is an oral multi-kinase inhibitor marketed in Canada as STIVARGA.
The TxGNN model predicts it may be effective for **liposarcoma**, but the direct evidence is mixed: **1 completed phase 2 trial** and **several publications** exist, and the dedicated liposarcoma cohort did not show clear benefit. Evidence level: **L2**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L2 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Regorafenib is a multi-kinase inhibitor that blocks angiogenic receptors (VEGFR1-3, TIE2), stromal receptors (PDGFR, FGFR) and oncogenic kinases (KIT, RET, RAF). These pathways drive tumour blood-vessel growth and proliferative signalling, and they are also relevant in soft tissue sarcomas, including liposarcoma.

The model gives this prediction a very high score (0.9976), and there is a real clinical signal in soft tissue sarcoma. However, the signal is subtype-dependent. In the randomized phase 2 REGOSARC trial, the benefit was seen mainly in non-adipocytic sarcomas and not in liposarcoma. The liposarcoma-specific cohort of SARC024 likewise concluded that the results do not support routine use of regorafenib in this population.

The prediction should therefore be viewed as a hypothesis with a plausible mechanism but weak direct clinical confirmation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024: oral regorafenib in selected sarcoma subtypes, including liposarcoma; the first systematic evaluation outside GIST |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32701199](https://pubmed.ncbi.nlm.nih.gov/32701199/) | 2020 | RCT | The Oncologist | SARC024 liposarcoma cohort (randomized, placebo-controlled phase 2): results do not support routine use of regorafenib in treatment-refractory liposarcoma |
| [27751846](https://pubmed.ncbi.nlm.nih.gov/27751846/) | 2016 | RCT | The Lancet Oncology | REGOSARC: randomized, double-blind, placebo-controlled phase 2 trial in anthracycline-pretreated advanced soft tissue sarcoma |
| [29902612](https://pubmed.ncbi.nlm.nih.gov/29902612/) | 2018 | RCT | European Journal of Cancer | Updated REGOSARC analysis including cross-over: efficacy in leiomyosarcoma, synovial sarcoma and other non-adipocytic sarcomas, but not in liposarcoma |
| [28295221](https://pubmed.ncbi.nlm.nih.gov/28295221/) | 2017 | RCT (post hoc) | Cancer | Quality-adjusted time without symptoms or toxicity analysis of REGOSARC in non-adipocytic sarcoma |
| [29931504](https://pubmed.ncbi.nlm.nih.gov/29931504/) | 2018 | Review | Targeted Oncology | Overview of regorafenib's growing role in sarcoma, including liposarcoma |
| [40975452](https://pubmed.ncbi.nlm.nih.gov/40975452/) | 2025 | Review | Critical Reviews in Oncology/Hematology | Maintenance therapy after first-line treatment for advanced soft tissue sarcoma |
| [33290314](https://pubmed.ncbi.nlm.nih.gov/33290314/) | 2021 | Retrospective study | Anti-Cancer Drugs | Anlotinib (a related kinase inhibitor) in well-differentiated/dedifferentiated liposarcoma |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Protocol | BMC Cancer | REGOSARC trial design |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02403390 | STIVARGA | Not listed | Not listed |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count, liver function (hepatic toxicity is a recognized class concern), renal function and proteinuria, blood pressure |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: The data compiled for this report list 100 interacting drugs. Examples of **major** interactions include acetylsalicylic acid, deferasirox, ibritumomab tiuxetan, tositumomab, abciximab, alteplase, antithrombin III and apixaban (mostly antithrombotic or bleeding-risk agents). **Moderate** interactions include dexamethasone, clarithromycin, naltrexone, rosuvastatin and cobicistat.
- **Class-related toxicities** reported in the literature for anti-angiogenic kinase inhibitors: hand-foot skin reaction, hepatic toxicity, hypertension and proteinuria.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Regorafenib has a plausible mechanism and a very high model score, and it has been studied in a randomized placebo-controlled phase 2 trial in liposarcoma (evidence level L2, no phase 3 trial). However, that liposarcoma cohort and the broader REGOSARC trial did not show clear benefit in liposarcoma, so any further work should be limited and carefully designed.

**To proceed, the following is needed:**
- Review of the SARC024 and REGOSARC subtype data to define whether any liposarcoma subpopulation or combination approach merits testing
- Detailed mechanism of action data and package insert warnings and contraindications
- A safety monitoring plan covering hepatic toxicity, bleeding risk, blood pressure and drug interactions

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

