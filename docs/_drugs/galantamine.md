---
layout: default
title: Galantamine
parent: 僅模型預測 (L5)
nav_order: 356
evidence_level: L5
indication_count: 9
---

# Galantamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Galantamine: From Alzheimer's Disease to Tardive Dyskinesia (Lingual-Facial-Buccal Dyskinesia)

## One-Sentence Summary

Galantamine is an acetylcholinesterase inhibitor (AChEI) with a dual mechanism — inhibiting acetylcholinesterase and allosterically potentiating nicotinic receptors — established as a treatment for mild-to-moderate Alzheimer's disease.
The TxGNN model generated **9 movement disorder predictions**; the strongest actionable evidence supports repurposing for **lingual-facial-buccal dyskinesia (tardive dyskinesia)**, backed by **2 Cochrane systematic reviews**, **1 dedicated galantamine RCT**, and **1 evidence-based AAN guideline**.
The overall evidence profile for this indication reaches **L3**, supporting a **Proceed with Guardrails** decision.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Alzheimer's disease (mild to moderate) |
| Primary Actionable Prediction | Lingual-Facial-Buccal Dyskinesia (Tardive Dyskinesia) |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L3 |
| Canada Market Status | ✗ Not marketed (0 DINs) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Summary of All Predicted Indications

This is a multi-indication evaluation covering 9 TxGNN predictions. Most are movement disorder subtypes with overlapping pathophysiology.

| Rank | Indication | TxGNN Score | Evidence | Recommendation | Key Constraint |
|------|-----------|-------------|----------|----------------|----------------|
| 1 | Psychogenic movement disorders | 99.89% | L5 | Hold | Functional neurological origin; cholinergic mechanism irrelevant |
| 2 | Chronic tic disorder | 99.89% | L5 | Hold | Only 1 narrative review from 1980; no galantamine-specific data |
| 3 | Primary orthostatic tremor | 99.89% | L5 | Hold | Brainstem-cerebellar oscillation circuit; no cholinergic basis |
| 4 | Extrapyramidal and movement disease | 99.88% | L4 | Research Question | 2 completed trials + 4 publications; endpoints indirect |
| 5 | Benign shuddering attacks | 99.88% | L5 | Hold | Self-limiting developmental phenomenon; likely KG proximity artifact |
| 6 | Tremor-nystagmus-duodenal ulcer syndrome | 99.88% | L5 | Hold | AChEI may **worsen** duodenal ulcer — active safety concern |
| **7** | **Lingual-facial-buccal dyskinesia** | **99.88%** | **L3** | **Proceed with Guardrails** | **Dedicated RCT exists; 2 Cochrane reviews support cholinergic class** |
| 8 | Benign paroxysmal tonic upgaze of childhood with ataxia | 99.88% | L5 | Hold | Rare pediatric syndrome; no AChEI rationale |
| 9 | Acute intermittent porphyria | 99.71% | L5 | Hold | AChEI may trigger cholinergic crisis during AIP neurological attacks — **contraindication to investigate** |

---

## Why is This Prediction Reasonable?

Galantamine acts through two complementary mechanisms: (1) reversible inhibition of acetylcholinesterase, raising synaptic acetylcholine concentrations; and (2) allosteric potentiation of nicotinic acetylcholine receptors (nAChRs), enhancing cholinergic signal transduction beyond simple enzyme inhibition. This dual action distinguishes galantamine from donepezil or rivastigmine and may be particularly relevant in the basal ganglia, where both muscarinic and nicotinic receptors regulate movement.

Tardive dyskinesia (TD) — the clinical entity underlying lingual-facial-buccal dyskinesia — results from prolonged dopamine receptor blockade by antipsychotics, causing postsynaptic D2 receptor supersensitivity. Critically, long-term antipsychotic exposure also damages striatal cholinergic interneurons, creating a dopamine–acetylcholine imbalance: excess dopaminergic activity is no longer balanced by cholinergic tone. This "cholinergic deficiency" model of TD directly implicates the pathway galantamine targets, making the mechanistic connection substantially stronger than for other movement disorder subtypes in this prediction set.

Two independent Cochrane systematic reviews (2002, 2018) have evaluated the cholinergic drug class for antipsychotic-induced TD and identified a biological rationale for intervention. More decisively, a 30-week randomized, double-blind, placebo-controlled crossover trial specifically testing galantamine in TD patients was published in 2007 (Caroff et al., PMID 17388711, J Clin Psychiatry), making this the only prediction in this pack supported by a directly targeted RCT.

---

## Clinical Trial Evidence

