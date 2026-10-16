---
layout: default
title: Simvastatin
parent: High Evidence (L1-L2)
nav_order: 850
evidence_level: L1
indication_count: 8
last_modified_at: 2026-10-13
description: "Simvastatin: predicted new indication Familial hypercholesterolemia (evidence level L1). Approved use: Hypertriglyceridemia, stroke disorder, cerebrovascular disorder…"
---

# Simvastatin
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **8** 
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

# Simvastatin: From Hyperlipidemia and Atherosclerotic Disease to Familial Hypercholesterolemia

## One-Sentence Summary

Simvastatin is a statin originally used to treat lipid disorders such as hypertriglyceridemia, hyperlipoproteinemia and homozygous familial hypercholesterolemia, as well as atherosclerosis and stroke-related conditions.
The TxGNN model predicts it may be effective for **familial hypercholesterolemia**, with **8 clinical trials** and **20 publications** currently supporting this direction.
This is closer to an on-label or closely related indication than a true repurposing, because homozygous familial hypercholesterolemia is already among the original indications.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertriglyceridemia, stroke disorder, cerebrovascular disorder, cerebral infarction, atherosclerosis, hyperlipoproteinemia, homozygous familial hypercholesterolemia (from the knowledge graph; no approved-indication text is available from Health Canada licences) |
| Predicted New Indication | Familial hypercholesterolemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, simvastatin is an HMG-CoA reductase inhibitor. It lowers hepatic cholesterol synthesis and upregulates LDL receptors, which increases clearance of LDL cholesterol.

Familial hypercholesterolemia is a genetic disorder of impaired LDL clearance, so this mechanism applies directly. Homozygous familial hypercholesterolemia is already among the listed original indications. The prediction therefore mostly extends simvastatin to the broader familial hypercholesterolemia group, particularly the heterozygous form.

