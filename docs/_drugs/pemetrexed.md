---
layout: default
title: Pemetrexed
parent: High Evidence (L1-L2)
nav_order: 608
evidence_level: L2
indication_count: 10
---

# Pemetrexed
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Pemetrexed: From Malignant Pleural Mesothelioma to Malignant Peritoneal Mesothelioma

## One-Sentence Summary

Pemetrexed, combined with cisplatin, is the established standard first-line chemotherapy for malignant pleural mesothelioma. The TxGNN model predicts it may also be effective for **Malignant Peritoneal Mesothelioma**, with **11 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Malignant Pleural Mesothelioma (established use, evidenced within this pack — see below; no formal Canadian label text on file) |
| Predicted New Indication | Malignant Peritoneal Mesothelioma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not separately catalogued for this drug (`original_moa`: Data Gap). However, the evidence pack itself documents that pemetrexed is a multitargeted antifolate — inhibiting thymidylate synthase (TS), dihydrofolate reductase (DHFR), and glycinamide ribonucleotide formyltransferase (GARFT) — which blocks folate-dependent DNA/RNA synthesis in rapidly dividing cells. This is the mechanistic basis for its established role, in combination with cisplatin, as guideline-standard first-line chemotherapy for malignant **pleural** mesothelioma; this use is not a model prediction but a clinically validated indication (L1 evidence level within this pack, supported by a completed Phase III RCT and post-marketing safety data).

Malignant peritoneal mesothelioma and malignant pleural mesothelioma arise from the same cell of origin — the mesothelial lining of serosal cavities (pleura vs. peritoneum) — and differ primarily in anatomic site rather than underlying tumor biology. Since pemetrexed-cisplatin's efficacy in the pleural setting is well established, extrapolating the same antifolate mechanism to peritoneal disease is biologically coherent.

