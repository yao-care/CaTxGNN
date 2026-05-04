---
layout: default
title: Celecoxib
parent: 僅模型預測 (L5)
nav_order: 144
evidence_level: L5
indication_count: 10
---

# Celecoxib
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

# Celecoxib: From Osteoarthritis & Rheumatoid Arthritis to Inflammatory Spondylopathy

## One-Sentence Summary

Celecoxib (Celebrex®) is a selective COX-2 inhibitor globally approved for osteoarthritis, rheumatoid arthritis, and acute pain, though it currently holds no Taiwan FDA marketing license.
The TxGNN model predicts it may be effective for **Inflammatory Spondylopathy** (encompassing ankylosing spondylitis and axial spondyloarthritis), with the highest evidence level (L1) among all ranked predictions — supported by **19 registered clinical trials**, including multiple completed Phase 3 and Phase 4 randomized controlled trials directly evaluating celecoxib in this indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Osteoarthritis, rheumatoid arthritis, acute pain (approved in multiple international jurisdictions; no Taiwan FDA license on record) |
| Predicted New Indication | Inflammatory Spondylopathy (Ankylosing Spondylitis / Axial Spondyloarthritis) |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L1 |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Currently, formal mechanism of action data is not available in this Evidence Pack (Data Gap DG002). Based on well-established pharmacology, celecoxib is a diarylheterocyclic compound that selectively inhibits cyclooxygenase-2 (COX-2) — the inducible isoform of the enzyme responsible for synthesizing pro-inflammatory prostaglandins, particularly PGE₂. Unlike non-selective NSAIDs, it spares COX-1 (the constitutive "housekeeping" isoform), which largely accounts for its superior gastrointestinal tolerability profile. This selectivity is the mechanistic cornerstone linking celecoxib to inflammatory musculoskeletal disease broadly.

Inflammatory spondylopathy — including ankylosing spondylitis (AS) and non-radiographic axial spondyloarthritis (nr-axSpA) — is driven by chronic, immune-mediated axial skeletal inflammation. Downstream of IL-17 and TNF signaling, COX-2 is markedly upregulated in inflamed spinal and sacroiliac joint tissues, resulting in excess PGE₂ release that mediates spinal pain, morning stiffness, and enthesitis. Sustained inhibition of this pathway by celecoxib not only controls symptoms but has been associated in longitudinal studies with retardation of radiographic spinal progression — a finding that elevates celecoxib from a simple analgesic to a potentially disease-modifying agent in this context.

The alignment between the prediction and existing clinical reality is striking: celecoxib is already an approved therapy for ankylosing spondylitis in the United States, the European Union, Japan, and several other major regulatory jurisdictions. Multiple completed Phase 3 RCTs directly comparing celecoxib to standard-of-care diclofenac in AS patients, as well as Phase 4 trials combining celecoxib with biologics, constitute an unusually robust L1 evidentiary base. This makes inflammatory spondylopathy the most actionable and best-supported repurposing target among all TxGNN predictions for celecoxib in this analysis.

---

## Clinical Trial Evidence

