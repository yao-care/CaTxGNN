---
layout: default
title: Lamotrigine
parent: High Evidence (L1-L2)
nav_order: 440
evidence_level: L2
indication_count: 9
---

# Lamotrigine
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **9** 
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

# Lamotrigine: From Epilepsy to Trigeminal Neuralgia

## One-Sentence Summary

Lamotrigine is an anticonvulsant (marketed elsewhere as Lamictal) established for the treatment of epilepsy, most notably focal/partial seizures. The TxGNN model predicts it may also be effective for **Trigeminal Neuralgia**, a neuropathic facial pain syndrome, and this is currently supported by **4 clinical trials** (including two completed head-to-head/placebo-controlled studies) and **19 publications**, including a European Academy of Neurology treatment guideline.

*Note: TxGNN's single highest-scoring hit, "trigeminal nerve neoplasm," is flagged in the underlying evidence as a likely knowledge-graph node mismatch (neuralgia vs. neoplasm) with no supporting trials and only tangentially related literature — it is not treated as the lead candidate here. Trigeminal Neuralgia (rank 2) is the clinically actionable prediction and is the subject of this report.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy / partial seizures (anticonvulsant; per clinical trial descriptions in the evidence pack — no formal indication text available) |
| Predicted New Indication | Trigeminal Neuralgia |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action documentation is not available in this evidence pack. Based on the supporting evidence collected, lamotrigine blocks voltage-gated sodium channels and inhibits presynaptic glutamate release, which stabilizes neuronal membranes and suppresses abnormal, repetitive neuronal firing. This is the same core mechanism that underlies its efficacy as an anticonvulsant.

Trigeminal neuralgia is itself driven by aberrant, paroxysmal hyperexcitability of trigeminal ganglion/brainstem neurons — pathophysiology that closely parallels epileptic hyperexcitability. This overlap is why sodium-channel-blocking anticonvulsants such as carbamazepine and oxcarbazepine are already the first-line drugs for trigeminal neuralgia, and why lamotrigine, sharing the same channel-blocking mechanism, is a mechanistically plausible substitute or adjunct — particularly for patients who cannot tolerate carbamazepine/oxcarbazepine.

This is not purely theoretical: lamotrigine is already named in the European Academy of Neurology (EAN) guideline on trigeminal neuralgia as a second-line/adjunctive option, and two completed trials directly compared it against carbamazepine or placebo in trigeminal neuralgia patients, lending real clinical support to the TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00913107](https://clinicaltrials.gov/study/NCT00913107) | Phase 2/3 | Completed | 21 | Head-to-head efficacy and safety comparison of lamotrigine vs. carbamazepine in trigeminal neuralgia |
| [NCT00203229](https://clinicaltrials.gov/study/NCT00203229) | N/A | Completed | 20 | Double-blind, placebo-controlled add-on study of lamotrigine (Lamictal) in trigeminal neuralgia |
| [NCT00243152](https://clinicaltrials.gov/study/NCT00243152) | N/A | Completed | 6 | fMRI study evaluating lamotrigine's effect on neuropathic facial pain/neuralgia |
| [NCT04996199](https://clinicaltrials.gov/study/NCT04996199) | Phase 4 | Unknown | 132 | Carbamazepine vs. oxcarbazepine in trigeminal neuralgia (contextual; no lamotrigine arm) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21621166](https://pubmed.ncbi.nlm.nih.gov/21621166/) | 2011 | Comparative Study | J Chin Med Assoc | Direct evaluation of lamotrigine vs. carbamazepine efficacy/safety in trigeminal neuralgia |
| [30081317](https://pubmed.ncbi.nlm.nih.gov/30081317/) | 2018 | Case Report | Mult Scler Relat Disord | Refractory trigeminal neuralgia successfully treated with pregabalin + lamotrigine combination |
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Guideline | Eur J Neurol | European Academy of Neurology guideline on trigeminal neuralgia management |
| [37892981](https://pubmed.ncbi.nlm.nih.gov/37892981/) | 2023 | Systematic Review | Biomedicines | Umbrella review of drug therapies and efficacy/side effects for trigeminal neuralgia |
| [34108244](https://pubmed.ncbi.nlm.nih.gov/34108244/) | 2021 | Review | Practical Neurology | Practical guide to diagnosis and treatment of trigeminal neuralgia |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | Review | Molecular Pain | Overview of trigeminal neuralgia pathophysiology and pharmacological treatments |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Rev Neurother | Update on pharmacotherapy options for trigeminal neuralgia |
| [39365662](https://pubmed.ncbi.nlm.nih.gov/39365662/) | 2025 | Cohort | Pain | Nationwide disease trajectory study of trigeminal neuralgia comorbidities |
| [34003166](https://pubmed.ncbi.nlm.nih.gov/34003166/) | 2021 | Review | Neurology India | Medical management approaches for trigeminal neuralgia |
| [25864062](https://pubmed.ncbi.nlm.nih.gov/25864062/) | 2015 | Review | Neurosciences (Riyadh) | Update on pharmacological and surgical treatment options for trigeminal neuralgia |

---

## Canada Market Information

Lamotrigine currently has **no Health Canada drug identification numbers (DINs)** on file in this evidence pack and is recorded as **not marketed**. No product-level licensing details are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed, direct comparative/controlled trials (NCT00913107, NCT00203229) plus an EAN clinical guideline placing lamotrigine within established trigeminal neuralgia management support a mechanistically plausible and clinically corroborated repurposing signal (L2 evidence), even though trial sample sizes are small.

**To proceed, the following is needed:**
- TFDA/Health Canada product warnings, contraindications, and full prescribing information (currently a Blocking data gap preventing safety pre-screening)
- Formal drug interaction (DDI) profile — no DDI data currently on file
- Confirmed detailed mechanism-of-action documentation from DrugBank
- Larger-scale confirmatory trial data given the small enrollment (n=20–21) of the two direct lamotrigine trials
- Clarification of the "trigeminal nerve neoplasm" TxGNN top-ranked hit to rule out a knowledge-graph disease-node mapping error before any further action on that candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

