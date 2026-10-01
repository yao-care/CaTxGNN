---
layout: default
title: Lovastatin
parent: Model Prediction Only (L5)
nav_order: 558
evidence_level: L5
indication_count: 6
---

# Lovastatin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Lovastatin: From Statin Lipid-Lowering Therapy to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Lovastatin is a statin (an HMG-CoA reductase inhibitor) used to lower cholesterol, and it is marketed in Canada. The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia (HoFH)** with a very high score. However, none of the **3 retrieved clinical trials** tests lovastatin, and the **19 publications** are mostly small or mixed case-level reports.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the provided licence data (indication text is empty) |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 (small clinical studies and case reports only; no completed lovastatin-specific Phase 3 RCT) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacology, lovastatin inhibits HMG-CoA reductase, which lowers cholesterol synthesis in the liver. This upregulates hepatic LDL receptors and increases LDL clearance. HoFH is a severe inherited condition of extremely high LDL cholesterol, so a cholesterol-lowering statin is a natural candidate.

The mechanism has an important limit. Statins depend on residual LDL receptor (LDLR) function, and HoFH patients carry two faulty LDLR alleles. The effect is therefore expected to be weak or absent in receptor-negative patients and may be partial in receptor-defective ones. The lovastatin-specific evidence reflects this. One study of three receptor-negative children found no LDL-cholesterol reduction on lovastatin. Other reports describe lovastatin only as part of combination regimens.

The high TxGNN score is a graph-based prediction. It is not backed by lovastatin-specific controlled data.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Completed | 44 | Long-term open-label safety of ezetimibe added to atorvastatin or simvastatin in HoFH (not lovastatin) |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Efficacy and safety of ezetimibe added to atorvastatin or simvastatin in HoFH (not lovastatin) |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label alirocumab (PCSK9 inhibitor) in children and adolescents with HoFH (not lovastatin) |

None of these trials studies lovastatin. They only show that HoFH usually needs combination or add-on therapy.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12034651](https://pubmed.ncbi.nlm.nih.gov/12034651/) | 2002 | RCT (other drug class) | Circulation | Ezetimibe added to atorvastatin or simvastatin in 50 HoFH patients (not lovastatin) |
| [3397806](https://pubmed.ncbi.nlm.nih.gov/3397806/) | 1988 | Clinical study | J Pediatr | Three children with receptor-negative HoFH: lovastatin 2 mg/kg/day gave no LDL-cholesterol decrease |
| [1785747](https://pubmed.ncbi.nlm.nih.gov/1785747/) | 1991 | Clinical study | An Esp Pediatr | Two HoFH patients: lovastatin combined with probucol and cholestyramine, with LDL receptor analysis |
| [2209665](https://pubmed.ncbi.nlm.nih.gov/2209665/) | 1990 | Case report | Eur J Pediatr | A 7-year-old girl with HoFH: LDL apheresis (HELP) with and without lovastatin |
| [3534334](https://pubmed.ncbi.nlm.nih.gov/3534334/) | 1986 | Case report | JAMA | A child with HoFH after liver transplantation: lovastatin brought cholesterol to normal levels |
| [2252289](https://pubmed.ncbi.nlm.nih.gov/2252289/) | 1990 | Case report | An Esp Pediatr | A receptor-defective HoFH patient treated with cholestyramine plus lovastatin |
| [12091863](https://pubmed.ncbi.nlm.nih.gov/12091863/) | 2002 | Case report | J Pediatr | 15 years of H.E.L.P. apheresis plus statins in a young woman with HoFH: 85% LDL-cholesterol reduction and xanthoma regression |
| [29284604](https://pubmed.ncbi.nlm.nih.gov/29284604/) | 2018 | Cohort/Mechanistic | Arterioscler Thromb Vasc Biol | Variable LDLR expression explains variable evolocumab response in HoFH |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Review | Clin Ther | Rosuvastatin review, including its HoFH indication (not lovastatin) |
| [7229037](https://pubmed.ncbi.nlm.nih.gov/7229037/) | 1981 | Preclinical | J Clin Invest | Compactin (an early statin) effects on sterol synthesis in HoFH patient fibroblasts |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2220180 | LOVASTATIN |
| 2220172 | LOVASTATIN |

Dosage form and approved indication text were not provided for these authorizations.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not supported by lovastatin-specific controlled evidence. The retrieved trials test other agents, and the lovastatin data are limited to small studies and case reports. The mechanism is expected to fail in receptor-negative HoFH, and one small pediatric study showed no effect.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data (for example from DrugBank)
- Confirmation of the current approved indication and dosage forms for the two DINs
- Lovastatin-specific data stratified by LDLR genotype (receptor-negative vs receptor-defective), or a case for why HoFH should not simply be managed with other established therapies
- Note that the same evidence pack shows stronger support (L1) for lovastatin in heterozygous familial hypercholesterolemia. That is a more promising direction to evaluate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

