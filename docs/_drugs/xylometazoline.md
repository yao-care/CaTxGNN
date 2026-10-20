---
layout: default
title: Xylometazoline
parent: Moderate Evidence (L3-L4)
nav_order: 986
evidence_level: L3
indication_count: 2
last_modified_at: 2026-10-13
description: "Xylometazoline: predicted new indication Nasal cavity disease (evidence level L3). Approved use: Pharyngitis, common cold"
monitor_inn: "Xylometazoline"
predicted_indications: ["nasal cavity disease", "acute laryngopharyngitis"]
---

# Xylometazoline
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **2** 
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

# Xylometazoline: From Pharyngitis and Common Cold to Nasal Cavity Disease

## One-Sentence Summary

Xylometazoline is a topical nasal decongestant, originally used for the common cold and pharyngitis.
The TxGNN model predicts it may be effective for **nasal cavity disease**,
with **no registered clinical trials** but **6 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pharyngitis, common cold (the Canadian licence records contain no indication text) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L3 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled records. Based on general pharmacology, xylometazoline is an imidazoline-derivative alpha-adrenergic agonist applied to the nose. It constricts the blood vessels of the nasal lining, which reduces swelling and nasal airway resistance. Pharmacology records list activity at alpha-2A, alpha-2B and alpha-2C adrenoceptors in humans, but no affinity data were found to confirm a primary target.

The original indications (common cold and pharyngitis) involve nasal congestion and swollen mucosa. "Nasal cavity disease" is a broader category covering the same problem, so the prediction is largely an extension of existing use rather than a completely new direction. The published studies support this, showing decongestant effects in nasal preparation for endoscopy and intubation.

A second predicted indication, acute laryngopharyngitis (score 99.89%), has no trials or literature. Pharyngitis is already an original indication, so it adds little new repurposing value and is not assessed further here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24158493](https://pubmed.ncbi.nlm.nih.gov/24158493/) | 2013 | Randomized, double-blind, placebo-controlled trial | JAMA Otolaryngol Head Neck Surg | Topical anaesthetic plus decongestant spray before flexible nasendoscopy in children, compared with placebo |
| [22427029](https://pubmed.ncbi.nlm.nih.gov/22427029/) | 2013 | Prospective randomized blinded study (100 patients) | Eur Arch Otorhinolaryngol | Cotton pledget packing compared with topical spray for nasal preparation before endoscopy |
| [24023995](https://pubmed.ncbi.nlm.nih.gov/24023995/) | 2013 | Clinical study | Korean J Anesthesiol | Xylometazoline spray compared with epinephrine gauze packing for expanding the nasal cavity before nasotracheal intubation |
| [8740084](https://pubmed.ncbi.nlm.nih.gov/8740084/) | 1996 | Double-blind randomized study (18 subjects) | Arzneimittel-Forschung | Tuaminoheptane plus N-acetylcysteine compared with xylometazoline and placebo for reducing nasal resistance; xylometazoline served as a comparator |
| [1281924](https://pubmed.ncbi.nlm.nih.gov/1281924/) | 1992 | Physiological/clinical study | Rhinology | Nasal airflow asymmetry in healthy subjects and people with common-cold rhinitis, and how xylometazoline affected it |
| [34783482](https://pubmed.ncbi.nlm.nih.gov/34783482/) | 2021 | Review | Vestnik Otorinolaringologii | Nasal mucosa changes in the elderly and treatment of inflammatory nasal and sinus disease, including combined decongestant sprays |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02208903 | Otrivin Medicated Cold & Allergy Relief with Moisturizers | Not listed | Not listed |
| 02452863 | Nasal Decongestant Spray with Moisturizers | Not listed | Not listed |
| 00653330 | Otrivin Medicated Cold & Allergy Relief | Not listed | Not listed |
| 02452812 | Decongestant Nasal Spray | Not listed | Not listed |
| 02331403 | Otrivin Medicated Complete Nasal Care | Not listed | Not listed |

All five licences are valid single-ingredient products. None are cancelled.

## Safety Considerations

- **Disease-based cautions (from the knowledge graph, not label text)**: Contraindication links were found for hypertension and other hypertensive disorders, heart and cardiovascular disease, diabetes mellitus and diabetic ketoacidosis, and hyperthyroidism (including Graves disease and thyrotoxicosis).
- **Drug Interactions**: The interaction search returned 5 records. These are pharmacology target associations (alpha-1D, alpha-2A, alpha-2B and alpha-2C adrenoceptors, and TAAR4P), not drug-drug interactions with severity ratings. Caution is also advised with MAO inhibitors, based on general pharmacology.
- **Duration of use**: Use should generally be limited to under 7 days because of the risk of rebound congestion (rhinitis medicamentosa).

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is consistent with its marketed use, and several clinical studies, including one randomized placebo-controlled trial, show decongestant effects in nasal procedures. However, there are no registered trials for this indication, and most studies are small or use xylometazoline as a comparator or part of a combination. The prediction also largely overlaps with existing use.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data, such as from DrugBank
- Approved indication text and dosage forms for the Canadian licences
- Clear definition of the target conditions within "nasal cavity disease"
- A plan limiting duration of use and screening patients with cardiovascular disease, hypertension, diabetes or thyroid disease, and those taking MAO inhibitors
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

