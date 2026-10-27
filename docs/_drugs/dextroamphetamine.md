---
layout: default
title: Dextroamphetamine
parent: Model Prediction Only (L5)
nav_order: 273
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
description: "Dextroamphetamine: predicted new indication Faciodigitogenital syndrome (evidence level L5). Approved use: Attention deficit hyperactivity disorder"
monitor_inn: "Dextroamphetamine"
predicted_indications: ["faciodigitogenital syndrome", "specific developmental disorder", "chondromyxoid fibroma", "multiple system atrophy", "variably protease-sensitive prionopathy", "postural orthostatic tachycardia syndrome", "trichotillomania"]
---

# Dextroamphetamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Dextroamphetamine: From Attention Deficit Hyperactivity Disorder to Faciodigitogenital Syndrome
{: .text-alpha }

## One-Sentence Summary

Dextroamphetamine is a central nervous system stimulant, originally used to treat attention deficit hyperactivity disorder (ADHD) and narcolepsy.
The TxGNN model predicts it may be effective for **faciodigitogenital syndrome** (Aarskog-Scott syndrome), but **no clinical trials and no publications** currently support this specific prediction.
The prediction is a knowledge-graph inference only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Attention deficit hyperactivity disorder; narcolepsy (from the knowledge graph, as the Canadian licence records contain no indication text) |
| Predicted New Indication | Faciodigitogenital syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. In general, dextroamphetamine is a sympathomimetic stimulant that increases catecholamine (dopamine and noradrenaline) release and reduces their reuptake, acting through TAAR1, VMAT2 and the dopamine transporter. Its benefit in ADHD is well established.

Faciodigitogenital syndrome (Aarskog-Scott syndrome, linked to the FGD1 gene) can include ADHD-like behavioural features. A stimulant could therefore plausibly ease those symptoms. This is an inference about symptom management, not a disease-modifying mechanism, and no study was found that tests it.

Other predictions for this drug were also reviewed. Most are weakly supported or unsupported. Examples are chondromyxoid fibroma and variably protease-sensitive prionopathy, for which no mechanistic link is evident. The highest-scoring prediction with some indirect literature is **specific developmental disorder**, which relies on the overlap with ADHD. The trichotillomania evidence points to harm rather than benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found for faciodigitogenital syndrome. The closest indirect evidence comes from the second-ranked prediction, specific developmental disorder, and is mostly about ADHD rather than learning or developmental disorders:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38391788](https://pubmed.ncbi.nlm.nih.gov/38391788/) | 2024 | Review | Expert Rev Neurother | Review of once-daily extended-release amphetamine options for ADHD |
| [42819375](https://pubmed.ncbi.nlm.nih.gov/42819375/) | 2026 | Cohort (pharmacovigilance) | Front Pediatr | Age-stratified FAERS safety signal analysis of ADHD medications in children |
| [18309764](https://pubmed.ncbi.nlm.nih.gov/18309764/) | 2007 | Review | Nutr Health | Stimulants (including dextroamphetamine) show about a 75% response in ADHD, with side effects; nutrition alternatives discussed |
| [11563573](https://pubmed.ncbi.nlm.nih.gov/11563573/) | 2001 | Review | Am Fam Physician | Evaluation and treatment of ADHD in school-age children |
| [8784874](https://pubmed.ncbi.nlm.nih.gov/8784874/) | 1996 | Review | Nurse Pract | Diagnosis of ADHD based on impulsivity, hyperactivity and inattention |
| [8719499](https://pubmed.ncbi.nlm.nih.gov/8719499/) | 1996 | Cohort | Clin EEG | QEEG distinguished children with attention deficit or learning disorders, and separated dextroamphetamine responders from methylphenidate responders |
| [31984712](https://pubmed.ncbi.nlm.nih.gov/31984712/) | 2020 | Case report | Arch Argent Pediatr | Two children developed new-onset trichotillomania during stimulant treatment (a safety signal for the trichotillomania prediction) |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02448327 | TEVA-DEXTROAMPHETAMINE SR | Not recorded | Not recorded |
| 02448319 | TEVA-DEXTROAMPHETAMINE SR | Not recorded | Not recorded |
| 01924516 | DEXEDRINE | Not recorded | Not recorded |
| 01924567 | DEXEDRINE SPANSULE | Not recorded | Not recorded |
| 01924559 | DEXEDRINE SPANSULE | Not recorded | Not recorded |

A sixth licence, DIN 02443236 (DEXTROAMPHETAMINE), is also valid. All six are single-ingredient products and none are cancelled.

## Safety Considerations

- **Contraindication-related conditions (knowledge graph, not label text):** The knowledge graph links dextroamphetamine to contraindications in several groups of conditions:
  - Cardiovascular and cerebrovascular: hypertension, coronary artery disease, myocardial infarction, stroke, arteriosclerosis, heart conduction disease, sudden cardiac arrest.
  - Psychiatric: bipolar disorder, psychotic disorders, schizoaffective disorder, substance abuse or dependence, anorexia nervosa.
  - Other: epilepsy, glaucoma, hyperthyroidism, Graves disease, thyrotoxicosis, hemoglobinopathy.
- **Drug Interactions:** 62 interactions were recorded. Those listed below are the **Major** ones among the 20 retrieved in detail:
  - Bupropion
  - Fenfluramine
  - Dexfenfluramine
  - Sibutramine

  Moderate interactions include epinephrine, ephedrine, isometheptene, and several antacids and alkalinising agents (for example magnesium hydroxide, aluminium hydroxide, calcium carbonate and potassium citrate).
- **Prediction-specific concerns:**
  - Amphetamines raise heart rate and blood pressure. This is a concern for postural orthostatic tachycardia syndrome and for multiple system atrophy.
  - Stimulant-associated trichotillomania has been reported in children.
  - A 2026 pharmacovigilance analysis of paediatric ADHD medications is relevant for any use in children.

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the Health Canada package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for faciodigitogenital syndrome has a high model score but no trials or literature (evidence level L5). Its only support is an inferred symptom-level link through ADHD-like features. The drug also carries notable cardiovascular, psychiatric and abuse-related risks.

**To proceed, the following is needed:**
- A literature review of ADHD-like symptoms and stimulant response in Aarskog-Scott syndrome, including case series
- Mechanism of action data for the drug (for example from DrugBank)
- Health Canada package insert warnings and contraindications, plus approved indication text and dosage forms for each DIN
- A safety plan covering cardiovascular screening, psychiatric history and misuse risk, particularly in children
- Review of the specific developmental disorder prediction (evidence level L4, mostly ADHD-based and indirect) as a possible alternative research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

