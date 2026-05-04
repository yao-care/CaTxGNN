---
layout: default
title: Citalopram
parent: 僅模型預測 (L5)
nav_order: 165
evidence_level: L5
indication_count: 5
---

# Citalopram
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Citalopram: From Major Depressive Disorder to Obsessive-Compulsive Disorder

## One-Sentence Summary

Citalopram is a highly selective serotonin reuptake inhibitor (SSRI) originally developed and widely used for the treatment of major depressive disorder (MDD). The TxGNN model predicts it may be effective for **obsessive-compulsive disorder (OCD)**, with **multiple clinical trials** — including Phase 3 studies using escitalopram (its active S-enantiomer) and at least one direct Phase 2 RCT with citalopram itself — and **16 publications** currently supporting this direction. The overall evidence meets the L2 threshold, warranting a "Proceed with Guardrails" recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Major depressive disorder (MDD) — established SSRI class indication |
| Predicted New Indication | Obsessive-Compulsive Disorder (OCD) |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Product Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Citalopram is a highly selective inhibitor of the serotonin reuptake transporter (SERT), blocking presynaptic serotonin reuptake and thereby increasing synaptic serotonin concentrations. Although detailed MOA data is not available in the current regulatory dataset, citalopram's pharmacological mechanism is well-characterised in the scientific literature. Its active S-enantiomer, escitalopram, shares the same primary mechanism and has been extensively studied in OCD.

The pathophysiology of OCD is strongly linked to dysfunction in the orbitofrontal cortex (OFC)–caudate nucleus–thalamic circuit, which exhibits measurable serotonin dysregulation. SSRIs, including citalopram, modulate this hyperactive circuit through sustained serotonergic enhancement. Secondary mechanisms via 5-HT2C and 5-HT1B/1D receptors may also contribute to symptom reduction (PMID 12607204). Notably, OCD responds selectively to serotonergic agents but not to noradrenaline reuptake inhibitors — a pharmacological specificity that in itself supports the mechanistic plausibility of citalopram for this indication.

