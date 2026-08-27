---
layout: default
title: Lovastatin
parent: 僅模型預測 (L5)
nav_order: 401
evidence_level: L5
indication_count: 6
---

# Lovastatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Lovastatin: From Hypercholesterolemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Lovastatin is a first-generation HMG-CoA reductase inhibitor (statin) originally used to treat hypercholesterolemia/dyslipidemia.
The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**,
with **3 clinical trials** and **19 publications** currently identified, though the evidence base is largely older cohort studies and case reports rather than lovastatin-specific randomized trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercholesterolemia / dyslipidemia (as an HMG-CoA reductase inhibitor) — Canada-specific label indication text is unavailable because the product is not currently marketed |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on known pharmacological information, lovastatin is a first-generation HMG-CoA reductase inhibitor that lowers LDL cholesterol by blocking hepatic cholesterol biosynthesis, which in turn upregulates hepatic LDL receptor expression and increases LDL-C clearance from plasma. This mechanism has been proven effective in common (heterozygous) hypercholesterolemia, and on the surface it appears mechanistically applicable to Homozygous Familial Hypercholesterolemia (HoFH), which is caused by biallelic LDL receptor gene mutations.

However, the repurposing rationale for HoFH carries an important caveat: because HoFH patients have severely reduced or completely absent LDL receptor function, and lovastatin's cholesterol-lowering effect depends on compensatory *upregulation* of that same receptor, patients with a **receptor-negative** genotype are expected to derive limited benefit, while patients with a **receptor-defective** genotype (retaining some residual receptor activity) may show a partial response. In other words, the mechanistic link exists but is highly genotype-dependent rather than uniformly effective — this is directly reflected in the literature (e.g., PMID 3397806 found no reduction in LDL-C or LDL turnover in receptor-negative HoFH children on lovastatin).

It is also worth noting that TxGNN's second-ranked prediction for this drug, hyperlipoproteinemia (Type IIa/IIb), is a well-established, already-approved statin indication with substantially stronger direct evidence (Level L1, including a Phase 4 lovastatin/niacin RCT). By comparison, the HoFH signal reviewed here is a genuinely novel, higher-risk repurposing hypothesis rather than a straightforward extension of existing statin use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Completed | 44 | Long-term (24-month) open-label safety/tolerability of ezetimibe added to atorvastatin or simvastatin in HoFH. Not a lovastatin trial; statin-class background only. |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Parent efficacy/safety study of ezetimibe co-administered with atorvastatin or simvastatin in HoFH. Not a lovastatin trial. |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Efficacy/safety of alirocumab (PCSK9 inhibitor) in children/adolescents with HoFH. Different drug class; indication-level overlap only, not lovastatin-specific. |

**Note:** None of the identified registered trials directly test lovastatin in HoFH — all three involve other lipid-lowering agents (ezetimibe, alirocumab) studied in the same disease population.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3397806](https://pubmed.ncbi.nlm.nih.gov/3397806/) | 1988 | Cohort (small clinical study) | The Journal of Pediatrics | Lovastatin (2 mg/kg/day) produced no reduction in LDL-C levels or LDL turnover in 3 children with receptor-negative HoFH — direct evidence that efficacy depends on residual LDL receptor function. |
| [1785747](https://pubmed.ncbi.nlm.nih.gov/1785747/) | 1991 | Cohort (LDL receptor correlation) | Anales Españoles de Pediatría | Lovastatin combined with probucol/cholestyramine reduced total cholesterol by ~41.7% in two HoFH patients characterized by LDL receptor analysis. |
| [3534334](https://pubmed.ncbi.nlm.nih.gov/3534334/) | 1986 | Case Report | JAMA | A child with HoFH achieved normal cholesterol levels on lovastatin after liver transplantation restored ~60% of LDL receptor activity, suggesting lovastatin only becomes effective once some receptor function is present. |
| [2252289](https://pubmed.ncbi.nlm.nih.gov/2252289/) | 1990 | Case Report | Anales Españoles de Pediatría | HoFH patient with residual (receptor-defective) activity responded to combined cholestyramine + lovastatin therapy. |
| [2209665](https://pubmed.ncbi.nlm.nih.gov/2209665/) | 1990 | Case Report | European Journal of Pediatrics | 7-year-old girl with HoFH treated with LDL apheresis (HELP) with and without lovastatin; long-term treatment was well tolerated with regression of xanthomata. |
| [8637439](https://pubmed.ncbi.nlm.nih.gov/8637439/) | 1996 | Case Report | Metabolism: Clinical and Experimental | In a girl with sitosterolemia plus heterozygous FH, lovastatin and cholestyramine had opposing effects on plasma sterol levels, illustrating variable/complex statin response in receptor-related lipid disorders. |
| [29284604](https://pubmed.ncbi.nlm.nih.gov/29284604/) | 2018 | Case Series (genotype-phenotype) | Arteriosclerosis, Thrombosis, and Vascular Biology | HoFH patients with identical LDLR mutations show variable receptor expression, helping explain heterogeneous responses to statins and PCSK9 inhibitors (contextual, not lovastatin-specific). |
| [12034651](https://pubmed.ncbi.nlm.nih.gov/12034651/) | 2002 | RCT (statin-class) | Circulation | Multicenter double-blind RCT (n=50) of ezetimibe plus atorvastatin/simvastatin in HoFH; supports statin-class background efficacy but not lovastatin directly. |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Review | Clinical Therapeutics | Review of rosuvastatin noting HoFH as an approved statin-class indication, supporting the general statin-HoFH mechanistic rationale. |
| [14727947](https://pubmed.ncbi.nlm.nih.gov/14727947/) | 2003 | Review | American Journal of Cardiovascular Drugs | Review of ezetimibe, a non-statin cholesterol-absorption inhibitor used as HoFH adjunct therapy (contextual background only). |

---

## Canada Market Information

Lovastatin is not currently marketed in Canada — no Drug Identification Numbers (DINs) are on record (0 licenses), so no product/dosage-form/indication table can be produced at this time.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** A Health Canada label / warnings-and-contraindications data gap has been flagged as **Blocking** (DG001) — this must be resolved before any formal safety pre-assessment (S1) can proceed for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A Blocking-severity data gap (DG001: no Health Canada label warnings/contraindications) currently prevents this candidate from entering the S1 safety pre-assessment stage, regardless of efficacy signal.
- The HoFH efficacy evidence itself is Level L3 (older cohort studies and case reports, no lovastatin-specific completed RCT) and shows genotype-dependent effect — patients with receptor-negative HoFH appear largely unresponsive, limiting the population that could realistically benefit.

**To proceed, the following is needed:**
- Health Canada product monograph / label warnings and contraindications (resolves Blocking gap DG001)
- Confirmed mechanism of action data via DrugBank API (resolves High-severity gap DG002)
- Genotype-stratified clinical data distinguishing receptor-negative vs. receptor-defective HoFH patients to identify which subgroup, if any, could benefit
- A regulatory pathway assessment given lovastatin's current non-marketed status in Canada (0 DINs)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

