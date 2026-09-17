---
layout: default
title: Zuclopenthixol
parent: Model Prediction Only (L5)
nav_order: 844
evidence_level: L5
indication_count: 9
---

# Zuclopenthixol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Zuclopenthixol: From Antipsychotic Therapy to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

> Zuclopenthixol is a thioxanthene-class typical antipsychotic that acts primarily as a D1/D2 dopamine receptor antagonist, historically used for psychotic disorders such as schizophrenia (original indication text is not present in this Evidence Pack).
> The TxGNN model predicts it may be effective for **Retinal Dystrophy with or without Extraocular Anomalies**,
> but currently **0 clinical trials** and only **15 loosely related publications** (none specific to this drug-disease pair) support this direction, and the model's own scoring assigns this candidate a "Hold" recommendation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in Evidence Pack (no `original_indications` or Canadian license text available); drug class is a thioxanthene-type typical antipsychotic |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data (`original_moa`) is marked as a data gap in this Evidence Pack. However, the repurposing rationale supplied for the top-ranked candidate identifies Zuclopenthixol as a thioxanthene-class typical antipsychotic that acts mainly through D1/D2 dopamine receptor antagonism — consistent with its known clinical use for psychotic disorders such as schizophrenia.

Retinal dystrophy with or without extraocular anomalies is a congenital/hereditary ophthalmological structural disorder. The evidence pack's own mechanistic analysis explicitly states there is **no known pathophysiological link** between dopamine receptor antagonism and this retinal/ocular developmental condition. The TxGNN score is derived purely from knowledge-graph pattern similarity, not from a validated biological mechanism.

The same pattern holds across all nine ranked candidates in this pack (hydranencephaly, congenital disorder of glycosylation, Charcot-Marie-Tooth disease type 1G, several inherited myopia subtypes, polymicrogyria syndrome, and atypical glycine encephalopathy): each is a congenital, developmental, or metabolic/genetic disorder with no established connection to dopaminergic antagonism, and each carries an evidence level of L5 with a "Hold" recommendation from the scoring model itself. This strongly suggests the prediction set reflects graph-topology signal rather than a mechanistically grounded repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The 15 publications retrieved for this indication are general ophthalmology reviews and case reports on congenital/orbital anomalies; none directly studies Zuclopenthixol or antipsychotic therapy in relation to retinal dystrophy. They are listed below for transparency, but should be read as background context on the disease phenotype rather than supporting evidence for the drug-disease link.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Semin Ultrasound CT MR | Overview of orbital infections and cellulitis staging secondary to sinusitis; not disease- or drug-specific |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Semin Neurol | Clinical approach to diplopia arising from ocular, neurologic, or extraocular muscle disorders |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klin Monbl Augenheilkd | Describes simple vs. complicated congenital ptosis and associated extraocular muscle fibrosis |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan J Ophthalmol | Congenital lens shape anomalies and their embryological origin |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Doc Ophthalmol | Wagner-Stickler syndrome: vitreoretinal degeneration with extraocular systemic features |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatr Radiol | Imaging classification of pediatric ocular pathologies including congenital/developmental lesions |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case Report | Am J Ophthalmol | Two cases of unilateral cryptophthalmia with absent extraocular muscles/optic nerve |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case Report | J Neuroophthalmol | Case of congenital trochlear-oculomotor synkinesis, a rare cranial dysinnervation disorder |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Case Report | Optom Vis Sci | Case of congenital fibrosis of extraocular muscles with variable synergistic divergence |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Unclassified | Int J Mol Sci | Reports optic nerve head and retinal abnormalities in congenital fibrosis of extraocular muscles (CFEOM), a genetic dysinnervation disorder |

*(5 additional lower-priority records exist in the source pack but are omitted here for brevity; none establishes a drug-specific link.)*

---

## Canada Market Information

Zuclopenthixol is currently **not marketed** in Canada per this Evidence Pack, with 0 Drug Identification Numbers (DINs) on record.

---

## Safety Considerations

Please refer to the package insert for safety information. This Evidence Pack does not contain confirmed key warnings, contraindications, or drug-drug interaction data for Zuclopenthixol; retrieval of the official Canadian (or TFDA) product label is flagged as a blocking data gap for any further safety evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No clinical trials or drug-specific literature support any of the nine TxGNN-predicted indications; the model's own scoring assigns "L5 / Hold" to every candidate, and the mechanistic rationale explicitly finds no known pathophysiological link between dopamine receptor antagonism and the predicted congenital/hereditary conditions. Combined with the drug's non-marketed status in Canada and missing safety labeling, there is insufficient basis to advance beyond S0.

**To proceed, the following is needed:**
- Confirmed original mechanism of action (MOA) and approved indication(s) for Zuclopenthixol (currently data gaps)
- Official product label / TFDA warnings, contraindications, and drug interaction data (blocking gap, DG001)
- A mechanistically plausible hypothesis linking dopaminergic antagonism to retinal/ocular developmental disorders, ideally supported by preclinical or case-level evidence
- Reassessment once new clinical trial or targeted literature evidence becomes available for this specific drug-disease pair
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

