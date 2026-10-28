---
layout: default
title: Fluvastatin
parent: Model Prediction Only (L5)
nav_order: 406
evidence_level: L5
indication_count: 6
monitor_inn: "FLUVASTATIN"
predicted_indications: ["HIV infectious disease", "cholesterol-ester transfer protein deficiency", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "fibroma of prostate"]
last_modified_at: 2026-10-28
description: "Fluvastatin: predicted new indication HIV infectious disease (evidence level L5). Approved use: Arteriosclerosis disorder, atherosclerosis…"
---

# Fluvastatin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Fluvastatin: From Atherosclerosis and Familial Combined Hyperlipidemia to HIV Infectious Disease
{: .text-alpha }

## One-Sentence Summary

Fluvastatin is a statin (HMG-CoA reductase inhibitor) whose relations recorded in the knowledge graph are arteriosclerosis disorder, atherosclerosis and familial combined hyperlipidemia.
The TxGNN model predicts it may be useful for **HIV infectious disease**, with **no registered clinical trials** and **13 publications** (mostly about lipid management, drug interactions and biomarkers in people with HIV, not HIV treatment itself).
This is a model-driven research question rather than an established use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Arteriosclerosis disorder, atherosclerosis, familial combined hyperlipidemia (relations recorded in the knowledge graph; the Canadian licence records provide no indication text) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 2 of 2) |
| Number of DINs | 2 (valid: 2) |
| Number of approvals | 2 (both single-ingredient licences) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on known class pharmacology, fluvastatin inhibits HMG-CoA reductase and lowers cholesterol. It has no established direct antiviral mechanism.

The links to HIV are indirect. First, HIV and protease-inhibitor therapy often cause dyslipidemia, and fluvastatin is metabolized mainly through CYP2C9, so it has fewer CYP3A4-mediated interactions with antiretrovirals. Second, statins may have anti-inflammatory and immunomodulatory effects, and one cohort study examined inflammation and immune activation biomarkers in people with HIV. Third, a mouse model of HIV-associated nephropathy showed reduced podocyte injury.

These points support managing HIV-associated comorbidities, not treating HIV infection itself. No cited study shows that fluvastatin treats HIV infection, so the evidence level is capped at L5 under the evidence rules.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12351967](https://pubmed.ncbi.nlm.nih.gov/12351967/) | 2002 | Clinical study | AIDS | Efficacy and safety of fluvastatin in hyperlipidemic HIV patients on protease inhibitors |
| [15293079](https://pubmed.ncbi.nlm.nih.gov/15293079/) | 2004 | Clinical study | Infection | Fluvastatin vs pravastatin for lipid lowering in HIV patients on antiretrovirals; interaction with indinavir |
| [20118492](https://pubmed.ncbi.nlm.nih.gov/20118492/) | 2010 | Open-label RCT | J Antimicrob Chemother | Fluvastatin as adjuvant to pegylated interferon and ribavirin in HIV/HCV co-infection (a hepatitis C question) |
| [19215577](https://pubmed.ncbi.nlm.nih.gov/19215577/) | 2009 | Pilot clinical study | J Viral Hepat | Whether fluvastatin affects HCV replication in HIV-HCV co-infected patients |
| [33238713](https://pubmed.ncbi.nlm.nih.gov/33238713/) | 2021 | Cohort | AIDS Res Hum Retroviruses | Statin use and inflammation and immune activation biomarkers in HIV patients on effective antiretroviral therapy |
| [23703578](https://pubmed.ncbi.nlm.nih.gov/23703578/) | 2013 | Review | Clin Pharmacokinet | Drug interactions between statins and antiviral protease inhibitors |
| [12660532](https://pubmed.ncbi.nlm.nih.gov/12660532/) | 2003 | Review | AIDS | Statins and fibrates for hyperlipidaemia in HIV patients on HAART |
| [19188342](https://pubmed.ncbi.nlm.nih.gov/19188342/) | 2009 | Preclinical (mouse) | Nephrol Dial Transplant | Fluvastatin prevented podocyte injury in a model of HIV-associated nephropathy |
| [19838098](https://pubmed.ncbi.nlm.nih.gov/19838098/) | 2010 | RCT (indirect) | AIDS | Rosuvastatin vs pravastatin in dyslipidemic HIV patients on protease inhibitors; fluvastatin not tested |
| [16868453](https://pubmed.ncbi.nlm.nih.gov/16868453/) | 2006 | Clinical study (indirect) | AIDS | Ezetimibe vs fluvastatin 80 mg for LDL-cholesterol in HIV; LDL fell 20% vs 24% |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02299224 | TEVA-FLUVASTATIN | Not stated | Not stated |
| 02299232 | TEVA-FLUVASTATIN | Not stated | Not stated |

---

## Safety Considerations

Relations recorded in the knowledge graph (not label text) list possible contraindications including liver disease, gallbladder disease, myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, hypotensive disorder, substance abuse/dependence, rhabdomyolysis, nodular fasciitis and injury.

**Drug Interactions** (100 recorded; the main ones are listed):
- **Moderate**: aprepitant, metronidazole, oxandrolone, naltrexone, nateglinide, nitisinone, rosuvastatin, simvastatin, tinidazole, glyburide, pectin
- **Unknown severity**: calcitriol, doxycycline, cimetidine, epinephrine, mannitol, dicyclomine, famotidine, acetylsalicylic acid, pantoprazole

Please refer to the package insert for warnings and contraindications from the label.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by studies of lipid management, drug interactions and biomarkers in people with HIV, plus one mouse study. None shows that fluvastatin treats HIV infection, and no trials are registered. The other predicted indications have model scores only.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications
- Mechanism of action data from DrugBank
- A clear research question (HIV comorbidity management versus antiviral or immunomodulatory effect), with a plan for a controlled study
- Safety review of interactions with antiretrovirals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

