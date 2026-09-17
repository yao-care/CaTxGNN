---
layout: default
title: Velpatasvir
parent: Moderate Evidence (L3-L4)
nav_order: 823
evidence_level: L4
indication_count: 10
---

# Velpatasvir
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Velpatasvir: From Chronic Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

Velpatasvir is the NS5A-inhibitor component of the sofosbuvir/velpatasvir (SOF/VEL, Epclusa®) combination, internationally used to treat chronic hepatitis C virus (HCV) infection. TxGNN assigns a very high score (99.87%) to a predicted new indication of **hepatitis B virus (HBV) infection**, and the evidence pack flags **26 clinical trials** and **20 publications** against this candidate — but on inspection, almost all of that evidence describes HCV treatment, with only one HBV-related publication, and it concerns a safety signal (viral reactivation), not therapeutic efficacy.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Health Canada filings (drug not marketed in Canada); internationally approved as part of SOF/VEL for chronic hepatitis C virus (HCV) infection |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for velpatasvir is not available in the standard MOA field, but the evidence pack's own mechanistic analysis provides relevant context: velpatasvir is a specific inhibitor of the HCV NS5A protein, a target unique to the *Flaviviridae* HCV replication complex. HBV belongs to the *Hepadnaviridae* family and replicates via a reverse-transcriptase mechanism with no NS5A homolog — meaning there is no known direct pharmacological target for velpatasvir in HBV.

The original indication (chronic hepatitis C) and the predicted new indication (hepatitis B) share only superficial similarity — both are viral hepatitides affecting the liver — but this does not translate into a shared drug target. Reviewing the supporting evidence confirms this: of the 26 registered trials, only **NCT04997564** actually involves HBV, and its design uses tenofovir alafenamide (TAF), not velpatasvir, to *prevent* HBV reactivation during HCV treatment with SOF/VEL — this is a safety/prophylaxis study, not evidence that velpatasvir treats HBV. The remaining trials are exclusively HCV treatment studies (several explicitly graded "C" / not relevant by the evidence pipeline). Of the 20 publications, only one (PMID 31542053) concerns HBV, and it is a case report of HBV reactivation occurring *during* HCV therapy with sofosbuvir/velpatasvir — again a safety observation, not efficacy data.

In short, the high TxGNN score appears to be driven by velpatasvir's dense association with viral-hepatitis-related knowledge graph nodes (shared diagnostic codes, co-infection studies, hepatology literature) rather than a genuine pharmacological signal for HBV treatment.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | Unknown | 120 | SOF/VEL for HCV in HCV/HBV co-infected patients, with prophylactic TAF to prevent HBV reactivation — tests TAF for HBV control, not velpatasvir efficacy against HBV |
| [NCT02996682](https://clinicaltrials.gov/study/NCT02996682) | Phase 3 | Completed | 102 | SOF/VEL ± ribavirin in HCV decompensated cirrhosis; graded not relevant — study population is HCV, not HBV |
| [NCT01858766](https://clinicaltrials.gov/study/NCT01858766) | Phase 2 | Completed | 379 | SOF/VEL ± ribavirin in treatment-naive chronic HCV genotypes 1–6; graded not relevant to HBV |
| [NCT02533427](https://clinicaltrials.gov/study/NCT02533427) | Phase 1 | Completed | 15 | Drug interaction study of SOF/VEL/voxilaprevir (HCV triple regimen) with hormonal contraceptives; graded not relevant to HBV |

**Note:** The remaining ~22 registered trials associated with this prediction are chronic HCV studies (treatment access, transplantation, retreatment, pharmacokinetics, etc.) with no HBV treatment arm and no mention of HBV efficacy.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Case report | Journal of Medical Case Reports | HBV reactivation (driven by an HBsAg immune-escape mutant) in an anti-HBc-positive patient during sofosbuvir/velpatasvir treatment for HCV — a safety/reactivation signal, not evidence of anti-HBV efficacy |

**Note:** The remaining 19 publications flagged for this prediction (e.g., PMID 35248213, 38910758, 33217040) all address sofosbuvir/velpatasvir efficacy and safety in HCV — including HCV genotype-specific cohorts, renal disease, and pediatric populations — with no data on velpatasvir activity against HBV.

## Canada Market Information

Velpatasvir (as a single entity or combination) currently holds **no Drug Identification Numbers (DINs) in Canada** and is not marketed here based on the available regulatory data.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN score for the HBV prediction is very high, the mechanistic basis is absent (velpatasvir's NS5A target has no HBV homolog) and the cited clinical/literature evidence is almost entirely about HCV treatment rather than HBV — the single HBV-relevant publication describes a reactivation risk, not therapeutic benefit. The remaining nine ranked predictions for this candidate (hepatitis E, hepatitis A, animal viral hepatitis, Omsk hemorrhagic fever, Kyasanur forest disease, HIV, SIV, feline AIDS, and an unrelated neurodevelopmental disorder) are similarly unsupported — most sit at Evidence Level L5 with zero relevant trials or literature, and are explicitly flagged by the evidence pack's own rationale as likely knowledge-graph noise rather than genuine repurposing signals.

**To proceed, the following is needed:**
- Health Canada product monograph / warnings and contraindications (currently a blocking data gap — DG001)
- Confirmed mechanism-of-action documentation from DrugBank (DG002)
- A prospective or retrospective study specifically evaluating velpatasvir (or SOF/VEL) as a direct anti-HBV therapeutic, rather than as a co-administered agent during HCV treatment in HBV/HCV co-infected patients
- Re-scoping of the TxGNN candidate list to exclude disease nodes with no plausible mechanistic link, before further evaluation resources are allocated to this drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

