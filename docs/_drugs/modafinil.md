---
layout: default
title: Modafinil
parent: Model Prediction Only (L5)
nav_order: 627
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-05
monitor_inn: "MODAFINIL"
predicted_indications: ["insomnia (disease)"]
description: "Modafinil: predicted new indication Insomnia (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Modafinil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Modafinil: Insomnia (disease)
{: .text-alpha }

## One-Sentence Summary

Modafinil is a wake-promoting agent used for sleep-wake disorders marketed in Canada.
The TxGNN model predicts it may be effective for **insomnia (disease)**, but the evidence level is **L5**: no completed study with posted or published results directly addresses insomnia.
The data compiled for this report include **2 clinical trials** and **19 publications**, but they mostly concern daytime sleepiness and fatigue, not insomnia itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 7 of 7) |
| Number of DINs | 7 (marketed: 7) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Modafinil is generally understood to be a wake-promoting agent that acts through dopamine transporter inhibition and modulation of monoaminergic and orexin/histamine wake circuits.

That mechanism addresses excessive sleepiness and impaired wakefulness. It does not obviously address the hyperarousal or sleep-initiation and maintenance failure that characterise insomnia. The very high TxGNN score (0.9985) most likely reflects network proximity to other sleep-wake disorders rather than a true therapeutic fit.

The plausible link is limited to daytime wake dysfunction in people with sleep disturbance. Using a stimulant for insomnia is mechanistically counterintuitive and could worsen nighttime sleep, so this prediction should be treated with caution.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00124384](https://clinicaltrials.gov/study/NCT00124384) | Phase 4 | Completed | 40 | Examined modafinil alone or with cognitive behavioural therapy for insomnia on daytime functioning and insomnia severity. No results are posted or published, and the population is not clearly primary insomnia. |
| [NCT00626210](https://clinicaltrials.gov/study/NCT00626210) | Phase 4 | Terminated | 2 | Modafinil for sleep/wake disturbances in older adults. Terminated after 2 participants, so no interpretable data. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24312590](https://pubmed.ncbi.nlm.nih.gov/24312590/) | 2013 | Systematic review/meta-analysis | PloS one | Efficacy and safety of modafinil for fatigue and excessive daytime sleepiness in neurological disorders; earlier trials gave inconsistent results. |
| [27010071](https://pubmed.ncbi.nlm.nih.gov/27010071/) | 2016 | Systematic review/meta-analysis | Parkinsonism & Related Disorders | Pharmacological options for daytime sleepiness and sleep disorders in Parkinson's disease. |
| [18729534](https://pubmed.ncbi.nlm.nih.gov/18729534/) | 2008 | Review | Drugs | Evidence-based review of approved and investigational uses of modafinil, based on randomised placebo-controlled trials. |
| [22021174](https://pubmed.ncbi.nlm.nih.gov/22021174/) | 2011 | Systematic review | Movement Disorders | Evidence review of treatments for non-motor symptoms of Parkinson's disease. |
| [17181377](https://pubmed.ncbi.nlm.nih.gov/17181377/) | 2006 | Review | Drugs | Burden and management of shift work sleep disorder. |
| [21904092](https://pubmed.ncbi.nlm.nih.gov/21904092/) | 2011 | Review | Postgraduate Medicine | Theories and therapies for shift work disorder, which can include insomnia during scheduled sleep. |
| [17060310](https://pubmed.ncbi.nlm.nih.gov/17060310/) | 2006 | Case series | American Journal of Hospice & Palliative Care | Modafinil reduced fatigue in Charcot-Marie-Tooth disease type 1A. |

None of these publications directly studies modafinil as a treatment for insomnia.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02239665 | ALERTEC | Not specified | Not specified |
| 02285398 | APO-MODAFINIL | Not specified | Not specified |
| 02420260 | TEVA-MODAFINIL | Not specified | Not specified |
| 02430487 | AURO-MODAFINIL | Not specified | Not specified |
| 02432560 | MAR-MODAFINIL | Not specified | Not specified |

All 7 single-ingredient licences are currently valid; the table lists five of them.

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were found. Moderate-level examples include rabeprazole, omeprazole, esomeprazole, dexamethasone, eliglustat, linagliptin and cisapride. Most others listed are minor (for example hydrocortisone, cimetidine, clarithromycin).

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5. The only insomnia-related trial (NCT00124384) was completed without posted or published results, and the other studies address fatigue or daytime sleepiness. The wake-promoting mechanism also runs counter to insomnia treatment, so the high model score is not enough to proceed.

**To proceed, the following is needed:**
- Results from NCT00124384, or a new randomised trial of modafinil in well-defined insomnia
- Detailed mechanism-of-action data and a rationale for how a wake-promoting drug could help insomnia
- Package insert warnings and contraindications, plus an assessment of the risk of worsening nighttime sleep

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

