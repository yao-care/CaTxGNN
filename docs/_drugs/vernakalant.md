---
layout: default
title: Vernakalant
parent: Moderate Evidence (L3-L4)
nav_order: 965
evidence_level: L4
indication_count: 6
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Vernakalant: From Atrial Fibrillation Conversion to Stroke Disorder

## One-Sentence Summary

Vernakalant is an atrial-selective antiarrhythmic used to convert recent-onset atrial fibrillation (AF) to sinus rhythm.
The TxGNN model predicts it may be relevant to **stroke disorder**, but the **3 clinical trials** and **7 publications** found all concern AF cardioversion, and none measures stroke outcomes.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute conversion of recent-onset atrial fibrillation (from the literature; the Health Canada record has no indication text) |
| Predicted New Indication | Stroke disorder |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Vernakalant is an atrial-selective ion channel blocker. It acts on sodium currents and early-activating potassium currents, including IKur, and is used to convert recent-onset AF to sinus rhythm. Detailed mechanism of action data is not available in the source record, so this description comes from the literature and the rationale review.

AF is a major risk factor for cardioembolic stroke, which is probably why the model links the two. The link is indirect, though. Pharmacological cardioversion is not stroke prevention, and cardioversion itself carries a peri-procedural thromboembolic risk. The high TxGNN score most likely reflects the AF–stroke association in the knowledge graph rather than a direct therapeutic effect of the drug on stroke.

Other candidates in the prediction list (sick sinus syndrome, sarcoglycanopathy, Wildervanck syndrome, ABri amyloidosis, an obsolete ischemic stroke susceptibility term) have no trials or literature and no plausible mechanism. Vernakalant could even worsen sinus node dysfunction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04485195](https://clinicaltrials.gov/study/NCT04485195) | Phase 4 | Completed | 350 | RAFF4: IV vernakalant vs IV procainamide for acute AF in 12 Canadian emergency departments. Endpoints are conversion efficacy and safety, not stroke. |
| [NCT01447862](https://clinicaltrials.gov/study/NCT01447862) | Phase 4 | Completed | 101 | Vernakalant vs ibutilide for recent-onset AF. The endpoint is conversion rate, not stroke or thromboembolism. |
| [NCT01646281](https://clinicaltrials.gov/study/NCT01646281) | Phase 4 | Unknown | 70 | Effects of vernakalant vs flecainide on atrial contractility after AF cardioversion. Atrial function is a surrogate for thrombus risk, but no stroke endpoint is reported. |

All three trials are rated as weakly relevant (grade C) to stroke.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27292602](https://pubmed.ncbi.nlm.nih.gov/27292602/) | 2016 | Cohort | Am J Emerg Med | Single-centre experience with pharmacological cardioversion of recent-onset AF in the ED, including 30-day thromboembolism or death. |
| [17371199](https://pubmed.ncbi.nlm.nih.gov/17371199/) | 2007 | Review | Expert Opin Investig Drugs | Vernakalant (RSD1235) as an atrial-selective antifibrillatory agent. Notes stroke as a consequence of AF. |
| [22576674](https://pubmed.ncbi.nlm.nih.gov/22576674/) | 2012 | Review | Curr Hypertens Rep | Recent AF trials in hypertensive patients, including vernakalant. AF is described as a major stroke risk factor. |
| [22166900](https://pubmed.ncbi.nlm.nih.gov/22166900/) | 2012 | Review | Lancet | AF management, with emphasis on stroke risk stratification and oral anticoagulants. |
| [23553811](https://pubmed.ncbi.nlm.nih.gov/23553811/) | 2013 | Review | Pharmacotherapy | Clinical update on AF management. |
| [19678722](https://pubmed.ncbi.nlm.nih.gov/19678722/) | 2009 | Review | J Manag Care Pharm | Established and emerging pharmacological options for AF. |
| [25024989](https://pubmed.ncbi.nlm.nih.gov/25024989/) | 2014 | Review | Heart Lung Vessels | 2013 themes in cardiothoracic anaesthesia, including a new antiarrhythmic and left atrial appendage occlusion for stroke reduction. |

None of these studies shows a stroke benefit from vernakalant. They mainly describe AF as a stroke risk factor.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2462400 | BRINAVESS | Not listed in the record | Not listed in the record |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on an indirect AF–stroke association. The three Phase 4 trials and the literature all address rhythm conversion or atrial function, and none measures stroke incidence. Cardioversion also carries its own thromboembolic risk, so no direct benefit for stroke can be supported.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Mechanism of action data from DrugBank to allow a proper mechanistic analysis
- Evidence with stroke or thromboembolic endpoints, such as post-cardioversion event rates in the RAFF4 data
- Indication text and dosage form for DIN 2462400
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

