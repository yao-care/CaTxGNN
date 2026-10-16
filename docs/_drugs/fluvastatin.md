---
layout: default
title: Fluvastatin
parent: Model Prediction Only (L5)
nav_order: 406
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Fluvastatin: predicted new indication Hyperlipoproteinemia (evidence level L5). Approved use: Arteriosclerosis disorder, atherosclerosis…"
monitor_inn: "FLUVASTATIN"
predicted_indications: ["hyperlipoproteinemia", "homozygous familial hypercholesterolemia", "hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency", "familial hypercholesterolemia", "HIV infectious disease", "cholesterol-ester transfer protein deficiency", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "fibroma of prostate"]
---

# Fluvastatin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Fluvastatin: From Familial Hyperlipidemia and Atherosclerosis to Hyperlipoproteinemia

## One-Sentence Summary

Fluvastatin is a statin originally used for hyperlipidemia (including familial combined hyperlipidemia) and atherosclerosis.
The TxGNN model predicts it may be effective for **hyperlipoproteinemia**, with **1 listed clinical trial** (which tests a different drug) and **20 publications** in the data compiled for this report. Because the predicted use overlaps closely with the drug's known lipid-lowering role, this is closer to an on-label or near-label use than a true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Arteriosclerosis disorder, atherosclerosis, familial combined hyperlipidemia (from the knowledge graph; no approved indication text is available for the Canadian licences) |
| Predicted New Indication | Hyperlipoproteinemia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 (per the evidence scoring in the compiled data; see the note below) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Proceed with Guardrails |

> Note on evidence level: the only listed trial (NCT03510715) tests alirocumab, not fluvastatin. The L1 grade rests mainly on fluvastatin RCTs in the literature. The directly relevant Phase 3 fluvastatin trial (NCT00171236) is listed under familial hypercholesterolemia, below.

---

## Why is This Prediction Reasonable?

Fluvastatin inhibits HMG-CoA reductase, which lowers hepatic cholesterol synthesis. This upregulates LDL receptors and reduces LDL cholesterol. This is the drug's core mechanism, and it fits the lipid disorders in the original indications.

Hyperlipoproteinemia is a broad group of lipid disorders that includes the familial combined hyperlipidemia fluvastatin was already linked to. The published fluvastatin studies cover monotherapy, combinations with bezafibrate or fenofibrate, and extended-release versus immediate-release formulations in hypercholesterolemic and mixed hyperlipidemic patients.

Detailed mechanism-of-action data was not available in the compiled data, so the mechanism above reflects well-known statin pharmacology.

### Other Predicted Indications

| Predicted Indication | Score | Evidence Level | Decision |
|------|------|------|------|
| Familial hypercholesterolemia | 99.89% | L1 | Proceed with Guardrails |
| HIV infectious disease | 99.88% | L3 | Research Question |
| Homozygous familial hypercholesterolemia | 99.97% | L4 | Hold |
| Other predictions (7 diseases, including CETP deficiency, cholesterol 7α-hydroxylase deficiency, and prostate fibroma) | 99.75%–99.89% | L5 | Hold |

- **Familial hypercholesterolemia** has the strongest direct evidence. A completed Phase 3 trial of fluvastatin in children with heterozygous disease (NCT00171236, n=84) is supported by several fluvastatin studies.
- **Homozygous familial hypercholesterolemia** is expected to respond poorly, because these patients have little or no functional LDL receptor activity, and no fluvastatin-specific evidence exists.
- **HIV infection** evidence concerns lipid management in patients on antiretrovirals, not antiviral efficacy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label alirocumab study in children and adolescents with homozygous familial hypercholesterolemia. It does not test fluvastatin and shows only that the disease area has active research. |

