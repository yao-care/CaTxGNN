---
layout: default
title: Irinotecan
parent: Model Prediction Only (L5)
nav_order: 496
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
monitor_inn: "IRINOTECAN"
predicted_indications: ["female breast carcinoma"]
description: "Irinotecan: predicted new indication Female breast carcinoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Irinotecan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Irinotecan: Female breast carcinoma
{: .text-alpha }

## One-Sentence Summary

Irinotecan is a topoisomerase I inhibitor, originally used to treat metastatic colon cancer and pancreatic adenocarcinoma.
The TxGNN model predicts it may be effective for **female breast carcinoma**.
The supporting evidence is mostly early-phase: **9 clinical trials** (only 2 directly test irinotecan in breast cancer or solid tumours) and **20 publications** are currently linked to this direction, and no Phase 3 trial of free irinotecan in breast cancer was found.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 0.9908 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 9 of 9) |
| Number of DINs | 9 (valid: 9) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the compiled drug record. Based on established pharmacology, irinotecan is a topoisomerase I inhibitor. Its active metabolite, SN-38, causes DNA damage and apoptosis in rapidly dividing cells. This mechanism is not specific to one tumour type, so activity in breast carcinoma is biologically plausible.

The strongest indirect support comes from sacituzumab govitecan, an anti-Trop-2 antibody-drug conjugate that carries SN-38 as its payload. It has Phase 3 evidence in HR+/HER2- and triple-negative metastatic breast cancer. This validates SN-38 as a payload in breast cancer, but it does not show that free irinotecan works. Delivery, exposure and toxicity differ between the two.

