---
layout: default
title: Cetuximab
parent: Model Prediction Only (L5)
nav_order: 179
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Cetuximab: predicted new indication Bronchial adenomas/carcinoids, childhood (evidence level L5). Approved use: Metastatic colorectal cancer and head and neck squamous cell carcinoma"
---

# Cetuximab
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

# Cetuximab: From Colorectal and Head and Neck Cancer to Bronchial Adenomas/Carcinoids (Childhood)

## One-Sentence Summary

Cetuximab is an anti-EGFR monoclonal antibody, originally used for EGFR-expressing metastatic colorectal cancer and squamous cell carcinoma of the head and neck.
The TxGNN model predicts it may be effective for **bronchial adenomas/carcinoids (childhood)**, the top-ranked prediction, but **no clinical trials and no publications** were found for this indication.
The top prediction is therefore a model output only. Among the other predictions, **cystic neoplasm** and **pre-malignant neoplasm** have the most supporting evidence and are discussed below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic colorectal cancer and head and neck squamous cell carcinoma (the Health Canada record has no indication text; this is taken from the drug's known indications in the data compiled for this report) |
| Predicted New Indication | Bronchial adenomas/carcinoids, childhood |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known information, cetuximab is a chimeric IgG1 antibody that binds the epidermal growth factor receptor (EGFR) and blocks ligand binding, which shuts down tumour-promoting downstream signalling. Its efficacy in EGFR-expressing colorectal cancer and head and neck squamous cell carcinoma is established.

For the top-ranked prediction, the mechanistic link is weak. Childhood bronchial carcinoids are neuroendocrine tumours and are usually not EGFR-driven, and no EGFR dependence has been shown. The score of about 99.95% reflects the model's output, not clinical support.

Several lower-ranked predictions have more plausible biology:

- **Cystic neoplasm (rank 9):** EGFR is expressed in adenoid cystic and other salivary gland carcinomas. A Phase 2 study of cetuximab in salivary gland carcinomas and a Phase 1/2 trial of cetuximab with radiotherapy in adenoid cystic carcinoma exist. The term is broad, and published salivary gland data suggest limited single-agent activity.
- **Pre-malignant neoplasm (rank 10):** EGFR is upregulated in premalignant upper aerodigestive tract lesions, which supports a chemoprevention rationale.
- **Ductal or ductular proliferation (rank 2):** The term most likely maps to pancreatic ductal adenocarcinoma. KRAS mutation, present in most cases, predicts lack of benefit from anti-EGFR antibodies. The mapping to a clinical entity needs confirmation.
- **Odontogenic cyst (rank 6):** Only case reports of carcinoma arising in the cyst exist, and the evidence concerns the malignant transformation, not the benign cyst.

---

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked indication (bronchial adenomas/carcinoids, childhood). The tables below show the trials retrieved for the two best-supported predictions.

**Cystic neoplasm (rank 9)**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01192087](https://clinicaltrials.gov/study/NCT01192087) | Phase 1/2 | Unknown | 49 | Cetuximab with IMRT plus carbon ion boost in adenoid cystic carcinoma; directly relevant, non-randomized |
| [NCT00397384](https://clinicaltrials.gov/study/NCT00397384) | Phase 1 | Completed | 43 | Erlotinib plus cetuximab in advanced solid tumours; not specific to cystic neoplasms |
| [NCT00101348](https://clinicaltrials.gov/study/NCT00101348) | Phase 1/2 | Completed | 66 | Erlotinib, cetuximab and bevacizumab in metastatic solid tumours; generic population |
| [NCT01637194](https://clinicaltrials.gov/study/NCT01637194) | Phase 1 | Completed | 12 | Cetuximab plus everolimus in solid tumours; small and not disease-specific |

**Pre-malignant neoplasm (rank 10)**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00524017](https://clinicaltrials.gov/study/NCT00524017) | Phase 2 | Completed | 35 | Single-agent cetuximab in high-risk premalignant upper aerodigestive lesions; directly relevant |
| [NCT00482222](https://clinicaltrials.gov/study/NCT00482222) | Phase 3 | Unknown | 340 | Oxaliplatin/fluoropyrimidine ± cetuximab in resectable colorectal liver metastases; falls under the existing indication |
| [NCT00719199](https://clinicaltrials.gov/study/NCT00719199) | Phase 1 | Terminated | 21 | FOLFIRI plus cetuximab plus IMO-2055 in colorectal cancer; not relevant to premalignancy |
| [NCT00537823](https://clinicaltrials.gov/study/NCT00537823) | Phase 2 | Terminated | 9 | Preoperative FOLFOX-based therapy before liver resection; not relevant to premalignancy |

---

## Literature Evidence

No publications were retrieved for the top-ranked indication. Selected publications for the better-supported predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18804410](https://pubmed.ncbi.nlm.nih.gov/18804410/) | 2009 | Phase 2 trial | Oral Oncology | Cetuximab in recurrent/metastatic salivary gland carcinomas (30 patients, mostly adenoid cystic carcinoma); clinical benefit rate was the primary measure |
| [24412287](https://pubmed.ncbi.nlm.nih.gov/24412287/) | 2014 | Review | Oral Oncology | Targeting EGFR for head and neck cancer chemoprevention; EGFR is overexpressed in oral premalignant lesions |
| [33243986](https://pubmed.ncbi.nlm.nih.gov/33243986/) | 2020 | Review | Nature Reviews Disease Primers | Overview of head and neck squamous cell carcinoma |
| [35300246](https://pubmed.ncbi.nlm.nih.gov/35300246/) | 2022 | Randomized phase II | Clin Transl Radiat Oncol | Long-term results of cetuximab, gemcitabine and radiotherapy in locally advanced pancreatic cancer (PARC trial) |
| [21552097](https://pubmed.ncbi.nlm.nih.gov/21552097/) | 2012 | Phase II | Am J Clin Oncol | Gemcitabine, oxaliplatin and cetuximab in advanced pancreatic cancer |
| [22571859](https://pubmed.ncbi.nlm.nih.gov/22571859/) | 2012 | Phase I/II | Ann Oncol | Neoadjuvant cetuximab, gemcitabine and IMRT in pancreatic adenocarcinoma |
| [27797376](https://pubmed.ncbi.nlm.nih.gov/27797376/) | 2017 | Preclinical | Oncogene | Mechanism of cetuximab resistance in pancreatic ductal adenocarcinoma cells (integrin β1-driven Src-Akt bypass) |
| [41546361](https://pubmed.ncbi.nlm.nih.gov/41546361/) | 2025 | Case report | Gan to Kagaku Ryoho | Primary intraosseous carcinoma arising in a mandibular odontogenic cyst |
| [30576676](https://pubmed.ncbi.nlm.nih.gov/30576676/) | 2019 | Case report | J Oral Maxillofac Surg | Regression of metastatic primary intraosseous carcinoma treated with nivolumab |
| [32518035](https://pubmed.ncbi.nlm.nih.gov/32518035/) | 2020 | Case report | Oral Oncology | Cetuximab monotherapy for relapsing high-grade mucoepidermoid carcinoma |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02271249 | ERBITUX | Not listed | Not listed |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-EGFR monoclonal antibody) |
| Myelosuppression Risk | Low as a single agent; combination chemotherapy partners may add risk |
| Emetogenicity Classification | Low |
| Monitoring Items | Skin reactions, infusion reactions, electrolytes (magnesium, potassium, calcium); CBC and liver and renal function when combined with chemotherapy |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions:** 20 interaction records were retrieved.
  - **Major:** aminolevulinic acid and thalidomide.
  - **Moderate:** proton pump inhibitors (rabeprazole, omeprazole, dexlansoprazole, esomeprazole, lansoprazole, pantoprazole), the chemotherapy agents capecitabine, carboplatin, cisplatin, fluorouracil and oxaliplatin, and others (methoxsalen, idelalisib, omacetaxine mepesuccinate, verteporfin, topical aminolevulinic acid, topical methyl aminolevulinate).
  - **Pharmacology:** the target is EGFR (antibody).

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for them.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction, childhood bronchial adenomas/carcinoids, has no trials or literature and no established EGFR rationale, so it rests on the model score alone (L5).
- Some lower-ranked predictions are more promising as research questions, namely cystic neoplasm (adenoid cystic and salivary gland carcinoma) and pre-malignant upper aerodigestive lesions (both L2). Even these rely on small, non-randomized studies, and no randomized efficacy evidence was found.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Clarification of how ambiguous disease labels map to clinical entities (e.g., "ductal or ductular proliferation")
- For the cystic neoplasm and premalignant directions, a focused review of the existing Phase 2 data, followed by a controlled study design
- A prevention-setting safety assessment (e.g., skin toxicity) before any chemoprevention use
- Confirmation of the approved indication text for the Canadian licence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

