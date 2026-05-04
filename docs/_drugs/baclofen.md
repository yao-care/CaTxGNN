---
layout: default
title: Baclofen
parent: 僅模型預測 (L5)
nav_order: 85
evidence_level: L5
indication_count: 2
---

# Baclofen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Baclofen: From Spasticity to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Baclofen is a well-established GABA-B receptor agonist widely used for muscle spasticity, though original indication and mechanism-of-action data are not captured in the current regulatory dataset. The TxGNN model's top prediction is **Attention Deficit-Hyperactivity Disorder (ADHD)**, currently supported by **0 registered clinical trials** and **10 publications** (primarily reviews and preclinical work), warranting a **Hold** decision. A second high-scoring prediction, **Nicotine Dependence**, carries substantially stronger evidence with **3 Phase 2 clinical trials** and **20 publications**, reaching Evidence Level L2.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Muscle spasticity (established clinical use; original indication data not captured in current dataset) |
| Predicted New Indication | Attention Deficit-Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed (possible data gap — verify against Health Canada Drug Product Database) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Baclofen is a selective GABA-B receptor agonist that suppresses excitatory neurotransmission by activating pre- and post-synaptic GABA-B receptors throughout the central nervous system. Although detailed mechanistic data is not available in the current evidence pack, the GABAergic rationale for ADHD rests on the following logic: GABA-B receptor activation within the mesocortical pathway theoretically modulates prefrontal dopamine and norepinephrine release — the two neurotransmitter systems most strongly implicated in ADHD pathophysiology. Standard ADHD treatments (methylphenidate, amphetamines, atomoxetine) all act on these systems, and GABAergic modulation is known to influence their activity indirectly.

Animal model evidence provides partial support. Studies using the spontaneously hypertensive rat (SHR) — the most widely validated rodent model of ADHD — show that various neurotransmitter agonists, including GABAergic agents, alter cortical and hippocampal EEG patterns associated with attention deficits. This suggests a plausible, if indirect, pathway.

