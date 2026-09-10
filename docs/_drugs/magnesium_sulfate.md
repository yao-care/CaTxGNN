---
layout: default
title: Magnesium Sulfate
parent: 僅模型預測 (L5)
nav_order: 485
evidence_level: L5
indication_count: 10
---

# Magnesium Sulfate
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

# Magnesium Sulfate: From Not Marketed in Canada to Preeclampsia/Eclampsia

## One-Sentence Summary

Magnesium sulfate (DrugBank DB00653) currently has no active market authorization or approved indication on file in Canada.
The TxGNN model predicts it may be effective for **preeclampsia/eclampsia**,
with **50 clinical trials** and **20 publications** currently supporting this direction — including a landmark large-scale RCT (the Magpie Trial) and a Cochrane systematic review.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented — drug has no license on file in Canada (0 DINs) |
| Predicted New Indication | Preeclampsia/Eclampsia |
| TxGNN Prediction Score | 99.9992% |
| Evidence Level | L1 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in DrugBank for this candidate. However, the clinical literature collected in this evidence pack itself describes a consistent pharmacological picture: magnesium sulfate acts centrally as an anticonvulsant (NMDA-receptor antagonism, reduction of hippocampal seizure activity — Cotton et al. 1992), and peripherally as a cerebral vasodilator that opposes calcium-dependent arterial vasospasm and reduces cerebral perfusion pressure (Sadeh 1989; Belfort et al. 2006). These mechanisms map directly onto the pathophysiology of eclamptic seizures, which are believed to involve cerebral vasospasm, endothelial dysfunction, and disrupted autoregulation of cerebral blood flow.

