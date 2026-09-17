---
layout: default
title: Norepinephrine
parent: Moderate Evidence (L3-L4)
nav_order: 561
evidence_level: L4
indication_count: 3
---

# Norepinephrine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Norepinephrine: From Vasopressor Therapy in Shock to Obstructive Lung Disease

## One-Sentence Summary

Norepinephrine is a catecholamine best known as a first-line vasopressor for acute hypotension and septic shock. The TxGNN model predicts it may be effective for **Obstructive Lung Disease**, but the **18 clinical trials** and **19 publications** currently linked to this pair are almost entirely incidental (disease-term co-occurrence or background ICU vasopressor use) rather than direct evidence of a therapeutic effect — this is a low-confidence, mechanism-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute hypotension / septic shock (vasopressor) — not extractable from the evidence pack; no Canadian license or indication text is on file |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this candidate is not available in the evidence pack (Data Gap DG002). Based on known pharmacology, norepinephrine is a non-selective α/β-adrenergic agonist whose established clinical role is raising blood pressure and cardiac output in shock states; it has essentially no approved role as a bronchodilator or airway-directed therapy.

The repurposing signal appears to stem from a real but indirect biological relationship: circulating and neuronally released noradrenaline modulates airway smooth-muscle tone and vascular caliber, and several of the retrieved publications describe altered plasma noradrenaline levels or autonomic/sympathetic signaling in COPD and asthma. This is a *disease-physiology* association, not a *treatment* association — norepinephrine's β2-mediated bronchial effect is far weaker than dedicated bronchodilators (e.g., albuterol, salmeterol), while its dominant α1 (vasoconstriction) and β1 (chronotropic/inotropic) effects raise safety concerns rather than therapeutic benefit in a population that often already has hypoxia and arrhythmia risk.

Taken together, the mechanistic link is plausible only in the loose sense of "the same neurotransmitter system is involved in this disease's pathophysiology," not in the sense of "this drug is a candidate treatment." This is consistent with the TxGNN internal rationale flag for this pair, which explicitly notes the association is more likely to reflect knowledge-graph semantic proximity (shared "respiratory/autonomic" nodes) than a genuine repurposing opportunity.

## Clinical Trial Evidence