For the related indication familial hypercholesterolemia, the directly relevant trial is [NCT00171236](https://clinicaltrials.gov/study/NCT00171236), a completed Phase 3 trial (n=84) of fluvastatin in children with heterozygous disease.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17062478](https://pubmed.ncbi.nlm.nih.gov/17062478/) | 2006 | RCT | Acta Paediatr | Fluvastatin in children and adolescents with heterozygous familial hypercholesterolaemia, assessing lipid profiles and vascular changes |
| [15598476](https://pubmed.ncbi.nlm.nih.gov/15598476/) | 2004 | RCT | Clin Ther | Fluvastatin plus fenofibrate vs fluvastatin alone over 12 months in combined hyperlipidemia, type 2 diabetes and coronary heart disease |
| [11219479](https://pubmed.ncbi.nlm.nih.gov/11219479/) | 2001 | RCT | Clin Ther | Fluvastatin 80 mg extended-release vs immediate-release in primary hypercholesterolemia |
| [10856536](https://pubmed.ncbi.nlm.nih.gov/10856536/) | 2000 | Clinical study | Atherosclerosis | FACT study: fluvastatin plus bezafibrate in 333 patients with mixed hyperlipidaemia and coronary artery disease |
| [8157036](https://pubmed.ncbi.nlm.nih.gov/8157036/) | 1993 | Clinical study | Eur J Clin Pharmacol | High-dose fluvastatin in 52 patients with familial hypercholesterolaemia (double-blind) |
| [7604789](https://pubmed.ncbi.nlm.nih.gov/7604789/) | 1995 | Clinical study | Am J Cardiol | Fluvastatin effects on lipid profile and apolipoproteins in 31 Chinese patients with hypercholesterolemia |
| [10067240](https://pubmed.ncbi.nlm.nih.gov/10067240/) | 1998 | Cohort | Ter Arkh | Variability of the lipid-lowering action of simvastatin and fluvastatin in primary hyperlipoproteinemia |
| [8462180](https://pubmed.ncbi.nlm.nih.gov/8462180/) | 1993 | Review | Circulation | Overview of dyslipoproteinemia drug treatment, focusing on fluvastatin |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Review | Clin Ther | Rosuvastatin in hyperlipidemia (a different statin; indirect evidence) |
| [11347136](https://pubmed.ncbi.nlm.nih.gov/11347136/) | 2001 | Review | Nihon Rinsho | Review of fluvastatin (Japanese) |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02299224 | TEVA-FLUVASTATIN | Not specified | Not specified |
| 02299232 | TEVA-FLUVASTATIN | Not specified | Not specified |

Both licences are valid single-ingredient products.

---

## Safety Considerations

- **Disease contraindications (knowledge graph, not label text)**: liver disease, gallbladder disease, myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, hypotensive disorder, substance abuse/dependence, rhabdomyolysis, nodular fasciitis, and injury.
- **Drug interactions**: The interaction query returned 100 entries. Those shown include:
  - **Moderate**: aprepitant, metronidazole, oxandrolone, naltrexone, nateglinide, nitisinone, rosuvastatin, simvastatin, tinidazole, glyburide, pectin
  - **Unknown severity**: calcitriol, doxycycline, cimetidine, epinephrine, mannitol, dicyclomine, famotidine, acetylsalicylic acid, pantoprazole

  Combining fluvastatin with other statins (rosuvastatin, simvastatin) warrants particular attention.

Package insert warnings and contraindications were not available. Please refer to the Canadian package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Fluvastatin has a well-established lipid-lowering mechanism, and several fluvastatin RCTs and clinical studies support its use in hyperlipoproteinemia and familial hypercholesterolemia. This is essentially a near-label use, but the only listed trial tests a different drug.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text, dosage forms, and manufacturer details for the two Canadian DINs
- Detailed mechanism-of-action data from DrugBank
- A DDI management plan, given the large number of reported interactions
- Pediatric dosing and safety monitoring if the familial hypercholesterolemia pathway is pursued
- Monitoring for liver and muscle toxicity, in line with the knowledge-graph contraindications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

