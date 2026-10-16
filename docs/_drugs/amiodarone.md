---
layout: default
title: Amiodarone
parent: Model Prediction Only (L5)
nav_order: 52
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Amiodarone: predicted new indication Catecholaminergic polymorphic ventricular tachycardia (evidence level L5). Approved use: Ventricular fibrillation"
monitor_inn: "Amiodarone"
predicted_indications: ["catecholaminergic polymorphic ventricular tachycardia", "incessant infant ventricular tachycardia", "ventricular tachycardia", "obsolete bundle branch block", "rheumatoid arthritis", "brachydactyly-syndactyly syndrome", "heparin cofactor 2 deficiency", "trichotillomania", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "gout"]
---

# Amiodarone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Amiodarone: From Ventricular Fibrillation to Catecholaminergic Polymorphic Ventricular Tachycardia

## One-Sentence Summary

Amiodarone is an antiarrhythmic originally used for ventricular fibrillation.
The TxGNN model's top-ranked prediction is **catecholaminergic polymorphic ventricular tachycardia (CPVT)**, but **no clinical trials** and only **9 publications** (cohorts, case reports and reviews, none showing a benefit from amiodarone) support it.
The best-supported direction among the model's top 10 is instead **ventricular tachycardia**, which is closer to an established use than to true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ventricular fibrillation (the approved indication text in the Canadian licence records is empty) |
| Predicted New Indication | Catecholaminergic polymorphic ventricular tachycardia |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L4 (CPVT); L1 for the rank 3 prediction, ventricular tachycardia |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 12 |
| Recommended Decision | Hold (CPVT); Proceed with Guardrails (ventricular tachycardia) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, amiodarone blocks potassium, sodium and calcium channels and has beta-adrenergic antagonist effects. This explains its efficacy in ventricular fibrillation and could in principle be relevant to arrhythmias triggered by adrenergic stress.

For CPVT, however, the plausibility is weak. The core defect is calcium leak related to RYR2/CASQ2 mutations. Guideline-supported therapies are beta-blockers, flecainide and sympathetic denervation, and amiodarone is generally considered ineffective or inferior in this condition. The high model score therefore should not be read as evidence of benefit.

