---
layout: default
title: Tropicamide
parent: Model Prediction Only (L5)
nav_order: 953
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Tropicamide: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Cycloplegia"
monitor_inn: "TROPICAMIDE"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome"]
---

# Tropicamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Tropicamide: From Cycloplegia to Cauda Equina Syndrome

## One-Sentence Summary

Tropicamide is a short-acting antimuscarinic eye drop, originally used for cycloplegia and pupil dilation during eye examinations.
The TxGNN model predicts it may be effective for **cauda equina syndrome**,
but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cycloplegia (from the knowledge-graph indication record; no approved indication text is available for the Canadian products) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug in the data compiled for this report. Based on known information, tropicamide is a muscarinic antagonist (anticholinergic). Pharmacology records list it as acting on the M2, M3, M4 and M5 muscarinic receptors. It is used as a short-acting mydriatic to allow better examination of the lens, vitreous humor and retina.

Cauda equina syndrome often causes bladder and bowel dysfunction. Anticholinergic drugs can reduce detrusor (bladder muscle) overactivity, which gives a theoretical, class-level link between tropicamide and the symptoms of this condition. This link is inferred from the drug class, not from tropicamide-specific data.

There are important limits to this rationale. The main treatment for cauda equina syndrome is urgent surgical decompression, not medication. Tropicamide is marketed only as a topical ophthalmic product with minimal systemic exposure. The high score of 0.995 is a computational prediction only.

Two other predictions were also generated, and neither has trial or literature support:
- **Obsolete neurogenic bladder (score 99.13%):** Antimuscarinics are an established class for neurogenic detrusor overactivity. Better-characterized agents such as oxybutynin and solifenacin already cover this use, and the disease term is flagged as obsolete in the ontology.
- **Irritable bowel syndrome (score 99.12%):** Antispasmodic anticholinergics such as dicyclomine and hyoscyamine are used for IBS cramping. The ophthalmic route gives negligible gut exposure, and established antispasmodics already fill this niche.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00000981 | MYDRIACYL | Not specified | Not specified |
| 00622885 | ODAN-TROPICAMIDE | Not specified | Not specified |
| 00001007 | MYDRIACYL | Not specified | Not specified |
| 02148536 | MINIMS TROPICAMIDE | Not specified | Not specified |

All four authorizations are valid single-ingredient products.

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** The TxGNN knowledge graph lists the following conditions as contraindication links for tropicamide:
  - Eye conditions: open-angle glaucoma, angle-closure glaucoma, closed-angle glaucoma, ocular hypertension
  - Cardiovascular conditions: hypertension, hypertensive disorder, sudden cardiac arrest, heart conduction disease, myocardial ischemia, coronary artery disease
  - Metabolic and endocrine conditions: diabetes mellitus, diabetic ketoacidosis, hyperthyroidism, Graves disease, thyrotoxicosis
- **Drug Interactions:** 10 interaction records were found in the DDInter database. The severity level is unclassified for all of them. The interacting drugs are atropine, potassium chloride, vancomycin, simvastatin, prednisolone, famotidine, warfarin, lidocaine, fluconazole and brimonidine. Pharmacology records also show binding to muscarinic receptors M2 to M5.

Please refer to the package insert for label warnings and contraindications, as these were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score (Evidence Level L5) and class-level pharmacology. No trials or publications exist for tropicamide in any of the three predicted indications. The drug is available only as a topical eye product with minimal systemic exposure, and better-characterized antimuscarinics already cover the related uses.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Evidence that a formulation with suitable systemic or local exposure for the new indication is feasible
- Preclinical or clinical data showing tropicamide itself has activity in the predicted indication
- Review of the knowledge-graph contraindication links against the label
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

