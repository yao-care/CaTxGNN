---
layout: default
title: Pravastatin
parent: Moderate Evidence (L3-L4)
nav_order: 763
evidence_level: L4
indication_count: 9
last_modified_at: 2026-10-13
description: "Pravastatin: predicted new indication Homozygous familial hypercholesterolemia (evidence level L4). Approved use: Hyperlipidemia, hypertriglyceridemia, atherosclerosis…"
---

# Pravastatin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **9** 
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

# Pravastatin: From Hyperlipidemia and Atherosclerotic Disease to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Pravastatin is a statin originally used for hyperlipidemia, atherosclerosis and stroke-related disorders.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia**,
but the data compiled for this report contain **1 clinical trial** (which tests a different drug, alirocumab) and **12 publications** (mostly reviews on other lipid-lowering agents), so direct evidence for pravastatin is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperlipidemia, hypertriglyceridemia, atherosclerosis, stroke and cerebrovascular disorders (the Canadian licence records contain no indication text, so this is taken from the knowledge-graph indications) |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, pravastatin inhibits HMG-CoA reductase, which reduces cholesterol synthesis in the liver and upregulates hepatic LDL receptors, increasing LDL clearance from the blood.

The prediction is plausible because pravastatin is already used for hyperlipidemia and is established in heterozygous familial hypercholesterolemia. Homozygous disease sits in the same disease family. However, homozygous FH involves severely reduced or absent LDL receptor function, and the statin mechanism depends on those receptors. Statin efficacy is therefore expected to be limited. One review in the data notes that statins are "not very effective" in homozygous familial hypercholesterolemia.

This is also an extension of an existing lipid-lowering use rather than true repurposing.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label study of alirocumab (a PCSK9 inhibitor) in children and adolescents aged 8–17 with homozygous FH. Pravastatin is not the studied drug, so this is background on the treatment landscape only. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28685504](https://pubmed.ncbi.nlm.nih.gov/28685504/) | 2017 | Systematic Review | Cochrane Database Syst Rev | Statins for children with familial hypercholesterolemia (general FH, not homozygous-specific) |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Systematic Review | Cochrane Database Syst Rev | Updated Cochrane review of statins in children with FH |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE guidelines for dyslipidemia management and cardiovascular prevention |
| [28416195](https://pubmed.ncbi.nlm.nih.gov/28416195/) | 2017 | Randomized trial | Lancet HIV | Pitavastatin vs pravastatin in HIV-infected adults with dyslipidaemia (not an FH population) |
| [15532136](https://pubmed.ncbi.nlm.nih.gov/15532136/) | 2004 | Commentary | Prescrire Int | Notes simvastatin and pravastatin are reference statins for heterozygous FH, and that statins are not very effective in homozygous FH |
| [12269853](https://pubmed.ncbi.nlm.nih.gov/12269853/) | 2002 | Review | Drugs | Rosuvastatin review; superior to pravastatin in lipid improvement in hypercholesterolaemia |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Review | Clin Ther | Rosuvastatin is indicated in homozygous FH |
| [14727947](https://pubmed.ncbi.nlm.nih.gov/14727947/) | 2003 | Review | Am J Cardiovasc Drugs | Ezetimibe reduces LDL-C via inhibition of intestinal cholesterol absorption |
| [14647533](https://pubmed.ncbi.nlm.nih.gov/14647533/) | 2003 | Review | Cardiovasc Drug Rev | Ezetimibe as a novel cholesterol absorption inhibitor |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Review | Drugs | Atorvastatin pharmacology and therapeutic potential in hyperlipidaemias |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02243824 | PRO-PRAVASTATIN | Not specified | Not specified |
| 02432056 | MAR-PRAVASTATIN | Not specified | Not specified |
| 02330954 | JAMP-PRAVASTATIN | Not specified | Not specified |
| 02389746 | PRAVASTATIN | Not specified | Not specified |
| 02535661 | NRA-PRAVASTATIN | Not specified | Not specified |

These are 5 of 20 valid single-ingredient licences; none are cancelled.

---

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: kidney disease, liver disease, gallbladder disease, thrombocytopenia, peptic ulcer disease, myopathy and other muscle diseases, rhabdomyolysis, gout, hemophilia, anemia, nephrolithiasis, hypercalcemia, sarcoidosis, hyperparathyroidism, and substance abuse/dependence, among others.
- **Drug Interactions**: 100 interactions were recorded. Moderate-level ones include metronidazole, clarithromycin, eluxadoline, naltrexone, pectin, rosuvastatin, simvastatin and tinidazole. Others, such as calcitriol, acarbose, sucralfate, prednisone and vancomycin, are of unknown severity.

Please refer to the package insert for the official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only trial listed tests alirocumab, not pravastatin, and the literature consists mostly of reviews on other lipid-lowering drugs. Mechanistically, statin efficacy is expected to be limited when LDL receptor function is severely impaired. The high TxGNN score reflects a model prediction rather than direct clinical evidence.

**To proceed, the following is needed:**
- Pravastatin-specific clinical data in homozygous FH patients (trials or case series)
- Mechanism of action data for pravastatin
- Health Canada package insert warnings and contraindications (currently missing, which blocks safety screening)
- Review of the 100 recorded drug interactions before any co-prescription

---

**Note on other predictions:** Familial hypercholesterolemia (heterozygous/general) has the strongest support, with pediatric pravastatin evidence including a randomized placebo-controlled study (PMID 8726243), a pharmacokinetic study (PMID 12891228) and a 20-year follow-up (PMID 31618540). It is graded L1 and "Proceed with Guardrails", though it is an extension of the existing lipid-lowering use rather than true repurposing. HIV-associated dyslipidemia (L2) is a research question with small trials. The remaining predictions have little or no supporting evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

