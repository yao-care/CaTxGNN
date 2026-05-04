---
layout: default
title: Asenapine
parent: 僅模型預測 (L5)
nav_order: 68
evidence_level: L5
indication_count: 10
---

# Asenapine
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

# Asenapine: From Schizophrenia/Bipolar I Disorder to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

Asenapine is a second-generation (atypical) antipsychotic currently approved in multiple markets for the acute treatment of schizophrenia and manic or mixed episodes associated with bipolar I disorder.
The TxGNN model predicts it may be effective for **Retinal Dystrophy with or without Extraocular Anomalies**,
with **0 clinical trials** and **15 publications** (of indirect relevance only) currently supporting this direction.
This is a highly speculative, hypothesis-generating prediction that requires substantial preclinical validation before any clinical consideration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia; Bipolar I Disorder (manic/mixed episodes) |
| Predicted New Indication | Retinal Dystrophy with or without Extraocular Anomalies |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data is not available in this evidence pack. Based on published literature included in the evidence review, asenapine is a multi-receptor atypical antipsychotic with higher binding affinity for serotonin 5-HT₂A receptors than for dopamine D₂ receptors — a profile shared with other second-generation antipsychotics. It also exerts activity at D₄, H₁, α₁/α₂ adrenergic, and multiple serotonin receptor subtypes (5-HT₁A, 2C, 6, 7), giving it a broad pharmacodynamic footprint relevant to mood and psychosis regulation.

The hypothesized mechanistic link to retinal dystrophy is based on the fact that the retina contains dopaminergic amacrine cells that express D₄ receptors, which play a role in photoreceptor light-adaptation signalling. Asenapine's D₂/D₄ antagonism could theoretically modulate retinal dopaminergic neurotransmission and thereby influence photoreceptor function. However, the known effects of D₂ receptor blockade on ocular physiology — particularly on axial eye growth — appear directionally inconsistent with a therapeutic benefit in retinal dystrophy. No preclinical or clinical data currently supports this connection.

In summary, this prediction is most likely an artefact of indirect knowledge-graph connections via shared "neurological/sensory disorder" nodes in TxGNN, rather than a pharmacologically grounded hypothesis. It should be treated as a signal requiring mechanistic investigation before further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for asenapine in retinal dystrophy or extraocular anomalies.

---

## Literature Evidence

> **Important caveat**: The 15 publications retrieved are not studies of asenapine in retinal dystrophy. They were returned based on keyword overlap with "extraocular anomalies" and represent general ophthalmology background literature. None constitute drug-specific evidence for this repurposing prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Differential diagnosis of pediatric ocular pathologies including congenital retinal lesions, Coats disease, and retinopathy of prematurity |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | Congenital anomalies of lens shape; may involve anterior segment dysgenesis or persistence of tunica vasculosa lentis |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Original Article | International Journal of Molecular Sciences | Optic nerve head and retinal abnormalities in congenital fibrosis of extraocular muscles (CFEOM); KIF21A and TUBB3 mutations |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | Journal of Binocular Vision and Ocular Motility | Overview of congenital cranial dysinnervation disorders (CCDDs) and their ophthalmoplegia phenotypes |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Original Article | American Journal of Ophthalmology | Unifying theory for maculopathy pathogenesis in cavitary optic disc anomalies; proposed permanent cure approach |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case Report | Journal of Neuro-Ophthalmology | Isolated trochlear-oculomotor synkinesis in a 6-year-old; discussion of congenital cranial dysinnervation pathophysiology |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klinische Monatsblätter für Augenheilkunde | Simple vs. complicated congenital ptosis; association with refractive errors and binocular vision disturbance |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Clinical Pearl | Seminars in Neurology | Systematic approach to diplopia evaluation covering ocular, neurologic, and extraocular muscle disorders |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Case Series | Documenta Ophthalmologica | Wagner-Stickler syndrome: vitreoretinal degeneration with myopia, cataract, and systemic extraocular manifestations |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case Series | American Journal of Ophthalmology | Two cases of unilateral cryptophthalmia with deformed orbit and absent intraocular structures |

---

## Canada Market Information

Asenapine is currently **not marketed in Canada**. No Drug Identification Numbers (DINs) are on record with Health Canada. There are no approved product listings, dosage forms, or labelled indications available through Canadian regulatory channels at this time.

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction data are available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.77%), the evidence level is L5 — meaning this prediction rests entirely on the computational model with no supporting clinical trials, no direct mechanistic studies, and no relevant published literature linking asenapine to retinal dystrophy. The proposed mechanistic pathway (D₄ receptor modulation in retinal amacrine cells) is biologically plausible in principle but has not been explored experimentally, and the known directionality of D₂ antagonism in ocular biology raises a potential safety concern rather than a therapeutic signal.

**To proceed, the following is needed:**
- Preclinical in vitro and in vivo studies assessing asenapine's effect on retinal dopaminergic signalling and photoreceptor function (e.g., electroretinography in dystrophy animal models)
- Targeted literature review on the role of D₄ receptors in human retinal dystrophy pathogenesis
- Retrospective review of ocular adverse events in existing asenapine clinical trial datasets to identify any inadvertent retinal signals
- Mechanistic clarification of whether D₂/D₄ antagonism can protect or preserve photoreceptors in hereditary dystrophy models

> **Note on higher-priority prediction**: Among all 10 TxGNN predictions for asenapine in this evidence pack, **Major Affective Disorder (Rank 10)** carries the highest clinical actionability — with 4 completed Phase 3 RCTs, meta-analytic evidence, and an Evidence Level of **L1 (Proceed with Guardrails)**. This reflects asenapine's well-established approved use for bipolar I disorder and schizophrenia. A separate, dedicated report for that indication is recommended as the primary repurposing evaluation for this drug.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

