---
layout: default
title: Lamivudine
parent: 僅模型預測 (L5)
nav_order: 439
evidence_level: L5
indication_count: 5
---

# Lamivudine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Lamivudine (DB00709): From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Lamivudine is a nucleoside reverse transcriptase inhibitor (NRTI) classically used against human HIV-1 and chronic hepatitis B; this evidence pack does not contain regulatory-confirmed original-indication data for this market. TxGNN's top-ranked prediction is **Feline Acquired Immunodeficiency Syndrome (FIV)** — a veterinary, not human, disease — with **5 clinical trials** (all human HIV trials, not FIV-specific) and **5 publications** (veterinary/in-vitro FIV studies) as supporting evidence. The evidence level is **L3**, and the system-generated recommendation for this candidate is **Hold**, largely because the predicted indication falls outside the human therapeutic scope this evaluation framework is meant to assess.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from this evidence pack's regulatory data (licenses list is empty). Based on general pharmacological knowledge, lamivudine is used for HIV-1 infection and chronic hepatitis B. |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV) — a veterinary disease |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L3 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on known pharmacology, lamivudine is a cytidine-analog NRTI that inhibits HIV-1 reverse transcriptase and HBV DNA polymerase — both viruses that replicate through a reverse-transcription step.

FIV (Feline Immunodeficiency Virus) is also a lentivirus, in the same broad retrovirus family as HIV, with a similar replication mechanism. This gives some theoretical cross-species plausibility for NRTI activity — several published in-vitro and small animal studies do show lamivudine (often combined with zidovudine) suppressing FIV replication in cats.

However, this predicted indication describes a **veterinary disease in cats, not a human condition**. It falls outside the scope of human drug repurposing evaluation. The most likely explanation is that TxGNN's knowledge graph placed the FIV node semantically adjacent to HIV/AIDS-related nodes, producing a high similarity score that does not reflect a viable human indication. None of the associated clinical trials are FIV-specific — they are all human HIV-1 trials evaluating lamivudine-containing regimens for unrelated purposes, and are only loosely relevant (graded "C" where assessed).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | Dolutegravir vs raltegravir, both with dual NRTI (incl. lamivudine), in ART-naïve HIV-1 adults. Relevance grade C: human HIV trial, not FIV. |
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Boosted darunavir + lamivudine vs other regimens in naïve HIV-1 adults. Relevance grade C: human HIV trial, not FIV. |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Dose-selection study of GSK1349572 with abacavir/lamivudine or tenofovir/emtricitabine in HIV-1 adults. Relevance not yet graded. |
| [NCT01499199](https://clinicaltrials.gov/study/NCT01499199) | Phase 3 | Completed | 13 | Dolutegravir + abacavir/lamivudine, CNS/plasma PK, in HIV-1 adults. Relevance not yet graded. |
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Dolutegravir + abacavir/lamivudine vs Atripla in ART-naïve HIV-1 adults. Relevance grade C: human HIV trial, not FIV. |

*Note: all five trials are human HIV-1 studies; none directly investigate FIV in cats.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25855689](https://pubmed.ncbi.nlm.nih.gov/25855689/) | 2016 | Cohort | J Feline Med Surg | Long-term antiretroviral therapy (incl. lamivudine-class agents) follow-up in FIV-infected cats. |
| [11943320](https://pubmed.ncbi.nlm.nih.gov/11943320/) | 2002 | Cohort | Vet Immunol Immunopathol | AZT/3TC (lamivudine) combination shows additive-to-synergistic anti-FIV activity in vitro and in vivo. |
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | Cohort | Antiviral Research | Zidovudine + lamivudine + abacavir combination suppresses FIV replication in vitro; FIV proposed as HIV animal model. |
| [22816032](https://pubmed.ncbi.nlm.nih.gov/22816032/) | 2012 | Cohort | Viruses | Evaluates antiretroviral protocols (incl. lamivudine) in naturally FIV-infected cats in late asymptomatic stage. |
| [11327469](https://pubmed.ncbi.nlm.nih.gov/11327469/) | 2001 | In vitro | Am J Vet Res | Characterizes FIV molecular clone and 3TC-resistant mutants; in-vitro replication/susceptibility study. |

---

## Canada Market Information

Lamivudine is currently not marketed in this jurisdiction under this evidence pack — no Drug Identification Numbers (DINs) or license records are present (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all currently absent from this evidence pack — TFDA/label warning data is flagged as a Blocking data gap, DG001, that must be resolved before any safety pre-assessment can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (FIV) is a veterinary indication, not a human disease, so it cannot proceed through a human drug-repurposing pathway regardless of its high TxGNN score. The remaining ranked candidates in this pack are similarly weak or inapplicable: simian immunodeficiency virus infection (L4, animal-model literature only), a rare neurodevelopmental disorder and an obsolete hyperlipidemia classification (both L5, no supporting evidence), and chronic hepatitis C (L4, but mechanistically mismatched since lamivudine targets reverse transcriptase while HCV replicates via RNA-dependent RNA polymerase). No candidate in this pack currently supports a "Go" or "Proceed with Guardrails" decision.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA label warnings/contraindications) — currently blocking any safety pre-assessment
- Resolve DG002 (mechanism-of-action data via DrugBank API)
- Re-run TxGNN candidate generation restricted to human-disease ontology nodes, to filter out veterinary/animal-model artifacts like FIV and SIV
- If a human-relevant candidate is identified, source dedicated human clinical trial and literature evidence specific to that indication (current trial/literature evidence here is all repurposed from unrelated HIV/HBV studies rather than indication-specific research)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

