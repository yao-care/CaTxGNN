---
layout: default
title: Fenofibrate
parent: Model Prediction Only (L5)
nav_order: 378
evidence_level: L5
indication_count: 7
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Fenofibrate: From Dyslipidemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Fenofibrate is a marketed lipid-lowering drug that mainly lowers triglycerides and raises HDL-C. The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia (HoFH)**, but the only registered trial found tests a different drug (alirocumab), and the only fenofibrate human data are a single-patient observation within a 1984 cohort. The prediction is a **model output with weak, indirect support**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence records provided. Literature describes fenofibrate as a treatment for dyslipidemia, mainly severe hypertriglyceridemia and mixed dyslipidemia |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 (mechanism/observational signal only, no fenofibrate-specific trial) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the source record. Based on general pharmacology, fenofibrate activates PPARα, which increases lipoprotein lipase activity and fatty-acid oxidation and lowers triglyceride-rich lipoproteins. It also raises HDL-C. This is well established for hypertriglyceridemia and mixed dyslipidemia.

The link to HoFH is weak. HoFH is driven by a near-absent LDL receptor function, so LDL-C is very high. Fenofibrate's LDL-C lowering is modest and depends on LDL receptor function, which is largely absent in HoFH. Small older studies in heterozygous FH show LDL-C reductions of roughly 20–30%. In one 1984 cohort, the single HoFH patient showed the largest fall in total and LDL cholesterol, but one patient cannot support a conclusion. The high model score is therefore not backed by a plausible mechanism. At most, fenofibrate could be an adjunct for accompanying triglyceride abnormalities.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label study of **alirocumab** (PCSK9 inhibitor) in children and adolescents (8–17 years) with HoFH, with LDL-C at Week 12 as the primary endpoint. **It does not involve fenofibrate** and provides no direct evidence for it. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6593751](https://pubmed.ncbi.nlm.nih.gov/6593751/) | 1984 | Cohort | Pharmacol Res Commun | 22 type II hyperlipoproteinemia patients on fenofibrate 300 mg/day for 4–12 months: total cholesterol −22%, LDL-C −24%. One HoFH patient showed the greatest fall in total and LDL cholesterol. |
| [24946816](https://pubmed.ncbi.nlm.nih.gov/24946816/) | 2014 | Review | Intern Med J | Liver transplantation for HoFH when standard drugs and LDL-apheresis are insufficient. Discusses emerging therapies, not fenofibrate efficacy. |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Review | Ann N Y Acad Sci | Drug and surgical treatment of dyslipidemic children. Fenofibrate is listed among agents that reduced lipids in FH. |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Review (guideline) | Endocr Pract | AACE/ACE guidelines for dyslipidemia management and cardiovascular prevention. |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart J | Non-statin lipid-lowering drugs. Fenofibrate's clearest indication is triglycerides >500 mg/dL to reduce pancreatitis risk, with modest cardiovascular benefit. |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | Pharmacokinetic study | Pharmacotherapy | Interaction of lomitapide (approved for HoFH) with lipid-lowering drugs including fenofibrate. |
| [35499807](https://pubmed.ncbi.nlm.nih.gov/35499807/) | 2022 | Review | Curr Atheroscler Rep | Dyslipidemia management in pregnancy. Not specific to HoFH. |
| [26432726](https://pubmed.ncbi.nlm.nih.gov/26432726/) | 2015 | Review | Indian Heart J | LDL-C, statins and PCSK9 inhibitors. Not fenofibrate-specific. |
| [14620392](https://pubmed.ncbi.nlm.nih.gov/14620392/) | 2003 | Review | Pharmacotherapy | Ezetimibe as a cholesterol absorption inhibitor. Not fenofibrate-specific. |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Review | Drugs | Atorvastatin pharmacology and use in hyperlipidaemia. Not fenofibrate-specific. |

Several entries are general lipid-therapy reviews and add little direct support. Only PMID 6593751 contains fenofibrate data on an HoFH patient, and it covers a single patient.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02269082 | LIPIDIL EZ |
| 02390701 | SANDOZ FENOFIBRATE E |
| 02246859 | AA-FENO-SUPER |
| 02246860 | AA-FENO-SUPER |
| 02390698 | SANDOZ FENOFIBRATE E |

Five of 10 authorizations are shown. Dosage form and approved-indication text were not available in the records.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the interaction database query.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not matched by evidence. The only registered trial tests alirocumab, and the fenofibrate data for HoFH amount to one patient in a 1984 cohort. HoFH lacks functional LDL receptors, and the current standard therapies (statins, ezetimibe, PCSK9 inhibitors, lomitapide) are much more effective, so a fenofibrate role would be at most adjunctive.

**To proceed, the following is needed:**
- Fenofibrate-specific clinical data in HoFH (case series or trials), including LDL-C outcomes
- Mechanism-of-action data and analysis of LDL-receptor-independent effects
- Health Canada monograph warnings and contraindications, and the approved indication text for the listed DINs
- A clearer clinical case, for example adjunct use for concurrent hypertriglyceridemia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

