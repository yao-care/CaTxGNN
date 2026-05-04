---
layout: default
title: Everolimus
parent: 僅模型預測 (L5)
nav_order: 278
evidence_level: L5
indication_count: 10
---

# Everolimus
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

# Everolimus: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Everolimus is a selective mTOR (mechanistic target of rapamycin) inhibitor approved internationally for renal cell carcinoma, hormone receptor-positive breast cancer, pancreatic neuroendocrine tumors, and transplant rejection prophylaxis, though currently not registered in Taiwan.
The TxGNN model predicts it may be effective for **Liposarcoma** (particularly the dedifferentiated subtype, DDLPS),
with **1 active Phase 2 clinical trial** and **4 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Taiwan; internationally approved for renal cell carcinoma, HR+/HER2− breast cancer, pancreatic neuroendocrine tumors, tuberous sclerosis complex, and transplant rejection |
| Predicted New Indication | Liposarcoma (Dedifferentiated) |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Everolimus is a selective inhibitor of mTORC1 (mammalian target of rapamycin complex 1), the master regulator of protein synthesis and cell cycle progression within the PI3K/Akt/mTOR signaling axis. By blocking mTORC1-mediated phosphorylation of downstream effectors S6K1 and 4E-BP1, everolimus suppresses tumor cell proliferation and angiogenesis. These properties underpin its efficacy across multiple solid tumor types and have been validated in large-scale international clinical trials.

Dedifferentiated liposarcoma (DDLPS) is a biologically aggressive soft-tissue sarcoma characterized by high-level activation of both the Akt-mTOR and MAPK signaling pathways — as demonstrated in a clinicopathological and in vitro study of 99 DDLPS specimens (PMID 26518767). This molecular profile provides a direct mechanistic rationale for mTOR inhibition. DDLPS also frequently harbors CDK4 gene amplification, creating a compelling case for combination therapy with a CDK4/6 inhibitor such as ribociclib, which exploits dual blockade of proliferative signaling cascades that neither agent can fully suppress alone.

This mechanistic convergence has been directly translated into an active clinical trial: NCT03114527 (Phase 2) tests ribociclib + everolimus specifically in advanced DDLPS and leiomyosarcoma. A 2024 publication from the SAR-096 trial (PMID 37967116) confirms the synergistic biological rationale and provides early clinical findings, supporting the L2 evidence classification for this predicted repurposing direction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, Not Recruiting | 48 | Two-arm study evaluating Ribociclib (300 mg/day, 3 weeks on/1 week off) + Everolimus (2.5 mg/day) in advanced dedifferentiated liposarcoma (Arm A) and leiomyosarcoma (Arm B); requires ≥1 prior systemic therapy; assesses anti-tumor activity of CDK4/6 + mTOR dual blockade; expected completion December 2025 |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase 2 trial publication | Clinical Cancer Research | SAR-096 trial: Ribociclib + Everolimus in advanced DDLPS and LMS; CDK4 and mTOR co-inhibition demonstrates synergistic growth inhibition across multiple tumor models; reports clinical activity and safety in sarcoma patients |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Molecular / Translational | Tumour Biology | Akt-mTOR and MAPK pathways confirmed highly activated in 99 DDLPS specimens by IHC; in vitro study demonstrates antitumor activity of mTOR inhibitor, establishing the primary molecular rationale for everolimus in DDLPS |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Preclinical Review | Frontiers in Oncology | PDOX mouse models of sarcoma identify CDK inhibitor (palbociclib) combinations with targeted agents as effective strategies; provides preclinical framework for CDK + mTOR combination approach in sarcoma histologies |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinical Combination Study | Anticancer Research | Eribulin combined with mechanistically distinct anticancer agents (including mTOR-targeting agents) evaluated across broad tumor panel including liposarcoma; supports rationale for combination targeting in advanced liposarcoma |

---

## Taiwan Market Information

Everolimus currently holds no approved drug licenses in Taiwan (未上市) and has no registered products on record. International regulatory approvals exist from the FDA and EMA for renal cell carcinoma, HR+/HER2− breast cancer (postmenopausal), pancreatic neuroendocrine tumors, tuberous sclerosis complex-associated tumors, and transplant rejection prevention. A dedicated Taiwan regulatory filing process would be required before any domestic clinical use.

