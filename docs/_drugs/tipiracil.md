---
layout: default
title: Tipiracil
parent: Model Prediction Only (L5)
nav_order: 916
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-20
description: "Tipiracil: predicted new indication Cecum villous adenoma (evidence level L5). Approved use: Colorectal cancer (malignant colon neoplasm, colonic neoplasm…"
monitor_inn: "Tipiracil"
predicted_indications: ["cecum villous adenoma", "lipoma of colon", "cecum neuroendocrine tumor G1", "colonic lymphangioma", "cecal disease", "colon leiomyoma", "benign neoplasm of cecum", "cavernous hemangioma of colon", "colorectal gastrointestinal stromal tumor"]
---

# Tipiracil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Tipiracil: From Colorectal Cancer to Cecum Villous Adenoma
{: .text-alpha }

## One-Sentence Summary

Tipiracil is a component of the trifluridine/tipiracil combination (marketed in Canada as LONSURF), originally used to treat colorectal cancer.
The TxGNN model predicts it may be effective for **cecum villous adenoma**, but **no clinical trials and no publications** currently support this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Colorectal cancer (malignant colon neoplasm, colonic neoplasm, squamous cell carcinoma of colon) |
| Predicted New Indication | Cecum villous adenoma |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 2 of 2) |
| Number of DINs | 2 (marketed: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for trifluridine and tipiracil (a combination product containing tipiracil): "LONSURF consists of a thymidine-based nucleoside analog, trifluridine, and the thymidine phosphorylase inhibitor, tipiracil, at a molar ratio 1:0.5 (weight ratio, 1:0.471). Inclusion of tipiracil increases trifluridine exposure by inhibiting its metabolism by thymidine phosphorylase." ([DailyMed: Lonsurf (trifluridine and tipiracil) prescribing information, Taiho Pharmaceutical Co., Ltd.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f5beed22-d71d-4c0d-8dca-2c7317d65d85), label version 2025-11-05; accessed 2026-11-19.) Based on known information, tipiracil is a thymidine phosphorylase inhibitor. It is marketed only in combination with trifluridine, a cytotoxic nucleoside analogue, for metastatic colorectal cancer. Tipiracil prevents rapid breakdown of trifluridine, which raises its exposure and antitumour activity.

A villous adenoma of the cecum is anatomically and histologically related to colorectal neoplasia, which probably explains the high model score. However, it is a benign, premalignant lesion. There is no evidence that a cytotoxic combination would be appropriate for it, and the mechanism has not been documented for this indication. The prediction should be treated as a hypothesis only.

Other top-ranked predictions show the same pattern:
- **Benign lesions** (colon lipoma, leiomyoma, lymphangioma, cavernous hemangioma): no plausible link to the drug's mechanism.
- **Cecum neuroendocrine tumor G1**: low proliferative index, so antimetabolite activity is unlikely to be effective.
- **Colorectal gastrointestinal stromal tumor**: driven by KIT/PDGFRA mutations and generally resistant to conventional cytotoxic chemotherapy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature directly supports the predicted indication of cecum villous adenoma. Publications retrieved for other lower-ranked predictions only concern the approved colorectal cancer use or its safety, for example:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32655959](https://pubmed.ncbi.nlm.nih.gov/32655959/) | 2020 | Case report | Case Rep Oncol Med | Readministration of cancer drugs in a patient with chemorefractory metastatic colorectal cancer (cecal carcinoma) |
| [30677817](https://pubmed.ncbi.nlm.nih.gov/30677817/) | 2018 | Case report | Dermatol Online J | Leukocytoclastic vasculitis with late-onset Henoch-Schönlein purpura after trifluridine/tipiracil in metastatic appendiceal cancer |

These are not evidence for the predicted indication.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02472104 | LONSURF | Not specified | Not specified |
| 02472112 | LONSURF | Not specified | Not specified |

---

## Cytotoxicity

Tipiracil is used only in combination with the cytotoxic agent trifluridine, which is used for colorectal cancer.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic combination (trifluridine, a nucleoside analogue, plus tipiracil, a thymidine phosphorylase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; haematological parameters (CBC) are generally monitored with cytotoxic agents |
| Handling Protection | Follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Drug Interactions**: 14 interaction records were found. Thirteen are rated Moderate:
  - Cimetidine
  - Tafenoquine
  - Ketoconazole
  - Brigatinib
  - Crizotinib
  - Encorafenib
  - Ethinylestradiol
  - Lenvatinib
  - Medroxyprogesterone acetate
  - Megestrol acetate
  - Ribociclib
  - Rucaparib
  - Vandetanib

  The remaining record is a pharmacology entry showing tipiracil binding to the SARS-CoV-2 non-structural protein 15 target, with no severity rating.
- **Literature safety signal**: One case report described leukocytoclastic vasculitis with Henoch-Schönlein purpura after trifluridine/tipiracil treatment.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for cecum villous adenoma is supported by model score only (L5), with no trials or literature. The disease is a benign, premalignant lesion, and exposing patients to a cytotoxic combination is hard to justify without supporting evidence. None of the other top-ranked predictions has direct evidence either.

**To proceed, the following is needed:**
- Mechanism of action data and a documented rationale for a premalignant or benign lesion
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Preclinical or early clinical data for the predicted indication
- A risk-benefit assessment of cytotoxic treatment for a benign lesion
- Approved indication text and dosage form details for the two DINs

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Lonsurf (trifluridine and tipiracil) prescribing information, Taiho Pharmaceutical Co., Ltd.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f5beed22-d71d-4c0d-8dca-2c7317d65d85) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

