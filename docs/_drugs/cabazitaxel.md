---
layout: default
title: Cabazitaxel
parent: Model Prediction Only (L5)
nav_order: 141
evidence_level: L5
indication_count: 10
---

# Cabazitaxel
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

# Cabazitaxel: From Prostate Cancer to Female Breast Carcinoma

## One-Sentence Summary

Cabazitaxel is a taxane chemotherapy drug marketed in Canada as an injectable. The data compiled for this report do not list an approved indication, but the published literature describes its established use in docetaxel-refractory metastatic prostate cancer.
The TxGNN model predicts it may be effective for **female breast carcinoma**. No clinical trials are registered in the compiled data, and **20 publications** were retrieved, of which one is a randomised phase II study (GENEVIEVE) and one is a phase I/II study.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian license data (literature describes metastatic castration-resistant prostate cancer) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 (preclinical and mechanistic studies dominate; no registered trials in the compiled data) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold (research question) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the compiled data. Based on general taxane pharmacology, cabazitaxel is a microtubule-stabilising agent that blocks cell division. It has lower affinity for P-glycoprotein, so it may be less affected by the resistance mechanisms that limit paclitaxel and docetaxel.

Breast cancer is a taxane-responsive tumour type, and paclitaxel and docetaxel are already widely used in it. Preclinical work supports this link: cabazitaxel was relatively less cross-resistant than paclitaxel and docetaxel in resistant breast cancer cell models, and nanoparticle formulations produced complete remission in some patient-derived triple-negative breast cancer xenografts.

Human data are limited. The GENEVIEVE phase II trial compared neoadjuvant cabazitaxel with paclitaxel in HER2-negative breast cancer. Its long-term outcomes were published in 2024. The details of its results were not available in the compiled data, so they are not interpreted here.

## Clinical Trial Evidence

Currently no related clinical trials registered in the compiled data. Two published clinical studies appear in the literature table below.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28768217](https://pubmed.ncbi.nlm.nih.gov/28768217/) | 2017 | Randomised phase II | Eur J Cancer | GENEVIEVE: neoadjuvant cabazitaxel vs weekly paclitaxel in operable triple-negative or luminal B/HER2-negative breast cancer, primary endpoint pathological complete response |
| [38663168](https://pubmed.ncbi.nlm.nih.gov/38663168/) | 2024 | Randomised phase II (long-term follow-up) | ESMO Open | Long-term outcomes of GENEVIEVE; earlier pCR differences between arms were reported, long-term effects were previously unknown |
| [21339064](https://pubmed.ncbi.nlm.nih.gov/21339064/) | 2011 | Phase I/II | Eur J Cancer | Cabazitaxel plus capecitabine in metastatic breast cancer after anthracycline and taxane; assessed MTD, safety, PK and activity |
| [25416788](https://pubmed.ncbi.nlm.nih.gov/25416788/) | 2015 | Review / mechanistic | Mol Cancer Ther | Cabazitaxel was less cross-resistant than paclitaxel and docetaxel in multidrug-resistant models, including MCF-7 breast cancer variants |
| [33753567](https://pubmed.ncbi.nlm.nih.gov/33753567/) | 2021 | Preclinical | J Immunother Cancer | Cabazitaxel's effect on macrophages improves CD47-targeted immunotherapy in triple-negative breast cancer |
| [30529259](https://pubmed.ncbi.nlm.nih.gov/30529259/) | 2019 | Preclinical | J Control Release | Nanoparticle-encapsulated cabazitaxel gave complete remission of 6 of 8 tumours in a patient-derived breast cancer xenograft |
| [28504249](https://pubmed.ncbi.nlm.nih.gov/28504249/) | 2017 | Preclinical | Acta Pharmacol Sin | Cabazitaxel-loaded polymeric micelles tested against breast cancer metastasis |
| [30521787](https://pubmed.ncbi.nlm.nih.gov/30521787/) | 2019 | Preclinical | Chem Phys Lipids | Cabazitaxel and thymoquinone co-loaded lipospheres as a combination for breast cancer |
| [21076710](https://pubmed.ncbi.nlm.nih.gov/21076710/) | 2010 | Review | Drugs Today | Drug profile: favourable pharmacokinetics, reduced P-glycoprotein-mediated resistance; neutropenia and neuropathy are main toxicities |
| [21152241](https://pubmed.ncbi.nlm.nih.gov/21152241/) | 2010 | Review | Clin Interv Aging | Appraisal in advanced prostate cancer; TROPIC phase III showed a survival advantage over mitoxantrone (indirect for breast) |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02553791 | Cabazitaxel for Injection | Not specified | Not specified |
| 02495635 | Cabazitaxel for Injection | Not specified | Not specified |
| 02487500 | Cabazitaxel for Injection | Not specified | Not specified |
| 02487497 | Cabazitaxel for Injection | Not specified | Not specified |
| 02553783 | Cabazitaxel for Injection | Not specified | Not specified |

All five licences are valid single-ingredient products.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (taxane, microtubule inhibitor) |
| Myelosuppression Risk | High (neutropenia is a main toxicity per the literature) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text):** kidney disease, liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, anaemia (including macrocytic anaemia), leukopenia, hyperbilirubinaemia (including hereditary forms and Gilbert syndrome), and pyoureter. These come from model graph edges and should be confirmed against the product monograph.
- **Drug interactions:** 100 interactions were found in total. The major-level ones listed are **deferiprone** and **samarium (153Sm) lexidronam**. Moderate-level examples include aprepitant, clarithromycin, clotrimazole, metronidazole, miconazole, rosuvastatin, simvastatin, tinidazole, ticagrelor, cobicistat, deferasirox, chloroquine and disulfiram. Several of these (azoles, clarithromycin, cobicistat) are consistent with CYP3A-related interactions, but the data do not state the mechanism.

For label warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold (research question)**

**Rationale:**
Breast carcinoma is a mechanistically plausible target for a taxane, and there is some human data (a randomised phase II study and a phase I/II study). However, there are no registered trials in the compiled data, most of the evidence is preclinical, and the Canadian label data and MOA are incomplete. This supports further investigation but not a move forward yet.

**To proceed, the following is needed:**
- Obtain the Health Canada product monograph, including approved indications, warnings and contraindications (a blocking gap for safety screening)
- Obtain mechanism of action data from DrugBank
- Review the full GENEVIEVE results (pCR, survival, safety) and compare them with standard taxane therapy
- Search for registered or ongoing breast cancer trials of cabazitaxel
- Define the target breast cancer subtype (e.g. triple-negative or taxane-resistant) and a myelosuppression and interaction monitoring plan

**Other predictions:** The remaining nine predicted indications (the sickle cell syndromes, HIV infection, hyperthyroidism, neuroblastoma and rheumatoid arthritis) have no supporting trials or literature and are evidence level L5. They should stay on Hold. For several of them, myelosuppression and immunosuppression from a cytotoxic taxane would also be a concern.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

