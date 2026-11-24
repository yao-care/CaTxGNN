---
layout: default
title: Ivabradine
parent: Model Prediction Only (L5)
nav_order: 506
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
description: "Ivabradine: predicted new indication hypertrichosis (disease) (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "IVABRADINE"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "nephrogenic syndrome of inappropriate antidiuresis"]
---

# Ivabradine
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

## Ivabradine: From an Unspecified Original Indication to hypertrichosis (disease)
{: .text-alpha }

## One-Sentence Summary

Ivabradine is a heart-rate-lowering drug that is marketed in Canada. The data compiled for this report do not state its approved indication.
The TxGNN model predicts it may be effective for **hypertrichosis**, with a score of 0.9979.
There are **0 clinical trials** and **0 publications** supporting this direction, so the prediction is based on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 0.9979 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 2 of 2) |
| Number of DINs | 2 (marketed: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for ivabradine: "Corlanor blocks the hyperpolarization-activated cyclic nucleotide-gated (HCN) channel responsible for the cardiac pacemaker I f current, which regulates heart rate. In clinical electrophysiology studies, the cardiac effects were most pronounced in the sinoatrial (SA) node, but prolongation of the AH interval has occurred as has PR interval prolongation." ([DailyMed: Corlanor (ivabradine) prescribing information, Amgen Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=92018a65-38f6-45f7-91d4-a34921b81d0d), label version 2026-11-09; accessed 2026-11-19.) Ivabradine is known to selectively inhibit the HCN channels (the If, or "funny", current) in the sinoatrial node, which slows heart rate. This is general pharmacology and was not retrieved as structured data.

No established link exists between this mechanism and hair follicle biology. HCN channels are found in some tissues outside the heart, but any role in hair growth is speculative. The high TxGNN score (0.9979) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other predicted indications are even less supported:

| Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|
| Ambras type hypertrichosis universalis congenita | 0.9972 | L5 | A congenital genetic disorder (TRPS1 regulation). No plausible pathway from HCN blockade, and paediatric safety concerns (bradycardia, visual phenomena). |
| Malformation syndrome with odontal and/or periodontal component | 0.9972 | L5 | A heterogeneous developmental group. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. |
| Syndrome with a Dandy-Walker malformation as major feature | 0.9970 | L5 | A structural developmental defect. No rationale for a symptomatic cardiac drug. |
| Isolated genetic hair shaft abnormality | 0.9969 | L5 | Caused by keratin or follicle gene defects. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. |
| Nephrogenic syndrome of inappropriate antidiuresis | 0.9908 | L5 | Caused by AVPR2 gain-of-function. HCN channels exist in the kidney, but there is no evidence of relevance. This is the most biologically conceivable candidate, yet still purely speculative. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02459973 | LANCORA | IVABRADINE (IVABRADINE HYDROCHLORIDE) | Marketed |
| 02459981 | LANCORA | IVABRADINE (IVABRADINE HYDROCHLORIDE) | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

## Safety Considerations

**Drug Interactions:** The interaction screening completed and returned 100 interacting drugs. The first 20 are listed in the data compiled for this report. Of these, 11 are rated Major and 9 are rated Moderate. The data do not explain the mechanisms. Many of the Major interactions involve drugs known to prolong the QT interval or inhibit CYP3A4, so this should be confirmed against the package insert.

- **Major:** aprepitant, clarithromycin, dolasetron, palonosetron, cisapride, clotrimazole, granisetron, levofloxacin, ondansetron, papaverine, cobicistat
- **Moderate:** famotidine, ranitidine, ranitidine (bismuth citrate), cimetidine, nizatidine, dexamethasone, metreleptin, miconazole, troglitazone

**Population note:** For the congenital paediatric candidates (such as Ambras syndrome), bradycardia and visual phenomena are a concern.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All six predictions rest on the TxGNN network score alone. There are no clinical trials, no literature, and no plausible mechanistic link between HCN channel inhibition and hair growth, developmental malformation or renal water handling. Safety review also cannot proceed, because the Canadian label warnings and contraindications are not available.

**To proceed, the following is needed:**
- The Health Canada package insert (warnings, contraindications, approved indication, dosage form), which is a blocking gap for safety screening
- Detailed mechanism of action data from DrugBank, to support any mechanistic analysis
- Preclinical or mechanistic evidence that HCN channels play a role in hair follicle biology, if hypertrichosis is to be pursued
- A review of whether the score from the TxGNN model (deep learning) only reflects similarities the model learned between related diseases, not biological evidence
- A fuller review of the 100 detected drug interactions, with a focus on the Major ones

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Corlanor (ivabradine) prescribing information, Amgen Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=92018a65-38f6-45f7-91d4-a34921b81d0d) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

