---
layout: default
title: Quetiapine
parent: 僅模型預測 (L5)
nav_order: 660
evidence_level: L5
indication_count: 10
---

# Quetiapine
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

Using the drug-repurposing report template directly (no additional skill needed — this is a single-pass writing task with a fully specified format).

# Quetiapine: From Schizophrenia/Bipolar Disorder to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

> Quetiapine is a second-generation (atypical) antipsychotic historically indicated for schizophrenia, bipolar disorder, and as adjunctive therapy for major depressive disorder.
> The TxGNN model's top-ranked prediction for this drug is **Retinal Dystrophy with or without Extraocular Anomalies**,
> but this prediction has **0 clinical trials** and **no literature directly linking quetiapine to this disease** — the model itself flags this association as a likely knowledge-graph embedding artifact rather than a biologically grounded hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia / Bipolar Disorder (general drug knowledge — not present in this evidence pack; `original_indications` and Canada license data are empty) |
| Predicted New Indication | Retinal Dystrophy with or without Extraocular Anomalies |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed (未上市) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (`original_moa: [Data Gap]`). Based on general pharmacological knowledge, quetiapine acts primarily as an antagonist at central dopamine D2, serotonin 5-HT2A, histamine H1, and α1-adrenergic receptors — a CNS receptor-modulation profile with proven efficacy in schizophrenia and bipolar disorder.

Retinal dystrophy with or without extraocular anomalies is a structural/developmental ophthalmic disease with a genetic etiology. There is no established pharmacological pathway connecting quetiapine's CNS receptor activity to retinal structural development or degeneration.

The evidence pack's own repurposing rationale is explicit on this point: *"No known mechanistic link. Quetiapine's CNS receptor targets (D2/5‑HT2A/H1/α1) have no pharmacological connection to the genetic/structural etiology of congenital retinal dystrophy. The high TxGNN score is likely an artifact of knowledge-graph embedding similarity rather than genuine biological plausibility."* This assessment should be taken at face value — the prediction is not currently actionable.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Seminars in Ultrasound, CT, and MR | Orbital infection etiology and imaging; no mention of quetiapine or retinal dystrophy |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Seminars in Neurology | Clinical approach to diplopia; unrelated to drug therapy |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klinische Monatsblätter für Augenheilkunde | Congenital ptosis pathophysiology and management |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | Congenital lens shape anomalies |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case Report | American Journal of Ophthalmology | Unilateral cryptophthalmia case description |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case Report | Journal of Neuro-Ophthalmology | Congenital trochlear-oculomotor synkinesis |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Documenta Ophthalmologica | Wagner-Stickler syndrome complex (vitreoretinal degeneration) |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Imaging classification of pediatric orbital/ocular pathology |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Case Report | Optometry and Vision Science | Congenital extraocular muscle fibrosis case |
| [19064847](https://pubmed.ncbi.nlm.nih.gov/19064847/) | 2008 | Case Report | Archives of Ophthalmology | Orbital arteriovenous malformation series |

**Note:** None of these publications mention quetiapine. They surfaced via disease-side keyword overlap (retinal/ocular/congenital terminology) rather than any drug-disease co-occurrence, consistent with the "embedding artifact" assessment above.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction lacks any mechanistic plausibility, clinical trial support, or relevant literature — the model's own rationale identifies it as a probable embedding artifact, and this drug is not currently marketed in Canada, so no regulatory/market foundation exists to build on.

**To proceed, the following is needed:**
- TFDA/Health Canada label warnings and contraindications (currently blocking — data gap DG001)
- Verified mechanism of action data from DrugBank (data gap DG002)
- If pursuing this candidate at all, preclinical/mechanistic studies establishing a biological rationale connecting quetiapine to retinal dystrophy

**Worth noting separately:** within the same prediction set, rank 8 — **trichotillomania** — has a materially stronger evidence base (7 PubMed publications, including case reports and reviews specifically on quetiapine's use in trichotillomania, evidence level L4, decision stage S1 "Research Question"). If the goal is identifying a viable repurposing candidate for this drug, that indication warrants evaluation ahead of the top-ranked but mechanistically unsupported retinal dystrophy prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