For comparison, the other predictions in the top 10 differ widely:
- **Ventricular tachycardia (rank 3):** strongly supported, because amiodarone's multichannel blockade addresses re-entrant and triggered ventricular arrhythmias. This is an established use.
- **Incessant infant ventricular tachycardia (rank 2):** plausible. Trials show IV amiodarone is effective in incessant tachyarrhythmias in children, though mostly supraventricular types, so VT-specific evidence is limited.
- **Obsolete bundle branch block, rheumatoid arthritis, brachydactyly-syndactyly syndrome, heparin cofactor 2 deficiency, trichotillomania, colobomatous microphthalmia-rhizomelic dysplasia syndrome and gout (ranks 4-10):** no plausible therapeutic mechanism. Amiodarone slows conduction and can worsen conduction block. The rheumatoid arthritis and gout literature describes toxicity and drug interactions, not efficacy.

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked prediction (CPVT). The most relevant trials, listed below, belong to the rank 3 prediction, ventricular tachycardia.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01401647](https://clinicaltrials.gov/study/NCT01401647) | Phase 3 | Completed | 3024 | Amiodarone vs lidocaine vs placebo in out-of-hospital cardiac arrest from shock-refractory VF/pulseless VT |
| [NCT00000531](https://clinicaltrials.gov/study/NCT00000531) | Phase 3 | Completed | N/A | AVID: antiarrhythmic drugs (mainly amiodarone) vs implantable defibrillator in life-threatening ventricular arrhythmias |
| [NCT00257959](https://clinicaltrials.gov/study/NCT00257959) | Phase 4 | Completed | 400 | OPTIC: amiodarone plus beta-blocker vs sotalol vs beta-blocker alone for preventing ICD shocks |
| [NCT00383799](https://clinicaltrials.gov/study/NCT00383799) | Phase 4 | Terminated | 302 | PROCAMIO: IV amiodarone vs procainamide in well-tolerated wide-QRS tachycardia (presumed VT); terminated early |
| [NCT03299517](https://clinicaltrials.gov/study/NCT03299517) | Phase 4 | Unknown | 80 | Amiodarone vs lidocaine in stable VT in the emergency room |
| [NCT02830360](https://clinicaltrials.gov/study/NCT02830360) | Phase 4 | Completed | 416 | Catheter ablation vs antiarrhythmic drug therapy after myocardial infarction with sustained monomorphic VT |
| [NCT03734562](https://clinicaltrials.gov/study/NCT03734562) | NA | Completed | 180 | Substrate ablation vs antiarrhythmic drugs in ischemic cardiomyopathy with monomorphic VT |
| [NCT01722942](https://clinicaltrials.gov/study/NCT01722942) | NA | Unknown | 1100 | CHAGASICS: amiodarone vs ICD for primary prevention in Chagas cardiomyopathy with non-sustained VT |
| [NCT03855826](https://clinicaltrials.gov/study/NCT03855826) | Phase 4 | Unknown | 756 | Nifekalant vs amiodarone in VT/VF; amiodarone is at most a comparator |
| [NCT01097330](https://clinicaltrials.gov/study/NCT01097330) | Phase 3 | Terminated | 12 | Catheter ablation vs amiodarone for shock prophylaxis in ICD patients; too small to be informative |

## Literature Evidence

**Top-ranked prediction (CPVT).** The retrieved literature is descriptive and none of it shows a benefit from amiodarone:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Systematic review | Life (Basel) | Clinical characteristics, genetics and arrhythmic outcomes of CPVT patients from China |
| [39076628](https://pubmed.ncbi.nlm.nih.gov/39076628/) | 2022 | Cohort | Rev Cardiovasc Med | Clinical features, genetics, healthcare use and costs of CPVT in a Chinese city |
| [26513538](https://pubmed.ncbi.nlm.nih.gov/26513538/) | 2015 | Review | Expert Opin Pharmacother | Advances in drug treatment of ventricular arrhythmias |
| [22553997](https://pubmed.ncbi.nlm.nih.gov/22553997/) | 2012 | Case report | Pacing Clin Electrophysiol | Flecainide suppressed defibrillator-induced storming in CPVT |

**Rank 3 prediction (ventricular tachycardia):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27354046](https://pubmed.ncbi.nlm.nih.gov/27354046/) | 2017 | RCT | Eur Heart J | PROCAMIO: IV procainamide vs amiodarone for tolerated wide-QRS tachycardia |
| [20730062](https://pubmed.ncbi.nlm.nih.gov/20730062/) | 2010 | Review | Vasc Health Risk Manag | Amiodarone as a leading therapy for terminating and preventing VF/VT |
| [30084131](https://pubmed.ncbi.nlm.nih.gov/30084131/) | 2018 | Cohort | Emerg Med Australas | Safety and efficacy of paramedic-administered amiodarone in stable VT |
| [37380314](https://pubmed.ncbi.nlm.nih.gov/37380314/) | 2023 | Trial analysis | JACC Clin Electrophysiol | VT and ICD therapy burden with catheter ablation vs escalated antiarrhythmic drugs |

**Rank 2 prediction (incessant infant ventricular tachycardia):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16316969](https://pubmed.ncbi.nlm.nih.gov/16316969/) | 2005 | RCT | Circulation | Randomized, double-blind trial of IV amiodarone for incessant tachyarrhythmias in children |
| [14508682](https://pubmed.ncbi.nlm.nih.gov/14508682/) | 2003 | Cohort | Eur J Pediatr | Efficacy and safety of IV amiodarone in 23 infants with incessant tachycardias |

## Canada Market Information

The Canadian licence records list 12 valid single-ingredient authorizations, but dosage form and approved indication text are not available for any of them. The first five are shown below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02364336 | AMIODARONE | Not available | Not available |
| 02243836 | SANDOZ AMIODARONE | Not available | Not available |
| 02247217 | RIVA-AMIODARONE | Not available | Not available |
| 02292173 | PMS-AMIODARONE | Not available | Not available |
| 02385465 | AMIODARONE | Not available | Not available |

Other authorizations include injectable products (02242325, 02245248) and tablet products (for example APO-AMIODARONE, 02246194).

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these come from model-graph associations, not from the label): long QT syndrome and torsades de pointes, atrioventricular block, sick sinus syndrome, liver disease and drug-induced liver injury, thyroid disorders (hypothyroidism and hyperthyroidism, including Graves disease), interstitial lung disease, eosinophilic pneumonia and hypersensitivity pneumonitis, optic neuritis and optic nerve disease, peripheral neuropathy, potassium deficiency, and corneal deposits.
- **Drug Interactions:** 100 interactions were identified. Major ones include clarithromycin, cisapride, dolasetron, eliglustat, clotrimazole, hydrocortisone, dexamethasone, agalsidase beta and several amphotericin B formulations. Moderate ones include famotidine, cimetidine, aprepitant, bisacodyl and budesonide.
- **Reported in the literature:** pulmonary toxicity (fibrosis, diffuse alveolar hemorrhage), thyroid dysfunction, and rhabdomyolysis when combined with statins or other interacting drugs. Neonatal and infant use needs close monitoring for thyroid, hemodynamic and proarrhythmic toxicity.

Package insert warnings and contraindications were not available for this report; please refer to the Health Canada package insert.

## Conclusion and Next Steps

**Decision: Hold (CPVT, the top-ranked prediction)**

**Rationale:**
- The CPVT prediction rests on model score alone. There are no trials, the literature shows no benefit, and guidelines favour beta-blockers, flecainide and sympathetic denervation over amiodarone.
- Among the other top predictions, ventricular tachycardia (L1, Proceed with Guardrails) is well supported by completed Phase 3 trials (AVID, ALPS) and Phase 4 comparisons, but this is essentially an established use. Incessant infant ventricular tachycardia (L2) is a research question, supported mainly by evidence from mixed, largely supraventricular tachyarrhythmias. Ranks 4-10 should be held, since none has a plausible mechanism.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- For CPVT: any comparative or mechanistic data against flecainide and beta-blockers; otherwise deprioritize
- For infant ventricular tachycardia: VT-specific pediatric data and a monitoring plan for thyroid, hemodynamic and proarrhythmic toxicity
- For ventricular tachycardia: a monitoring plan for pulmonary, thyroid, hepatic and ocular toxicity and QT prolongation, plus a drug-interaction management strategy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

