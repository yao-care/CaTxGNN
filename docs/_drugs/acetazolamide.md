---
layout: default
title: Acetazolamide
parent: Model Prediction Only (L5)
nav_order: 18
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Acetazolamide: predicted new indication Exercise-induced malignant hyperthermia (evidence level L5). Approved use: Absence epilepsy, congestive heart failure…"
monitor_inn: "ACETAZOLAMIDE"
predicted_indications: ["exercise-induced malignant hyperthermia", "hypertrophic cardiomyopathy", "congenital myopathy with excess of thin filaments", "hypertrophic cardiomyopathy due to intensive athletic training", "distal myopathy, Tateyama type", "cirrhotic cardiomyopathy", "cardiomyopathy", "intestinal obstruction", "glycogen storage disease due to acid maltase deficiency, late-onset", "myopathic intestinal pseudoobstruction"]
---

# Acetazolamide
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

# Acetazolamide: From Glaucoma and Heart Failure to Hypertrophic Cardiomyopathy

## One-Sentence Summary

Acetazolamide is a carbonic anhydrase inhibitor originally used for glaucoma, absence epilepsy, congestive heart failure and altitude sickness.
The TxGNN model predicts it may be effective for **exercise-induced malignant hyperthermia** (rank 1) and **hypertrophic cardiomyopathy** (rank 2).
Currently there are **0 clinical trials** and only **3 indirect publications** for the second candidate, and none for the top candidate, so the signal is mostly model-based.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Absence epilepsy, congestive heart failure, open-angle and angle-closure glaucoma, altitude sickness (from the knowledge graph; the Canadian licence records contain no indication text) |
| Predicted New Indication | Exercise-induced malignant hyperthermia (top-ranked); hypertrophic cardiomyopathy is the highest-ranked candidate with any literature |
| TxGNN Prediction Score | 99.95% (exercise-induced malignant hyperthermia); 99.93% (hypertrophic cardiomyopathy) |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Acetazolamide is a carbonic anhydrase inhibitor. Its efficacy in glaucoma, heart failure-related fluid retention and altitude sickness is established, and these actions involve fluid and acid-base handling.

For the top prediction, exercise-induced malignant hyperthermia, no clinical or literature evidence was found. A link through altered acid-base balance or muscle ion handling is plausible but speculative and unsupported by the data compiled for this report.

For hypertrophic cardiomyopathy, the link is indirect. Acetazolamide is used as a diuretic adjunct in heart failure, and heart failure often accompanies hypertrophic cardiomyopathy. A case report describes correcting hypochloremia with acetazolamide in an advanced heart failure patient who also had hypertrophic cardiomyopathy. None of the retrieved papers tests acetazolamide for hypertrophic cardiomyopathy itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Literature for the highest-ranked candidate with evidence (hypertrophic cardiomyopathy):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30279861](https://pubmed.ncbi.nlm.nih.gov/30279861/) | 2018 | Case report | Journal of Cardiology Cases | Acetazolamide corrected hypochloremia in an 87-year-old with advanced heart failure and hypertrophic cardiomyopathy; urinary electrolyte monitoring emphasized |
| [38806171](https://pubmed.ncbi.nlm.nih.gov/38806171/) | 2025 | Review | ESC Heart Failure | General heart failure update; not specific to acetazolamide or hypertrophic cardiomyopathy |
| [37169875](https://pubmed.ncbi.nlm.nih.gov/37169875/) | 2023 | Review | Eur Heart J Cardiovasc Pharmacother | Review of new cardiovascular drugs in 2022, including mavacamten for obstructive hypertrophic cardiomyopathy; acetazolamide not the focus |

Related evidence for the broader "cardiomyopathy" prediction (rank 7) is mostly indirect. It includes an animal study of acetazolamide in ischemia-reperfused rabbit hearts (PMID 22426904, 2012), and a case report of non-cardiogenic pulmonary edema after intravenous acetazolamide in a patient with dilated cardiomyopathy (PMID 29123889, 2017), which is a safety signal.

No literature was found for the other top-ranked predictions, except intestinal obstruction (rank 8), where the papers describe acetazolamide-induced adynamic ileus (PMID 19653068), a safety concern rather than support for efficacy.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02537893 | Acetazolamide for Injection USP | Not specified | Not specified |
| 00545015 | Acetazolamide | Not specified | Not specified |
| 02358328 | Acetazolamide for Injection, USP | Not specified | Not specified |

---

## Safety Considerations

- **Disease-level contraindication signals (from the knowledge graph, not label text)**: liver failure and liver disease, kidney disease, renal tubular acidosis, adrenal insufficiency (including Addison disease and congenital adrenal hyperplasia), gout, diabetes (type 1 and type 2) and diabetic ketoacidosis, respiratory failure, hematologic disease, gallbladder disease, and pyoureter.
- **Drug Interactions**: 100 interactions were identified. Major ones include acetylsalicylic acid and cisapride. Moderate ones include antidiabetic agents (acarbose, acetohexamide, alogliptin, canagliflozin, chlorpropamide, dapagliflozin, and others), corticosteroids (beclomethasone, betamethasone, dexamethasone), amphotericin B formulations, and laxatives (bisacodyl, castor oil). Doxycycline is a minor interaction.
- **Candidate-specific concerns**: reports of ileus raise concern for intestinal obstruction and pseudo-obstruction. In cirrhosis, acetazolamide can precipitate hyperammonemia and encephalopathy, which argues against use in cirrhotic cardiomyopathy.

Please refer to the package insert for the official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predictions have only model-level support (L5), except cardiomyopathy, which reaches L4 on indirect preclinical data. No clinical trials exist, and the available papers are reviews and case reports not directed at the predicted diseases. Two predictions (intestinal obstruction and myopathic intestinal pseudo-obstruction) are contradicted by safety signals, and the contraindication profile is substantial.

**To proceed, the following is needed:**
- Mechanism of action data and a clear mechanistic rationale for the top candidates
- Official Health Canada package insert warnings and contraindications, along with the missing dosage forms and approved indications for the three DINs
- A targeted literature review for hypertrophic cardiomyopathy and exercise-induced malignant hyperthermia, plus preclinical studies
- Evaluation of the safety profile in the target populations, especially those with liver, kidney or metabolic comorbidities and those on interacting drugs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

