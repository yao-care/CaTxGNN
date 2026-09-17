---
layout: default
title: Nitric Oxide
parent: High Evidence (L1-L2)
nav_order: 554
evidence_level: L1
indication_count: 10
---

# Nitric Oxide
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Nitric Oxide: From an Undocumented Original Indication to Pulmonary Arterial Hypertension Associated with Congenital Heart Disease

## One-Sentence Summary

Nitric Oxide (DrugBank DB00435) has no original indication or DrugBank mechanism-of-action data recorded in the current evidence pack. TxGNN generated 10 candidate indications for this drug; most (including the single top-ranked hit) show no real mechanistic support and are flagged internally as **noise**, but one candidate — **Pulmonary Arterial Hypertension Associated with Congenital Heart Disease (PAH-CHD)** — stands out with the strongest evidence in the set (**14 clinical trials**, **20 publications**, evidence level **L1**). This report focuses on that candidate as the clinically meaningful signal.

> **Note on candidate selection**: The evidence pack ranks 10 TxGNN predictions by raw model score. Scores alone are not informative here — ranks 1–5 (score 0.9949–0.9957) are annotated by the evidence-review process as knowledge-graph noise with no mechanistic basis ("Hold," evidence level L5). PAH-CHD (rank 8, score 0.9941) is the only candidate reaching evidence level L1 with an advanced decision stage (S3) and a "Proceed with Guardrails" recommendation, so it is presented below in place of the raw rank-1 result.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the current dataset |
| Predicted New Indication | Pulmonary Arterial Hypertension Associated with Congenital Heart Disease |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L1 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for Nitric Oxide is not available in DrugBank, and no original approved indication is recorded in this dataset. Based on the evidence collected for this candidate, Nitric Oxide (NO) is an endogenous pulmonary vasodilator produced via the endothelial NO synthase (eNOS) pathway. Patients with pulmonary arterial hypertension associated with congenital heart disease (PAH-CHD) frequently show impaired endothelial NO synthesis and reduced NO bioavailability, which contributes to pulmonary vascular remodeling and elevated pulmonary vascular resistance.

