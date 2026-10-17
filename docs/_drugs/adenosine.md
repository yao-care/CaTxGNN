---
layout: default
title: Adenosine
parent: Model Prediction Only (L5)
nav_order: 27
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Adenosine: predicted new indication Obsolete bundle branch block (evidence level L5). Approved use: Ventricular tachycardia"
monitor_inn: "ADENOSINE"
predicted_indications: ["obsolete bundle branch block"]
---

# Adenosine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Adenosine: From Ventricular Tachycardia to Obsolete Bundle Branch Block

## One-Sentence Summary

Adenosine is an injectable antiarrhythmic originally used for ventricular tachycardia.
The TxGNN model predicts it may be effective for **obsolete bundle branch block** (a deprecated disease term) with a very high score, but there are **0 clinical trials** and **0 publications** supporting this prediction.
A second, more credible candidate, **catecholaminergic polymorphic ventricular tachycardia (CPVT)**, has **0 clinical trials** and only **1 case report** (using ATP, not adenosine) as directly relevant evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ventricular tachycardia (from the knowledge graph; the Canadian licence records contain no indication text) |
| Predicted New Indication | Obsolete bundle branch block |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, adenosine slows conduction through the atrioventricular (AV) node and is used in the diagnosis and treatment of supraventricular and wide-complex tachycardias.

For the top-ranked prediction, **obsolete bundle branch block**, no direct therapeutic rationale is evident. The term is flagged as obsolete, so the high score may be an artifact of the ontology rather than a real signal. Because adenosine suppresses conduction, it could even worsen conduction disturbances. This prediction should not be treated as a credible repurposing lead.

The second-ranked prediction, **CPVT** (score 99.42%), is mechanistically more plausible. CPVT is driven by calcium leak from the sarcoplasmic reticulum and triggered, delayed-afterdepolarization-mediated arrhythmia that depends on adrenergic stimulation. Adenosine and ATP can oppose beta-adrenergic, cAMP-dependent triggered activity, which offers a possible link. However, ATP is not identical to adenosine, and a single case report cannot establish efficacy or safety.

---

## Clinical Trial Evidence

Currently no related clinical trials registered, for either the top prediction or CPVT.

---

## Literature Evidence

**Obsolete bundle branch block:** Currently no related literature available.

**Catecholaminergic polymorphic ventricular tachycardia (second-ranked prediction):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18313614](https://pubmed.ncbi.nlm.nih.gov/18313614/) | 2008 | Case report | Heart Rhythm | ATP terminated bidirectional ventricular tachycardia in a patient with CPVT |
| [21699856](https://pubmed.ncbi.nlm.nih.gov/21699856/) | 2011 | Case report/Cohort | Heart Rhythm | Abnormal repolarization after pacing in CPVT linked to a cardiac ryanodine receptor mutation |
| [40165484](https://pubmed.ncbi.nlm.nih.gov/40165484/) | 2025 | Review | Europace | Consensus statement on pharmacological provocation testing in cardiac electrophysiology |
| [18368865](https://pubmed.ncbi.nlm.nih.gov/18368865/) | 2007 | Review | J Assoc Physicians India | Recognition and management of ventricular tachycardia in structurally normal hearts |
| [39148245](https://pubmed.ncbi.nlm.nih.gov/39148245/) | 2024 | Review | Paediatr Anaesth | Pediatric arrhythmias for anesthesiologists |
| [15324613](https://pubmed.ncbi.nlm.nih.gov/15324613/) | 2004 | Review | Curr Treat Options Cardiovasc Med | Treatment alternatives for syncope |
| [41691612](https://pubmed.ncbi.nlm.nih.gov/41691612/) | 2026 | Preclinical (in vitro) | J Physiol | Cardiac-neural microtissues suggest CPVT also involves sympathetic neurons |
| [38776406](https://pubmed.ncbi.nlm.nih.gov/38776406/) | 2024 | Preclinical (gene therapy) | Cardiovasc Res | PDE2A and PDE4B gene therapy improved heart failure and arrhythmias in mice through cAMP compartmentation |
| [35577932](https://pubmed.ncbi.nlm.nih.gov/35577932/) | 2022 | Preclinical (mechanistic) | Commun Biol | TECRL deficiency disrupts mitochondrial function in cardiomyocytes |
| [30209242](https://pubmed.ncbi.nlm.nih.gov/30209242/) | 2018 | Preclinical (animal) | Sci Transl Med | Sarcoplasmic reticulum calcium leak contributes to arrhythmia but not heart failure progression |

Only PMID 18313614 directly concerns an adenosine-related agent in CPVT, and it is a single case report using ATP.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02457474 | ADENOSINE INJECTION | Injection | Not specified in the available data |
| 02457482 | ADENOSINE INJECTION | Injection | Not specified in the available data |
| 02267659 | ADENOSINE INJECTION | Injection | Not specified in the available data |

All three are valid single-ingredient authorizations.

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (these are graph associations, not package insert text):
- Respiratory: chronic obstructive pulmonary disease, asthma (including intrinsic and allergic), pulmonary emphysema, respiratory failure
- Cardiac conduction: atrioventricular block, sick sinus syndrome (including the familial form)
- Valvular and structural: aortic stenosis (including aortic valve and supravalvular forms), mitral valve stenosis, pulmonary valve insufficiency, pericarditis
- Ischemic: acute coronary syndrome, coronary artery disease
- Other: hypotensive disorder, autonomic nervous system disease, Horner syndrome

**Drug interactions:** 100 interactions were found in total. The main ones listed are:
- **Major:** cisapride, dolasetron, papaverine
- **Moderate:** famotidine, clarithromycin, granisetron, levofloxacin, ondansetron, palonosetron

Many of the Major and Moderate interactions involve drugs that prolong the QT interval, which matters in patients with arrhythmia.

**Repurposing-specific concern:** Catecholamine-sensitive arrhythmias such as CPVT carry a risk of adenosine-induced atrial fibrillation or proarrhythmia. A dedicated safety assessment is needed before any recommendation.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top prediction (obsolete bundle branch block) rests on the model score alone. It has no trials, no literature, and no clear therapeutic rationale. It involves a deprecated disease term, and adenosine could worsen conduction disturbances.
- The CPVT prediction is mechanistically plausible but supported only by one ATP case report (evidence level L4). It is best treated as a research question rather than a candidate for development.

**To proceed, the following is needed:**
- Confirm whether the obsolete bundle branch block term maps to a current disease concept, or discard it as an ontology artifact
- Obtain the Health Canada package insert to review warnings, contraindications, and approved indications
- Obtain mechanism of action data for adenosine
- For CPVT, run a focused literature review and a safety assessment of proarrhythmia risk, including atrial fibrillation
- If CPVT is pursued, begin with preclinical or small mechanistic studies, since no trials are registered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

