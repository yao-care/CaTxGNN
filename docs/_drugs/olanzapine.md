---
layout: default
title: Olanzapine
parent: Model Prediction Only (L5)
nav_order: 575
evidence_level: L5
indication_count: 3
---

# Olanzapine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Olanzapine: From Antipsychotic Use to Potential Adjunct in Treatment-Resistant Agoraphobia

## One-Sentence Summary

Olanzapine is an atypical (second-generation) antipsychotic, historically used for schizophrenia and bipolar disorder. The TxGNN model flags three candidate new indications for this drug — **benign paroxysmal torticollis of infancy**, **agoraphobia**, and **dysthymic disorder** — but only the latter two are backed by any real-world evidence (7 and 5 publications respectively, no clinical trials registered for any of them), and the top-ranked prediction is itself assessed by the evidence pipeline as a likely knowledge-graph artifact rather than a genuine signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not present in this evidence pack (0 Canadian licenses on file). Olanzapine is generally known as an atypical antipsychotic for schizophrenia and bipolar I disorder |
| Predicted New Indications | 1) Benign paroxysmal torticollis of infancy (Rank 1, **likely false positive**) · 2) Agoraphobia (Rank 2) · 3) Dysthymic disorder (Rank 3) |
| TxGNN Prediction Score | 99.54% (Rank 1) / 99.47% (Rank 2, agoraphobia) / 99.28% (Rank 3, dysthymic disorder) |
| Evidence Level | L5 (Rank 1 — no trials, no literature) / L3 (Rank 2 & 3 — case reports, open-label study, reviews only) |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (`original_moa: [Data Gap]`). Based on general pharmacological knowledge, olanzapine acts as a D2/5-HT2A/5-HT1A receptor antagonist with sedative and anxiolytic properties, and its established efficacy is in schizophrenia and bipolar disorder — conditions unrelated pathologically to either of the two evidence-backed candidates here.

For **agoraphobia** (Rank 2), the mechanistic rationale is indirect: olanzapine has been studied as an *augmentation agent* added to SSRIs/benzodiazepines in treatment-resistant panic disorder with agoraphobia, where its sedative/anxiolytic action reduces panic attack frequency and anticipatory anxiety — not a first-line mechanism targeting the disorder's core pathology. For **dysthymic disorder** (Rank 3), the rationale rests on 5-HT2A antagonism producing mild antidepressant augmentation effects, again in the context of adjunct therapy for comorbid personality/bipolar disorder patients rather than as monotherapy evidence.

For **benign paroxysmal torticollis of infancy** (Rank 1, the highest-scoring prediction), the evidence pipeline itself concludes there is **no known pathological connection** to olanzapine's D2/5-HT2A antagonism — this is a self-limiting infant migraine-variant condition. With zero clinical trials and zero literature despite the highest TxGNN score, this is assessed as a false positive driven by knowledge-graph embedding similarity rather than a real biological signal, and should not be pursued.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the three predicted indications (torticollis, agoraphobia, or dysthymic disorder).

---

## Literature Evidence

### Agoraphobia (Rank 2) — 7 publications

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16415705](https://pubmed.ncbi.nlm.nih.gov/16415705/) | 2006 | Open-label trial (12-week, fixed-dose) | J Clin Psychopharmacol | Olanzapine 5mg/d augmentation of SSRI in 31 SSRI-resistant panic disorder patients (with/without agoraphobia); reduced panic and anticipatory anxiety scores |
| [40946318](https://pubmed.ncbi.nlm.nih.gov/40946318/) | 2025 | Review | Psychother Psychosom | Integrative review of pharmacological/psychotherapeutic/neurostimulatory options for treatment-resistant anxiety disorders |
| [26635099](https://pubmed.ncbi.nlm.nih.gov/26635099/) | 2016 | Review | Expert Opin Pharmacother | Systematic review of treatment-resistant panic disorder management |
| [25012437](https://pubmed.ncbi.nlm.nih.gov/25012437/) | 2014 | Cohort | J Affect Disord | Comorbid anxiety/OCD (incl. agoraphobia) impact on 24-month bipolar I disorder outcomes |
| [15470803](https://pubmed.ncbi.nlm.nih.gov/15470803/) | 2004 | Case report | Pharmacopsychiatry | Remission of panic disorder with olanzapine + paroxetine combination |
| [10739446](https://pubmed.ncbi.nlm.nih.gov/10739446/) | 2000 | Case report | Am J Psychiatry | Early report of olanzapine and panic attacks |
| [17099612](https://pubmed.ncbi.nlm.nih.gov/17099612/) | 2006 | Case report (CBT-focused) | Psychiatria Danubina | Panic disorder with agoraphobia comorbid with psychosis, treated primarily via CBT |

### Dysthymic Disorder (Rank 3) — 5 publications

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10578457](https://pubmed.ncbi.nlm.nih.gov/10578457/) | 1999 | Open-label study | Biol Psychiatry | Olanzapine safety/efficacy in borderline personality disorder with comorbid dysthymia |
| [21154393](https://pubmed.ncbi.nlm.nih.gov/21154393/) | 2010 | Cochrane review | Cochrane Database Syst Rev | Second-generation antipsychotics (incl. olanzapine) as add-on for major depression and dysthymia |
| [22938165](https://pubmed.ncbi.nlm.nih.gov/22938165/) | 2012 | Review (bipolar-focused, not dysthymia-specific) | Bipolar Disord | Evidence-based options for treatment-resistant bipolar disorder |
| [11920152](https://pubmed.ncbi.nlm.nih.gov/11920152/) | 2002 | Review (different drug class — benzamides) | Mol Psychiatry | Substituted benzamides in dysthymia and schizophrenia negative symptoms; not olanzapine-specific |
| [34727399](https://pubmed.ncbi.nlm.nih.gov/34727399/) | 2021 | Systematic review/meta-analysis (different drug — amisulpride) | Hum Psychopharmacol | Amisulpride for depressive symptoms; mechanistic analogy only, not direct olanzapine evidence |

### Benign Paroxysmal Torticollis of Infancy (Rank 1)

Currently no related literature available.

---

## Canada Market Information

Olanzapine currently has **no active Canadian market authorizations** on file in this evidence pack (0 DINs, market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data are not available in this evidence pack — retrieval of the TFDA/Health Canada product label (`data_gaps: DG001`) is flagged as a **Blocking** gap that must be resolved before any safety pre-screening can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The highest-scoring prediction (torticollis) is assessed as a likely false positive with zero supporting trials or literature. The two candidates with actual literature support — agoraphobia and dysthymic disorder — are backed only by open-label studies, case reports, and reviews (L3), with no completed RCTs or registered trials, and several cited papers concern different drug classes (benzamides, amisulpride) rather than olanzapine directly. Combined with a Blocking gap on core safety/label data and no current Canadian market presence, the evidence does not yet support advancing beyond a research question.

**To proceed, the following is needed:**
- TFDA/Health Canada product label (warnings, contraindications) — currently blocking (DG001)
- DrugBank-sourced mechanism of action detail (DG002)
- A prospective/randomized trial specifically testing olanzapine augmentation in treatment-resistant agoraphobia or dysthymic disorder
- Independent confirmation (or refutation) of the torticollis signal as a true knowledge-graph artifact before any further evaluation
- Drug interaction (DDI) profile, since none is currently on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

