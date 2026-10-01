---
layout: default
title: Piroxicam
parent: Model Prediction Only (L5)
nav_order: 736
evidence_level: L5
indication_count: 10
---

# Piroxicam
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

# Piroxicam: From Marketed NSAID to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Piroxicam is a non-selective COX inhibitor (an NSAID) that is marketed in Canada under 4 DINs. The TxGNN model's top-ranked prediction is **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, an ultra-rare developmental malformation syndrome, but **0 clinical trials** and **0 publications** support it. Of the 10 predictions in this pack, only **juvenile idiopathic arthritis** has supporting literature, and that is covered below.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 99.996% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the pack. Piroxicam is described as a non-selective COX-1/COX-2 inhibitor that reduces prostaglandin-mediated inflammation, pain and stiffness. Its approved indication text was also not available.

**For the top-ranked prediction, the mechanism does not support the link.** The syndrome is an ultra-rare developmental malformation with no inflammatory driver, so COX inhibition has no plausible target. The score of 99.996% most likely reflects knowledge-graph topology, not biology. The other top-ranked predictions show the same pattern:

- Brachydactyly-syndactyly syndrome
- Acromesomelic dysplasia, Hunter-Thompson type
- Brachyolmia-amelogenesis imperfecta syndrome
- Brachyolmia
- Pseudoachondroplasia
- WHIM syndrome

**Juvenile idiopathic arthritis (JIA) is the one biologically coherent candidate.** It ranks 10th, with a score of 99.93%. NSAIDs are an established symptomatic therapy class for JIA. Direct piroxicam studies exist, but they are old (1986–1987), and the available metadata do not confirm trial phase or randomisation. Network meta-analyses of NSAIDs in JIA (2021, 2024) add class-level context. Piroxicam is not disease-modifying, so any role would be symptomatic. Evidence level for JIA is L3.

## Clinical Trial Evidence

Currently no related clinical trials registered. This also applies to JIA, where no registered trials were found.

## Literature Evidence

Currently no related literature available for the top-ranked prediction.

The most relevant publications for JIA, the only candidate with direct piroxicam data, are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3510686](https://pubmed.ncbi.nlm.nih.gov/3510686/) | 1986 | Comparative clinical study | Br J Rheumatol | 8-week double-blind crossover of piroxicam vs naproxen in 47 children with seronegative juvenile chronic arthritis. No significant difference between treatments was reported. |
| [2957205](https://pubmed.ncbi.nlm.nih.gov/2957205/) | 1987 | Clinical study | Eur J Rheumatol Inflamm | 26 patients (age 3–25) randomised to piroxicam or naproxen in juvenile rheumatoid arthritis. Painful and swollen joint counts decreased significantly. |
| [1782984](https://pubmed.ncbi.nlm.nih.gov/1782984/) | 1991 | Pharmacokinetic study | Eur J Clin Pharmacol | Steady-state piroxicam in 10 children with rheumatic diseases. Mean half-life was about 32.6 hours. |
| [38680254](https://pubmed.ncbi.nlm.nih.gov/38680254/) | 2024 | Systematic review / network meta-analysis | World J Clin Cases | Compares NSAIDs for JIA (class-level context). |
| [33632948](https://pubmed.ncbi.nlm.nih.gov/33632948/) | 2021 | Systematic review / network meta-analysis | Indian Pediatr | Compares the efficacy and safety of nine NSAIDs in JIA (class-level context). |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 642894 | APO PIROXICAM CAP 20MG |
| 695718 | TEVA-PIROXICAM |
| 642886 | APO PIROXICAM CAP 10MG |
| 695696 | TEVA-PIROXICAM |

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the queried source.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction is a model output with no trial, literature or mechanistic support, so it is not actionable. The same applies to the other developmental and skeletal syndromes in the top ranks. JIA is the only candidate worth following up. It sits at L3, with a Research Question recommendation, and any role would be symptomatic.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data from DrugBank
- Approved indication text for the 4 DINs
- For JIA, confirmation of whether the 1986 piroxicam vs naproxen study was a controlled trial, which could raise the evidence level to L2
- For JIA, a review of piroxicam against other NSAIDs in children, including the network meta-analyses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

