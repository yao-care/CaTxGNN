---
layout: default
title: Desvenlafaxine
parent: Model Prediction Only (L5)
nav_order: 265
evidence_level: L5
indication_count: 10
---

# Desvenlafaxine
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

# Desvenlafaxine: From Major Depressive Disorder to Obsessive-Compulsive Disorder

## One-Sentence Summary

Desvenlafaxine is a serotonin-norepinephrine reuptake inhibitor (SNRI) and the active metabolite of venlafaxine, marketed for major depressive disorder.
The TxGNN model predicts it may be effective for **obsessive-compulsive disorder (OCD)**.
The 2 listed clinical trials and 4 publications give only **indirect** support, and none tests desvenlafaxine in OCD.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major depressive disorder (the Canadian licence records carry no indication text, so this comes from the drug's known use and the evidence pack's rationale) |
| Predicted New Indication | Obsessive-compulsive disorder |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 (indirect evidence from the parent compound venlafaxine; no desvenlafaxine-specific OCD study) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source record. Based on known information, desvenlafaxine is an SNRI and the active metabolite of venlafaxine. It has proven efficacy in major depressive disorder and mechanistically may be applicable to OCD.

Blocking serotonin reuptake is the established pharmacological basis for OCD treatment. Clomipramine and SSRIs are the standard drugs, and the literature review in the table below describes a central role for the serotonin system in OCD. Desvenlafaxine shares this serotonergic action.

The support is indirect. The only head-to-head OCD data are for the parent drug venlafaxine, in a double-blind trial against paroxetine. No study of desvenlafaxine itself in OCD was found.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03299166](https://clinicaltrials.gov/study/NCT03299166) | Phase 2/3 | Completed | 426 | Adjunctive troriluzole vs placebo in OCD patients with inadequate response to an SSRI, clomipramine, venlafaxine or desvenlafaxine. The disease matches, but desvenlafaxine is only a prior therapy, not the study drug. |
| [NCT01527786](https://clinicaltrials.gov/study/NCT01527786) | Phase 3 | Completed | 25 | Pilot of desvenlafaxine in postpartum depression, measuring return to functioning. The drug matches, but the disease is not OCD, so it gives only indirect tolerability information. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14624187](https://pubmed.ncbi.nlm.nih.gov/14624187/) | 2003 | RCT | J Clin Psychopharmacol | First randomized double-blind comparison of an SNRI (venlafaxine) with paroxetine in 150 OCD patients, assessing efficacy and tolerability. This is parent-compound evidence, not desvenlafaxine. |
| [24766145](https://pubmed.ncbi.nlm.nih.gov/24766145/) | 2014 | Review | Expert Opin Pharmacother | Reviews double-blind studies of serotonergic antidepressants in OCD and confirms a key role for the serotonin system. |
| [36686097](https://pubmed.ncbi.nlm.nih.gov/36686097/) | 2022 | Review | Cureus | Comprehensive review of postpartum depression, noting that untreated cases can later lead to OCD and anxiety. Only tangentially related. |
| [40224942](https://pubmed.ncbi.nlm.nih.gov/40224942/) | 2025 | Clinical study | Psychiatry Clin Psychopharmacol | Risperidone augmentation in antidepressant-resistant somatic symptom disorder. It mentions OCD only as a related condition. |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2321092 | PRISTIQ |
| 2554976 | DESVENLAFAXINE |
| 2495147 | JAMP DESVENLAFAXINE |
| 2525615 | AG-DESVENLAFAXINE |
| 2458217 | TEVA-DESVENLAFAXINE |

These are 5 of the 20 authorizations. Dosage form and approved-indication text are not populated in the source records.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, and the serotonergic mechanism is plausible for OCD. No trial or publication tests desvenlafaxine in OCD, though. The nearest evidence is one venlafaxine RCT and general reviews. The Health Canada safety labelling has also not been reviewed.

**To proceed, the following is needed:**
- The Health Canada package insert (warnings and contraindications), which blocks safety screening
- Detailed mechanism of action data
- Desvenlafaxine-specific OCD evidence, from a systematic search of trial registries and literature or from a new controlled study
- A comparison against the established OCD options (SSRIs, clomipramine) to judge whether a repurposing case is worthwhile

Among the other predictions for this drug, dysthymic disorder has stronger evidence (L2), including direct desvenlafaxine studies in chronic depression. It may be a better first candidate.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

