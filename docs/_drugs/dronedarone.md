---
layout: default
title: Dronedarone
parent: 僅模型預測 (L5)
nav_order: 243
evidence_level: L5
indication_count: 10
---

# Dronedarone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Dronedarone: From Atrial Fibrillation to Stroke Disorder

## One-Sentence Summary

Dronedarone (brand name Multaq®) is a multichannel-blocking antiarrhythmic agent approved in the United States and European Union for atrial fibrillation (AF) and atrial flutter, used to reduce the risk of cardiovascular hospitalization and death.
The TxGNN model predicts it may offer therapeutic benefit in **stroke disorder**, supported by **19 clinical trials** and **20 publications** currently covering this indication.
With a prediction confidence of **99.97%** and an evidence level of **L2**, this candidate warrants structured clinical evaluation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Atrial fibrillation / Atrial flutter (FDA/EMA-approved; not currently authorized in Canada) |
| Predicted New Indication | Stroke Disorder |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data from Health Canada product monographs is not yet available for this assessment. Based on published clinical and pharmacological evidence, dronedarone is a non-iodinated amiodarone analogue that blocks multiple cardiac ion channels — sodium (Na⁺), potassium (K⁺), and calcium (Ca²⁺) — and exerts non-competitive anti-adrenergic activity. Its primary mechanism involves restoring and maintaining sinus rhythm in patients with paroxysmal or persistent AF, thereby reducing AF burden and the downstream risks associated with sustained irregular rhythm.

The link between dronedarone and stroke prevention is mechanistically well-grounded. AF is one of the strongest modifiable risk factors for cardioembolic stroke: atrial thrombi — most commonly in the left atrial appendage — can embolize to cerebral arteries and cause ischemic stroke. By controlling cardiac rhythm and reducing AF episodes, dronedarone attenuates the hemodynamic stasis and endothelial dysfunction that drive thrombus formation. The landmark EAST-AFNET 4 trial (NCT01288352, n=2,789) demonstrated that early rhythm control strategies — in which dronedarone was a principal antiarrhythmic agent — significantly reduced a composite cardiovascular endpoint that included stroke compared with usual care.

