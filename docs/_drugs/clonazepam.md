---
layout: default
title: Clonazepam
parent: 僅模型預測 (L5)
nav_order: 187
evidence_level: L5
indication_count: 3
---

# Clonazepam
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

# Clonazepam: From Seizure Disorder to Restless Legs Syndrome

## One-Sentence Summary

Clonazepam is a long-acting benzodiazepine anticonvulsant with internationally established uses in epilepsy and panic disorder; no Health Canada DINs appear in the current dataset for this drug.
The TxGNN model's top prediction is **Restless Legs Syndrome (RLS)** (score 99.65%), supported by **20 publications** including a 2025 AASM Clinical Practice Guideline and a 2017 Cochrane Systematic Review, though no prospective registered clinical trials specifically target this combination.
Two additional predictions — **Insomnia** (score 99.32%, L2, 12 clinical trials) and **Trigeminal Nerve Neoplasm** (score 99.29%, L5, 2 case reports) — complete the repurposing profile; Insomnia represents the most immediately actionable opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Epilepsy / Panic disorder (internationally established; no Canadian DIN on record in this dataset) |
| Predicted New Indication | Restless Legs Syndrome |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L3 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why Is This Prediction Reasonable?

Clonazepam belongs to the benzodiazepine class and acts as a positive allosteric modulator of GABA-A receptors, enhancing chloride ion channel opening frequency and amplifying inhibitory neurotransmission across the central nervous system. Detailed mechanism of action data was not recovered in this Evidence Pack, but this drug's well-established GABAergic pharmacology provides a clear biological basis for activity in disorders characterised by motor dyscontrol and sleep disruption.

Restless Legs Syndrome involves an irresistible urge to move the legs accompanied by uncomfortable sensations that worsen at rest and at night, with core pathophysiology centring on dopaminergic dysfunction and spinal cord hyperexcitability. By enhancing GABAergic inhibitory tone, clonazepam can dampen spinal motor cortex excitability and reduce the frequency of periodic limb movements (PLM) — the objective polysomnographic correlate of RLS — while its sedative properties additionally address the severe sleep fragmentation that defines RLS-related morbidity.

Although dopamine agonists remain the pharmacological first line, the GABAergic pathway is an established adjunctive mechanism, particularly when nocturnal sleep disruption predominates over the sensorimotor complaint. This rationale is reflected in four decades of clinical use: from the first double-blind placebo-controlled crossover trial in 1984 (Montagna et al., *Acta Neurol Scand*) through the 2017 Cochrane review through to the 2025 AASM Clinical Practice Guideline, clonazepam has consistently appeared as a recognised, if second-line, treatment option for RLS and PLMD.

---

## Clinical Trial Evidence — Restless Legs Syndrome

Currently no related clinical trials registered for Clonazepam in Restless Legs Syndrome.

---

