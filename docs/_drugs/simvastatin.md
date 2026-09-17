---
layout: default
title: Simvastatin
parent: High Evidence (L1-L2)
nav_order: 718
evidence_level: L1
indication_count: 8
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

Using no additional skill — this is a direct content-generation task fully specified by the prompt template; proceeding straight to the report.

---

# Simvastatin: From Established Statin Use to Familial Hypercholesterolemia (Confirmatory Indication)

## One-Sentence Summary

> Simvastatin is a well-established HMG-CoA reductase inhibitor used broadly for hypercholesterolemia and cardiovascular risk reduction, though the Canadian regulatory record in this evidence pack contains no license or approved-indication text (the drug is currently **not marketed** in Canada under this dataset).
> The TxGNN model's top-ranked candidate, **Familial Hypercholesterolemia**, is supported by **20 clinical trials** and **20 publications**, but the evidence itself indicates this is a **confirmed, textbook-level indication** for statins rather than a novel repurposing hypothesis.
> A critical **blocking data gap** exists — no TFDA/product-label safety data (warnings, contraindications) is available — so this candidate cannot yet proceed to safety review.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in current dataset (no Canadian license record available; see Market Status) |
| Predicted New Indication | Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L1 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | **Hold** (blocked by missing safety data) |

---

## Why is This Prediction Reasonable?

Currently, detailed original mechanism-of-action data from the regulatory record is not available (`original_moa: [Data Gap]`). However, the evidence pack's repurposing rationale supplies the pharmacological basis directly: **Simvastatin is an HMG-CoA reductase inhibitor** that suppresses endogenous cholesterol synthesis and upregulates hepatic LDL-receptor expression — the exact pathway defective or dysregulated in Familial Hypercholesterolemia (FH), particularly the heterozygous form.

Importantly, the evidence pack itself flags this as **not a novel repurposing signal**: the mechanistic rationale explicitly states that statin-mediated LDL-receptor upregulation is "a textbook-level, already-established indication rather than a novel repurposing hypothesis" for FH. In other words, TxGNN's top prediction is essentially re-discovering simvastatin's core, long-standing clinical role in hypercholesterolemia management (including combination use with ezetimibe, e.g., in VYTORIN/Inegy), rather than identifying a genuinely new therapeutic use.

For context, three lower-ranked candidates in this pack (brain stem infarction, HIV infectious disease, and several ultra-rare genetic disorders) were also evaluated but carry weak or misleading mechanistic support — in the case of HIV, existing evidence concerns drug-drug interactions between simvastatin and antiretrovirals (CYP3A4-mediated), not antiviral efficacy, and the model likely mistook comorbidity co-occurrence for a therapeutic signal. These were scored L4–L5 and marked **Hold** in the source data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01617655](https://clinicaltrials.gov/study/NCT01617655) | Phase 3 | Completed | 107 | RCT of alirocumab add-on in heFH patients with LDL-C ≥160 mg/dL on background lipid-modifying therapy (incl. simvastatin) |
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | ENHANCE trial: simvastatin ± ezetimibe on carotid atherosclerosis progression in heFH |
| [NCT01070966](https://clinicaltrials.gov/study/NCT01070966) | N/A (post-marketing) | Completed | 2089 | Re-examination/post-marketing safety and efficacy survey of VYTORIN (ezetimibe/simvastatin) |
| [NCT00465088](https://clinicaltrials.gov/study/NCT00465088) | Phase 3 | Completed | 199 | SUPREME: niacin ER + simvastatin vs. atorvastatin on HDL-C in hyperlipidemia/mixed dyslipidemia |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Completed | 44 | Long-term safety/tolerability of ezetimibe added to atorvastatin or simvastatin in homozygous FH |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Efficacy/safety of ezetimibe + atorvastatin or simvastatin in homozygous FH |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Phase 3 | Completed | 248 | Ezetimibe + simvastatin in adolescents with heterozygous FH |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3b | Completed | 442 | Renal effects of rosuvastatin vs. simvastatin in Fredrickson Type IIa/IIb dyslipidemia incl. heFH |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Phase 3 | Completed | 249 | RCT of alirocumab in heFH not adequately controlled on lipid-modifying therapy |
| [NCT01507831](https://clinicaltrials.gov/study/NCT01507831) | Phase 3 | Completed | 2341 | Long-term safety/tolerability of alirocumab in high-CV-risk hypercholesterolemia patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | RCT | N Engl J Med | ENHANCE: simvastatin with/without ezetimibe in FH — effect on atherosclerosis progression |
| [41824552](https://pubmed.ncbi.nlm.nih.gov/41824552/) | 2026 | Guideline | Circulation | ACC/AHA/multi-society dyslipidemia management guideline (replaces 2018 cholesterol guideline) |
| [41824590](https://pubmed.ncbi.nlm.nih.gov/41824590/) | 2026 | Guideline | J Am Coll Cardiol | Companion publication of the 2026 ACC/AHA dyslipidemia guideline |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE guideline for dyslipidemia management and CVD prevention |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Cochrane Review | Cochrane Database Syst Rev | Systematic review of statins (incl. simvastatin) for children with FH |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Review | Expert Opin Drug Saf | Benefits and risks assessment of simvastatin in FH |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Review | Drug Saf | Benefits and risks of simvastatin in patients with FH |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | Observational | J Am Coll Cardiol | Statins in FH: impact on coronary artery disease and all-cause mortality |
| [35629051](https://pubmed.ncbi.nlm.nih.gov/35629051/) | 2022 | Cross-sectional | J Clin Med | Cellular immunity parameters in children with FH treated with simvastatin |
| [35361995](https://pubmed.ncbi.nlm.nih.gov/35361995/) | 2022 | Genetic/Pharmacogenomic | Pharmacogenomics J | Combined FH and statin pharmacogenomic testing strategy |

---

## Canada Market Information

Simvastatin currently has **no market authorization record** in this dataset (0 DINs, market status: Not Marketed). No license table is available to display.

---

## Safety Considerations

Please refer to the package insert for safety information. Both `key_warnings` and `contraindications` are marked as data gaps, and no drug-drug interaction records were found in this evidence pack (`ddi.query_status: not_found`).

**⚠ Blocking data gap (DG001):** TFDA-equivalent product label warnings/contraindications are missing, which per protocol **prevents this candidate from entering the S1 safety pre-assessment stage**. This must be resolved before any clinical or regulatory next step.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Efficacy evidence for the top-ranked indication (Familial Hypercholesterolemia) is strong (L1, ≥2 completed Phase 3 RCTs), but this reflects an **already-established statin indication**, not a novel repurposing opportunity — limiting the strategic value of pursuing it as a "new use" candidate.
- A **Blocking-severity safety data gap** (DG001) means the candidate cannot legitimately proceed past initial safety triage regardless of efficacy strength.
- The drug is not currently marketed in Canada under this dataset (0 DINs), so there is no existing local label to anchor a guardrail-based launch.

**To proceed, the following is needed:**
- TFDA/product-label warnings and contraindications (DG001, Blocking) — download and parse official label PDF
- Mechanism-of-action confirmation from DrugBank API (DG002, High)
- Clarification of Canadian regulatory/market status for simvastatin (verify whether "not marketed" reflects this specific evidence pack's scope or an actual withdrawal)
- If pursuing FH as a positioning, reframe as **label-consistent use confirmation** rather than a repurposing candidate; consider whether lower-ranked, higher-novelty candidates (e.g., disease areas with L3–L4 evidence and genuine mechanistic novelty) better fit a repurposing program's goals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

