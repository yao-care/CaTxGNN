---
layout: default
title: Perampanel
parent: Moderate Evidence (L3-L4)
nav_order: 715
evidence_level: L3
indication_count: 10
---

# Perampanel
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

# Perampanel: From Epilepsy (Focal and Generalized Tonic-Clonic Seizures) to Visual Epilepsy

## One-Sentence Summary

Perampanel is an oral anti-seizure medication, marketed for focal-onset seizures and generalized tonic-clonic seizures.
The TxGNN model predicts it may be effective for **visual epilepsy** (visually triggered seizures), with **3 clinical trials** and **20 publications** retrieved.
None of these studies specifically examines visually triggered seizures, so the evidence is indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy: focal-onset seizures and primary generalized tonic-clonic seizures (taken from the published literature; the Canadian indication text was not supplied) |
| Predicted New Indication | Visual epilepsy |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 12 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Perampanel is a selective, non-competitive antagonist of the AMPA-type glutamate receptor. It reduces glutamate-mediated excitation at postsynaptic membranes and was the first approved antiepileptic drug with this mechanism. A structured mechanism-of-action field was not available in the Evidence Pack, so this description comes from the supplied literature.

Visual epilepsy, meaning seizures triggered by visual stimuli such as photosensitive epilepsy, is a seizure subtype within epilepsy, not a new disease area. Excessive glutamatergic excitation underlies seizure generation in general, so blocking AMPA receptors is plausible here. Perampanel also reduced seizures in rodent models of reflex seizures, such as audiogenic seizures in genetically epilepsy-prone rats.

The model score is very high, but no retrieved trial or paper confirms that a visually triggered or photosensitive population was treated. The prediction is therefore best read as a research question, not a demonstrated effect.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03780907](https://clinicaltrials.gov/study/NCT03780907) | Phase 2 | Completed | 18 | Randomised, double-blind, placebo-controlled study of tolerability, safety and PK of perampanel (E2007) in refractory partial or generalised seizures. Whether it enrolled a visually triggered population is unconfirmed. |
| [NCT03653741](https://clinicaltrials.gov/study/NCT03653741) | Phase 4 | Completed | 12 | Effects of perampanel on EEG and evoked potentials (SEP, BAEP, VEP) in healthy volunteers. Pharmacodynamic only, with no seizure-efficacy endpoint. |
| [NCT02900755](https://clinicaltrials.gov/study/NCT02900755) | Phase 4 | Completed | 30 | Effects of perampanel on cognition and EEG in epilepsy patients. Provides safety and EEG context, not efficacy in this seizure type. |

---

## Literature Evidence

None of the 20 retrieved papers addresses visually triggered seizures. The table lists the 10 most relevant general perampanel and epilepsy papers.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36206645](https://pubmed.ncbi.nlm.nih.gov/36206645/) | 2022 | Systematic review / meta-analysis of RCTs | Seizure | Efficacy and safety of perampanel in epilepsy across randomised trials |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Systematic review / network meta-analysis | J Neurol | Compares anti-seizure medications for idiopathic generalized epilepsies |
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Guideline | Neurology | AAN/AES guideline update on newer antiepileptic drugs in new-onset epilepsy |
| [36878742](https://pubmed.ncbi.nlm.nih.gov/36878742/) | 2023 | Systematic review / meta-analysis | Brain Dev | Efficacy, tolerability and safety of perampanel in children and adolescents |
| [36150304](https://pubmed.ncbi.nlm.nih.gov/36150304/) | 2022 | Review | Epilepsy Behav | Perampanel monotherapy for epilepsy: clinical trial and real-world evidence |
| [25878177](https://pubmed.ncbi.nlm.nih.gov/25878177/) | 2015 | Pooled analysis of Phase 3 trials | Neurology | Impact of enzyme-inducing antiepileptic drugs on perampanel efficacy and safety |
| [36034267](https://pubmed.ncbi.nlm.nih.gov/36034267/) | 2022 | Cohort | Front Neurol | Real-life effectiveness and tolerability of perampanel in childhood absence epilepsy |
| [37329172](https://pubmed.ncbi.nlm.nih.gov/37329172/) | 2023 | Cohort | Ann Clin Transl Neurol | Perampanel outcomes in paediatric epilepsy with known or presumed genetic etiology |
| [41043235](https://pubmed.ncbi.nlm.nih.gov/41043235/) | 2025 | Prospective multicenter study | Epilepsy Behav | Effects of perampanel on seizures and sleep quality |
| [24559052](https://pubmed.ncbi.nlm.nih.gov/24559052/) | 2014 | Review | Expert Opin Drug Discov | Discovery and development of perampanel as an AMPA antagonist |

---

## Canada Market Information

Dosage form, manufacturer and approved-indication text were not supplied for these licences. The five main authorizations (of 12 DINs) are:

| DIN | Product Name |
|---------|------|
| 2404532 | FYCOMPA |
| 2404524 | FYCOMPA |
| 2522632 | TARO-PERAMPANEL |
| 2522667 | TARO-PERAMPANEL |
| 2522675 | TARO-PERAMPANEL |

---

## Safety Considerations

Drug interaction searches returned no records. Irritability is described in the literature as a frequent adverse event with perampanel (PMID 30675751). A single case report also describes new-onset food aversion (PMID 30842918).

Please refer to the Health Canada product monograph for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Perampanel is well established in epilepsy, and AMPA antagonism is a plausible fit for visually triggered seizures. However, no retrieved trial or paper treats a visually triggered or photosensitive population, and the Canadian safety documentation is missing. The evidence supports a research question, not a development decision.

**To proceed, the following is needed:**
- The Health Canada product monograph (indications, warnings, contraindications)
- Confirmation of the enrolled population in NCT03780907, and a search for photosensitive or reflex-seizure data specific to perampanel
- Structured mechanism-of-action data from DrugBank
- A targeted study design in photosensitive or visually triggered epilepsy if the above is promising

**Related prediction:** Status epilepticus (rank 10, score 99.77%) has more direct evidence than visual epilepsy. It has a recruiting randomised Phase 2 prophylaxis trial ([NCT06401707](https://clinicaltrials.gov/study/NCT06401707)), systematic reviews and retrospective cohorts. It remains at the research-question stage because the available data come from uncontrolled series and two terminated trials that enrolled one patient each.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

