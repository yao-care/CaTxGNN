---
layout: default
title: Flecainide
parent: High Evidence (L1-L2)
nav_order: 386
evidence_level: L2
indication_count: 10
---

# Flecainide
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Flecainide: From Cardiac Arrhythmia to Stroke Disorder

## One-Sentence Summary

Flecainide is a class IC antiarrhythmic drug used for rhythm control in atrial fibrillation (AF) and other arrhythmias.
The TxGNN model predicts it may be useful for **stroke disorder**, but the support is indirect: **21 registered trials** and **20 publications** were retrieved, and none shows that flecainide itself reduces stroke.
The strongest signal is the large EAST-AFNET 4 trial, which supports early rhythm control as a strategy, not flecainide specifically.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cardiac arrhythmias, mainly atrial fibrillation (Canadian license text is blank in the data, so this is inferred from the evidence) |
| Predicted New Indication | Stroke disorder |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L2 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Flecainide is a class IC sodium channel blocker that slows cardiac conduction and is used to keep patients with AF in normal rhythm. Its efficacy in AF rhythm control is established, and the link to stroke is indirect.

AF is a major cause of cardioembolic stroke. Restoring and maintaining normal rhythm early might lower stroke risk, and the TxGNN prediction probably reflects this graph proximity between AF and stroke. In EAST-AFNET 4 (NCT01288352, 2,789 patients), early rhythm control with antiarrhythmic drugs (flecainide among them) or ablation had a favourable composite outcome that included stroke. The finding applies to the strategy as a whole, not to flecainide alone.

Flecainide should not be given to patients with structural heart disease, coronary artery disease or prior myocardial infarction (CAST), and many stroke patients have these conditions. Any use would need an AF-confirmed population and strict patient selection.

The other nine predictions (ranks 2–10) are weak. "Cerebrovascular disorder" overlaps heavily with stroke and shares the same evidence. "Obsolete susceptibility to ischemic stroke" is an obsolete term and probably a graph artifact. "Sick sinus syndrome 2" is a safety concern, since flecainide can worsen sinus node dysfunction. The rest (ABri amyloidosis, sarcoglycanopathy, Wildervanck syndrome, macrocephaly syndrome, duodenal obstruction, nephrogenic SIAD) have no plausible mechanism and no clinical evidence.

---

## Clinical Trial Evidence

