---
layout: default
title: Auranofin
parent: Model Prediction Only (L5)
nav_order: 83
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Auranofin: predicted new indication Colobomatous microphthalmia-rhizomelic dysplasia syndrome (evidence level L5). Approved use: Rheumatoid arthritis"
---

# Auranofin
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

# Auranofin: From Rheumatoid Arthritis to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Auranofin is a gold-based medicine originally used to treat rheumatoid arthritis.
The TxGNN model predicts it may be effective for **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, a rare congenital disorder.
This prediction currently has **no clinical trials** and **no publications** behind it; it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis |
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Auranofin is a gold-containing drug whose efficacy in rheumatoid arthritis is established. In general terms it is known to modulate inflammatory pathways, but this is not supported by the data compiled here.

No mechanistic link to the predicted condition could be established. The only support is the high TxGNN knowledge-graph score (99.56%). The predicted disease is a rare congenital disorder with eye and skeletal malformations. It is very different from an adult inflammatory joint disease, and no pharmacological reason is apparent for an anti-rheumatic drug to help with a developmental condition.

A second prediction, brachydactyly-syndactyly syndrome (score 99.24%), also has no trials, no publications and no mechanistic rationale. Both predictions should be treated as hypothesis-generating signals only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 01916823 | RIDAURA | Not listed | Not listed |

---

## Safety Considerations

**Contraindication-related conditions (from the TxGNN knowledge graph, not from label text):**
The knowledge graph links auranofin with the following conditions as contraindications. They should be checked against the official label.
- Blood disorders: hematologic disease, thrombocytopenia, neutropenia, agranulocytosis, leukopenia
- Kidney and liver: kidney disease, liver disease, hepatitis, gallbladder disease
- Skin and allergy: exanthem, exfoliative dermatitis, urticaria, angioedema, atopic eczema, dermatitis
- Lung: pulmonary fibrosis, postinflammatory pulmonary fibrosis
- Gut: colitis, necrotizing enterocolitis, pyoureter
- Metabolic and cardiovascular: diabetes mellitus, diabetic ketoacidosis, hypertension, hypertensive disorder
- Autoimmune and other: systemic lupus erythematosus (including pediatric), Sjogren syndrome, dry eye syndrome

**Drug Interactions:** 86 potential interactions were identified. Examples from the list reviewed:
- **Major:** Deferiprone, Proguanil, Chloroquine
- **Moderate:** Metronidazole, Tinidazole, Benznidazole, Rosuvastatin, Simvastatin, Disulfiram
- **Unknown severity:** Warfarin, Prednisone, Prednisolone, Omeprazole, Pantoprazole, Lansoprazole, Ranitidine, Misoprostol, Clarithromycin, Calcitriol, Folic acid

The Health Canada package insert warnings were not available for this report. Please refer to the package insert for the official safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials, no literature and no identifiable mechanism. The disease is a congenital malformation syndrome, which makes a benefit from an anti-rheumatic drug biologically unlikely. The knowledge graph also lists many contraindicated conditions, including serious blood, kidney and liver disorders.

**To proceed, the following is needed:**
- Mechanism of action data for auranofin (for example from DrugBank)
- The Health Canada package insert, with its warnings and contraindications, to allow safety screening
- A biological rationale linking auranofin to the genetic or developmental pathways of the predicted disease
- Preclinical or mechanistic studies, since no human evidence currently exists
- A review of whether a drug with this safety profile is suitable for the rare, likely paediatric population affected
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