Other high-scoring predictions include autosomal dominant hypercholesterolemia (99.36%), which overlaps substantially with this indication and has the same evidence base (L1). Predictions for brain stem infarction, CETP deficiency, CYP7A1 deficiency, ABri amyloidosis and a rare neurodevelopmental disorder rest on model output alone or on very weak evidence, and are on Hold. The HIV prediction is a safety-constrained research question, not an efficacy signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | ENHANCE: ezetimibe plus high-dose simvastatin vs simvastatin alone on carotid atherosclerosis progression in heterozygous FH |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Phase 3 | Completed | 248 | Ezetimibe coadministered with simvastatin in adolescents with heterozygous FH (randomized, double-blind) |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Phase 3 | Completed | 249 | Alirocumab vs placebo in heterozygous FH on background lipid-modifying therapy (simvastatin role indirect) |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3 | Completed | 442 | Renal effects of rosuvastatin vs simvastatin in dyslipidaemia, including heterozygous FH (open-label) |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe 10 mg added to atorvastatin or simvastatin in homozygous FH |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Completed | 44 | 24-month open-label safety extension of ezetimibe with atorvastatin or simvastatin in homozygous FH |
| [NCT03510884](https://clinicaltrials.gov/study/NCT03510884) | Phase 3 | Completed | 153 | Alirocumab in children and adolescents with heterozygous FH on statin background |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label alirocumab in children with homozygous FH (simvastatin as background only) |
| [NCT01890967](https://clinicaltrials.gov/study/NCT01890967) | Phase 2 | Completed | 527 | Dose-ranging study of LY3015014 in primary hypercholesterolemia on stable statin therapy (indirect) |

Note: Most trials test simvastatin in combination (mainly with ezetimibe) or as background therapy, so the simvastatin-specific contribution is only clearly shown in the ENHANCE and adolescent ezetimibe/simvastatin studies.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | Trial (ENHANCE) | N Engl J Med | Simvastatin with or without ezetimibe in familial hypercholesterolemia, measuring atherosclerosis progression |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Cochrane systematic review | Cochrane Database Syst Rev | Statins for children with familial hypercholesterolemia |
| [28685504](https://pubmed.ncbi.nlm.nih.gov/28685504/) | 2017 | Cochrane systematic review | Cochrane Database Syst Rev | Earlier update of statins in children with FH |
| [18940534](https://pubmed.ncbi.nlm.nih.gov/18940534/) | 2008 | Clinical study | J Am Coll Cardiol | Efficacy and safety of ezetimibe plus simvastatin in adolescents with heterozygous FH |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Review | Drug Saf | Benefits and risks of simvastatin in familial hypercholesterolaemia |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Review | Expert Opin Drug Saf | Long-term safety and tolerability of simvastatin in FH |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | Comparative study | Nutr Metab Cardiovasc Dis | Atorvastatin vs simvastatin in heterozygous FH for reaching LDL-C goals |
| [2679083](https://pubmed.ncbi.nlm.nih.gov/2679083/) | 1989 | Clinical study | Am J Med | Simvastatin 20 to 40 mg reduced LDL-C by about 38% to 42% in FH |
| [41824590](https://pubmed.ncbi.nlm.nih.gov/41824590/) | 2026 | Guideline | J Am Coll Cardiol | 2026 ACC/AHA multisociety dyslipidemia management guideline |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE guidelines for dyslipidemia and cardiovascular disease prevention |

---

## Canada Market Information

Simvastatin is marketed in Canada with 20 valid single-ingredient licences and no cancelled licences. Dosage form and approved-indication text were not available for these licences. Five of the 20 are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02375605 | JAMP-SIMVASTATIN | Not available | Not available |
| 02549638 | PMSC-SIMVASTATIN | Not available | Not available |
| 02247221 | PRO-SIMVASTATIN | Not available | Not available |
| 02284766 | SIMVASTATIN | Not available | Not available |
| 02469987 | PHARMA-SIMVASTATIN | Not available | Not available |

---

## Safety Considerations

- **Contraindication signals (knowledge graph, not label text)**: Pancreatitis, liver disease, gallbladder disease, thrombocytopenia, hyperglycemia, peptic ulcer disease, myopathy and other muscle diseases, rhabdomyolysis, diabetes mellitus, diabetic ketoacidosis, hypotensive disorder, gout, substance abuse/dependence, blood coagulation disease, acute coronary syndrome, coronary artery disease, myocardial infarction, hemoglobinopathy, and hypophosphatemia. These should be checked against the Canadian product monograph.
- **Drug Interactions**: 100 interactions are recorded. Major-level examples include **amiodarone**, **amlodipine** and **fenofibrate**. Moderate-level examples include nifedipine, paclitaxel, zidovudine, omeprazole, aprepitant, apalutamide and ethanol. Strong CYP3A4 inhibitors, such as HIV protease inhibitors and cobicistat-boosted regimens, markedly raise simvastatin exposure and myopathy risk. The literature describes simvastatin-associated myopathy and rhabdomyolysis in HIV patients.
- **Dose-dependent myopathy**: The risk rises at high doses (the ENHANCE trial used high-dose simvastatin), and pediatric dosing needs particular care.

Please refer to the package insert for warnings and contraindications, because label-based safety data was not available for this report.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 trials, Cochrane reviews and current guidelines support statin-based therapy, including simvastatin, in familial hypercholesterolemia. The indication largely overlaps the existing homozygous FH indication. Safety is the main constraint: the dose-dependent myopathy risk and the large number of drug interactions.

**To proceed, the following is needed:**
- Health Canada product monograph warnings and contraindications (a blocking gap for safety screening)
- Approved indication text and dosage forms for the Canadian licences
- Mechanism of action data from DrugBank
- Clarification of heterozygous vs homozygous disease, pediatric dosing, and the place of combination therapy (ezetimibe, PCSK9 inhibitors) when LDL-C targets are not met
- A DDI management plan, especially for CYP3A4 inhibitors, amiodarone, amlodipine and fibrates

**Other predicted indications:** Hold brain stem infarction, CETP deficiency, CYP7A1 deficiency, ABri amyloidosis and the rare neurodevelopmental disorder, because they rest on model prediction or non-simvastatin evidence. Treat HIV-associated dyslipidemia as a safety-constrained research question, with pitavastatin or pravastatin generally preferred alongside interacting antiretrovirals.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

