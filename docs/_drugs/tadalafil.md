---
layout: default
title: Tadalafil
parent: Model Prediction Only (L5)
nav_order: 877
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-13
description: "Tadalafil: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Erectile dysfunction, benign prostatic hyperplasia…"
monitor_inn: "TADALAFIL"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly", "kyphoscoliotic heart disease", "migraine with brainstem aura"]
---

# Tadalafil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Tadalafil: From Erectile Dysfunction and Pulmonary Hypertension to Ambras-Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Tadalafil is a PDE5 inhibitor originally used for erectile dysfunction, benign prostatic hyperplasia and pulmonary hypertension, among other conditions.
The TxGNN model predicts it may be effective for **Ambras-type hypertrichosis universalis congenita**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on computational prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Erectile dysfunction, benign prostatic hyperplasia, pulmonary hypertension, psychologic dyspareunia, premature ejaculation (the Health Canada licence records contain no indication text, so these come from the knowledge-graph indication list) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tadalafil is a PDE5 inhibitor that raises cGMP levels. Its efficacy in erectile dysfunction and pulmonary hypertension is established, but no mechanism links it to this rare congenital hypertrichosis.

The very high TxGNN score is a computational prediction only. It is probably driven by network proximity to other hair-phenotype diseases rather than by biological evidence. Vasodilation and cGMP signalling could in theory affect hair follicle biology, but this is speculative. Related vasodilators such as minoxidil are associated with hypertrichosis, which suggests an adverse-effect signal rather than a therapeutic one.

## Other Predicted Indications (for Context)

The model also ranked the following conditions. None has any clinical trial support, and all remain at evidence level L5 except where noted.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Hypertrichosis | 99.98% | L5 | Speculative link; may reflect an adverse-effect signal |
| 3 | Malformation syndrome with odontal and/or periodontal component | 99.97% | L5 | No identifiable mechanistic link |
| 4 | Syndrome with Dandy-Walker malformation as major feature | 99.97% | L5 | Structural brain anomaly; no expected benefit |
| 5 | Isolated genetic hair shaft abnormality | 99.96% | L5 | No plausible pathway |
| 6 | Familial isolated trichomegaly | 99.65% | L5 | No established mechanism |
| 7 | Kyphoscoliotic heart disease | 99.43% | L5 | Partial rationale through secondary pulmonary hypertension, but no data |
| 8 | Migraine with brainstem aura | 99.08% | L4 | Only a case report, and it suggests tadalafil may trigger aura |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top predicted indication, currently no related literature is available.

For context, the only publication found across the predicted indications relates to rank 8 (migraine with brainstem aura):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/) | 2006 | Case report | Cephalalgia | Tadalafil associated with typical migraine aura without headache, suggesting a possible adverse-event signal rather than a treatment benefit |

## Canada Market Information

There are 20 valid single-ingredient authorisations, with none cancelled. Dosage form and approved-indication text are not available in the records. The first five are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02410656 | MYLAN-TADALAFIL | – | – |
| 02457016 | TADALAFIL | – | – |
| 02512289 | PRZ-TADALAFIL | – | – |
| 02481405 | AG-TADALAFIL | – | – |
| 02455366 | TADALAFIL | – | – |

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these come from knowledge-graph relationships, not from package insert text):
  - Cardiovascular: acute coronary syndrome, myocardial infarction, coronary thrombosis, stroke and cerebrovascular disorders, cerebral infarction, hypotensive disorder, aortic stenosis and aortic valve disease, hypertrophic cardiomyopathy
  - Haematological: sickle cell anaemia, hemoglobinopathy, blood coagulation disease, plasma cell myeloma, leukaemia
  - Penile conditions: priapism, Peyronie disease, penile fibromatosis, balanitis xerotica obliterans
  - Other: liver failure, epilepsy, hearing loss disorder, functional visual loss
- **Drug Interactions**: The interaction query returned 100 records. Those listed include:
  - Moderate: aprepitant, dexamethasone, clarithromycin, cimetidine, miconazole, clotrimazole, lorcaserin, sapropterin, troglitazone, and the SGLT2 inhibitors canagliflozin, dapagliflozin, empagliflozin and ertugliflozin
  - Minor: papaverine
  - Unknown severity: pantoprazole, glimepiride, doxycycline, morphine, metformin, omeprazole
- Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials, no literature, and no plausible mechanism. Related evidence for hypertrichosis points toward an adverse-effect signal rather than a therapeutic one. None of the other top predictions has trial support either, and the only published evidence (migraine with brainstem aura) suggests possible harm.

**To proceed, the following is needed:**
- Detailed mechanism of action data, and a mechanistic hypothesis linking PDE5 inhibition to hair follicle biology
- Preclinical or case-level evidence for the predicted indication
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Assessment of whether the hypertrichosis signal reflects a therapeutic effect or an adverse effect
- If the project looks for a better-supported lead, consider kyphoscoliotic heart disease, which has a partial biological rationale through pulmonary hypertension, though it too has no supporting data yet
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

