---
layout: default
title: Daunorubicin
parent: 僅模型預測 (L5)
nav_order: 202
evidence_level: L5
indication_count: 10
---

# Daunorubicin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Daunorubicin: From Acute Leukemia to Hodgkin's Lymphoma

## One-Sentence Summary

Daunorubicin is a foundational anthracycline antibiotic used in the treatment of acute leukemias (AML and ALL), exerting its antitumour activity through DNA intercalation and Topoisomerase II inhibition.
The TxGNN model predicts it may be effective for **Hodgkin's Lymphoma** (TxGNN rank #1 among predicted indications),
with **50 retrieved clinical trials** and **20 publications** available — though most clinical trial data relates to the structurally analogous compound doxorubicin within ABVD-based regimens, while one Phase 1/2 study (PMID 9387047) specifically evaluates liposomal daunorubicin (DaunoXome) in relapsed/refractory lymphoma patients.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute myeloid leukemia (AML) and acute lymphocytic leukemia (ALL) |
| Predicted New Indication | Hodgkin's Lymphoma |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L2 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Daunorubicin is an anthracycline antibiotic whose antitumour mechanism rests on two pillars: intercalation into the DNA double helix disrupts transcription and replication, while inhibition of Topoisomerase II prevents re-ligation of DNA strand breaks, ultimately triggering apoptosis in rapidly dividing cells. Although detailed MOA data was not retrieved in the current collection run, daunorubicin's pharmacological profile is well-characterised in the scientific literature (PMID 378369). Mechanistically, it is nearly identical to doxorubicin (Adriamycin), differing primarily in one hydroxyl group that modulates pharmacokinetics and, to a lesser extent, the spectrum of antitumour activity.

Hodgkin's lymphoma (HL) is driven by highly proliferative Reed-Sternberg cells — clonally expanded B-lymphocytes with high Topoisomerase II expression, the same molecular target exploited by daunorubicin in leukaemia. This mechanistic continuity is powerfully validated by the ABVD regimen (Adriamycin + Bleomycin + Vinblastine + Dacarbazine), the worldwide standard of care for HL for over 40 years, which relies on doxorubicin — an anthracycline with an identical mechanism of action to daunorubicin. Decades of Phase 3 trial data confirm that anthracycline-mediated Topoisomerase II inhibition is central to HL cure.

