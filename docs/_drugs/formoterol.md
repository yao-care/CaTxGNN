---
layout: default
title: Formoterol
parent: Model Prediction Only (L5)
nav_order: 410
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Formoterol: predicted new indication Respiratory malformation (evidence level L5). Approved use: Pulmonary emphysema, intrinsic asthma, allergic asthma"
monitor_inn: "Formoterol"
predicted_indications: ["respiratory malformation", "bronchitis", "Rienhoff syndrome"]
---

# Formoterol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Formoterol: From Asthma and Emphysema to Respiratory Malformation

## One-Sentence Summary

Formoterol is a long-acting beta2-adrenergic agonist, originally used for **pulmonary emphysema, intrinsic asthma and allergic asthma**.
The TxGNN model's top-ranked prediction is **respiratory malformation**, but it has **no clinical trials** and only **9 loosely related publications** supporting it. The prediction looks like a graph-proximity artifact. The best-supported prediction is **obstructive lung disease** (about 30 registered trials and 20 publications), and that is essentially an existing use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary emphysema, intrinsic asthma, allergic asthma (the Canadian licence records list no indication text) |
| Predicted New Indication | Respiratory malformation (rank 1) |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

Other predictions, for comparison:

| Predicted Indication | Score | Evidence Level | Decision |
|------|------|------|------|
| Bronchitis | 99.92% | L1 | Research question (largely overlaps COPD use) |
| Rienhoff syndrome | 99.90% | L5 | Hold |
| Obstructive lung disease | 99.90% | L1 | Proceed with Guardrails |
| Asthma | 99.74% | L1 | Proceed with Guardrails (existing indication) |
| Asthma-related traits, susceptibility to | 99.50% | L5 | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Formoterol is a well-known long-acting beta2-adrenergic agonist that relaxes bronchial smooth muscle and improves airflow. Its efficacy in asthma and COPD is well established.

**For respiratory malformation, the prediction is not mechanistically plausible.** Bronchodilation does not correct structural congenital abnormalities. The high score (0.999) most likely reflects the disease's closeness to other respiratory conditions in the knowledge graph. The retrieved publications cover COPD, asthma, Down syndrome cognition and post-COVID small airway disease. None addresses congenital respiratory malformation.

**Predictions with a sound mechanistic basis:**
- **Obstructive lung disease and bronchitis:** Airflow obstruction in the COPD spectrum responds to beta2 agonism. Large Phase 3 programmes support this, but it matches formoterol's established COPD use, so it is not novel repurposing.
- **Asthma:** This is an original indication, so the prediction confirms existing use.

## Clinical Trial Evidence

Respiratory malformation (the top-ranked prediction): currently no related clinical trials registered.

