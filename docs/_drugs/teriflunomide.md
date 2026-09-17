---
layout: default
title: Teriflunomide
parent: High Evidence (L1-L2)
nav_order: 763
evidence_level: L1
indication_count: 1
---

# Teriflunomide
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **1** 
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

# Teriflunomide: Established Efficacy Signal for Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

> This evidence pack does not record a distinct original indication or approved product license for teriflunomide in this dataset — the drug is currently **not marketed in Canada** (0 DINs).
> The TxGNN model assigns a **99.24%** confidence score to **Relapsing-Remitting Multiple Sclerosis (RRMS)**,
> and this is strongly corroborated by **28 clinical trials** (including 4 completed Phase 3 RCTs) and **20 publications**, several of which are head-to-head Phase 3 comparator trials against newer MS therapies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (see Data Gaps DG001/DG002) |
| Predicted New Indication | Relapsing-Remitting Multiple Sclerosis |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L1 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available at the drug-record level for this evidence pack (DG002). However, the supporting literature itself describes the mechanism clearly: PMID 31098896 and PMID 32757523 characterize teriflunomide as an oral agent that **selectively and reversibly inhibits mitochondrial dihydro-orotate dehydrogenase (DHODH)**, blocking de novo pyrimidine synthesis and thereby reducing proliferation of activated T- and B-lymphocytes — the autoreactive immune cells central to MS pathophysiology.

No original indication is recorded in the structured `taiwan_regulatory` data for this evidence pack, so a mechanistic "old indication → new indication" comparison cannot be constructed from the drug record alone. That said, the volume and phase-distribution of the trial and literature evidence — four completed Phase 3 RCTs plus multiple head-to-head Phase 3 comparator trials against later-generation MS drugs (ofatumumab, ublituximab, tolebrutinib, ponesimod, evobrutinib) — indicate that RRMS is not a speculative new target for this molecule but a **well-established, extensively validated clinical use**. In effect, the TxGNN prediction here reproduces a clinically confirmed indication rather than identifying a novel repurposing hypothesis, which is consistent with the very high (99.24%) prediction score despite a comparatively low model rank (12,975).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00134563](https://clinicaltrials.gov/study/NCT00134563) | Phase 3 | Completed | 1,088 | Pivotal placebo-controlled RCT — teriflunomide reduced relapse frequency and delayed disability accumulation (EDSS, MRI outcomes) |
| [NCT00803049](https://clinicaltrials.gov/study/NCT00803049) | Phase 3 | Completed | 742 | Long-term extension of pivotal placebo-controlled study documenting long-term safety and efficacy on disability progression and relapse rate |
| [NCT00883337](https://clinicaltrials.gov/study/NCT00883337) | Phase 3 | Completed | 324 | Rater-blinded comparison of two teriflunomide doses vs interferon beta-1a on relapse, fatigue, and treatment satisfaction |
| [NCT04788615](https://clinicaltrials.gov/study/NCT04788615) | Phase 3 | Completed | 185 | Ofatumumab vs physician's-choice first-line DMT (including teriflunomide) in newly diagnosed RMS |
| [NCT00228163](https://clinicaltrials.gov/study/NCT00228163) | Phase 2 | Completed | 147 | Long-term extension of Phase 2 safety/efficacy study |
| [NCT02490982](https://clinicaltrials.gov/study/NCT02490982) | N/A | Completed | 106 | Real-world observational effectiveness study over ≥2 years in a routine MS clinic setting |
| [NCT03464448](https://clinicaltrials.gov/study/NCT03464448) | N/A | Completed | 30 | Mechanistic study — regulatory B lymphocytes as central mediators of teriflunomide's therapeutic effect |
| [NCT03561402](https://clinicaltrials.gov/study/NCT03561402) | N/A | Completed | 24 | Biomarker association with disease activity during teriflunomide treatment |
| [NCT02833714](https://clinicaltrials.gov/study/NCT02833714) | N/A | Terminated | 26 | Characterization of teriflunomide's effect on B-cell activation and cytokine secretion |
| [NCT04129736](https://clinicaltrials.gov/study/NCT04129736) | Phase 4 | Completed | 12 | Serum and CSF teriflunomide concentration in patients on 14 mg daily dosing |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32757523](https://pubmed.ncbi.nlm.nih.gov/32757523/) | 2020 | RCT | N Engl J Med | Ofatumumab vs teriflunomide — describes teriflunomide's pyrimidine-synthesis-inhibiting mechanism reducing T/B-cell activation |
| [36001711](https://pubmed.ncbi.nlm.nih.gov/36001711/) | 2022 | RCT | N Engl J Med | Ublituximab vs teriflunomide in relapsing MS |
| [40202623](https://pubmed.ncbi.nlm.nih.gov/40202623/) | 2025 | RCT | N Engl J Med | Tolebrutinib (BTK inhibitor) vs teriflunomide in relapsing MS |
| [39307151](https://pubmed.ncbi.nlm.nih.gov/39307151/) | 2024 | RCT | Lancet Neurology | Evobrutinib vs teriflunomide, two Phase 3 trials (evolutionRMS1/2) |
| [33779698](https://pubmed.ncbi.nlm.nih.gov/33779698/) | 2021 | RCT | JAMA Neurology | Ponesimod vs teriflunomide — OPTIMUM Phase 3 trial, first head-to-head oral DMT comparison |
| [35266417](https://pubmed.ncbi.nlm.nih.gov/35266417/) | 2022 | RCT | Mult Scler | Ofatumumab vs teriflunomide in treatment-naive patients — ASCLEPIOS I/II |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Systematic Review/Meta-analysis | Cochrane Database Syst Rev | Network meta-analysis of immunomodulators/immunosuppressants including teriflunomide for RRMS |
| [31098896](https://pubmed.ncbi.nlm.nih.gov/31098896/) | 2019 | Review | Drugs | Comprehensive review of teriflunomide's mechanism and RCT/real-world evidence in RRMS |
| [26758290](https://pubmed.ncbi.nlm.nih.gov/26758290/) | 2016 | Review | CNS Drugs | Review of EU SmPC for teriflunomide, safety outcomes and prescribing considerations |
| [33620411](https://pubmed.ncbi.nlm.nih.gov/33620411/) | 2021 | Review | JAMA | General review of MS diagnosis and treatment, including disease-modifying therapies |

---

## Canada Market Information

Teriflunomide currently has **no marketing authorization (DIN) records** in this dataset. Market status is recorded as **Not Marketed** with 0 total licenses, so no product/dosage-form table can be generated.

---

## Safety Considerations

Please refer to the package insert for safety information. This evidence pack contains no populated warnings, contraindications, or drug-interaction data for teriflunomide (DG001, severity: Blocking).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Clinical and literature evidence for teriflunomide in RRMS is extensive and mature (L1), but a blocking data gap exists — no TFDA/Health Canada label warnings or contraindications are available (DG001), which prevents initial safety screening (S1). The drug is also not currently marketed in Canada (0 DINs), so there is no existing regulatory pathway on file to build from.

**To proceed, the following is needed:**
- Official product label / warnings and contraindications (source: TFDA or Health Canada label, per DG001 remediation)
- Structured mechanism-of-action record for the drug entry (per DG002 remediation — currently only available indirectly via literature abstracts)
- Confirmation of original approved indication(s) and any existing global regulatory status, to properly frame this as repurposing vs. established use
- Canada market-entry/licensing pathway assessment if pursuing DIN application
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

