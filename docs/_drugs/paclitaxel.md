---
layout: default
title: Paclitaxel
parent: Model Prediction Only (L5)
nav_order: 698
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Paclitaxel: predicted new indication Female breast carcinoma (evidence level L5). Approved use: Ovarian cancer"
monitor_inn: "PACLITAXEL"
predicted_indications: ["parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
---

# Paclitaxel
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

## Paclitaxel: From Ovarian Cancer to Female Breast Carcinoma
{: .text-alpha }

## One-Sentence Summary

Paclitaxel is a taxane chemotherapy drug whose original indications in the knowledge graph centre on ovarian cancer and related ovarian tumours.
The TxGNN model predicts it may be effective for **female breast carcinoma**, and the data compiled for this report list **40 clinical trials** and **19 publications** for this direction.
Paclitaxel is already a standard-of-care taxane in breast cancer, so this is a confirmation of established use rather than a true repurposing discovery.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian cancer (the Canadian licence records contain no indication text; the original indication comes from the knowledge graph) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.995% |
| Evidence Level | L2 (as scored in the data; Phase 3 trials exist in the list but are mostly combination studies) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on established pharmacology, paclitaxel stabilises microtubules, which causes mitotic arrest and apoptosis in rapidly dividing tumour cells.

Ovarian cancer and breast cancer are both solid epithelial tumours that respond to anti-microtubule chemotherapy. The mechanism does not depend on a tumour-specific target, so it applies directly to breast carcinoma. Literature in the data describes paclitaxel and docetaxel as evidence-based components of therapy for advanced breast, lung and ovarian cancers, and a 1997 review notes licensing extended to metastatic breast carcinoma.

This prediction should be read as consistent with existing practice. The sampled trial list contains mainly Phase 1/2 studies and combination regimens, and Phase 3 evidence for solvent-based paclitaxel alone is only partly visible.

---

## Clinical Trial Evidence

The data list 40 trials for this indication. The table shows the 10 most relevant (ranked by relevance grade, then design).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00003539](https://clinicaltrials.gov/study/NCT00003539) | Phase 2 | Completed | 50 | Weekly 1-hour paclitaxel plus trastuzumab in metastatic breast cancer; direct paclitaxel use |
| [NCT00006120](https://clinicaltrials.gov/study/NCT00006120) | Phase 2 | Unknown | N/A | Randomized comparison of two docetaxel or paclitaxel schedules in metastatic breast cancer |
| [NCT05020860](https://clinicaltrials.gov/study/NCT05020860) | Phase 2 | Recruiting | 185 | Neoadjuvant systemic therapy; clinical response as a predictor of pathologic response |
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Phase 3 | Completed | 652 | Taxane-based chemotherapy with lapatinib versus trastuzumab in HER2-positive metastatic breast cancer |
| [NCT00006459](https://clinicaltrials.gov/study/NCT00006459) | Phase 3 | Completed | N/A | Gemcitabine plus paclitaxel versus paclitaxel in metastatic breast cancer |
| [NCT00553358](https://clinicaltrials.gov/study/NCT00553358) | Phase 3 | Completed | 455 | Neo-ALTTO: neoadjuvant lapatinib, trastuzumab or both plus paclitaxel in HER2-positive disease |
| [NCT00075270](https://clinicaltrials.gov/study/NCT00075270) | Phase 3 | Completed | 580 | Oral lapatinib plus paclitaxel versus paclitaxel alone in first-line metastatic breast cancer |
| [NCT00513292](https://clinicaltrials.gov/study/NCT00513292) | Phase 3 | Completed | 280 | Neoadjuvant FEC then paclitaxel plus trastuzumab versus the reverse sequence in HER2-positive operable breast cancer |
| [NCT01822314](https://clinicaltrials.gov/study/NCT01822314) | Phase 3 | Completed | 632 | ETNA: neoadjuvant nab-paclitaxel versus solvent-based paclitaxel in HER2-negative high-risk breast cancer |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Phase 3 | Completed | 478 | Dose-dense adjuvant chemotherapy followed by docetaxel versus paclitaxel in node-positive breast cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10791395](https://pubmed.ncbi.nlm.nih.gov/10791395/) | 2000 | Review | Lancet | Taxanes are evidence-based components of therapy for advanced breast, lung and ovarian cancers; paclitaxel approved in the USA for adjuvant node-positive breast cancer |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug and Therapeutics Bulletin | Review of paclitaxel and docetaxel in breast and ovarian cancer, including licence extension to metastatic breast carcinoma |
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Phase 2 trial | Cancer | Doxorubicin plus paclitaxel in advanced breast carcinoma; relevance of prior adjuvant anthracycline therapy |
| [11745249](https://pubmed.ncbi.nlm.nih.gov/11745249/) | 2001 | Clinical study | Cancer | Paclitaxel in multimodality treatment of inflammatory breast carcinoma |
| [9296218](https://pubmed.ncbi.nlm.nih.gov/9296218/) | 1997 | Dose-finding study | Annals of Oncology | Maximum tolerated doses of 3-hour paclitaxel with cyclophosphamide in advanced breast cancer |
| [10898354](https://pubmed.ncbi.nlm.nih.gov/10898354/) | 2000 | Review | Cancer | Developments in breast cancer chemotherapy |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | Genomic study | Nature Communications | TEKT4 germline variations enriched in post-treatment tumours, linked to paclitaxel resistance |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | Computational/preclinical | Chemical Biology & Drug Design | Paclitaxel combinations against breast carcinoma and in vivo biomarkers |
| [20665703](https://pubmed.ncbi.nlm.nih.gov/20665703/) | 2011 | Preclinical | J Cell Physiol | ZD6474 enhances paclitaxel antiproliferative and apoptotic effects in breast carcinoma cells |
| [7904376](https://pubmed.ncbi.nlm.nih.gov/7904376/) | 1993 | Overview | Seminars in Oncology Nursing | History and development of paclitaxel |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02281066 | ABRAXANE FOR INJECTABLE SUSPENSION | Not listed | Not listed |
| 02391465 | PACLITAXEL INJECTION USP | Not listed | Not listed |
| 02320150 | PACLITAXEL INJECTION USP | Not listed | Not listed |
| 02496097 | PACLITAXEL POWDER FOR INJECTABLE SUSPENSION NANOPARTICLE, ALBUMIN-BOUND PACLITAXEL | Not listed | Not listed |
| 02244372 | PACLITAXEL FOR INJECTION | Not listed | Not listed |

All five authorisations are valid single-ingredient products. Two are albumin-bound (nab-paclitaxel) formulations, which differ from solvent-based paclitaxel.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (taxane, anti-microtubule agent) |
| Myelosuppression Risk | High (neutropenia is the dose-limiting toxicity; the knowledge graph also flags neutropenia, agranulocytosis, thrombocytopenia and anaemia as cautions) |
| Emetogenicity Classification | Low |
| Monitoring Items | Complete blood count with differential, liver function (including bilirubin), renal function, peripheral neurological assessment |
| Handling Protection | Must follow cytotoxic drug handling regulations |

Please refer to the package insert warnings and precautions for full detail.

---

## Safety Considerations

Package-insert warnings and contraindications were not available in the data compiled for this report, so the points below come from the knowledge graph and interaction database and are not label text.

- **Disease-level cautions (knowledge graph):** Listed conditions include neutropenia, agranulocytosis, thrombocytopenia, anaemia, liver disease, hyperbilirubinaemia (including Gilbert syndrome), kidney disease, peripheral neuropathy, myocardial infarction and sudden cardiac arrest, asthma, diabetes mellitus and diabetic ketoacidosis, psoriasis, hypotensive disorder, and anxiety or dysthymic disorders.
- **Drug interactions (100 recorded; the first 20 retrieved are summarised):**
  - Moderate: aprepitant, cimetidine, clarithromycin, clotrimazole, dexamethasone, eliglustat, metronidazole, miconazole, rolapitant, rosuvastatin, simvastatin, tinidazole, troglitazone.
  - Minor: ascorbic acid, levofloxacin.
  - Severity unknown: glimepiride, doxycycline, morphine, metformin, omeprazole.
- **Adverse events in the literature:** Case reports describe pneumonitis, uveitis, corneal lesions, periarticular thenar erythema with onycholysis, taxane-induced polyneuropathy and amenorrhoea.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Paclitaxel's mechanism is directly applicable to breast carcinoma, and multiple completed Phase 2 and Phase 3 trials use paclitaxel-containing regimens. This is already accepted standard therapy, so the assessment is a confirmation of established use rather than novel repurposing. The Phase 3 trials mostly test combinations or nab-paclitaxel, so direct evidence for solvent-based paclitaxel alone is limited in the sampled list.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications and approved indication text. The licence records contain no indication text, and this gap blocks safety screening.
- Detailed mechanism of action data from DrugBank.
- Confirmation of the Canadian approved breast cancer indications by formulation (solvent-based versus albumin-bound).
- A safety monitoring plan covering myelosuppression, neuropathy, hypersensitivity, hepatic impairment and the listed drug interactions.

**Other predicted indications (for reference):**
- Estrogen-receptor negative breast cancer (L1) and estrogen-receptor positive breast cancer (L1): Proceed with Guardrails. These are already standard practice, and the Phase 3 evidence is partly indirect (nab-paclitaxel or HER2-driven studies).
- Hormone-resistant breast carcinoma (L2): Proceed with Guardrails. The evidence is mostly Phase 1/2 combination studies.
- Breast carcinoma by gene expression profile (L2): research question only. The trials are biomarker studies.
- Ehrlich tumour carcinoma, bilateral breast carcinoma, nipple carcinoma, parameningeal embryonal rhabdomyosarcoma, and botryoid-type embryonal rhabdomyosarcoma of the vagina: Hold. The evidence is preclinical, case reports, or model prediction only.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

