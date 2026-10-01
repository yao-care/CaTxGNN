---
layout: default
title: Lamotrigine
parent: Model Prediction Only (L5)
nav_order: 515
evidence_level: L5
indication_count: 9
---

# Lamotrigine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Lamotrigine: From Epilepsy and Bipolar Disorder to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Lamotrigine is a broad-spectrum anticonvulsant used for seizure and bipolar mood disorders. The TxGNN model's top-ranked prediction is **trigeminal nerve neoplasm**, but there are **0 clinical trials** and only **2 loosely related publications** (neither mentions lamotrigine), so this prediction is not supported by evidence. The related prediction **trigeminal neuralgia** (rank 2) has the strongest evidence of all eight predictions.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy and bipolar disorder (taken from literature; the Health Canada licence records in the pack contain no indication text) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Literature describes lamotrigine as a sodium-channel blocker that reduces glutamate release. Its efficacy in seizure disorders is established.

The high score for trigeminal nerve neoplasm most likely reflects a graph neighbourhood shared with **trigeminal neuralgia**, the facial pain syndrome that lamotrigine's sodium-channel blockade can plausibly dampen. Neuralgia can be a symptom of a tumour, but nothing in the evidence suggests lamotrigine acts against the neoplasm itself. Any benefit would be symptomatic pain control, not anti-tumour activity. The prediction is better read as a pointer to trigeminal neuralgia than as a true oncology candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for trigeminal nerve neoplasm.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurother | Overview of medical and surgical treatments for trigeminal neuralgia; does not address tumours or lamotrigine |
| [30650431](https://pubmed.ncbi.nlm.nih.gov/30650431/) | 2018 | Case report | Stereotact Funct Neurosurg | Gamma Knife radiosurgery for trigeminal neuralgia caused by a brainstem cavernous malformation; not a neoplasm, no lamotrigine |

---

## Other Predicted Indications

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision |
|------|------|------|------|------|
| 2 | Trigeminal neuralgia | 99.89% | L2 | Proceed with Guardrails |
| 3 | Startle epilepsy | 99.38% | L4 | Research Question |
| 4 | Micturition-induced seizures | 99.38% | L4 | Hold |
| 5 | Thinking seizures | 99.38% | L4 | Hold |
| 6 | Audiogenic seizures | 99.38% | L4 | Hold |
| 7 | Orgasm-induced seizures | 99.38% | L5 | Hold |
| 8 | Eating seizures | 99.38% | L5 | Hold |
| 9 | Reading seizures | 99.29% | L4 | Hold |

**Trigeminal neuralgia is the lead candidate.** Its trials (lamotrigine-specific ones listed below) are:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00913107](https://clinicaltrials.gov/study/NCT00913107) | Phase 2/3 | Completed | 21 | Lamotrigine vs carbamazepine for efficacy and safety; too small to support Phase 3-level conclusions |
| [NCT00203229](https://clinicaltrials.gov/study/NCT00203229) | Not labelled | Completed | 20 | Double-blind, placebo-controlled add-on study of Lamictal (indication inferred from its listing under trigeminal neuralgia) |
| [NCT00243152](https://clinicaltrials.gov/study/NCT00243152) | N/A | Completed | 6 | fMRI study of lamotrigine in neuropathic facial pain; exploratory, not an efficacy trial |

Supporting literature includes a published comparison of lamotrigine and carbamazepine ([21621166](https://pubmed.ncbi.nlm.nih.gov/21621166/), 2011), a case of refractory trigeminal neuralgia in multiple sclerosis controlled with pregabalin plus lamotrigine ([30081317](https://pubmed.ncbi.nlm.nih.gov/30081317/), 2018), and the EAN guideline ([30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/), 2019). The guideline's position on lamotrigine has not been verified and should be checked before any recommendation.

The seizure-related predictions (rows 3 to 9) are supported mainly by small case series for startle-induced seizures ([21896426](https://pubmed.ncbi.nlm.nih.gov/21896426/), [10512780](https://pubmed.ncbi.nlm.nih.gov/10512780/)), animal models for audiogenic seizures, and generic epilepsy literature.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2381370 | AURO-LAMOTRIGINE |
| 2243803 | LAMICTAL |
| 2302993 | LAMOTRIGINE-150 |
| 2302969 | LAMOTRIGINE-25 |
| 2245210 | APO-LAMOTRIGINE |

Showing 5 of 20 authorizations.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, trigeminal nerve neoplasm, rests on the model score alone: there are no trials, and neither linked paper evaluates lamotrigine. The trigeminal neuralgia prediction is credible but is a separate indication that should be evaluated on its own.

**To proceed, the following is needed:**
- Re-evaluate the programme around trigeminal neuralgia (rank 2) rather than the neoplasm
- Verify the EAN guideline's position on lamotrigine for trigeminal neuralgia
- Mechanism of action data (MOA)
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text for the Canadian licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

