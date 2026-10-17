---
layout: default
title: Cladribine
parent: Model Prediction Only (L5)
nav_order: 201
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
description: "Cladribine: predicted new indication Parameningeal embryonal rhabdomyosarcoma (evidence level L5). Approved use: Hairy cell leukemia"
monitor_inn: "CLADRIBINE"
predicted_indications: ["parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "embryonal extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "rhabdomyosarcoma (disease)", "liver sarcoma"]
---

# Cladribine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Cladribine: From Hairy Cell Leukemia to Parameningeal Embryonal Rhabdomyosarcoma

## One-Sentence Summary

Cladribine is a purine nucleoside analog originally used for hairy cell leukemia, hairy cell leukemia variant, and relapsing-remitting multiple sclerosis.
The TxGNN model predicts it may be effective for **parameningeal embryonal rhabdomyosarcoma**,
but **no clinical trials and no directly relevant publications** currently support this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hairy cell leukemia; hairy cell leukemia variant; relapsing-remitting multiple sclerosis (the Canadian license records provide no indication text) |
| Predicted New Indication | Parameningeal embryonal rhabdomyosarcoma |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, cladribine is a purine nucleoside analog. It is activated by deoxycytidine kinase (dCK), causing DNA strand breaks and apoptosis, mainly in lymphocytes and monocytes. This explains its established use in lymphoid malignancies and its role in multiple sclerosis.

The link to the predicted indication is weak. Rhabdomyosarcoma is a solid mesenchymal tumour, not a lymphoid cancer, and no cladribine-specific mechanism has been established for it. The six highest-ranked predictions are all rhabdomyosarcoma-related (embryonal subtypes at the vagina, bile duct, and prostate, plus the parent disease). Their scores (0.997–0.998) are likely correlated through the same knowledge-graph neighbourhood, so they should not be read as independent confirmations. Before any clinical consideration, preclinical validation would be needed, such as in vitro sensitivity and dCK expression in rhabdomyosarcoma cells.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature directly supports the lead prediction. The only publication retrieved was for a lower-ranked prediction (liver sarcoma) and is not direct evidence for it:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15241520](https://pubmed.ncbi.nlm.nih.gov/15241520/) | 2004 | Case report | Der Hautarzt | Successful cladribine therapy in smoldering systemic mastocytosis, a haematologic neoplasm rather than liver sarcoma |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02470179 | MAVENCLAD | Not specified | Not specified |
| 02494574 | CLADRIBINE INJECTION | Not specified | Not specified |
| 02319918 | CLADRIBINE INJECTION | Not specified | Not specified |
| 02553295 | APO-CLADRIBINE | Not specified | Not specified |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analog) |
| Myelosuppression Risk | High. The contraindication data list neutropenia, thrombocytopenia, anemia, and agranulocytosis |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with differential, renal function, and neurological assessment (peripheral neuropathy appears among the listed contraindications) |
| Handling Protection | Follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text)**: kidney disease, pyoureter, thrombocytopenia, hyperuricemia, neutropenia, agranulocytosis, peripheral nervous system disease, peripheral neuropathy, anemia, and macrocytic anemia.
- **Drug Interactions**: 100 interactions were identified. The main ones include:
  - **Major**: corticosteroids (hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone), deferiprone, and radiopharmaceuticals and radioimmunotherapy agents (ibritumomab tiuxetan, iobenguane I-131, tositumomab, samarium-153 lexidronam, strontium-89 chloride).
  - **Moderate**: palifermin, dipyridamole, cilostazol, and eltrombopag.

Official label warnings were not available, so please refer to the Health Canada package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with 0 clinical trials and no directly relevant literature. There is also no plausible mechanistic basis for a lymphoid-selective nucleoside analog in a solid tumour. The cluster of correlated rhabdomyosarcoma predictions adds no independent support, and the known myelosuppression risk raises the bar for further investigation.

**To proceed, the following is needed:**
- Preclinical validation, such as cladribine sensitivity and dCK expression in rhabdomyosarcoma cell lines or models
- Detailed mechanism of action data
- Health Canada package insert warnings and contraindications, and the approved indication text for each DIN
- A literature search focused on cladribine in paediatric solid tumours and rhabdomyosarcoma
- A benefit-risk assessment that accounts for myelosuppression and the major drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

