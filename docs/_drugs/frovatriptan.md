---
layout: default
title: Frovatriptan
parent: 僅模型預測 (L5)
nav_order: 351
evidence_level: L5
indication_count: 3
---

# Frovatriptan
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

# Frovatriptan: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Frovatriptan is a selective 5-HT1B/1D receptor agonist belonging to the triptan class, indicated for the acute treatment of migraine with or without aura in adults.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura** (formerly basilar-type migraine),
with **0 clinical trials** and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute migraine (with or without aura) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Frovatriptan is a second-generation triptan that acts as a selective agonist at serotonin 5-HT1B and 5-HT1D receptors. Its mechanism involves constriction of intracranial meningeal blood vessels, inhibition of the trigeminovascular system, and suppression of pro-inflammatory neuropeptide release (CGRP, substance P). Compared to other triptans, frovatriptan stands out for its exceptionally long plasma half-life (~26 hours) and high receptor selectivity, which translate to a lower recurrence rate (~17%) and a potentially broader therapeutic window.

Migraine with brainstem aura (ICHD-3 classification, formerly known as basilar-type migraine) was historically considered a contraindication to triptans due to theoretical concerns about basilar artery vasospasm. However, the current mechanistic understanding has shifted: the dominant hypothesis now attributes the brainstem aura to cortical spreading depression (CSD) propagating into the brainstem, not to primary arterial vasospasm. This re-framing directly challenges the traditional contraindication and opens a rational pathway for triptan use in this subtype.

Given this mechanistic re-assessment, frovatriptan's long half-life is particularly relevant: migraine with brainstem aura attacks tend to be prolonged and more debilitating, which may benefit most from a long-acting triptan that reduces the likelihood of headache recurrence. While no randomised controlled trials have been conducted specifically in this ICHD-3 subtype, pooled analyses and subgroup data from crossover RCTs in migraine with aura, together with the American Headache Society evidence assessment (which includes aura-associated attacks), provide indirect but meaningful clinical support for this use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Clinical Guideline | *Headache* | American Headache Society updated evidence assessment of pharmacotherapies for acute migraine, including triptans such as frovatriptan, in adults |
| [22644173](https://pubmed.ncbi.nlm.nih.gov/22644173/) | 2012 | RCT Subgroup Analysis | *Neurological Sciences* | Frovatriptan vs. zolmitriptan in a subgroup of 18 patients with migraine with aura in a double-blind randomised crossover study; provides the most direct subtype-specific efficacy data available |
| [25916333](https://pubmed.ncbi.nlm.nih.gov/25916333/) | 2015 | Comparative Clinical Study | *The Journal of Headache and Pain* | Meta-analysis comparing frovatriptan vs. rizatriptan, zolmitriptan, and almotriptan across attacks with and without aura; concludes frovatriptan is efficacious in the headache phase of aura attacks |
| [27757013](https://pubmed.ncbi.nlm.nih.gov/27757013/) | 2016 | Narrative Review | *Drug Design, Development and Therapy* | Comprehensive review of three double-blind randomised crossover preference studies; highlights frovatriptan's long half-life as a differentiating pharmacokinetic advantage |
| [27910087](https://pubmed.ncbi.nlm.nih.gov/27910087/) | 2017 | Review | *Headache* | Review of treatment options for menstrual migraine; discusses frovatriptan's role in perimenstrual prophylaxis and acute treatment, including aura presentations |
| [22900951](https://pubmed.ncbi.nlm.nih.gov/22900951/) | 2012 | Narrative Review | *CNS Drugs* | Reviews frovatriptan pharmacology, mechanism, efficacy in acute migraine (with/without aura), and tolerability; clarifies that mechanism remains presumed 5-HT1B/1D agonism |
| [18457529](https://pubmed.ncbi.nlm.nih.gov/18457529/) | 2008 | Clinical Review | *Expert Review of Neurotherapeutics* | Overview of frovatriptan's clinical profile including 26-hour half-life, low recurrence rate, and use in both acute migraine and perimenstrual prophylaxis |
| [24867847](https://pubmed.ncbi.nlm.nih.gov/24867847/) | 2014 | Subgroup Analysis | *Neurological Sciences* | Pooled analysis evaluating frovatriptan efficacy in normal-weight vs. obese patients across three Italian randomised studies of migraine with or without aura |
| [23695053](https://pubmed.ncbi.nlm.nih.gov/23695053/) | 2013 | Subgroup Analysis | *Neurological Sciences* | Subgroup analysis comparing frovatriptan vs. other triptans in hypertensive vs. normotensive migraineurs; notes consistent efficacy across vascular risk subgroups |
| [15311727](https://pubmed.ncbi.nlm.nih.gov/15311727/) | 2004 | Pharmacological Review | *International Journal of Clinical Practice* | Early pharmacological review following FDA approval; documents high 5-HT1B/1D receptor affinity, long elimination half-life, and efficacy in migraine with or without aura |

---

## Canada Market Information

Frovatriptan is not currently marketed in Canada. No Drug Identification Numbers (DINs) are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The ICHD-3 reclassification of basilar-type migraine to "migraine with brainstem aura" reflects a mechanistic shift — CSD propagation rather than vasospasm — that removes the primary theoretical basis for triptan contraindication in this subtype. Frovatriptan's long half-life, high receptor selectivity, and established efficacy across migraine-with-aura presentations provide a biologically coherent and clinically plausible basis for further evaluation. The available evidence is indirect (L3: subgroup analyses and systematic reviews) but directionally consistent.

**To proceed, the following is needed:**

- **Detailed safety data**: Retrieve full prescribing information (package insert warnings, contraindications, cardiovascular precautions) to confirm safety profile before clinical use in this subtype
- **Mechanism of action confirmation**: Obtain formal MOA data from DrugBank (DG002) to complete the mechanistic bridging argument
- **Prospective subtype-specific study**: A dedicated open-label pilot or crossover RCT in patients with confirmed ICHD-3 migraine with brainstem aura is needed to upgrade evidence from L3 to L1/L2
- **Cardiovascular risk stratification**: Given residual theoretical concerns about brainstem vascular effects, enrolment criteria should exclude patients with established cerebrovascular disease, hemiplegic migraine co-diagnosis, or significant cardiovascular risk factors
- **Canada regulatory pathway**: As frovatriptan holds no DINs in Canada, a full New Drug Submission or reliance on existing FDA/EMA approvals would be required before any local clinical programme
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