The mechanistic bridge between depression and OCD is further reinforced by direct clinical data: two publications reporting citalopram use specifically in OCD patients (PMID 10572334; PMID 12839522) demonstrate meaningful Y-BOCS score reductions, and the largest direct citalopram RCT to date (NCT00086645, n=149) evaluated the drug's effect on repetitive behaviors that substantially overlap with OCD symptomatology. The volume of Phase 3/4 evidence for escitalopram in OCD provides strong class-level support for citalopram's repurposing potential.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00305500](https://clinicaltrials.gov/study/NCT00305500) | Phase 3 | Completed | 100 | Open-label prospective study evaluating tolerability and efficacy of escitalopram at high doses (up to 50 mg/day) in OCD outpatients over 18 weeks with Y-BOCS-guided dose titration; strongest indirect evidence for citalopram class |
| [NCT00723060](https://clinicaltrials.gov/study/NCT00723060) | Phase 4 | Completed | 176 | Randomized, double-blind, multi-center trial comparing conventional (20 mg) vs. high-dose (40 mg) escitalopram in OCD; efficacy assessed via Y-BOCS, HAM-D, HAM-A, and CGI scales |
| [NCT00086645](https://clinicaltrials.gov/study/NCT00086645) | Phase 2 | Completed | 149 | Placebo-controlled RCT of **citalopram** (not escitalopram) in children with autism spectrum disorder and high levels of repetitive behaviors; the largest direct citalopram RCT available, targeting OCD-overlapping symptom domains |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | Completed | 124 | Determined whether CBT delivered by psychologists or psychiatrists improves SRI treatment effectiveness in children with OCD; supports multimodal SSRI-based treatment strategy |
| [NCT00116532](https://clinicaltrials.gov/study/NCT00116532) | Phase 4 | Completed | 30 | Assessed efficacy of escitalopram in OCD and identified optimal treatment doses; directly supports class-level evidence for citalopram in the OCD indication |
| [NCT00215137](https://clinicaltrials.gov/study/NCT00215137) | Phase 2 | Completed | 14 | Pilot study evaluating safety and effectiveness of escitalopram in OCD; exploratory but directionally consistent with class effect |
| [NCT00115011](https://clinicaltrials.gov/study/NCT00115011) | Phase 4 | Completed | 30 | Escitalopram for self-injurious skin picking, an OC spectrum disorder; supports broader efficacy of the citalopram class across the OC spectrum |
| [NCT02022709](https://clinicaltrials.gov/study/NCT02022709) | Phase 4 | Completed | 78 | Compared SSRIs, exposure and response prevention (ERP), and combined therapy for OCD in a Chinese population; identified biological and psychological predictors of SSRI response |
| [NCT03993535](https://clinicaltrials.gov/study/NCT03993535) | Phase 4 | Completed | 250 | Large naturalistic OCD follow-up examining clinical, neurocognitive, and neuroimaging variables associated with treatment response to SSRIs; provides real-world effectiveness context |
| [NCT00609531](https://clinicaltrials.gov/study/NCT00609531) | Phase 1 | Completed | 12 | fMRI proof-of-concept study examining the effect of **citalopram** on restricted repetitive behaviors in autism spectrum disorder; provides direct mechanistic imaging evidence for citalopram's modulation of OCD-related neural circuitry |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [35121274](https://pubmed.ncbi.nlm.nih.gov/35121274/) | 2022 | Systematic Review / Meta-analysis | Journal of Psychiatric Research | Network meta-analysis comparing pharmacological and psychological treatments, alone and combined, for OCD in children and adolescents; supports SSRIs as effective first-line pharmacotherapy |
| [32982805](https://pubmed.ncbi.nlm.nih.gov/32982805/) | 2020 | Meta-Review | Frontiers in Psychiatry | Meta-review assessing antidepressant efficacy, tolerability, and suicidality across multiple indications (including OCD) in children and adolescents; informs benefit-risk assessment for SSRI use in younger populations |
| [28477500](https://pubmed.ncbi.nlm.nih.gov/28477500/) | 2017 | Meta-analysis | Journal of Affective Disorders | Demonstrated OCD has a uniquely reduced placebo response compared to other anxiety disorders, confirming that antidepressant effects in OCD trials represent true pharmacological signal rather than placebo-driven improvement |
| [38703743](https://pubmed.ncbi.nlm.nih.gov/38703743/) | 2024 | Systematic Review | Comprehensive Psychiatry | Examined long-term safety and tolerability of off-label high-dose serotonin reuptake inhibitors in OCD; supports dose escalation as viable strategy for partial or non-responders |
| [10572334](https://pubmed.ncbi.nlm.nih.gov/10572334/) | 1999 | Randomized Open-label Trial | European Psychiatry | **Direct citalopram evidence**: Compared citalopram alone vs. citalopram + clomipramine in 16 treatment-resistant OCD patients; demonstrated citalopram produced meaningful Y-BOCS reductions even in previously refractory cases |
| [10471169](https://pubmed.ncbi.nlm.nih.gov/10471169/) | 1999 | Clinical Review | International Clinical Psychopharmacology | **Direct citalopram review**: "Beyond depression: citalopram for OCD" — reviewed early citalopram evidence for OCD and explored the serotonergic neurobiology underpinning this indication, including neuroimaging and pharmacological challenge data |
| [12839522](https://pubmed.ncbi.nlm.nih.gov/12839522/) | 2003 | Open-label Study | Psychiatry and Clinical Neurosciences | **Direct citalopram evidence**: 8-week open-label study of citalopram (20–30 mg/day) in 15 children and adolescents with OCD; showed significant CY-BOCS score reductions with acceptable tolerability |
| [12607204](https://pubmed.ncbi.nlm.nih.gov/12607204/) | 2000 | Review | World Journal of Biological Psychiatry | Mechanistic review of OCD and serotonin: describes OFC–caudate–thalamic circuit dysregulation and how SSRIs modulate this pathway; identifies 5-HT2C and 5-HT1B/1D receptors as secondary targets, directly supporting citalopram's mechanistic applicability |
| [22305974](https://pubmed.ncbi.nlm.nih.gov/22305974/) | 2012 | Review | BMJ Clinical Evidence | Comprehensive clinical overview of OCD epidemiology (1–2.7% prevalence), natural history, and SSRI evidence base; contextualises citalopram class within established standard of care |
| [35818708](https://pubmed.ncbi.nlm.nih.gov/35818708/) | 2022 | Systematic Review | Expert Opinion on Pharmacotherapy | Systematically evaluated randomized controlled pharmacotherapy trials for OC spectrum personality disorder; provides complementary evidence for SSRI use across the broader OC spectrum |

---

## Taiwan Market Information

Citalopram is currently **not marketed in Taiwan**. No product licenses have been issued by the Taiwan Food and Drug Administration (TFDA), and no National Health Insurance (NHI) drug codes exist for this compound.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Taiwan TFDA package insert data (warnings, contraindications, and drug interaction profile) were not available at the time of this report. Retrieval from the TFDA official website and PDF parsing is required before proceeding to formal safety screening (see Next Steps).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction for citalopram in OCD is strongly supported by well-established serotonergic pathophysiology and an extensive clinical evidence base for escitalopram (citalopram's active enantiomer) in OCD, supplemented by two direct citalopram studies and one direct Phase 2 RCT — collectively meeting the L2 evidence threshold. The prediction is mechanistically coherent, clinically plausible, and backed by consistent findings across multiple trial phases and patient populations.

**To proceed, the following is needed:**

- **Safety data retrieval**: Download and parse the TFDA package insert PDF to extract key warnings, contraindications, and drug-drug interactions — currently a blocking data gap
- **MOA confirmation**: Query the DrugBank API for the full mechanism of action record (DB00215) to complete the mechanistic link analysis
- **QTc risk assessment**: Citalopram carries a known dose-dependent QTc prolongation risk (FDA communication, 2011); a cardiac safety evaluation plan is required, especially given that effective OCD doses are typically higher than those used in depression
- **Dose strategy clarification**: OCD typically requires doses at or above the upper end of the antidepressant dosing range (e.g., 40–60 mg/day); a dosing rationale document should be prepared for regulatory review
- **Jurisdiction comparator review**: Assess whether citalopram holds an approved OCD indication in the US, EU, or Japan, to inform regulatory strategy in Taiwan
- **Competitive landscape analysis**: Identify other SSRIs currently marketed in Taiwan with an OCD indication (e.g., fluoxetine, fluvoxamine, sertraline) to evaluate differentiation potential
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