None of the retrieved trials test norepinephrine as an intervention for obstructive lung disease; norepinephrine appears only as background ICU/vasopressor therapy or the diseases co-occur incidentally. Listed below are the most topically relevant of the 18 registered trials:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02360865](https://clinicaltrials.gov/study/NCT02360865) | NA | Completed | 18 | Investigates endothelial dysfunction and muscle sympathetic nerve activity (noradrenergic signaling) as mechanisms of exercise intolerance in COPD — mechanistic, not interventional on norepinephrine |
| [NCT01536587](https://clinicaltrials.gov/study/NCT01536587) | Phase 4 | Completed | 32 | Salmeterol's effect on sympathetic activity in COPD (GOLD II/III) via microneurography — tests a bronchodilator, not norepinephrine |
| [NCT01219738](https://clinicaltrials.gov/study/NCT01219738) | NA | Completed | 20 | Inhaled budesonide's acute effect on airway vascular smooth muscle; references endogenous norepinephrine as a background mediator (Grade C — not a norepinephrine trial) |
| [NCT07332442](https://clinicaltrials.gov/study/NCT07332442) | Phase 3 | Not yet recruiting | 250 | CPAP/arousal-threshold mechanisms in obstructive sleep apnea; no norepinephrine intervention (Grade C) |
| [NCT00834509](https://clinicaltrials.gov/study/NCT00834509) | N/A | Completed | 181 | Blood-test biomarker development for obstructive sleep apnea diagnosis; unrelated to norepinephrine treatment (Grade C) |
| [NCT02627378](https://clinicaltrials.gov/study/NCT02627378) | Phase 1 | Completed | 35 | ECMO support for MERS-CoV respiratory failure; norepinephrine only as standard ICU vasopressor background (Grade C) |
| [NCT02564406](https://clinicaltrials.gov/study/NCT02564406) | NA | Completed | 35 | Extracorporeal CO2 removal in hypercapnic COPD exacerbation failing NIV; no norepinephrine intervention |
| [NCT02966665](https://clinicaltrials.gov/study/NCT02966665) | Phase 1 | Recruiting | 420 | Vascular tone/sympathetic regulation in hypertension rehabilitation; disease-mechanism study, not COPD treatment |
| [NCT05655065](https://clinicaltrials.gov/study/NCT05655065) | NA | Recruiting | 30 | Effect of raising mean arterial pressure (via vasopressors, incl. norepinephrine) on renal function in shock — ICU hemodynamics, not obstructive lung disease |
| [NCT07022210](https://clinicaltrials.gov/study/NCT07022210) | N/A | Recruiting | 100 | Incidence of post-anesthesia hypotension; norepinephrine relevant only as rescue therapy for hypotension, not lung disease |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9009625](https://pubmed.ncbi.nlm.nih.gov/9009625/) | 1996 | Cohort | Monaldi Arch Chest Dis | Right-heart catheterization study finding elevated plasma noradrenaline and altered hormone/haemodynamic profile in early-stage COPD |
| [1617386](https://pubmed.ncbi.nlm.nih.gov/1617386/) | 1992 | Review | Br Med Bull | Reviews tracheobronchial vasculature control in asthma; sympathetic nerves (noradrenaline, NPY) constrict airway vasculature |
| [24486056](https://pubmed.ncbi.nlm.nih.gov/24486056/) | 2014 | Review | Semin Immunol | Reviews sympathetic–immune interaction and neuroendocrine regulation of inflammation, including catecholamine signaling |
| [2048831](https://pubmed.ncbi.nlm.nih.gov/2048831/) | 1991 | Review | Am Rev Respir Dis | Reviews autonomic (cholinergic/noradrenergic) control of airway caliber in asthma and COPD |
| [3332227](https://pubmed.ncbi.nlm.nih.gov/3332227/) | 1987 | Review | Crit Care Clin | Reviews catecholamines (norepinephrine, epinephrine, dopamine) in critical illness, congestive heart failure, and cardiopulmonary conditions |
| [38987587](https://pubmed.ncbi.nlm.nih.gov/38987587/) | 2024 | Preclinical (mechanistic) | Nature | Identifies brainstem Dbh+ (noradrenergic) neurons controlling allergen-induced airway hyperreactivity in mice |
| [6777857](https://pubmed.ncbi.nlm.nih.gov/6777857/) | 1980 | Observational | Scand J Clin Lab Invest | Reports increased plasma noradrenaline in chronic obstructive lung disease, correlated with hypoxemia/hypercapnia |
| [3420304](https://pubmed.ncbi.nlm.nih.gov/3420304/) | 1988 | Observational | Respiration | Hemodynamic effects of dopamine/L-dopa (not norepinephrine) in pulmonary hypertension secondary to COPD |
| [11099681](https://pubmed.ncbi.nlm.nih.gov/11099681/) | 2000 | Observational | Am J Med | Investigates norepinephrine, endothelin-1, and ANF as mechanisms of hypertension during acute respiratory failure in COPD |
| [21271508](https://pubmed.ncbi.nlm.nih.gov/21271508/) | 2011 | Review | Pneumologie | Reviews airway innervation (noradrenergic and cholinergic) in asthma and COPD |

## Canada Market Information

Norepinephrine currently has no marketing authorizations on file in this evidence pack (market status: **Not Marketed**, 0 licenses/DINs recorded).

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data were not available in the evidence pack — Data Gap DG001, flagged as Blocking.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale is weak and arguably points toward a safety risk rather than a therapeutic benefit — none of the 18 trials or 19 publications directly test norepinephrine as a treatment for obstructive lung disease, and its dominant α1/β1 pharmacology could worsen outcomes in a population prone to hypoxia and arrhythmia. Combined with a Blocking data gap on labeling/safety and no current Canadian market authorization, this candidate does not meet the bar to proceed.

**To proceed, the following is needed:**
- TFDA/Health Canada label warnings and contraindications (DG001, Blocking)
- Confirmed mechanism-of-action reference data (DG002)
- Any direct interventional evidence (preclinical or clinical) testing norepinephrine specifically for airway obstruction rather than as incidental ICU vasopressor
- Cardiopulmonary safety monitoring plan given the target population's hypoxia/arrhythmia risk

*Note: Two additional TxGNN candidates for this drug — "respiratory malformation" and "Rienhoff syndrome" — scored similarly but at Evidence Level L5 (model prediction only, no supporting trials/literature) and are considered lower priority than the above.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