The strongest trials come from the obstructive lung disease prediction (bronchitis and asthma overlap with these):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04320342](https://clinicaltrials.gov/study/NCT04320342) | Phase 3 | Completed | 3406 | 52-week trial of beclomethasone/formoterol/glycopyrronium triple therapy vs. beclomethasone/formoterol in COPD |
| [NCT01462942](https://clinicaltrials.gov/study/NCT01462942) | Phase 3 | Completed | 2443 | Aclidinium/formoterol fixed-dose combinations vs. components and placebo in stable COPD |
| [NCT01437397](https://clinicaltrials.gov/study/NCT01437397) | Phase 3 | Completed | 1692 | 24-week aclidinium/formoterol combination study in stable COPD |
| [NCT03022097](https://clinicaltrials.gov/study/NCT03022097) | Phase 3 | Completed | 1625 | 24-week aclidinium/formoterol vs. components and placebo in COPD |
| [NCT03162055](https://clinicaltrials.gov/study/NCT03162055) | Phase 3 | Completed | 1119 | Glycopyrronium/formoterol vs. umeclidinium/vilanterol over 24 weeks in COPD (AERISTO) |
| [NCT00238784](https://clinicaltrials.gov/study/NCT00238784) | Phase 3 | Completed | 1300 | Symbicort single inhaler therapy vs. conventional best practice in persistent asthma |
| [NCT00381485](https://clinicaltrials.gov/study/NCT00381485) | Phase 3 | Completed | 834 | Mometasone/formoterol vs. mometasone alone in persistent asthma |
| [NCT00064415](https://clinicaltrials.gov/study/NCT00064415) | Phase 3 | Completed | 799 | 12-month chronic safety study of (R,R)-formoterol (arformoterol) in COPD |
| [NCT00651651](https://clinicaltrials.gov/study/NCT00651651) | Phase 3 | Completed | 450 | Symbicort vs. its monocomponents in children and adults with asthma |
| [NCT00624754](https://clinicaltrials.gov/study/NCT00624754) | Phase 2 | Completed | 32 | Budesonide/formoterol for bronchiolitis obliterans after stem cell transplant |

## Literature Evidence

Respiratory malformation: the 9 retrieved publications are not on topic (COPD sleep mechanics, asthma reviews, Down syndrome, long COVID, a fungal case report). The most relevant publications come from the obstructive lung disease and asthma predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32579807](https://pubmed.ncbi.nlm.nih.gov/32579807/) | 2020 | RCT | N Engl J Med | Triple therapy at two glucocorticoid doses in moderate-to-very-severe COPD |
| [33252985](https://pubmed.ncbi.nlm.nih.gov/33252985/) | 2021 | RCT | Am J Respir Crit Care Med | ETHOS: reduced all-cause mortality with budesonide/glycopyrrolate/formoterol |
| [30232048](https://pubmed.ncbi.nlm.nih.gov/30232048/) | 2018 | RCT | Lancet Respir Med | KRONOS: triple vs. dual therapy in COPD |
| [29768149](https://pubmed.ncbi.nlm.nih.gov/29768149/) | 2018 | RCT | N Engl J Med | As-needed budesonide-formoterol in mild asthma |
| [29768147](https://pubmed.ncbi.nlm.nih.gov/29768147/) | 2018 | RCT | N Engl J Med | As-needed budesonide-formoterol vs. maintenance budesonide in mild asthma |
| [31112386](https://pubmed.ncbi.nlm.nih.gov/31112386/) | 2019 | RCT | N Engl J Med | Novel START: as-needed budesonide-formoterol in mild asthma |
| [41033330](https://pubmed.ncbi.nlm.nih.gov/41033330/) | 2025 | RCT | Lancet | CARE: budesonide-formoterol vs. salbutamol reliever in children with mild asthma |
| [31015757](https://pubmed.ncbi.nlm.nih.gov/31015757/) | 2019 | Meta-analysis | Int J Chron Obstruct Pulmon Dis | Risks of budesonide/formoterol in stable COPD |
| [33273813](https://pubmed.ncbi.nlm.nih.gov/33273813/) | 2020 | Review | Int J Chron Obstruct Pulmon Dis | Formoterol for COPD |
| [31553802](https://pubmed.ncbi.nlm.nih.gov/31553802/) | 2019 | Systematic review | Cochrane Database Syst Rev | Serious adverse events with inhaled steroids with and without regular formoterol in asthma |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02237224 | OXEZE TURBUHALER | Not listed | Not listed |
| 02237225 | OXEZE TURBUHALER | Not listed | Not listed |
| 02245386 | SYMBICORT 200 TURBUHALER | Not listed | Not listed |
| 02245385 | SYMBICORT 100 TURBUHALER | Not listed | Not listed |
| 02361760 | ZENHALE | Not listed | Not listed |

Three more valid licences exist (ZENHALE, DUAKLIR GENUAIR, BREZTRI AEROSPHERE), making 8 valid single-ingredient licences in total.

## Safety Considerations

- **Drug Interactions:** 100 interactions were found. Examples at moderate level include acarbose, famotidine, canagliflozin, dapagliflozin, empagliflozin, cisapride, clarithromycin, dolasetron, ephedrine and isometheptene. Minor interactions include the corticosteroids beclomethasone, betamethasone, budesonide and dexamethasone.
- **Knowledge-graph contraindication signals** (not label text): hypertension, long QT syndrome, epilepsy, liver disease, gallbladder disease, and various pituitary hormone deficiency conditions.
- **Class considerations from the literature:** LABAs raise cardiovascular and asthma-safety concerns. Formoterol must not be used as monotherapy in asthma and should always be paired with an inhaled corticosteroid.

For full warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, respiratory malformation)

**Rationale:**
- Respiratory malformation has no plausible mechanism, no trials and no relevant literature. Its high score looks like a model artifact.
- The well-supported predictions (obstructive lung disease, bronchitis, asthma) are existing COPD and asthma uses, not novel repurposing. They can **Proceed with Guardrails** if the aim is to confirm or extend labelled use.

**To proceed, the following is needed:**
- Mechanism of action data
- Health Canada package insert warnings and contraindications (flagged as a blocking gap for safety screening)
- Approved indication text, dosage forms and manufacturers for each DIN
- For bronchitis, trial enrollment criteria to separate chronic bronchitis from other forms
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

