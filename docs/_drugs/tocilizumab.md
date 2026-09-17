---
layout: default
title: Tocilizumab
parent: Moderate Evidence (L3-L4)
nav_order: 782
evidence_level: L3
indication_count: 10
---

# Tocilizumab
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

Using this evidence pack directly (Canada regulatory template, field key retained as `taiwan_regulatory` per shared codebase convention), I'll flag that `original_indications` and `original_moa` are empty/data-gap in the source pack — I'm not filling these from outside knowledge, per house rule against guessing.

---

# Tocilizumab: A Predicted New Indication in Ankylosing Spondylitis

## One-Sentence Summary

> Tocilizumab's original indication is not yet documented in this evidence pack (flagged as a data gap), though supporting literature identifies it as an IL-6 receptor-targeting biologic developed for rheumatoid arthritis and juvenile idiopathic arthritis.
> The TxGNN model predicts it may be effective for **Ankylosing Spondylitis**,
> with **9 clinical trials** and **19 publications** currently identified — though notably, the two dedicated Phase 3 trials in this indication were **terminated** rather than completed.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (Data Gap — see Conclusion) |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed, manufacturer-sourced mechanism of action data is not currently available in this evidence pack. However, literature within the pack (e.g., PMID 28841363) describes tocilizumab as a recombinant humanized monoclonal antibody against the interleukin-6 receptor (IL-6R), historically developed for rheumatoid arthritis (RA), systemic juvenile idiopathic arthritis (sJIA), and polyarticular JIA. IL-6 blockade suppresses a key pro-inflammatory cytokine cascade shared across several autoimmune/rheumatic diseases.

The mechanistic rationale for ankylosing spondylitis (AS) rests on IL-6's documented role in spondyloarthritis pathogenesis (PMID 22452603, "Antagonizing IL-6 in ankylosing spondylitis"), and on the precedent that IL-6/TNF-pathway biologics are broadly used across the RA–AS–PsA disease spectrum (PMID 19822066, PMID 28413099).

