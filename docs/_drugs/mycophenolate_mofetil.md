---
layout: default
title: Mycophenolate Mofetil
parent: High Evidence (L1-L2)
nav_order: 534
evidence_level: L2
indication_count: 10
---

# Mycophenolate Mofetil
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Mycophenolate Mofetil: From Transplant Rejection Prophylaxis to HIV Infectious Disease

> Note: The Evidence Pack's `original_indications` and `original_moa` fields are empty/Data Gap. The original-indication context below (prevention of organ transplant rejection, marketed as CellCept) is well-established public background knowledge, not data from this pack — flagged accordingly rather than presented as sourced fact.

## One-Sentence Summary

Mycophenolate mofetil (DrugBank DB00688) is an immunosuppressant historically used to prevent organ transplant rejection, though this Evidence Pack contains no confirmed original-indication or MOA record for it. The TxGNN model's top prediction is **HIV infectious disease**, supported by **10 clinical trials** and **20 publications**, but most trials are terminated, withdrawn, or of unreported outcome, so the signal remains a research hypothesis rather than established evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in Evidence Pack (no `licenses` data). Known clinically as prevention of organ transplant rejection. |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L2 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (`original_moa`: Data Gap). Based on the mechanistic rationale supplied alongside the prediction, mycophenolate mofetil (MMF) inhibits IMPDH (inosine monophosphate dehydrogenase), blocking de novo guanine nucleotide synthesis and selectively suppressing T- and B-lymphocyte proliferation — the same mechanism underlying its established use in transplant immunosuppression.

The proposed link to HIV is a "host-directed" hypothesis rather than a direct antiviral mechanism: by shrinking the pool of activated, proliferating CD4+ T cells (the cells HIV preferentially infects and replicates in), MMF may reduce chronic immune activation, viral target-cell availability, and potentially the size of the latent reservoir. This is mechanistically distinct from — and complementary to — standard antiretroviral therapy (ART), which is why most supporting trials tested MMF as an *adjunct* to ART or in ART-naïve patients rather than as monotherapy.

