---
layout: default
title: Dronedarone
parent: Moderate Evidence (L3-L4)
nav_order: 305
evidence_level: L3
indication_count: 10
---

# Dronedarone
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Dronedarone: From Atrial Fibrillation to Stroke Disorder

## One-Sentence Summary

Dronedarone is a multichannel-blocking antiarrhythmic used for atrial fibrillation (AF) and atrial flutter, and it is marketed in Canada as MULTAQ.
The TxGNN model predicts it may help with **stroke disorder**, but the link is indirect (through AF rhythm control), with **19 registered trials** (only a few dronedarone-specific) and **20 publications**.
No Phase 3 trial has tested dronedarone with stroke prevention as its primary endpoint.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation / atrial flutter (inferred from the trials and literature; no approved-indication text was supplied for the Canadian licence) |
| Predicted New Indication | Stroke disorder |
| TxGNN Prediction Score | 99.97% (model rank 1138) |
| Evidence Level | L3 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the Evidence Pack. Published abstracts describe dronedarone as a multichannel-blocking Class III antiarrhythmic. It has rate- and rhythm-controlling properties, and it reduced cardiovascular hospitalisation or death in the ATHENA trial in AF and flutter.

Stroke is a major complication of AF, and rhythm control may reduce cardioembolic events. Three lines of evidence support the link:
- Post-hoc analyses of ATHENA suggest a lower stroke incidence with dronedarone.
- EAST-AFNET 4, a Phase 4 RCT of early rhythm control (dronedarone was one option), lowered a composite of cardiovascular death, stroke and hospitalisation.
- A preclinical study (PMID 28992468) reports anticoagulant and antiplatelet effects independent of antiarrhythmic action.

