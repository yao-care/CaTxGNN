---
layout: default
title: Phenytoin
parent: Model Prediction Only (L5)
nav_order: 726
evidence_level: L5
indication_count: 10
---

# Phenytoin
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

# Phenytoin: From Seizure Control to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Phenytoin is an established antiseizure drug, marketed in Canada under several brand and generic licences. The TxGNN model's top-ranked prediction is **trigeminal nerve neoplasm**, but this is supported by **0 clinical trials** and only **5 publications**, none of which test phenytoin against a neoplasm. The best-supported candidate in the same prediction list is the neighbouring condition **trigeminal neuralgia**, with **1 completed trial** and about **19 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Seizure disorders (the Health Canada indication text is not included in the evidence pack) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |
| Best-Supported Candidate | Trigeminal neuralgia (99.97%, L3, Proceed with Guardrails) |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not currently available for this drug. Phenytoin is known as a voltage-gated sodium-channel blocker, and its efficacy in seizure disorders is long established.

For **trigeminal nerve neoplasm**, the prediction is probably driven by closeness in the knowledge graph to trigeminal neuralgia and other trigeminal-nerve nodes. The retrieved literature covers trigeminal neuralgia, Sturge-Weber syndrome and nerve fibre physiology, not tumour treatment. Nothing in the evidence supports an antitumour mechanism for phenytoin. Sodium-channel blockade may relieve neuralgic pain, but that is not a neoplasm indication.

For **trigeminal neuralgia**, the mechanism is plausible. Reducing abnormal high-frequency firing in trigeminal afferents is the same mechanism class as carbamazepine, the standard first-line drug. Phenytoin is already used clinically as an intravenous rescue treatment during acute exacerbations.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked indication (trigeminal nerve neoplasm).

Trials linked to trigeminal neuralgia, the best-supported related candidate:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03712254](https://clinicaltrials.gov/study/NCT03712254) | N/A | Completed | 15 | Prospective study of phenytoin for acute exacerbations of trigeminal neuralgia. It is directly on-indication, but small and non-phase, so it supports feasibility, not efficacy. |

---

## Literature Evidence

Literature linked to trigeminal nerve neoplasm. None of it addresses neoplasm treatment.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurother | Overview of medical and surgical treatments for trigeminal neuralgia. |
| [21751615](https://pubmed.ncbi.nlm.nih.gov/21751615/) | 2011 | Review | J Assoc Physicians India | Sturge-Weber syndrome (face, eye and leptomeningeal vascular malformation with seizures), with a case report. |
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | An Esp Pediatr | 14 Sturge-Weber cases reviewed for clinical features, course and treatment response. |
| [4155965](https://pubmed.ncbi.nlm.nih.gov/4155965/) | 1971 | Cohort | Birth Defects Orig Artic Ser | Skin disorders in institutionalised people with intellectual disability, including drug-induced effects. |
| [5514358](https://pubmed.ncbi.nlm.nih.gov/5514358/) | 1970 | Preclinical/Physiology | Trans Am Neurol Assoc | Trigeminal root fibre size and pain conduction; analgesia without anaesthesia in trigeminal neuralgia. |

Key trigeminal neuralgia literature, for the best-supported candidate:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35469475](https://pubmed.ncbi.nlm.nih.gov/35469475/) | 2022 | Cohort | Cephalalgia | Retrospective analysis of 144 cases of intravenous lacosamide and phenytoin for acute exacerbations. |
| [32981076](https://pubmed.ncbi.nlm.nih.gov/32981076/) | 2020 | Case series | Headache | Retrospective cohort of responses to IV phenytoin in trigeminal neuralgia crisis. |
| [28761370](https://pubmed.ncbi.nlm.nih.gov/28761370/) | 2017 | Review | J Pain Res | Phenytoin and carbamazepine in trigeminal neuralgia: marketing-based versus evidence-based treatment. |
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Guideline | Eur J Neurol | European Academy of Neurology guideline on trigeminal neuralgia. Its phenytoin recommendations should be verified in the full text. |

---

## Canada Market Information

Showing 5 of 8 licences. Dosage form and approved-indication text were not provided.

| DIN | Product Name |
|---------|------|
| 2250896 | TARO-PHENYTOIN |
| 23698 | DILANTIN INFATABS |
| 22772 | DILANTIN |
| 498335 | PHENYTOIN SODIUM INJECTION USP |
| 22780 | DILANTIN |

---

## Other Predicted Indications

| Rank | Indication | Score | Evidence Level | Decision | Note |
|------|------|------|------|------|------|
| 2 | Startle epilepsy | 99.98% | L4 | Hold | Case reports and a rat study only; the one treatment-focused item favours lamotrigine. |
| 3 | Micturition-induced seizures | 99.98% | L5 | Hold | Prediction only. A single case report (PMID 21561835) used clobazam plus phenytoin. |
| 4 | Audiogenic seizures | 99.98% | L4 | Hold | Mostly rodent studies in which phenytoin is a reference drug. |
| 5 | Thinking seizures | 99.98% | L4 | Hold | Three unrelated trials (pharmacokinetic and TMS studies); indirect literature. |
| 6 | Orgasm-induced seizures | 99.98% | L5 | Hold | Prediction only. |
| 7 | Eating seizures | 99.98% | L4 | Hold | One healthy-volunteer pharmacokinetic trial; loosely related literature. |
| 8 | Reading seizures | 99.97% | L5 | Hold | Prediction only. |
| 9 | Trigeminal neuralgia | 99.97% | L3 | Proceed with Guardrails | Small prospective study plus several clinical series. |
| 10 | Beta-ketothiolase deficiency | 99.95% | L5 | Hold | Prediction only; no plausible mechanism. |

---

## Safety Considerations

Please refer to the package insert for safety information.

The retrieved literature also reports these phenytoin-related concerns:
- Gingival hyperplasia in roughly 50–60% of patients (PMID 11789440).
- Total external ophthalmoplegia with drowsiness to coma at serum levels of 36–55 µg/mL (PMID 824568).
- Fracture risk with long-term enzyme-inducing antiepileptics (PMID 21711263).
- Congenital malformation risk with in-utero antiepileptic exposure (PMID 18929083).

---

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, trigeminal nerve neoplasm)

**Rationale:**
- The prediction is model-only (L5). There are no trials, and the linked literature concerns trigeminal neuralgia and related syndromes rather than tumours.
- The related candidate **trigeminal neuralgia** is the only one that reaches **Proceed with Guardrails** (L3). It is limited to acute rescue use under monitoring, with cardiac and infusion-rate precautions and attention to long-term toxicity.

**To proceed, the following is needed:**
- Mechanism-of-action data from DrugBank.
- Health Canada package insert warnings and contraindications, including approved indications and dosage forms for each DIN.
- Confirmation of whether the "trigeminal nerve neoplasm" prediction is a graph artefact of the neuralgia link. If it is, re-prioritise trigeminal neuralgia as the lead candidate.
- Full-text verification of the guideline (PMID 30860637) and the lacosamide comparison study (PMID 35469475).
- For trigeminal neuralgia, a controlled study or systematic review of intravenous phenytoin against standard rescue options.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

