---
layout: default
title: Riluzole
parent: Model Prediction Only (L5)
nav_order: 802
evidence_level: L5
indication_count: 10
---

# Riluzole
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

# Riluzole: From Amyotrophic Lateral Sclerosis to Bilateral Parasagittal Parieto-Occipital Polymicrogyria

## One-Sentence Summary

Riluzole is a glutamate-modulating neuroprotective drug. The literature in this pack describes it as the only drug shown to modestly prolong survival in amyotrophic lateral sclerosis (ALS).
The TxGNN model ranks **bilateral parasagittal parieto-occipital polymicrogyria** as its top prediction, but there are **0 clinical trials** and **0 publications** behind it, and no plausible mechanistic link. This is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALS (inferred from the literature; the Canadian license records carry no indication text) |
| Predicted New Indication | Bilateral parasagittal parieto-occipital polymicrogyria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in DrugBank for this pack. The pack's own rationale notes that riluzole inhibits glutamate release and modulates voltage-gated sodium channels. This addresses the glutamate excitotoxicity proposed in ALS pathogenesis.

Polymicrogyria is a developmental malformation of the cerebral cortex. It is not a glutamate-driven neurodegenerative process like ALS. The evidence review found **no evident mechanistic link** between riluzole's neuroprotective actions and this condition. The high TxGNN score (99.99%) is the only support for the prediction, and a high score alone does not indicate clinical plausibility.

The top-10 list is dominated by other poorly supported predictions. The motor neuron disorders (rank 3, 5, 6, 7 and 10) have an indirect, plausible link through the ALS mechanism, but none is verified. Several other entries (skeletal dysplasia, mitochondrial myopathy, retinal-dwarfism syndrome) have no plausible link. Rank 8, "amyotrophic lateral sclerosis, susceptibility to", is the only prediction with literature support. It is essentially the drug's original disease area, so it is not a true repurposing candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked indication.

For context, the 20 publications retrieved for rank 8 (ALS susceptibility) are mostly reviews, with some preclinical work. They are not RCTs:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9178165](https://pubmed.ncbi.nlm.nih.gov/9178165/) | 1997 | Review | Journal of Neurology | Glutamate excitotoxicity as a major pathophysiological mechanism of motor neuron injury in ALS |
| [21128691](https://pubmed.ncbi.nlm.nih.gov/21128691/) | 2011 | Review | CNS Drugs | Riluzole is the only medication shown to modestly prolong ALS survival |
| [20698807](https://pubmed.ncbi.nlm.nih.gov/20698807/) | 2011 | Not classified | Amyotroph Lateral Scler | Riluzole, thought to affect glutamate metabolism, improves survival only modestly; critical appraisal of ALS trial design |
| [8061281](https://pubmed.ncbi.nlm.nih.gov/8061281/) | 1994 | Preclinical | Neuroreport | Neuroprotective effects of riluzole against ALS cerebrospinal fluid toxicity in cultured neurons |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2352583 | APO-RILUZOLE |
| 2390299 | MYLAN-RILUZOLE |
| 2242763 | RILUTEK |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no clinical trials, no literature and no plausible mechanistic link, so it rests solely on the model score (evidence level L5). Rank 8 (ALS susceptibility) is the only prediction with literature support, and it overlaps with riluzole's existing use. It would be treated as a research question rather than a new indication.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data from DrugBank
- Approved indication text for the three Canadian licenses
- Preclinical or mechanistic evidence linking glutamatergic or sodium-channel modulation to cortical malformation, before any clinical consideration
- Separate review of the motor neuron disorders (Mills syndrome, monomelic amyotrophy, lower motor neuron syndrome) as the more plausible directions

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