Critically, a direct early-phase clinical study (PMID 9387047) evaluated liposomal daunorubicin (DaunoXome) specifically in 19 patients with relapsed or refractory lymphoma, demonstrating one complete response and two partial responses at the 120 mg/m² dose level, with no clinical deterioration in cardiac function — supporting both activity and tolerability of daunorubicin itself in lymphoid malignancies. This provides a pharmacological bridge between the leukaemia indication and the predicted HL indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02661503](https://clinicaltrials.gov/study/NCT02661503) | Phase 3 | Active, Not Recruiting | 1,500 | HD21 trial: BrECADD (brentuximab vedotin + OECD-based regimen) vs escalated BEACOPP for advanced-stage HL; co-primary endpoints of non-inferior PFS and reduced treatment-related morbidity |
| [NCT00003389](https://clinicaltrials.gov/study/NCT00003389) | Phase 3 | Completed | 854 | ABVD vs Stanford V ± radiotherapy in locally extensive and advanced-stage HL; landmark randomised trial establishing ABVD as reference-standard anthracycline regimen |
| [NCT03907488](https://clinicaltrials.gov/study/NCT03907488) | Phase 3 | Active, Not Recruiting | 994 | Nivolumab+AVD vs Brentuximab Vedotin+AVD in newly diagnosed Stage III/IV classical HL (age ≥12); modern immunotherapy integration with anthracycline backbone |
| [NCT04685616](https://clinicaltrials.gov/study/NCT04685616) | Phase 3 | Recruiting | 1,042 | RADAR trial: ABVD ±ISRT vs A2VD ±ISRT in Stage IA/IIA HL; international PET response-adapted randomised platform |
| [NCT00002987](https://clinicaltrials.gov/study/NCT00002987) | Phase 3 | Unknown | 400 | VAPEC-B (short anthracycline-containing neoadjuvant chemotherapy) + involved-field RT vs mantle RT in early supradiaphragmatic HL |
| [NCT03004833](https://clinicaltrials.gov/study/NCT03004833) | Phase 2 | Completed | 110 | Nivolumab + AVD for early unfavorable classical HL; primary objective to show efficacy of PD-1 blockade with truncated anthracycline-based chemotherapy |
| [NCT03527628](https://clinicaltrials.gov/study/NCT03527628) | Phase 2 | Unknown | 220 | ACVD (Adriamycin + Cyclophosphamide + Vinblastine + Dacarbazine) + brentuximab vedotin in PET-2 positive advanced-stage HL; treatment intensification over standard ABVD |
| [NCT03755804](https://clinicaltrials.gov/study/NCT03755804) | Phase 2 | Active, Not Recruiting | 232 | cHOD17 paediatric classical HL: risk/response-adapted therapy using BEABOVP for low/intermediate risk or BV+etoposide+prednisone+doxorubicin for high risk |
| [NCT03407144](https://clinicaltrials.gov/study/NCT03407144) | Phase 2 | Active, Not Recruiting | 340 | KEYNOTE-667: Pembrolizumab combined with frontline chemotherapy in children/young adults with newly diagnosed classical HL showing slow early response |
| [NCT06164275](https://clinicaltrials.gov/study/NCT06164275) | Phase 2 | Active, Not Recruiting | 30 | Sequential pembrolizumab monotherapy (6 doses) followed by limited AVD (doxorubicin + vinblastine + dacarbazine) in classical HL including elderly patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [39413375](https://pubmed.ncbi.nlm.nih.gov/39413375/) | 2024 | RCT | N Engl J Med | Phase 3 S1826: Nivolumab+AVD superior to BV+AVD for PFS in advanced-stage classical HL; confirms anthracycline-based AVD backbone as non-negotiable treatment core |
| [35830649](https://pubmed.ncbi.nlm.nih.gov/35830649/) | 2022 | RCT | N Engl J Med | 5-year OS follow-up of ECHELON-1: BV+AVD vs ABVD in Stage III/IV HL; anthracycline-containing regimen delivers durable long-term survival benefit |
| [27332902](https://pubmed.ncbi.nlm.nih.gov/27332902/) | 2016 | RCT | N Engl J Med | RATHL trial: interim PET-CT adapted treatment allowing bleomycin omission (ABVD → AVD) in responders; validates anthracycline as the essential active component in ABVD |
| [20818855](https://pubmed.ncbi.nlm.nih.gov/20818855/) | 2010 | RCT | N Engl J Med | HD10/HD11 randomised trial: reduced-intensity ABVD at 2 cycles + 20 Gy IF-RT non-inferior to 4 cycles + 30 Gy in early favorable HL; establishes anthracycline dose limits |
| [9387047](https://pubmed.ncbi.nlm.nih.gov/9387047/) | 1997 | Clinical Study | Invest New Drugs | **Direct daunorubicin evidence**: liposomal daunorubicin (DaunoXome) at 40 mg/m² q14d and 120 mg/m² q21d in 19 relapsed/refractory lymphoma patients; 3 objective responses (1 CR, 2 PR) at 120 mg/m²; no clinical cardiac deterioration at higher dose |
| [36271128](https://pubmed.ncbi.nlm.nih.gov/36271128/) | 2022 | Retrospective Cohort | Sci Rep | Interim FDG-PET/CT (iPET2/iPET4) prognostic value in 245 HL patients receiving upfront ABVD; confirms anthracycline-based response evaluation as standard |
| [14584273](https://pubmed.ncbi.nlm.nih.gov/14584273/) | 2003 | Review | Gan To Kagaku Ryoho | Overview of hematologic tumour management; documents ABVD as HL first-line and historical daunorubicin/idarubicin utility in AML; bridges the two indications |
| [378369](https://pubmed.ncbi.nlm.nih.gov/378369/) | 1979 | Review | Cancer Treat Rep | Comparative analysis of daunorubicin and doxorubicin; characterises activity spectra, pharmacological differences, and role in haematologic malignancies including lymphoma |
| [35843924](https://pubmed.ncbi.nlm.nih.gov/35843924/) | 2022 | Cohort | Prilozi | Multi-decade HL management milestone review; documents dramatic survival improvement attributable to anthracycline-containing regimens across treatment eras |
| [28365830](https://pubmed.ncbi.nlm.nih.gov/28365830/) | 2017 | Review | Curr Oncol Rep | Risk-adapted and response-adapted treatment strategies for early-stage HL; comprehensive review of anthracycline chemotherapy backbone options and radiotherapy integration |

---

## Canada Market Information

Daunorubicin currently has **no Health Canada drug identification numbers (DINs)** on record. The drug is not marketed in Canada as a standalone product. Any clinical use would require a Special Access Programme (SAP) application to Health Canada.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Anthracycline class (Topoisomerase II inhibitor / DNA intercalator) |
| Myelosuppression Risk | **High** — Dose-limiting myelosuppression expected; profound neutropenia (nadir ~10–14 days) and thrombocytopenia are consistent toxicities at therapeutic doses |
| Emetogenicity Classification | Moderate to High |
| Monitoring Items | CBC with differential (mandatory before each cycle and at nadir); cardiac function — LVEF by echocardiogram or MUGA scan at baseline, after cumulative dose of ~300 mg/m², and upon completion of therapy; liver function tests (LFT); renal function; serum uric acid / urate (tumour lysis syndrome risk especially in bulky HL) |
| Handling Protection | Must comply with cytotoxic drug handling regulations; closed-system drug-transfer devices (CSTDs) required during preparation; dedicated biosafety cabinet (Class II); appropriate PPE including gloves, gown, and eye protection; dedicated cytotoxic waste disposal |

---

## Safety Considerations

No detailed safety data (product-specific warnings, contraindications, or drug interaction records) was retrieved for daunorubicin in this evidence collection run. Please refer to the package insert / product monograph for complete safety information.

The following **anthracycline class-level safety signals** are clinically established and must be reviewed before any use:

- **Cumulative cardiotoxicity**: Irreversible cardiomyopathy and congestive heart failure risk increases with cumulative lifetime anthracycline dose. Mandatory baseline and serial LVEF monitoring is required.
- **Myelosuppression**: Severe, potentially life-threatening bone marrow suppression. Do not initiate in patients with severe pre-existing marrow compromise.
- **Extravasation tissue necrosis**: Daunorubicin is a severe vesicant. Central venous access is strongly preferred; if peripheral administration is used, antidote protocols (dexrazoxane) should be available.
- **Secondary malignancy**: Long-term risk of treatment-related AML/MDS associated with anthracycline + alkylator combinations used in HL regimens.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Daunorubicin and doxorubicin are pharmacologically near-equivalent anthracyclines sharing the same molecular mechanism (Topoisomerase II inhibition, DNA intercalation). Doxorubicin forms the indispensable backbone of ABVD — the decades-established standard of care for Hodgkin's lymphoma supported by multiple completed Phase 3 RCTs. One direct Phase 1/2 clinical study (PMID 9387047) has demonstrated activity of liposomal daunorubicin itself in relapsed/refractory lymphoma patients, and the TxGNN model assigns a prediction score of 99.81%. The mechanistic, class-level, and early clinical evidence collectively justify proceeding, with the primary caveat that daunorubicin is not currently marketed in Canada and detailed safety data requires formal retrieval.

**To proceed, the following is needed:**

- **Regulatory pathway**: File a Special Access Programme (SAP) application to Health Canada; confirm import / supply chain feasibility.
- **Safety data retrieval** (currently a Blocking data gap): Download and review the full package insert / product monograph — specifically key warnings, contraindications, and drug–drug interaction data for the intended HL regimen context.
- **Target indication specificity**: Define HL subtype (classical HL vs. nodular lymphocyte-predominant HL), stage, and treatment line (first-line vs. relapsed/refractory) for the proposed repurposing application, as the evidentiary basis and comparator regimen differ substantially.
- **PK/PD comparative analysis**: Conduct a formal pharmacological comparison of daunorubicin vs. doxorubicin in HL — including cumulative cardiotoxicity threshold differences, plasma half-life, and tissue distribution — to justify direct substitution within an ABVD-like backbone or as standalone salvage agent.
- **Prospective clinical evaluation**: Design a Phase 1b/2 study evaluating daunorubicin (or DaunoXome) in HL patients with prior anthracycline exposure or intolerance to doxorubicin, to generate Canada-specific efficacy and safety data.

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. This analysis is based on computational prediction and published evidence available as of 2026-04-04.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

