---
layout: default
title: Lomitapide
parent: 僅模型預測 (L5)
nav_order: 395
evidence_level: L5
indication_count: 10
---

# Lomitapide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

Using the Evidence Pack provided, I selected the predicted indication with actual supporting evidence (rank 9, "hyperlipoproteinemia" — L1/S3/Proceed with Guardrails) rather than the TxGNN score-ranked #1 entry, because the evidence pack's own `repurposing_rationale` flags ranks 1–8 and 10 (all rare platelet/thrombocytopenia disorders) as likely **model embedding artifacts** — each has a 99%+ TxGNN score but **zero clinical trials and zero literature**, and several rationale fields explicitly state this pattern indicates KG-embedding clustering noise rather than a real signal. Rank 9 is the only candidate with substantive evidence (12 trials, 19 publications), so it is the only one that can actually be evaluated. This substitution is noted below for transparency.

---

# Lomitapide: From an Undocumented Original Indication to Hyperlipoproteinemia

## One-Sentence Summary

> Lomitapide's original indication could not be extracted from this Evidence Pack (no Canadian license records, no structured original-indication data), though the collected literature consistently describes it as a microsomal triglyceride transfer protein (MTP) inhibitor already used for **Homozygous Familial Hypercholesterolemia (HoFH)**. The TxGNN model — and independently, the collected real-world evidence — converge on **Hyperlipoproteinemia** as the most substantiated indication, supported by **12 clinical trials** and **19 publications**. Note: nine of the ten TxGNN-predicted indications in this pack (all rare platelet/thrombocytopenia disorders) returned **zero trials and zero literature** and are flagged in the source data itself as likely model artifacts — they are not covered further in this report.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Canadian license records exist for this drug; the collected literature indicates it is used elsewhere for Homozygous Familial Hypercholesterolemia (HoFH) |
| Predicted New Indication | Hyperlipoproteinemia (clinically corresponds to HoFH / familial hypercholesterolemia) |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L1 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not present in this drug's structured fields (`original_moa` is a data gap). However, the evidence collected under this specific prediction describes the mechanism clearly: Lomitapide is a microsomal triglyceride transfer protein (MTP) inhibitor. It blocks the assembly and secretion of ApoB-containing lipoproteins (VLDL and chylomicrons) in the liver and intestine, which directly lowers LDL-cholesterol and overall plasma lipoprotein levels.

This mechanism maps directly onto hyperlipoproteinemia — particularly Homozygous Familial Hypercholesterolemia (Fredrickson type IIa), where LDL-receptor function is severely impaired and patients depend on LDL-receptor-independent pathways to lower LDL-C. Because MTP inhibition works independently of the LDL receptor, it is pharmacologically well-suited to exactly this patient population.

