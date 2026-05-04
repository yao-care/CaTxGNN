---
layout: default
title: Cytarabine
parent: 僅模型預測 (L5)
nav_order: 190
evidence_level: L5
indication_count: 9
---

# Cytarabine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Cytarabine: From Acute Leukemia to Small Cell Lung Carcinoma

## One-Sentence Summary

Cytarabine (Ara-C) is an S-phase-specific antimetabolite classically used in the treatment of acute myeloid leukemia and other hematologic malignancies.
The TxGNN model predicts it may be effective for **Small Cell Lung Carcinoma (SCLC)**,
with **3 clinical trials** and **20 publications** identified in the evidence search — though most are indirect, historical (1979–1990), or concern related lung cancer subtypes rather than SCLC directly.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute leukemia / hematologic malignancies (not registered in Taiwan; 0 DINs) |
| Predicted New Indication | Small Cell Lung Carcinoma |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L3 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cytarabine is an S-phase-specific DNA synthesis inhibitor. It functions as a pyrimidine analogue: once phosphorylated intracellularly to ara-CTP, it competes with dCTP for incorporation into DNA, causing chain termination and inhibition of DNA polymerase. Detailed mechanistic data (MOA) from the regulatory file is unavailable for this analysis, but the pharmacological basis is well-established in the literature.

Small cell lung carcinoma is one of the most aggressive thoracic malignancies, characterized by an extremely high proliferative index (Ki-67 typically >80%). This biological feature makes SCLC theoretically sensitive to S-phase-specific cytotoxic agents such as cytarabine — cells cycling rapidly are more vulnerable to DNA synthesis blockade during replication. The mechanistic rationale is therefore plausible at a conceptual level.

