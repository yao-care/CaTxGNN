---
layout: default
title: Lacosamide
parent: Moderate Evidence (L3-L4)
nav_order: 511
evidence_level: L3
indication_count: 10
---

# Lacosamide
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

# Lacosamide: From Epilepsy (Focal Seizures) to Manic Bipolar Affective Disorder

## One-Sentence Summary

Lacosamide is a sodium-channel-modulating antiseizure medication, marketed in Canada and used for focal epilepsy. The TxGNN model predicts it may be effective for **manic bipolar affective disorder**, but the clinical signal so far is for the *depressive* phase of bipolar disorder rather than mania. Support currently consists of **1 recruiting Phase 3 trial** and **a handful of small open-label, retrospective and case-level publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (focal seizures), as described in the literature. The Health Canada licence text was not supplied. |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data were not supplied in the Evidence Pack. The literature describes lacosamide as selectively enhancing slow inactivation of voltage-gated sodium channels, which stabilises neuronal membranes. It also interacts with CRMP2, a protein involved in ion-channel trafficking.

Several antiepileptic drugs, such as lamotrigine and carbamazepine, have long been used as mood stabilisers in psychiatry, and membrane stabilisation is the proposed common thread. Lacosamide shares this sodium-channel mechanism, so a role in bipolar disorder is biologically plausible.

The mapping to the **manic** phenotype is indirect, though. The available clinical work (an open-label pilot, a retrospective cohort and the registered Phase 3 trial) focuses on bipolar **depression**, not mania. There is also a safety flag: a published case report links lacosamide to neutropenia in a patient with bipolar disorder.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07412132](https://clinicaltrials.gov/study/NCT07412132) | Phase 3 | Recruiting | 40 | Randomised, double-blind, parallel-group trial of lacosamide as add-on to first- or second-line treatment in major depressive episodes of bipolar disorder types I and II. Expected completion is January 2027. No results yet, and it targets the depressive pole rather than mania. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33666402](https://pubmed.ncbi.nlm.nih.gov/33666402/) | 2021 | Open-label pilot trial | J Clin Psychopharmacol | 12-week pilot of lacosamide efficacy and safety in bipolar depression. No abstract was supplied, so outcomes could not be summarised. |
| [30251375](https://pubmed.ncbi.nlm.nih.gov/30251375/) | 2018 | Retrospective cohort | Psychiatry Clin Neurosci | 30-day comparison of lacosamide against a retrospective control group on other antiepileptics, in bipolar patients without epilepsy. |
| [29253680](https://pubmed.ncbi.nlm.nih.gov/29253680/) | 2018 | Prospective multicentre study | Epilepsy Behav | Examined the effect of lacosamide on depression and anxiety symptoms in focal refractory epilepsy. |
| [30275630](https://pubmed.ncbi.nlm.nih.gov/30275630/) | 2018 | Case report | Indian J Psychol Med | Lacosamide precipitated neutropenia in a patient with bipolar disorder and epilepsy (safety signal). |
| [28845834](https://pubmed.ncbi.nlm.nih.gov/28845834/) | 2017 | Case report | Acta Biomed | Clinical stabilisation with lacosamide of a mood disorder comorbid with PTSD and fronto-temporal epilepsy. |
| [38304661](https://pubmed.ncbi.nlm.nih.gov/38304661/) | 2024 | Case report | Cureus | Management of a pregnant patient with bipolar I disorder and multiple comorbidities. |
| [32693579](https://pubmed.ncbi.nlm.nih.gov/32693579/) | 2020 | Review | ACS Chem Neurosci | CRMP2 druggability, which offers a mechanistic rationale. |
| [29957667](https://pubmed.ncbi.nlm.nih.gov/29957667/) | 2018 | Review | Ther Drug Monit | Therapeutic drug monitoring of antiepileptic drugs. It notes their use in conditions such as bipolar disorder, but it is not specific to lacosamide. |

---

## Canada Market Information

Dosage form and approved-indication text were not supplied for these products. Five of the 20 authorisations are shown.

| DIN | Product Name |
|---------|------|
| 2512874 | LACOSAMIDE |
| 2490544 | MINT-LACOSAMIDE |
| 2357615 | VIMPAT |
| 2490552 | MINT-LACOSAMIDE |
| 2512890 | LACOSAMIDE |

---

## Safety Considerations

- **Haematological signal**: A published case report (PMID 30275630) describes lacosamide-precipitated neutropenia in a patient with bipolar disorder. This is a single case, but it is relevant to this population.

Please refer to the package insert for warnings, contraindications and drug interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence for mania specifically is thin. There is one recruiting Phase 3 trial with no results, and it targets bipolar depression. The remaining support is small open-label, retrospective and case-level work, and the neutropenia report is an unresolved safety flag. Health Canada safety documentation is also missing, which blocks safety screening.

**Other predicted indication worth noting:** Migraine (TxGNN rank 5) has much stronger evidence in the same pack. It includes a completed Phase 3 trial (NCT05851781) with a corresponding RCT publication (PMID 41863672), a completed Phase 2 placebo-controlled trial, and a CGRP biomarker study. It is rated L1 with a "Proceed with Guardrails" recommendation. Most of these trials come from one research group and need independent replication. If the goal is the most actionable repurposing direction for lacosamide, migraine deserves its own report.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap)
- Mechanism-of-action data from DrugBank
- Results from NCT07412132 and full outcome data from the open-label pilot (PMID 33666402)
- Evidence specific to manic episodes, as opposed to bipolar depression
- A haematological monitoring plan given the neutropenia case report
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

