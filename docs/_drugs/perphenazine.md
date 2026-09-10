---
layout: default
title: Perphenazine
parent: 僅模型預測 (L5)
nav_order: 612
evidence_level: L5
indication_count: 10
---

# Perphenazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Perphenazine: From Antipsychotic Use to Anxiety Disorder

> **Methodology note:** TxGNN's top-ranked prediction for this drug (rank 1, "retinal dystrophy with or without extraocular anomalies," score 99.96%) and eight other top-9 candidates are all rare congenital/genetic diseases with **zero supporting clinical trials or literature**, and the evidence pack's own mechanistic review flags them as likely knowledge-graph embedding artifacts rather than real signals. This report therefore focuses on the **rank-10 candidate, Anxiety Disorder**, which is the only prediction in this evidence pack backed by actual clinical trials and a coherent, literature-supported mechanistic story.

## One-Sentence Summary

Perphenazine is a first-generation (typical) antipsychotic of the phenothiazine class; the evidence pack does not record its formal original indication (data gap), but it is well established for treatment of psychotic disorders such as schizophrenia. The TxGNN model's most credible signal points to **Anxiety Disorder**, historically supported by its fixed-dose combination with amitriptyline (Triavil/Etrafon), with **2 clinical trials** and **20 publications** identified, though most of the literature predates 1980.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (data gap) — perphenazine is a phenothiazine-class typical antipsychotic |
| Predicted New Indication | Anxiety Disorder (selected over TxGNN's top-ranked candidate — see methodology note above) |
| TxGNN Prediction Score | 99.53% (rank 8,846 of all drug-disease pairs) |
| Evidence Level | L2 |
| Canada Market Status | Not marketed (未上市) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for perphenazine in this evidence pack (flagged as a High-severity data gap). Based on known pharmacology, perphenazine is a typical antipsychotic (D2 dopamine receptor antagonist) of the phenothiazine class, and at low doses phenothiazines have long-recognized sedative/anxiolytic effects independent of their antipsychotic action.

The link to Anxiety Disorder is not a novel hypothesis — it reflects historical clinical practice. Perphenazine was marketed in fixed-dose combination with the tricyclic antidepressant amitriptyline (brand names Triavil/Etrafon) specifically for mixed anxiety-depression states from the 1960s through the 1980s, and multiple controlled studies from that era (see Literature Evidence below) tested this combination directly.

However, this mechanistic plausibility is dated. Modern treatment guidelines no longer recommend antipsychotics as first-line therapy for anxiety disorders, given the more favorable risk profile of SSRIs and benzodiazepines relative to perphenazine's extrapyramidal symptom (EPS) and metabolic risks. This explains why the automated scoring stage classifies this as a "Research Question" rather than an actionable candidate.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05646693](https://clinicaltrials.gov/study/NCT05646693) | Phase 2 | Unknown | 58 | Evaluates Adepsique® (amitriptyline + perphenazine + diazepam) combined with antioxidant therapy in chronic subjective tinnitus, measuring inflammatory cytokines and oxidative stress; not an anxiety-specific efficacy trial (relevance grade C — low). |
| [NCT02374567](https://clinicaltrials.gov/study/NCT02374567) | Phase 3 | Terminated | 407 | Pharmacovigilance study of psychopharmacological treatment safety and adverse drug reaction rates in elderly (gerontopsychiatric) inpatients; a safety-monitoring study, not an anxiety efficacy RCT, and was terminated (relevance grade B). |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17017818](https://pubmed.ncbi.nlm.nih.gov/17017818/) | 2006 | Review | J Clin Psychiatry | Reviews efficacy of typical and atypical antipsychotics for primary and comorbid anxiety symptoms/disorders. |
| [14249358](https://pubmed.ncbi.nlm.nih.gov/14249358/) | 1964 | RCT/Cohort | J Med Assoc Georgia | Combined amitriptyline and perphenazine in combined depression and anxiety. |
| [4867598](https://pubmed.ncbi.nlm.nih.gov/4867598/) | 1968 | RCT (double-blind) | Psychosomatics | Double-blind study of perphenazine-amitriptyline for anxiety and depression secondary to physical disorders. |
| [4886995](https://pubmed.ncbi.nlm.nih.gov/4886995/) | 1969 | RCT | Dis Nerv Syst | Double-blind comparison of thiothixene vs. perphenazine-amitriptyline for psychotic and psychoneurotic depression. |
| [13726172](https://pubmed.ncbi.nlm.nih.gov/13726172/) | 1961 | RCT | Am J Psychiatry | Effectiveness of psychotherapy alone vs. combined with perphenazine or placebo in neurotic and hyperkinetic children. |
| [14401911](https://pubmed.ncbi.nlm.nih.gov/14401911/) | 1959 | RCT | J Ment Sci | Compares perphenazine ("Fentazin"), sodium amylobarbitone, and placebo in anxious and depressed outpatients. |
| [13405719](https://pubmed.ncbi.nlm.nih.gov/13405719/) | 1957 | Clinical study (type pending) | J Am Geriatr Soc | Preliminary report on trilafon (perphenazine) for treatment of anxiety, agitation and excitement in the elderly. |
| [4554486](https://pubmed.ncbi.nlm.nih.gov/4554486/) | 1972 | Clinical study (type pending) | Psychopharmacologia | Collaborative controlled study comparing doxepin vs. amitriptyline-perphenazine in mixed anxious-depressed neurotic outpatients. |
| [13687810](https://pubmed.ncbi.nlm.nih.gov/13687810/) | 1960 | Clinical study (type pending) | Rass Studi Psichiatr | Perphenazine in treatment of neuroses and depressive syndromes — symptomatological/psychopathological findings. |
| [14149372](https://pubmed.ncbi.nlm.nih.gov/14149372/) | 1964 | Review | Psychosomatics | Reviews phenothiazines in the management of stress and anxiety. |

## Canada Market Information

Perphenazine currently holds **no active Health Canada Drug Identification Numbers (DINs)** — market status is **not marketed** in this evidence pack, so no product-level licensing table is available.

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data were retrievable in this evidence pack — this is recorded as a **Blocking-severity data gap (DG001)**, meaning safety information cannot currently be sourced from a Health Canada/TFDA label.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Anxiety Disorder is the only prediction in this evidence pack with real (if dated) clinical and literature support, reflecting perphenazine's historical use in the amitriptyline-perphenazine combination. However, the supporting evidence predates modern trial standards, the one Phase 3 trial identified was terminated and was a safety/pharmacovigilance study rather than an efficacy RCT, perphenazine is not currently marketed in Canada (0 DINs), and a Blocking-severity gap in label warnings/contraindications means the candidate cannot yet clear even an initial safety screen (S1).

**To proceed, the following is needed:**
- Health Canada product monograph or TFDA label data (warnings, contraindications) — resolves Blocking gap DG001
- Detailed mechanism of action data from DrugBank — resolves High-severity gap DG002
- Contemporary (post-1990) efficacy evidence for antipsychotic use in anxiety disorder, since existing RCTs are 40–65 years old
- A documented decision to exclude the nine top-ranked TxGNN congenital-disease predictions from further evaluation, given the absence of any clinical, literature, or mechanistic support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