Historical evidence (1979–1990) confirms that cytarabine was incorporated into early SCLC combination chemotherapy regimens — including with cyclophosphamide, doxorubicin, vincristine, and radiotherapy — and was used for SCLC-related leptomeningeal disease. However, the standard of care for SCLC has since evolved firmly toward platinum (cisplatin or carboplatin) plus etoposide, supplemented in the first-line setting by atezolizumab or durvalumab. Cytarabine has been effectively displaced in this indication, and no modern randomized trials have re-examined its role.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00863512](https://clinicaltrials.gov/study/NCT00863512) | Phase 3 | Terminated | 34 | Adjuvant chemotherapy (vinorelbine, cisplatin, docetaxel, etc.) in early-stage **NSCLC** post-surgery; cytarabine not the study drug; enrollment severely inadequate; not relevant to SCLC |
| [NCT03101579](https://clinicaltrials.gov/study/NCT03101579) | Phase 1 | Completed | 13 | Intrathecal **pemetrexed** (not cytarabine) for recurrent leptomeningeal metastasis from NSCLC; cytarabine mentioned as a comparator for standard intrathecal therapy; small sample, indirect relevance |
| [NCT03507244](https://clinicaltrials.gov/study/NCT03507244) | Phase 1/2 | Completed | 34 | Intrathecal pemetrexed combined with involved-field radiotherapy for leptomeningeal metastasis from solid tumors (primarily NSCLC); cytarabine not the study drug; provides context for intrathecal strategies only |

> **Note:** None of the identified clinical trials directly study cytarabine in SCLC. All three trials target NSCLC or use pemetrexed rather than cytarabine as the primary agent. The absence of any contemporary cytarabine-in-SCLC registered trial is itself a meaningful signal.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [232239](https://pubmed.ncbi.nlm.nih.gov/232239/) | 1979 | Clinical series | Med Pediatr Oncol | 20 previously untreated SCLC patients received cyclophosphamide + doxorubicin + cytarabine (days 5–9 SC) followed by thoracic and whole-brain radiotherapy; preliminary activity observed in an early combination regimen |
| [6095640](https://pubmed.ncbi.nlm.nih.gov/6095640/) | 1984 | Clinical study | Am J Clin Oncol | Cytarabine 100 mg/m²/day continuous infusion in SCLC: no responses in 10 heavily pre-treated patients; in 25 extensive-stage patients, added to CAV regimen with limited benefit; severe toxicity |
| [2841844](https://pubmed.ncbi.nlm.nih.gov/2841844/) | 1988 | Clinical study | Am J Clin Oncol | VP-16 plus infusional cytarabine (45 mg/m²/day × 72h) in 17 refractory SCLC patients; evaluable for response; exploratory salvage regimen with high toxicity burden |
| [9363869](https://pubmed.ncbi.nlm.nih.gov/9363869/) | 1997 | RCT | J Clin Oncol | CALGB randomized trial of chemotherapy + RT ± warfarin in limited-stage SCLC; multi-drug backbone; provides context for SCLC combination regimen design |
| [6264785](https://pubmed.ncbi.nlm.nih.gov/6264785/) | 1981 | Case series | Am J Medicine | 60 SCLC patients studied for cerebral/meningeal metastases; intensive chemotherapy without prophylactic cranial irradiation; 78% response rate; leptomeningeal disease context relevant to cytarabine's intrathecal role |
| [28223673](https://pubmed.ncbi.nlm.nih.gov/28223673/) | 2017 | Case report | Gan To Kagaku Ryoho | SCLC (Stage IV) with meningeal carcinomatosis treated with multidisciplinary approach including cytarabine; demonstrates feasibility of cytarabine in SCLC-related CNS disease |
| [348088](https://pubmed.ncbi.nlm.nih.gov/348088/) | 1978 | Review | Antibiotics Chemother | Comprehensive review of ara-C analogues; discusses cytidine deaminase inactivation and strategies for prolonging Ara-C biological activity; mechanistic reference |
| [2157307](https://pubmed.ncbi.nlm.nih.gov/2157307/) | 1990 | Phase II trial | Tumori | 32 advanced NSCLC patients treated with cisplatin + vindesine + cytarabine (15 mg/m² SC q12h days 1–3); 18% partial response; shows cytarabine activity in lung cancer context |
| [2156598](https://pubmed.ncbi.nlm.nih.gov/2156598/) | 1990 | Phase II trial | Cancer | 37 chemotherapy-naive NSCLC patients: high-dose cytarabine (3 g/m²) + cisplatin; 14% overall response; Grade IV myelosuppression in 32%; demonstrates dose-limiting toxicity profile |
| [11331076](https://pubmed.ncbi.nlm.nih.gov/11331076/) | 2001 | Preclinical | Biochem Pharmacol | MDR-variant SCLC cell lines showed collateral sensitivity to cytarabine (and gemcitabine) compared to cross-resistance to other agents; mechanistic basis for cytarabine circumventing some MDR mechanisms in SCLC |

---

## Taiwan Market Information

Cytarabine is **not currently registered or marketed in Taiwan**. No DINs are recorded in the regulatory database. No approved indications, dosage forms, or license data are available from this jurisdiction.

---

## Cytotoxicity

Cytarabine is a conventional cytotoxic chemotherapy agent (pyrimidine analogue / antimetabolite). This section is required.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Antimetabolite (Pyrimidine analogue) |
| Myelosuppression Risk | **High** — Dose-dependent leukopenia, thrombocytopenia, and anemia are the primary dose-limiting toxicities; Grade IV myelosuppression reported in 32% of patients at high-dose regimens (PMID 2156598) |
| Emetogenicity Classification | Low to moderate (standard dose); moderate to high at high-dose regimens (≥1 g/m²) |
| Monitoring Items | Complete blood count with differential (nadir typically 7–14 days), liver function tests (transaminases, bilirubin), renal function (creatinine), neurological monitoring (cerebellar toxicity at high doses), ophthalmological assessment at high doses |
| Handling Protection | Must follow cytotoxic drug handling regulations — closed-system transfer devices, appropriate PPE, designated preparation area |

---

## Safety Considerations

Please refer to the package insert for safety information.

> Formal warning, contraindication, and drug–drug interaction data were not available in the current evidence pack. Known cytarabine toxicities from the literature include myelosuppression, cerebellar syndrome (at high doses), conjunctivitis, hepatotoxicity, and cytarabine syndrome (fever, myalgia, bone pain — particularly in pediatric settings).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns cytarabine a high prediction score (99.78%) for SCLC, and a mechanistic basis exists — SCLC's extreme proliferative index theoretically makes it vulnerable to S-phase-specific agents. However, cytarabine's role in SCLC was explored and largely abandoned in the 1979–1990 era due to modest efficacy and significant toxicity, and has since been displaced by etoposide-based regimens. None of the identified clinical trials directly study cytarabine in SCLC, and no contemporary randomized evidence supports re-examination of this combination. This is a model-driven signal without modern clinical validation.

**To proceed, the following would be needed:**
- A systematic review or meta-analysis of historical SCLC cytarabine trials to formally quantify response rates across the 1979–1990 literature
- Preclinical validation in contemporary SCLC cell line panels and patient-derived organoid models (particularly for resistant/relapsed SCLC where current standard etoposide+platinum has failed)
- Mechanistic rationale differentiating cytarabine from etoposide in SCLC — e.g., exploiting collateral sensitivity in MDR-SCLC (see PMID 11331076)
- Assessment of intrathecal cytarabine specifically for SCLC-related leptomeningeal disease, which may represent a niche application with a clearer unmet need
- Safety profiling and drug interaction assessment in the context of contemporary SCLC backbone regimens (platinum + etoposide ± immunotherapy)

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