---

## All Predicted Indications — Summary

This Evidence Pack covers 10 TxGNN-predicted indications. The table below provides a complete overview for prioritization:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|----------------|----------------|
| 1 | Liposarcoma | 99.88% | L2 | Proceed with Guardrails |
| 2 | Ovarian myxoid liposarcoma | 99.84% | L5 | Hold |
| 3 | Dermatofibrosarcoma protuberans | 99.82% | L4 | Research Question |
| 4 | Parameningeal embryonal rhabdomyosarcoma | 99.77% | L5 | Hold |
| 5 | Botryoid-type embryonal RMS of the vagina | 99.76% | L5 | Hold |
| 6 | Embryonal extrahepatic bile duct RMS | 99.75% | L5 | Hold |
| 7 | Rhabdomyosarcoma | 99.74% | L2 | Proceed with Guardrails |
| 8 | Prostate embryonal rhabdomyosarcoma | 99.74% | L5 | Hold |
| 9 | Unclassified renal cell carcinoma | 99.72% | L2 | Proceed with Guardrails |
| 10 | RCC associated with neuroblastoma | 99.72% | L5 | Hold |

> **Secondary Candidates Worth Noting:**
> - **Unclassified RCC (Rank 9)** has the strongest overall evidence base in this pack — 9 publications including multiple Phase 2 RCTs (ASPEN, ESPN trials), two Phase 2 RCTs comparing everolimus vs. sunitinib directly, and a completed lenvatinib + everolimus Phase 2 study. This indication is mechanistically well-established and clinically mature.
> - **Rhabdomyosarcoma (Rank 7)** has 3 clinical trials (including a completed Phase 1/2 study NCT03245151 with a 2025 publication) and direct PI3K/mTOR pathway evidence in RMS subtypes.
> - **Dermatofibrosarcoma Protuberans (Rank 3)** is currently at the research question stage — PI3K/mTOR pathway activation has been identified as an imatinib-resistance escape mechanism, providing indirect mechanistic support.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — mTOR inhibitor (rapalog / macrolide class) |
| Myelosuppression Risk | Low (occasional anemia; grade 3/4 neutropenia and thrombocytopenia uncommon) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, fasting blood glucose, fasting lipid panel (triglycerides, cholesterol), liver function tests, serum creatinine, pulmonary function / chest imaging (non-infectious pneumonitis is a class-specific risk in 10–18% of patients), oral mucosa assessment (stomatitis/mucositis) |
| Handling Protection | Standard oral targeted therapy handling precautions; institutional cytotoxic compounding and disposal protocols apply per pharmacy policy |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A dedicated Phase 2 clinical trial (NCT03114527) is actively evaluating ribociclib + everolimus in advanced DDLPS with a 2024 trial publication confirming mechanistic rationale; molecular evidence of Akt-mTOR pathway hyperactivation in DDLPS tissue specimens (PMID 26518767) provides direct biological grounding for L2-level evidence supporting this repurposing direction.

**To proceed, the following is needed:**
- Monitor and retrieve final results of NCT03114527 upon expected completion (December 2025)
- Retrieve complete MOA data from DrugBank to close the current data gap and strengthen mechanistic analysis
- Initiate Taiwan regulatory pathway assessment (everolimus has no existing Taiwan approval; pre-NDA consultation with TFDA recommended)
- Obtain and parse the Taiwan (TFDA) package insert PDF to complete safety screening (currently a blocking data gap for S1 safety evaluation)
- Develop patient selection biomarker strategy (CDK4 amplification by FISH/IHC, mTOR pathway activation status) for trial design
- Establish a safety monitoring plan specifically addressing mTOR inhibitor class effects: non-infectious pneumonitis, hyperglycemia, hyperlipidemia, stomatitis, and infection risk from immunosuppression
- For secondary indications (Rhabdomyosarcoma, Unclassified RCC), initiate separate indication-specific evidence reviews with dedicated safety and regulatory assessments

---

> ⚠️ **Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

