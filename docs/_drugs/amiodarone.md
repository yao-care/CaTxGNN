---
layout: default
title: Amiodarone
parent: Moderate Evidence (L3-L4)
nav_order: 52
evidence_level: L4
indication_count: 9
last_modified_at: 2026-11-03
monitor_inn: "Amiodarone"
predicted_indications: ["catecholaminergic polymorphic ventricular tachycardia", "incessant infant ventricular tachycardia", "obsolete bundle branch block", "rheumatoid arthritis", "brachydactyly-syndactyly syndrome", "heparin cofactor 2 deficiency", "trichotillomania", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "gout"]
description: "Amiodarone: predicted new indication Catecholaminergic polymorphic ventricular tachycardia (evidence level L4). Approved use: Not recorded in the local data"
---

# Amiodarone
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **9** 
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

Amiodarone is an antiarrhythmic drug that blocks several cardiac ion channels and also has beta-adrenergic antagonism.
The TxGNN model predicts it may be useful for **catecholaminergic polymorphic ventricular tachycardia (CPVT)**.
No clinical trials are registered for this use, and the **9 publications** retrieved describe the disease but show no benefit from amiodarone, so the evidence is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Catecholaminergic polymorphic ventricular tachycardia |
| TxGNN Prediction Score | 0.9978 |
| Evidence Level | L4 |
| Canada Market Status | Marketed (valid licenses: 12 of 12) |
| Number of DINs | 12 (valid: 12) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Amiodarone blocks potassium, sodium and calcium channels and has beta-adrenergic antagonism. These actions are plausibly relevant to ventricular arrhythmias triggered by adrenergic stress, which is the defining feature of CPVT. CPVT is a rare inherited channelopathy.

The mechanistic fit is only partial. The core defect in CPVT is calcium leak related to RYR2 or CASQ2 mutations. The therapies supported by guidelines are beta-blockers, flecainide and sympathetic denervation. Amiodarone is generally considered ineffective or inferior in CPVT. The high model score therefore looks more like a general association with ventricular arrhythmia drugs than evidence of a specific benefit.

Detailed mechanism-of-action data were not available in the data compiled for this report. The reasoning above rests on the drug's known pharmacology.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Systematic review | Life (Basel) | Clinical features, genetics and arrhythmic outcomes of CPVT patients from China; describes the disease, with no amiodarone benefit shown |
| [39076628](https://pubmed.ncbi.nlm.nih.gov/39076628/) | 2022 | Retrospective cohort | Rev Cardiovasc Med | Clinical characteristics, genetic basis, healthcare use and costs of CPVT patients in a Chinese city |
| [26513538](https://pubmed.ncbi.nlm.nih.gov/26513538/) | 2015 | Review | Expert Opin Pharmacother | General review of drug treatment for ventricular arrhythmias; not specific to CPVT |
| [22553997](https://pubmed.ncbi.nlm.nih.gov/22553997/) | 2012 | Case report | Pacing Clin Electrophysiol | Flecainide suppressed defibrillator-induced storming in a boy with CPVT |
| [39735866](https://pubmed.ncbi.nlm.nih.gov/39735866/) | 2024 | Case report | Front Cardiovasc Med | CPVT in a teenager resolved after right cardiac sympathetic denervation following left-sided denervation |
| [30116135](https://pubmed.ncbi.nlm.nih.gov/30116135/) | 2018 | Case report | Turk Pediatri Arsivi | CPVT presenting as sudden cardiac arrest in a 2-year-old |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Case report | Medicine | Six-year delayed diagnosis of CPVT with an RYR2 variant in a child |
| [37852665](https://pubmed.ncbi.nlm.nih.gov/37852665/) | 2023 | Case report | BMJ Case Rep | Young child survived out-of-hospital cardiac arrest with recurrent ventricular arrhythmias; the case discusses departing from standard resuscitation guidelines |

None of these publications shows that amiodarone benefits CPVT patients. The treatments they report are flecainide and sympathetic denervation.

## Canada Market Information

Amiodarone is marketed in Canada, with single-ingredient products holding valid licences. The licence records do not carry approved-indication text, so the approved indication is not recorded in the local data. Dosage forms are also not recorded.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02364336 | AMIODARONE | Not available | Not available |
| 02243836 | SANDOZ AMIODARONE | Not available | Not available |
| 02247217 | RIVA-AMIODARONE | Not available | Not available |
| 02292173 | PMS-AMIODARONE | Not available | Not available |
| 02385465 | AMIODARONE | Not available | Not available |

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 records. Major-level interactions include:
  - Corticosteroids: hydrocortisone and dexamethasone.
  - Amphotericin B products, including the cholesteryl sulfate, lipid complex and liposomal forms.
  - Cisapride and dolasetron.
  - Clarithromycin and clotrimazole.
  - Eliglustat and agalsidase beta.
- Moderate-level examples include famotidine, cimetidine, aprepitant, budesonide and bisacodyl.
- **Pediatric and monitoring note**: CPVT often presents in children and young people. Amiodarone use in these groups needs close monitoring for thyroid, hemodynamic and proarrhythmic toxicity.

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The model score is very high (0.9978), but no clinical trials exist and the retrieved literature shows no benefit from amiodarone in CPVT. Established options (beta-blockers, flecainide, sympathetic denervation) are mechanistically better matched and have guideline support.

**To proceed, the following is needed:**
- Studies that directly evaluate amiodarone in CPVT, such as comparative cohorts or registry data.
- Detailed mechanism-of-action data.
- Package insert warnings and contraindications, including safety in children and young adults.

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