This hypothesis has been tested clinically since the early 2000s (e.g., the MAN2 study and several pilot/PK studies combining MMF with abacavir or other NRTIs), giving it more real-world traction than a pure graph-embedding prediction. However, the consistent pattern across trials — small sample sizes, early termination, withdrawal, or unreported ("Unknown") status — indicates the hypothesis has not yet been confirmed as clinically beneficial.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00038272](https://clinicaltrials.gov/study/NCT00038272) | Phase 1/2 | Completed | 56 | Double-blind, placebo-controlled pilot of DAPD ± MMF added to ART regimens in treatment-experienced HIV patients; highest-grade direct evidence for this indication |
| [NCT00021489](https://clinicaltrials.gov/study/NCT00021489) | Phase 2 | Withdrawn | 0 | Planned safety/tolerability/antiretroviral-activity study of MMF added to abacavir in heavily treatment-experienced patients; withdrawn before enrollment, no results |
| [NCT00120419](https://clinicaltrials.gov/study/NCT00120419) | Phase 4 | Unknown | 90 | MAN2 study — MMF vs. no treatment in ART-naïve, chronically HIV-1 infected patients; assessed CD4+ count, plasma HIV-1 RNA, and disease progression; outcome status unreported |
| [NCT00247494](https://clinicaltrials.gov/study/NCT00247494) | Phase 4 | Unknown | 90 | MAN2 substudy evaluating MMF's effect on cardiovascular surrogate markers in ART-naïve HIV-1 patients; outcome status unreported |
| [NCT00009009](https://clinicaltrials.gov/study/NCT00009009) | Phase 2 | Completed | 10 | Renal transplantation in HIV-infected patients with end-stage renal disease, using MMF-based immunosuppression; transplant-context use, not direct HIV therapy |
| [NCT01453192](https://clinicaltrials.gov/study/NCT01453192) | Phase 3 | Completed | 27 | National multicenter follow-up of renal transplantation in HIV-1 infected patients under antiretroviral regimens including raltegravir; transplant-context, not a direct MMF-for-HIV test |
| [NCT00112593](https://clinicaltrials.gov/study/NCT00112593) | N/A | Completed | 5 | Allogeneic HSCT for mixed chimerism induction in HIV-1 infected patients, using cyclosporine + MMF post-transplant; transplant-context use |
| [NCT02793544](https://clinicaltrials.gov/study/NCT02793544) | Phase 2 | Completed | 80 | HLA-mismatched unrelated donor bone marrow transplant with post-transplant cyclophosphamide, sirolimus, and MMF for GVHD prophylaxis in hematologic malignancies; not an HIV indication |
| [NCT01288131](https://clinicaltrials.gov/study/NCT01288131) | Phase 3 | Terminated | 8 | RCT of cyclosporine + MMF vs. cyclophosphamide + prednisolone for anti-EPO associated PRCA; unrelated to HIV |
| [NCT06869265](https://clinicaltrials.gov/study/NCT06869265) | Phase 2 | Recruiting | 56 | TBF conditioning regimen for haploidentical HSCT in elderly high-risk AML patients; MMF not the primary study drug, no HIV relevance |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15355127](https://pubmed.ncbi.nlm.nih.gov/15355127/) | 2004 | PK interaction study | Clinical Pharmacokinetics | MMF's effect on pharmacokinetics of antiretroviral drugs and on intracellular deoxynucleotide triphosphate pools |
| [15871638](https://pubmed.ncbi.nlm.nih.gov/15871638/) | 2005 | PK/PD study | Clinical Pharmacokinetics | Low-dose MMF pharmacokinetics/pharmacodynamics in HIV patients on abacavir, efavirenz, and nelfinavir |
| [16379601](https://pubmed.ncbi.nlm.nih.gov/16379601/) | 2005 | Cohort/observational | AIDS Research and Human Retroviruses | No detrimental immunological effects observed with MMF + HAART in treatment-naïve acute/chronic HIV-1 patients |
| [12352149](https://pubmed.ncbi.nlm.nih.gov/12352149/) | 2002 | Cohort study | J Acquired Immune Deficiency Syndromes | Adding MMF to abacavir-containing ART associated with dGTP depletion and decreased plasma HIV-1 RNA in 5 patients |
| [15213566](https://pubmed.ncbi.nlm.nih.gov/15213566/) | 2004 | Randomized pilot study | J Acquired Immune Deficiency Syndromes | MMF's effect on immune response and viral load during/after HAART interruption in chronic HIV infection |
| [15353978](https://pubmed.ncbi.nlm.nih.gov/15353978/) | 2004 | Clinical study | AIDS (London) | HAART with or without MMF in treatment-naïve HIV-1 patients; effect on plasma HIV-1 RNA decay and latent reservoir |
| [11391161](https://pubmed.ncbi.nlm.nih.gov/11391161/) | 2001 | Pilot study | J Acquired Immune Deficiency Syndromes | MMF as a component of therapy for multidrug-resistant HIV-1 infection in 7 heavily pre-treated AIDS patients |
| [17885292](https://pubmed.ncbi.nlm.nih.gov/17885292/) | 2007 | Clinical study | AIDS (London) | Safety, tolerability, and antiretroviral activity of DAPD with or without MMF in drug-resistant HIV infection |
| [17017956](https://pubmed.ncbi.nlm.nih.gov/17017956/) | 2006 | Review | Current Topics in Medicinal Chemistry | Review of immunosuppressive drugs, including MMF, targeting chronic immune activation in HIV disease |
| [41118390](https://pubmed.ncbi.nlm.nih.gov/41118390/) | 2025 | Mechanistic/translational study | J Clinical Investigation | Antiproliferative drugs selectively targeting clonally expanded HIV-infected CD4+ T cells |

---

## Canada Market Information

No marketing authorization records are present in this Evidence Pack. `taiwan_regulatory.market_status` is "Not Marketed" with `total_licenses: 0` and an empty `licenses` array — no DINs, product names, or approved indication text are available for mycophenolate mofetil in this dataset.

---

## Safety Considerations

Please refer to the package insert for safety information. (All safety fields in this Evidence Pack — key warnings, contraindications, and drug interactions — are marked as data gaps or return no results.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although MMF-for-HIV has a mechanistically coherent, decades-old research thread (L2 evidence: several Phase 1/2 pilot and cohort studies), the pivotal Phase 4 trials (MAN2 and its substudy) have unreported ("Unknown") outcomes and other studies were withdrawn or terminated — no completed trial demonstrates clinical benefit. Combined with a **Blocking** data gap on TFDA/regulatory safety labeling (DG001, which by itself prevents entry into the S1 safety pre-assessment) and the drug's current non-marketed status in Canada (0 DINs), this candidate is not ready to proceed even with guardrails.

**To proceed, the following is needed:**
- TFDA/Health Canada product monograph — warnings, contraindications, precautions (resolves DG001, Blocking)
- Confirmed original indication and MOA from DrugBank (resolves DG002)
- Follow-up on unreported outcomes for NCT00120419 and NCT00247494 (MAN2 study and substudy)
- Clarification of the Canadian regulatory/import pathway given "Not Marketed" status before any clinical use could be considered
- DDI data, since the current query returned zero results (`query_status: not_found`)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

