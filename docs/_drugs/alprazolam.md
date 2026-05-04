---
layout: default
title: Alprazolam
parent: 僅模型預測 (L5)
nav_order: 38
evidence_level: L5
indication_count: 3
---

# Alprazolam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Alprazolam: From Anxiety Disorders to Insomnia

## One-Sentence Summary

Alprazolam is a benzodiazepine with globally established use for anxiety disorders and panic disorder, though it currently holds no marketing authorization in Canada.
The TxGNN model predicts it may be effective for **Insomnia**, with **7 clinical trials** and **18 publications** identified in support of this direction — though most trials carry limited direct relevance to insomnia as a standalone primary indication.
The overall evidence reflects real-world co-use patterns and off-label practice rather than dedicated regulatory-grade studies for insomnia, placing this candidate at Evidence Level L3 with a current **Hold** recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not marketed in Canada; globally known for anxiety disorders and panic disorder |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L3 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the current data sources. Based on published pharmacological knowledge, alprazolam belongs to the benzodiazepine class and acts as a positive allosteric modulator of GABA-A receptors, particularly at the α1 subunit. Activation of this subunit enhances GABAergic inhibitory transmission throughout the central nervous system, producing sedative and hypnotic effects. α1 subunit activation is associated with increased N3 slow-wave sleep, which explains the well-recognised short-term sleep-onset benefit seen in clinical practice.

However, the same mechanism introduces important limitations for insomnia as a chronic indication. Alprazolam simultaneously suppresses REM sleep, which is critical for memory consolidation and emotional regulation. With repeated administration, pharmacodynamic tolerance develops at the GABA-A receptor, and abrupt or rapid discontinuation frequently triggers rebound insomnia — a paradoxical worsening of the very symptom being treated. This rebound effect is dose- and duration-dependent and represents the central mechanistic barrier to repositioning alprazolam as a first-line insomnia therapy.

