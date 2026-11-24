---
layout: default
title: Tapentadol
parent: Model Prediction Only (L5)
nav_order: 882
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "TAPENTADOL"
predicted_indications: ["migraine disorder", "migraine with brainstem aura"]
description: "Tapentadol: predicted new indication Migraine disorder (evidence level L5). In Canada: 8 DINs (8 marketed)"
---

# Tapentadol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Tapentadol: Migraine disorder
{: .text-alpha }

## One-Sentence Summary

Tapentadol is an opioid analgesic marketed in Canada under the NUCYNTA brand, with immediate-release and extended-release products.
The TxGNN model (deep learning) predicts it may be effective for **migraine disorder**, but this is a model prediction only, which may reflect similarities the model learned between related diseases, not biological evidence, with **0 clinical trials** and **0 directly relevant publications** supporting it.
The two publications retrieved for a related migraine node argue against, rather than for, opioid use in migraine.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9967 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 8 of 8) |
| Number of DINs | 8 (marketed: 8) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for tapentadol: "Tapentadol is a centrally-acting synthetic analgesic. The exact mechanism of action is unknown. Although the clinical relevance is unclear, preclinical studies have shown that tapentadol is a mu-opioid receptor (MOR) agonist and a norepinephrine reuptake inhibitor (NRI)." ([DailyMed: Nucynta (tapentadol hydrochloride) prescribing information, Collegium Pharmaceutical, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=80938c30-9fe3-4c7d-9d9c-5476638cfb2d), label version 2025-12-30; accessed 2026-11-19.) Based on general knowledge, tapentadol is a mu-opioid receptor agonist and a norepinephrine reuptake inhibitor. A plausible link to migraine is modulation of central pain pathways through opioid and noradrenergic signalling.

This rationale is speculative. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Opioids are generally not recommended for migraine because of the risks of medication-overuse headache, chronification of headache, and dependence.

One related prediction was also generated: **migraine with brainstem aura** (score 0.9957). This most likely reflects similarities the model learned to general migraine rather than subtype-specific biology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature was retrieved for the top prediction (migraine disorder). Neither provides direct evidence of tapentadol efficacy in migraine.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33689517](https://pubmed.ncbi.nlm.nih.gov/33689517/) | 2021 | Review | Expert Opin Pharmacother | Reviews NSAIDs and acetaminophen as alternatives to opioids for acute pain, in the context of the opioid overdose crisis. It argues against opioid use. |
| [29760569](https://pubmed.ncbi.nlm.nih.gov/29760569/) | 2018 | Cross-sectional utilization study | Drug Healthc Patient Saf | Notes that opioids are not recommended for routine migraine treatment because of medication-overuse headache and dependence risks. Examines co-prescription of opioids with triptans or serotonergic antidepressants, which carries a serotonin syndrome warning. It concerns safety and prescribing patterns, not efficacy. |

---

## Canada Market Information

Eight valid single-ingredient licences are on record. Dosage form, manufacturer and approved indication text are not available in the compiled data.

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02378272 | NUCYNTA IR | TAPENTADOL (TAPENTADOL HYDROCHLORIDE) | Marketed |
| 02378280 | NUCYNTA IR | TAPENTADOL (TAPENTADOL HYDROCHLORIDE) | Marketed |
| 02378299 | NUCYNTA IR | TAPENTADOL (TAPENTADOL HYDROCHLORIDE) | Marketed |
| 02415577 | NUCYNTA EXTENDED-RELEASE | TAPENTADOL (TAPENTADOL HYDROCHLORIDE) | Marketed |
| 02415585 | NUCYNTA EXTENDED-RELEASE | TAPENTADOL (TAPENTADOL HYDROCHLORIDE) | Marketed |
| 02415593 | NUCYNTA EXTENDED-RELEASE | TAPENTADOL (TAPENTADOL HYDROCHLORIDE) | Marketed |
| 02415607 | NUCYNTA EXTENDED-RELEASE | TAPENTADOL (TAPENTADOL HYDROCHLORIDE) | Marketed |
| 02415615 | NUCYNTA EXTENDED-RELEASE | TAPENTADOL (TAPENTADOL HYDROCHLORIDE) | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

<!-- review:begin ca-lic-20261124b-tapentadol-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Three other NUCYNTA EXTENDED-RELEASE licences (02415593, 02415607, 02415615) are also valid." Removed: it referred to the earlier licence table, which showed only some of the DINs (for example "the sixth", "the remaining …", "shown here"). The table under Canada Market Information is now generated from the Health Canada DPD data and lists every DIN in the data with its current status. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261124b-tapentadol-1 -->

---

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 interacting drugs. Examples of **Major** interactions include:
  - Bupropion
  - Morphine
  - Lorcaserin
  - Diethylpropion
  - Dolasetron
  - Palonosetron
  - Phentermine

  Examples of **Moderate** interactions include:
  - Epinephrine
  - Hyoscyamine
  - Atropine
  - Glycopyrronium
  - Dicyclomine
  - Naloxone
  - Dronabinol
  - Eluxadoline
  - Nabilone
  - Trospium
- **Serotonergic co-medication**: The retrieved literature notes a US FDA safety communication (March 2016) on the risk of serotonin syndrome when opioids are combined with triptans or serotonergic antidepressants (SSRIs, SNRIs). This matters because triptans are standard migraine therapy.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a TxGNN model (deep learning) score alone, which may reflect similarities the model learned between related diseases, not biological evidence (Evidence Level L5). There are no clinical trials, and the available literature points away from opioid use in migraine because of medication-overuse headache, dependence and serotonergic interaction risks.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Approved indication text for the Canadian licences, to confirm the original indication
- Mechanism of action data (e.g. from DrugBank) to support a mechanistic-link analysis
- Any clinical or preclinical studies of tapentadol in migraine, and a benefit-risk assessment against guideline-recommended non-opioid therapies
- Evaluation of the serotonin syndrome risk with triptans and other serotonergic drugs

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Nucynta (tapentadol hydrochloride) prescribing information, Collegium Pharmaceutical, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=80938c30-9fe3-4c7d-9d9c-5476638cfb2d) |
| 2026-11-24 | Removed: "Three other NUCYNTA EXTENDED-RELEASE licences (02415593, 02415607, 02415615) are also valid." | Corrected | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

