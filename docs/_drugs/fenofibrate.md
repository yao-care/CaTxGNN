---
layout: default
title: Fenofibrate
parent: Model Prediction Only (L5)
nav_order: 380
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
description: "Fenofibrate: predicted new indication Homozygous familial hypercholesterolemia (evidence level L5). Approved use: Hypertriglyceridemia and hyperlipidemia (including familial and combi…"
monitor_inn: "FENOFIBRATE"
predicted_indications: ["homozygous familial hypercholesterolemia", "hyperlipoproteinemia", "cholesterol-ester transfer protein deficiency", "hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency", "hyperlipidemia due to hepatic triglyceride lipase deficiency", "hypercholesterolemia, autosomal dominant"]
---

# Fenofibrate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Fenofibrate: From Hyperlipidemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Fenofibrate is a lipid-lowering drug originally used for hypertriglyceridemia and several forms of hyperlipidemia.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia**, but the only linked trial tests a different drug (alirocumab), and the supporting literature is indirect.
Evidence for this top-ranked prediction is weak. The strongest evidence in the data compiled for this report is for a lower-ranked prediction, **hyperlipoproteinemia**, which largely overlaps the drug's existing use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertriglyceridemia and hyperlipidemia (including familial and combined forms). The Canadian licence records contain no indication text. |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 (rank 1 prediction); the hyperlipoproteinemia prediction reaches L1 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, fenofibrate is a PPAR-alpha agonist. It lowers triglycerides, raises HDL-C, and modestly lowers LDL-C.

Homozygous familial hypercholesterolemia (HoFH) is caused by a severe LDL receptor pathway defect. Fenofibrate's mechanism does not compensate for that defect, so its link to HoFH is weak. It may only be useful as an adjunct when triglycerides are also elevated.

Other predictions fit better. For **hyperlipoproteinemia**, PPAR-alpha activation increases lipoprotein lipase activity, reduces apoC-III and lowers VLDL and triglycerides. This is consistent with fenofibrate's existing lipid indications, so it is better described as an extension of labeled use than as true repurposing.

---

## Clinical Trial Evidence

**Top prediction: homozygous familial hypercholesterolemia**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Alirocumab in children and adolescents with HoFH. Fenofibrate is not the intervention, so this gives no direct evidence. |

