---
layout: default
title: Fluorouracil
parent: Model Prediction Only (L5)
nav_order: 398
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Fluorouracil: predicted new indication Botryoid-type embryonal rhabdomyosarcoma of the vagina (evidence level L5). Approved use: Superficial multifocal basal cell carcinoma, actinic keratosis…"
monitor_inn: "Fluorouracil"
predicted_indications: ["botryoid-type embryonal rhabdomyosarcoma of the vagina", "rhabdomyosarcoma (disease)", "parameningeal embryonal rhabdomyosarcoma", "embryonal extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "liver sarcoma", "sickle cell-beta-thalassemia disease syndrome", "sickle cell-hemoglobin c disease syndrome", "sickle cell-hemoglobin d disease syndrome"]
---

# Fluorouracil
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

# Fluorouracil: From Skin Conditions and Gastrointestinal Cancers to Rhabdomyosarcoma

## One-Sentence Summary

Fluorouracil is a long-established antimetabolite chemotherapy, originally used for skin conditions such as actinic keratosis and basal cell carcinoma, and for gastrointestinal cancers such as colon, pancreatic and gastric cancer.
The TxGNN model predicts it may be effective for **rhabdomyosarcoma**, with **0 registered clinical trials** and only **4 publications**, none of which show a benefit specific to fluorouracil.
This is a computational prediction with very limited supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Superficial multifocal basal cell carcinoma, actinic keratosis, and gastrointestinal cancers (colon metastases, pancreatic, gastric) |
| Predicted New Indication | Botryoid-type embryonal rhabdomyosarcoma of the vagina (top-ranked prediction); rhabdomyosarcoma (the broader category) is ranked second and is the only rhabdomyosarcoma entry with literature, so it is the focus of this report |
| TxGNN Prediction Score | 99.75% (top-ranked prediction); 99.74% for rhabdomyosarcoma |
| Evidence Level | L5 for the top-ranked prediction; L4 for rhabdomyosarcoma |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 7 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, fluorouracil is a thymidylate synthase inhibitor and antimetabolite. It disrupts DNA and RNA synthesis in rapidly dividing cells. Its efficacy in several epithelial cancers is well established.

Rhabdomyosarcoma is a rapidly proliferating soft tissue sarcoma, mostly seen in children. In principle, an antimetabolite could act against it. The prediction may also partly reflect the graph-based similarity to other cancers in which fluorouracil is used. For example, fluorouracil has an established role in biliary tract and gastrointestinal adenocarcinomas, which may influence the prediction for the bile duct rhabdomyosarcoma entries.

However, standard rhabdomyosarcoma regimens (such as VAC, VDC and IE) do not center on fluorouracil. Any contribution of fluorouracil is therefore indirect and unproven. For the more specific subtypes (vaginal botryoid, parameningeal, bile duct and prostate), no trials or publications were available, so those predictions rest on the model alone.

Other predictions in the list include liver sarcoma (L4) and several sickle cell syndromes (L5). The sickle cell predictions are highly speculative. Fluorouracil's myelosuppression and toxicity would be a major concern in a non-malignant blood disorder.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The table covers the rhabdomyosarcoma prediction (rank 2).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3884137](https://pubmed.ncbi.nlm.nih.gov/3884137/) | 1985 | Review | Cancer | Reviews adjuvant chemotherapy for childhood sarcomas, about half of which are rhabdomyosarcomas; no fluorouracil-specific benefit is described in the available text |
| [42483493](https://pubmed.ncbi.nlm.nih.gov/42483493/) | 2026 | Case report | Case Reports in Oncological Medicine | A young adult with lingual rhabdomyosarcoma progressed on cisplatin plus 5-fluorouracil (after doxorubicin plus ifosfamide); a later vincristine-based regimen was used in the third line |
| [6277228](https://pubmed.ncbi.nlm.nih.gov/6277228/) | 1981 | Review | Annals of the Academy of Medicine, Singapore | General review of curable cancers with chemotherapy, listing rhabdomyosarcoma among childhood cancers; not specific to fluorouracil |
| [3951398](https://pubmed.ncbi.nlm.nih.gov/3951398/) | 1986 | Cohort | Medical and Pediatric Oncology | Childhood nasopharyngeal carcinoma series; not directly relevant to rhabdomyosarcoma |

The only fluorouracil-specific data point is the 2026 case report, in which a fluorouracil-containing regimen did not control the disease.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00012882 | Fluorouracil Injection | Not specified | Not specified |
| 00330582 | Efudex | Not specified | Not specified |
| 02485346 | Tolak | Not specified | Not specified |
| 02473763 | Fluorouracil Injection | Not specified | Not specified |
| 02473771 | Fluorouracil Injection | Not specified | Not specified |

Two further authorizations are also valid: 02413450 (Fluorouracil Injection USP) and 02428946 (Actikerall). All 7 licenses are single-ingredient products and currently valid.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine antimetabolite) |
| Myelosuppression Risk | Medium to high for systemic use; thrombocytopenia, neutropenia, leukopenia and agranulocytosis appear among the associated conditions in the knowledge graph |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Complete blood count with differential, liver and renal function, electrolytes |
| Handling Protection | Systemic injectable forms must be handled according to cytotoxic drug handling regulations |

Please refer to the package insert warnings and precautions for full details.

---

## Safety Considerations

- **Conditions flagged as contraindication-related (from a knowledge graph, not label text):** kidney disease, liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, leukopenia, diarrheal disease, active peptic ulcer disease, pharyngitis, stomatitis, pyoureter, and dihydropyrimidine dehydrogenase (DPD) deficiency. DPD deficiency is particularly important because it can lead to severe toxicity.
- **Drug Interactions:** 100 interactions were identified. The main ones with a classified severity are:
  - Moderate: metronidazole, tinidazole
  - Minor: cimetidine, levofloxacin
  - Many others (e.g., omeprazole, pantoprazole, morphine, metformin, doxycycline) have unclassified severity.

Please refer to the package insert for the official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction scores are very high (about 99.7%), but no clinical trials exist, and the available literature contains no controlled evidence that fluorouracil benefits rhabdomyosarcoma. The only recent case report showed disease progression on a fluorouracil-containing regimen. Standard treatments for this disease do not rely on fluorouracil. The sickle cell predictions are purely speculative and carry significant toxicity concerns.

**To proceed, the following is needed:**
- Official Canadian package insert warnings and contraindications (currently missing, and a blocking gap for safety screening)
- Mechanism of action data to support the mechanistic link analysis
- Preclinical or retrospective data on fluorouracil activity in rhabdomyosarcoma models or patient series
- Approved indication text and dosage forms for the Canadian licenses
- A comparison against standard rhabdomyosarcoma regimens to judge whether fluorouracil could add value
- Screening for DPD deficiency as part of any safety plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