Beyond rhythm control, a key mechanistic study (PMID 28992468) demonstrated that dronedarone exerts **direct anticoagulant and antiplatelet effects independent of its antiarrhythmic action**, including inhibition of P-selectin expression, GPIIb/IIIa activation, and thrombin generation. This dual mechanism — rhythm normalization *plus* direct antithrombotic activity — provides a compelling biological rationale for the TxGNN prediction and helps explain the stroke reduction observed in the ATHENA post-hoc analysis (paroxysmal/persistent AF patients). The 2025 EAST-AFNET 4 sub-analysis (PMID 40387892) further confirmed long-term safety and efficacy of dronedarone for early rhythm control in reducing stroke-related outcomes.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01288352](https://clinicaltrials.gov/study/NCT01288352) | Phase 4 | Completed | 2,789 | EAST-AFNET 4: Early AF rhythm control (dronedarone as principal AAD) vs usual care; significantly reduced composite endpoint including stroke and cardiovascular death |
| [NCT05293080](https://clinicaltrials.gov/study/NCT05293080) | Phase 3 | Not Yet Recruiting | 1,746 | EAST-STROKE: Evaluates early, comprehensive rhythm control (including dronedarone) in acute ischemic stroke patients with AF to prevent recurrent cardiovascular events; stroke is the primary endpoint |
| [NCT07270848](https://clinicaltrials.gov/study/NCT07270848) | Phase 4 | Not Yet Recruiting | 1,898 | Prospective multicenter RCT directly evaluating dronedarone efficacy, safety, and quality of life for early rhythm control in AF (2026–2028); head-to-head vs alternative AAD |
| [NCT05130268](https://clinicaltrials.gov/study/NCT05130268) | Phase 4 | Completed | 339 | Pragmatic RCT of early dronedarone vs usual care in first-detected AF; directly assesses outcomes including stroke prevention in a previously understudied AF population |
| [NCT01151137](https://clinicaltrials.gov/study/NCT01151137) | Phase 3 | Terminated | 3,236 | PALLAS trial: Dronedarone 400 mg BID in permanent AF with additional stroke risk factors; terminated early due to increased rates of stroke, HF hospitalization, and cardiovascular death — critical safety reference for patient selection |
| [NCT01856075](https://clinicaltrials.gov/study/NCT01856075) | Observational | Completed | 1,015 | International real-world cohort (Germany, Spain, Italy, USA) comparing dronedarone vs other AADs for AF in clinical practice; stroke as secondary effectiveness endpoint |
| [NCT05279833](https://clinicaltrials.gov/study/NCT05279833) | SLR/NMA | Completed | 87,810 | Systematic literature review and network meta-analysis comparing dronedarone vs sotalol safety and effectiveness across interventional and observational studies in AF |
| [NCT01266681](https://clinicaltrials.gov/study/NCT01266681) | N/A | Unknown | 100 | Head-to-head: Amiodarone vs dronedarone for sinus rhythm maintenance after DC cardioversion in persistent AF; indirect evidence for rhythm control capacity |
| [NCT04704050](https://clinicaltrials.gov/study/NCT04704050) | Phase 4 | Terminated | 22 | EDORA: Dronedarone vs placebo post-cardiac ablation — effect on atrial fibrosis progression and AF recurrence; provides mechanistic insight into structural cardiac remodeling |
| [NCT02618577](https://clinicaltrials.gov/study/NCT02618577) | Phase 3 | Terminated | 2,608 | NOAH-AFNET 6: NOAC (edoxaban) vs usual care for AF high-rate episodes; dronedarone used as background rhythm control; stroke was a secondary endpoint |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40387892](https://pubmed.ncbi.nlm.nih.gov/40387892/) | 2025 | RCT Post-hoc Analysis | Clinical Research in Cardiology | Long-term safety and outcomes of dronedarone and amiodarone in EAST-AFNET 4 early rhythm control; confirms dronedarone's contribution to stroke endpoint reduction with acceptable safety |
| [28992468](https://pubmed.ncbi.nlm.nih.gov/28992468/) | 2017 | Mechanistic Study | Atherosclerosis | Dronedarone inhibits P-selectin, GPIIb/IIIa, and thrombin generation independently of antiarrhythmic effects, providing a direct antithrombotic mechanism relevant to stroke prevention |
| [28496906](https://pubmed.ncbi.nlm.nih.gov/28496906/) | 2013 | Cohort Study | Journal of Atrial Fibrillation | Real-world US retrospective cohort (n=10,455): Dronedarone vs amiodarone and other AADs — comparative risk of stroke, CHF, interstitial lung disease, and acute liver injury |
| [37485722](https://pubmed.ncbi.nlm.nih.gov/37485722/) | 2023 | Retrospective Cohort | Circulation: Arrhythmia and Electrophysiology | Dronedarone vs sotalol in AAD-naïve veterans with AF: dronedarone did not require QT monitoring and demonstrated comparable sinus rhythm maintenance without excess arrhythmia risk |
| [35293087](https://pubmed.ncbi.nlm.nih.gov/35293087/) | 2022 | RCT Post-hoc Analysis | European Journal of Heart Failure | ATHENA post-hoc: Dronedarone reduced cardiovascular events in AF patients with concomitant HFpEF/HFmrEF — expands target population beyond systolic dysfunction |
| [22082198](https://pubmed.ncbi.nlm.nih.gov/22082198/) | 2011 | Phase 3 RCT (PALLAS) | New England Journal of Medicine | PALLAS trial: Dronedarone significantly increased stroke, HF hospitalization, and death in **permanent** AF — establishes the critical contraindication boundary for stroke indication |
| [20730068](https://pubmed.ncbi.nlm.nih.gov/20730068/) | 2010 | Review | Vascular Health and Risk Management | Comprehensive review of dronedarone FDA approval; ATHENA post-hoc analysis showed significant reduction in stroke and TIA in paroxysmal/persistent AF patients |
| [22433576](https://pubmed.ncbi.nlm.nih.gov/22433576/) | 2012 | Clinical Guideline | Canadian Journal of Cardiology | Canadian Cardiovascular Society 2012 AF guideline focused update — includes dronedarone in recommendations for stroke prevention and rhythm control strategy selection |
| [24469871](https://pubmed.ncbi.nlm.nih.gov/24469871/) | 2013 | Review | Cardiology Journal | Clinical practice review of dronedarone efficacy and tolerability in AF: summarizes major trial data including ATHENA, DIONYSOS, ANDROMEDA, and PALLAS |
| [22920480](https://pubmed.ncbi.nlm.nih.gov/22920480/) | 2012 | Review | Current Cardiology Reviews | Stroke prevention in AF: evolving strategies including rhythm control agents and novel anticoagulants; contextualizes dronedarone's role within the antithrombotic landscape |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Critical Evidence-Based Caution:** The PALLAS trial (NCT01151137, published in NEJM 2011, PMID 22082198) was terminated early because dronedarone significantly **increased** stroke, heart failure hospitalization, and cardiovascular death in patients with **permanent** AF. This is a well-established class contraindication: dronedarone must only be used in **non-permanent (paroxysmal or persistent)** AF. Any stroke-prevention indication must rigorously exclude patients with permanent AF. Additionally, dronedarone inhibits P-glycoprotein and CYP3A4, increasing plasma concentrations of co-administered direct oral anticoagulants (DOACs) — a pharmacokinetic interaction requiring dose adjustment and monitoring (PMID 41152878, 27693025).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The EAST-AFNET 4 trial (n=2,789, completed Phase 4) and the post-hoc ATHENA analysis provide convergent evidence that dronedarone, as part of early rhythm control in **non-permanent** AF, significantly reduces stroke and cardiovascular events. The dual mechanism of rhythm normalization plus direct antithrombotic activity (PMID 28992468) and the inclusion of dronedarone in the 2012 Canadian Cardiovascular Society AF guidelines support the scientific credibility of this repurposing prediction. Evidence meets the L2 threshold. However, the PALLAS safety signal mandates careful patient selection and guardrails.

**To proceed, the following is needed:**

- Obtain the Health Canada product monograph (once/if authorized) to confirm Canadian-specific indication language, warnings, and contraindications
- Apply the PALLAS exclusion rule rigorously: **dronedarone is contraindicated in permanent AF** — any stroke indication must target paroxysmal or persistent AF only
- Define the precise target population using EAST-AFNET 4 and ATHENA stroke sub-population data (early AF diagnosis, ≥1 cardiovascular comorbidity, no permanent AF)
- Evaluate the clinical significance of the dronedarone–DOAC pharmacokinetic interaction (P-gp inhibition elevating DOAC levels) given that AF stroke-prevention regimens commonly combine antiarrhythmic and anticoagulant drugs
- Monitor emerging data from NCT05293080 (EAST-STROKE, n=1,746) and NCT07270848 (Phase 4 RCT, n=1,898) — both expected to provide direct evidence in the stroke population by 2028–2029
- Pursue Health Canada Drug Identification Number (DIN) application as a prerequisite for Canadian market access
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

