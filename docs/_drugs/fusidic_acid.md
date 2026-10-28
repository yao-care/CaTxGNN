---
layout: default
title: Fusidic Acid
parent: Model Prediction Only (L5)
nav_order: 421
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "FUSIDIC ACID"
predicted_indications: ["exposure keratitis", "non-human animal disease", "otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "parasitic eyelid infestation"]
description: "Fusidic Acid: predicted new indication Exposure keratitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Fusidic Acid
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

## Fusidic Acid: Exposure keratitis
{: .text-alpha }

## One-Sentence Summary

Fusidic acid is an antibacterial agent used mainly against Gram-positive infections, especially Staphylococcus.
The TxGNN model predicts it may be effective for **exposure keratitis**,
but there are **0 clinical trials** and only **1 publication** (a case series on a different organism) behind this prediction, so the evidence is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Exposure keratitis |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 6 of 6) |
| Number of DINs | 6 (valid: 6) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Fusidic acid inhibits bacterial protein synthesis by binding elongation factor G. Its activity is mainly against Gram-positive organisms such as Staphylococcus. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description relies on the general understanding of the drug.

Exposure keratitis is mainly a mechanical or desiccation disorder of the cornea, in which the surface dries out because the eyelids do not close properly. Antibacterial activity would only matter if a secondary infection developed. The one retrieved paper is a case series of ocular Tsukamurella infections. It is not a study of fusidic acid in exposure keratitis. The link between the original indications and this prediction is therefore indirect and speculative.

It is worth noting that a licensed ophthalmic product (FUCITHALMIC) is already marketed in Canada. This suggests ocular use for bacterial infection is established, but that is different from evidence for exposure keratitis itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31246677](https://pubmed.ncbi.nlm.nih.gov/31246677/) | 2019 | Case series | Cornea | Largest case series of Tsukamurella-associated ophthalmic infections, covering clinical spectrum, risk factors, treatment and outcome. It does not study fusidic acid in exposure keratitis. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02243862 | FUCITHALMIC | Not specified | Not specified |
| 00586668 | FUCIDIN CREAM 2% | Not specified | Not specified |
| 00586676 | FUCIDIN OINTMENT 2% | Not specified | Not specified |
| 02528096 | TARO-FUSIDIC ACID | Not specified | Not specified |
| 02474883 | FUCIBET | Not specified | Not specified |

A sixth authorization, FUCIDIN H (DIN 02238578), is also valid. All 6 of 6 licenses are valid.

---

## Safety Considerations

The knowledge graph lists the following conditions as contraindication-related for this drug. These come from graph relationships, not from package insert text, and should be verified against the label:

- **Hepatic and renal:** liver failure, liver disease, kidney disease, gallbladder disease
- **Ocular:** herpes simplex virus keratitis, open-angle glaucoma, glaucoma, ocular hypertension, eye infectious disease, conjunctivitis
- **Metabolic:** diabetes mellitus, diabetic ketoacidosis, potassium deficiency, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease
- **Cardiac:** atrial fibrillation, atrioventricular block, Adams-Stokes syndrome, Wolff-Parkinson-White syndrome
- **Gastrointestinal:** Clostridium difficile colitis, colitis, perinatal necrotizing enterocolitis, dyskinesia of esophagus
- **Neuromuscular and respiratory:** myasthenia gravis, neuromuscular junction disease, respiratory failure, central nervous system origin vertigo
- **Other:** pyoureter

Several of these entries (for example the cardiac and metabolic ones) look unusual for fusidic acid, which suggests the graph may mix in class-level or combination-product signals (the Canadian list includes combination-type brands such as FUCIDIN H and FUCIBET). They should be interpreted cautiously.

No drug interaction records were found. Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but no clinical trials exist and the single publication is an unrelated-organism case series. Exposure keratitis is mainly a non-infectious surface disorder, so the mechanistic link is weak. The package insert safety information has also not yet been obtained.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, plus approved indication text and dosage forms for each DIN
- Detailed mechanism-of-action data
- Evidence on whether fusidic acid has any role in infected or secondary exposure keratitis, including ophthalmic-use clinical data
- Review of the other predictions, in particular **otitis externa** (score 0.9984, 5 supporting microbiology papers, mostly canine). It has a more plausible mechanism, as typical pathogens such as *S. aureus* are within fusidic acid's spectrum. However, there are no clinical studies, and it may reflect an existing use rather than a novel one. It may be a better candidate for a research question than exposure keratitis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

