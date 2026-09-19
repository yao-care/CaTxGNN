---
layout: default
title: Hexaminolevulinate
parent: Moderate Evidence (L3-L4)
nav_order: 380
evidence_level: L3
indication_count: 10
---

# Hexaminolevulinate
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Hexaminolevulinate: From Fluorescence Diagnosis of Bladder Cancer to Detection of Colonic Neoplasm

> **Candidate Selection Explanation**: This Evidence Pack presents 10 predicted indications for Hexaminolevulinate (HAL) by TxGNN, but only **Colonic Neoplasm** has substantial clinical trial evidence (Decision Stage S1). Although the highest-ranked bronchitis (score 0.9906) has the highest score, the model's own mechanistic reasoning has been clearly noted as "false positive caused by TxGNN graph noise or indirect node connections" and lacks any clinical or literature evidence, making further investigation not recommended. Therefore, this report focuses on Colonic Neoplasm as the primary assessment target, with the remaining 8 low-evidence candidates summarized in the appendix table at the end for reference.

## One-Sentence Summary

> Hexaminolevulinate (HAL) is a fluorescence contrast agent whose approved use is for photodynamic diagnosis (PDD) via cystoscopy to detect bladder cancer lesions.
> The TxGNN model predicts it may be applicable to fluorescent endoscopic detection of **colonic neoplasms**.
> Currently **3 related clinical trials** (1 completed with 38 enrolled subjects) support this direction, however, there are no supporting literature reports yet.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original indication | Fluorescence imaging diagnosis of bladder cancer (from mechanistic description in evidence; formal package insert/indication record pending, see DG002) |
| Predicted new indication | Colonic Neoplasm |
| TxGNN prediction score | 98.64% |
| Evidence level | L3 |
| Taiwan market status | Not marketed |
| Number of licenses | 0 |
| Recommended decision | Hold |

---

## Why Is This Prediction Reasonable?

DrugBank currently does not provide complete mechanism of action (MOA) data (data gap DG002, severity High). According to the mechanistic description provided in the repurposing_rationale of the evidence package: HAL is a precursor of protoporphyrin IX (PpIX), which after administration selectively accumulates in rapidly proliferating/neoplastic tissues, and upon blue light excitation produces red fluorescence, thereby assisting in endoscopic lesion detection—this is precisely the mechanistic principle of its approved cystoscopic photodynamic diagnosis (PDD).

Although colonic neoplasms and bladder cancer belong to different organ systems, they share common pathophysiological characteristics: both are epithelial rapidly proliferating/neoplastic tissues that in theory should have the same fluorescence imaging properties of selective PpIX accumulation. Therefore, extending HAL from "cystoscopic fluorescence diagnosis" to "colonoscopic fluorescence diagnosis" is a reasonable extrapolation mechanistically of "same diagnostic platform, different detection sites," rather than a hypothesis of entirely new pharmacological mechanism, and the mechanistic relevance is relatively strong.

It is worth noting that this is an extension of **diagnostic application** rather than drug repurposing for therapeutic indication—HAL itself is not an antitumor therapeutic drug. Its potential new indication value lies in "assisting detection" rather than "treating" colonic neoplasms, and this distinction needs to be particularly noted in subsequent safety and clinical positioning assessment.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|--------------|-------|--------|------------|-------------|
| [NCT00285701](https://clinicaltrials.gov/study/NCT00285701) | Phase 1/2 | Completed | 38 | Local/oral administration of HAL prior to colonoscopy for sensitization; blue light excitation produces red fluorescence in polyps and tumors, improving lesion detection rate; also tested different doses to identify optimal visualization conditions and tolerability |
| [NCT01344902](https://clinicaltrials.gov/study/NCT01344902) | Phase 1/2 | Terminated | 13 | Open-label dose-escalation study evaluating oral HAL fluorescence technology for detection in patients with suspected/high-risk colonic neoplasms; terminated after enrolling only 13 subjects, limiting result interpretation |
| [NCT03272659](https://clinicaltrials.gov/study/NCT03272659) | Phase 2 | Withdrawn (enrollment failed, 0 enrolled) | 0 | Originally planned to evaluate the correlation between pathology of colorectal cancer surgical specimens after neoadjuvant chemoradiation and photodynamic fluorescence (HAL rectal instillation for sensitization); withdrawn due to enrollment failure with no substantive data generated |

---

## Literature Evidence

Currently no relevant literature available for reference.

---

## Taiwan Market Information

Hexaminolevulinate is currently **not marketed in Taiwan**, with no license issuance records (total_licenses = 0).

---

## Safety Considerations

Please refer to the drug package insert for safety information.

*(Data gap DG001: Health Canada package insert warnings/contraindications not yet obtained, severity Blocking, this is an essential item to be completed before entering S1 initial safety assessment.)*

---

## Conclusions and Next Steps

**Recommended Decision: Hold**

**Rationale:**
Existing evidence is only at Phase 1/2 early proof-of-concept level (1 completed, 1 terminated due to insufficient enrollment, 1 withdrawn due to enrollment failure), with no Phase 3 randomized controlled trial or published literature to support it; meanwhile, critical safety package insert data (DG001, Blocking) and formal mechanism of action record (DG002, High) are both data gaps, insufficient to support entry into the next phase of assessment.

**To proceed further, the following gaps need to be filled:**
- Health Canada package insert warnings/contraindications data (DG001, Blocking, must download and parse official package insert PDF)
- Formal mechanism of action (MOA) record verified through DrugBank API (DG002)
- Larger-scale, complete enrollment Phase 2/3 clinical trials for colonic neoplasm detection
- Independent peer-reviewed literature to support existing clinical trial findings
- Endoscopic administration routes (rectal instillation/oral) and compatibility assessment with current colonoscopy equipment

---

## Appendix Table: Other TxGNN Predicted Candidates (Not to Proceed at This Time)

The following 8 candidates all lack clinical trial or literature evidence support (Decision Stage S0), and the model's mechanistic reasoning also determines weak relevance or graph noise, making further investigation not recommended at this time:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Primary Judgment Rationale |
|------|---------|-------------|----------------|----------------|---------------------------|
| 1 | Bronchitis | 99.06% | L5 | Hold | Completely unrelated to HAL fluorescence imaging mechanism, likely a false positive |
| 3 | Severe nonproliferative diabetic retinopathy | 98.60% | L5 | Hold | Disease pathophysiology (microvascular disease) has no direct association with neoplastic tissue fluorescence detection |
| 4 | Cecum villous adenoma | 98.43% | L4 | Hold | In same spectrum as colonic neoplasm, can only be indirectly inferred, no direct evidence |
| 5 | Rectosigmoid junction neoplasm | 98.43% | L4 | Hold | Same as above, only inference possible, no direct trial or literature |
| 6 | Cecum neuroendocrine tumor G1 | 98.43% | L5 | Hold | Neuroendocrine tumors have different proliferation characteristics, mechanistic extension is speculative |
| 7 | Colonic lymphangioma | 98.43% | L5 | Hold | Non-epithelial neoplastic lesion, weak mechanistic relevance |
| 8 | Lipoma of colon | 98.43% | L5 | Hold | Benign tumor of mesenchymal origin, mechanism does not match |
| 9 | Cecal disease | 98.42% | L5 | Hold | Disease definition too broad to establish clear mechanistic association |
| 10 | Cavernous hemangioma of colon | 98.42% | L5 | Hold | Vascular malformation lesion, non-proliferative tissue, mechanism does not match |

---

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.*

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