The TxGNN prediction is nonetheless mechanistically coherent: insomnia and anxiety disorders share overlapping neurobiological substrates (amygdala hyperactivation, dysregulated hypothalamic-pituitary-adrenal axis, and cortical arousal), and benzodiazepines are empirically used off-label for short-term sleep management. The prediction likely reflects this well-documented real-world co-use pattern rather than a novel indication opportunity. Current evidence and mechanistic understanding support short-term sedation, but do not support formal repositioning for chronic insomnia management.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | Unknown | 1,400 | Prospective cohort study directly examining risk–benefit profiles of hypnotics (including benzodiazepines) for sleep disorders in elderly Taiwanese patients; evaluates medication use patterns, efficacy, safety, and pharmacokinetic/pharmacogenetic characteristics — the most directly relevant trial in this set |
| [NCT00266409](https://clinicaltrials.gov/study/NCT00266409) | Phase 4 | Completed | 418 | Open-label trial comparing time to anxiety-symptom response with Niravam™ (alprazolam ODT) added to a newly initiated SSRI/SNRI versus SSRI/SNRI alone in GAD or panic disorder; provides safety and tolerability data in a large cohort with sleep-related anxiety symptoms |
| [NCT01584440](https://clinicaltrials.gov/study/NCT01584440) | Phase 2 | Completed | 220 | Randomised double-blind placebo-controlled study of AVP-923 (dextromethorphan/quinidine) for agitation in Alzheimer's disease; large, well-designed RCT in a population where sleep-related outcomes overlap with agitation — indirect evidence for benzodiazepine class comparator |
| [NCT04572750](https://clinicaltrials.gov/study/NCT04572750) | N/A | Completed | 170 | Electronic self-management intervention to support benzodiazepine (including Xanax/alprazolam) cessation in US Veterans prescribed BZDs for anxiety and insomnia; reflects the real-world context of insomnia as a core indication driving BZD prescribing |
| [NCT03327506](https://clinicaltrials.gov/study/NCT03327506) | Phase 4 | Unknown | 128 | RCT comparing hypnosis versus alprazolam pre-medication for perioperative anxiety in gynaecological surgery; single-dose perioperative use context — not applicable to chronic insomnia |
| [NCT01146600](https://clinicaltrials.gov/study/NCT01146600) | Phase 2 | Completed | 26 | Phase 2 study of clarithromycin for hypersomnia; not alprazolam-specific and addresses the opposite sleep disorder (excessive daytime sleepiness) — minimal relevance |
| [NCT01893632](https://clinicaltrials.gov/study/NCT01893632) | Phase 2 | Terminated | 2 | Gabapentin for benzodiazepine dependence withdrawal; trial terminated early with only 2 participants enrolled — no analytical value for insomnia indication |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [39183410](https://pubmed.ncbi.nlm.nih.gov/39183410/) | 2024 | RCT (Integrative) | Medicine | Retrospective observational study of 116 patients with coronary heart disease and insomnia; alprazolam served as the control arm while the experimental arm received Du Meridian moxibustion plus ear acupuncture — directly documents alprazolam use for insomnia comorbid with cardiac disease |
| [33403184](https://pubmed.ncbi.nlm.nih.gov/33403184/) | 2020 | Comparative Study | Cureus | Head-to-head comparison of alprazolam versus melatonin for sleep disturbances in end-stage renal disease patients on haemodialysis; alprazolam used explicitly as the active comparator for insomnia in a medically complex population |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta-analysis | Acta Pharmaceutica | Systematic review and meta-analysis of randomised, case-control, and prospective studies on tranquilizer use (including benzodiazepines) in elderly patients with chronic non-communicable diseases; assesses dose optimisation, efficacy, and adverse effect profiles relevant to long-term insomnia management |
| [37801512](https://pubmed.ncbi.nlm.nih.gov/37801512/) | 2023 | Preclinical | Aging | Proteomic analysis of hippocampal changes in mice after 24-day repeated alprazolam administration; identifies mitochondrial dysfunction as the mechanism underlying alprazolam-induced memory impairment — key safety signal for chronic use in insomnia |
| [25532388](https://pubmed.ncbi.nlm.nih.gov/25532388/) | 2014 | Real-World Analysis | China Journal of Chinese Materia Medica | Real-world analysis of 1,067 insomnia patients from 20 hospitals; characterises concurrent disease burden and medication use patterns (including benzodiazepines) in insomnia — documents alprazolam prescribing context |
| [15341891](https://pubmed.ncbi.nlm.nih.gov/15341891/) | 2004 | Descriptive Study | Sleep Medicine | Large managed-care population analysis of hypnotic prescription patterns for insomnia; quantifies the shift from benzodiazepines to non-hypnotic agents and characterises patient profiles receiving BZD prescriptions for insomnia |
| [37984023](https://pubmed.ncbi.nlm.nih.gov/37984023/) | 2024 | Pharmacoeconomic | Value in Health Regional Issues | 10-year predictive model of benzodiazepine utilisation trends in Croatia; documents BZD prescribing for anxiety and insomnia alongside associated risks (memory loss, Alzheimer's disease, dependence, falls) — informs population-level risk–benefit assessment |
| [38363887](https://pubmed.ncbi.nlm.nih.gov/38363887/) | 2024 | Cross-sectional | Medicine | Cross-sectional study of insomnia prevalence and influencing factors in 8-question survey of COVID-19 survivors; contextualises insomnia as a post-COVID sequela and maps pharmacological management landscape |
| [35493764](https://pubmed.ncbi.nlm.nih.gov/35493764/) | 2022 | Cohort | JHEP Reports | Retrospective cohort study demonstrating that deprescribing benzodiazepines (including zolpidem) in cirrhosis patients reduces falls and fractures; highlights the harms of long-term BZD use for sleep and the safety case for discontinuation |
| [35041261](https://pubmed.ncbi.nlm.nih.gov/35041261/) | 2022 | RCT | Brain and Behavior | RCT of eszopiclone versus placebo for sleep quality and cognitive function in Alzheimer's disease patients; provides comparative benchmark for non-BZD hypnotics in the elderly insomnia population — relevant for positioning alprazolam against current standard of care |

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data were available in the current evidence pack (all items were flagged as data gaps). This is classified as a **Blocking** data gap that must be resolved before proceeding to formal safety evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the TxGNN prediction score is high (99.81%) and alprazolam's GABAergic mechanism produces demonstrable short-term sedative effects, the mechanistic evidence strongly argues *against* chronic insomnia use: the drug suppresses REM sleep, induces pharmacodynamic tolerance, and causes rebound insomnia upon discontinuation — the very condition it is intended to treat. The literature evidence base (L3) reflects off-label co-prescribing and comparative safety data rather than dedicated regulatory-grade insomnia trials, and no alprazolam-specific randomised insomnia trials were identified. Current international guidelines (e.g., AASM, NICE) do not recommend benzodiazepines as first-line chronic insomnia therapy.

**To proceed, the following is needed:**

- **Resolve Blocking Data Gaps**: Retrieve full package insert (or Health Canada Product Monograph) to populate key warnings, contraindications, and drug interaction data before any S1 safety evaluation can begin
- **Clarify MOA documentation**: Obtain DrugBank API data for the formal mechanism of action record to complete mechanistic link scoring
- **Define scope of use**: Determine whether the repositioning target is *short-term* insomnia (where evidence is stronger but market differentiation is low) versus *chronic* insomnia (where mechanistic barriers are significant)
- **Review regulatory history**: Confirm whether alprazolam has been previously reviewed and declined by Health Canada for any indication, and identify if there are existing market authorisations in comparable jurisdictions (US FDA, EMA, TGA)
- **Assess addiction/dependence scheduling**: Alprazolam is a Schedule IV controlled substance in most jurisdictions; any new indication filing must address the dependency risk profile specifically in the insomnia patient population
- **Consider comparator landscape**: Evaluate positioning against approved alternatives for insomnia (z-drugs, doxepin, suvorexant, melatonin agonists) to assess whether a meaningful unmet need exists that justifies repositioning despite known BZD risks
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

