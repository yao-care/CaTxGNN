---
layout: default
title: Sotalol
parent: Model Prediction Only (L5)
nav_order: 865
evidence_level: L5
indication_count: 7
---

# Sotalol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Sotalol: From Atrial Fibrillation to Sick Sinus Syndrome 2 (Autosomal Dominant)

## One-Sentence Summary

Sotalol is an antiarrhythmic drug, originally used to maintain normal heart rhythm in atrial fibrillation.
The TxGNN model predicts it may be effective for **sick sinus syndrome 2, autosomal dominant**, with a very high score, but **no clinical trials and no publications** currently support this prediction.
Mechanistically, the prediction appears implausible and potentially harmful, so this is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation (from the knowledge graph; no approved indication text is available in the Canadian licence records) |
| Predicted New Indication | Sick sinus syndrome 2, autosomal dominant |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, sotalol combines beta-adrenergic blockade with class III antiarrhythmic action (potassium-channel inhibition that prolongs repolarization). Its efficacy in atrial fibrillation is established.

The predicted condition, sick sinus syndrome 2, is linked to HCN4 variants that cause sinus node dysfunction. Sotalol's beta-blockade and prolonged repolarization are expected to slow the heart rate and **worsen** bradycardia and sinus node dysfunction. The knowledge graph itself lists sick sinus syndrome (including the familial form) as a contraindication for sotalol.

The high score is therefore most likely an artifact of the shared cardiac-rhythm context in the graph rather than a true therapeutic signal.

Other predictions reviewed also lack support:
- **Wildervanck syndrome, sarcoglycanopathy, and macrocephaly with dysmorphic facies and psychomotor retardation**: no plausible mechanistic link and no studies.
- **Stroke disorder** (score 99.44%): the only indirect connection is through atrial fibrillation as a stroke risk factor. One Phase 3 trial (NCT00007605) tested rhythm maintenance, not stroke prevention.
- **Manic bipolar affective disorder**: the two papers found address drug-interaction safety (QT-related risk with antipsychotics), not efficacy.
- **Obsolete susceptibility to ischemic stroke**: an obsolete ontology term, not a valid indication.

## Clinical Trial Evidence

Currently no related clinical trials are registered for the top predicted indication (sick sinus syndrome 2, autosomal dominant).

For reference, one trial was found for a lower-ranked prediction (stroke disorder). It reflects the original atrial fibrillation indication, not a new use:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00007605](https://clinicaltrials.gov/study/NCT00007605) | Phase 3 | Completed | 706 | CSP #399: amiodarone and sotalol compared for maintaining sinus rhythm in atrial fibrillation. The endpoint was rhythm stability, not stroke prevention. |

## Literature Evidence

Currently no related literature is available for the top predicted indication.

For reference, literature retrieved for the lower-ranked stroke prediction (all concerning atrial fibrillation management, not sick sinus syndrome):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37485722](https://pubmed.ncbi.nlm.nih.gov/37485722/) | 2023 | Cohort | Circ Arrhythm Electrophysiol | Dronedarone vs sotalol in antiarrhythmic-drug-naive veterans with atrial fibrillation; sotalol requires initial QT and proarrhythmia monitoring |
| [38782070](https://pubmed.ncbi.nlm.nih.gov/38782070/) | 2024 | Cohort | Int J Cardiol | Antiarrhythmic drugs and cardiovascular outcomes in patients with atrial fibrillation and coronary artery disease |
| [37777295](https://pubmed.ncbi.nlm.nih.gov/37777295/) | 2023 | Guideline review | Am J Cardiol | Guideline recommendations on antiarrhythmic drug selection in atrial fibrillation |
| [38011245](https://pubmed.ncbi.nlm.nih.gov/38011245/) | 2023 | Review | Circulation | Management of atrial fibrillation in hypertrophic cardiomyopathy |
| [25430048](https://pubmed.ncbi.nlm.nih.gov/25430048/) | 2014 | Review | BMJ Clin Evid | Acute-onset atrial fibrillation; increased risk of stroke and heart failure |
| [29954667](https://pubmed.ncbi.nlm.nih.gov/29954667/) | 2019 | Observational | Int J Cardiol | Efficacy and adverse effects of sotalol in adults with congenital heart disease |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02210428 | APO-SOTALOL | Not listed | Not listed |
| 02167794 | APO-SOTALOL | Not listed | Not listed |
| 02238326 | PMS-SOTALOL - 80 MG | Not listed | Not listed |
| 02238327 | PMS-SOTALOL - 160 MG | Not listed | Not listed |

All four authorizations are valid single-ingredient products.

## Safety Considerations

- **Disease-level contraindications (knowledge graph, not label text)**: long QT syndrome (including familial), torsades de pointes, asthma (intrinsic and allergic), bronchial disease, potassium deficiency, diabetes mellitus, diabetic ketoacidosis, hypotension, impaired renal function, atrioventricular block, sick sinus syndrome (including familial), and anaphylaxis.
- **Drug interactions**: 100 interactions were identified. Examples of **major** interactions include epinephrine, clarithromycin, picosulfuric acid, and polyethylene glycol (3350 with electrolytes). Moderate interactions include famotidine, cimetidine, morphine, bupropion, loperamide, atropine, and canagliflozin and dapagliflozin.
- **QT-related risk**: published work shows beta-blockade can augment torsadogenic risk when combined with QT-prolonging agents such as risperidone.

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there are no trials or publications for sick sinus syndrome 2. Sotalol's pharmacology would be expected to worsen sinus node dysfunction, and the knowledge graph lists sick sinus syndrome as a contraindication. None of the other predicted indications show a credible therapeutic signal either.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank) to support mechanistic analysis
- Reconciliation of the prediction with the sick sinus syndrome contraindication, and expert review of whether it is a graph artifact
- Exclusion or merging of the obsolete stroke susceptibility entry with the stroke disorder entry
- Dosage form and approved-indication details for the four Canadian authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

