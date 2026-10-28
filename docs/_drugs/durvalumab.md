---
layout: default
title: Durvalumab
parent: Model Prediction Only (L5)
nav_order: 310
evidence_level: L5
indication_count: 6
monitor_inn: "Durvalumab"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
last_modified_at: 2026-10-28
description: "Durvalumab: predicted new indication Uterine ligament adenocarcinoma (evidence level L5). Approved use: Transitional cell carcinoma"
---

# Durvalumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Durvalumab: From Transitional Cell Carcinoma to Uterine Ligament Adenocarcinoma
{: .text-alpha }

## One-Sentence Summary

Durvalumab is marketed in Canada as IMFINZI, and transitional cell carcinoma is listed as its original indication.
The TxGNN model's top-ranked prediction is **uterine ligament adenocarcinoma**, and **no clinical trials or publications** currently study this disease directly.
The evidence is therefore model prediction only (L5). The data compiled for this report show some research activity in a related disease, endocervical carcinoma (1 Phase 1 trial and 2 publications).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Transitional cell carcinoma (relation recorded in the knowledge graph; the Canadian licence record contains no indication text) |
| Predicted New Indication | Uterine ligament adenocarcinoma |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Number of approvals | 1 licence (DIN) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, durvalumab is a PD-L1 immune checkpoint inhibitor. Blocking PD-L1 may restore anti-tumour T-cell activity in cancers with immune infiltration.

The link between the original indication (transitional cell carcinoma) and the predicted one (uterine ligament adenocarcinoma) is a shared checkpoint-blockade rationale. Plausibly, PD-L1 blockade could apply to gynaecologic adenocarcinomas with immune infiltration, but this is speculative. No study in the compiled data addresses this disease, and the mechanism cannot be verified from the data provided.

For context, the other predicted indications are mostly cervical or uterine-ligament tumours: endocervical carcinoma, adenoid cystic carcinoma of the cervix uteri, uterine ligament serous adenocarcinoma, and signet ring cell and intestinal variants of cervical mucinous adenocarcinoma. Only endocervical carcinoma has any related studies. The remaining predictions have no trials or literature.

## Clinical Trial Evidence

Currently no clinical trials are registered for uterine ligament adenocarcinoma.

For reference, one trial was found for the related predicted indication endocervical carcinoma. It does not study the top-ranked disease directly and is not counted toward its evidence level:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03452332](https://clinicaltrials.gov/study/NCT03452332) | Phase 1 | Completed | 20 | Hypofractionated radiotherapy with durvalumab and tremelimumab in recurrent or metastatic cervical, vaginal or vulvar cancer; early safety and feasibility study |

## Literature Evidence

Currently no related literature is available for uterine ligament adenocarcinoma.

For reference, the following publications relate to the predicted indication endocervical carcinoma and are not direct evidence for the top-ranked disease:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37467967](https://pubmed.ncbi.nlm.nih.gov/37467967/) | 2023 | Review | Biomedical journal | Review of small cell neuroendocrine carcinoma of the cervix, a rare aggressive tumour with limited trial evidence |
| [42518016](https://pubmed.ncbi.nlm.nih.gov/42518016/) | 2026 | Nonrandomized clinical trial | Oncology and therapy | Phase I study of ceralasertib plus durvalumab in Chinese patients with advanced solid tumours |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02468816 | IMFINZI | Not specified | Not specified in the licence record |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (PD-L1 checkpoint inhibitor, based on general knowledge) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: The interaction query completed with 81 records. The examples below come from the first 20 records returned.
  - **Major**: adalimumab
  - **Moderate**: corticosteroids (hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone, methylprednisolone, deflazacort), roflumilast, alefacept, alemtuzumab, anakinra, tetanus toxoid vaccine, anthrax vaccine
  - **Minor**: zinc salts (acetate, gluconate, sulfate, chloride)

  Corticosteroids and other immunosuppressants may counteract the immune-activating effect of checkpoint blockade, so combined use needs clinical review.

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or publication directly studies durvalumab in uterine ligament adenocarcinoma. The high TxGNN score (0.9992) is a computational prediction only, so the evidence level is L5.

**To proceed, the following is needed:**
- Direct clinical or preclinical evidence in uterine ligament adenocarcinoma, for example PD-L1 expression and immune infiltration profiling of this tumour type
- Detailed mechanism of action data
- Health Canada package insert warnings and contraindications, which are required before safety screening
- Approved indication text and dosage form for the IMFINZI licence
- Consideration of endocervical carcinoma as a better-supported alternative direction, since a Phase 1 trial with durvalumab exists there, though it is early-stage and small (n=20)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

