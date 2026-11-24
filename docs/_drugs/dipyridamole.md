---
layout: default
title: Dipyridamole
parent: Model Prediction Only (L5)
nav_order: 291
evidence_level: L5
indication_count: 6
monitor_inn: "DIPYRIDAMOLE"
predicted_indications: ["sick sinus syndrome 2, autosomal dominant", "sarcoglycanopathy", "Wildervanck syndrome", "macrocephaly, dysmorphic facies, and psychomotor retardation", "lateral sinus thrombosis", "cavernous sinus thrombosis"]
last_modified_at: 2026-11-24
description: "Dipyridamole: predicted new indication Sick sinus syndrome 2, autosomal dominant (evidence level L5). In Canada: 2 DINs (2 marketed)"
---

# Dipyridamole
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

## Dipyridamole: Sick sinus syndrome 2, autosomal dominant
{: .text-alpha }

## One-Sentence Summary

Dipyridamole is an antiplatelet and vasodilating drug with two valid single-ingredient licences in Canada.
The TxGNN model predicts it may be relevant to **sick sinus syndrome 2, autosomal dominant**, with a score of 0.9989.
There are currently **no clinical trials** and **no publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Sick sinus syndrome 2, autosomal dominant |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 2 of 2) |
| Number of DINs | 2 (marketed: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for dipyridamole: "Dipyridamole inhibits the uptake of adenosine into platelets, endothelial cells and erythrocytes in vitro and in vivo; the inhibition occurs in a dose-dependent manner at therapeutic concentrations (0.5 to 1.9 mcg/mL). This inhibition results in an increase in local concentrations of adenosine which acts on the platelet A 2 -receptor thereby stimulating platelet adenylate cyclase and increasing platelet cyclic-3',5'-adenosine monophosphate (cAMP) levels." ([DailyMed: dipyridamole prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=226099e2-70bb-4b9b-bb52-c20fbca2aec5), label version 2026-04-29; accessed 2026-11-19.) Dipyridamole is generally known to raise adenosine levels and to inhibit platelet aggregation, but these properties are not documented in the data compiled for this report.

The predicted condition is a rare inherited disorder of the heart's sinus node (HCN4-related channelopathy). No mechanistic link has been established. Dipyridamole's adenosine-enhancing effects could in theory influence sinus node function, but increased adenosine activity may worsen slow heart rhythms. This is therefore a potential safety concern rather than a likely benefit. The high TxGNN score has no clinical or literature support behind it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 00637734 | PERSANTINE | DIPYRIDAMOLE | Marketed |
| 02244475 | DIPYRIDAMOLE INJECTION, USP | DIPYRIDAMOLE | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

Both are single-ingredient products with valid status.

## Safety Considerations

- **Drug Interactions**: Interaction screening returned 100 records. The ones graded Moderate are dexfenfluramine, sibutramine and fenfluramine. Other listed interactions (for example acetylsalicylic acid, cimetidine, omeprazole, metformin, morphine and simvastatin) have no severity grade recorded.
- **Theoretical concern for this prediction**: Because dipyridamole potentiates adenosine, it could worsen bradyarrhythmia in people with sinus node dysfunction.

For all other safety information, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting clinical trials or publications, and no plausible mechanism. The adenosine-related effects of the drug raise a safety concern in sinus node disease. Evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data for dipyridamole
- Package insert warnings and contraindications from Health Canada
- Preclinical or genetic-model evidence linking dipyridamole to HCN4-related sinus node dysfunction
- A cardiac safety assessment, particularly for bradyarrhythmia

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not currently available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: dipyridamole prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=226099e2-70bb-4b9b-bb52-c20fbca2aec5) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

