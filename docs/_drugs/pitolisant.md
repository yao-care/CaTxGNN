---
layout: default
title: Pitolisant
parent: Model Prediction Only (L5)
nav_order: 744
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
monitor_inn: "Pitolisant"
predicted_indications: ["insomnia (disease)", "attention deficit-hyperactivity disorder", "faciodigitogenital syndrome"]
description: "Pitolisant: predicted new indication Insomnia (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Pitolisant
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Pitolisant: Insomnia (disease)
{: .text-alpha }

## One-Sentence Summary

Pitolisant is a histamine H3 receptor inverse agonist, originally used to treat narcolepsy (with or without cataplexy).
The TxGNN model predicts it may be effective for **insomnia**, but there are **no registered clinical trials** and the **10 publications** compiled concern narcolepsy and related sleep disorders rather than insomnia itself.
The prediction is mechanistically questionable, because pitolisant is a wake-promoting drug and insomnia is a known adverse effect of it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 (no trials; mechanism and review-level literature only) |
| Canada Market Status | Marketed (valid licenses: 2 of 2) |
| Number of DINs | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. From the literature, pitolisant is a selective histamine H3 receptor antagonist/inverse agonist. By blocking the H3 autoreceptor, it increases histamine release in the brain and promotes wakefulness. That is why it works for excessive daytime sleepiness in narcolepsy.

The relationship between the original and predicted indications is weak. Both are sleep-wake disorders, which is likely why the TxGNN model (deep learning) links them. However, they call for opposite pharmacological effects. Narcolepsy treatment needs more arousal, while insomnia treatment needs less. Enhancing histaminergic signaling would more plausibly worsen insomnia, and insomnia is a recognized side effect of pitolisant. The high score (0.9971) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, so it is not a true therapeutic rationale. Any benefit would probably be limited to indirect situations, such as residual daytime sleepiness in related sleep disorders.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the publications below tests pitolisant in insomnia. They are included as the closest available evidence on pitolisant and sleep-wake disorders.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36931805](https://pubmed.ncbi.nlm.nih.gov/36931805/) | 2023 | RCT | The Lancet. Neurology | Phase 3 double-blind, placebo-controlled trial of pitolisant in children aged 6 and older with narcolepsy, with or without cataplexy |
| [33121980](https://pubmed.ncbi.nlm.nih.gov/33121980/) | 2021 | RCT | Chest | Pitolisant for residual excessive daytime sleepiness in sleep apnoea patients adherent to CPAP |
| [31917607](https://pubmed.ncbi.nlm.nih.gov/31917607/) | 2020 | RCT | Am J Respir Crit Care Med | Pitolisant for daytime sleepiness in moderate to severe sleep apnoea patients who refuse CPAP |
| [36169322](https://pubmed.ncbi.nlm.nih.gov/36169322/) | 2022 | Cohort | Revista de neurologia | Real-life WAKE study of pitolisant in type 1 narcolepsy patients unresponsive to previous treatments |
| [41588264](https://pubmed.ncbi.nlm.nih.gov/41588264/) | 2026 | Cohort | Neurological Sciences | Real-world study of pitolisant in 40 Chinese children with narcolepsy |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Review | Drug Des Devel Ther | Profile of pitolisant in narcolepsy management: design, development and place in therapy |
| [34521328](https://pubmed.ncbi.nlm.nih.gov/34521328/) | 2022 | Review | Current Neuropharmacology | Histaminergic system changes in neuropsychiatric disorders; pitolisant for narcolepsy sleepiness, doxepin (an H1 antagonist) for insomnia |
| [42525367](https://pubmed.ncbi.nlm.nih.gov/42525367/) | 2026 | Review | Neurology and Therapy | Current and emerging therapies for paediatric sleep disorders, including insomnia and narcolepsy |
| [34225942](https://pubmed.ncbi.nlm.nih.gov/34225942/) | 2021 | Review | Handbook of Clinical Neurology | Overview of histamine receptors, agonists and antagonists in health and disease |
| [22356925](https://pubmed.ncbi.nlm.nih.gov/22356925/) | 2012 | Review | Clinical Neuropharmacology | Pitolisant as an alternative stimulant for teenagers with narcolepsy-cataplexy and refractory sleepiness |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02516268 | WAKIX | Not specified | Not specified |
| 02516241 | WAKIX | Not specified | Not specified |

---

## Safety Considerations

- **Drug Interactions**: 100 potential interactions were identified in the interaction screening. Examples of **Major** interactions are **bupropion** and **dolasetron**. Examples of **Moderate** interactions include famotidine, cimetidine, hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone, metformin, morphine, acetylsalicylic acid, clarithromycin, loperamide, empagliflozin and eliglustat.
- **Insomnia as an adverse effect**: The mechanistic assessment notes that insomnia is a known adverse effect of pitolisant. This is directly relevant to the proposed indication.

Please refer to the package insert for warnings and contraindications, which were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trial support and no insomnia-specific literature. Pitolisant's wake-promoting mechanism runs opposite to what insomnia treatment requires, and insomnia is a known side effect. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence or a therapeutic rationale.

**To proceed, the following is needed:**
- A clear mechanistic argument for why H3 inverse agonism would help insomnia, or evidence that it would not worsen it
- Preclinical or early clinical data in insomnia populations
- Health Canada package insert warnings and contraindications, which are required before safety screening
- Mechanism of action data confirmed from DrugBank
- Review of the major interactions (bupropion, dolasetron) for any proposed use

**Other predicted indications (for reference):**
- **Attention deficit-hyperactivity disorder (score 0.9936, L4, research question):** H3 antagonism increases release of histamine, acetylcholine, norepinephrine and dopamine in the prefrontal cortex, which is a plausible basis for improving attention. Support is limited to preclinical and review-level literature, with no ADHD-specific pitolisant trials. Pediatric narcolepsy data show tolerability in children. This is a reasonable hypothesis worth a dedicated study.
- **Faciodigitogenital syndrome (score 0.9929, L5, Hold):** This rare X-linked developmental disorder (caused by FGD1 mutations) has no plausible link to H3 receptor modulation. There are no trials or literature, so this is likely a prediction artifact.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

