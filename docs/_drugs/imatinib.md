---
layout: default
title: Imatinib
parent: Model Prediction Only (L5)
nav_order: 471
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Imatinib: predicted new indication Heart fibrosarcoma (evidence level L5). Approved use: Systemic mastocytosis, GIST…"
---

# Imatinib
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

# Imatinib: From Systemic Mastocytosis and Gastrointestinal Stromal Tumor to Heart Fibrosarcoma

## One-Sentence Summary

Imatinib is a tyrosine kinase inhibitor originally used for chronic myelogenous leukaemia, gastrointestinal stromal tumour (GIST), systemic mastocytosis, dermatofibrosarcoma protuberans and hypereosinophilic syndromes.
The TxGNN model predicts it may be effective for **heart fibrosarcoma** (top-ranked prediction), but **no clinical trials** are registered and only **1 publication** (a general drug commentary) is linked to this specific indication.
Evidence is therefore weak for the top prediction, and the stronger signal in this dataset is for **liposarcoma** (3 Phase 1/2 or Phase 2 sarcoma trials).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Systemic mastocytosis, GIST, BCR-ABL1-positive chronic myelogenous leukaemia, dermatofibrosarcoma protuberans, hypereosinophilic syndrome (from the knowledge graph; no approved-indication text is available for Canadian licences) |
| Predicted New Indication | Heart fibrosarcoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 (preclinical or mechanism-level only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 16 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, imatinib inhibits the tyrosine kinases BCR-ABL, KIT and PDGFR. Its efficacy in GIST (KIT/PDGFRA-driven) and in dermatofibrosarcoma protuberans (COL1A1-PDGFB fusion driving constitutive PDGFRB activation) is established.

The link to heart fibrosarcoma is by analogy only: both are fibroblastic or mesenchymal tumours, and imatinib might work if the tumour depends on PDGFB/PDGFR signalling. No cardiac-specific data exist in the dataset. The single linked paper is a 2008 drug-bulletin commentary on new imatinib indications.

Other top-ranked predictions share this pattern. Several (fibroblastic neoplasm, conventional fibrosarcoma) are close relatives of dermatofibrosarcoma protuberans, which is already an approved indication. For fibroblastic neoplasm, the signal largely reflects the known original indication rather than a new opportunity. Other predictions (familial Mediterranean fever, familial rhabdoid tumour, ovarian myxoid liposarcoma) have no supporting evidence and weak mechanistic rationale.

---

## Clinical Trial Evidence

No clinical trials are registered for heart fibrosarcoma, the top prediction. The only trials in the dataset are linked to lower-ranked predictions, and they are the most informative clinical signal available. They are shown below for context.

**Liposarcoma (rank 6)**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00031915](https://clinicaltrials.gov/study/NCT00031915) | Phase 2 | Completed | Not reported | Imatinib in metastatic or unresectable soft tissue and bone sarcomas; liposarcoma likely a subgroup, subtype results not available |
| [NCT00154388](https://clinicaltrials.gov/study/NCT00154388) | Phase 2 | Completed | 185 | Basket study in life-threatening rare malignancies; liposarcoma enrolment not confirmed |
| [NCT00006357](https://clinicaltrials.gov/study/NCT00006357) | Phase 1/2 | Completed | 91 | Dose-finding and efficacy in advanced soft tissue sarcoma; limited subtype-level efficacy data |

**Kidney fibrosarcoma (rank 4)**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00154388](https://clinicaltrials.gov/study/NCT00154388) | Phase 2 | Completed | 185 | Same basket study; no evidence it enrolled kidney fibrosarcoma, so the link is indirect |

---

## Literature Evidence

**Heart fibrosarcoma (rank 1)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18623899](https://pubmed.ncbi.nlm.nih.gov/18623899/) | 2008 | Review | Prescrire International | Commentary on new imatinib indications, noting the evidence is not robust; no cardiac-specific data |

**Related predictions (for context)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39904126](https://pubmed.ncbi.nlm.nih.gov/39904126/) | 2025 | Guideline | Eur J Cancer | European interdisciplinary guideline update on dermatofibrosarcoma protuberans diagnosis and treatment (fibroblastic neoplasm) |
| [42062942](https://pubmed.ncbi.nlm.nih.gov/42062942/) | 2026 | Cohort | BMC Cancer | 153 Chinese patients with DFSP; Mohs surgery with postoperative imatinib (fibroblastic neoplasm / fibrosarcoma) |
| [40558511](https://pubmed.ncbi.nlm.nih.gov/40558511/) | 2025 | Preclinical | Cells | Patient-derived DFSP cell lines used to predict imatinib sensitivity; resistance arises in 10–50% of cases |
| [25852058](https://pubmed.ncbi.nlm.nih.gov/25852058/) | 2015 | Preclinical | Mol Cancer Ther | CDKN2A/p16 loss implicates CDK4 as a target in imatinib-resistant DFSP |
| [30901500](https://pubmed.ncbi.nlm.nih.gov/30901500/) | 2019 | Preclinical | Drug Dev Res | Liposomes and nanocochleates with imatinib plus dexketoprofen against fibrosarcoma |
| [19451433](https://pubmed.ncbi.nlm.nih.gov/19451433/) | 2009 | Phase 2 trial | J Clin Oncol | Imatinib in 10 sarcoma subtypes using a Bayesian hierarchical model (liposarcoma) |
| [12702540](https://pubmed.ncbi.nlm.nih.gov/12702540/) | 2003 | Report | Ann Oncol | Potential use of imatinib in ocular melanoma and liposarcoma expressing c-KIT |
| [16158966](https://pubmed.ncbi.nlm.nih.gov/16158966/) | 2005 | Report | Anticancer Res | c-kit expression in dedifferentiated and well-differentiated liposarcomas |
| [30096127](https://pubmed.ncbi.nlm.nih.gov/30096127/) | 2018 | Case report | Anti-Cancer Drugs | Imatinib-induced DRESS in a DFSP patient, with successful desensitization (safety signal) |

---

## Canada Market Information

Sixteen valid single-ingredient licences are on record, and none is cancelled. Dosage form, manufacturer and approved-indication text are not available in the data compiled for this report. Five are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02253283 | GLEEVEC | Not available | Not available |
| 02253275 | GLEEVEC | Not available | Not available |
| 02399814 | TEVA-IMATINIB | Not available | Not available |
| 02355345 | APO-IMATINIB | Not available | Not available |
| 02397285 | NAT-IMATINIB | Not available | Not available |

Other licensed products include IMATINIB (generic), MINT-IMATINIB and ACH-IMATINIB.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert; the knowledge graph lists neutropenia, thrombocytopenia, anaemia and agranulocytosis among its contraindication-related conditions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count, liver function, renal function, and fluid retention/cardiac status |
| Handling Protection | Please refer to the package insert and local handling regulations for antineoplastic agents |

---

## Safety Considerations

**Contraindication-related conditions (from the knowledge graph, not label text):** hypertension, liver failure and liver disease, kidney disease, congestive heart failure and heart failure, coronary artery disease, heart valve disease, congenital heart disease, pericardial effusion, pulmonary edema, brain edema, thrombocytopenia, neutropenia, agranulocytosis, anaemia, diabetes mellitus and diabetic ketoacidosis, hyperbilirubinaemia (including Gilbert syndrome), active peptic ulcer disease, hypophosphataemia, gallbladder disease, obesity disorder.

These come from knowledge-graph relationships and have not been verified against the Health Canada package insert. The cardiac conditions are particularly relevant to a cardiac tumour indication.

**Drug interactions:** The interaction search returned 100 records. Examples:
- **Major:** eliglustat, naloxegol
- **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), pioglitazone, glimepiride, saxagliptin, cimetidine, clarithromycin, aprepitant, morphine, naltrexone, naldemedine, lansoprazole, dexlansoprazole, metreleptin

**Other signal:** One case report describes imatinib-induced drug reaction with eosinophilia and systemic symptoms (DRESS) in a patient with dermatofibrosarcoma protuberans, which was managed with desensitization.

The package-insert warnings and contraindications for Canada have not yet been obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, heart fibrosarcoma, has no registered trials and only one non-specific commentary, so the evidence level is L4. The high TxGNN scores (all about 99.8–99.9%) do not separate well-supported predictions from unsupported ones. The best-supported item is liposarcoma (L2 per the scoring, with three sarcoma trials), but its biology (MDM2/CDK4 amplification, FUS-DDIT3) is not KIT/PDGFR-driven, and subtype-specific results are not shown. The fibroblastic neoplasm signal largely reflects dermatofibrosarcoma protuberans, which is already an approved indication.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data from DrugBank
- Subtype-level results from NCT00031915, NCT00006357 and the published Phase 2 study (PMID 19451433), to determine whether any liposarcoma or fibrosarcoma responses occurred
- Evidence of PDGFB/PDGFR or KIT pathway dependence in cardiac or conventional fibrosarcoma
- Cardiac safety assessment, given the cardiac-related contraindication signals and the cardiac site of the predicted tumour
- Review of the drug interaction profile for likely co-medications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