The mechanistic link is further reinforced by baclofen's documented use in Tourette syndrome, a condition with very high ADHD comorbidity (approximately 50–60% of Tourette patients carry an ADHD diagnosis). Several publications in the evidence base report baclofen's tic-suppressive effects in Tourette patients, many of whom are managed concurrently for ADHD. Despite these plausible connections, no registered clinical trials exist specifically testing baclofen for ADHD, and the underlying pathway remains highly inferential. This is a model-driven hypothesis that requires prospective human data before any development decision can advance.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for Baclofen in ADHD.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35345730](https://pubmed.ncbi.nlm.nih.gov/35345730/) | 2022 | Systematic Review / Meta-analysis | Cureus | Behavioural therapy, antipsychotics, and alpha-agonists for Tourette syndrome tics; ADHD highlighted as a major comorbidity requiring integrated management |
| [26366961](https://pubmed.ncbi.nlm.nih.gov/26366961/) | 2015 | Review | Clinical Neuropharmacology | Mood stabilisers in paediatric autism spectrum disorders; discusses symptom overlap with ADHD and GABAergic psychopharmacological strategies |
| [24295630](https://pubmed.ncbi.nlm.nih.gov/24295630/) | 2013 | Review | International Review of Neurobiology | Emerging therapies for Tourette syndrome covering ADHD/OCD comorbidities; baclofen included in the treatment landscape |
| [11393328](https://pubmed.ncbi.nlm.nih.gov/11393328/) | 2001 | Review | Paediatric Drugs | Tourette syndrome management strategies; clonidine and baclofen cited for tic suppression; ADHD addressed as a key comorbidity |
| [10342599](https://pubmed.ncbi.nlm.nih.gov/10342599/) | 1999 | Review | Journal of Child Neurology | 450-patient series using baclofen and botulinum toxin for tic/Tourette's symptoms, rated by Yale Global Tic Severity Scale; only dataset directly applying baclofen to a neurodevelopmental disorder |
| [30122296](https://pubmed.ncbi.nlm.nih.gov/30122296/) | 2019 | Review | L'Encéphale | Off-label methylphenidate prescribing in adult ADHD; contextualises the broader off-label treatment landscape and unmet need |
| [24062084](https://pubmed.ncbi.nlm.nih.gov/24062084/) | 2014 | Animal Study | Psychopharmacology | Guanfacine (α2A-adrenergic agonist) in the ventral hippocampus reduces impulsive decision-making; supports noradrenergic modulation as relevant to ADHD but does not test baclofen directly |
| [21300040](https://pubmed.ncbi.nlm.nih.gov/21300040/) | 2011 | Animal Study | Brain Research | EEG effects of multiple neurotransmitter agonists in SHR (ADHD model) vs. control rats; GABAergic agonists alter cortical/hippocampal activity patterns in ADHD model animals |
| [24496320](https://pubmed.ncbi.nlm.nih.gov/24496320/) | 2014 | Animal Study | Neuropsychopharmacology | Anterior cingulate cortex and basolateral amygdala contributions to cognitive effort decision-making; relevant to the motivational deficits seen in ADHD |
| [24103016](https://pubmed.ncbi.nlm.nih.gov/24103016/) | 2013 | Animal Study | European Journal of Neuroscience | Habenula regulation of social play behaviour via monoaminergic neurotransmission; tangential relevance to social and reward-processing dimensions of ADHD |

---

## Second Predicted Indication: Nicotine Dependence

> **Note:** The TxGNN model ranks Nicotine Dependence second (score 99.19%), but its clinical evidence base is considerably richer than the top-ranked ADHD indication. This section is included because the evidence profile warrants a different and more actionable recommendation.

### Overview

| Item | Content |
|------|---------|
| TxGNN Prediction Score | 99.19% |
| Evidence Level | L2 |
| Recommended Decision | Proceed with Research |

### Why Is This Prediction Reasonable?

Baclofen's mechanistic rationale for nicotine dependence is direct and well-grounded. As a GABA-B receptor agonist, baclofen suppresses mesolimbic dopamine release from the ventral tegmental area (VTA) to the nucleus accumbens (NAc) — the core neurobiological substrate of nicotine's reinforcing and rewarding effects. Pre-synaptic inhibition of glutamate release simultaneously disrupts the consolidation and reconsolidation of addiction-related cue memories, potentially reducing craving triggered by smoking-associated environmental stimuli.

This mechanism has been confirmed across multiple preclinical models: baclofen reduces nicotine self-administration in rodents, blocks nicotine-induced conditioned place preference (CPP), and prevents reinstatement of nicotine-seeking behaviour after extinction. The GABAergic hypothesis of addiction is not limited to nicotine — baclofen has received regulatory approval for alcohol use disorder in France, establishing a precedent for GABA-B–targeted therapy across addictive behaviours. One completed Phase 2 clinical trial (NCT01821560, n=44) has used neuroimaging to examine baclofen's effects on brain and behavioural responses to smoking cues in humans, representing the most direct clinical evidence to date.

### Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT01821560](https://clinicaltrials.gov/study/NCT01821560) | Phase 2 | Completed | 44 | Perfusion fMRI study examining baclofen's effects on brain activity and behaviour in cigarette smokers; evaluated dopaminergic genetic polymorphisms and appetitive cue-triggered responses; the only completed Phase 2 trial for this indication — primary source of human efficacy signal |
| [NCT00257894](https://clinicaltrials.gov/study/NCT00257894) | Phase 2 | Terminated | 41 | Directly measured smoking urge, withdrawal symptoms, and nicotine reinforcement in moderate-to-heavy smokers; terminated before completion but enrolled a substantial proportion of the target, providing a partial efficacy signal |
| [NCT01228994](https://clinicaltrials.gov/study/NCT01228994) | Phase 2 | Terminated | 6 | Randomised proof-of-concept trial testing the GABAergic hypothesis of nicotine dependence; only 6 participants enrolled before termination — insufficient for any efficacy estimate; demonstrates feasibility challenges |

### Literature Evidence (Nicotine Dependence)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [29250815](https://pubmed.ncbi.nlm.nih.gov/29250815/) | 2018 | Review | Pharmacotherapy | Current and emerging pharmacotherapies for tobacco cessation; baclofen discussed among GABAergic candidates, noting insufficient human data to recommend routine use |
| [24654737](https://pubmed.ncbi.nlm.nih.gov/24654737/) | 2014 | Review | Expert Opinion on Emerging Drugs | 2014 update on emerging therapies for tobacco dependence; baclofen identified as a candidate requiring further clinical validation |
| [24971600](https://pubmed.ncbi.nlm.nih.gov/24971600/) | 2015 | Review | Neuropharmacology | GABA-B receptors as therapeutic targets across substance use disorders; reviews positive allosteric modulators as potentially superior alternatives to baclofen with improved tolerability |
| [38555115](https://pubmed.ncbi.nlm.nih.gov/38555115/) | 2024 | Review | International Review of Neurobiology | Drug repurposing for addiction treatment; baclofen's regulatory approval for alcohol use disorder in France cited as precedent supporting its cross-addiction potential |
| [19250803](https://pubmed.ncbi.nlm.nih.gov/19250803/) | 2009 | Animal Study | European Neuropsychopharmacology | Baclofen prevents reinstatement of nicotine-seeking behaviour and conditioned place preference in rodents after extinction; key preclinical evidence for anti-relapse potential |
| [24553576](https://pubmed.ncbi.nlm.nih.gov/24553576/) | 2014 | Animal Study | Psychopharmacology | Baclofen attenuates nicotine rewarding properties and behavioural expression of nicotine withdrawal in rodents; supports both acute reward-blocking and withdrawal-relief mechanisms |
| [18682277](https://pubmed.ncbi.nlm.nih.gov/18682277/) | 2008 | Animal Study | Neuroscience Letters | Baclofen (3 mg/kg) reduces nicotine-conditioned place preference in rats; high doses also suppress food-reinforced behaviour, raising selectivity concerns at therapeutic doses |
| [23500668](https://pubmed.ncbi.nlm.nih.gov/23500668/) | 2013 | Animal Study | Progress in Neuro-Psychopharmacology & Biological Psychiatry | Baclofen prevents mecamylamine-precipitated nicotine withdrawal syndrome and attenuates associated changes in α4β2 nicotinic receptor density in mice |
| [25868070](https://pubmed.ncbi.nlm.nih.gov/25868070/) | 2015 | Conference Abstract / Pilot Study | Neuropsychopharmacology | Double-blind, placebo-controlled pilot RCT of baclofen for concurrent alcohol and nicotine dependence; co-use scenario directly relevant to the comorbid patient population |
| [17338593](https://pubmed.ncbi.nlm.nih.gov/17338593/) | 2007 | Review | CNS Drugs | Pharmacotherapy of dual substance abuse; reviews baclofen as a candidate across co-occurring nicotine and alcohol dependence, reflecting the typical poly-substance clinical profile |

---

## Canada Market Information

According to the current regulatory dataset, Baclofen has **0 registered DINs** and is listed as **not marketed** in Canada. This almost certainly represents a data gap — Baclofen is a well-established generic medication available in multiple jurisdictions worldwide. Independent verification against the Health Canada Drug Product Database is strongly recommended before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

### Primary Indication — Attention Deficit-Hyperactivity Disorder

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score, the mechanistic link between baclofen and ADHD is indirect and speculative, there are zero registered clinical trials in this indication, and the available literature is dominated by animal studies and reviews of tangentially related conditions. The evidence sits firmly at L4, insufficient to justify investment without additional foundational work.

**To proceed, the following is needed:**
- A human proof-of-concept study (at minimum an open-label feasibility trial) to establish whether GABA-B agonism produces measurable improvements on validated ADHD endpoints (e.g., ADHD-RS, CPT)
- Mechanistic biomarker studies (e.g., neuroimaging) linking baclofen's GABA-B activity to prefrontal dopamine/norepinephrine modulation in ADHD patients
- Paediatric-specific pharmacokinetic and safety data, given the predominantly paediatric ADHD population
- Full safety profile including package insert warnings, contraindications, and drug interactions
- Confirmation of Canada DIN status via the Health Canada Drug Product Database

---

### Second Indication — Nicotine Dependence

**Decision: Proceed with Research**

**Rationale:**
With one completed Phase 2 neuroimaging trial (NCT01821560, n=44), two terminated-but-informative Phase 2 trials, a convergent preclinical evidence base, and regulatory precedent from France (alcohol use disorder approval), nicotine dependence reaches Evidence Level L2. The GABAergic mechanism is directly linked to the neurobiology of nicotine reward and withdrawal, and the unmet clinical need in smoking cessation is substantial.

**To proceed, the following is needed:**
- A well-powered, double-blind, placebo-controlled Phase 2 RCT with pre-specified endpoints for 7-day point prevalence abstinence at 12 weeks
- Dose-finding data to establish optimal dosing for smoking cessation (distinct from spasticity dosing)
- A safety monitoring plan addressing sedation, respiratory depression, and discontinuation risk on abrupt withdrawal
- Evaluation of combination strategies (baclofen + nicotine replacement therapy or baclofen + varenicline)
- Assessment of the concurrent alcohol + nicotine dependence population, given high clinical co-occurrence
- Regulatory pathway consultation with Health Canada for a new addiction indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

