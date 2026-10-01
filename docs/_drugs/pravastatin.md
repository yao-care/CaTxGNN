---
layout: default
title: Pravastatin
parent: Moderate Evidence (L3-L4)
nav_order: 756
evidence_level: L4
indication_count: 9
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

# Pravastatin: From Lipid Lowering to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Pravastatin is a statin (HMG-CoA reductase inhibitor) marketed in Canada for lipid lowering.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia (HoFH)**.
The supporting evidence is weak: **1 registered trial** (it studies a different drug) and **13 publications**, none of which tests pravastatin in HoFH.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Lipid lowering (statin). The Canadian licence records supplied contain no indication text. |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the supplied record. Pravastatin is a statin that inhibits HMG-CoA reductase, which reduces hepatic cholesterol synthesis. This upregulates hepatic LDL receptors and lowers LDL-C.

HoFH is a severe inherited form of hypercholesterolemia. It is usually caused by null or defective LDL receptor (LDLR) alleles on both copies of the gene. That is the main reason the prediction is questionable: the statin mechanism depends on upregulating LDL receptors, and in HoFH that pathway is largely unavailable, so the expected response is small.

The high TxGNN score most likely reflects the general pravastatin–hypercholesterolemia association in the knowledge graph rather than evidence in the homozygous form. No supplied evidence tests pravastatin in HoFH.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label study of alirocumab (a PCSK9 inhibitor) in children and adolescents aged 8–17 with HoFH. The primary endpoint is LDL-C change at Week 12. Pravastatin is not studied, so this gives no direct evidence for it. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28685504](https://pubmed.ncbi.nlm.nih.gov/28685504/) | 2017 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Statins for children with familial hypercholesterolemia. It covers FH broadly, and the abstract notes that homozygous patients have severe disease. |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Update of the review above on statins in children with FH. |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE guidelines for managing dyslipidemia and preventing cardiovascular disease. |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Review | Clin Ther | Rosuvastatin in hyperlipidemia. HoFH is among its indications, but the drug is rosuvastatin, not pravastatin. |
| [12269853](https://pubmed.ncbi.nlm.nih.gov/12269853/) | 2002 | Review | Drugs | Rosuvastatin review. In trials of 6–52 weeks it was superior to pravastatin, among other statins, in improving lipid profiles in hypercholesterolaemia. |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Review | Drugs | Atorvastatin pharmacology and therapeutic potential in hyperlipidaemias. Not specific to pravastatin or HoFH. |
| [14727947](https://pubmed.ncbi.nlm.nih.gov/14727947/) | 2003 | Review | Am J Cardiovasc Drugs | Ezetimibe, a cholesterol absorption inhibitor, as a non-statin lipid-lowering option. |
| [31358055](https://pubmed.ncbi.nlm.nih.gov/31358055/) | 2019 | Preclinical (iPSC-derived hepatocyte model) | Stem Cell Res Ther | LDLR-deficient hepatocytes derived from iPSCs, used to model FH and test CRISPR/Cas genetic correction. A disease model with no pravastatin data. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02243824 | PRO-PRAVASTATIN |
| 02432056 | MAR-PRAVASTATIN |
| 02330954 | JAMP-PRAVASTATIN |
| 02389746 | PRAVASTATIN |
| 02535661 | NRA-PRAVASTATIN |

Dosage forms and approved-indication text were not available for these licences. They are 5 of the 20 authorizations.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No supplied trial or publication tests pravastatin in HoFH, and the only registered trial studies a different drug. Mechanistically, HoFH typically lacks functional LDL receptors, so a statin's main effect is expected to be limited.

**To proceed, the following is needed:**
- Direct clinical data on pravastatin in HoFH, for example LDL-C response by LDLR genotype, in patients and in children
- The Health Canada package insert, for approved indications, warnings and contraindications
- Mechanism of action data from DrugBank

**Note on other predictions in this pack:** two other predicted indications have stronger evidence than HoFH.
- **Familial hypercholesterolemia** has an L1 rating and "Proceed with Guardrails". The rating rests on Cochrane-level literature rather than the supplied trials. Pravastatin is an established lipid-lowering agent here, so this is not true repurposing.
- **HIV-associated dyslipidemia** has an L2 rating and "Proceed with Guardrails". Any recommendation should be limited to dyslipidemia in people with HIV, not HIV infection itself.

*This report is for research reference only and does not constitute medical advice. Predicted indications require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