No trials are registered under the exact ICD term "lingual-facial-buccal dyskinesia." The following trials from the related **extrapyramidal and movement disease** prediction (rank 4) provide indirect context in populations at risk for antipsychotic-induced movement disorders:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00176423](https://clinicaltrials.gov/study/NCT00176423) | Phase 4 | Completed | 117 | Adjunctive galantamine for cognitive impairment in schizophrenia patients maintained on antipsychotics; EPS and movement adverse effects may have been recorded as safety outcomes |
| [NCT01012167](https://clinicaltrials.gov/study/NCT01012167) | Phase 2 | Completed | 86 | Galantamine vs. placebo for cognitive and negative symptoms in schizophrenia; antipsychotic-using population overlaps substantially with TD risk population |

> **Note:** The most directly relevant evidence is a non-ClinicalTrials.gov–registered RCT (predating mandatory registration) — Caroff et al. 2007 (PMID 17388711): a 30-week double-blind crossover RCT of galantamine specifically for tardive dyskinesia. Full text review is required.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [29553158](https://pubmed.ncbi.nlm.nih.gov/29553158/) | 2018 | Cochrane Systematic Review | Cochrane Database Syst Rev | Evaluates cholinergic drugs (incl. galantamine) for antipsychotic-induced TD; examines the class-level evidence for cholinergic deficiency hypothesis |
| [17388711](https://pubmed.ncbi.nlm.nih.gov/17388711/) | 2007 | RCT | J Clin Psychiatry | **Key trial:** 30-week randomized, double-blind, placebo-controlled crossover trial of galantamine specifically for tardive dyskinesia, motivated by cholinesterase inhibitor hypothesis of TD |
| [15610922](https://pubmed.ncbi.nlm.nih.gov/15610922/) | 2004 | Meta-analysis of RCTs | Prog Neuropsychopharmacol Biol Psychiatry | Systematic review and meta-analysis of cholinergic drugs for neuroleptic-induced TD; includes galantamine and other AChEIs across RCTs |
| [23897874](https://pubmed.ncbi.nlm.nih.gov/23897874/) | 2013 | Evidence-based Guideline | Neurology | AAN Guideline Development Subcommittee evidence-based guideline on treatment of tardive syndromes; addresses pharmacological agents including cholinergic drugs |
| [12137608](https://pubmed.ncbi.nlm.nih.gov/12137608/) | 2002 | Cochrane Systematic Review | Cochrane Database Syst Rev | Original Cochrane review of cholinergic drugs for neuroleptic-induced TD; establishes the theoretical framework and early evidence base |
| [24127392](https://pubmed.ncbi.nlm.nih.gov/24127392/) | 2014 | Pharmacovigilance Study | Pharmacotherapy | FDA FAERS analysis of ChEI-associated Pisa syndrome (a focal dystonia variant); adjusted reporting ratios for donepezil, rivastigmine, and galantamine — important safety signal for movement side effects |
| [25850380](https://pubmed.ncbi.nlm.nih.gov/25850380/) | 2015 | Animal Study | J Pharmacol Sci | Galantamine and donepezil interactions with antipsychotic-induced EPS in mice; galantamine potentiated bradykinesia in some combinations — important safety context |
| [40224553](https://pubmed.ncbi.nlm.nih.gov/40224553/) | 2025 | Systematic Review | Brain Circulation | Systematic review of movement disorders associated with AChEIs (including galantamine) in Alzheimer's disease; characterizes both therapeutic and adverse movement effects |
| [24969380](https://pubmed.ncbi.nlm.nih.gov/24969380/) | 2014 | RCT | Dement Geriatr Cogn Disord | 12-week RCT of galantamine vs. risperidone for agitation in dementia; provides comparative safety data on galantamine vs. an antipsychotic in a relevant population |
| [25575935](https://pubmed.ncbi.nlm.nih.gov/25575935/) | 2015 | Commentary | Am J Geriatr Psychiatry | Critical commentary on an unsubstantiated conclusion in the galantamine/movement disorder literature; flags a methodological concern relevant to evidence quality assessment |

---

## Canada Market Information

Galantamine (DB00674) is **not currently marketed in Canada**. No Drug Identification Numbers (DINs) are on record. Any new therapeutic use would require a full Health Canada new drug submission (NDS) or supplemental new drug submission (SNDS), and a product monograph would need to be filed.

---

## Safety Considerations

Detailed Health Canada product monograph data is not yet available for this drug in the Canadian database. Based on galantamine's established pharmacological class (AChEI), the following safety signals are clinically relevant to the predicted movement disorder indications:

- **Cholinergic adverse effects:** Nausea, vomiting, diarrhea, bradycardia, and syncope are characteristic class effects; dose titration required
- **Gastric acid secretion:** AChEIs increase gastric acid — patients with peptic ulcer disease or NSAID use at elevated risk; this is a **direct contraindication** for the rank 6 prediction (tremor-nystagmus-duodenal ulcer syndrome)
- **Paradoxical movement effects:** PMID 25850380 (animal study) showed that galantamine may **potentiate** antipsychotic-induced bradykinesia in some combinations; PMID 24127392 (pharmacovigilance) identified a Pisa syndrome signal with AChEIs including galantamine — monitoring for new-onset dystonia is warranted
- **Acute intermittent porphyria (rank 9):** Cholinergic stimulation during AIP neurological crises may precipitate cholinergic crisis; this indication should be flagged as a **potential contraindication** pending formal assessment
- **Drug–drug interactions:** Galantamine is metabolized via CYP2D6 and CYP3A4; co-administration with antipsychotics (the target population for TD treatment) requires DDI review

Please obtain and review the Health Canada product monograph before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (Lingual-Facial-Buccal Dyskinesia / Tardive Dyskinesia)

**Rationale:**
Galantamine's cholinergic mechanism directly addresses the established cholinergic deficiency pathophysiology of tardive dyskinesia, and it is the only drug in this multi-candidate pack supported by both a dedicated galantamine RCT (Caroff 2007) and two independent Cochrane systematic reviews for its predicted drug class. Evidence level L3 is achieved, warranting structured evidence review and protocol planning — provided that the safety paradox (AChEI may both treat and worsen movement disorders depending on context) is carefully managed.

**To proceed, the following is needed:**
- Full text retrieval and effect size extraction from Caroff et al. 2007 (PMID 17388711) — this is the pivotal trial
- Health Canada product monograph retrieval to complete S1 safety screening (currently blocking data gap)
- MOA documentation from DrugBank to confirm nAChR allosteric potentiation details
- DDI assessment for galantamine + antipsychotics (the standard co-medication in the target population)
- Comparison against current standard-of-care: VMAT2 inhibitors (valbenazine, deutetrabenazine) are now FDA/Health Canada–approved for TD and represent the active comparator
- Regulatory pathway mapping: a DIN does not currently exist in Canada, requiring a new submission strategy
- For rank 9 (acute intermittent porphyria): formal contraindication investigation before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

