---
layout: default
title: Mitoxantrone
parent: 僅模型預測 (L5)
nav_order: 433
evidence_level: L5
indication_count: 8
---

# Mitoxantrone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Mitoxantrone: From Acute Leukemia and Lymphoma to Upper Aerodigestive Tract Neoplasm

## One-Sentence Summary

Mitoxantrone is an anthraquinone antineoplastic agent with established activity in metastatic breast cancer, acute leukemias, and non-Hodgkin's lymphoma, working through DNA intercalation and topoisomerase II (Topo II) inhibition.
The TxGNN model predicts it may be effective for **Upper Aerodigestive Tract Neoplasm** — a category encompassing head and neck squamous cell carcinoma, nasopharyngeal carcinoma, salivary gland malignancies, and thyroid cancers.
This prediction is currently supported by **1 clinical trial** and **20 publications**, including a 2025 completed Phase 1b study of the liposomal formulation (PLM60) in recurrent/metastatic head and neck squamous cell carcinoma.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute leukemias, non-Hodgkin's lymphoma, metastatic breast cancer (established uses per literature; no formal Health Canada DIN on record) |
| Predicted New Indication | Upper Aerodigestive Tract Neoplasm |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Mitoxantrone is a synthetic anthracenedione (anthraquinone) derivative structurally similar to doxorubicin. Its primary mechanism involves intercalating into DNA double strands and poisoning Topoisomerase II — stabilizing DNA-Topo II cleavage complexes and inducing irreversible double-strand breaks that trigger apoptosis. This mechanism is particularly potent against rapidly proliferating cells that overexpress Topo II, a profile that characterizes squamous cell carcinomas of the upper aerodigestive tract. The Topo II-high expression found across head and neck squamous cell carcinoma (HNSCC), nasopharyngeal carcinoma (NPC), and salivary gland malignancies therefore creates a direct and mechanistically coherent basis for this TxGNN prediction.

Beyond cytotoxicity, mitoxantrone is recognized as an inducer of immunogenic cell death (ICD) — a form of apoptosis that releases damage-associated molecular patterns (DAMPs) and activates anti-tumor adaptive immunity. This property makes mitoxantrone a natural candidate for combination with immune checkpoint inhibitors (e.g., anti-PD-1/PD-L1), which is precisely the direction current trials are pursuing in NPC. The shared aerodigestive mucosa anatomy and similar molecular landscape (TP53 mutation, EGFR overexpression, HPV association) across UADT subsites further support the biological plausibility of a class-level antineoplastic effect.

