---
layout: default
title: Betahistine
parent: 僅模型預測 (L5)
nav_order: 97
evidence_level: L5
indication_count: 10
---

# Betahistine
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

# Betahistine: From Ménière's Disease to Restless Legs Syndrome

## One-Sentence Summary

Betahistine is a histamine analogue (H1 agonist / H3 antagonist) with established global use for Ménière's disease and vestibular vertigo, though it is not currently registered in Canada.
The TxGNN model's highest-ranked prediction is **Restless Legs Syndrome** (score 98.51%), supported by **no clinical trials** and **no publications** — placing evidence at Level L5.
However, the model's rank-6 prediction of **Peripheral Vertigo** and rank-3 prediction of **Active Vestibular Ménière's Disease** are collectively backed by a Phase 3 RCT, two Cochrane systematic reviews, a 12-study meta-analysis, and European clinical guidelines (L2), representing the most actionable repurposing opportunity in this report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Canada; established globally for Ménière's disease and vestibular vertigo |
| Predicted New Indication (#1 TxGNN) | Restless Legs Syndrome |
| TxGNN Prediction Score | 98.51% |
| Evidence Level | L5 (for Restless Legs Syndrome; L2 for Peripheral Vertigo at Rank 6) |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold (for Restless Legs Syndrome) |

> **Key Observation:** The highest-evidence prediction in this pack is **Peripheral Vertigo (Rank 6, L2, "Proceed with Guardrails")**. The narrative and evidence sections below reflect this clinical reality.

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data was not retrieved for this evidence pack. Based on established pharmacological literature, betahistine acts through two complementary pathways: **(1) H1 receptor agonism** — causing vasodilation of the labyrinthine arteries and stria vascularis vasculature, improving inner ear microcirculation, and reducing endolymphatic hydrops pressure; and **(2) H3 receptor antagonism** — removing autoinhibition at presynaptic histaminergic terminals in the lateral vestibular nuclei, augmenting histamine release, facilitating vestibular compensation, and suppressing excessive neuronal firing. These mechanisms are well-characterised across more than three decades of pharmacodynamic research.

For the rank-1 prediction of **Restless Legs Syndrome**, the core pathology involves striatal dopaminergic hypofunction and central iron metabolism disturbance. H3 receptor antagonism could theoretically modulate striatal dopamine release through presynaptic cross-regulatory mechanisms — but this represents an extremely speculative and tenuous link. The TxGNN score of 0.985 most likely reflects knowledge graph topological similarity rather than direct biological plausibility, and there is currently no preclinical, animal model, or clinical evidence to support betahistine for RLS.

The more compelling repurposing targets are the **vestibular spectrum predictions (Ranks 2–6)**. Betahistine's dual mechanism maps precisely onto the pathophysiology of Ménière's disease (endolymphatic hydrops, labyrinthine ischemia) and peripheral vestibular vertigo (impaired vestibular compensation). More than 12 double-blind placebo-controlled trials compiled in a 2014 meta-analysis — alongside European clinical guidelines (EAONO, 2018) and two Cochrane reviews (2016, 2023) — position betahistine as a reference-standard medical treatment for these conditions in countries where it is approved. Introducing betahistine to Canada for vestibular indications constitutes the genuine repurposing opportunity here.

---

## Clinical Trial Evidence

*No clinical trials were identified for the top TxGNN prediction (Restless Legs Syndrome). The following table presents evidence for **Peripheral Vertigo (Rank 6)** — the highest-evidence indication in this report.*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01759251](https://clinicaltrials.gov/study/NCT01759251) | Post-marketing (N/A) | Completed | 309 | International observational study of Betaserc® (betahistine dihydrochloride) in vestibular vertigo (Russia/Ukraine); evaluated real-world effectiveness and course of vertigo after treatment discontinuation in routine outpatient settings |
| [NCT03908567](https://clinicaltrials.gov/study/NCT03908567) | Phase 2 | Completed | 124 | TRAVERS trial: AM-125 vs. placebo for acute peripheral vertigo following neurosurgery (vestibular schwannoma resection, labyrinthectomy, vestibular neurectomy); provides validated endpoints and disease-model reference for this indication class |
| [NCT07203248](https://clinicaltrials.gov/study/NCT07203248) | N/A | Not Yet Recruiting | 2,000 | Real-world study of CGRP-targeted medications for vestibular migraine in Chinese patients; not a betahistine study — low direct relevance |
| [NCT06001047](https://clinicaltrials.gov/study/NCT06001047) | N/A | Recruiting | 120 | Head acupuncture vs. standard care for residual BPPV symptoms after canalith repositioning; non-pharmacological intervention — low direct relevance |

---

## Literature Evidence

*No literature was identified for the top TxGNN prediction (Restless Legs Syndrome). The following presents the 10 highest-quality publications supporting **Peripheral Vertigo (Rank 6)** and **Active Vestibular Ménière's Disease (Rank 3)**, which share a common evidence base.*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [36827524](https://pubmed.ncbi.nlm.nih.gov/36827524/) | 2023 | Cochrane Systematic Review | Cochrane Database Syst Rev | Comprehensive review of systemic pharmacological interventions for Ménière's disease including betahistine, diuretics, antivirals, and corticosteroids; evaluates prevention of vertigo attacks and associated symptoms |
| [40070497](https://pubmed.ncbi.nlm.nih.gov/40070497/) | 2025 | Meta-analysis | World J Otorhinolaryngol Head Neck Surg | Betahistine as add-on to Epley maneuver for BPPV; systematic review and meta-analysis demonstrates superior reduction of residual dizziness compared to maneuver alone |
| [26797774](https://pubmed.ncbi.nlm.nih.gov/26797774/) | 2016 | Phase 3 RCT | BMJ | BEMED trial: long-term, multicentre, double-blind, placebo-controlled, dose-defining trial of betahistine dihydrochloride; primary endpoint was vertigo attack incidence in Ménière's disease |
| [30256205](https://pubmed.ncbi.nlm.nih.gov/30256205/) | 2018 | Clinical Practice Guideline | J Int Adv Otology | European Academy of Otology and Neurotology (EAONO) position statement on Ménière's disease diagnosis and treatment; endorses betahistine as first-line pharmacological therapy |
| [23778722](https://pubmed.ncbi.nlm.nih.gov/23778722/) | 2014 | Meta-analysis | Eur Arch Otorhinolaryngol | Pooled analysis of 12 double-blind, placebo-controlled RCTs of betahistine in vestibular vertigo and Ménière's disease; demonstrates significant odds ratio in favour of betahistine for overall treatment response |
| [27327415](https://pubmed.ncbi.nlm.nih.gov/27327415/) | 2016 | Cochrane Systematic Review | Cochrane Database Syst Rev | Betahistine vs. placebo for vertigo symptoms of multiple aetiologies; examines whether improved labyrinthine blood flow translates to clinical benefit |
| [26245698](https://pubmed.ncbi.nlm.nih.gov/26245698/) | 2015 | Review | Acta Oto-Laryngologica | Clinical studies and meta-analyses confirm betahistine's safety and efficacy in Ménière's disease, BPPV, vestibular neuronitis, and other peripheral vertigo types |
| [31111729](https://pubmed.ncbi.nlm.nih.gov/31111729/) | 2020 | Prospective Cohort | Ear Nose Throat J | Real-world study of betahistine 48 mg/day for peripheral vestibular vertigo in primary care (Colombia, N=150); demonstrates clinical effectiveness, safety, and symptom reduction at 8 weeks |
| [24177346](https://pubmed.ncbi.nlm.nih.gov/24177346/) | 2013 | Review | J Vestibular Research | Clarifies betahistine's dual mechanisms — H1-mediated inner ear vasodilation and H3-mediated enhancement of vestibular compensation — as the basis for symptomatic vertigo relief |
| [7113814](https://pubmed.ncbi.nlm.nih.gov/7113814/) | 1982 | Long-term RCT | Adv Otorhinolaryngol | 12–14-year continuous betahistine HCl treatment in Ménière's disease; >80% long-term success rate, no drug tolerance observed, effective in patients who had failed prior therapies |

---

## Canada Market Information

Betahistine (DB06698) is **not currently marketed in Canada**. Health Canada has issued no Drug Identification Numbers (DINs) for any betahistine-containing product. The drug is approved and marketed in over 100 countries — including all EU member states, Japan, China, and many others — for vestibular disorders, but has not received Health Canada market authorisation. No Canadian product monograph is available.

---

## Safety Considerations

Please refer to the package insert for safety information. No Canadian product monograph exists, and no key warnings, contraindications, or drug interaction data were retrieved in this evidence pack. Based on international prescribing information and pharmacological literature:

- **Drug Interactions:** Betahistine is a structural histamine analogue; H1 antihistamines (e.g., dimenhydrinate, meclizine, diphenhydramine) may pharmacodynamically antagonise betahistine's therapeutic effects and should not be co-administered
- International prescribing information notes caution in patients with **peptic ulcer disease** (theoretical H1-mediated gastric acid stimulation) and **bronchial asthma** (potential histaminergic bronchospasm risk)

---

## Conclusion and Next Steps

**Decision: Hold (for Restless Legs Syndrome) | Proceed with Guardrails (for Peripheral Vertigo / Vestibular Ménière's Disease)**

**Rationale:**
The TxGNN rank-1 prediction of Restless Legs Syndrome is unsupported by any clinical or preclinical evidence (L5) and rests on a speculative mechanistic link; a "Hold" decision is appropriate until any preliminary data emerge. The genuine opportunity identified in this report is the **introduction of betahistine to Canada for vestibular indications** — specifically Peripheral Vertigo (Rank 6) and Active Vestibular Ménière's Disease (Rank 3) — where an L2 evidence base from Phase 3 RCTs, two Cochrane reviews, and European clinical guidelines supports a "Proceed with Guardrails" recommendation.

**To proceed (for Peripheral Vertigo / Vestibular Ménière's Disease in Canada), the following is needed:**
- Obtain full MOA documentation from DrugBank to complete the mechanistic regulatory dossier (Data Gap DG002)
- Retrieve and review international product monographs (EU SmPC, Japanese package insert) for warnings, contraindications, and risk minimisation measures pending a Canadian monograph (Data Gap DG001)
- Conduct Health Canada regulatory pathway assessment: New Drug Submission (NDS) strategy, including whether foreign approval data (EU/Japan) can support an expedited review under existing policy
- Pharmacoeconomic analysis comparing betahistine against current Canadian standard-of-care for vestibular vertigo (dimenhydrinate, meclizine, prochlorperazine)
- Canadian clinical practice guideline alignment review to define positioning within otolaryngology and neurology workflows
- For Restless Legs Syndrome specifically: seek any preclinical mechanistic evidence linking H3 antagonism to striatal dopamine modulation before escalating to clinical investigation

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

