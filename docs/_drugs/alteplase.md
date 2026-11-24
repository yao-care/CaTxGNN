---
layout: default
title: Alteplase
parent: Model Prediction Only (L5)
nav_order: 42
evidence_level: L5
indication_count: 6
monitor_inn: "ALTEPLASE"
predicted_indications: ["heparin cofactor 2 deficiency", "congenital coronary artery anomaly", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "thrombophilia", "coronary stenosis"]
last_modified_at: 2026-11-24
description: "Alteplase: predicted new indication heparin cofactor 2 deficiency (evidence level L5). In Canada: 3 DINs (3 marketed)"
---

# Alteplase
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

## Alteplase: recombinant tissue plasminogen activator → heparin cofactor 2 deficiency
{: .text-alpha }

## One-Sentence Summary

Alteplase is a recombinant tissue plasminogen activator, a clot-dissolving (thrombolytic) drug that is currently marketed in Canada.
The TxGNN model predicts it may be useful for **heparin cofactor 2 deficiency**, an inherited clotting disorder.
This prediction rests on the model score alone: there are **no clinical trials** and **no publications** directly studying this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 0.9972 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 3 of 3) |
| Number of DINs | 3 (marketed: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for alteplase: "Alteplase is an enzyme (serine protease) that has the property of fibrin-enhanced conversion of plasminogen to plasmin. It produces limited conversion of plasminogen in the absence of fibrin. Alteplase binds to fibrin in a thrombus and converts the entrapped plasminogen to plasmin, thereby initiating local fibrinolysis." ([DailyMed: Cathflo Activase (alteplase) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=91ecdef2-95ff-42dd-a31c-c8a09cab3ad9), label version 2026-01-20; accessed 2026-11-19.) Alteplase is generally understood to act by converting plasminogen to plasmin, which breaks down fibrin in blood clots.

Heparin cofactor 2 deficiency is an inherited thrombophilia, meaning a tendency to form abnormal clots. In principle, an acute clot in an affected patient could be dissolved by a fibrinolytic drug such as alteplase. That is the only reasoning offered for this prediction, and it comes from the model score rather than from any study.

Alteplase would not correct the underlying deficiency. It could at most treat a clot that has already formed. This is a plausible but unverified idea, and the model's high score should not be read as evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered for heparin cofactor 2 deficiency.

## Literature Evidence

Currently no related literature available for heparin cofactor 2 deficiency.

## Canada Market Information

The table below lists each DIN with its current status in the DPD. The local data do not record dosage form or approved indication text for them.

<!-- review:begin ca-lic-20261106-alteplase-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Alteplase has three valid single-ingredient authorizations in Canada." Removed: it described the products as single-ingredient or combination products in a way that did not match the Health Canada DPD data (the Health Canada Drug Product Database as of 2026-11-06). Revised 2026-11-24: the number of DINs and any reference to the earlier licence table, which showed only some of the DINs, were removed from the corrected sentence; the Quick Overview and the table under Canada Market Information show the current number and status of DINs. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261106-alteplase-1 -->

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02147440 | ACTIVASE RT-PA | ALTEPLASE; WATER | Marketed |
| 02225689 | ACTIVASE RT-PA | ALTEPLASE; WATER | Marketed |
| 02245859 | CATHFLO | ALTEPLASE | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

## Safety Considerations

Package insert warnings and contraindications are not available in the compiled data. Please refer to the package insert for them.

**Drug Interactions:** The interaction screen recorded 100 interacting drugs. The first 20 returned include the following.

- **Major:** deferasirox, ibritumomab tiuxetan, tositumomab (including I-131 tositumomab), abciximab, acalabrutinib, fondaparinux, anisindione and apixaban. Most of these affect bleeding or clotting, so combined use needs close attention to bleeding risk.
- **Moderate:** acetylsalicylic acid, ibuprofen, ketorolac (including ophthalmic), fluvoxamine, fosinopril, aminocaproic acid, aprotinin, dexfenfluramine, fenfluramine and sibutramine.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no clinical trials or publications for this disease, so the evidence level is L5. Alteplase also would not treat the underlying deficiency.

**To proceed, the following is needed:**
- Clinical or case evidence that directly addresses heparin cofactor 2 deficiency
- Mechanism-of-action data for alteplase
- Package insert warnings and contraindications from Health Canada
- A bleeding-risk and concurrent-anticoagulation plan for patients with inherited clotting disorders

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "single-ingredient"; revised 2026-11-24 to remove the DIN count and the reference to the earlier licence table | Corrected (revised 2026-11-24; earlier version kept in the record) | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |
| 2026-11-19 | "Detailed mechanism-of-action data for alteplase are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cathflo Activase (alteplase) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=91ecdef2-95ff-42dd-a31c-c8a09cab3ad9) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