Of the 21 trials retrieved, only one is graded highly relevant, and none tests flecainide against a stroke endpoint. The most relevant are listed below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01288352](https://clinicaltrials.gov/study/NCT01288352) | Phase 4 | Completed | 2,789 | EAST-AFNET 4: early rhythm control (antiarrhythmic drugs including flecainide, or ablation) vs usual care in AF, composite outcome includes stroke; strategy-level evidence |
| [NCT05213104](https://clinicaltrials.gov/study/NCT05213104) | Phase 3 | Active, not recruiting | 186 | Flecainide to reduce atrial arrhythmia after patent foramen ovale closure in cryptogenic stroke patients; endpoint is arrhythmia, not stroke |
| [NCT05293080](https://clinicaltrials.gov/study/NCT05293080) | Phase 3 | Recruiting | 1,746 | Early rhythm control in acute ischemic stroke with AF; flecainide use unconfirmed and likely restricted |
| [NCT01646281](https://clinicaltrials.gov/study/NCT01646281) | Phase 4 | Unknown | 70 | Flecainide vs vernakalant on atrial contractility in AF; relevant to thromboembolic risk, no stroke outcome |
| [NCT00911508](https://clinicaltrials.gov/study/NCT00911508) | N/A | Completed | 2,204 | CABANA: catheter ablation vs antiarrhythmic or rate-control drugs; drug arm gives context, flecainide not isolated |
| [NCT07405671](https://clinicaltrials.gov/study/NCT07405671) | Phase 4 | Recruiting | 988 | Flecainide safety vs sotalol or amiodarone in AF with stable coronary artery disease; addresses the key safety question |
| [NCT00523978](https://clinicaltrials.gov/study/NCT00523978) | Phase 3 | Completed | 245 | STOP AF: cryoablation vs antiarrhythmic drugs (flecainide, propafenone or sotalol) in paroxysmal AF |
| [NCT06783868](https://clinicaltrials.gov/study/NCT06783868) | N/A | Not yet recruiting | 100 | AF ablation vs medication after recent stroke; flecainide not the intervention |
| [NCT05939076](https://clinicaltrials.gov/study/NCT05939076) | Phase 3 | Not yet recruiting | 220 | First-line cryoablation vs antiarrhythmic medication in persistent AF |
| [NCT06096337](https://clinicaltrials.gov/study/NCT06096337) | N/A | Active, not recruiting | 484 | Pulsed field ablation vs antiarrhythmic drugs in persistent AF; drug arm not flecainide-specific |

---

## Literature Evidence

Most publications concern AF management in general. Only a few address flecainide directly.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38702961](https://pubmed.ncbi.nlm.nih.gov/38702961/) | 2024 | RCT (secondary analysis) | Europace | EAST-AFNET 4 analysis of the safety and efficacy of long-term sodium channel blockers (flecainide, propafenone) for early rhythm control |
| [25820938](https://pubmed.ncbi.nlm.nih.gov/25820938/) | 2015 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Antiarrhythmics for maintaining sinus rhythm after AF cardioversion; no stroke reduction attributable to flecainide |
| [41954064](https://pubmed.ncbi.nlm.nih.gov/41954064/) | 2026 | Cohort | J Am Heart Assoc | Long-term outcomes of class 1C drugs in AF, asking whether they beat rate control |
| [23871349](https://pubmed.ncbi.nlm.nih.gov/23871349/) | 2013 | Trial analysis | Int J Cardiol | Flec-SL trial analysis: low stroke risk after elective cardioversion of AF |
| [8729366](https://pubmed.ncbi.nlm.nih.gov/8729366/) | 1995 | Clinical study (38 patients) | Arch Mal Coeur Vaiss | Atrial electrophysiology and effects of intravenous flecainide in unexplained ischemic cerebrovascular events |
| [41152878](https://pubmed.ncbi.nlm.nih.gov/41152878/) | 2025 | Cohort | BMC Med | Stroke and bleeding risk with combined direct oral anticoagulant and interacting antiarrhythmic use in AF |
| [35114252](https://pubmed.ncbi.nlm.nih.gov/35114252/) | 2022 | Mechanism study | J Mol Cell Cardiol | Altered sodium channel biophysics explain flecainide's greater effect in atrium than ventricle |
| [27159789](https://pubmed.ncbi.nlm.nih.gov/27159789/) | 2016 | Review | Nat Rev Dis Primers | Overview of AF, including its association with stroke |
| [38551548](https://pubmed.ncbi.nlm.nih.gov/38551548/) | 2024 | Study | JACC Clin Electrophysiol | Class 1C drugs for PVC suppression in nonischemic cardiomyopathy, a population where guidelines restrict use |
| [8199770](https://pubmed.ncbi.nlm.nih.gov/8199770/) | 1994 | Review | Heart Dis Stroke | Flecainide's value in supraventricular tachycardia and its risks |

---

## Canada Market Information

Flecainide has 10 licenses in Canada; five are listed below. Dosage form and approved indication text are blank in the source data.

| DIN | Product Name |
|---------|------|
| 2534819 | FLECAINIDE |
| 2275538 | APO-FLECAINIDE |
| 2459957 | AURO-FLECAINIDE |
| 2493713 | JAMP FLECAINIDE |
| 2516063 | AG-FLECAINIDE |

---

## Safety Considerations

Package insert warnings and contraindications were not retrieved, and no drug interaction data were found. The points below come from the evidence pack's rationale and the retrieved literature, not from the Canadian label.

- **Structural and ischemic heart disease**: flecainide is contraindicated in structural heart disease, coronary artery disease and after myocardial infarction (CAST). Many stroke patients fall into these groups.
- **Sick sinus syndrome**: flecainide can worsen sinus node dysfunction and is generally avoided without pacing support.
- **Proarrhythmia**: the literature reports QRS widening, refractory ventricular tachycardia and unmasking of a Brugada pattern, especially at higher doses or heart rates.

Please refer to the Health Canada package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The stroke signal comes from a strategy-level trial (EAST-AFNET 4), not from flecainide-specific data, and no trial tests flecainide against a stroke endpoint. The population most likely to have a stroke is also the population where flecainide is restricted. The Canadian safety data are also missing, which blocks safety screening.

**To proceed, the following is needed:**
- The Health Canada package insert (warnings, contraindications, interactions)
- Mechanism of action data from DrugBank
- Flecainide-specific outcomes from EAST-AFNET 4 sub-analyses and from NCT05213104 (flecainide after PFO closure)
- Results from NCT07405671 (flecainide safety in AF with coronary artery disease)
- A defined study population of AF-confirmed patients without structural or ischemic heart disease
- A decision on whether the overlapping "stroke disorder" and "cerebrovascular disorder" predictions are treated as one candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

