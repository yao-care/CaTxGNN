---
layout: default
title: Mitomycin
parent: Model Prediction Only (L5)
nav_order: 624
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Mitomycin: predicted new indication Osteoclastic giant cell tumor of pancreas (evidence level L5). Approved use: Pancreatic adenocarcinoma"
monitor_inn: "MITOMYCIN"
predicted_indications: ["osteoclastic giant cell tumor of pancreas", "solid pseudopapillary carcinoma of pancreas", "pancreatic carcinoma with mixed differentiation", "pancreatic intraductal papillary-mucinous carcinoma", "mixed ductal-endocrine carcinoma of pancreas", "pancreatic signet ring cell adenocarcinoma", "undifferentiated pancreatic carcinoma", "malignant exocrine pancreas neoplasm", "pancreatic intraductal papillary-mucinous neoplasm", "pancreatic acinar cell cystadenocarcinoma"]
---

# Mitomycin
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

# Mitomycin: From Pancreatic Adenocarcinoma to Osteoclastic Giant Cell Tumor of the Pancreas

## One-Sentence Summary

Mitomycin is a DNA cross-linking cytotoxic agent, originally used for pancreatic adenocarcinoma.
The TxGNN model predicts it may be effective for **osteoclastic giant cell tumor of pancreas**,
but **no clinical trials and no publications** currently support this specific prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pancreatic adenocarcinoma (the approved indication text was not available for the Canadian licences; this is taken from the drug's knowledge-graph indication) |
| Predicted New Indication | Osteoclastic giant cell tumor of pancreas |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, mitomycin is a DNA cross-linking cytotoxic agent. Its efficacy in pancreatic adenocarcinoma is the basis for this prediction, and mechanistically it may be applicable to related pancreatic tumours.

Osteoclastic giant cell tumor of the pancreas is a rare variant of undifferentiated pancreatic carcinoma. Because it arises in the same organ and shares some biology with ductal adenocarcinoma, a shared sensitivity to cytotoxic agents is plausible. However, this link is untested: no trials or publications were found for this disease.

Other highly ranked predictions are also pancreatic tumour subtypes (for example solid pseudopapillary carcinoma, mixed ductal-endocrine carcinoma, signet ring cell adenocarcinoma and undifferentiated pancreatic carcinoma). They all rest on the same general cytotoxic rationale, with scores between 99.82% and 99.86%. Most have no supporting studies.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top predicted indication.

Some lower-ranked pancreatic predictions retrieved a few papers, but none test mitomycin in the predicted disease:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10897253](https://pubmed.ncbi.nlm.nih.gov/10897253/) | 2000 | Review | Strahlenther Onkol | Adjuvant and neoadjuvant radiochemotherapy in ductal pancreatic carcinoma (related to pancreatic IPMN prediction; indirect only) |
| [8361472](https://pubmed.ncbi.nlm.nih.gov/8361472/) | 1993 | Clinical study | Nihon Geka Gakkai Zasshi | Tamoxifen added to immuno-chemotherapy (including mitomycin) after resection of pancreatic carcinoma; the study tests tamoxifen, not mitomycin |
| [15983445](https://pubmed.ncbi.nlm.nih.gov/15983445/) | 2005 | Case report | Pancreatology | Pseudomyxoma peritonei with pancreatic IPMN managed with intraperitoneal hyperthermic chemoperfusion; not evidence of mitomycin efficacy in the pancreatic tumour |
| [2695183](https://pubmed.ncbi.nlm.nih.gov/2695183/) | 1989 | Review | Bull Cancer | General article on unknown primary tumours; no mitomycin-specific data |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02230451 | Mitomycin for Injection | Not specified | Not specified |
| 02464691 | Mitomycin for Injection USP | Not specified | Not specified |
| 02531941 | Mitomycin for Injection, USP | Not specified | Not specified |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (DNA cross-linking agent) |
| Myelosuppression Risk | High. Knowledge-graph contraindication links to thrombocytopenia, leukopenia and anaemia point to bone marrow toxicity |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with platelets, kidney function (including signs of haemolytic-uremic syndrome), and heart failure symptoms |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** kidney disease, pyoureter, thrombocytopenia, blood coagulation disease, anaemia, macrocytic anaemia, leukopenia, haemolytic-uremic syndrome (including the typical form), congestive heart failure, heart failure, and stomatitis.
- **Drug interactions:** 100 interactions were found in total. The main ones with a defined severity are:
  - **Major:** deferiprone, samarium (153Sm) lexidronam
  - **Moderate:** palifermin, strontium chloride Sr-89, fostamatinib
  - **Minor:** levofloxacin
  - Many other interactions (for example warfarin, simvastatin, prednisone, dexamethasone, ondansetron, omeprazole, pantoprazole and leucovorin) have no severity rating.

Package insert warnings and contraindications were not available. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (99.86%) and a general cytotoxic rationale. There are no clinical trials or directly relevant publications. The tumour is rare, and mitomycin carries significant haematological and renal risks.

**To proceed, the following is needed:**
- A literature and trial search that targets mitomycin in this specific rare tumour (for example case series, registry data)
- Detailed mechanism of action data
- Health Canada package insert warnings, contraindications, approved indications and dosage forms for the three DINs
- A review of whether the predicted disease differs enough from pancreatic adenocarcinoma to justify a separate indication
- A safety monitoring plan covering myelosuppression, kidney function and haemolytic-uremic syndrome
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