This extrapolation is further reinforced by the evidence pack: multiple studies test pemetrexed-based regimens specifically in peritoneal mesothelioma, often combined with cytoreductive surgery and hyperthermic intraperitoneal chemotherapy (CRS/HIPEC), which has become part of accepted treatment pathways. The rationale text accompanying this prediction states that "peritoneal and pleural mesothelioma are both of mesothelial cell origin, and systemic pemetrexed chemotherapy (often combined with CRS/HIPEC) is already incorporated into treatment guidelines" — supporting a reasonable mechanistic extrapolation rather than a purely data-free prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06057935](https://clinicaltrials.gov/study/NCT06057935) | Phase 2 | Recruiting | 64 | Multicenter RCT comparing intraperitoneal vs. intravenous chemotherapy after CRS + HIPEC in peritoneal mesothelioma |
| [NCT00061477](https://clinicaltrials.gov/study/NCT00061477) | Phase 2 | Completed | 48 | Pemetrexed (ALIMTA) + gemcitabine as front-line therapy for pleural or peritoneal mesothelioma; assessed safety, response, survival |
| [NCT05001880](https://clinicaltrials.gov/study/NCT05001880) | Phase 2 | Recruiting | 66 | Randomized trial of neoadjuvant/palliative chemo (carboplatin + pemetrexed + bevacizumab) ± atezolizumab immunotherapy |
| [NCT02535312](https://clinicaltrials.gov/study/NCT02535312) | Phase 1/2 | Active, not recruiting | 30 | Methoxyamine (TRC102) + cisplatin/pemetrexed in solid tumors/mesothelioma refractory to pemetrexed-platinum |
| [NCT01353482](https://clinicaltrials.gov/study/NCT01353482) | Phase 1/2 | Withdrawn | 0 | First-line vorinostat + pemetrexed-cisplatin for pleural mesothelioma; withdrawn before enrollment |
| [NCT04462809](https://clinicaltrials.gov/study/NCT04462809) | Phase 2 | Unknown | 40 | Three-cohort trial of talazoparib maintenance after first-line platinum-based chemo in pleural or peritoneal mesothelioma |
| [NCT00402766](https://clinicaltrials.gov/study/NCT00402766) | Phase 1 | Completed | 19 | Cisplatin + pemetrexed + imatinib in unresectable/metastatic malignant mesothelioma; determined maximum tolerated dose |
| [NCT06543069](https://clinicaltrials.gov/study/NCT06543069) | Phase 2 | Recruiting | 28 | Sintilimab + bevacizumab + pemetrexed/cisplatin for unresectable peritoneal mesothelioma; exploring efficacy/safety biomarkers |
| [NCT03875144](https://clinicaltrials.gov/study/NCT03875144) | Phase 2 | Suspended | 66 | RCT comparing PIPAC + systemic chemo (cisplatin/pemetrexed) vs. systemic chemo alone as first-line therapy |
| [NCT02029690](https://clinicaltrials.gov/study/NCT02029690) | Phase 1 | Terminated | 85 | ADI-PEG 20 (arginine-depleting enzyme) + pemetrexed/cisplatin in arginine-auxotrophic tumors, including peritoneal mesothelioma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31417959](https://pubmed.ncbi.nlm.nih.gov/31417959/) | 2019 | Cohort | Pleura and peritoneum | Bidirectional chemotherapy enabling conversion to resectability in initially unresectable peritoneal mesothelioma |
| [28594258](https://pubmed.ncbi.nlm.nih.gov/28594258/) | 2017 | Retrospective | Expert Rev Anticancer Ther | Retrospective evaluation of first-line pemetrexed + cisplatin efficacy specifically in peritoneal mesothelioma |
| [31287877](https://pubmed.ncbi.nlm.nih.gov/31287877/) | 2019 | Retrospective | Jpn J Clin Oncol | Efficacy and safety of pemetrexed + cisplatin as first-line therapy in advanced peritoneal mesothelioma, given no established standard regimen |
| [23291819](https://pubmed.ncbi.nlm.nih.gov/23291819/) | 2013 | Case report | BMJ Case Reports | Patient responding to rechallenge with cisplatin + pemetrexed after initial response and relapse, with literature review |
| [30450291](https://pubmed.ncbi.nlm.nih.gov/30450291/) | 2018 | Review | Transl Lung Cancer Res | Review of peritoneal mesothelioma epidemiology, pathology and treatment approaches |
| [35407498](https://pubmed.ncbi.nlm.nih.gov/35407498/) | 2022 | Review | J Clin Med | Review of diagnosis and treatment strategies, including CRS/HIPEC, for peritoneal mesothelioma |
| [34723916](https://pubmed.ncbi.nlm.nih.gov/34723916/) | 2022 | Case series | J Immunother | Chemoimmunotherapy in platinum-nonresponsive metastatic peritoneal mesothelioma after prior CRS/chemo (n=2) |
| [33257382](https://pubmed.ncbi.nlm.nih.gov/33257382/) | 2020 | Case report | BMJ Case Reports | Nivolumab used in peritoneal mesothelioma following asbestos-exposure-related diagnosis |
| [38806763](https://pubmed.ncbi.nlm.nih.gov/38806763/) | 2024 | Cohort | Ann Surg Oncol | Multi-center study of demographic, clinicopathologic and prognostic characteristics and treatment strategies |
| [22104079](https://pubmed.ncbi.nlm.nih.gov/22104079/) | 2012 | Review | Cancer Treat Rev | Update on diagnosis and treatment, including chemotherapy, for diffuse peritoneal mesothelioma |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antifolate/antimetabolite class — TS/DHFR/GARFT inhibitor) |
| Myelosuppression Risk | Moderate to high — hematologic toxicity (anemia, neutropenia, thrombocytopenia) is the main dose-limiting toxicity; commonly mitigated with vitamin B9/B12 supplementation and dose adjustment (per trial NCT03537833 within this pack) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions (emetogenic risk increases substantially when combined with cisplatin, per standard combination regimens referenced above) |
| Monitoring Items | CBC with differential, renal function (creatinine clearance — pemetrexed is renally cleared), hepatic function, folate/vitamin B12 status |
| Handling Protection | Must follow cytotoxic drug handling regulations (hazardous IV chemotherapy agent) |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Pemetrexed's mechanism and efficacy are well-validated in pleural mesothelioma, and peritoneal mesothelioma shares the same mesothelial cell origin. Multiple dedicated trials and retrospective studies of pemetrexed-based regimens in peritoneal mesothelioma (evidence level L2) support cautious clinical extrapolation, but no completed Phase 3 RCT specific to the peritoneal site yet exists.

**To proceed, the following is needed:**
- Product label safety information (warnings, contraindications) — currently a blocking data gap (DG001)
- Formal mechanism-of-action documentation from DrugBank (DG002)
- Route compatibility assessment (IV vs. intraperitoneal/HIPEC administration) — currently pending
- Confirmation of Canadian regulatory/market status before any clinical positioning, since the drug currently has no marketed license or DIN on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