The high TxGNN score most likely reflects the AF–stroke association in the knowledge graph rather than a proven independent effect of dronedarone. In PALLAS (permanent AF), dronedarone was associated with excess stroke and heart failure events, which is a key caution.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01288352](https://clinicaltrials.gov/study/NCT01288352) | Phase 4 | Completed | 2789 | EAST-AFNET 4: early rhythm control (antiarrhythmic drugs including dronedarone, or ablation) vs usual care. It lowered a composite of CV death, stroke and hospitalisation. This is a strategy trial, not dronedarone alone. |
| [NCT01151137](https://clinicaltrials.gov/study/NCT01151137) | Phase 3 | Terminated | 3236 | PALLAS: placebo-controlled trial of dronedarone 400 mg BID in permanent AF with additional risk factors. It was terminated early after an excess of stroke and heart failure events. |
| [NCT05130268](https://clinicaltrials.gov/study/NCT05130268) | Phase 4 | Completed | 339 | Pragmatic randomized trial of early dronedarone vs usual care in first-detected AF. No results are available here. |
| [NCT05293080](https://clinicaltrials.gov/study/NCT05293080) | Phase 3 | Not yet recruiting | 1746 | Early rhythm control in acute ischemic stroke with AF. The population is directly relevant, but the intervention is a strategy, not dronedarone specifically. |
| [NCT07270848](https://clinicaltrials.gov/study/NCT07270848) | Phase 4 | Not yet recruiting | 1898 | Dronedarone for early rhythm control in AF, assessing efficacy, safety and quality of life. A stroke endpoint is not confirmed. |
| [NCT01856075](https://clinicaltrials.gov/study/NCT01856075) | N/A | Completed | 1015 | Observational study comparing dronedarone with other AF treatments in real-world practice. Stroke is not the primary endpoint. |
| [NCT05279833](https://clinicaltrials.gov/study/NCT05279833) | N/A | Completed | 87,810 | Systematic review and network meta-analysis of the safety and effectiveness of dronedarone vs sotalol in AF. |
| [NCT04704050](https://clinicaltrials.gov/study/NCT04704050) | Phase 4 | Terminated | 22 | EDORA: dronedarone vs placebo after ablation, looking at AF recurrence and atrial fibrosis. It was too small to be informative. |
| [NCT01266681](https://clinicaltrials.gov/study/NCT01266681) | N/A | Unknown | 100 | Amiodarone vs dronedarone for sinus rhythm maintenance after cardioversion. The endpoint is rhythm, not stroke. |
| [NCT07447297](https://clinicaltrials.gov/study/NCT07447297) | N/A | Recruiting | 520 | Early rhythm control (drugs, cardioversion or ablation) in subclinical AF. It does not necessarily involve dronedarone. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40387892](https://pubmed.ncbi.nlm.nih.gov/40387892/) | 2025 | RCT secondary analysis | Clin Res Cardiol | Long-term safety and efficacy of amiodarone and dronedarone for early rhythm control in EAST-AFNET 4. |
| [22082198](https://pubmed.ncbi.nlm.nih.gov/22082198/) | 2011 | RCT (PALLAS) | N Engl J Med | Tested dronedarone in high-risk permanent AF for reduction of major vascular events. This is the source of the safety signal in permanent AF. |
| [35293087](https://pubmed.ncbi.nlm.nih.gov/35293087/) | 2022 | Review (ATHENA post-hoc analysis) | Eur J Heart Fail | Dronedarone in AF with concomitant heart failure with preserved or mildly reduced ejection fraction. |
| [28992468](https://pubmed.ncbi.nlm.nih.gov/28992468/) | 2017 | Mechanistic / preclinical | Atherosclerosis | Dronedarone showed anticoagulant and antiplatelet effects independent of its antiarrhythmic action. This may help explain the lower stroke and TIA rates seen in ATHENA. |
| [28496906](https://pubmed.ncbi.nlm.nih.gov/28496906/) | 2013 | Cohort | J Atr Fibrillation | Real-world US cohort (10,455 patients) comparing dronedarone with amiodarone and other antiarrhythmics for CV events, stroke, heart failure, interstitial lung disease and acute liver injury. |
| [37485722](https://pubmed.ncbi.nlm.nih.gov/37485722/) | 2023 | Cohort | Circ Arrhythm Electrophysiol | Retrospective comparison of dronedarone vs sotalol in antiarrhythmic-drug-naive veterans with AF. |
| [33888353](https://pubmed.ncbi.nlm.nih.gov/33888353/) | 2021 | Real-world data study | Clin Ther | Risk of digitalis intoxication with concomitant dronedarone and digoxin (P-glycoprotein inhibition). |
| [20730068](https://pubmed.ncbi.nlm.nih.gov/20730068/) | 2010 | Review | Vasc Health Risk Manag | Approval and efficacy of dronedarone. A post-hoc ATHENA analysis suggested reduced stroke risk, with safety concerns in higher-risk patients. |
| [22433576](https://pubmed.ncbi.nlm.nih.gov/22433576/) | 2012 | Guideline | Can J Cardiol | Canadian Cardiovascular Society focused update on AF stroke prevention and rate/rhythm control. |
| [22166900](https://pubmed.ncbi.nlm.nih.gov/22166900/) | 2012 | Review | Lancet | Overview of AF management, including stroke risk stratification and anticoagulation. |

The most stroke-specific dronedarone papers (ATHENA post-hoc and pooled analyses, PMIDs 22149318, 20396635, 40295782 and 30528621) appear under the related "cerebrovascular disorder" prediction. They also report lower stroke incidence, but remain post-hoc or pooled analyses.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2330989 | MULTAQ |

---

## Safety Considerations

Health Canada label warnings and contraindications were not available in the Evidence Pack. Please refer to the package insert for authoritative safety information.

The following cautions come from the published literature and the pack's repurposing rationale, not from the label:
- **Permanent AF**: PALLAS showed excess stroke and heart failure events, so dronedarone is contraindicated in permanent AF.
- **Heart failure**: it is contraindicated in decompensated heart failure.
- **Sinus node dysfunction**: it is not recommended without a pacemaker.
- **Digoxin**: dronedarone may raise digoxin levels through P-glycoprotein inhibition (PMID 33888353).
- **Anticoagulants**: interactions with DOACs such as rivaroxaban are under study (PMIDs 27693025, 41152878).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The stroke signal is indirect and comes mainly from post-hoc analyses and from strategy trials in which dronedarone was one option. No dronedarone RCT has a stroke primary endpoint. The one large placebo-controlled trial in high-risk permanent AF (PALLAS) was terminated early with excess stroke and heart failure events. The finding is best treated as a research question, not a repurposing candidate. The other nine TxGNN predictions (for example ABri amyloidosis, duodenal obstruction, sarcoglycanopathy) have no supporting evidence. "Sick sinus syndrome 2" also raises a safety concern.

**To proceed, the following is needed:**
- Health Canada product monograph (warnings, contraindications, indicated population)
- Mechanism-of-action data (for example from DrugBank)
- Results and stroke-related outcomes from NCT05130268 and the planned NCT07270848
- A dronedarone-specific analysis of stroke within EAST-AFNET 4
- A prospective or pooled analysis with stroke as the primary endpoint, restricted to non-permanent AF without decompensated heart failure
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

