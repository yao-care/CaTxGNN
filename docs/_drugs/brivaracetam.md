---
layout: default
title: Brivaracetam
parent: Moderate Evidence (L3-L4)
nav_order: 123
evidence_level: L4
indication_count: 10
---

# Brivaracetam
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Brivaracetam: From Focal-Onset Seizures to Visual Epilepsy

## One-Sentence Summary

Brivaracetam is an antiseizure medication approved for focal-onset seizures.
The TxGNN model predicts it may be effective for **visual epilepsy** (seizures provoked by visual stimuli), but there are currently **0 registered clinical trials** and **19 publications**, all of them general epilepsy literature rather than visual-epilepsy-specific studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Focal-onset seizures (from the literature; Canadian licence indication text was not provided) |
| Predicted New Indication | Visual epilepsy |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 14 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the DrugBank field of the evidence pack. The literature, however, describes brivaracetam as a high-affinity ligand of synaptic vesicle protein 2A (SV2A). It is a propyl analogue of levetiracetam, binds SV2A with roughly 15- to 30-fold higher affinity, and penetrates the brain rapidly. It is approved as adjunctive and monotherapy treatment for focal-onset seizures.

Visual epilepsy involves seizures triggered by visual stimuli. It is a reflex epilepsy in which neuronal hyperexcitability drives the seizures. SV2A modulation reduces this hyperexcitability, so the mechanism could plausibly extend from focal seizures to visually provoked seizures.

The literature retrieved for this indication is general epilepsy material, not visual epilepsy. Two photosensitivity studies, which use the EEG photoparoxysmal response as a biomarker of antiseizure efficacy, appeared under a different predicted indication:
- **PMID 17785672**: brivaracetam in the photosensitivity model (2007).
- **PMID 32949370**: a randomized, double-blind crossover trial of brivaracetam vs levetiracetam on the photoparoxysmal response (2020).

These are not counted in the evidence above. If manual review confirms they are relevant, they could support an upgrade to L2–L3.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the publications below is specific to visual epilepsy. They support brivaracetam's approved use in epilepsy only indirectly.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38576178](https://pubmed.ncbi.nlm.nih.gov/38576178/) | 2024 | RCT (Phase III, focal seizures, indirect) | Epilepsia Open | Adjunctive brivaracetam vs placebo in adult Asian patients with uncontrolled focal-onset seizures |
| [26165169](https://pubmed.ncbi.nlm.nih.gov/26165169/) | 2015 | Meta-analysis | Expert Opin Pharmacother | Efficacy and safety of different brivaracetam doses vs placebo in partial-onset epilepsy |
| [39664134](https://pubmed.ncbi.nlm.nih.gov/39664134/) | 2024 | Systematic review | Cureus | Efficacy, safety and reasons for switching to brivaracetam in adults and children with epilepsy |
| [37483441](https://pubmed.ncbi.nlm.nih.gov/37483441/) | 2023 | Systematic review and meta-analysis | Front Neurol | Safety and efficacy of brivaracetam in childhood epilepsy |
| [40568060](https://pubmed.ncbi.nlm.nih.gov/40568060/) | 2025 | Review | J Epilepsy Res | Pharmacology, efficacy and safety of brivaracetam, combining trial and real-world data |
| [38811492](https://pubmed.ncbi.nlm.nih.gov/38811492/) | 2024 | Review | Adv Ther | Narrative review of the preclinical profile and clinical benefits of brivaracetam |
| [31195850](https://pubmed.ncbi.nlm.nih.gov/31195850/) | 2019 | Review | Expert Rev Neurother | Efficacy and tolerability of brivaracetam in focal epilepsy compared with levetiracetam |
| [31937513](https://pubmed.ncbi.nlm.nih.gov/31937513/) | 2020 | Pooled analysis | Epilepsy Behav | In-depth pooled safety and tolerability analysis of adjunctive brivaracetam for focal seizures |
| [38970892](https://pubmed.ncbi.nlm.nih.gov/38970892/) | 2024 | Pooled retrospective analysis | Epilepsy Behav | EXPERIENCE study: effectiveness and tolerability in older vs younger adults |
| [30530134](https://pubmed.ncbi.nlm.nih.gov/30530134/) | 2019 | Case series | Epilepsy Behav | 25 patients with drug-resistant epilepsy and psychiatric comorbidities |

---

## Canada Market Information

Health Canada lists 14 authorizations. The five main ones are below.

| DIN | Product Name |
|---------|------|
| 02538679 | APO-BRIVARACETAM |
| 02538687 | APO-BRIVARACETAM |
| 02538709 | APO-BRIVARACETAM |
| 02539306 | AURO-BRIVARACETAM |
| 02452960 | BRIVLERA |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 99.51% model score is not backed by visual-epilepsy-specific evidence. There are no registered trials, and the retrieved literature is general epilepsy material, which puts this indication at L4. The mechanism is plausible, but the evidence is indirect.

**To proceed, the following is needed:**
- Manual review of the photosensitivity studies (PMID 17785672 and PMID 32949370) to confirm they are relevant to visual epilepsy. If confirmed, re-grade the evidence at L2–L3.
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening.
- DrugBank mechanism of action data.
- Approved indication text and dosage forms for the Canadian licences.

**Note:** Among the other predicted indications for brivaracetam, **status epilepticus** currently has stronger support. It is graded L3 and has a completed head-to-head trial of intravenous brivaracetam vs levetiracetam in children ([NCT07163572](https://clinicaltrials.gov/study/NCT07163572), n=152, no results provided) plus several systematic reviews. It may be a better first candidate for further evaluation.

*This report is for research reference only and does not constitute medical advice. Predicted indications require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