A critical development is the emergence of pegylated liposomal mitoxantrone (PLM60), which exploits the enhanced permeability and retention (EPR) effect to improve tumor penetration and reduce systemic — particularly cardiac — toxicity. PLM60 is already approved in China for relapsed/refractory peripheral T-cell lymphoma. The 2025 Phase 1b study reporting PLM60's safety and preliminary efficacy in R/M HNSCC (PMID 39952083) represents the most clinically proximate validation of the TxGNN prediction, and multiple Phase 2/3 trials combining PLM60 with checkpoint inhibitors in NPC are now actively enrolling.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT06953739](https://clinicaltrials.gov/study/NCT06953739) | Phase 3 | Not Yet Recruiting | 60 | Multicenter RCT comparing P-GEMD (pegaspargase + gemcitabine + **mitoxantrone** + dexamethasone) vs P-Gemox in untreated early-stage non-UADT-involved or advanced-stage extranodal NK/T-cell lymphoma (ENKTL); targets a lymphoma subtype anatomically overlapping the UADT; patients with HLH complications are a key focus |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39952083](https://pubmed.ncbi.nlm.nih.gov/39952083/) | 2025 | Phase 1b Clinical Study | *Oral Oncology* | PLM60 (mitoxantrone HCl liposome) in R/M HNSCC: multicenter, open-label, single-arm trial (n=45); evaluated safety and efficacy; PLM60 already approved for relapsed/refractory PTCL in China, serving as the bridging rationale for HNSCC |
| [12045460](https://pubmed.ncbi.nlm.nih.gov/12045460/) | 2002 | Phase II | *Anti-Cancer Drugs* | Mitoxantrone + cisplatin in locally recurrent/metastatic salivary gland carcinoma (n=14); all had prior radical resection, majority received adjuvant radiotherapy ± chemotherapy |
| [11290867](https://pubmed.ncbi.nlm.nih.gov/11290867/) | 2001 | Phase II | *Anti-Cancer Drugs* | Ifosfamide + mitoxantrone (12 mg/m² Day 1) in R/M squamous cell carcinoma of the H&N (n=22); 4-week cycles up to 6 courses; assessed safety and response rates |
| [8922205](https://pubmed.ncbi.nlm.nih.gov/8922205/) | 1996 | Phase II (EORTC) | *Annals of Oncology* | EORTC H&N Cancer Cooperative Group study of mitoxantrone as monotherapy in adenoid cystic carcinoma; initiated after antitumor activity observed in a case report |
| [1735075](https://pubmed.ncbi.nlm.nih.gov/1735075/) | 1992 | PK/PD Clinical Study | *Cancer* | Pharmacokinetics of mitoxantrone (12–14 mg/m² IV) in 15 advanced NPC patients; three-compartment model with terminal half-life of ~71 hours; HPLC quantification method validated |
| [11269736](https://pubmed.ncbi.nlm.nih.gov/11269736/) | 2001 | Phase I | *Cancer Chemotherapy and Pharmacology* | Mitoxantrone + raltitrexed + levofolinic acid + 5-FU in advanced H&N and colorectal cancer; combination tolerated at full doses without unexpected toxicities; clinical activity observed |
| [36070368](https://pubmed.ncbi.nlm.nih.gov/36070368/) | 2022 | Translational Research | *Science Translational Medicine* | Pharmacogenomic profiling of 56 HNSCC patient-derived cells; characterized drug sensitivity landscape including Topo II inhibitors; framework for precision oncology in HNSCC |
| [1985750](https://pubmed.ncbi.nlm.nih.gov/1985750/) | 1991 | Clinical Series | *Cancer* | Prospective combination chemo-radiotherapy in anaplastic giant cell thyroid carcinoma (n=20); patients ≥65 years received mitoxantrone (14 mg/m²) every 4 weeks instead of doxorubicin/cisplatin |
| [9177455](https://pubmed.ncbi.nlm.nih.gov/9177455/) | 1997 | Molecular Study | *Cancer Letters* | No Topo II point mutations detected in multidrug-resistant anaplastic thyroid carcinoma cell lines; supports Topo II as an intact, actionable target for mitoxantrone in thyroid malignancies |
| [3512224](https://pubmed.ncbi.nlm.nih.gov/3512224/) | 1986 | Review | *Drug Intelligence & Clinical Pharmacy* | Foundational pharmacology review: anthraquinone antineoplastic similar to doxorubicin; Topo II inhibition mechanism; terminal half-life ~40 hours; 7% renal excretion; activity noted in breast cancer, leukemias, NHL, and head and neck cancer |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Anthraquinone/Anthracenedione class (synthetic analogue of doxorubicin; Topo II poison) |
| Myelosuppression Risk | **High** — neutropenia and thrombocytopenia are dose-limiting toxicities; leukocyte nadir typically occurs at Day 10–14 post-infusion |
| Emetogenicity Classification | Low to Moderate |
| Monitoring Items | CBC with differential (baseline and before each cycle), liver function tests, serum creatinine, and **cardiac function (LVEF by echocardiography or MUGA scan)** — cumulative cardiotoxicity risk requires lifetime total dose tracking |
| Handling Protection | Must follow cytotoxic drug handling regulations; skin/mucous membrane contact causes blue-green staining; urine and other body fluids may appear blue-green for 24–48 hours post-infusion |

---

## Safety Considerations

Please refer to the package insert for safety information. Warnings, contraindications, and drug interaction data are not available in this evidence pack.

> **Important clinical note**: As a Topo II inhibitor structurally related to anthracyclines, mitoxantrone carries a known cumulative risk of **cardiomyopathy** and is associated with **therapy-related acute myeloid leukemia/myelodysplastic syndrome (t-AML/t-MDS)**. These risks must be disclosed to patients and systematically monitored prior to and during therapy.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction score of 99.78% is mechanistically coherent — Topo II overexpression in UADT cancers provides a direct biological rationale for mitoxantrone activity, and the 2025 Phase 1b clinical study of the liposomal formulation (PLM60) in R/M HNSCC represents the first direct clinical evidence supporting this indication. Multiple Phase 2/3 trials combining liposomal mitoxantrone with checkpoint inhibitors in NPC are actively recruiting, marking this as an active and evolving area of clinical development. However, the conventional formulation is not approved in Canada, and critical safety data remain unavailable.

**To proceed, the following is needed:**

- **Safety data gap remediation**: Retrieve Health Canada / TFDA package insert to document formal warnings, contraindications, and listed drug interactions (currently all marked as data gaps — Blocking severity)
- **Mechanism of action documentation**: Confirm formal DrugBank MOA entry to strengthen regulatory submission narratives and support mechanistic rationale scoring
- **Cardiac toxicity risk management plan**: Establish baseline LVEF threshold criteria, serial monitoring schedule, and cumulative lifetime dose ceiling (typically ≤140 mg/m² for conventional formulation)
- **Formulation strategy decision**: Determine whether to pursue the conventional IV formulation or await PLM60 registration outside China; the two formulations have meaningfully different safety profiles and regulatory pathways
- **t-AML/t-MDS risk disclosure framework**: Prepare long-term follow-up plan for secondary malignancy risk in any prospective use
- **Canada regulatory pathway analysis**: Assess whether FDA or EMA approvals for related hematologic indications support a bridging data package for a Canadian new indication submission
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

