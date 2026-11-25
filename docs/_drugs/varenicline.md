---
layout: default
title: Varenicline
parent: Model Prediction Only (L5)
nav_order: 967
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-25
description: "Varenicline: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the compiled Canadian license data (smoking cessation i…"
monitor_inn: "Varenicline"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "congenital hypotrichosis milia", "hypotrichosis simplex of the scalp", "diffuse alopecia areata", "alopecia", "open-angle glaucoma", "primary hereditary glaucoma", "headache disorder", "pulmonary hypertension"]
---

# Varenicline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Varenicline: From Smoking Cessation to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Varenicline is a nicotine receptor partial agonist marketed in Canada, and it is widely known as a smoking cessation aid. Canadian license records compiled for this report do not include indication text, so that use is based on general knowledge of the drug. The TxGNN model predicts it may be effective for **migraine disorder**, but there are **0 clinical trials** and only **1 publication** (a cardiac arrest case report that does not address migraine), so this prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the compiled Canadian license data (smoking cessation is the generally known use) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 13 of 13) |
| Number of DINs | 13 (marketed: 13) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for varenicline: "Varenicline binds with high affinity and selectivity at α4β2 neuronal nicotinic acetylcholine receptors. The efficacy of CHANTIX in smoking cessation is believed to be the result of varenicline's activity at α4β2 sub-type of the nicotinic receptor where its binding produces agonist activity, while simultaneously preventing nicotine binding to these receptors." ([DailyMed: Chantix (varenicline tartrate) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f0ff4f27-5185-4881-a749-c6b7a0ca5696), label version 2026-01-23; accessed 2026-11-19.) Based on general pharmacology, varenicline is a partial agonist at α4β2 nicotinic acetylcholine receptors and a full agonist at α7 receptors. Nicotinic signaling has been loosely linked to trigeminovascular and cortical spreading depression pathways involved in migraine, but this link is speculative.

The prediction is not well supported. The only retrieved publication is a cardiac arrest case report, which is a safety signal and not evidence of efficacy in migraine. Headache is also a commonly reported adverse effect of varenicline, so the drug may worsen rather than treat migraine. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other top predictions (migraine with brainstem aura, several hair loss disorders, glaucoma subtypes, headache disorder, and pulmonary hypertension) also have no clinical trials and no supporting literature. Their scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, so they are not independent evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19585710](https://pubmed.ncbi.nlm.nih.gov/19585710/) | 2009 | Case report | Therapie | Cardiac arrest reported in a patient taking varenicline. This is a safety signal and does not address migraine efficacy. |

---

## Canada Market Information

The listed licences are valid single-ingredient products; the current number and status of DINs are shown in the Quick Overview and in the table under Canada Market Information. Dosage form, manufacturer, and approved indication text are not available in the compiled data.

<!-- review:begin ca-lic-20261125b-varenicline-1 -->

> **Review correction (2026-11-25)**: Originally stated: "Eleven valid single-ingredient licenses are listed." Corrected: DINs marketed after the March 2026 DPD extract were added to the evidence for this page (same matching rule as the original collector), so the earlier count no longer applies. The current number and status of DINs are shown in the Quick Overview and in the table under Canada Market Information. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261125b-varenicline-1 -->

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02419882 | APO-VARENICLINE | VARENICLINE (VARENICLINE TARTRATE) | Marketed |
| 02419890 | APO-VARENICLINE | VARENICLINE (VARENICLINE TARTRATE) | Marketed |
| 02435675 | APO-VARENICLINE | VARENICLINE (VARENICLINE TARTRATE) | Marketed |
| 02542951 | NRA-VARENICLINE | VARENICLINE (VARENICLINE TARTRATE) | Marketed |
| 02542978 | NRA-VARENICLINE | VARENICLINE (VARENICLINE TARTRATE) | Marketed |
| 02542986 | NRA-VARENICLINE | VARENICLINE (VARENICLINE TARTRATE) | Marketed |
| 02546949 | MINT-VARENICLINE | VARENICLINE (VARENICLINE TARTRATE) | Marketed |
| 02546957 | MINT-VARENICLINE | VARENICLINE (VARENICLINE TARTRATE) | Marketed |
| 02546965 | MINT-VARENICLINE | VARENICLINE (VARENICLINE TARTRATE) | Marketed |
| 02554445 | AURO-VARENICLINE | VARENICLINE (VARENICLINE TARTRATE) | Marketed |
| 02554453 | AURO-VARENICLINE | VARENICLINE (VARENICLINE TARTRATE) | Marketed |
| 02559897 | ZDS-VARENICLINE | VARENICLINE (VARENICLINE TARTRATE) | Marketed |
| 02559900 | ZDS-VARENICLINE | VARENICLINE (VARENICLINE TARTRATE) | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

---

## Safety Considerations

- **Disease contraindication signals (from the knowledge graph, not label text):** anxiety disorder, neurotic disorder, dysthymic disorder, bipolar disorder, major affective disorder, substance abuse/dependence, schizophrenia, acute coronary syndrome, peripheral vascular disease, intermittent vascular claudication, and peripheral arterial disease.
- **Drug Interactions:** The interaction screen returned 100 records. Most are of unknown severity. The only one graded is a minor interaction with cimetidine. Others in the list include phentermine, metformin, glimepiride, rosiglitazone, morphine, prednisone, simvastatin, epinephrine, and several proton pump inhibitors (omeprazole, pantoprazole, lansoprazole).
- **Headache:** Headache is a commonly reported adverse effect of varenicline, and a case report describes bath-related headache induced by the drug. This argues against use in migraine.
- Please refer to the package insert for full warnings and contraindications, which were not available in the compiled data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a computational score. There are no clinical trials, the single retrieved publication is an unrelated safety case report, and headache is a known adverse effect of the drug. The mechanistic link is speculative.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are required before safety screening can continue
- Approved indication text and dosage forms for the Canadian licenses
- Detailed mechanism of action data
- Preclinical or clinical evidence that nicotinic receptor modulation affects migraine, including whether the headache adverse-effect signal outweighs any potential benefit
- Review of the psychiatric and cardiovascular contraindication signals for the target migraine population

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Chantix (varenicline tartrate) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f0ff4f27-5185-4881-a749-c6b7a0ca5696) |
| 2026-11-25 | Corrected: "Eleven valid single-ingredient licenses are listed." | Corrected | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