Importantly, the literature in this pack (e.g., PMID 23122768, the original Phase 3 registration trial, and multiple consensus/guideline documents) indicates lomitapide is **already an approved therapy for HoFH internationally**. This means the "predicted new indication" here largely reflects a known, established use rather than a genuinely novel repurposing signal — the TxGNN model has correctly recovered a true drug–disease relationship, but it is not new information. Whether this constitutes a "repurposing opportunity" in Canada therefore depends entirely on confirming current Canadian regulatory status, which this Evidence Pack could not establish (0 DINs, no license records).

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00690443](https://clinicaltrials.gov/study/NCT00690443) | Phase 2 | Completed | 44 | RCT of lomitapide (AEGR-733) + atorvastatin vs. atorvastatin monotherapy in moderate hypercholesterolemia; assessed LDL-C reduction at 4/8 weeks |
| [NCT02173158](https://clinicaltrials.gov/study/NCT02173158) | Phase 3 | Completed | 9 | Single-arm, open-label study of lomitapide in Japanese HoFH patients on concurrent lipid-lowering therapy |
| [NCT00730236](https://clinicaltrials.gov/study/NCT00730236) | Phase 3 | Completed | 29 | Pivotal registration trial of the MTP inhibitor AEGR-733 (lomitapide) in HoFH; long-term LDL-C and safety outcomes |
| [NCT00559962](https://clinicaltrials.gov/study/NCT00559962) | Phase 2 | Completed | 260 | Randomized, double-blind, placebo-controlled trial of low-dose MTP inhibitor on hepatic fat accumulation (MRS-measured) |
| [NCT04681170](https://clinicaltrials.gov/study/NCT04681170) | Phase 3 | Completed | 46 | Single-arm, multicentre study of lomitapide efficacy/long-term safety in pediatric HoFH patients on stable lipid-lowering therapy |
| [NCT01556906](https://clinicaltrials.gov/study/NCT01556906) | Phase 2 | Completed | 6 | Open-label dose-escalation study of MTP inhibitor BMS-201038 (lomitapide) safety/tolerability in HoFH |
| [NCT02765841](https://clinicaltrials.gov/study/NCT02765841) | Phase 3 | Withdrawn | 0 | Planned pediatric HoFH efficacy/safety study; withdrawn with no enrollment |
| [NCT06832371](https://clinicaltrials.gov/study/NCT06832371) | N/A | Active, not recruiting | 73 | Observational study evaluating lomitapide's effect on Major Adverse Cardiovascular Events (MACE) in HoFH |
| [NCT02135705](https://clinicaltrials.gov/study/NCT02135705) | N/A | Recruiting | 300 | LOWER registry — global, multicentre, long-term observational registry of lomitapide safety and effectiveness |
| [NCT00943306](https://clinicaltrials.gov/study/NCT00943306) | Phase 3 | Completed | 19 | Long-term, open-label follow-on study of continued lomitapide safety/efficacy in HoFH |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23122768](https://pubmed.ncbi.nlm.nih.gov/23122768/) | 2013 | Phase 3 Trial | Lancet | Pivotal single-arm, open-label Phase 3 study establishing lomitapide efficacy and safety in adults with HoFH inadequately responsive to existing drugs |
| [39426393](https://pubmed.ncbi.nlm.nih.gov/39426393/) | 2024 | Phase 3 Trial | Lancet Diabetes & Endocrinology | Efficacy-phase results (APH-19) of lomitapide in pediatric HoFH patients on standard-of-care lipid-lowering therapy |
| [37130090](https://pubmed.ncbi.nlm.nih.gov/37130090/) | 2023 | Guideline/Consensus | European Heart Journal | 2023 EAS consensus update on HoFH diagnosis and treatment, including lomitapide's role |
| [40494715](https://pubmed.ncbi.nlm.nih.gov/40494715/) | 2025 | Review (real-world) | Journal of Clinical Lipidology | Over 10 years of long-term efficacy and safety data on lomitapide in HoFH |
| [39751968](https://pubmed.ncbi.nlm.nih.gov/39751968/) | 2025 | Review | Current Atherosclerosis Reports | Review of novel pharmacological therapies, including lomitapide, for lowering LDL-C in HoFH |
| [31741187](https://pubmed.ncbi.nlm.nih.gov/31741187/) | 2019 | Review | Current Atherosclerosis Reports | Mechanistic review of lomitapide (MTP inhibition) and mipomersen (apoB100 synthesis inhibition) |
| [21846156](https://pubmed.ncbi.nlm.nih.gov/21846156/) | 2011 | Review | American Journal of Cardiovascular Drugs | Early drug-development review of lomitapide as an oral MTP inhibitor for familial/primary hypercholesterolemia |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Review | Journal of the American College of Cardiology | Overview of new/emerging LDL-C and ApoB-lowering therapies, including lomitapide |
| [36152419](https://pubmed.ncbi.nlm.nih.gov/36152419/) | 2022 | Review | Atherosclerosis | Explores efficacy/safety of lomitapide in familial chylomicronaemia syndrome (indication-expansion evidence) |
| [24231894](https://pubmed.ncbi.nlm.nih.gov/24231894/) | 2014 | Review | Journal of Cardiovascular Nursing | Review of lomitapide and mipomersen as novel lipid-lowering agents for familial hypercholesterolemia |

*Canada market information is omitted — no license/DIN records exist for this drug in the dataset provided.*

## Safety Considerations

Please refer to the package insert for safety information.

*Note: this Evidence Pack flags a **Blocking**-severity data gap (DG001 — TFDA/label warnings and contraindications not yet retrieved) that currently prevents any S1 safety pre-screen. This must be resolved before further evaluation, independent of the strength of the efficacy evidence above.*

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The efficacy evidence for lomitapide in hyperlipoproteinemia/HoFH is strong (L1: multiple completed Phase 3 studies plus a 2023 consensus guideline), but two blocking gaps prevent a full go decision: (1) no confirmed Canadian regulatory/market status (0 DINs, market status "Not Marketed"), and (2) no safety/label data (warnings, contraindications, interactions) has been retrieved. Separately, note that this indication likely represents lomitapide's already-known/approved use rather than a genuinely new repurposing signal — the other nine TxGNN-predicted indications in this pack (rare platelet disorders) returned no supporting evidence at all and are assessed as probable model artifacts, not viable candidates.

**To proceed, the following is needed:**
- Retrieve TFDA/product-label warnings, contraindications, and drug-interaction data (DG001, Blocking)
- Retrieve confirmed mechanism-of-action documentation from DrugBank (DG002, High)
- Confirm current Canadian regulatory/marketing status for lomitapide (currently 0 licenses on record)
- Clarify whether "hyperlipoproteinemia" here should be treated as a repurposing candidate or as confirmation of an existing approved indication, since this materially changes the recommended decision pathway
- Do not advance the remaining nine predicted indications (thrombocytopenia/platelet disorders) without independent mechanistic justification — current evidence in this pack does not support them
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

