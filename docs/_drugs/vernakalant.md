---
layout: default
title: Vernakalant
parent: Moderate Evidence (L3-L4)
nav_order: 972
evidence_level: L4
indication_count: 6
last_modified_at: 2026-10-13
description: "Vernakalant: predicted new indication Stroke disorder (evidence level L4). Approved use: Atrial fibrillation"
monitor_inn: "Vernakalant"
predicted_indications: ["stroke disorder", "sick sinus syndrome 2, autosomal dominant", "obsolete susceptibility to ischemic stroke", "sarcoglycanopathy", "Wildervanck syndrome", "ABri amyloidosis"]
---

# Vernakalant
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **6** 
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

## Vernakalant: From Atrial Fibrillation to Stroke Disorder
{: .text-alpha }

## One-Sentence Summary

Vernakalant was originally used to treat atrial fibrillation (acute cardioversion of recent-onset AF).
The TxGNN model predicts it may be relevant for **stroke disorder**, but the support is weak: **0 clinical trials** and **7 publications** are currently available, all of which concern AF management rather than stroke outcomes with vernakalant.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation (the Canadian licence record contains no indication text; this comes from the knowledge graph) |
| Predicted New Indication | Stroke disorder |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, vernakalant is an atrial-selective antiarrhythmic that blocks several ion channels (IKur, Ito and early-activating INa). Its efficacy in converting recent-onset atrial fibrillation to sinus rhythm is established.

The link to stroke is indirect. Atrial fibrillation is a major risk factor for cardioembolic stroke, so restoring sinus rhythm could in theory lower stroke risk. However, the retrieved literature covers AF management and cardioversion, not stroke prevention or treatment. Cardioversion itself carries a peri-procedural risk of thromboembolism, and no stroke outcome data for vernakalant were available.

The high TxGNN score reflects the drug's closeness to atrial fibrillation in the knowledge graph. It does not show clinical benefit in stroke.

Other predictions (sick sinus syndrome 2, obsolete susceptibility to ischemic stroke, sarcoglycanopathy, Wildervanck syndrome, ABri amyloidosis) have scores of 99.3%–99.5% but no trials or literature. Most have no plausible mechanistic basis. Sick sinus syndrome could even be worsened by a channel blocker. All are rated L5 and Hold.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27292602](https://pubmed.ncbi.nlm.nih.gov/27292602/) | 2016 | Cohort | Am J Emerg Med | Single-centre study of pharmacological cardioversion of recent-onset AF in the emergency department; assessed safety, efficacy and 30-day thromboembolism or death |
| [17371199](https://pubmed.ncbi.nlm.nih.gov/17371199/) | 2007 | Review | Expert Opin Investig Drugs | Mechanism and development of vernakalant (RSD1235) for acute conversion of AF to sinus rhythm |
| [22166900](https://pubmed.ncbi.nlm.nih.gov/22166900/) | 2012 | Review | Lancet | AF management, including oral anticoagulants and stroke risk stratification |
| [22576674](https://pubmed.ncbi.nlm.nih.gov/22576674/) | 2012 | Review | Curr Hypertens Rep | Recent AF trials in hypertensive patients, including data on novel antiarrhythmics such as dronedarone and vernakalant |
| [23553811](https://pubmed.ncbi.nlm.nih.gov/23553811/) | 2013 | Review | Pharmacotherapy | Clinical update on AF management, including rate versus rhythm control |
| [19678722](https://pubmed.ncbi.nlm.nih.gov/19678722/) | 2009 | Review | J Manag Care Pharm | Established and emerging drug options for AF, with amiodarone as the most effective for maintaining sinus rhythm |
| [25024989](https://pubmed.ncbi.nlm.nih.gov/25024989/) | 2014 | Review | Heart Lung Vessels | 2013 progress in cardiothoracic and vascular anaesthesia, including a new antiarrhythmic and left atrial appendage occlusion for stroke reduction |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02462400 | BRINAVESS | Not specified | Not specified |

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction data were available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for the stroke prediction is a high model score driven by the drug's link to atrial fibrillation. There are no registered trials, no stroke outcome data for vernakalant, and the literature is mostly general AF reviews. Safety data are also missing.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data for vernakalant
- Evidence that vernakalant-based rhythm control reduces stroke or thromboembolic events, ideally from controlled studies
- Mapping of the obsolete "susceptibility to ischemic stroke" term to a current ontology entry
- Approved indication text and dosage form for the Canadian licence (DIN 02462400)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

