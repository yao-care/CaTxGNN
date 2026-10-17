---
layout: default
title: Aminophylline
parent: Moderate Evidence (L3-L4)
nav_order: 51
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Aminophylline: predicted new indication Migraine disorder (evidence level L4). Approved use: Not specified in the Canadian licence data"
monitor_inn: "Aminophylline"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "migraine with or without aura, susceptibility to", "atrophoderma vermiculata", "ulerythema ophryogenesis", "Prinzmetal angina", "pulmonary hypertension", "sciatic neuropathy", "hyperthyroidism", "kyphoscoliotic heart disease"]
---

# Aminophylline
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

# Aminophylline: From an Unspecified Original Indication to Migraine Disorder

## One-Sentence Summary

Aminophylline is a methylxanthine drug (an adenosine receptor antagonist and phosphodiesterase inhibitor) that is currently marketed in Canada as an injectable. The TxGNN model predicts it may be effective for **migraine disorder**, but there are **no registered clinical trials** and only **4 publications** (one narrative review, the rest case reports or older articles), so this remains a research question rather than a validated direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the Canadian licence data |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the data compiled for this report. Based on general pharmacology, aminophylline is a non-selective adenosine receptor antagonist and phosphodiesterase inhibitor. It is widely known for bronchodilation and smooth muscle relaxation.

Adenosine signalling has been implicated in migraine and trigeminovascular activation. A 2023 narrative review (PMID 38059379) argues that migraine may involve impaired brain energy metabolism with high adenosine levels, and that aminophylline may relieve pain, particularly post-dural headache. A case report of hemiplegic migraine triggered by regadenoson (an adenosine A2A agonist) indirectly supports the adenosine link.

This reasoning is mechanistic inference. No trial has tested aminophylline in migraine, and the supporting literature consists of a narrative article and case reports.

**Other predicted indications (for context):**

| Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|
| Migraine with brainstem aura | 99.84% | L5 | No specific evidence; extrapolated from general migraine |
| Migraine with or without aura, susceptibility to | 99.82% | L4 | Same migraine papers; adds no independent evidence |
| Atrophoderma vermiculata | 99.60% | L5 | No plausible mechanistic link |
| Ulerythema ophryogenesis | 99.50% | L5 | No plausible mechanistic link |
| Prinzmetal angina | 99.33% | L4 | Evidence suggests a safety signal (coronary vasospasm), not benefit |
| Pulmonary hypertension | 99.23% | L3 | Small, old haemodynamic studies and one Phase 1 safety trial |
| Sciatic neuropathy | 99.07% | L4 | One indirect preclinical paper |
| Hyperthyroidism | 99.06% | L4 | Literature concerns interactions; potentially harmful |
| Kyphoscoliotic heart disease | 99.01% | L5 | Prediction only |

Among these, pulmonary hypertension has the most developed evidence base, though it is still modest.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for migraine disorder.

For reference, the only registered trial found among the other predicted indications was for pulmonary hypertension:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01530464](https://clinicaltrials.gov/study/NCT01530464) | Phase 1 | Completed | 18 | Safety, tolerability and pharmacokinetics of oral aminophylline and ambrisentan, alone and combined, in healthy volunteers. Safety study only; no efficacy measured. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38059379](https://pubmed.ncbi.nlm.nih.gov/38059379/) | 2023 | Review | Pain Management | Proposes migraine is linked to impaired brain energy metabolism and high adenosine; discusses aminophylline as an adenosine antagonist with therapeutic relief in pain, especially post-dural headache |
| [34308528](https://pubmed.ncbi.nlm.nih.gov/34308528/) | 2022 | Case report | J Nucl Cardiol | Hemiplegic migraine triggered by regadenoson (A2A agonist); methylxanthines such as aminophylline reverse its adverse effects |
| [7728647](https://pubmed.ncbi.nlm.nih.gov/7728647/) | 1995 | Case report | Can J Cardiol | Syndrome X patient with an excessive adenosine effect ("myocardial migraine" without ischaemia) |
| [14168418](https://pubmed.ncbi.nlm.nih.gov/14168418/) | 1964 | Review | Aggiornamenti Clinicoterapeutici | Historical article on medical headaches; no abstract available |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00582662 | AMINOPHYLLINE INJ 25MG/ML | Injection (form not recorded) | Not recorded in licence data |

---

## Safety Considerations

- **Drug Interactions:** An interaction screen returned 100 potential interactions. The sample reviewed includes:
  - **Major:** Bupropion
  - **Moderate:** Famotidine, ranitidine, cimetidine, nizatidine, doxycycline, tetracycline, minocycline, clarithromycin, hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide, obeticholic acid, metreleptin, and several bowel-preparation products (picosulfuric acid, sodium sulfate, polyethylene glycol with electrolytes)
  - **Minor:** Lansoprazole
- **Signals from the literature (other predicted indications):**
  - Aminophylline termination of dipyridamole stress triggered coronary vasospasm in variant angina patients.
  - Aminophylline increased tremor in hyperthyroid patients, and as a stimulant it may worsen tachycardia in thyrotoxicosis.

Please refer to the package insert for warnings and contraindications, as this information was not available in the compiled data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The migraine prediction has a high model score (99.88%) and a plausible adenosine-antagonism rationale, but the evidence is limited to a narrative review, case reports and mechanistic inference, with no registered trials. The Canadian licence record also lacks indication and safety text, so safety screening cannot yet proceed.

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications, approved indications, dosage form) for DIN 00582662
- Detailed mechanism of action data
- A systematic literature review specific to aminophylline in migraine and post-dural puncture headache
- A well-designed controlled trial (or at least a prospective pilot) for migraine
- A cardiovascular and drug-interaction risk plan, given the major interaction with bupropion and the vasospasm and tachycardia signals
- Separately, if pulmonary hypertension is pursued, controlled efficacy data beyond the small, older haemodynamic studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

