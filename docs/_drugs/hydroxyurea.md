---
layout: default
title: Hydroxyurea
parent: Model Prediction Only (L5)
nav_order: 455
evidence_level: L5
indication_count: 10
---

# Hydroxyurea
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

# Hydroxyurea: From Antineoplastic Therapy to Female Breast Carcinoma

## One-Sentence Summary

Hydroxyurea is an oral antineoplastic drug used for leukemia and other neoplastic diseases, as well as sickle cell disease.
The TxGNN model predicts it may be effective for **female breast carcinoma**, but **0 clinical trials** are registered and only **2 early-phase clinical studies (1991 and 1994)** appear among the 20 publications retrieved. The rest are preclinical or indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 (preclinical and early-phase combination studies; the pack lists L3) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

The pack has no approved-indication text for the Canadian licenses, so that row is omitted.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the pack. Hydroxyurea is known to inhibit ribonucleotide reductase, which depletes dNTP pools and induces replication stress. Some breast cancer cells depend on replication-stress-avoidance or ATR/RPA2-dependent DNA repair pathways. Preclinical work shows that these cells respond to hydroxyurea, and that inhibiting RPA2-mediated repair (for example with valproic acid) sensitizes them further.

Hydroxyurea is already used against blood cancers and other neoplasms, so a link to another malignancy is plausible. However, the clinical support is thin. The only human data are 1990s phase I/II studies in which hydroxyurea was one component of a multi-drug regimen. These do not show single-agent efficacy in breast cancer. The very high TxGNN score reflects the knowledge-graph link, not confirmed clinical benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1957839](https://pubmed.ncbi.nlm.nih.gov/1957839/) | 1991 | Phase I | Am J Clin Oncol | 20 patients with advanced GI and breast cancers received 5-FU/leucovorin followed by hydroxyurea with allopurinol protection (HALF regimen) |
| [7914447](https://pubmed.ncbi.nlm.nih.gov/7914447/) | 1994 | Early-phase clinical | Bone Marrow Transplant | 26 women with responding metastatic breast cancer; hydroxyurea 18 g/m² added to cyclophosphamide and thiotepa with stem cell rescue as consolidation |
| [38211596](https://pubmed.ncbi.nlm.nih.gov/38211596/) | 2024 | Preclinical (in silico) | Drug Res | Design of hydroxyurea-lipid conjugates to improve uptake in breast cancer, targeting PI3K/AKT/mTOR |
| [28837865](https://pubmed.ncbi.nlm.nih.gov/28837865/) | 2017 | Preclinical | DNA Repair | Valproic acid sensitizes breast cancer cells to hydroxyurea by inhibiting RPA2 hyperphosphorylation-mediated DNA repair |
| [32795962](https://pubmed.ncbi.nlm.nih.gov/32795962/) | 2020 | Preclinical | DNA Repair | A valproic acid analogue acts on the same RPA2 pathway that sensitizes breast tumor cells to hydroxyurea |
| [37777742](https://pubmed.ncbi.nlm.nih.gov/37777742/) | 2023 | Preclinical (mechanistic) | Mol Cancer | EYA4 promotes breast cancer progression via replication stress avoidance, the biology hydroxyurea exploits |
| [21730979](https://pubmed.ncbi.nlm.nih.gov/21730979/) | 2011 | Preclinical | Br J Cancer | ATR inhibitor NU6027 tested in breast and ovarian cancer cell lines; hydroxyurea used as a tool compound |
| [25814515](https://pubmed.ncbi.nlm.nih.gov/25814515/) | 2015 | Preclinical | Mol Pharmacol | The ribonucleotide reductase inhibitor COH29 (same target class as hydroxyurea) inhibits DNA repair in BRCA1-defective breast cancer cells |
| [30159181](https://pubmed.ncbi.nlm.nih.gov/30159181/) | 2018 | Case report | Case Rep Hematol | Management of coexisting hormone-positive breast cancer and JAK2-positive essential thrombocythemia |
| [26844848](https://pubmed.ncbi.nlm.nih.gov/26844848/) | 2016 | Preclinical | Cancer Biother Radiopharm | In vitro and in vivo evaluation of radiolabeled hydroxyurea conjugates |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2247937 | APO-HYDROXYUREA |
| 465283 | HYDREA |
| 2530260 | RIVA-HYDROXYUREA |
| 2242920 | MYLAN-HYDROXYUREA |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antimetabolite, ribonucleotide reductase inhibitor) |
| Myelosuppression Risk | High (leukopenia, thrombocytopenia and anemia are the main dose-limiting effects) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, renal and liver function |
| Handling Protection | Follow cytotoxic drug handling regulations |

This section is based on the drug's class, since the pack contains no DrugBank toxicity data. Please refer to the package insert warnings and precautions for full details.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Other Predicted Indications in This Evidence Pack

Some other predictions have stronger support than breast carcinoma.

| Predicted Indication | TxGNN Score | Evidence Level | Note |
|------|------|------|------|
| Sickle cell-hemoglobin C disease | 99.67% | L2 | Three HbSC-specific phase 2 trials (NCT00532883, NCT02336373, NCT02640573) were all terminated. A 2025 NEJM Evidence publication ([39647172](https://pubmed.ncbi.nlm.nih.gov/39647172/)) and Cochrane reviews support hydroxyurea in sickle cell disease. Guardrails advised. |
| Sickle cell-hemoglobin D, -hemoglobin E, and -beta-thalassemia syndromes | 99.67% | L3–L4 | Class-level inference from sickle cell disease; no genotype-specific efficacy data. |
| Hereditary persistence of fetal hemoglobin-sickle cell disease | 99.67% | L4 | Incremental benefit unclear because HbF is already elevated. Hold. |
| Cervical adenosarcoma; colon, rectum and gallbladder mucinous adenocarcinoma | 99.3–99.4% | L5 | Model prediction only, with no trials or literature. Hold. |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The score is very high, but there are no registered trials. The clinical data are limited to 1990s combination-regimen studies, and the rest is preclinical. Single-agent efficacy in breast cancer has not been shown. For a myelosuppressive cytotoxic drug, that is not enough to justify moving forward.

**To proceed, the following is needed:**
- Human evidence of hydroxyurea activity in breast cancer, either as monotherapy or in rational combinations such as with ATR/RPA2-pathway modulators
- Health Canada package insert warnings and contraindications
- Mechanism-of-action data from DrugBank
- Approved-indication text for the four Canadian DINs
- A separate review of the HbSC indication, which has the strongest supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