Direct evidence for irinotecan itself in breast cancer is limited to early-phase combination studies (with gemcitabine, capecitabine and UCN-01) and a 1998 review. A 2003 article notes that irinotecan has only "marginal activity" in breast cancer as a single agent, with possible synergy when sequenced after mitomycin. The high TxGNN score is a computational prediction, not clinical proof.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00083148](https://clinicaltrials.gov/study/NCT00083148) | Phase 1 | Completed | 12 | Irinotecan followed by capecitabine in advanced breast carcinoma. Directly relevant, but small, with no efficacy conclusions |
| [NCT00031681](https://clinicaltrials.gov/study/NCT00031681) | Phase 1 | Completed | 41 | UCN-01 plus irinotecan in resistant solid tumours, with a triple-negative breast cancer expansion |
| [NCT00004095](https://clinicaltrials.gov/study/NCT00004095) | Phase 1 | Completed | 38 | Irinotecan plus gemcitabine in unresectable or metastatic solid tumours. Mixed population, not breast-specific |
| [NCT03678883](https://clinicaltrials.gov/study/NCT03678883) | Phase 2 | Active, not recruiting | 350 | 9-ING-41 (GSK-3β inhibitor) alone or with chemotherapy in refractory cancers. Irinotecan's contribution cannot be separated |
| [NCT05453825](https://clinicaltrials.gov/study/NCT05453825) | Phase 2 | Unknown | 180 | Navicixizumab basket study, alone or with paclitaxel or irinotecan, including a triple-negative breast cancer cohort. Irinotecan's role is unclear |
| [NCT02419495](https://clinicaltrials.gov/study/NCT02419495) | Phase 1 | Terminated | 221 | Selinexor with several standard chemotherapy or immunotherapy regimens. No breast-specific irinotecan evidence |
| [NCT06840886](https://clinicaltrials.gov/study/NCT06840886) | Phase 1 | Recruiting | 426 | First-in-human study of PHST001 in advanced solid tumours. Indirect relevance |
| [NCT06769425](https://clinicaltrials.gov/study/NCT06769425) | Phase 1 | Recruiting | 157 | HS-10502 (PARP1 inhibitor) combination in advanced solid tumours. Irinotecan relevance unclear |
| [NCT05238831](https://clinicaltrials.gov/study/NCT05238831) | Early Phase 1 | Withdrawn | 0 | Adaptive precision-medicine pilot (SMMART-ACT). No participants enrolled, so no usable evidence |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32223649](https://pubmed.ncbi.nlm.nih.gov/32223649/) | 2020 | Phase 3 design paper | Future Oncology | TROPiCS-02: sacituzumab govitecan (SN-38 payload) in HR+/HER2- metastatic breast cancer |
| [25944802](https://pubmed.ncbi.nlm.nih.gov/25944802/) | 2015 | Phase 1/2 trial | Clin Cancer Res | First-in-human trial of sacituzumab govitecan in diverse metastatic solid tumours |
| [41371050](https://pubmed.ncbi.nlm.nih.gov/41371050/) | 2026 | Phase 2 study | Eur J Cancer | PHENOMENAL: liposomal irinotecan in HER2-negative breast cancer with brain metastases |
| [40877204](https://pubmed.ncbi.nlm.nih.gov/40877204/) | 2025 | Clinical study | Cancer Reports | Etirinotecan pegol (PEGylated irinotecan-type agent) in active brain metastases from lung or breast cancer |
| [9726101](https://pubmed.ncbi.nlm.nih.gov/9726101/) | 1998 | Review | Oncology (Williston Park) | Irinotecan activity in lymphoma, leukaemia, and breast, pancreatic, ovarian and small-cell lung cancers |
| [12800602](https://pubmed.ncbi.nlm.nih.gov/12800602/) | 2003 | Review | Oncology (Williston Park) | Rationale for sequential mitomycin and irinotecan in advanced breast cancer; marginal single-agent activity |
| [28558150](https://pubmed.ncbi.nlm.nih.gov/28558150/) | 2017 | Review | Cancer | Safety and pharmacokinetics of sacituzumab govitecan in diverse epithelial cancers |
| [26101915](https://pubmed.ncbi.nlm.nih.gov/26101915/) | 2015 | Preclinical | Oncotarget | Trop-2 as a target for the SN-38 antibody-drug conjugate IMMU-132 |
| [40749148](https://pubmed.ncbi.nlm.nih.gov/40749148/) | 2025 | Early-phase study | J Clin Oncol | Dendrimer-nanoparticle SN-38 (DEP-SN38) in advanced solid tumours |
| [19059062](https://pubmed.ncbi.nlm.nih.gov/19059062/) | 2008 | Review | Clin Lab Med | Pharmacogenomics of irinotecan and tamoxifen, including genotyping recommendations |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02528789 | Irinotecan Hydrochloride Injection | Injection | Not listed in the data |
| 02501279 | Irinotecan Hydrochloride Injection | Injection | Not listed in the data |
| 02501295 | Irinotecan Hydrochloride Injection | Injection | Not listed in the data |
| 02258218 | Irinotecan Hydrochloride Injection USP | Injection | Not listed in the data |
| 02467135 | Onivyde | Injection | Not listed in the data |

Nine valid single-ingredient DINs are listed in total. Only the first five are shown here.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (topoisomerase I inhibitor) |
| Emetogenicity Classification | Moderate to high (general class knowledge; please confirm against the package insert) |
| Monitoring Items | CBC with differential, liver function (including bilirubin), renal function, electrolytes, and monitoring for diarrhoea |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindication signals (from a knowledge graph, not label text)**: kidney disease, liver disease, gallbladder disease, pancreatitis, pyoureter, thrombocytopenia, neutropenia, agranulocytosis, anaemia (including macrocytic anaemia), ileus, intestinal obstruction, hyperbilirubinaemia (including hereditary forms and Gilbert syndrome), interstitial lung disease and diarrhoeal disease.
- **Drug Interactions**: 100 interactions were found in total. The main ones are:
  - **Major**: clarithromycin.
  - **Moderate**: aprepitant, dexamethasone, cimetidine, miconazole, metreleptin and eluxadoline.
  - **Moderate (laxatives and osmotic agents)**: bisacodyl, picosulfuric acid, magnesium sulfate, magnesium citrate, magnesium hydroxide, castor oil, glycerin, lactitol, lactulose, mannitol, mineral oil and phenolphthalein.
  - **Minor**: levofloxacin.

Package insert warnings and contraindications were not retrieved. Please refer to the Health Canada package insert for official safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible and the TxGNN score is high. However, direct evidence for free irinotecan in breast cancer is limited to small Phase 1 studies (n=12 and n=41) with no efficacy conclusions. The strongest supporting data concern sacituzumab govitecan, a different product. Official safety information is also missing, which blocks progression to formal safety screening. The topic is best treated as a research question for now.

**To proceed, the following is needed:**
- Download and review the Health Canada package insert (warnings, contraindications, approved indications for each DIN)
- Obtain detailed mechanism of action data (for example from DrugBank)
- Review the PHENOMENAL Phase 2 study (liposomal irinotecan in breast cancer with brain metastases) for efficacy and safety signals
- Search for Phase 2 or later trials of irinotecan or liposomal irinotecan specific to breast cancer
- Assess the differences between free irinotecan and SN-38-based products in delivery, exposure and toxicity
- Set up a safety monitoring plan covering myelosuppression, diarrhoea and UGT1A1 genotype considerations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

