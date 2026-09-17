---
layout: default
title: Raltegravir
parent: Moderate Evidence (L3-L4)
nav_order: 662
evidence_level: L4
indication_count: 3
---

# Raltegravir
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Raltegravir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Raltegravir is an HIV-1 integrase strand transfer inhibitor (INSTI), as reflected throughout its own clinical trial record, though a formally documented original indication is not available in this data pack. TxGNN's top-ranked prediction proposes **Feline Acquired Immunodeficiency Syndrome (FIV)** with a 99.78% score, but the two clinical trials cited as supporting evidence are actually human HIV-1 Phase 3 trials comparing dolutegravir to raltegravir — they appear to have been matched on text similarity ("acquired immunodeficiency syndrome") rather than genuine species-specific relevance, and no literature evidence exists for this candidate.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (inferred from trial descriptions in the evidence pack; not formally recorded in `original_indications`) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV) |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this pack (marked as a High-severity data gap). Based on the trial descriptions present in the evidence, raltegravir is known to act as an HIV-1 integrase strand transfer inhibitor (INSTI), blocking viral DNA integration into the host genome.

The mechanistic rationale for FIV is theoretical: Feline Immunodeficiency Virus (FIV) and HIV are both lentiviruses, and integrase inhibitors could in principle have cross-species activity against related retroviral integrases. However, this pack contains **no FIV-specific efficacy, safety, or pharmacokinetic data**. The two clinical trials attached as "evidence" (NCT01231516, NCT01227824) are human HIV-1 Phase 3 trials with no feline component — they most likely appear here due to disease-name text overlap rather than true relevance, as noted directly in the model's own relevance grading (Grade C, "文字比對誤植" / text-matching artifact). This candidate should be treated as **mechanistically plausible but evidentially unsupported**.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01231516](https://clinicaltrials.gov/study/NCT01231516) | Phase 3 | Completed | 724 | Dolutegravir 50mg QD vs raltegravir 400mg BID in HIV-1 infected, integrase-inhibitor-naïve, ART-experienced adults (human trial; not feline-related) |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | Dolutegravir 50mg QD vs raltegravir 400mg BID + fixed-dose dual NRTI in HIV-1 ART-naïve adults over 96 weeks (human trial; not feline-related) |

**Note:** Both trials are human HIV-1 studies and provide no direct support for the FIV indication; they are included here only because they were returned by the underlying evidence query.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Raltegravir is not currently marketed in Canada (market status: Not Marketed, 0 DINs on file). No product license records are available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked FIV prediction is a high TxGNN score with no genuine supporting evidence — the cited trials are a human-disease text-matching artifact, not species-relevant data, and the drug is unmarketed in Canada with no available safety label. This candidate should not advance without independent verification.

**To proceed, the following is needed:**
- Resolve the TFDA/Health Canada label data gap (key warnings, contraindications — currently Blocking, DG001)
- Confirm formal mechanism of action from DrugBank (currently High severity, DG002)
- Obtain genuine FIV-specific pharmacology, efficacy, or veterinary trial data before treating this as a supported repurposing candidate
- Note: a lower-ranked candidate in this same evidence pack, **simian immunodeficiency virus (SIV) infection** (rank 2, Evidence Level L3, decision stage "Research Question"), has substantially stronger mechanistic and translational-model support (19 literature citations on raltegravir in SIV-infected macaque models) and may be a more credible research direction than the rank-1 FIV pairing evaluated above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

