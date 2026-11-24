---
layout: default
title: Lansoprazole
parent: Model Prediction Only (L5)
nav_order: 524
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "LANSOPRAZOLE"
predicted_indications: ["duodenal obstruction"]
description: "Lansoprazole: predicted new indication Duodenal obstruction (evidence level L5). In Canada: at least 20 DINs"
---

# Lansoprazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Lansoprazole: Duodenal obstruction
{: .text-alpha }

## One-Sentence Summary

Lansoprazole is a proton pump inhibitor originally used for acid-related conditions such as gastric ulcer, duodenal ulcer, gastroesophageal reflux disease (GERD) and Zollinger-Ellison syndrome.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Duodenal obstruction |
| TxGNN Prediction Score | 0.9968 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs on record: at least 19; dormant: 1) |
| Number of DINs | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for lansoprazole: "Lansoprazole belongs to a class of antisecretory compounds, the substituted benzimidazoles, that suppress gastric acid secretion by specific inhibition of the (H +, K + )-ATPase enzyme system at the secretory surface of the gastric parietal cell. Because this enzyme system is regarded as the acid (proton) pump within the parietal cell, lansoprazole has been characterized as a gastric acid-pump inhibitor, in that it blocks the final step of acid production." ([DailyMed: Prevacid (lansoprazole) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=71ba78cb-7e46-43eb-9425-fa130f537f84), label version 2025-07-08; accessed 2026-11-19.) Based on general pharmacology, lansoprazole is a proton pump inhibitor that suppresses gastric acid secretion, and its efficacy in acid-related diseases such as GERD, esophagitis, and peptic and duodenal ulcer is well established.

Duodenogastric (bile) reflux is the backflow of duodenal contents into the stomach. Lowering gastric acidity may reduce mucosal injury and symptoms when refluxed contents are present, which links the condition to lansoprazole's approved uses.

This benefit is likely to be symptomatic and indirect. Proton pump inhibitors do not reduce bile reflux itself or restore pyloric or duodenal motility. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It is a computational prediction only.

A second predicted indication, **duodenal obstruction** (score 0.9968), has no clinical trials or supporting literature. It is a mechanical or structural condition treated surgically or endoscopically, and acid suppression could at most help with secondary complications. It is not considered a credible repurposing target at present.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | European Journal of Clinical Pharmacology | Update on clinical use and pharmacokinetics of proton pump inhibitors as first-choice drugs for peptic ulcer, H. pylori infection, GERD, NSAID-related GI lesions and Zollinger-Ellison syndrome. It does not directly address duodenogastric reflux. |

## Canada Market Information

Lansoprazole has 20 valid single-ingredient licences in Canada. Dosage form and approved indication text are not available in the data compiled for this report.

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02165503 | PREVACID | LANSOPRAZOLE | Marketed |
| 02165511 | PREVACID | LANSOPRAZOLE | Marketed |
| 02249464 | PREVACID FASTAB | LANSOPRAZOLE | Marketed |
| 02249472 | PREVACID FASTAB | LANSOPRAZOLE | Marketed |
| 02280515 | TEVA-LANSOPRAZOLE | LANSOPRAZOLE | Marketed |
| 02280523 | TEVA-LANSOPRAZOLE | LANSOPRAZOLE | Marketed |
| 02293811 | APO-LANSOPRAZOLE | LANSOPRAZOLE | Marketed |
| 02293838 | APO-LANSOPRAZOLE | LANSOPRAZOLE | Marketed |
| 02353830 | MYLAN-LANSOPRAZOLE | LANSOPRAZOLE | Marketed |
| 02353849 | MYLAN-LANSOPRAZOLE | LANSOPRAZOLE | Marketed |
| 02357682 | LANSOPRAZOLE | LANSOPRAZOLE | Marketed |
| 02357690 | LANSOPRAZOLE | LANSOPRAZOLE | Marketed |
| 02366282 | PRO-LANSOPRAZOLE | LANSOPRAZOLE | Marketed |
| 02385643 | SANDOZ LANSOPRAZOLE | LANSOPRAZOLE | Marketed |
| 02385651 | SANDOZ LANSOPRAZOLE | LANSOPRAZOLE | Marketed |
| 02385767 | LANSOPRAZOLE | LANSOPRAZOLE | Marketed |
| 02402610 | TARO-LANSOPRAZOLE | LANSOPRAZOLE | Marketed |
| 02402629 | TARO-LANSOPRAZOLE | LANSOPRAZOLE | Marketed |
| 02410389 | LANSOPRAZOLE | LANSOPRAZOLE | Marketed |
| 02422816 | RIVA-LANSOPRAZOLE | LANSOPRAZOLE | Dormant |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

The data contain only part of the DINs for this ingredient; the list may be incomplete.

<!-- licenses:end -->

The remaining licences cover generic lansoprazole products (Riva, Taro, Apo, Teva, Sandoz, Pro and others).

## Safety Considerations

- **Disease-level contraindication signals (from the knowledge graph, not label text):** These include hypertension, long QT syndrome and torsades de pointes, liver failure and liver disease, kidney disease, porphyria, congestive heart failure, osteoporosis, blood coagulation disorders, stroke and cerebrovascular disorders, myocardial infarction, anaemia and haemoglobinopathy, *Clostridium difficile* colitis, myasthenia gravis and others. These should be verified against the official product labelling.
- **Drug Interactions:** 100 interactions were identified in the interaction database. Examples include:
  - **Major:** acalabrutinib, atazanavir
  - **Moderate:** hydrochlorothiazide, amphotericin B, amikacin, ampicillin, atorvastatin, fenofibrate, apalutamide, aprepitant, bosutinib, brigatinib, bromocriptine
  - **Minor:** acetylsalicylic acid, axitinib, brivaracetam, cyanocobalamin

Please refer to the package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are a blocking gap for safety screening
- Detailed mechanism-of-action data for lansoprazole
- Targeted literature search and clinical evidence on proton pump inhibitors in duodenogastric (bile) reflux
- Dosage form and approved indication details for the Canadian licences
- A clinical rationale showing benefit beyond symptom relief, if the research question is pursued

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for lansoprazole is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Prevacid (lansoprazole) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=71ba78cb-7e46-43eb-9425-fa130f537f84) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

