---
layout: default
title: Dronedarone
parent: Moderate Evidence (L3-L4)
nav_order: 307
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Dronedarone: predicted new indication Stroke disorder (evidence level L4). Approved use: Atrial fibrillation"
monitor_inn: "DRONEDARONE"
predicted_indications: ["stroke disorder", "obsolete susceptibility to ischemic stroke", "ABri amyloidosis", "cerebrovascular disorder", "brain stem infarction", "sick sinus syndrome 2, autosomal dominant", "duodenal obstruction", "cerebral artery occlusion", "sarcoglycanopathy", "Wildervanck syndrome"]
---

# Dronedarone
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

## Dronedarone: From Atrial Fibrillation to Stroke Disorder
{: .text-alpha }

## One-Sentence Summary

Dronedarone is an antiarrhythmic drug originally used to treat atrial fibrillation (AF).
The TxGNN model predicts it may be useful for **stroke disorder**, with **no registered clinical trials** and **20 publications** (mostly AF management reviews and post hoc or observational analyses) currently related to this direction. The link is indirect, because AF is a major cause of cardioembolic stroke.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation |
| Predicted New Indication | Stroke disorder |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, dronedarone is a class III antiarrhythmic with multichannel-blocking properties. It is structurally related to amiodarone but is non-iodinated. Its efficacy in atrial fibrillation has been established, and the literature describes it as slowing heart rate and restoring or maintaining sinus rhythm.

The relationship between the two conditions is indirect. AF is a major cause of cardioembolic stroke, so any stroke benefit is most likely to come from rhythm or rate control and reduced AF burden, not from a direct neuroprotective action. A post hoc analysis of the ATHENA trial suggested a lower stroke risk with dronedarone in paroxysmal or persistent AF. One laboratory study also reported anticoagulant and antiplatelet effects that are independent of its antiarrhythmic action. Preclinical reviews describe pleiotropic effects on ischemia/reperfusion injury in heart and brain.

These signals come from AF populations and from post hoc or preclinical work. They do not show stroke prevention beyond the existing AF indication. The prediction is therefore best treated as a research question, not an established new use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40387892](https://pubmed.ncbi.nlm.nih.gov/40387892/) | 2025 | RCT (secondary analysis) | Clin Res Cardiol | Long-term safety and efficacy of amiodarone and dronedarone for early rhythm control in EAST-AFNET 4 |
| [37485722](https://pubmed.ncbi.nlm.nih.gov/37485722/) | 2023 | Cohort | Circ Arrhythm Electrophysiol | Dronedarone vs sotalol in antiarrhythmic drug-naive veterans with AF |
| [22082198](https://pubmed.ncbi.nlm.nih.gov/22082198/) | 2011 | RCT (PALLAS) | N Engl J Med | Dronedarone in high-risk permanent AF, tested for reduction of major vascular events |
| [28992468](https://pubmed.ncbi.nlm.nih.gov/28992468/) | 2017 | Experimental | Atherosclerosis | Dronedarone has anticoagulant and antiplatelet effects independent of its antiarrhythmic action; stroke/TIA was reduced in ATHENA |
| [35293087](https://pubmed.ncbi.nlm.nih.gov/35293087/) | 2022 | Post hoc analysis of RCT | Eur J Heart Fail | ATHENA post hoc analysis of dronedarone in AF with preserved or mildly reduced ejection fraction heart failure |
| [20730068](https://pubmed.ncbi.nlm.nih.gov/20730068/) | 2010 | Review | Vasc Health Risk Manag | Approval and efficacy of dronedarone; ATHENA post hoc analysis suggested lower stroke risk |
| [21370206](https://pubmed.ncbi.nlm.nih.gov/21370206/) | 2011 | Review | Swiss Med Wkly | Dronedarone for AF management, in the context of stroke, heart failure and hospitalisation |
| [22166900](https://pubmed.ncbi.nlm.nih.gov/22166900/) | 2012 | Review | Lancet | Overview of AF management, including stroke risk stratification and anticoagulation |
| [28496906](https://pubmed.ncbi.nlm.nih.gov/28496906/) | 2013 | Retrospective cohort | J Atr Fibrillation | Real-world risk of cardiovascular events, stroke, heart failure, interstitial lung disease and liver injury with dronedarone vs amiodarone and others |
| [22433576](https://pubmed.ncbi.nlm.nih.gov/22433576/) | 2012 | Guideline | Can J Cardiol | Canadian Cardiovascular Society 2012 focused update on AF: stroke prevention and rate/rhythm control |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02330989 | MULTAQ | Not listed | Not listed |

---

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: long QT syndrome, familial long QT syndrome, torsades de pointes, liver failure, potassium deficiency disease, atrioventricular block, sick sinus syndrome, familial sick sinus syndrome.
- **Drug Interactions**: The interaction search returned 100 records. Examples of **Major** interactions include hydrocortisone, amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms), loperamide, clarithromycin, picosulfuric acid, polyethylene glycol (3350 with electrolytes) and dolasetron. Examples of **Moderate** interactions include famotidine, alvimopan, aprepitant, dexamethasone, bisacodyl, budesonide, cimetidine, saxagliptin and castor oil.
- **Points from the literature**: Dronedarone is contraindicated in permanent AF and decompensated heart failure. In PALLAS, patients with permanent AF had more heart failure events and higher mortality. It may raise levels of direct oral anticoagulants through P-gp inhibition, which matters for stroke prevention.

Please also refer to the Health Canada package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the supporting evidence is indirect: AF management reviews, post hoc and observational analyses, and preclinical work. There are no stroke-specific trials. Safety concerns in permanent AF and heart failure, and interactions with anticoagulants, further limit any move forward.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are required for safety screening
- Detailed mechanism of action data
- Stroke-specific analysis of ATHENA and similar data, or a prospective study with stroke as the primary outcome
- Evaluation of the interaction with direct oral anticoagulants in AF patients at risk of stroke
- Defined target populations that exclude permanent AF and decompensated heart failure
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

