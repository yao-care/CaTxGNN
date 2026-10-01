---
layout: default
title: Cabazitaxel
parent: Model Prediction Only (L5)
nav_order: 139
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

# Cabazitaxel: From Metastatic Castration-Resistant Prostate Cancer to Female Breast Carcinoma

## One-Sentence Summary

Cabazitaxel is a taxane chemotherapy drug. According to the publications in this pack, it is used for docetaxel-pretreated metastatic castration-resistant prostate cancer.
The TxGNN model predicts it may be effective for **female breast carcinoma**, with **20 publications** but **no registered clinical trials** in the pack supporting this direction.
Nine of the other ten predicted indications are prediction-only, with no supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic castration-resistant prostate cancer (from published literature; the Health Canada records supplied have no indication text) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 (one randomized Phase II study, GENEVIEVE; its results are not visible in the supplied abstract) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cabazitaxel is a taxane that stabilizes microtubules and arrests cells in mitosis. Detailed mechanism-of-action data are not available in the DrugBank record supplied. The mechanism above comes from the literature and the pack's rationale notes.

Breast cancer is a taxane-responsive tumour type, and paclitaxel and docetaxel are already widely used in it. This makes the prediction mechanistically plausible.

Preclinical studies add two further points:
- Cabazitaxel is less affected by P-glycoprotein-mediated efflux and shows better binding in cells with high βIII-tubulin. It may therefore work in taxane-resistant settings.
- In triple-negative breast cancer models, it affects macrophages and improves CD47-targeted immunotherapy.

Most of the breast cancer literature is formulation and delivery work in cell and animal models (liposphere, NLC, micelle, nanoparticle). It is not clinical proof of benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

The literature below refers to one trial, NCT01934894 (cabazitaxel plus lapatinib), but its registry record was not part of the pack.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28768217](https://pubmed.ncbi.nlm.nih.gov/28768217/) | 2017 | RCT (Phase II, open-label) | Eur J Cancer | GENEVIEVE: neoadjuvant cabazitaxel vs weekly paclitaxel in operable HER2-negative breast cancer (triple-negative or luminal B). Primary endpoint was pCR rate; results are not in the supplied abstract |
| [21339064](https://pubmed.ncbi.nlm.nih.gov/21339064/) | 2011 | Phase I/II | Eur J Cancer | Cabazitaxel plus capecitabine in metastatic breast cancer after anthracycline and taxane; assessed MTD, safety, PK and activity |
| [29678476](https://pubmed.ncbi.nlm.nih.gov/29678476/) | 2018 | Phase II dose-finding | Clin Breast Cancer | Cabazitaxel plus lapatinib in HER2+ metastatic breast cancer with brain metastases (NCT01934894) |
| [25416788](https://pubmed.ncbi.nlm.nih.gov/25416788/) | 2015 | Mechanistic study | Mol Cancer Ther | Cabazitaxel was less cross-resistant than paclitaxel and docetaxel in multidrug-resistant models, including MCF-7 breast cancer variants |
| [33753567](https://pubmed.ncbi.nlm.nih.gov/33753567/) | 2021 | Preclinical | J Immunother Cancer | Cabazitaxel's effect on macrophages improves CD47-targeted immunotherapy in triple-negative breast cancer |
| [28567478](https://pubmed.ncbi.nlm.nih.gov/28567478/) | 2017 | Preclinical | Cancer Chemother Pharmacol | βIII-tubulin enhances cabazitaxel efficacy compared with docetaxel |
| [30529259](https://pubmed.ncbi.nlm.nih.gov/30529259/) | 2019 | Preclinical | J Control Release | Cabazitaxel nanoparticles gave complete remission in 6 of 8 tumours in a patient-derived breast cancer xenograft, better than free drug |
| [30521787](https://pubmed.ncbi.nlm.nih.gov/30521787/) | 2019 | Preclinical | Chem Phys Lipids | Cabazitaxel plus thymoquinone co-loaded lipospheres as a combination for breast cancer |
| [33360926](https://pubmed.ncbi.nlm.nih.gov/33360926/) | 2021 | Preclinical | Colloids Surf B | Cabazitaxel-loaded nanostructured lipid carriers evaluated in breast cancer cell lines |
| [21076710](https://pubmed.ncbi.nlm.nih.gov/21076710/) | 2010 | Review | Drugs Today | Cabazitaxel has a favourable PK and safety profile and reduced P-gp-mediated resistance; neutropenia and neuropathy are the most common toxicities |

---

## Canada Market Information

| DIN | Product Name | Dosage Form |
|---------|------|------|
| 2553791 | Cabazitaxel for Injection | Injection (per product name) |
| 2495635 | Cabazitaxel for Injection | Injection (per product name) |
| 2487500 | Cabazitaxel for Injection | Injection (per product name) |
| 2487497 | Cabazitaxel for Injection | Injection (per product name) |
| 2553783 | Cabazitaxel for Injection | Injection (per product name) |

Approved indication text and manufacturer were not provided in the Health Canada records supplied.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (taxane, antimicrotubule agent) |
| Myelosuppression Risk | High (neutropenia is among the most common toxicities in the literature supplied) |
| Emetogenicity Classification | Low to moderate; please confirm against the package insert |
| Monitoring Items | CBC with differential, liver and renal function; neuropathy assessment |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Breast cancer is a plausible new use. Taxanes are established there, and a randomized Phase II study (GENEVIEVE) exists. However, no clinical trial records are supplied, the study outcomes are not visible, and most of the breast cancer literature is preclinical. Health Canada safety information is also missing, which the pack flags as a blocking gap for safety screening.

The other predicted indications are prediction-only (L5) and should stay on Hold. This applies to the sickle cell disease subtypes, HIV, hyperthyroidism, rheumatoid arthritis and neuroblastoma. The sickle cell subtypes share identical scores, which suggests a graph artifact, and myelosuppression is a concern for the non-malignant conditions.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking)
- Full GENEVIEVE results (pCR rate and safety) and the registry record for NCT01934894
- Mechanism-of-action data from DrugBank
- A comparison against current taxane standards of care in breast cancer, in specific subtypes such as triple-negative or taxane-resistant disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

