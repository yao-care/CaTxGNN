---
layout: default
title: Orphenadrine
parent: Model Prediction Only (L5)
nav_order: 682
evidence_level: L5
indication_count: 7
---

# Orphenadrine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Orphenadrine: From Muscle Relaxant Use to Retinal Dystrophy

## One-Sentence Summary

Orphenadrine is an anticholinergic, H1-antagonist and NMDA-antagonist muscle relaxant, marketed in Canada under one DIN.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies** (score 99.29%), but there are **0 clinical trials** and **14 publications** that appear to be unrelated keyword matches.
This is a model-only prediction with no real supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available licence data |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Orphenadrine is described as an anticholinergic, H1-antagonist and NMDA-antagonist muscle relaxant. Its literature shows use for parkinsonism and for antipsychotic-induced extrapyramidal symptoms.

**No plausible mechanistic link was identified** between these actions and retinal degeneration or photoreceptor biology. The high TxGNN score reflects knowledge-graph topology only. The retrieved literature consists of general ophthalmology and extraocular muscle papers, such as diplopia, congenital ptosis and congenital fibrosis of the extraocular muscles. None of them appear to mention orphenadrine. They were most likely matched on the words "extraocular" or "ocular" in the disease name.

This prediction should therefore be treated as noise unless independent evidence emerges.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The Evidence Pack lists 14 papers. All are tier 3 or unclassified, and none appear to study orphenadrine. The most relevant by study type are shown below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Seminars in Neurology | Systematic approach to examining patients with diplopia; no drug content |
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Seminars in Ultrasound, CT, and MR | Imaging and clinical features of orbital infections |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klinische Monatsblätter für Augenheilkunde | Congenital ptosis forms and associated eye findings |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | Congenital anomalies of lens size, shape and position |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Differential diagnosis and imaging of pediatric ocular pathologies |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | Journal of Binocular Vision and Ocular Motility | Congenital cranial dysinnervation disorders causing ophthalmoplegia |
| [30747268](https://pubmed.ncbi.nlm.nih.gov/30747268/) | 2019 | Cohort | Neuroradiology | Neuroradiological evaluation of acute ophthalmoplegia |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case report | American Journal of Ophthalmology | Two patients with unilateral cryptophthalmia |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2243559 | SANDOZ ORPHENADRINE | Not specified | Not specified |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a graph-based score. There are no clinical trials, no orphenadrine-specific literature and no plausible mechanism linking orphenadrine to retinal dystrophy. The retrieved papers are most likely keyword-matched noise.

**To proceed, the following is needed:**
- A Health Canada package insert review (warnings, contraindications and approved indication), which is currently a blocking gap for safety screening
- Detailed mechanism of action data from DrugBank
- Any preclinical or mechanistic evidence connecting muscarinic, H1 or NMDA pathways to photoreceptor or retinal biology

**Other predictions in the same pack:**
- **Schizophrenia** (score 99.13%, L4, stage S1) is the only prediction with orphenadrine-specific literature. That literature concerns managing antipsychotic-induced parkinsonism, not treating core schizophrenia symptoms. Its signal is indirect and potentially double-edged, because NMDA antagonism could theoretically worsen psychosis and anticholinergic burden can impair cognition. It is better framed as a research question than as a repurposing candidate.
- **Congenital glycosylation disorder, perisylvian polymicrogyria, Charcot-Marie-Tooth type 1G and the two X-linked myopia forms** all have L5 evidence and no identified mechanistic link. All remain on Hold.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

