---
layout: default
title: Epinephrine
parent: Model Prediction Only (L5)
nav_order: 336
evidence_level: L5
indication_count: 4
---

# Epinephrine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Epinephrine: From Asthma and Anaphylaxis to Obstructive Lung Disease

## One-Sentence Summary

Epinephrine is a non-selective adrenergic agonist originally used for asthma, bronchitis, anaphylaxis, hypotensive disorder, open-angle glaucoma, pulmonary emphysema and bronchiectasis.
The TxGNN model predicts it may be effective for **obstructive lung disease**, with **15 clinical trials** and **20 publications** currently supporting this direction.
This is largely an extension or reclassification of existing uses rather than a true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma, bronchitis, anaphylaxis, hypotensive disorder, open-angle glaucoma, pulmonary emphysema, bronchiectasis (approved indication text is not available in the Canadian licence records) |
| Predicted New Indication | Obstructive lung disease |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L1 (3 completed Phase 3 trials in asthma, though two are small paediatric studies and one is a safety extension) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Epinephrine is a non-selective adrenergic agonist. Stimulating beta-2 receptors relaxes bronchial smooth muscle and causes bronchodilation. Stimulating alpha-1 receptors constricts blood vessels and reduces mucosal swelling in the airway. Detailed mechanism-of-action data was not available in the data compiled for this report, so this description is based on the established pharmacology of the drug.

Obstructive lung disease is the umbrella category that includes asthma, chronic obstructive pulmonary disease (COPD), bronchitis and bronchiectasis. Epinephrine is already associated with asthma, bronchitis and bronchiectasis, so this prediction mostly restates or broadens existing uses.

Bronchiolitis in infants is a separate sub-question. The trial and literature results there are less consistent, and the reviews describe the benefit as modest and uncertain.

## Clinical Trial Evidence

