---
layout: default
title: Methotrexate
parent: 僅模型預測 (L5)
nav_order: 386
evidence_level: L5
indication_count: 10
---

# Methotrexate
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

# Methotrexate: From Leukemia and Autoimmune Disease to Hodgkin's Lymphoma

## One-Sentence Summary

Methotrexate (MTX) is a classic antifolate antimetabolite with decades of established use in leukemia, lymphoma, osteosarcoma, and autoimmune diseases such as rheumatoid arthritis and psoriasis.
In this multi-indication TxGNN analysis covering **10 predicted indications**, **Hodgkin's Lymphoma** emerges as the most actionable target — supported by Phase 2/3 clinical trials of the VBM (Vinblastine + Bleomycin + Methotrexate) regimen in early-stage disease and **20 publications**.
The overall recommendation for Hodgkin's Lymphoma is **Proceed with Guardrails**, reflecting the strongest evidence level in this analysis (L2).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Leukemia, lymphoma, osteosarcoma, rheumatoid arthritis, psoriasis (established globally; no Health Canada regulatory data retrieved — see note below) |
| Predicted New Indication | Hodgkin's Lymphoma (Rank 5 of 10; highest actionable evidence level across all predictions) |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L2 |
| Canada Market Status | Not marketed (0 DINs retrieved — data gap likely; verification recommended) |
| Number of DINs | 0 (data gap — Health Canada product database should be consulted directly) |
| Recommended Decision | Proceed with Guardrails |

> **Note on Canada Market Status**: The Health Canada query returned 0 DINs for Methotrexate. Methotrexate is a widely available generic drug worldwide; this result most likely reflects a data retrieval gap rather than actual market absence. Direct verification against the Health Canada Drug Product Database is strongly recommended before drawing regulatory conclusions.

---

## Why is This Prediction Reasonable?

Methotrexate is a competitive inhibitor of dihydrofolate reductase (DHFR), the enzyme responsible for reducing dihydrofolate to tetrahydrofolate. By blocking folate metabolism, MTX depletes the intracellular pool of reduced folates required for de novo thymidylate and purine synthesis. The result is DNA synthesis arrest, which preferentially affects rapidly proliferating cells — a mechanism that fundamentally underpins its activity across a broad range of malignancies. Although detailed MOA data was not retrieved from the automated pipeline for this report, MTX's mechanism is one of the best-characterised in clinical oncology.

Hodgkin's Lymphoma (HL) is characterised by Reed-Sternberg cells with a high proliferative index, making them biologically susceptible to antifolate-mediated DNA synthesis inhibition. The mechanistic link is not speculative: MTX has historically been embedded in the VBM chemotherapy backbone (Vinblastine + Bleomycin + Methotrexate) as a combination regimen evaluated in early-stage, favorable-risk HL in multiple Phase 2 and Phase 2/3 trials, demonstrating complete remission rates of 94–100% and 5-year progression-free survival of 75–95%. The HL literature in this pack includes a directly relevant Phase 2/3 Italian multi-centre trial (Gobbi et al., 2003) and a British National Lymphoma Investigation pilot study (Bates et al., 1994).

It is important to note that while this mechanistic and historical evidence is genuine, modern standard-of-care HL regimens (ABVD, BEACOPPesc, and increasingly pembrolizumab-based approaches) have largely superseded VBM in routine practice. MTX's repositioning value in HL therefore sits at the intersection of historical evidence for early-stage disease and emerging interest in less-cardiotoxic alternatives to bleomycin/doxorubicin for specific patient populations (e.g., elderly, pulmonary-comorbidity patients). Additionally, the Literature section flags a notable safety signal: long-term low-dose MTX use has itself been associated with a distinct MTX-associated lymphoproliferative disorder (MTX-LPD) that can histologically resemble classic HL — a clinical phenomenon that must be distinguished carefully.

---

## Clinical Trial Evidence

