---
layout: default
title: Ezetimibe
parent: Model Prediction Only (L5)
nav_order: 373
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
monitor_inn: "EZETIMIBE"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
description: "Ezetimibe: predicted new indication Cholesterol-ester transfer protein deficiency (evidence level L5). Approved use: Not recorded in the local data"
---

# Ezetimibe
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

## Ezetimibe: Cholesterol-ester transfer protein deficiency
{: .text-alpha }

## One-Sentence Summary

Ezetimibe is a cholesterol-absorption inhibitor originally used to treat hyperlipidemia, including familial and homozygous familial hypercholesterolemia and sitosterolemia.
Because this prediction overlaps closely with the original indications, it is better described as an on-label or near-label use than as true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Cholesterol-ester transfer protein deficiency |
| TxGNN Prediction Score | 0.9909 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 19 of 19) |
| Number of DINs | 19 (valid: 19) |
| Recommended Decision | Proceed with Guardrails |

Note: The Health Canada records compiled for this report contain no approved indication text.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the evidence reviewed, ezetimibe blocks NPC1L1-mediated cholesterol absorption in the intestine. This lowers LDL cholesterol and complements statins.

Hyperlipoproteinemia is a disorder of lipid and lipoprotein levels, and it is essentially the same disease family as the hyperlipidemia for which ezetimibe is already used. The same mechanism applies, so the prediction is reasonable. Phase 3 and Phase 4 trials, including combination studies with statins, fenofibrate and PCSK9 inhibitors, support the use.

For context, the other predicted indications were weaker:
- This overlaps with the original indications and is not novel repurposing. The effect is smaller in homozygous disease with absent LDL receptor activity.
- There are no clinical trials. Evidence level L4, decision Hold.
- **Cholesterol-ester transfer protein deficiency (0.9909)**: No direct evidence exists. Evidence level L5, decision Hold.

---

## Clinical Trial Evidence

The table lists the most relevant trials for hyperlipoproteinemia.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00753883](https://clinicaltrials.gov/study/NCT00753883) | Phase 4 | Completed | 40 | Randomized comparison of adding ezetimibe to a statin versus statin alone for lipid lowering |
| [NCT01984424](https://clinicaltrials.gov/study/NCT01984424) | Phase 3 | Completed | 511 | Evolocumab versus ezetimibe on LDL-C in statin-intolerant patients, with ezetimibe as the active comparator |
| [NCT03847506](https://clinicaltrials.gov/study/NCT03847506) | Phase 4 | Completed | 127 | Ezetimibe/rosuvastatin plus candesartan/amlodipine in patients with hypertension and hyperlipidemia |
| [NCT00092833](https://clinicaltrials.gov/study/NCT00092833) | Phase 3 | Terminated | 49 | Open-label treatment-use study of ezetimibe 10 mg/day in homozygous FH or sitosterolemia |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe 10 mg added to atorvastatin or simvastatin in homozygous FH |
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | ENHANCE: ezetimibe plus high-dose simvastatin versus simvastatin alone on carotid atherosclerosis in heterozygous FH |
| [NCT00271817](https://clinicaltrials.gov/study/NCT00271817) | Phase 3 | Completed | 1220 | Ezetimibe/simvastatin plus extended-release niacin in type IIa/IIb hyperlipidemia |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Phase 3 | Completed | 576 | Fenofibrate plus ezetimibe in mixed hyperlipidemia |
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Phase 3 | Completed | 611 | Ezetimibe/simvastatin plus fenofibrate in mixed hyperlipidemia |
| [NCT00704535](https://clinicaltrials.gov/study/NCT00704535) | N/A | Completed | 4105 | Post-marketing surveillance of ezetimibe safety, tolerability and efficacy in Filipino patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | RCT (Phase 3) | Lancet | TANDEM: obicetrapib/ezetimibe fixed-dose combination for LDL-C reduction |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | RCT | JAMA | Oral PCSK9 inhibitor enlicitide in heterozygous FH, with background lipid-lowering therapy |
| [25282519](https://pubmed.ncbi.nlm.nih.gov/25282519/) | 2015 | RCT | Lancet | RUTHERFORD-2: evolocumab in heterozygous FH patients not at LDL-C goal despite statin with or without ezetimibe |
| [37850379](https://pubmed.ncbi.nlm.nih.gov/37850379/) | 2024 | RCT | Circulation | ORION-5: inclisiran in homozygous FH |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Review | J Am Coll Cardiol | New and emerging LDL-C-lowering therapies on top of statins, ezetimibe and PCSK9 inhibitors |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Review | Mol Med Rep | Advances in drugs targeting hyperlipidemia |
| [19654419](https://pubmed.ncbi.nlm.nih.gov/19654419/) | 2009 | Review | Drug Ther Bull | Update on ezetimibe: lowers LDL-C alone or with a statin, with no demonstrated effect on cardiovascular outcomes at that time |
| [35101175](https://pubmed.ncbi.nlm.nih.gov/35101175/) | 2022 | Cohort | Lancet | Worldwide retrospective cohort of homozygous FH patients and their treatment outcomes |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Review | Cardiol Clin | Familial hypercholesterolemia treatments, including ezetimibe |
| [29219151](https://pubmed.ncbi.nlm.nih.gov/29219151/) | 2017 | Review | Nat Rev Dis Primers | Overview of familial hypercholesterolaemia |

---

## Canada Market Information

Ezetimibe has 19 valid single-ingredient authorizations in Canada. The records compiled for this report do not include dosage form or approved indication text. Five main authorizations are listed.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02247521 | EZETROL | Not available | Not available |
| 02354101 | TEVA-EZETIMIBE | Not available | Not available |
| 02416778 | SANDOZ EZETIMIBE | Not available | Not available |
| 02419548 | TARO-EZETIMIBE | Not available | Not available |
| 02416409 | PMS-EZETIMIBE | Not available | Not available |

---

## Safety Considerations

Warnings and contraindications from the Canadian package insert are not available in the data compiled for this report. Please refer to the package insert for full safety information.

- **Conditions linked to ezetimibe in the knowledge graph (not label text)**: pancreatitis, liver disease, gallbladder disease, myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, substance abuse/dependence, rhabdomyolysis and nodular fasciitis. These need verification against the label.
- **Drug interactions**: 100 interactions were identified. Those rated Moderate:
  - Chenodeoxycholic acid
  - Eluxadoline
  - Rosuvastatin
  - Simvastatin

  Many others, such as calcitriol, pantoprazole, glimepiride, metformin and omeprazole, have an unknown severity level.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Multiple completed Phase 3 trials and large post-marketing studies support ezetimibe in hyperlipidemia and familial hypercholesterolemia. The predicted indication shares the same mechanism as the established use and is largely on-label.
- Safety data from the Canadian label are missing, so the decision carries guardrails.

**To proceed, the following is needed:**
- Download and review the Health Canada package insert for warnings, contraindications, dosage forms and approved indications
- Detailed mechanism of action data from DrugBank
- Confirmation of how hyperlipoproteinemia is defined and how it differs from the already-approved indications
- Review of the knowledge-graph contraindications (liver disease, myopathy, pancreatitis, gallbladder disease) against the label
- Monitoring plan for statin co-administration, given the moderate interactions with rosuvastatin and simvastatin
- For the two lower-ranked predictions (CYP7A1 deficiency and CETP deficiency), no further action unless direct clinical or mechanistic evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