Magnesium sulfate is already widely reported in the literature as "the drug of choice" for seizure prophylaxis and treatment in preeclampsia/eclampsia (Sibai 1990; Witlin & Sibai 1998), a role reinforced by decades of accumulated RCT evidence, including the large multinational **Magpie Trial** and a **Cochrane systematic review** confirming its superiority over other anticonvulsants for this indication. Because this evidence base is so extensive and consistent, the TxGNN prediction aligns strongly with independently established real-world clinical use — even though this specific evidence pack lacks a documented "original indication" or formal MOA entry for the jurisdiction in question.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00004399](https://clinicaltrials.gov/study/NCT00004399) | N/A | Completed | 2000 | Randomized comparison of nimodipine vs. magnesium sulfate for prevention of eclamptic seizures in severe preeclampsia |
| [NCT01492608](https://clinicaltrials.gov/study/NCT01492608) | Phase 3 | Completed | 560 | MASP-STUDY: antenatal magnesium sulphate for prevention of cerebral palsy and death in preterm infants |
| [NCT02317146](https://clinicaltrials.gov/study/NCT02317146) | Phase 2/3 | Completed | 280 | Novel postpartum magnesium sulfate protocol (6 vs 24 hours) in severe preeclampsia |
| [NCT01911494](https://clinicaltrials.gov/study/NCT01911494) | N/A | Completed | 87,500 | CLIP cluster-RCT: community-level care package (including MgSO4 access) for hypertensive disorders of pregnancy |
| [NCT04576364](https://clinicaltrials.gov/study/NCT04576364) | N/A | Completed | 280 | 12-hour vs 24-hour postpartum magnesium sulphate for preeclampsia with severe features |
| [NCT00344058](https://clinicaltrials.gov/study/NCT00344058) | N/A | Completed | 200 | Abbreviated postpartum magnesium sulfate seizure prophylaxis: 12 vs 24 hour regimens |
| [NCT01408979](https://clinicaltrials.gov/study/NCT01408979) | Phase 4 | Completed | 120 | Postpartum prophylaxis with short-course magnesium sulfate in severe preeclampsia |
| [NCT02396030](https://clinicaltrials.gov/study/NCT02396030) | Phase 4 | Terminated | 62 | 1g/hour vs 2g/hour magnesium sulfate maintenance dose for eclampsia prevention |
| [NCT03318211](https://clinicaltrials.gov/study/NCT03318211) | Phase 4 | Unknown | 100 | Continuation vs discontinuation of magnesium sulfate after delivery in severe preeclampsia |
| [NCT02835339](https://clinicaltrials.gov/study/NCT02835339) | Phase 4 | Completed | 66 | Pharmacokinetics of magnesium sulfate in obese preeclamptic women |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12057549](https://pubmed.ncbi.nlm.nih.gov/12057549/) | 2002 | RCT | Lancet | The Magpie Trial — landmark placebo-controlled RCT establishing magnesium sulfate's benefit for women with pre-eclampsia and their babies |
| [12576241](https://pubmed.ncbi.nlm.nih.gov/12576241/) | 2003 | RCT | Obstetrics and Gynecology | Randomized controlled trial: magnesium sulfate in women with mild preeclampsia to prevent disease progression |
| [38865319](https://pubmed.ncbi.nlm.nih.gov/38865319/) | 2024 | RCT | PLoS One | Springfusor pump vs standard-of-care MgSO4 administration — acceptability trial for preeclampsia/eclampsia |
| [21069663](https://pubmed.ncbi.nlm.nih.gov/21069663/) | 2010 | Review (Cochrane) | Cochrane Database of Systematic Reviews | Systematic review: magnesium sulphate and other anticonvulsants for women with pre-eclampsia |
| [9794688](https://pubmed.ncbi.nlm.nih.gov/9794688/) | 1998 | Review | Obstetrics and Gynecology | Review of efficacy, benefits, and risks of magnesium sulfate seizure prophylaxis in preeclampsia/eclampsia |
| [2288560](https://pubmed.ncbi.nlm.nih.gov/2288560/) | 1990 | Review | American Journal of Obstetrics and Gynecology | Magnesium sulfate as the ideal anticonvulsant in preeclampsia-eclampsia |
| [16978425](https://pubmed.ncbi.nlm.nih.gov/16978425/) | 2006 | Review | Obstetrical & Gynecological Survey | Cerebral hemodynamics in preeclampsia and rationale for magnesium sulfate use |
| [25353716](https://pubmed.ncbi.nlm.nih.gov/25353716/) | 2015 | Review | Acta Obstetricia et Gynecologica Scandinavica | Reducing maternal mortality from preeclampsia/eclampsia in low-resource countries |
| [36413336](https://pubmed.ncbi.nlm.nih.gov/36413336/) | 2023 | Observational | Biological Trace Element Research | Incidence and risk factors of critical hypermagnesemia under MgSO4 regimen in severe preeclampsia |
| [39110688](https://pubmed.ncbi.nlm.nih.gov/39110688/) | 2024 | Qualitative study | PLoS One | Nurse-midwife perspectives on providing magnesium sulfate for preeclampsia/eclampsia in Tanzania |

## Canada Market Information

Magnesium sulfate currently holds no active drug license (DIN) in Canada per the available regulatory data (market status: not marketed, 0 licenses on file). No approved Canadian indication text is therefore available for reference.

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data are not currently available in this evidence pack — notably, TFDA/Health Canada label warnings and contraindications are flagged as a **Blocking** data gap (DG001), meaning this candidate cannot yet proceed to initial safety screening (S1).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Efficacy evidence for magnesium sulfate in preeclampsia/eclampsia is exceptionally strong (L1: multiple completed Phase 2/3/4 RCTs, a landmark large-scale RCT, and a Cochrane systematic review). However, this candidate cannot advance because label warnings/contraindications data is marked as a **Blocking** gap, and the drug currently has no market authorization in Canada.

**To proceed, the following is needed:**
- TFDA/Health Canada product monograph (warnings, contraindications, DDI) to complete S1 safety screening
- Confirmed DrugBank mechanism of action data for formal mechanistic linkage analysis
- Clarification of current Canadian regulatory/licensing pathway, since no DIN is currently on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