*(Primary focus: Hodgkin's Lymphoma and lymphoma indications; selected trials with directly graded relevance ≥ B)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT02631239](https://clinicaltrials.gov/study/NCT02631239) | Phase 3 | Unknown | 256 | EDP (Etoposide/Dexamethasone/PEG-asparaginase) ± MTX with sandwiched radiotherapy for stage I–II NK/T-cell lymphoma nasal type. MTX arm versus non-MTX arm randomised comparison; provides Phase 3 data on the added value of MTX in an aggressive lymphoma setting. |
| [NCT00051311](https://clinicaltrials.gov/study/NCT00051311) | Phase 2 | Completed | 62 | EPOCH-F/R induction followed by reduced-intensity HLA-related allogeneic HSCT with Cyclosporine/MTX GvHD prophylaxis for refractory/relapsed hematologic malignancies including B-cell lymphomas. MTX as core GvHD prevention in lymphoma transplant context. |
| [NCT00045539](https://clinicaltrials.gov/study/NCT00045539) | Phase 2 | Completed | N/A | MTX + Thiotepa for newly diagnosed primary CNS lymphoma. Direct Phase 2 evidence of MTX as the primary anti-lymphoma agent in CNS-sanctuary lymphoma; provides safety and efficacy benchmark. |
| [NCT00989352](https://clinicaltrials.gov/study/NCT00989352) | Phase 2 | Unknown | 56 | Rituximab + high-dose MTX + lomustine + procarbazine followed by procarbazine maintenance in PCNSL patients >65 years. HD-MTX-based combination for aggressive lymphoma in an elderly population. |
| [NCT03206671](https://clinicaltrials.gov/study/NCT03206671) | Phase 3 | Active, not recruiting | 650 | B-NHL 2013 multinational protocol (NHL-BFM + NOPHO groups) evaluating rituximab in aggressive B-cell NHL in children and adolescents; HD-MTX is included in consolidation cycles. Phase 3 paediatric lymphoma data with MTX as standard backbone. |
| [NCT03959241](https://clinicaltrials.gov/study/NCT03959241) | Phase 3 | Completed | 431 | Randomised comparison of Tacrolimus/MTX vs PTCy/Tac/MMF for GvHD prophylaxis post reduced-intensity allogeneic PBSC transplantation (BMT CTN 1703). Establishes MTX's comparative profile against modern GvHD prophylaxis regimens in haematologic malignancy transplant setting. |

---

## Literature Evidence

*(Primary focus: Hodgkin's Lymphoma and lymphoma indications; ordered by evidence strength)*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [14635074](https://pubmed.ncbi.nlm.nih.gov/14635074/) | 2003 | Phase 2/3 Trial | Cancer | Gobbi et al. — VBM (Vinblastine, Bleomycin, Methotrexate) + involved-field irradiation in early-stage favorable Hodgkin's Lymphoma (GISL multi-centre). CR rates 94–100%, 5-year PFS 75–95%. Directly validates MTX as a core component of early-stage HL regimen. |
| [7509382](https://pubmed.ncbi.nlm.nih.gov/7509382/) | 1994 | Clinical Trial | J Clin Oncol | Bates et al. — VBM + involved-field radiotherapy in clinical stage IA and IIA Hodgkin's disease (British National Lymphoma Investigation pilot). Efficacy and toxicity assessment of MTX-containing regimen as an alternative to MOPP/ABVD in low-risk HL. |
| [21592816](https://pubmed.ncbi.nlm.nih.gov/21592816/) | 2012 | Review/Analysis | Crit Rev Oncol Hematol | Gobbi & Federico — Comprehensive review of VBM chemotherapy combined with involved-field radiotherapy across 9 trials and 11 reports in early-stage HL. CR rates 94–100%, 5-year PFS 75–95%; identifies pulmonary toxicity as manageable concern; discusses why VBM was underadopted despite strong results. |
| [2363941](https://pubmed.ncbi.nlm.nih.gov/2363941/) | 1990 | Retrospective | Acta Oncologica | Enblad et al. — MIME (Methyl-GAG, Ifosfamide, MTX, Etoposide) salvage therapy in 103 patients with recurrent/refractory Hodgkin's disease (44 patients) and NHL. MTX-containing salvage yielded 43% CR + 54% total response in HD, demonstrating activity in relapsed HL. |
| [35848760](https://pubmed.ncbi.nlm.nih.gov/35848760/) | 2022 | Research Article | Am J Surg Pathol | Shiraiwa et al. — 9p24.1 genetic alteration and PD-L1 expression in de novo and MTX-associated Epstein-Barr virus-positive Hodgkin Lymphoma vs MTX-associated Hodgkin-like lesions (34 patients). Critical for distinguishing bona fide MTX-associated HL from MTX-LPD — relevant safety signal for any MTX-in-lymphoma strategy. |
| [28380678](https://pubmed.ncbi.nlm.nih.gov/28380678/) | 2017 | Retrospective Analysis | Cancer Science | Gion et al. — Clinicopathological analysis of MTX-associated LPD in RA patients: DLBCL vs classic HL subtypes. Spontaneous regression patterns after MTX discontinuation clarified. Essential background for regulatory and safety assessment. |
| [8635099](https://pubmed.ncbi.nlm.nih.gov/8635099/) | 1996 | Phase 2 Trial | Cancer | Stamatoullas et al. — IVAM (Ifosfamide, Etoposide, Cytarabine, MTX) salvage chemotherapy in relapsed/refractory aggressive NHL with PBSC collection intent. Demonstrated MTX's role as a bridge-to-transplant salvage partner in aggressive lymphoma. |
| [12967352](https://pubmed.ncbi.nlm.nih.gov/12967352/) | 2003 | Review | Clinical Evidence | Mead et al. — Evidence-based review of NHL management; contextualises MTX's position within lymphoma treatment landscape alongside CHOP and other regimens. |

---

## Cytotoxicity

Methotrexate is a conventional cytotoxic antineoplastic drug (antifolate/antimetabolite class); this section is required.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Antifolate antimetabolite (Dihydrofolate reductase inhibitor) |
| Myelosuppression Risk | **High** at high-dose regimens (HD-MTX ≥1 g/m²): leucopenia, thrombocytopenia, anaemia common; requires leucovorin rescue. **Low to moderate** at low/intermediate doses. |
| Emetogenicity Classification | Low to moderate (dose-dependent; high-dose MTX regimens have greater emetogenic potential) |
| Monitoring Items | CBC with differential (weekly during active treatment), serum creatinine and eGFR (MTX is renally cleared; renal impairment markedly increases toxicity), LFTs (hepatotoxicity with cumulative doses), serum MTX levels (mandatory with HD-MTX regimens), mucositis assessment |
| Handling Protection | Must be handled according to cytotoxic drug handling regulations (closed-system transfer devices, appropriate PPE); parenteral formulations particularly require BSC/isolator preparation |

---

## Safety Considerations

The automated data pipeline did not retrieve TFDA package insert warnings, contraindications, or drug-drug interaction data for this analysis (Blocking data gap DG001, High-severity gap DG002). Based on the well-established pharmacology of Methotrexate, the following summary reflects publicly known safety profile:

Please refer to the Health Canada-approved package insert for complete safety information.

Key areas requiring attention in any clinical use plan:
- **Myelosuppression and infection risk**: Dose-limiting toxicity requiring close haematological monitoring and leucovorin rescue protocols for HD-MTX regimens
- **Hepatotoxicity and pulmonary toxicity**: Cumulative dose-related liver fibrosis (particularly at chronic low doses); MTX pneumonitis is a distinct immune-mediated pulmonary adverse event (one case report in this pack: PMID 22550565)
- **Renal function dependency**: MTX clearance is entirely renal; even mild renal impairment dramatically increases systemic exposure and toxicity risk
- **MTX-associated lymphoproliferative disorder (MTX-LPD)**: Long-term low-dose MTX therapy (typically for RA/psoriasis) is associated with a distinct lymphoproliferative syndrome — some cases mimic HL histologically and may regress after MTX discontinuation (PMIDs 35848760, 28380678). This is a critical consideration when positioning MTX as a new lymphoma treatment.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for Hodgkin's Lymphoma)

**Rationale:**
The VBM regimen (Vinblastine + Bleomycin + Methotrexate) has demonstrated Phase 2/3 clinical evidence in early-stage favorable Hodgkin's Lymphoma with CR rates of 94–100% across multiple trials, providing genuine mechanistic and clinical basis for MTX's activity in HL. However, modern HL treatment standards (ABVD, escalated BEACOPP, pembrolizumab combinations) have largely superseded VBM, and the unique safety concern of MTX-associated lymphoproliferative disorder must be carefully managed in any repositioning strategy.

**Summary of all 10 TxGNN predictions:**

| Rank | Indication | Evidence Level | Recommendation |
|------|-----------|---------------|----------------|
| 1 | Pulmonary blastoma | L5 | Hold |
| 2 | Primary pulmonary lymphoma | L3 | Research Question |
| 3 | Small cell lung carcinoma | L3 | Research Question |
| 4 | Well-differentiated fetal adenocarcinoma of the lung | L5 | Hold |
| **5** | **Hodgkin's Lymphoma** | **L2** | **Proceed with Guardrails** |
| 6 | Rhabdomyosarcoma | L3 | Research Question |
| 7 | Pregerminal center CLL/SLL | L5 | Hold |
| 8 | CLL/SLL with IGHV somatic hypermutation | L5 | Hold |
| 9 | Parameningeal embryonal rhabdomyosarcoma | L4 | Hold |
| 10 | Botryoid-type embryonal RMS of the vagina | L5 | Hold |

**To proceed with the Hodgkin's Lymphoma indication, the following is needed:**

- **Health Canada regulatory verification**: Confirm actual DIN status and approved indications for MTX products marketed in Canada (current data shows 0 DINs, which is inconsistent with MTX's global availability and likely reflects a data retrieval gap)
- **Package insert review**: Obtain TFDA/Health Canada approved labelling to complete S1 safety screening (Blocking data gap DG001)
- **Mechanism of action documentation**: Retrieve DrugBank MOA data to formally confirm DHFR inhibition and antifolate classification (High-severity data gap DG002)
- **Positioning analysis**: Evaluate MTX's role within modern HL treatment algorithms (particularly BV-AVD, pembrolizumab-AVD) to identify specific patient populations or treatment-line positions where VBM-based approaches remain relevant (e.g., elderly patients, bleomycin-intolerant patients, resource-limited settings)
- **MTX-LPD exclusion protocol**: Define clear clinical criteria to distinguish therapeutic anti-HL use from MTX-LPD-induced HL-like lesions, including EBV status testing and response-to-discontinuation monitoring
- **Rhabdomyosarcoma and primary pulmonary lymphoma**: Both warrant dedicated Research Question evaluation; HDMTX has a 1997 Phase 2 trial in high-risk RMS (PMID 9329466) and mechanistic rationale for B-cell primary pulmonary lymphoma via CNS-penetrating HD-MTX
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