**Better-supported prediction: hyperlipoproteinemia (mixed hyperlipidemia)**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00349375](https://clinicaltrials.gov/study/NCT00349375) | Phase 3 | Completed | 1040 | Fenofibrate 145 mg plus simvastatin vs simvastatin alone in mixed dyslipidemia |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Phase 3 | Completed | 576 | Fenofibrate and ezetimibe coadministration in mixed hyperlipidemia |
| [NCT00092560](https://clinicaltrials.gov/study/NCT00092560) | Phase 3 | Completed | 587 | Fenofibrate and ezetimibe coadministration in mixed hyperlipidemia |
| [NCT00459745](https://clinicaltrials.gov/study/NCT00459745) | Phase 3 | Completed | 481 | Pravastatin, fenofibrate, or their combination in combined hyperlipidemia, with a 52-week open-label safety phase |
| [NCT01956201](https://clinicaltrials.gov/study/NCT01956201) | Phase 3 | Unknown | 476 | Fenofibrate added to atorvastatin vs atorvastatin in mixed hypercholesterolemia; results unverified |
| [NCT00362934](https://clinicaltrials.gov/study/NCT00362934) | Phase 3 | Completed | 516 | Fenofibrate plus simvastatin vs atorvastatin monotherapy in mixed dyslipidemia |
| [NCT00362206](https://clinicaltrials.gov/study/NCT00362206) | Phase 3 | Completed | 423 | Fenofibrate plus simvastatin vs pravastatin monotherapy in mixed dyslipidemia |
| [NCT00006412](https://clinicaltrials.gov/study/NCT00006412) | Phase 3 | Completed | 630 | Fenofibrate vs pravastatin in HIV-infected patients with lipid abnormalities |
| [NCT00754039](https://clinicaltrials.gov/study/NCT00754039) | Phase 4 | Completed | 129 | Welchol plus TriCor vs TriCor alone in mixed hyperlipidemia |
| [NCT00349284](https://clinicaltrials.gov/study/NCT00349284) | Phase 3 | Completed | 181 | Fenofibrate, ezetimibe, and their combination in type IIb dyslipidemia with metabolic syndrome |

These are the 10 most relevant of 26 registered trials for this prediction.

---

## Literature Evidence

**Homozygous familial hypercholesterolemia**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6593751](https://pubmed.ncbi.nlm.nih.gov/6593751/) | 1984 | Cohort | Pharmacol Res Commun | In type II hyperlipoproteinemia, fenofibrate lowered total cholesterol by about 22% and LDL-C by about 24%. One HoFH patient showed the greatest fall in total and LDL cholesterol. |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart J | Fenofibrate monotherapy is most clearly indicated for fasting triglycerides above 500 mg/dl. It is a non-statin option for dyslipidaemia. |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE dyslipidemia management guideline (general, not specific to fenofibrate in HoFH) |

**Hyperlipoproteinemia**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11942772](https://pubmed.ncbi.nlm.nih.gov/11942772/) | 2002 | RCT | Endocr Pract | Fenofibrate vs gemfibrozil in type IIa/IIb hyperlipoproteinemia (crossover) |
| [8847874](https://pubmed.ncbi.nlm.nih.gov/8847874/) | 1996 | RCT | J Cardiovasc Pharmacol | Micronized fenofibrate vs simvastatin in type IIa/IIb hyperlipoproteinemia |
| [9110923](https://pubmed.ncbi.nlm.nih.gov/9110923/) | 1997 | RCT | Eur J Med Res | Bezafibrate vs micronized fenofibrate in type III hyperlipoproteinemia |
| [12816176](https://pubmed.ncbi.nlm.nih.gov/12816176/) | 2003 | RCT | Int J Clin Pharmacol Ther | Fenofibrate and simvastatin effects on sICAM-1 and MCP-1 in hyperlipoproteinemia |
| [2226216](https://pubmed.ncbi.nlm.nih.gov/2226216/) | 1990 | Review | Drugs | Pharmacology and therapeutic use of fenofibrate in dyslipidaemia |

**Other lower-ranked predictions with some human data**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16224048](https://pubmed.ncbi.nlm.nih.gov/16224048/) | 2005 | Clinical kinetic study | Arterioscler Thromb Vasc Biol | Fenofibrate effects on lipoprotein composition and kinetics in 2 patients with complete hepatic lipase deficiency |
| [16337207](https://pubmed.ncbi.nlm.nih.gov/16337207/) | 2006 | Clinical kinetic study | Atherosclerosis | Fenofibrate and apolipoprotein kinetics in patients with coexisting dysbetalipoproteinemia and heterozygous familial hypercholesterolemia |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02269082 | LIPIDIL EZ | Not specified | Not specified |
| 02390701 | SANDOZ FENOFIBRATE E | Not specified | Not specified |
| 02246859 | AA-FENO-SUPER | Not specified | Not specified |
| 02246860 | AA-FENO-SUPER | Not specified | Not specified |
| 02390698 | SANDOZ FENOFIBRATE E | Not specified | Not specified |

Ten valid single-ingredient licences are held in total; the first five are listed here.

---

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: liver failure and liver disease, pancreatitis, gallbladder disease and cholelithiasis, myopathy and rhabdomyolysis, impaired renal function, and blood disorders (thrombocytopenia, anemia, leukopenia, neutropenia, agranulocytosis).
- **Drug Interactions**: 100 interactions were found, all of Moderate level among those shown. They include sulfonylureas (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide), many insulin products, chenodeoxycholic acid, and esomeprazole.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, homozygous familial hypercholesterolemia)

**Rationale:**
- Fenofibrate's mechanism does not address the LDL receptor defect in HoFH, and the only linked trial tests alirocumab. Evidence is indirect only (L4).
- The hyperlipoproteinemia prediction has many Phase 3 trials (L1, Proceed with Guardrails), but it largely overlaps the existing approved use. Familial hypercholesterolemia and autosomal dominant hypercholesterolemia are research questions at best (L3), where fenofibrate is less potent than statins for LDL-C.

**To proceed, the following is needed:**
- Fenofibrate-specific clinical data in HoFH (for example, adjunct use with triglyceride elevation)
- Mechanism of action data
- Health Canada package insert warnings and contraindications, plus approved indication text for each DIN
- A safety monitoring plan covering liver, renal, muscle, and gallbladder risks, and glucose-lowering drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