Inhaled nitric oxide (iNO) directly supplies the deficient signaling molecule at the site of disease. This is not a distant mechanistic analogy — iNO is already used clinically as a selective pulmonary vasodilator in acute settings closely related to PAH-CHD, including postoperative pulmonary hypertension after congenital cardiac surgery and persistent pulmonary hypertension of the newborn (PPHN), a condition frequently comorbid with congenital heart disease. The mechanistic link here is direct and well-characterized, which is why this candidate reaches evidence level L1 while most of the other TxGNN-predicted indications for this drug (hypertrichosis, periodontal malformation syndromes, Dandy-Walker malformation, hair shaft abnormalities) show no plausible NO-related biology at all.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01959828](https://clinicaltrials.gov/study/NCT01959828) | Phase 3 | Completed | 18 | IK-3001 (inhaled NO) safety/efficacy in Japanese patients with pulmonary hypertension after cardiac surgery — most direct evidence for this drug/indication pair |
| [NCT00955487](https://clinicaltrials.gov/study/NCT00955487) | Phase 2 | Completed | 124 | Low-dose iNO in premature newborns to reduce bronchopulmonary dysplasia and associated pulmonary hypertension |
| [NCT00023296](https://clinicaltrials.gov/study/NCT00023296) | Phase 1 | Completed | 59 | iNO plus transfusion therapy for pulmonary hypertension secondary to sickle cell anemia |
| [NCT01383083](https://clinicaltrials.gov/study/NCT01383083) | N/A | Unknown | 42 | Iloprost (non-NO comparator pathway) in adults with CHD-related PAH (Eisenmenger physiology) — mechanistically adjacent |
| [NCT02261883](https://clinicaltrials.gov/study/NCT02261883) | Phase 2 | Terminated | 42 | IV treprostinil as add-on therapy for persistent pulmonary hypertension of the newborn |
| [NCT02951130](https://clinicaltrials.gov/study/NCT02951130) | Phase 2 | Completed | 66 | Milrinone in congenital diaphragmatic hernia with PPHN resistant to conventional iNO therapy |
| [NCT03177603](https://clinicaltrials.gov/study/NCT03177603) | Phase 2 | Completed | 23 | Recombinant human ACE2 (GSK2586881) safety/PK in PAH patients |
| [NCT07356778](https://clinicaltrials.gov/study/NCT07356778) | Phase 4 | Recruiting | 36 | Sotatercept add-on for PAH due to unrepaired congenital shunts, including Eisenmenger syndrome |
| [NCT05201144](https://clinicaltrials.gov/study/NCT05201144) | Phase 2 | Recruiting | 40 | Sildenafil (PDE5 inhibitor, NO-pathway potentiator) for postoperative PH in congenital diaphragmatic hernia |
| [NCT00352430](https://clinicaltrials.gov/study/NCT00352430) | Phase 1 | Completed | 31 | NO-based therapy assessment in hemolysis-associated pulmonary hypertension |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18333354](https://pubmed.ncbi.nlm.nih.gov/18333354/) | 2007 | Review | Rom J Intern Med | Management review of PAH associated with congenital heart disease |
| [40681972](https://pubmed.ncbi.nlm.nih.gov/40681972/) | 2025 | Cohort/Clinical trial | BMC Cardiovasc Disord | Novel electrochemical NO generator for postoperative PAH after congenital cardiac surgery in China |
| [18041423](https://pubmed.ncbi.nlm.nih.gov/18041423/) | 2007 | Cohort | J Med Assoc Thai | Plasma NO levels measured in children with CHD and increased pulmonary blood flow |
| [35699093](https://pubmed.ncbi.nlm.nih.gov/35699093/) | 2022 | Genetic association | Clin Exp Hypertens | eNOS gene polymorphisms linked to PAH risk in newborns with CHD |
| [33555425](https://pubmed.ncbi.nlm.nih.gov/33555425/) | 2021 | Cohort | Eur J Pediatr | Perioperative endogenous H2S and NO levels as prognostic markers in CHD-PAH children |
| [24689825](https://pubmed.ncbi.nlm.nih.gov/24689825/) | 2014 | Clinical review | Pediatr Int | Clinical characteristics of PAH associated with Down syndrome (a CHD-enriched population) |
| [20143207](https://pubmed.ncbi.nlm.nih.gov/20143207/) | 2010 | Review | World J Pediatr | Advances in diagnosis/treatment of PAH in neonates and children with CHD |
| [22526220](https://pubmed.ncbi.nlm.nih.gov/22526220/) | 2012 | Cohort | Pediatr Cardiol | Elevated homocysteine and ADMA (NO-pathway inhibitor) levels in PH-CHD |
| [28608969](https://pubmed.ncbi.nlm.nih.gov/28608969/) | 2017 | Cohort | Clin Exp Pharmacol Physiol | Effect of iloprost on NO-pathway biomarkers in CHD-PAH |
| [16919006](https://pubmed.ncbi.nlm.nih.gov/16919006/) | 2006 | Review | Eur J Clin Invest | Treatment options in children with PAH, including experience with oral bosentan |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Among the 10 TxGNN-predicted indications for Nitric Oxide, only PAH-CHD reaches evidence level L1 with a completed Phase 3 trial (IK-3001) and a coherent, direct mechanistic rationale (NO deficiency in pulmonary endothelium). Inhaled NO is already used off-label/adjacently in related acute pulmonary-hypertension settings (post-cardiac-surgery PH, PPHN), supporting biological plausibility, but dedicated long-term efficacy/safety data specifically in chronic CHD-PAH populations remain limited.

**To proceed, the following is needed:**
- TFDA/Health Canada label warnings and contraindications for Nitric Oxide (currently a blocking data gap — safety review cannot proceed without this)
- Formal DrugBank mechanism-of-action confirmation
- Original approved indication documentation (currently absent from regulatory data)
- Dosing/route feasibility assessment for chronic vs. acute inhaled administration in CHD-PAH
- Given the drug is currently unmarketed in this jurisdiction (0 DINs on record), a market-access and import pathway review is also required before clinical use can be considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

