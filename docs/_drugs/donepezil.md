---
layout: default
title: Donepezil
parent: Model Prediction Only (L5)
nav_order: 298
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-13
description: "Donepezil: predicted new indication Psychogenic movement disorders (evidence level L5). Approved use: Alzheimer disease"
---

# Donepezil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Donepezil: From Alzheimer Disease to Psychogenic Movement Disorders

## One-Sentence Summary

Donepezil is a drug originally used to treat Alzheimer disease.
The TxGNN model predicts it may be effective for **psychogenic movement disorders**, but this top-ranked prediction currently has **no registered clinical trials and no publications** behind it.
The best-supported related directions among the other predictions are **chronic tic disorder** (5 publications, mostly small or preclinical) and **tardive and other extrapyramidal movement disorders** (including Cochrane reviews of cholinergic drugs).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Alzheimer disease (the Canadian licence records list no indication text; this indication comes from the knowledge-graph data) |
| Predicted New Indication | Psychogenic movement disorders |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Based on general knowledge, donepezil is an acetylcholinesterase inhibitor that raises cholinergic signalling in the brain. Its efficacy in Alzheimer disease is established, and mechanistically it could influence the dopamine-acetylcholine balance in the striatum, which matters in many movement disorders.

For the top-ranked prediction, psychogenic movement disorders, this link is speculative. These conditions are functional in origin, and there is no established pharmacological target for donepezil. The high TxGNN score (99.23%) is a model output only and is not supported by any trial or publication.

Other predictions have more plausible rationale:
- **Chronic tic disorder (rank 2, score 99.19%):** Cholinergic interneurons in the striatum modulate the dopaminergic circuits implicated in tics. Mouse studies and small human reports point in this direction.
- **Extrapyramidal and movement disease (rank 4) and lingual-facial-buccal dyskinesia (rank 8):** A cholinergic-deficiency hypothesis underlies the use of cholinergic drugs in tardive dyskinesia. However, donepezil can also cause or worsen movement disorders, so the signal is mixed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for psychogenic movement disorders. No trials were registered for the other top predictions either.

---

## Literature Evidence

No literature is available for psychogenic movement disorders. The most relevant publications found for the neighbouring predictions are listed below, and they should be read as supporting related directions, not the top-ranked prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29553158](https://pubmed.ncbi.nlm.nih.gov/29553158/) | 2018 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Cholinergic medication for antipsychotic-induced tardive dyskinesia; covers cholinergic agents broadly (tardive dyskinesia) |
| [12137608](https://pubmed.ncbi.nlm.nih.gov/12137608/) | 2002 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Earlier version of the review of cholinergic drugs for neuroleptic-induced tardive dyskinesia |
| [15610922](https://pubmed.ncbi.nlm.nih.gov/15610922/) | 2004 | Meta-analysis of RCTs | Prog Neuropsychopharmacol Biol Psychiatry | Systematic review of cholinergic drugs, including donepezil, for tardive dyskinesia |
| [40224553](https://pubmed.ncbi.nlm.nih.gov/40224553/) | 2025 | Systematic review (safety) | Brain Circ | Reviews movement disorders associated with cholinesterase inhibitors in Alzheimer's dementia; a safety signal |
| [18343255](https://pubmed.ncbi.nlm.nih.gov/18343255/) | 2008 | Open-label study | Clin Ther | 18-week dose-escalating study of donepezil in children and adolescents with tics and ADHD (chronic tic disorder) |
| [15669896](https://pubmed.ncbi.nlm.nih.gov/15669896/) | 2005 | Clinical study (small) | J Clin Psychiatry | Donepezil reported to be beneficial in elderly patients with tardive movement disorders |
| [16364675](https://pubmed.ncbi.nlm.nih.gov/16364675/) | 2006 | Clinical report | Parkinsonism Relat Disord | Treatment of levodopa-induced dyskinesias with donepezil |
| [19142126](https://pubmed.ncbi.nlm.nih.gov/19142126/) | 2009 | Clinical study | J Clin Psychopharmacol | Effect of donepezil on tardive dyskinesia |
| [10440471](https://pubmed.ncbi.nlm.nih.gov/10440471/) | 1999 | Case report/small series | J Clin Psychopharmacol | Donepezil for Tourette's disorder and ADHD |
| [24127392](https://pubmed.ncbi.nlm.nih.gov/24127392/) | 2014 | Pharmacovigilance study | Pharmacotherapy | Cholinesterase inhibitors and reports of Pisa syndrome (a safety signal) |

---

## Canada Market Information

Donepezil has 20 valid single-ingredient licences in Canada (no cancelled licences). The licence records compiled for this report do not include dosage form or approved indication text. Main authorizations:

| DIN | Product Name |
|---------|------|
| 02232044 | ARICEPT |
| 02232043 | ARICEPT |
| 02362279 | APO-DONEPEZIL |
| 02328682 | SANDOZ DONEPEZIL |
| 02340615 | TEVA-DONEPEZIL |

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text):** epilepsy, asthma (including intrinsic and allergic asthma), bladder neck obstruction, active peptic ulcer disease, sick sinus syndrome (including the familial form), and atrioventricular block.
- **Movement-disorder safety signal:** Published reports and a 2025 systematic review link cholinesterase inhibitors to new or worsened movement disorders (for example Pisa syndrome and jaw tremor). This matters directly for any movement-disorder indication.
- **Drug interactions:** 100 interactions were found in the DDI query. The one **Major** interaction listed is **bupropion**. Many **Moderate** interactions involve anticholinergic or related drugs (atropine, hyoscyamine, glycopyrronium, clidinium, dicyclomine), acid-suppressing H2 blockers (famotidine, ranitidine, cimetidine), and others such as loperamide, dexamethasone, metronidazole, and dolasetron. Minor interactions include aspirin, aprepitant, clarithromycin, and lorcaserin.

Please also refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, psychogenic movement disorders, is supported only by the model score (L5), with no trials or publications and no plausible pharmacological rationale. Related directions, particularly chronic tic disorder and tardive dyskinesia (both L3, "Research Question"), have some preliminary evidence, but it is small-scale, preclinical, or indirect, and donepezil may itself cause movement disorders.

**To proceed, the following is needed:**
- Mechanism of action data for donepezil
- Package insert warnings and contraindications from Health Canada
- Full-text review of the tic-disorder studies (PMID 18343255) and the Cochrane reviews to confirm study designs and donepezil-specific findings
- Consideration of re-prioritizing the evaluation toward chronic tic disorder or tardive dyskinesia, where evidence is stronger
- A benefit-risk assessment addressing donepezil's potential to worsen movement disorders and the knowledge-graph contraindications (cardiac conduction, epilepsy, asthma)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