However, this mechanistic plausibility is significantly tempered by direct clinical evidence: two purpose-built Phase 3 RCTs of tocilizumab in AS (NCT01209689, NCT01209702) were both **terminated** in 2011 rather than completed. This is a materially different situation from a drug with no clinical testing — it indicates the hypothesis was already tested at Phase 3 and did not proceed to completion, which historically reflects that IL-6 blockade — unlike TNF inhibition — has not shown the efficacy in axial spondyloarthritis needed to support continued development. This caveat should weigh heavily against the high TxGNN score.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01209689](https://clinicaltrials.gov/study/NCT01209689) | Phase 3 | Terminated | 113 | RCT of tocilizumab vs. placebo in AS patients with inadequate response to prior TNF antagonist therapy; trial did not reach completion. |
| [NCT01209702](https://clinicaltrials.gov/study/NCT01209702) | Phase 3 | Terminated | 306 | Seamless Ph II/III RCT of tocilizumab vs. placebo in NSAID-failure, TNF-naïve AS patients; trial did not reach completion. |
| [NCT05670301](https://clinicaltrials.gov/study/NCT05670301) | N/A | Recruiting | 2500 | Observational cytokine/biomarker profiling across systemic inflammatory diseases; not AS/tocilizumab-specific. |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not Yet Recruiting | 80 | Perioperative immunosuppressant management in rheumatology patients undergoing shoulder arthroplasty; broad rheumatology population. |
| [NCT02569736](https://clinicaltrials.gov/study/NCT02569736) | N/A | Completed | 60 | Mechanistic study of tocilizumab's effect on T follicular helper cells in RA; not AS-specific. |
| [NCT07477795](https://clinicaltrials.gov/study/NCT07477795) | Phase 2 | Not Yet Recruiting | 52 | Secukinumab (not tocilizumab) trial in Takayasu arteritis; included for pathway relevance only. |
| [NCT02925338](https://clinicaltrials.gov/study/NCT02925338) | N/A | Completed | 1431 | Real-world registry of infliximab (Inflectra) use; not tocilizumab/AS-specific. |
| [NCT01965132](https://clinicaltrials.gov/study/NCT01965132) | N/A | Recruiting | 10000 | Korean nationwide biologics/targeted-therapy registry covering RA, AS, and PsA safety. |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750000 | Large-scale registry study of incident IMID risk in patients on biologics/immunosuppressants. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23765873](https://pubmed.ncbi.nlm.nih.gov/23765873/) | 2014 | RCT | Annals of the Rheumatic Diseases | BUILDER-1/2 randomised, placebo-controlled trials assessing short-term symptomatic efficacy of tocilizumab in AS (corresponds to the terminated NCT01209689/NCT01209702 trials). |
| [26986130](https://pubmed.ncbi.nlm.nih.gov/26986130/) | 2016 | Systematic Review/Meta-analysis | Medicine | Network meta-analysis comparing effectiveness of biologic therapy regimens for AS. |
| [22452603](https://pubmed.ncbi.nlm.nih.gov/22452603/) | 2012 | Review | Inflammation & Allergy Drug Targets | Short review on IL-6 antagonism as a mechanistic rationale in AS. |
| [29290076](https://pubmed.ncbi.nlm.nih.gov/29290076/) | 2018 | Meta-analysis | Clinical Rheumatology | Meta-analysis of serious infection risk with biologics in AS and non-radiographic axial spondyloarthritis. |
| [20959960](https://pubmed.ncbi.nlm.nih.gov/20959960/) | 2011 | Review | Osteoporosis International | Review of systemic bone effects of biologic therapies in RA and AS. |
| [22450391](https://pubmed.ncbi.nlm.nih.gov/22450391/) | 2012 | Review | Current Opinion in Rheumatology | Review of treatment alternatives for AS refractory to TNF inhibition. |
| [33981717](https://pubmed.ncbi.nlm.nih.gov/33981717/) | 2021 | Case Report | Frontiers in Medicine | Two case reports of AA amyloidosis in AS successfully treated with tocilizumab. |
| [20851032](https://pubmed.ncbi.nlm.nih.gov/20851032/) | 2010 | Case Report | Joint Bone Spine | Case report of tocilizumab use in a patient with AS and Crohn's disease refractory to TNF antagonists. |
| [28413099](https://pubmed.ncbi.nlm.nih.gov/28413099/) | 2017 | Review | Seminars in Arthritis and Rheumatism | Review of second-line biologic therapy optimization in RA, PsA, and AS. |
| [19822066](https://pubmed.ncbi.nlm.nih.gov/19822066/) | 2009 | Review | Clinical and Experimental Rheumatology | Review comparing biologics in RA and AS treatment, noting pathogenetic differences between the two diseases. |

## Canada Market Information

Tocilizumab currently has **no active market authorization records** in this evidence pack (market status: Not Marketed; 0 DINs on file).

## Safety Considerations

Please refer to the package insert for safety information. Regulatory-sourced key warnings, contraindications, and drug-interaction data are currently unavailable (flagged as a Blocking data gap — DG001).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score (99.99%) and a plausible IL-6–mediated mechanistic link to spondyloarthritis, the two dedicated Phase 3 RCTs in AS were **terminated rather than completed**, which historically reflects that tocilizumab did not demonstrate sufficient efficacy in this indication — a materially different signal than "no trials attempted." Combined with the absence of any regulatory safety documentation (Blocking data gap) and no current Canadian market authorization, this candidate does not currently meet the bar to proceed.

**To proceed, the following is needed:**
- Regulatory safety documentation (warnings, contraindications) — currently Blocking (DG001)
- Confirmed mechanism of action data from DrugBank/product labeling (DG002)
- Retrieval of the terminated NCT01209689/NCT01209702 study reports to confirm whether termination reflects efficacy failure, safety concerns, or sponsor/business decisions
- Clarification of original approved indication(s), currently missing from this evidence pack
- Assessment of a Canadian market-entry pathway given the current "Not Marketed" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

