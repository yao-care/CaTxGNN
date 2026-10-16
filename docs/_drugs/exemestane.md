---
layout: default
title: Exemestane
parent: Model Prediction Only (L5)
nav_order: 372
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
description: "Exemestane: predicted new indication Antithrombin deficiency type 2 (evidence level L5). Approved use: Not listed in the Canadian licence data"
monitor_inn: "EXEMESTANE"
predicted_indications: ["antithrombin deficiency type 2", "amenorrhea (disease)", "factor 5 excess with spontaneous thrombosis", "heparin cofactor 2 deficiency", "thrombophilia", "migraine disorder", "migraine with brainstem aura"]
---

# Exemestane
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Exemestane: From Breast Cancer to Antithrombin Deficiency Type 2

## One-Sentence Summary

Exemestane is a steroidal aromatase inhibitor that lowers estrogen levels. It is marketed in Canada under three licences, but the data compiled for this report do not list an approved indication text.
The TxGNN model predicts it may be effective for **antithrombin deficiency type 2**, but **no clinical trials and no publications** currently support this prediction. It is a graph-based prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian licence data |
| Predicted New Indication | Antithrombin deficiency type 2 |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Based on known information, exemestane is a steroidal aromatase inhibitor that blocks the conversion of androgens to estrogens and lowers circulating estrogen. It is used in hormone-receptor-positive breast cancer in postmenopausal women.

Antithrombin deficiency type 2 is an inherited defect of the *SERPINC1* gene that impairs the function of antithrombin. No plausible mechanistic path from aromatase inhibition to correcting this defect is evident. Lowering estrogen might marginally reduce estrogen-driven thrombotic risk, but this is speculative. The high score most likely reflects associations in the knowledge graph rather than a real therapeutic effect.

Other predictions follow a similar pattern:

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Amenorrhea | 99.82% | L4 | Literature covers amenorrhea as a treatment-related state in breast cancer patients, not as a condition exemestane treats |
| Factor 5 excess with spontaneous thrombosis | 99.82% | L5 | No evident mechanism |
| Heparin cofactor 2 deficiency | 99.82% | L5 | No known mechanism; likely shared thrombophilia-related graph neighbours |
| Thrombophilia | 99.67% | L5 | Aromatase inhibitors carry a lower venous thromboembolism risk than tamoxifen, but this is a safety comparison, not therapeutic evidence |
| Migraine disorder | 99.02% | L5 | Estrogen fluctuation is a migraine trigger, but aromatase inhibitors can cause headaches |
| Migraine with brainstem aura | 99.01% | L5 | Largely genetic or channelopathy basis; no supported link |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked indication, antithrombin deficiency type 2.

For the second-ranked prediction, amenorrhea, the following indirect literature was retrieved. It concerns breast cancer care and does not show that exemestane treats amenorrhea:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23108951](https://pubmed.ncbi.nlm.nih.gov/23108951/) | 2013 | Cohort | Annals of Oncology | Incidence and predictors of ovarian function recovery in breast cancer patients with chemotherapy-induced amenorrhea who switched from tamoxifen to exemestane |
| [26178334](https://pubmed.ncbi.nlm.nih.gov/26178334/) | 2015 | Review | Oncology (Williston Park) | Role of ovarian suppression in premenopausal women with hormone-receptor-positive early breast cancer |
| [26951320](https://pubmed.ncbi.nlm.nih.gov/26951320/) | 2016 | Review | Journal of Clinical Oncology | Whether estradiol monitoring is needed in women receiving ovarian suppression for breast cancer |
| [31379370](https://pubmed.ncbi.nlm.nih.gov/31379370/) | 2019 | Review | Recenti Progressi in Medicina | Role of LHRH analogues in premenopausal breast cancer; chemotherapy-induced amenorrhea is linked to lower recurrence risk |
| [28118723](https://pubmed.ncbi.nlm.nih.gov/28118723/) | 2016 | Review | Klinicka Onkologie | Aromatase inhibitor treatment in postmenopausal breast cancer and management of side effects |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02242705 | AROMASIN | Not listed | Not listed |
| 02390183 | ACT EXEMESTANE | Not listed | Not listed |
| 02407841 | MED-EXEMESTANE | Not listed | Not listed |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal therapy (steroidal aromatase inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: The interaction screen was completed and returned 100 potential interactions. Two are rated Moderate: **dexamethasone** and **troglitazone**. Most of the others, such as pantoprazole, morphine, metformin, omeprazole, simvastatin and acetylsalicylic acid, have no severity rating.
- **Other considerations**: Aromatase inhibitors are contraindicated in women with functional ovaries, and can cause headaches, which is relevant to the migraine predictions.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based score. There are no clinical trials or publications for antithrombin deficiency type 2, and no plausible mechanism connects aromatase inhibition to the *SERPINC1* defect. The evidence level is L5. None of the other six predicted indications has better support.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada
- Mechanism-of-action data for exemestane
- Approved indication text, dosage forms and manufacturers for the three Canadian licences
- Preclinical or mechanistic studies linking aromatase inhibition to antithrombin function, or a re-ranking of predictions toward indications with direct evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

