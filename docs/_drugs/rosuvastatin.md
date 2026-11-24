---
layout: default
title: Rosuvastatin
parent: Model Prediction Only (L5)
nav_order: 825
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
monitor_inn: "ROSUVASTATIN"
predicted_indications: ["cholesterol-ester transfer protein deficiency", "brain stem infarction", "HIV infectious disease", "hypoalphalipoproteinemia", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "ABri amyloidosis"]
description: "Rosuvastatin: predicted new indication Cholesterol-ester transfer protein deficiency (evidence level L5). In Canada: at least 20 DINs"
---

# Rosuvastatin
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

## Rosuvastatin: Cholesterol-ester transfer protein deficiency
{: .text-alpha }

## One-Sentence Summary

Rosuvastatin is a statin originally used to treat high cholesterol and related conditions, including hyperlipidemia, homozygous familial hypercholesterolemia and atherosclerosis.
The TxGNN model predicts it may be effective for **cholesterol-ester transfer protein (CETP) deficiency**.
However, **0 clinical trials** and **0 publications** currently support this direction, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Cholesterol-ester transfer protein deficiency |
| TxGNN Prediction Score | 0.9954 |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | Marketed (marketed DINs on record: at least 20) |
| Number of DINs | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for rosuvastatin: "CRESTOR is an inhibitor of HMG‑CoA reductase, the rate-limiting enzyme that converts 3‑hydroxy‑3‑methylglutaryl coenzyme A to mevalonate, a precursor of cholesterol." ([DailyMed: Crestor (rosuvastatin) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=325a5d0e-9a72-4015-9fcd-1655fb504cee), label version 2026-09-23; accessed 2026-11-19.) Based on known information, rosuvastatin is a statin (an HMG-CoA reductase inhibitor). It lowers LDL cholesterol (LDL-C) by reducing cholesterol synthesis in the liver, and it is well established for hyperlipidemia and familial hypercholesterolemia.

CETP deficiency is also a disorder of lipid metabolism. It raises HDL cholesterol and lowers LDL cholesterol. This shared lipid-metabolism territory is probably why the model scored the pairing so highly.

The mechanistic link is speculative, though. Rosuvastatin already lowers LDL-C, and CETP deficiency tends to lower it as well. There is no clear unmet need that a statin would address in this condition. No clinical or literature evidence was found to support the prediction, so the high score should be read as a model signal, not as evidence of benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Rosuvastatin has 20 valid single-ingredient licences in Canada. Dosage form and approved-indication text are not available for these licences.

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02337975 | APO-ROSUVASTATIN | ROSUVASTATIN (ROSUVASTATIN CALCIUM) | Marketed |
| 02338726 | SANDOZ ROSUVASTATIN | ROSUVASTATIN (ROSUVASTATIN CALCIUM) | Marketed |
| 02378531 | PMS-ROSUVASTATIN | ROSUVASTATIN (ROSUVASTATIN CALCIUM) | Marketed |
| 02378558 | PMS-ROSUVASTATIN | ROSUVASTATIN (ROSUVASTATIN CALCIUM) | Marketed |
| 02378566 | PMS-ROSUVASTATIN | ROSUVASTATIN (ROSUVASTATIN CALCIUM) | Marketed |
| 02380056 | RIVA-ROSUVASTATIN | ROSUVASTATIN (ROSUVASTATIN CALCIUM) | Marketed |
| 02397803 | MINT-ROSUVASTATIN | ROSUVASTATIN (ROSUVASTATIN CALCIUM) | Marketed |
| 02411644 | ROSUVASTATIN | ROSUVASTATIN (ROSUVASTATIN CALCIUM) | Marketed |
| 02413078 | MAR-ROSUVASTATIN | ROSUVASTATIN (ROSUVASTATIN CALCIUM) | Marketed |
| 02413108 | MAR-ROSUVASTATIN | ROSUVASTATIN (ROSUVASTATIN CALCIUM) | Marketed |
| 02438917 | ACH-ROSUVASTATIN | ROSUVASTATIN (ROSUVASTATIN CALCIUM) | Marketed |
| 02438933 | ACH-ROSUVASTATIN | ROSUVASTATIN (ROSUVASTATIN CALCIUM) | Marketed |
| 02442604 | AURO-ROSUVASTATIN | ROSUVASTATIN (ROSUVASTATIN CALCIUM) | Marketed |
| 02444976 | BIO-ROSUVASTATIN | ROSUVASTATIN (ROSUVASTATIN CALCIUM) | Marketed |
| 02498367 | JAMP ROSUVASTATIN TABLETS | ROSUVASTATIN (ROSUVASTATIN CALCIUM) | Marketed |
| 02500140 | AG-ROSUVASTATIN | ROSUVASTATIN (ROSUVASTATIN CALCIUM) | Marketed |
| 02505576 | PRZ-ROSUVASTATIN | ROSUVASTATIN (ROSUVASTATIN CALCIUM) | Marketed |
| 02505592 | PRZ-ROSUVASTATIN | ROSUVASTATIN (ROSUVASTATIN CALCIUM) | Marketed |
| 02505606 | PRZ-ROSUVASTATIN | ROSUVASTATIN (ROSUVASTATIN CALCIUM) | Marketed |
| 02536625 | NRA-ROSUVASTATIN TABLETS | ROSUVASTATIN (ROSUVASTATIN CALCIUM) | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

The data contain only part of the DINs for this ingredient; the list may be incomplete.

<!-- licenses:end -->

---

## Safety Considerations

Label-based warnings and contraindications are not available in the data compiled for this report. Please refer to the package insert for these.

- **Contraindication signals (from the TxGNN knowledge graph, not label text)**: liver disease, gallbladder disease, hypothyroidism, myxedema, congenital hypothyroidism, myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, substance abuse/dependence, rhabdomyolysis, nodular fasciitis, injury, proteinuria.
- **Drug Interactions**: 100 interactions were identified, of which the first 20 were reviewed.
  - **Major**: fenofibrate, atazanavir.
  - **Moderate** (examples): atorvastatin, ezetimibe, bempedoic acid, amiodarone, paclitaxel, alpelisib, apalutamide, ethanol.
  - **Minor**: levonorgestrel, norethisterone, desogestrel.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score (0.9954) but no supporting trials or publications. The mechanistic link is speculative, and CETP deficiency has no clear unmet need that a statin would address.

**To proceed, the following is needed:**
- Any clinical, genetic or mechanistic evidence for statin use in CETP deficiency, such as case series or lipid-response data.
- A clear clinical rationale for what benefit rosuvastatin would add in this condition.
- Mechanism of action data and package-insert warnings and contraindications to support safety screening.
- Review of the major interactions (fenofibrate, atazanavir) and the myopathy and liver-related contraindication signals, if the project advances.

**Context from other predictions:** HIV infection (L2) has Phase 2 trial evidence. It concerns cardiovascular and metabolic comorbidity and would be an adjunctive use, not treatment of HIV itself.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Crestor (rosuvastatin) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=325a5d0e-9a72-4015-9fcd-1655fb504cee) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

