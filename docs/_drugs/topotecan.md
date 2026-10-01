---
layout: default
title: Topotecan
parent: Model Prediction Only (L5)
nav_order: 917
evidence_level: L5
indication_count: 10
---

# Topotecan
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

# Topotecan: From Antineoplastic Chemotherapy to Female Breast Carcinoma

## One-Sentence Summary

Topotecan is a topoisomerase I inhibitor chemotherapy drug, and the supplied Canadian license records do not list a specific approved indication.
The TxGNN model predicts it may be effective for **female breast carcinoma**.
**5 clinical trials** and **20 publications** were retrieved, but most are indirect, preclinical, or older single-arm studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 (the Evidence Pack assigned L2, but no completed Phase 2/3 RCT of topotecan in breast cancer could be verified. The available evidence is single-arm Phase II studies, preclinical work and reviews.) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the DrugBank record. Based on general pharmacology, topotecan inhibits topoisomerase I and causes DNA damage in rapidly dividing cells. Breast cancer cells are among the cells it can affect.

Preclinical studies support this link. One study found that topoisomerase I inhibition is synthetically lethal in MYC-driven breast cancer cells (PMID 37987734). Another identified topotecan as a therapeutic option for triple-negative breast cancer (PMID 40300683).

Clinical activity has been modest, however. Single-agent Phase II studies show limited efficacy (PMID 10362325, 9413954). A brain-metastasis pilot study was small and uncontrolled (PMID 11455218). The 0.999 TxGNN score is a model prediction, not clinical proof.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | Terminated | Not reported | Intensive-dose topotecan, ifosfamide/mesna and etoposide (TIME) with autologous stem cell rescue in metastatic breast cancer. This is the only trial that directly tests topotecan in breast cancer, and it is an old high-dose approach. |
| [NCT02282020](https://clinicaltrials.gov/study/NCT02282020) | Phase 3 | Completed | 266 | Olaparib vs physician's choice single-agent chemotherapy in gBRCA-mutated ovarian cancer. Topotecan is not confirmed as an arm, and the disease is ovarian. |
| [NCT02419495](https://clinicaltrials.gov/study/NCT02419495) | Phase 1 | Terminated | 221 | Selinexor with several standard chemotherapy or immunotherapy agents in advanced malignancies. Gives only limited safety and combination data. |
| [NCT04739800](https://clinicaltrials.gov/study/NCT04739800) | Phase 2 | Active, not recruiting | 120 | Durvalumab, olaparib and cediranib combinations vs standard chemotherapy in platinum-resistant ovarian cancer. The topotecan role is unclear. |
| [NCT04279509](https://clinicaltrials.gov/study/NCT04279509) | N/A | Unknown | 35 | Organoid drug-screen-guided chemotherapy selection in refractory solid tumours. A selection strategy, not evidence of topotecan efficacy. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10362325](https://pubmed.ncbi.nlm.nih.gov/10362325/) | 1999 | Phase II single-arm (CALGB) | Am J Clin Oncol | Topotecan in advanced breast cancer after one prior chemotherapy course. 53 patients entered, 40 were evaluable. |
| [9413954](https://pubmed.ncbi.nlm.nih.gov/9413954/) | 1997 | Phase II single-arm | Br J Cancer | Continuous infusional topotecan in advanced breast cancer and NSCLC. The title reports no evidence of increased efficacy. |
| [9626200](https://pubmed.ncbi.nlm.nih.gov/9626200/) | 1998 | Phase II | J Clin Oncol | Paclitaxel plus topotecan with G-CSF support in pretreated metastatic breast cancer. |
| [11455218](https://pubmed.ncbi.nlm.nih.gov/11455218/) | 2001 | Pilot study | Onkologie | Topotecan as primary chemotherapy for breast cancer brain metastases. Small and uncontrolled. |
| [40300683](https://pubmed.ncbi.nlm.nih.gov/40300683/) | 2025 | Preclinical | Int J Biol Macromol | TFDP1 drives triple-negative breast cancer and is a therapeutic target for topotecan. |
| [37987734](https://pubmed.ncbi.nlm.nih.gov/37987734/) | 2023 | Preclinical | Cancer Res | Topoisomerase 1 inhibition causes R-loop accumulation and synthetic lethality in MYC-driven breast cancer cells. |
| [26623560](https://pubmed.ncbi.nlm.nih.gov/26623560/) | 2015 | Preclinical | Oncotarget | Metronomic topotecan plus pazopanib was effective in triple-negative breast cancer models. |
| [10472342](https://pubmed.ncbi.nlm.nih.gov/10472342/) | 1999 | Preclinical xenograft | Anticancer Res | Compared doxorubicin, cisplatin, irinotecan and oral topotecan in colon, lung and breast xenografts. The excerpt shows irinotecan and doxorubicin halted or regressed breast lines. |
| [9445630](https://pubmed.ncbi.nlm.nih.gov/9445630/) | 1997 | Review | Gynakol Geburtshilfliche Rundsch | Overview of new drugs for breast carcinoma. |
| [7910993](https://pubmed.ncbi.nlm.nih.gov/7910993/) | 1994 | Review | World J Surg | Management of metastatic breast cancer. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2396378 | TOPOTECAN HYDROCHLORIDE FOR INJECTION |
| 2390981 | TOPOTECAN INJECTION |
| 2379422 | TOPOTECAN HYDROCHLORIDE FOR INJECTION |
| 2441071 | TEVA-TOPOTECAN |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (topoisomerase I inhibitor, camptothecin derivative) |
| Myelosuppression Risk | High. A Phase II study in germ cell tumours (PMID 8617580) reported myelosuppression as the major toxicity, with a median leukocyte nadir of 1.75 cells/mm³ and a median platelet nadir of 20,500/mm³. |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible and preclinical data support it. Clinical evidence in breast cancer is limited to older, small, single-arm Phase II studies with modest activity, and no confirmed randomized trial exists. Health Canada safety data is also missing.

**To proceed, the following is needed:**
- The Health Canada product monograph (warnings, contraindications, approved indications)
- DrugBank mechanism of action data
- Verification of the intervention lists for NCT02282020 and NCT04739800 before using them as evidence
- Modern comparative clinical data for topotecan in breast cancer, such as triple-negative disease

**Note on other predictions:** Germ cell tumour, the second-ranked prediction, has only a negative Phase II study (PMID 8617580: no responses in 14 evaluable cisplatin-refractory patients). The remaining yolk sac tumour subtypes are model predictions only, with no trials or literature.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

