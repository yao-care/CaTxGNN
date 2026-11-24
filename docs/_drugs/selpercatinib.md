---
layout: default
title: Selpercatinib
parent: Model Prediction Only (L5)
nav_order: 842
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
description: "Selpercatinib: predicted new indication Pulmonary hypertension (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "SELPERCATINIB"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "migraine with brainstem aura"]
---

# Selpercatinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Selpercatinib: From an Unspecified Original Indication to Pulmonary Hypertension
{: .text-alpha }

## One-Sentence Summary

Selpercatinib is a selective RET kinase inhibitor marketed in Canada as RETEVMO, but the data compiled for this report do not state its approved indication.
The TxGNN model predicts it may be effective for **pulmonary hypertension**, but this is a model prediction only, with **0 registered clinical trials** and **3 publications**, none of which studies pulmonary hypertension.
The evidence is weak, and the supplied data suggest a possible safety signal rather than a therapeutic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 0.9918 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 2 of 2) |
| Number of DINs | 2 (marketed: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for selpercatinib: "Selpercatinib is a kinase inhibitor. Selpercatinib inhibited wild-type RET and multiple mutated RET isoforms as well as VEGFR1 and VEGFR3 with IC 50 values ranging from 0.92 nM to 67.8 nM. In other enzyme assays, selpercatinib also inhibited FGFR 1, 2, and 3 at higher concentrations that were still clinically achievable." ([DailyMed: Retevmo (selpercatinib) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7fa848ba-a59c-4144-9f52-64d090f4d828), label version 2026-09-11; accessed 2026-11-19.) Based on known information, selpercatinib is a selective RET kinase inhibitor. The literature compiled for this report relates to RET fusion-positive non-small-cell lung cancer and RET-mutated medullary thyroid carcinoma. The official Canadian indication text is not available here.

The prediction score is very high (0.9905), but the data do not document any pathway linking RET inhibition to pulmonary vascular remodelling. Multi-kinase inhibitors have been explored in pulmonary arterial hypertension, but selective RET inhibition has no established rationale in this setting. Other kinase-inhibitor classes have been associated with vascular or hypertensive adverse effects, so a safety signal is more plausible than a therapeutic benefit. The score should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39372206](https://pubmed.ncbi.nlm.nih.gov/39372206/) | 2024 | Cohort (real-world pharmacovigilance) | Frontiers in Pharmacology | Compares adverse event profiles of pralsetinib and selpercatinib using FDA adverse event reports |
| [34178121](https://pubmed.ncbi.nlm.nih.gov/34178121/) | 2021 | Cohort (retrospective) | Therapeutic Advances in Medical Oncology | Real-world use of selpercatinib in RET fusion-positive NSCLC through an access program |
| [41918669](https://pubmed.ncbi.nlm.nih.gov/41918669/) | 2026 | Case report | Cureus | Long-term management and targeted therapy in metastatic medullary thyroid carcinoma with MEN 2B and RET M918T mutation |

None of these publications addresses pulmonary hypertension as a treatment target.

---

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02516918 | RETEVMO | SELPERCATINIB | Marketed |
| 02516926 | RETEVMO | SELPERCATINIB | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (selective RET kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 records. The 20 shown in the data include the following.
  - **Major**: famotidine, ranitidine, cimetidine, rabeprazole, omeprazole, dexlansoprazole (acid-suppressing agents), aprepitant, dexamethasone, clarithromycin, magnesium oxide.
  - **Moderate**: hydrocortisone, triamcinolone, betamethasone, budesonide, pioglitazone, saxagliptin, loperamide, bisacodyl, polyethylene glycol (3350 with electrolytes).

For warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no clinical trials and no literature on pulmonary hypertension. No mechanistic link is documented, and a vascular adverse-effect signal is more plausible than benefit.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications and approved indication text (currently blocking safety screening)
- Mechanism of action data from DrugBank
- A preclinical hypothesis and supporting data linking RET inhibition to pulmonary vascular biology
- A review of pulmonary or vascular adverse events in pharmacovigilance data
- Dosage form and route information to assess route compatibility

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Retevmo (selpercatinib) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7fa848ba-a59c-4144-9f52-64d090f4d828) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

