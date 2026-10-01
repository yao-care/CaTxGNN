---
layout: default
title: Baclofen
parent: Model Prediction Only (L5)
nav_order: 93
evidence_level: L5
indication_count: 2
---

# Baclofen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Baclofen: From Spasticity to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Baclofen is a GABA-B receptor agonist that is marketed in Canada, and it is generally used for spasticity. The supplied data does not state its approved indication.
The TxGNN model predicts it may be useful for **attention deficit-hyperactivity disorder (ADHD)**, but this rests on a model score alone: **0 clinical trials** are registered and **none of the 10 listed publications tests baclofen in ADHD**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied data (baclofen is generally used for spasticity) |
| Predicted New Indication | Attention deficit-hyperactivity disorder |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L5 (model prediction only, no actual studies) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not supplied for this report. Baclofen is known to be a GABA-B receptor agonist. Its efficacy in its original indication is established, and mechanistically it may be relevant to ADHD.

Possible links to ADHD include modulation of dopaminergic and glutamatergic tone and of the brain circuits that control impulsivity. A second link is baclofen's off-label use in tic disorders such as Tourette syndrome, which often co-occur with ADHD.

These links are hypotheses, not findings. The supplied literature does not test baclofen in ADHD. The papers are reviews of Tourette syndrome and of autism mood stabilizers, plus rodent studies of impulsivity and noradrenergic signalling. The very high TxGNN score (0.993) is a knowledge-graph prediction and is not backed by any registered trial.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Nothing below tests baclofen in ADHD. The table lists the 10 supplied publications. Reviews come first, then a clinical series, then the remaining items.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26366961](https://pubmed.ncbi.nlm.nih.gov/26366961/) | 2015 | Review | Clin Neuropharmacol | Mood stabilizers for irritability and attention-deficit behaviours in children and adolescents with autism spectrum disorders; not baclofen-specific for ADHD |
| [11393328](https://pubmed.ncbi.nlm.nih.gov/11393328/) | 2001 | Review | Paediatr Drugs | Clinical features and management of Tourette syndrome, including psychiatric comorbidities such as ADHD |
| [24295630](https://pubmed.ncbi.nlm.nih.gov/24295630/) | 2013 | Review | Int Rev Neurobiol | Emerging treatments for Tourette syndrome, whose behavioural problems include ADHD |
| [35345730](https://pubmed.ncbi.nlm.nih.gov/35345730/) | 2022 | Review | Cureus | Behavioural intervention, antipsychotics and alpha agonists for tics in Tourette syndrome |
| [10342599](https://pubmed.ncbi.nlm.nih.gov/10342599/) | 1999 | Clinical series (classified as Review) | J Child Neurol | 450 patients with tics/Tourette syndrome treated with baclofen/botulinum toxin type A and rated on the Yale Global Tic Severity Scale; concerns tics, not ADHD |
| [30122296](https://pubmed.ncbi.nlm.nih.gov/30122296/) | 2019 | Observational | L'Encephale | Supervised off-label methylphenidate prescribing in adult ADHD; not about baclofen |
| [24062084](https://pubmed.ncbi.nlm.nih.gov/24062084/) | 2014 | Preclinical (animal) | Psychopharmacology | Stimulating α2A-adrenergic receptors in the rat ventral hippocampus (guanfacine) reduced impulsive decision-making |
| [21300040](https://pubmed.ncbi.nlm.nih.gov/21300040/) | 2011 | Preclinical (animal) | Brain Res | EEG responses to neurotransmitter agonists in spontaneously hypertensive rats (an ADHD model) versus kainate-treated rats |
| [24496320](https://pubmed.ncbi.nlm.nih.gov/24496320/) | 2014 | Preclinical (animal) | Neuropsychopharmacology | Roles of the anterior cingulate cortex and basolateral amygdala in effort-based decision-making in rodents |
| [24103016](https://pubmed.ncbi.nlm.nih.gov/24103016/) | 2013 | Preclinical (animal) | Eur J Neurosci | Habenula integrity is needed for social play behaviour in rats |

---

## Canada Market Information

Five of the 20 authorizations are listed. Dosage form and approved-indication text were not supplied.

| DIN | Product Name |
|---------|------|
| 02242151 | RIVA-BACLOFEN |
| 02544490 | JAMP BACLOFEN |
| 02287048 | BACLOFEN |
| 02413639 | BACLOFEN INJECTION |
| 02063743 | PMS-BACLOFEN |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The ADHD prediction is supported only by the model score (L5). There are no registered trials, and the supplied literature is indirect, consisting of Tourette/tic reviews and rodent studies.

**To proceed, the following is needed:**
- Any direct evidence of baclofen in ADHD, such as clinical trials or human studies
- Detailed mechanism-of-action data for baclofen and an analysis linking it to ADHD
- Health Canada package insert warnings and contraindications, needed before safety screening
- Approved-indication text and dosage forms for the Canadian licenses

**Note:** The second-ranked prediction, **nicotine dependence** (TxGNN score 99.19%, evidence level L2), has three Phase 2 trials, but two were terminated early and none has reported efficacy results. It may deserve separate follow-up.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

