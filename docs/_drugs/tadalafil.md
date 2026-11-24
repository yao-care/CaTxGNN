---
layout: default
title: Tadalafil
parent: Model Prediction Only (L5)
nav_order: 877
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-24
monitor_inn: "TADALAFIL"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly", "kyphoscoliotic heart disease", "migraine with brainstem aura"]
description: "Tadalafil: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). In Canada: at least 20 DINs"
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

## Tadalafil: Ambras type hypertrichosis universalis congenita
{: .text-alpha }

## One-Sentence Summary

Tadalafil is a PDE5 inhibitor originally used for erectile dysfunction, benign prostatic hyperplasia and pulmonary hypertension, among other conditions.
The TxGNN model predicts it may be effective for **Ambras-type hypertrichosis universalis congenita**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on computational prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs on record: at least 20) |
| Number of DINs | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for tadalafil: "Penile erection during sexual stimulation is caused by increased penile blood flow resulting from the relaxation of penile arteries and corpus cavernosal smooth muscle. This response is mediated by the release of nitric oxide (NO) from nerve terminals and endothelial cells, which stimulates the synthesis of cGMP in smooth muscle cells. […] Tadalafil inhibits PDE5." ([DailyMed: Cialis (tadalafil) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bcd8f8ab-81a2-4891-83db-24a0b0e25895), label version 2026-06-03; accessed 2026-11-19.) Based on known information, tadalafil is a PDE5 inhibitor that raises cGMP levels. Its efficacy in erectile dysfunction and pulmonary hypertension is established, but no mechanism links it to this rare congenital hypertrichosis.

The very high TxGNN score is a computational prediction only. It is probably driven by network proximity to other hair-phenotype diseases rather than by biological evidence. Vasodilation and cGMP signalling could in theory affect hair follicle biology, but this is speculative. Related vasodilators such as minoxidil are associated with hypertrichosis, which suggests an adverse-effect signal rather than a therapeutic one.

## Other Predicted Indications (for Context)

The model also ranked the following conditions. None has any clinical trial support, and all remain at evidence level L5 except where noted.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Hypertrichosis | 0.9998 | L5 | Speculative link; may reflect an adverse-effect signal |
| 3 | Malformation syndrome with odontal and/or periodontal component | 0.9997 | L5 | No identifiable mechanistic link |
| 4 | Syndrome with Dandy-Walker malformation as major feature | 0.9997 | L5 | Structural brain anomaly; no expected benefit |
| 5 | Isolated genetic hair shaft abnormality | 0.9996 | L5 | No plausible pathway |
| 6 | Familial isolated trichomegaly | 0.9965 | L5 | No established mechanism |
| 7 | Kyphoscoliotic heart disease | 0.9943 | L5 | Partial rationale through secondary pulmonary hypertension, but no data |
| 8 | Migraine with brainstem aura | 0.9908 | L5 | Only a case report, and it suggests tadalafil may trigger aura |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top predicted indication, currently no related literature is available.

For context, the only publication found across the predicted indications relates to rank 8 (migraine with brainstem aura):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/) | 2006 | Case report | Cephalalgia | Tadalafil associated with typical migraine aura without headache, suggesting a possible adverse-event signal rather than a treatment benefit |

## Canada Market Information

There are 20 valid single-ingredient authorisations, with none cancelled. Dosage form and approved-indication text are not available in the records.

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02410648 | MYLAN-TADALAFIL | TADALAFIL | Marketed |
| 02410656 | MYLAN-TADALAFIL | TADALAFIL | Marketed |
| 02422085 | APO-TADALAFIL | TADALAFIL | Marketed |
| 02422107 | APO-TADALAFIL | TADALAFIL | Marketed |
| 02435934 | AURO-TADALAFIL | TADALAFIL | Marketed |
| 02440172 | TEVA-TADALAFIL | TADALAFIL | Marketed |
| 02451697 | MINT-TADALAFIL | TADALAFIL | Marketed |
| 02451832 | JAMP-TADALAFIL | TADALAFIL | Marketed |
| 02452251 | MAR-TADALAFIL | TADALAFIL | Marketed |
| 02452278 | MAR-TADALAFIL | TADALAFIL | Marketed |
| 02454742 | RIVA-TADALAFIL | TADALAFIL | Marketed |
| 02455358 | TADALAFIL | TADALAFIL | Marketed |
| 02455366 | TADALAFIL | TADALAFIL | Marketed |
| 02457016 | TADALAFIL | TADALAFIL | Marketed |
| 02457024 | TADALAFIL | TADALAFIL | Marketed |
| 02457032 | TADALAFIL | TADALAFIL | Marketed |
| 02481405 | AG-TADALAFIL | TADALAFIL | Marketed |
| 02512289 | PRZ-TADALAFIL | TADALAFIL | Marketed |
| 02520966 | NRA-TADALAFIL | TADALAFIL | Marketed |
| 02536684 | TADALAFIL | TADALAFIL | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

The data contain only part of the DINs for this ingredient; the list may be incomplete.

<!-- licenses:end -->

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

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cialis (tadalafil) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bcd8f8ab-81a2-4891-83db-24a0b0e25895) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

