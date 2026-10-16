---
layout: default
title: Varenicline
parent: Model Prediction Only (L5)
nav_order: 967
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Varenicline: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the compiled Canadian license data (smoking cessation i…"
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Varenicline: From Smoking Cessation to Migraine Disorder

## One-Sentence Summary

Varenicline is a nicotine receptor partial agonist marketed in Canada, and it is widely known as a smoking cessation aid. Canadian license records compiled for this report do not include indication text, so that use is based on general knowledge of the drug. The TxGNN model predicts it may be effective for **migraine disorder**, but there are **0 clinical trials** and only **1 publication** (a cardiac arrest case report that does not address migraine), so this prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the compiled Canadian license data (smoking cessation is the generally known use) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, varenicline is a partial agonist at α4β2 nicotinic acetylcholine receptors and a full agonist at α7 receptors. Nicotinic signaling has been loosely linked to trigeminovascular and cortical spreading depression pathways involved in migraine, but this link is speculative.

The prediction is not well supported. The only retrieved publication is a cardiac arrest case report, which is a safety signal and not evidence of efficacy in migraine. Headache is also a commonly reported adverse effect of varenicline, so the drug may worsen rather than treat migraine. The high score likely reflects proximity in the knowledge graph and not specific biology.

Other top predictions (migraine with brainstem aura, several hair loss disorders, glaucoma subtypes, headache disorder, and pulmonary hypertension) also have no clinical trials and no supporting literature. The hair loss and glaucoma predictions appear to cluster in shared graph neighborhoods and are not independent evidence.

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

Eleven valid single-ingredient licenses are listed. Dosage form, manufacturer, and approved indication text are not available in the compiled data. The first five are shown below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02542978 | NRA-VARENICLINE | Not available | Not available |
| 02554445 | AURO-VARENICLINE | Not available | Not available |
| 02546957 | MINT-VARENICLINE | Not available | Not available |
| 02419882 | APO-VARENICLINE | Not available | Not available |
| 02554453 | AURO-VARENICLINE | Not available | Not available |

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

