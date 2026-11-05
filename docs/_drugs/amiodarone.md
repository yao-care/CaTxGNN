---
layout: default
title: Amiodarone
parent: Model Prediction Only (L5)
nav_order: 52
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-05
monitor_inn: "Amiodarone"
predicted_indications: ["catecholaminergic polymorphic ventricular tachycardia", "incessant infant ventricular tachycardia", "obsolete bundle branch block", "rheumatoid arthritis", "brachydactyly-syndactyly syndrome", "heparin cofactor 2 deficiency", "trichotillomania", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "gout"]
description: "Amiodarone: predicted new indication Catecholaminergic polymorphic ventricular tachycardia (evidence level L5). Approved use: Not recorded in the local data"
---

# Amiodarone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Amiodarone: Catecholaminergic polymorphic ventricular tachycardia
{: .text-alpha }

## One-Sentence Summary

Amiodarone is a multichannel-blocking antiarrhythmic drug that is marketed in Canada in oral and injectable forms.
The TxGNN model predicts it may be effective for **catecholaminergic polymorphic ventricular tachycardia**, but **no clinical trials** and **9 publications** were found, and none of them tests amiodarone in this disease, so the evidence level is **L5** (model prediction only).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Catecholaminergic polymorphic ventricular tachycardia |
| TxGNN Prediction Score | 0.9978 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 12 of 12) |
| Number of DINs | 12 (marketed: 12) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, amiodarone blocks potassium, sodium and calcium channels and also has beta-adrenergic antagonism. These effects are plausibly relevant to ventricular arrhythmias triggered by adrenergic stimulation.

However, the mechanistic fit is weak. The core defect in catecholaminergic polymorphic ventricular tachycardia is calcium leak linked to RYR2 or CASQ2 gene variants. The therapies supported by guidelines are beta-blockers, flecainide and cardiac sympathetic denervation. Amiodarone is generally considered ineffective or inferior in this condition. The high model score should therefore be read as a hypothesis, not as evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26513538](https://pubmed.ncbi.nlm.nih.gov/26513538/) | 2015 | Review | Expert Opin Pharmacother | Overview of drug treatment of ventricular arrhythmias; not specific to this disease |
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Systematic review | Life (Basel) | Clinical features, genetics and arrhythmic outcomes of patients from China with this disease |
| [39076628](https://pubmed.ncbi.nlm.nih.gov/39076628/) | 2022 | Cohort | Rev Cardiovasc Med | Clinical features, genetics, healthcare use and costs in a Chinese city |
| [22553997](https://pubmed.ncbi.nlm.nih.gov/22553997/) | 2012 | Case report | Pacing Clin Electrophysiol | Flecainide suppressed defibrillator-induced storming in a boy with a CASQ2 variant |
| [39735866](https://pubmed.ncbi.nlm.nih.gov/39735866/) | 2024 | Case report | Front Cardiovasc Med | Right cardiac sympathetic denervation resolved arrhythmia after left denervation in a teenager |
| [30116135](https://pubmed.ncbi.nlm.nih.gov/30116135/) | 2018 | Case report | Turk Pediatri Ars | Sudden cardiac arrest in a 2-year-old with this disease |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Case report | Medicine | Six-year delayed diagnosis in a child with an RYR2 variant |
| [37852665](https://pubmed.ncbi.nlm.nih.gov/37852665/) | 2023 | Case report | BMJ Case Rep | Young child with out-of-hospital cardiac arrest and diagnostic difficulty |
| [22218697](https://pubmed.ncbi.nlm.nih.gov/22218697/) | 2012 | Case report | Anesth Analg | Neonate with long QT syndrome and refractory arrhythmia treated with several drugs including amiodarone; not this disease |

None of these publications shows a benefit of amiodarone in catecholaminergic polymorphic ventricular tachycardia.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02364336 | AMIODARONE | Not available | Not available |
| 02243836 | SANDOZ AMIODARONE | Not available | Not available |
| 02247217 | RIVA-AMIODARONE | Not available | Not available |
| 02292173 | PMS-AMIODARONE | Not available | Not available |
| 02385465 | AMIODARONE | Not available | Not available |

All 12 single-ingredient licences are valid, so the list above shows only 5 of them.

## Cytotoxicity

Not applicable. Amiodarone is not an antineoplastic drug. (This section is omitted.)

## Safety Considerations

- **Drug Interactions**: Interaction screening returned 100 entries. Major-level interactions include clarithromycin, cisapride, dolasetron, eliglustat, clotrimazole, hydrocortisone, dexamethasone, amphotericin B (several formulations) and agalsidase beta. Moderate-level interactions include famotidine, cimetidine, aprepitant, bisacodyl, budesonide and castor oil. Many of these relate to QT prolongation or electrolyte disturbance.
- **Conditions of concern**: Conditions linked to amiodarone as contraindications or cautions include long QT syndrome, torsades de pointes, sick sinus syndrome, atrioventricular block, thyroid disease (hypothyroidism and hyperthyroidism), liver disease, interstitial lung disease, hypersensitivity pneumonitis, optic neuritis, peripheral neuropathy and potassium deficiency. These come from relation data, not from label text.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No study tests amiodarone in catecholaminergic polymorphic ventricular tachycardia, so support is a model prediction only (L5). The mechanism is not a good fit, and the established treatments in this disease are different drugs and procedures.

**To proceed, the following is needed:**
- Direct clinical or preclinical evidence of amiodarone in this disease, compared against beta-blockers and flecainide
- Mechanism of action data
- Package insert warnings and contraindications from Health Canada
- A safety plan covering QT prolongation, thyroid, lung and liver toxicity, and drug interactions

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

