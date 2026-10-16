---
layout: default
title: Prasugrel
parent: Model Prediction Only (L5)
nav_order: 762
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Prasugrel: predicted new indication Pulmonary hypertension (evidence level L5). Approved use: Acute coronary syndrome"
---

# Prasugrel
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

# Prasugrel: From Acute Coronary Syndrome to Pulmonary Hypertension

## One-Sentence Summary

Prasugrel is an antiplatelet drug originally used to treat acute coronary syndrome.
The TxGNN model predicts it may be effective for **pulmonary hypertension**, but the evidence is thin: **0 clinical trials** and **2 publications**, neither of which studies prasugrel in this disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute coronary syndrome |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Prasugrel is a P2Y12 antagonist that inhibits platelet aggregation. Platelet activation and microvascular thrombosis are thought to contribute to pulmonary vascular remodelling, so a theoretical link to pulmonary hypertension exists. Detailed mechanism-of-action data was not available in the data compiled for this report, so this reasoning rests on the drug's known class.

Prasugrel's benefit is established in acute coronary syndrome, where it prevents platelet-driven clot formation. The new indication is a vascular disease in which thrombosis may play a role. The link is plausible in principle, but no clinical evidence supports this use. The high TxGNN score is a computational prediction only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Cohort | Current Medical Research and Opinion | Factors associated with clopidogrel use, adherence and persistence in ACS patients after percutaneous coronary intervention. Not about pulmonary hypertension. |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Cohort | Kardiologiia | Registry analysis of how background drug therapy for comorbidities affects COVID-19 severity and outcome. Not about pulmonary hypertension. |

Both publications are only loosely related to the predicted indication. Neither tests prasugrel in pulmonary hypertension.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02502429 | JAMP PRASUGREL | — | — |

---

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text)**: liver failure, hypotensive disorder, blood coagulation disease, stroke disorder, cerebrovascular disorder, susceptibility to ischemic stroke, cerebral infarction, injury, thrombocytopenic purpura, intracranial hemorrhage, transient ischemic attack, vertebrobasilar insufficiency.
- **Drug Interactions**: 100 interactions were recorded. The 20 reviewed include:
  - **Major**: deferasirox, ibritumomab tiuxetan.
  - **Moderate**: acetylsalicylic acid (aspirin), morphine, opium, fenfluramine, dexfenfluramine, sibutramine.
  - **Minor**: several acid-suppressing drugs (proton pump inhibitors and H2 blockers, including omeprazole, pantoprazole, famotidine and ranitidine) and bupropion.

Package insert warnings were not available in the data compiled for this report. Please refer to the Health Canada package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score and a theoretical mechanism alone. There are no relevant clinical trials or publications, and the bleeding risk of a potent antiplatelet drug is a concern. By comparison, migraine (particularly in patients with patent foramen ovale) is a better-supported prasugrel prediction. It has a Phase 3 trial of PFO-directed therapy that mentions prasugrel and class-level retrospective and pilot data, and it is worth evaluating as a research question.

**To proceed, the following is needed:**
- Preclinical or clinical evidence that prasugrel or other P2Y12 inhibitors benefit pulmonary hypertension
- Detailed mechanism-of-action data
- Health Canada package insert warnings and contraindications
- A benefit-risk assessment, especially bleeding risk, in the pulmonary hypertension population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