## Literature Evidence — Restless Legs Syndrome

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39324694](https://pubmed.ncbi.nlm.nih.gov/39324694/) | 2025 | Clinical Practice Guideline | J Clin Sleep Med (AASM) | AASM guideline establishing clinical practice recommendations for RLS and PLMD in adults and paediatric patients; clonazepam cited within the treatment landscape |
| [28319266](https://pubmed.ncbi.nlm.nih.gov/28319266/) | 2017 | Cochrane Systematic Review | Cochrane Database Syst Rev | Systematic review of benzodiazepines (particularly clonazepam) for RLS; evaluated the evidence base for efficacy and safety in this population |
| [36692194](https://pubmed.ncbi.nlm.nih.gov/36692194/) | 2023 | Systematic Review / Meta-analysis | J Clin Sleep Med | Meta-analysis of pharmacological responsiveness of PLM in RLS; provides quantitative comparison across drug classes including benzodiazepines |
| [38708125](https://pubmed.ncbi.nlm.nih.gov/38708125/) | 2024 | Narrative Review | Tremor Other Hyperkinetic Mov | Historical overview of benzodiazepines in RLS; among 16,694 surveyed RLS patients, approximately 25% received benzodiazepines; identified 17 articles specifically on clonazepam in RLS/PLMS |
| [31942156](https://pubmed.ncbi.nlm.nih.gov/31942156/) | 2019 | Prospective Open-Label RCT | J Mid-Life Health | Direct head-to-head comparison of clonazepam vs nortriptyline in women over 40 with RLS; assessed rate, frequency, and severity of symptoms |
| [11313161](https://pubmed.ncbi.nlm.nih.gov/11313161/) | 2001 | Placebo-Controlled Sleep Lab Study | Eur Neuropsychopharmacol | Acute placebo-controlled sleep laboratory study with 1 mg clonazepam in RLS/PLMD patients; measured both objective polysomnographic and subjective sleep quality outcomes |
| [6380197](https://pubmed.ncbi.nlm.nih.gov/6380197/) | 1984 | Randomized Double-Blind Crossover Trial | Acta Neurol Scand | First controlled RCT of clonazepam vs placebo in 6 RLS patients; significant improvement in subjective sleep quality and leg dysesthesia; established clonazepam as a safe and effective option |
| [18925578](https://pubmed.ncbi.nlm.nih.gov/18925578/) | 2008 | Evidence-Based Review | Mov Disord | Movement Disorder Society task force evidence-based review of RLS treatments; formally classified therapeutic efficacy level of each drug including clonazepam |
| [17876423](https://pubmed.ncbi.nlm.nih.gov/17876423/) | 2007 | Expert Consensus | Arq Neuropsiquiatr | Brazilian RLS Study Group consensus from 2006 meeting on diagnosis and management; clonazepam cited alongside dopamine agonists as treatment option |
| [24363103](https://pubmed.ncbi.nlm.nih.gov/24363103/) | 2014 | Review | Neurotherapeutics | Comprehensive review of RLS treatment evolution over recent decades; benzodiazepines discussed as adjunct class, with assessment of role relative to first-line dopaminergic agents |

---

## Additional Predicted Indications

### Insomnia — Rank #2 | Score 99.32% | Evidence Level L2 | Decision: Proceed with Guardrails

Clonazepam's GABA-A modulatory mechanism directly promotes sleep initiation and maintenance by suppressing hypothalamic arousal systems (histaminergic and orexinergic pathways) and inhibiting REM-period motor disinhibition in the ponto-medullary brainstem circuit — making this the most mechanistically direct of the three predictions. It is supported by 12 clinical trials and 18 publications, including direct RCT evidence and a completed trial of high-dose versus low-dose clonazepam specifically in insomnia patients.

**Key Clinical Trials — Insomnia**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT03255642](https://clinicaltrials.gov/study/NCT03255642) | N/A | Completed | 34 | Prospective randomised study of melatonin vs Rivotril (clonazepam) for idiopathic REM sleep behaviour disorder; direct efficacy and polysomnographic comparison |
| [NCT03977441](https://clinicaltrials.gov/study/NCT03977441) | Phase 4 | Unknown | 240 | Multicenter double-blind placebo-controlled RCT of agomelatine vs standard care (including clonazepam) for sleep disorders and depression in Parkinson's disease |
| [NCT00025740](https://clinicaltrials.gov/study/NCT00025740) | Phase 4 | Completed | 78 | Clonazepam + paroxetine for PTSD with sleep-related outcomes; completed trial with direct clonazepam arm |
| [NCT04884503](https://clinicaltrials.gov/study/NCT04884503) | Phase 2 | Completed | 58 | Treatment of primary burning mouth syndrome including insomnia outcomes; clonazepam as one active treatment modality |

**Key Literature — Insomnia**

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [37940498](https://pubmed.ncbi.nlm.nih.gov/37940498/) | 2024 | RCT | Clin Therapeutics | Prospective cohort comparing high-dose (1 mg) vs low-dose (0.5 mg) clonazepam combined with CBT-i in older adults with moderately severe insomnia; provides direct dose-response data |
| [26923575](https://pubmed.ncbi.nlm.nih.gov/26923575/) | 2015 | Observational | Neurol Res | Executive function effects of clonazepam in patients with chronic primary insomnia (n=90, three-group design); important safety/cognitive side-effect characterisation |
| [39297769](https://pubmed.ncbi.nlm.nih.gov/39297769/) | 2024 | Cross-Sectional | Clin Neuropharmacol | Pharmacological management patterns in acute and chronic insomnia; real-world prescribing context for clonazepam |

---

### Trigeminal Nerve Neoplasm — Rank #3 | Score 99.29% | Evidence Level L5 | Decision: Hold

Only 2 tangentially related case reports were identified (burning mouth pain and ocular neuromyotonia secondary to meningioma), with no clinical trials. The high TxGNN score most likely reflects an indirect knowledge graph path — trigeminal nerve → neuropathic pain → benzodiazepine class — rather than any direct antitumor activity. Clonazepam has no established mechanism against neoplastic processes. This prediction is not actionable at this time.

---

## Canada Market Information

No Health Canada DINs are recorded for Clonazepam in this dataset (total licences: 0, market status: Not Marketed).

> **Verification recommended:** Clonazepam (Rivotril® and generics) is a widely used Schedule F prescription drug internationally. If this result conflicts with known Canadian approvals, the Health Canada Drug Product Database should be queried directly to confirm current registration status, as a data extraction gap may be present.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Class-level alert:** As a benzodiazepine, clonazepam carries well-recognised risks of physical dependence, tolerance development, rebound insomnia on withdrawal, and cognitive impairment — risks that are substantially elevated in elderly populations. Any repurposing evaluation for chronic use in RLS or insomnia must incorporate a formal risk management plan addressing these class-level concerns, including patient selection criteria, maximum treatment duration, and tapering protocols.

---

## Conclusion and Next Steps

### Prediction 1: Restless Legs Syndrome

**Decision: Hold (Research Question)**

**Rationale:**
Clonazepam has documented clinical activity in RLS backed by over 40 years of literature, including a Cochrane review and the 2025 AASM guideline, but the evidence base consists primarily of reviews, small historical RCTs, and observational data — no large modern Phase 3 trial exists, and it functions as a second-line adjunctive option rather than a first-line agent.

**To proceed, the following is needed:**
- Mechanism of action data clarifying GABA-A subtype specificity and spinal cord effects in RLS
- A prospective randomised controlled trial comparing clonazepam to dopamine agonists as monotherapy or as adjunct therapy, with polysomnographic endpoints
- Long-term dependence and tolerance data in the RLS population specifically
- Health Canada regulatory pathway assessment for this indication

---

### Prediction 2: Insomnia

**Decision: Proceed with Guardrails**

**Rationale:**
Direct RCT evidence exists for clonazepam's efficacy in insomnia (particularly REM sleep behaviour disorder), with multiple completed Phase 4 trials and a well-established mechanistic link through GABA-A modulation of hypothalamic arousal and brainstem REM circuits.

**To proceed, the following is needed:**
- Confirmation of Health Canada regulatory status (DIN database query recommended)
- Safety monitoring plan addressing benzodiazepine dependence risk, cognitive effects in elderly patients, and rebound insomnia on discontinuation
- Clear definition of target patient population (primary insomnia vs insomnia secondary to RBD, Parkinson's disease, or other neurological conditions)
- Comparative effectiveness data against newer sleep agents (z-drugs, melatonin receptor agonists, suvorexant/lemborexant) to establish positioning

---

### Prediction 3: Trigeminal Nerve Neoplasm

**Decision: Hold**

**Rationale:**
No clinical evidence exists and no plausible direct antitumor mechanism has been identified; the prediction appears driven by an indirect network inference path rather than biologically grounded repurposing logic.

**To proceed, the following is needed:**
- Preclinical (in vitro/in vivo) evidence of GABA-A modulation in trigeminal nerve tumour biology
- A mechanistic hypothesis beyond incidental symptom palliation (neuropathic pain relief) that would justify pursuing this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