19 trials were identified for inflammatory spondylopathy. The 10 most relevant are presented below, prioritized by grade and study design:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00762463](https://clinicaltrials.gov/study/NCT00762463) | Phase 3 | Completed | 240 | Randomized double-blind RCT in Chinese AS patients: celecoxib 200 mg QD vs. diclofenac 75 mg SR QD over 6 weeks with a 6-week extension at celecoxib 400 mg QD. Core pivotal evidence directly supporting AS indication. |
| [NCT00648141](https://clinicaltrials.gov/study/NCT00648141) | Phase 3 | Completed | 458 | 12-week double-blind Phase 3 RCT comparing celecoxib 200 mg QD, celecoxib 200 mg BID, and diclofenac BID for AS symptom control and safety; the largest direct comparison study in this dataset. |
| [NCT02528201](https://clinicaltrials.gov/study/NCT02528201) | Phase 4 | Completed | 330 | 12-week double-blind RCT (celecoxib 200 mg QD, 400 mg QD vs. diclofenac TID in AS), conducted to confirm results of the prior 6-week pivotal trial. |
| [NCT01934933](https://clinicaltrials.gov/study/NCT01934933) | Phase 4 | Completed | 150 | Multi-center open-label randomized trial: celecoxib 200 mg BID alone vs. etanercept 50 mg QW alone vs. celecoxib + etanercept in active AS; primary endpoint was MRI SPARCC score of sacroiliac joints over 54 weeks. |
| [NCT02758782](https://clinicaltrials.gov/study/NCT02758782) | Phase 4 | Completed | 156 | CONSUL trial: evaluated whether adding celecoxib to golimumab (anti-TNF) reduces AS spinal structural damage progression compared to golimumab alone over 2 years. |
| [NCT04115098](https://clinicaltrials.gov/study/NCT04115098) | Phase 2 | Terminated | 42 | Individualized N-of-1 trial design directly comparing selective COX-2 vs. non-selective COX inhibitors in axial SpA adults; terminated early (n=42) but provides feasibility and initial comparative data. |
| [NCT03190603](https://clinicaltrials.gov/study/NCT03190603) | Phase 4 | Completed | 12 | Pilot study using MRI to assess the effect of NSAID on inflammatory lesions in axial SpA; small sample limits generalizability, but provides imaging-based mechanistic support. |
| [NCT02355236](https://clinicaltrials.gov/study/NCT02355236) | Phase 4 | Unknown | 106 | Double-blind RCT comparing Naxozol (naproxen/esomeprazole) vs. celecoxib in OA/RA/AS patients for gastroprotection and pain relief; indirect comparative gastrointestinal safety evidence. |
| [NCT02456363](https://clinicaltrials.gov/study/NCT02456363) | Phase 2 | Unknown | 300 | Registry study comparing adalimumab + NSAID vs. adalimumab alone in AS; NSAID as background therapy component provides indirect evidence of celecoxib's role in combination treatment. |
| [NCT01572675](https://clinicaltrials.gov/study/NCT01572675) | N/A | Completed | 547 | Real-world pharmacoepidemiology study of etoricoxib and celecoxib use in France; provides class-level real-world usage and safety context for COX-2 inhibitors in spondyloarthropathy. |

---

## Literature Evidence

Currently no related literature is directly catalogued in this Evidence Pack for inflammatory spondylopathy. The primary evidentiary basis for this indication rests on the completed Phase 3 and Phase 4 randomized controlled trials listed above — particularly the results from NCT00762463 and NCT00648141, whose published findings constitute the core of the L1 evidence classification.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Taiwan FDA package insert data (TFDA 仿單) was unavailable for this evaluation (Data Gap DG001). Formal warnings and contraindications should be obtained directly from the TFDA official website or from the Celebrex® prescribing information published by approved international regulatory authorities (FDA, EMA, PMDA).

The following class-level safety signals are established for COX-2 selective inhibitors and should be considered in any risk management plan:

- **Cardiovascular risk**: Increased risk of serious thrombotic cardiovascular events (myocardial infarction, stroke), especially with higher doses or prolonged use. The PRECISION trial specifically evaluated celecoxib's cardiovascular profile against ibuprofen and naproxen.
- **Gastrointestinal**: Lower risk of GI ulceration and bleeding compared to non-selective NSAIDs, but the risk is not eliminated — particularly in elderly patients or those on concomitant antiplatelet agents or anticoagulants.
- **Renal function**: Monitor renal function in patients with pre-existing renal impairment, dehydration, heart failure, or concurrent use of diuretics or ACE inhibitors/ARBs.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Celecoxib has an unusually robust L1-level clinical evidence base for inflammatory spondylopathy, anchored by multiple completed Phase 3 and Phase 4 RCTs with direct head-to-head comparisons in ankylosing spondylitis populations. It is already approved for this indication in the United States, the EU, and Japan, providing a clear regulatory precedent that substantially de-risks the pathway. The mechanistic alignment between selective COX-2 inhibition and axial inflammatory disease pathophysiology is well-characterized and clinically validated.

**To proceed, the following is needed:**

- **Taiwan FDA regulatory strategy**: Determine whether a new drug application (NDA) or supplemental indication submission is required by TFDA; evaluate bridging data requirements given existing international AS approvals
- **Package insert and safety data**: Retrieve and review the TFDA 仿單 or international prescribing information to complete the safety assessment and resolve Data Gap DG001 (Blocking severity)
- **Formal MOA documentation**: Obtain DrugBank pharmacology data to support mechanism-based regulatory filing (Data Gap DG002)
- **Cardiovascular risk management plan**: Define patient selection criteria, monitoring protocols, and contraindicated populations before initiating any clinical or market access activities
- **Local population considerations**: Assess whether Taiwan-specific PK, efficacy, or disease epidemiology data is required by TFDA for label approval; the existing Chinese-patient RCT (NCT00762463, n=240) provides partial ethnic bridging evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

