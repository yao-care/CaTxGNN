---
layout: default
title: Galantamine
parent: Model Prediction Only (L5)
nav_order: 424
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-25
description: "Galantamine: predicted new indication Psychogenic movement disorders (evidence level L5). Approved use: Alzheimer disease"
monitor_inn: "GALANTAMINE"
predicted_indications: ["psychogenic movement disorders", "chronic tic disorder", "primary orthostatic tremor", "extrapyramidal and movement disease", "benign shuddering attacks", "tremor-nystagmus-duodenal ulcer syndrome", "lingual-facial-buccal dyskinesia", "benign paroxysmal tonic upgaze of childhood with ataxia", "acute intermittent porphyria"]
---

# Galantamine
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

## Galantamine: From Alzheimer Disease to Psychogenic Movement Disorders
{: .text-alpha }

## One-Sentence Summary

Galantamine is a cholinesterase inhibitor originally used to treat Alzheimer disease.
The TxGNN model predicts it may be effective for **psychogenic movement disorders**, but **no clinical trials and no publications** were found to support this prediction. It rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Alzheimer disease |
| Predicted New Indication | Psychogenic movement disorders |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 15 of 15) |
| Number of DINs | 15 (marketed: 15) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for galantamine: "Although the etiology of cognitive impairment in Alzheimer’s disease (AD) is not fully understood, it has been reported that acetylcholine-producing neurons degenerate in the brains of patients with Alzheimer’s disease. The degree of this cholinergic loss has been correlated with degree of cognitive impairment and density of amyloid plaques (a neuropathological hallmark of Alzheimer’s disease). […] Galantamine, a tertiary alkaloid, is a competitive and reversible inhibitor of acetylcholinesterase." ([DailyMed: galantamine prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=261889d3-41c8-4655-98f7-41317778e7a1), label version 2026-07-02; accessed 2026-11-19.) Based on known pharmacology, galantamine inhibits acetylcholinesterase and allosterically modulates nicotinic acetylcholine receptors. Its efficacy in Alzheimer disease is established, and in principle cholinergic modulation could influence movement-control circuits.

The data compiled for this report do not support a link between this mechanism and psychogenic movement disorders. These disorders are functional in nature, and no study was provided showing that boosting cholinergic signalling helps. The prediction is a computational hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Galantamine is marketed in Canada under valid single-ingredient authorizations (none cancelled); the current number and status of DINs are shown in the Quick Overview and in the table under Canada Market Information. The product names indicate extended-release (ER) formulations. Dosage form and approved indication text were not available in the compiled data.

<!-- review:begin ca-lic-20261125b-galantamine-1 -->

> **Review correction (2026-11-25)**: Originally stated: "Galantamine is marketed in Canada under 12 valid single-ingredient authorizations (none cancelled)." Corrected: DINs marketed after the March 2026 DPD extract were added to the evidence for this page (same matching rule as the original collector), so the earlier count no longer applies. The current number and status of DINs are shown in the Quick Overview and in the table under Canada Market Information. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261125b-galantamine-1 -->

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02316943 | PAT-GALANTAMINE ER | GALANTAMINE (GALANTAMINE HYDROBROMIDE) | Marketed |
| 02316951 | PAT-GALANTAMINE ER | GALANTAMINE (GALANTAMINE HYDROBROMIDE) | Marketed |
| 02316978 | PAT-GALANTAMINE ER | GALANTAMINE (GALANTAMINE HYDROBROMIDE) | Marketed |
| 02339439 | MYLAN-GALANTAMINE ER | GALANTAMINE (GALANTAMINE HYDROBROMIDE) | Marketed |
| 02339447 | MYLAN-GALANTAMINE ER | GALANTAMINE (GALANTAMINE HYDROBROMIDE) | Marketed |
| 02339455 | MYLAN-GALANTAMINE ER | GALANTAMINE (GALANTAMINE HYDROBROMIDE) | Marketed |
| 02425157 | AURO-GALANTAMINE ER | GALANTAMINE (GALANTAMINE HYDROBROMIDE) | Marketed |
| 02425165 | AURO-GALANTAMINE ER | GALANTAMINE (GALANTAMINE HYDROBROMIDE) | Marketed |
| 02425173 | AURO-GALANTAMINE ER | GALANTAMINE (GALANTAMINE HYDROBROMIDE) | Marketed |
| 02443015 | GALANTAMINE ER | GALANTAMINE (GALANTAMINE HYDROBROMIDE) | Marketed |
| 02443023 | GALANTAMINE ER | GALANTAMINE (GALANTAMINE HYDROBROMIDE) | Marketed |
| 02443031 | GALANTAMINE ER | GALANTAMINE (GALANTAMINE HYDROBROMIDE) | Marketed |
| 02562154 | GALANTAMINE ER | GALANTAMINE (GALANTAMINE HYDROBROMIDE) | Marketed |
| 02562162 | GALANTAMINE ER | GALANTAMINE (GALANTAMINE HYDROBROMIDE) | Marketed |
| 02562170 | GALANTAMINE ER | GALANTAMINE (GALANTAMINE HYDROBROMIDE) | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

## Safety Considerations

- **Contraindications from the knowledge graph** (derived from drug-disease relationships in the TxGNN knowledge graph, not from package insert text): familial long QT syndrome, atrioventricular block, liver failure, liver disease, kidney disease, epilepsy, asthma (including intrinsic and allergic), chronic obstructive pulmonary disease, peptic ulcer disease, duodenal ulcer, gallbladder disease, bladder neck obstruction, and pyoureter.
- **Drug interactions:** 100 interactions were recorded, and 20 are detailed in the compiled data.
  - **Major:** bupropion.
  - **Moderate:** the H2 blockers famotidine, ranitidine and cimetidine; anticholinergic or antispasmodic agents such as atropine, dicyclomine, hyoscyamine, glycopyrronium, clidinium and trospium; clarithromycin; metronidazole; loperamide; dolasetron and palonosetron; eliglustat; lorcaserin; and bowel-preparation agents (picosulfuric acid, polyethylene glycol with electrolytes, sodium sulfate).
- Please refer to the Health Canada package insert for official warnings and contraindications, as this label information was not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are no trials, no literature, and no established mechanistic link to psychogenic movement disorders (Evidence Level L5). The knowledge-graph contraindications (cardiac conduction, hepatic, renal, respiratory, and peptic ulcer conditions) call for caution.

Among the other predictions in the data, "lingual-facial-buccal dyskinesia" (tardive dyskinesia) has the most supporting material. It includes Cochrane reviews of cholinergic drugs and a randomized crossover trial of galantamine (PMID 17388711). It could be evaluated as a separate research question.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications
- Detailed mechanism of action data
- Any clinical or preclinical evidence linking galantamine to psychogenic movement disorders
- A safety review for patients with the conditions listed above
- A decision on whether to prioritize a better-supported prediction (such as tardive dyskinesia) instead

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: galantamine prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=261889d3-41c8-4655-98f7-41317778e7a1) |
| 2026-11-25 | Corrected: "Galantamine is marketed in Canada under 12 valid single-ingredient authorizations (none cancelled)." | Corrected | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

