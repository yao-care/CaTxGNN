---
layout: default
title: Ammonium Chloride
parent: Model Prediction Only (L5)
nav_order: 54
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Ammonium Chloride: predicted new indication Acute laryngopharyngitis (evidence level L5). Approved use: Pharyngitis, common cold, nasopharyngitis"
monitor_inn: "AMMONIUM CHLORIDE"
predicted_indications: ["nasal cavity disease"]
---

# Ammonium Chloride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Ammonium Chloride: From Pharyngitis and Common Cold to Acute Laryngopharyngitis

## One-Sentence Summary

Ammonium chloride was originally used for upper respiratory conditions such as pharyngitis, common cold and nasopharyngitis, and is traditionally used as an expectorant.
The TxGNN model predicts it may be effective for **acute laryngopharyngitis**, but **no clinical trials and no publications** currently support this direction. It is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pharyngitis, common cold, nasopharyngitis (from the knowledge graph; Canadian licence records contain no indication text) |
| Predicted New Indication | Acute laryngopharyngitis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ammonium chloride is traditionally used as an expectorant that may loosen mucus in the upper airway. Its use in pharyngitis, common cold and nasopharyngitis is already recognised, and mechanistically it may be applicable to acute laryngopharyngitis. This mechanistic link cannot be verified with the data compiled for this report.

The predicted condition is closely related to the existing indications, since all of them are upper respiratory tract conditions. The high score may therefore reflect proximity to known indications in the knowledge graph. This looks more like an extension of the existing pharyngitis indication than true repurposing.

A second prediction, **nasal cavity disease** (score 99.94%), is also at L5 with no trials or literature. The term is broad and overlaps with common cold and nasopharyngitis. A more specific sub-indication, such as rhinitis or sinusitis, should be defined before any further evaluation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02245592 | DAMYLIN WITH CODEINE SYRUP | Not stated | Not stated |
| 00690074 | COUGH SYRUP | Not stated | Not stated |
| 00535230 | CALMYLIN | Not stated | Not stated |

All three are valid single-ingredient authorisations; none has been cancelled.

## Safety Considerations

**Drug Interactions** (21 interactions recorded in the interaction database; 20 are itemised in the data compiled for this report, and all of those are Minor or Moderate):
- **Moderate**: amphetamine, dextroamphetamine, lisdexamfetamine, metamfetamine, benzphetamine
- **Minor**: ephedrine (including nasal), pseudoephedrine, tricyclic antidepressants (amitriptyline, clomipramine, desipramine, doxepin including topical, imipramine, nortriptyline, protriptyline, trimipramine), methadone, mexiletine, flecainide

**Knowledge-graph contraindication signals** (from drug-disease links in the knowledge graph, not from label text, so they must be checked against the official label):
- Cardiovascular: hypertension, hypertensive disorder, myocardial ischemia, coronary artery disease, sudden cardiac arrest, heart conduction disease, pulmonary edema
- Renal, hepatic and metabolic: liver failure, impaired renal function, anuria, nephrocalcinosis, hypercalcemia, phosphorus metabolism disease, adrenocortical insufficiency, Addison disease
- Endocrine: hyperthyroidism, Graves disease, thyrotoxicosis
- Gastrointestinal: peptic ulcer disease, necrotizing enterocolitis
- Eye: angle-closure and closed-angle glaucoma, ocular hypertension
- Urological: benign prostatic hyperplasia, bladder neck obstruction
- Neuropsychiatric: epilepsy, insomnia, anxiety disorder, agoraphobia, obsessive-compulsive disorder

Several of these signals may relate to combination products, such as those containing codeine or decongestants, rather than to ammonium chloride alone. Package insert warnings and contraindications for the Canadian products have not been obtained. Please refer to the package insert for label safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high model score (L5), with no clinical trials, no literature and no verifiable mechanism. The predicted condition largely overlaps with the existing indications, so it adds little new value as repurposing.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) to test the mechanistic link
- Health Canada package insert warnings, contraindications and approved indication text for the three DINs, which is required before safety screening
- A clear definition of the target indication, including a specific sub-indication in place of "nasal cavity disease"
- Targeted literature and trial searches for ammonium chloride in acute laryngopharyngitis
- Dosage form and route information to assess route compatibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

