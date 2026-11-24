---
layout: default
title: Bupivacaine
parent: Model Prediction Only (L5)
nav_order: 134
evidence_level: L5
indication_count: 4
monitor_inn: "Bupivacaine"
predicted_indications: ["acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "amyopathic dermatomyositis"]
last_modified_at: 2026-11-24
description: "Bupivacaine: predicted new indication acrodermatitis chronica atrophicans (evidence level L5). In Canada: 16 DINs (15 marketed, 1 dormant)"
---

# Bupivacaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Bupivacaine: Amide local anesthetic (sodium channel blocker) → acrodermatitis chronica atrophicans
{: .text-alpha }

## One-Sentence Summary

Bupivacaine is an amide local anesthetic that is marketed in Canada under multiple licences.
The TxGNN model predicts it may be effective for **acrodermatitis chronica atrophicans**, with a score of **0.9923**.
There are currently **no clinical trials and no publications** supporting this direction, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | acrodermatitis chronica atrophicans |
| TxGNN Prediction Score | 0.9923 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 15 of 16; dormant: 1) |
| Number of DINs | 16 (marketed: 15) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for bupivacaine: "Local anesthetics block the generation and the conduction of nerve impulses presumably by increasing the threshold for electrical excitation in the nerve, by slowing the propagation of the nerve impulse, and by reducing the rate of rise of the action potential. In general, the progression of anesthesia is related to the diameter, myelination, and conduction velocity of affected nerve fibers." ([DailyMed: Exparel (bupivacaine) prescribing information, Pacira Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bb5a9e59-0f51-11df-8a39-0800200c9a66), label version 2026-11-09; accessed 2026-11-19.) Bupivacaine is generally known as an amide local anesthetic that blocks voltage-gated sodium channels and thereby interrupts nerve conduction.

Acrodermatitis chronica atrophicans is the late skin manifestation of Borrelia infection, and its treatment relies on antibiotics. The only plausible role for bupivacaine is symptomatic relief of neuropathic pain, which is speculative. The high score reflects a model-based association, not a demonstrated mechanism, and no study cited here addresses this disease directly.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 01976141 | SENSORCAINE | BUPIVACAINE HYDROCHLORIDE | Marketed |
| 01976168 | SENSORCAINE | BUPIVACAINE HYDROCHLORIDE | Marketed |
| 01976184 | SENSORCAINE WITH EPINEPHRINE | BUPIVACAINE HYDROCHLORIDE; EPINEPHRINE (EPINEPHRINE BITARTRATE) | Marketed |
| 01976206 | SENSORCAINE WITH EPINEPHRINE | BUPIVACAINE HYDROCHLORIDE; EPINEPHRINE (EPINEPHRINE BITARTRATE) | Marketed |
| 02241915 | MARCAINE E | BUPIVACAINE HYDROCHLORIDE; EPINEPHRINE BITARTRATE | Marketed |
| 02241916 | MARCAINE E | BUPIVACAINE HYDROCHLORIDE; EPINEPHRINE BITARTRATE | Marketed |
| 02241917 | MARCAINE | BUPIVACAINE HYDROCHLORIDE | Marketed |
| 02305909 | MARCAINE | BUPIVACAINE HYDROCHLORIDE | Marketed |
| 02443686 | BUPIVACAINE INJECTION BP | BUPIVACAINE HYDROCHLORIDE | Marketed |
| 02443694 | BUPIVACAINE INJECTION BP | BUPIVACAINE HYDROCHLORIDE | Marketed |
| 02460645 | BUPIVACAINE HYDROCHLORIDE IN DEXTROSE INJECTION USP | BUPIVACAINE HYDROCHLORIDE | Marketed |
| 02474247 | MARCAINE | BUPIVACAINE HYDROCHLORIDE; EPINEPHRINE BITARTRATE | Marketed |
| 02488930 | BUPIVACAINE HYDROCHLORIDE INJECTION, USP | BUPIVACAINE HYDROCHLORIDE | Marketed |
| 02512424 | BUPIVACAINE HYDROCHLORIDE IN DEXTROSE INJECTION USP | BUPIVACAINE HYDROCHLORIDE | Marketed |
| 02536714 | BUPIVACAINE HYDROCHLORIDE IN DEXTROSE INJECTION USP | BUPIVACAINE HYDROCHLORIDE | Marketed |
| 02381850 | BUPIVACAINE HCL 0.5% AND EPINEPHRINE 1:200,000 INJECTION | BUPIVACAINE HYDROCHLORIDE; EPINEPHRINE BITARTRATE | Dormant |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

The table above lists each DIN with its current status in the DPD.

<!-- review:begin ca-lic-20261106-bupivacaine-1 -->

> **Review correction (2026-11-24)**: Originally stated: "All 16 licences are valid single-ingredient products; the five above are shown as examples." Removed: it described the products as single-ingredient or combination products in a way that did not match the Health Canada DPD data (the Health Canada Drug Product Database as of 2026-11-06). Revised 2026-11-24: the number of DINs and any reference to the earlier licence table, which showed only some of the DINs, were removed from the corrected sentence; the Quick Overview and the table under Canada Market Information show the current number and status of DINs. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261106-bupivacaine-1 -->

## Safety Considerations

- **Drug Interactions**: 56 interactions were recorded. Those with a "Moderate" level are aprepitant and liposomal morphine. Others, such as pantoprazole, omeprazole, vancomycin, atropine, and several corticosteroids (prednisone, hydrocortisone, dexamethasone), have an unclassified severity level.
- **Conditions flagged as contraindications in the compiled data** (not taken from label text): hypertension, liver failure and liver disease, kidney disease, epilepsy, COPD, respiratory failure, coronary artery disease, myocardial infarction, atrial fibrillation, heart conduction disease, sudden cardiac arrest, diabetes mellitus, hypothyroidism, inflammatory bowel disease, angle-closure glaucoma, and others.
- Bupivacaine is myotoxic at high concentrations, and neonates are at added risk of systemic local anesthetic toxicity.

Please also refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications, and the proposed mechanism is speculative. The disease is an infection that needs antibiotic treatment, so bupivacaine has no clear disease-modifying role.

**To proceed, the following is needed:**
- Published or registered studies that directly address this disease
- Mechanism of action data and a clear mechanistic rationale
- Package insert warnings and contraindications from Health Canada
- A defined route of administration and a safety review for the target population

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "single-ingredient"; revised 2026-11-24 to remove the DIN count and the reference to the earlier licence table | Corrected (revised 2026-11-24; earlier version kept in the record) | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Exparel (bupivacaine) prescribing information, Pacira Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bb5a9e59-0f51-11df-8a39-0800200c9a66) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

