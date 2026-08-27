---
layout: default
title: Lomustine
parent: 僅模型預測 (L5)
nav_order: 396
evidence_level: L5
indication_count: 10
---

# Lomustine
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

# Lomustine: From Malignant Glioma to Lymphosarcoma

## One-Sentence Summary

Lomustine (CCNU) is a nitrosourea alkylating agent long used against brain tumours and Hodgkin lymphoma; detailed original-indication and MOA data are not on file for this evidence pack (Data Gaps DG001/DG002), and the drug is currently **not marketed in Canada**.
The TxGNN model predicts it may be effective for **Lymphosarcoma**, with **16 clinical trials** and **20 publications** currently identified as supporting evidence, several of which directly describe lomustine-containing regimens used in lymphoma/NHL over more than four decades.
Overall evidence strength is rated **L2**, and the recommended decision is **Proceed with Guardrails**, pending resolution of the blocking safety data gap (DG001).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in this evidence pack — drug not marketed in Canada; nitrosourea class historically used for brain tumours (malignant glioma) and Hodgkin lymphoma (see rationale below) |
| Predicted New Indication | Lymphosarcoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data specific to this evidence pack is not available (Data Gap DG002). Based on known pharmacological classification, lomustine is a nitrosourea-class alkylating agent that cross-links DNA and inhibits DNA/RNA synthesis in rapidly dividing cells; it is highly lipid-soluble, allowing good penetration across biological barriers (including the blood-brain barrier). Its established use has centred on brain tumours (malignant glioma, medulloblastoma) and, historically, Hodgkin lymphoma — both reflected repeatedly in the evidence collected here (e.g., the "PCV" regimen [procarbazine, CCNU, vincristine] as a standard glioma treatment component, and CCNU vs. methyl-CCNU trials conducted jointly across Hodgkin's disease, lymphosarcoma, and reticulum cell sarcoma).

Lymphosarcoma and Hodgkin lymphoma/NHL belong to the same broad lymphoproliferative disease family that lomustine has already been applied to for decades, both as monotherapy and as a component of multi-drug oral regimens (LOPP, LEMP, PACET, DECC, CAMP, CIBO-P). This is not a purely novel extrapolation: the evidence base shows lomustine has an extensive, if largely older and non-randomized, track record specifically in lymphoma/NHL populations, including AIDS-related and primary CNS lymphoma settings.

Mechanistically, lymphosarcoma cells — like glioma and Hodgkin lymphoma cells — are rapidly dividing and therefore susceptible to DNA alkylation/cross-linking damage, which is consistent with the repeated clinical use of lomustine-containing regimens across this disease spectrum. The main limitation is that supporting evidence is largely older, small-sample, or non-randomized (cohort/case-series), rather than confirmed by contemporary large Phase 3 RCTs specific to lymphosarcoma.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01989052](https://clinicaltrials.gov/study/NCT01989052) | Phase 1 | Terminated | 9 | CTO alone or combined with lomustine in bevacizumab-naïve recurrent malignant glioma; direct lomustine treatment arm, but trial terminated early. |
| [NCT00074191](https://clinicaltrials.gov/study/NCT00074191) | Phase 2 | Completed | 1 | Methotrexate/procarbazine/CCNU (lomustine) plus intraventricular cytarabine/methotrexate ± intra-ocular chemotherapy for primary CNS lymphoma; direct lomustine regimen but only 1 patient enrolled. |
| [NCT00989352](https://clinicaltrials.gov/study/NCT00989352) | Phase 2 | Unknown | 56 | Rituximab + high-dose methotrexate + lomustine + procarbazine, followed by procarbazine maintenance, for primary CNS lymphoma in patients >65 years. |
| [NCT00003113](https://clinicaltrials.gov/study/NCT00003113) | Phase 2 | Terminated | 6 | Oral combination chemotherapy + G-CSF for elderly patients with intermediate/high-grade non-Hodgkin's lymphoma; terminated with small sample size. |
| [NCT00049439](https://clinicaltrials.gov/study/NCT00049439) | Phase 2 | Completed | 54 | Dose-modified oral chemotherapy including lomustine, etoposide, cyclophosphamide, and procarbazine for AIDS-related non-Hodgkin's lymphoma (US and Africa). |
| [NCT01775475](https://clinicaltrials.gov/study/NCT01775475) | Phase 2 | Completed | 7 | Randomized CHOP vs. oral chemotherapy (including lomustine) with concurrent antiretroviral therapy for HIV-associated non-Hodgkin lymphoma in Sub-Saharan Africa. |
| [NCT01954030](https://clinicaltrials.gov/study/NCT01954030) | Phase 1 | Terminated | 17 | CTO alone or with bevacizumab for recurrent malignant glioma post-bevacizumab failure; no confirmed lomustine treatment arm in this trial. |
| [NCT03462095](https://clinicaltrials.gov/study/NCT03462095) | N/A | Unknown | 350 | Maintenance/auto-HSCT randomization for adult Ph-negative T-cell ALL; disease mismatch with lymphosarcoma and lomustine use unconfirmed. |
| [NCT05518383](https://clinicaltrials.gov/study/NCT05518383) | Phase 4 | Recruiting | 300 | B-cell mature non-Hodgkin lymphoma treatment protocol in children/adolescents evaluating molecular characteristics and MRD; lomustine content not confirmed. |
| [NCT03678883](https://clinicaltrials.gov/study/NCT03678883) | Phase 2 | Active, not recruiting | 350 | GSK-3β inhibitor 9-ING-41 alone or combined with chemotherapy for refractory hematologic malignancies/solid tumors; not specifically lomustine-directed. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [348294](https://pubmed.ncbi.nlm.nih.gov/348294/) | 1978 | RCT (CALGB) | Cancer | Randomized comparison of CCNU vs. methyl-CCNU in advanced Hodgkin's disease, lymphosarcoma, and reticulum cell sarcoma. |
| [2259920](https://pubmed.ncbi.nlm.nih.gov/2259920/) | 1990 | Phase 2 | Seminars in Oncology | CAMP regimen (lomustine, cytarabine, mitoxantrone, prednisone) in doxorubicin-resistant intermediate/high-grade NHL; 27% complete response rate. |
| [8436213](https://pubmed.ncbi.nlm.nih.gov/8436213/) | 1993 | Cohort | European Journal of Haematology | LEMP regimen (lomustine, etoposide, methotrexate, prednisone) for relapsed/refractory non-Hodgkin's lymphoma in 22 patients. |
| [8422281](https://pubmed.ncbi.nlm.nih.gov/8422281/) | 1993 | Cohort | European Journal of Cancer | PACET regimen (prednisolone, cytarabine, lomustine/CCNU, etoposide, thioguanine) for relapsed/refractory NHL in 27 patients; 26% complete response. |
| [21303800](https://pubmed.ncbi.nlm.nih.gov/21303800/) | 2011 | Cohort | Annals of Oncology | Rituximab + methotrexate + procarbazine + lomustine (R-MPL) for primary CNS lymphoma in elderly patients. |
| [15803492](https://pubmed.ncbi.nlm.nih.gov/15803492/) | 2005 | Cohort | Cancer | Lomustine-ifosfamide-bleomycin-vincristine-cisplatin (CIBO-P) regimen effective in poor-prognosis refractory/recurrent aggressive NHL. |
| [33336792](https://pubmed.ncbi.nlm.nih.gov/33336792/) | 2021 | Cohort | British Journal of Haematology | DECC (dexamethasone, etoposide, chlorambucil, lomustine) oral regimen in relapsed/refractory diffuse large B-cell lymphoma. |
| [10711848](https://pubmed.ncbi.nlm.nih.gov/10711848/) | 1999 | Cohort | Drugs | Oral combination regimen with lomustine, etoposide, cyclophosphamide, and procarbazine in 38 patients with AIDS-related lymphoproliferative malignancies. |
| [36503518](https://pubmed.ncbi.nlm.nih.gov/36503518/) | 2022 | Cohort (translational/veterinary) | Acta Veterinaria Scandinavica | 12-week combination chemotherapy followed by lomustine consolidation in canine B- and T-cell lymphoma; supports biological plausibility of lomustine activity in lymphoma. |
| [22888657](https://pubmed.ncbi.nlm.nih.gov/22888657/) | 2012 | Preclinical (animal model) | Voprosy Onkologii | Combined gemcitabine + lomustine markedly increased survival in mice with intracranial transplanted lymphosarcoma (LIO-1) versus monotherapy. |

---

## Canada Market Information

Lomustine currently holds **no active Health Canada drug identification numbers (DINs)** — market status is "Not Marketed" and `total_licenses = 0`. No product license or approved-indication text is available for review in this evidence pack. Access in Canada, if pursued, would need to proceed through an alternative regulatory pathway (e.g., Special Access Programme) rather than an existing marketed authorization.

---

## Cytotoxicity

Lomustine is a nitrosourea alkylating agent and a conventional cytotoxic chemotherapeutic — this classification is well established from its drug class and mechanism, independent of the missing DrugBank/TFDA-style records in this pack (DG001/DG002).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (nitrosourea/alkylating agent) |
| Myelosuppression Risk | High — nitrosoureas classically cause delayed and cumulative myelosuppression (thrombocytopenia and leukopenia typically nadir ~4–6 weeks post-dose); repeated dosing carries cumulative marrow toxicity risk |
| Emetogenicity Classification | Moderate to high (oral nitrosourea class) |
| Monitoring Items | CBC with differential (extended-interval monitoring given delayed nadir), pulmonary function (nitrosourea-associated pulmonary toxicity is documented in the literature evidence above, e.g., PMID 1470749), hepatic and renal function |
| Handling Protection | Must follow standard cytotoxic/hazardous drug handling and disposal precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data were not available in this evidence pack (query status: not found), and this is flagged as a **Blocking** data gap (DG001) that must be resolved before a formal safety review (S1) can be completed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted lymphosarcoma indication is supported by a substantial, though largely older and non-randomized, body of clinical trial and literature evidence (L2) showing lomustine used across multiple lymphoma/NHL regimens for over four decades, including one prospective randomized trial directly spanning lymphosarcoma. However, the drug is not currently marketed in Canada, and critical safety/label data (DG001, Blocking) and formal MOA documentation (DG002, High) are missing, so guardrails are required before advancing further.

**To proceed, the following is needed:**
- Resolve DG001: obtain official product labelling (warnings, contraindications) to complete the S1 safety initial review
- Resolve DG002: confirm mechanism of action and original approved indication(s) via DrugBank or equivalent regulatory source
- Determine a Canadian access pathway given current "Not Marketed" status (e.g., Special Access Programme, new drug submission)
- Prioritize contemporary, ideally randomized, clinical evidence specific to lymphosarcoma/NHL to strengthen beyond the current cohort/case-series-heavy evidence base
- Note: lower-ranked predicted indications (malignant tumor of meninges, spinal cord cancer, cerebral neuroblastoma, and others, L3–L5) are held at Research Question/Hold status and require substantially more evidence before consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