Fifteen trials were retrieved; the 10 most relevant are listed below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01357642](https://clinicaltrials.gov/study/NCT01357642) | Phase 3 | Completed | 373 | 12-week efficacy and safety of epinephrine HFA inhalation aerosol versus placebo and Primatene Mist in adolescents and adults with asthma |
| [NCT01476904](https://clinicaltrials.gov/study/NCT01476904) | Phase 3 | Completed | 208 | 3-month safety extension of the above study, giving a 6-month safety profile of inhaled epinephrine versus placebo |
| [NCT01460511](https://clinicaltrials.gov/study/NCT01460511) | Phase 3 | Completed | 70 | 4-week placebo-controlled study of E004 inhaled epinephrine in children aged 4-11 with asthma |
| [NCT01737905](https://clinicaltrials.gov/study/NCT01737905) | Phase 3 | Completed | 28 | Single-dose crossover study of E004 in children with asthma; very small sample |
| [NCT01705964](https://clinicaltrials.gov/study/NCT01705964) | Phase 4 | Completed | 49 | Intramuscular epinephrine as an add-on to inhaled beta-2 agonists in severe paediatric asthma exacerbation |
| [NCT04207840](https://clinicaltrials.gov/study/NCT04207840) | Phase 4 | Completed | 28 | Systemic exposure of Primatene Mist versus intramuscular epinephrine and ProAir in healthy adults (pharmacokinetic and safety study) |
| [NCT01834820](https://clinicaltrials.gov/study/NCT01834820) | Phase 4 | Completed | 120 | Epinephrine, dexamethasone and hypertonic saline in children with bronchiolitis (pilot) |
| [NCT00817466](https://clinicaltrials.gov/study/NCT00817466) | Phase 4 | Unknown | 500 | Optimal inhalation treatment for infants aged 0-12 months with acute bronchiolitis |
| [NCT01255709](https://clinicaltrials.gov/study/NCT01255709) | Phase 2 | Completed | 24 | Pharmacokinetics of epinephrine inhalation aerosol (E004) in healthy volunteers |
| [NCT01276821](https://clinicaltrials.gov/study/NCT01276821) | Phase 4 | Completed | 100 | Nebulised 3% hypertonic saline in bronchiolitis; epinephrine is not the central intervention |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35093318](https://pubmed.ncbi.nlm.nih.gov/35093318/) | 2022 | RCT | The Journal of Pediatrics | Corticosteroids plus nebulised epinephrine versus standard care for children with bronchiolitis in intensive care, measuring duration of positive pressure support |
| [21678340](https://pubmed.ncbi.nlm.nih.gov/21678340/) | 2011 | Systematic review (Cochrane) | Cochrane Database of Systematic Reviews | Epinephrine for bronchiolitis; bronchodilators are widely used despite uncertain effectiveness |
| [14974006](https://pubmed.ncbi.nlm.nih.gov/14974006/) | 2004 | Systematic review (Cochrane) | Cochrane Database of Systematic Reviews | Earlier Cochrane review of epinephrine in bronchiolitis |
| [33893229](https://pubmed.ncbi.nlm.nih.gov/33893229/) | 2021 | Network meta-analysis | Pediatrics | Comparative efficacy of bronchiolitis interventions in acute care |
| [35953216](https://pubmed.ncbi.nlm.nih.gov/35953216/) | 2022 | Review | Emerg Med Clin North Am | Emergency department evaluation and management of asthma and COPD exacerbations |
| [30488718](https://pubmed.ncbi.nlm.nih.gov/30488718/) | 2019 | Review | Expert Rev Respir Med | Role of racemic epinephrine, corticosteroids, hypertonic saline and high-flow oxygen in infant bronchiolitis |
| [21157348](https://pubmed.ncbi.nlm.nih.gov/21157348/) | 2011 | Review | Curr Opin Pediatr | None of the bronchiolitis treatments has been conclusively shown to change the course of the disease |
| [23393929](https://pubmed.ncbi.nlm.nih.gov/23393929/) | 2012 | Review | Duodecim | Bronchiolitis overview; racemic epinephrine inhalation is mentioned as an option when required |
| [20876171](https://pubmed.ncbi.nlm.nih.gov/20876171/) | 2010 | Cost-effectiveness analysis | Pediatrics | Cost-effectiveness of epinephrine and dexamethasone in bronchiolitis, using Canadian trial data |
| [30856157](https://pubmed.ncbi.nlm.nih.gov/30856157/) | 2019 | News/commentary | Med Lett Drugs Ther | Return of over-the-counter Primatene Mist |

## Canada Market Information

Twenty single-ingredient licences are valid. Dosage form and approved indication text are not recorded for these licences. Five of the main authorizations are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00578657 | EPIPEN JR | Not available | Not available |
| 00509558 | EPIPEN | Not available | Not available |
| 02458454 | EMERADE | Not available | Not available |
| 02435810 | EPINEPHRINE INJECTION USP | Not available | Not available |
| 00155365 | ADRENALIN TOPICAL SOLUTION | Not available | Not available |

The remaining licences include other epinephrine injections, ADRENALIN, and several dental or local anaesthetic products combining lidocaine with epinephrine.

## Safety Considerations

- **Contraindications suggested by the knowledge graph (not label text):** hypertension, coronary artery disease, myocardial infarction, atrial fibrillation, heart conduction disease, sudden cardiac arrest, cardiovascular and heart disease, hyperthyroidism, diabetes mellitus, diabetic ketoacidosis, angle-closure glaucoma, epilepsy, liver and kidney disease, benign prostatic hyperplasia, myasthenia gravis and respiratory failure. These flags need confirmation against the official labelling.
- **Drug Interactions:** 100 interactions were found. Those listed include the following.
  - Major: amitriptyline, amoxapine.
  - Moderate: beta-blockers (acebutolol, atenolol, betaxolol), other beta-agonists (formoterol, salbutamol, arformoterol), stimulants (methylphenidate, amphetamine, atomoxetine, benzphetamine), antidiabetic drugs (acarbose, acetohexamide, albiglutide, alogliptin), and antipsychotics (amisulpride, aripiprazole, asenapine).

Package insert warnings and contraindications from Health Canada were not available, so please refer to the package insert for authoritative safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Several completed Phase 3 trials of inhaled epinephrine in asthma support the obstructive lung disease direction, and the drug is already marketed in Canada with 20 valid licences. However, the prediction largely overlaps with existing indications, the Phase 3 trials are mostly small or paediatric, and the bronchiolitis evidence is inconsistent.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data
- Confirmation of which Canadian products carry respiratory indications, and by which route; the inhaled formulations studied in the trials are not identified among the listed licences
- A cardiovascular and metabolic safety monitoring plan, given the knowledge-graph contraindication flags and the major interactions with tricyclic antidepressants

**Other predicted indications (not recommended for advancement at this stage):**
- Food-dependent exercise-induced anaphylaxis: L4, a subtype extension of the existing anaphylaxis indication supported by reviews only, with no dedicated trials. Treat as a research question.
- Respiratory malformation: L3, Hold. The only trial concerns transient tachypnoea of the newborn, a functional condition, and the retrieved literature is largely off-topic.
- Rienhoff syndrome: L5, Hold. There are no trials or literature, and the prediction is likely a knowledge-graph artefact.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

