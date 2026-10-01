---
layout: default
title: Ozanimod
parent: Model Prediction Only (L5)
nav_order: 691
evidence_level: L5
indication_count: 1
---

# Ozanimod
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Ozanimod: From Relapsing Multiple Sclerosis to Progressive Relapsing Multiple Sclerosis

## One-Sentence Summary

Ozanimod (ZEPOSIA) is an oral sphingosine-1-phosphate (S1P) receptor modulator. Published literature describes its approval for relapsing forms of multiple sclerosis (MS).
The TxGNN model predicts it may be effective for **progressive relapsing multiple sclerosis**, with **7 registered clinical trials** and **18 publications** retrieved.
The evidence is **adjacent, not direct**: none of the trials or papers tests ozanimod in this phenotype. The high score mostly reflects the existing relapsing-MS approval rather than a new repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relapsing forms of multiple sclerosis (per published literature; the licence records provided contain no indication text) |
| Predicted New Indication | Progressive relapsing multiple sclerosis |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L4 (no direct study in the predicted indication; the only Phase 3 RCT is in relapsing MS) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the structured drug record. The literature describes ozanimod as a novel, orally administered S1P receptor modulator (receptor subtypes 1 and 5). It retains lymphocytes in lymphoid tissue and reduces their infiltration into the central nervous system. It may also act directly on CNS-resident cells.

"Progressive relapsing MS" is a legacy phenotype label. Current classification maps it to progressive MS with superimposed disease activity. The mechanism therefore plausibly supports a benefit on the inflammatory (relapse) component. It does not clearly support a benefit on neurodegeneration-driven progression. Reviews in the evidence set make the same point: disease-modifying therapies for relapsing MS act mainly on peripheral immune cells and have limited efficacy once progression is established. Early preclinical work suggests S1PR-1/5 modulation may have effects in models of CNS degeneration, but this is not clinical evidence.

Ozanimod is already marketed for relapsing forms of MS. The TxGNN score of 99.34% therefore mostly reflects an existing approval. This is best treated as a **label-adjacent extension question**, not a new-indication finding.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02576717](https://clinicaltrials.gov/study/NCT02576717) | Phase 3 | Completed | 2,494 | Randomized, double-blind, double-dummy, active-controlled study of RPC1063 (ozanimod's development code) in relapsing MS. Only Phase 3 RCT in the set, but not in the predicted phenotype. No results provided. |
| [NCT06396039](https://clinicaltrials.gov/study/NCT06396039) | Phase 4 | Active, not recruiting | 84 | Single-arm, open-label study of effectiveness and safety of oral ozanimod in Chinese adults with relapsing MS. |
| [NCT05605782](https://clinicaltrials.gov/study/NCT05605782) | N/A | Active, not recruiting | 9,000 | ORION: post-authorisation, long-term, non-interventional safety study of ozanimod in RRMS. Provides safety data only, not efficacy. |
| [NCT05828901](https://clinicaltrials.gov/study/NCT05828901) | N/A | Recruiting | 60 | Observational study of disease activity and rebound risk in MS patients on S1P receptor modulators. Class-relevant for safety, not ozanimod-specific. |
| [NCT04676204](https://clinicaltrials.gov/study/NCT04676204) | N/A | Enrolling by invitation | 323 | STATURE: observational study of treatment burden and adherence across six oral MS therapies, including ozanimod. |
| [NCT03535298](https://clinicaltrials.gov/study/NCT03535298) | Phase 4 | Active, not recruiting | 800 | DELIVER-MS: early intensive versus escalation therapy in RRMS. Addresses treatment strategy; ozanimod is not confirmed as a study drug. |
| [NCT03500328](https://clinicaltrials.gov/study/NCT03500328) | N/A | Active, not recruiting | 900 | Pragmatic trial of early aggressive versus escalation therapy in MS. Addresses strategy; does not test ozanimod. |

One further registered study (NCT05688436, pregnancy outcomes with diroximel fumarate) concerns a different drug and is not listed.

---

## Literature Evidence

No randomized controlled trials were found. Network meta-analyses are listed first, followed by reviews.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39254048](https://pubmed.ncbi.nlm.nih.gov/39254048/) | 2024 | Network meta-analysis | Cochrane Database Syst Rev | Immunomodulators and immunosuppressants in progressive MS. A broader range of options now exists, but relative benefit and safety remain unclear for lack of direct comparison trials. |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Network meta-analysis | Cochrane Database Syst Rev | Update of the Cochrane review on immunomodulators and immunosuppressants in relapsing-remitting MS. |
| [33287177](https://pubmed.ncbi.nlm.nih.gov/33287177/) | 2020 | Review | Neurol Int | Comprehensive review of ozanimod's efficacy and side effects in relapsing forms of MS. |
| [32385738](https://pubmed.ncbi.nlm.nih.gov/32385738/) | 2020 | Review | Drugs | "Ozanimod: First Approval." Describes US FDA approval (March 2020) for relapsing forms of MS, including clinically isolated syndrome, relapsing-remitting disease and active secondary progressive disease. |
| [36946625](https://pubmed.ncbi.nlm.nih.gov/36946625/) | 2023 | Review | Expert Opin Pharmacother | Update on S1P receptor modulators (fingolimod, siponimod, ozanimod, ponesimod) in relapsing MS. |
| [33797705](https://pubmed.ncbi.nlm.nih.gov/33797705/) | 2021 | Review | CNS Drugs | Overview of S1P receptor modulators for MS. |
| [31598138](https://pubmed.ncbi.nlm.nih.gov/31598138/) | 2019 | Review | Ther Adv Neurol Disord | Latest developments in progressive MS. Continued compartmentalized inflammation is among the proposed drivers of progression. |
| [38162670](https://pubmed.ncbi.nlm.nih.gov/38162670/) | 2023 | Review | Front Immunol | Therapies for relapsing MS suppress peripheral immune cells and have limited efficacy in progressive forms, where CNS-resident cells play a critical role. |
| [37638037](https://pubmed.ncbi.nlm.nih.gov/37638037/) | 2023 | Preclinical | Front Immunol | S1PR-1/5 modulator RP-101074 showed beneficial effects in a model of CNS degeneration. Mechanistic support only. |
| [35805142](https://pubmed.ncbi.nlm.nih.gov/35805142/) | 2022 | Review | Cells | S1P signalling and S1P pathway modulators, from current insights to future perspectives. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2506009 | ZEPOSIA |
| 2505991 | ZEPOSIA |

---

## Safety Considerations

Please refer to the package insert for safety information.

Two registered studies address safety. ORION (NCT05605782) is a long-term post-authorisation study of ozanimod. NCT05828901 examines disease rebound with S1P receptor modulators.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is plausible mechanistically for the inflammatory component of the disease. However, no study in the evidence set tests ozanimod in progressive relapsing MS (a legacy label for progressive MS with superimposed activity). The high model score largely reflects ozanimod's existing relapsing-MS approval. The Health Canada package insert warnings are also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications), obtained from the Health Canada website
- Approved indication text and dosage forms for both DINs, to confirm whether the current label already covers active progressive disease
- Mechanism of action data from DrugBank
- Direct clinical evidence in progressive MS with superimposed relapse activity, or a subgroup analysis from the completed Phase 3 programme
- A review of the NCT05605782 (ORION) and NCT05828901 safety findings, including rebound risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

