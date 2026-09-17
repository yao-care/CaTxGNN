---
layout: default
title: Zidovudine
parent: Moderate Evidence (L3-L4)
nav_order: 837
evidence_level: L4
indication_count: 6
---

# Zidovudine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **6** 
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

# Zidovudine: From HIV/AIDS to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

> Zidovudine (AZT) is a nucleoside reverse transcriptase inhibitor originally developed and approved for the treatment of human immunodeficiency virus (HIV) infection/AIDS.
> The TxGNN model's top-ranked prediction links it to **Feline Acquired Immunodeficiency Syndrome (FIV/FAIDS)** — a veterinary lentiviral disease in cats —
> with a **99.96% prediction score**, but currently supported only by **20 preclinical/veterinary literature reports** and **no clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV/AIDS (human immunodeficiency virus infection) — based on general drug knowledge; no Canadian license record is available to confirm this |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV/FAIDS) |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in this Evidence Pack (Data Gap DG002). Based on general pharmacological knowledge, zidovudine is a thymidine-analogue nucleoside reverse transcriptase inhibitor (NRTI), and its efficacy against human immunodeficiency virus (HIV) has been well established since its original approval.

The top-ranked predicted indication — feline acquired immunodeficiency syndrome — is caused by the feline immunodeficiency virus (FIV), a lentivirus whose reverse transcriptase is structurally homologous to HIV-1's. This shared enzymatic target is presumably why TxGNN's knowledge graph connects the two conditions: the underlying antiviral mechanism (reverse-transcriptase inhibition) is common to both. However, as the evidence pack's own rationale notes, FIV/FAIDS is a veterinary indication in cats, not a human clinical target. It is mechanistically informative — essentially an animal-model confirmation of zidovudine's antiretroviral activity — but it does not constitute a viable human drug-repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2475068](https://pubmed.ncbi.nlm.nih.gov/2475068/) | 1989 | Preclinical model | Antimicrob Agents Chemother | Establishes FIV as a model for reverse-transcriptase-targeted chemotherapy of AIDS; compares FIV and HIV-1 reverse transcriptase |
| [18550661](https://pubmed.ncbi.nlm.nih.gov/18550661/) | 2008 | Molecular epidemiology | J Virol | Phylogenetic analysis of FIV gag/pol/env genes in AZT-treated vs. treatment-naïve cats in Brazil |
| [7688949](https://pubmed.ncbi.nlm.nih.gov/7688949/) | 1993 | Animal study | Arch Virol | Zidovudine and cyclosporine reduced FIV plasma virus titer but not PBMC virus titer in infected cats |
| [7618256](https://pubmed.ncbi.nlm.nih.gov/7618256/) | 1995 | Animal model (SCID-feline mice) | Vet Immunol Immunopathol | AZT reduced provirus burden and enhanced humoral immune function in SCID-feline mice inoculated with FIV |
| [9226004](https://pubmed.ncbi.nlm.nih.gov/9226004/) | 1997 | Drug delivery study | J Leukoc Biol | Erythrocyte-based targeted delivery system for phosphorylated nucleoside analogues (incl. AZT derivatives) to macrophages |
| [15047505](https://pubmed.ncbi.nlm.nih.gov/15047505/) | 2004 | Topical prophylaxis study | Antimicrob Agents Chemother | AZT-derivative spermicide WHI-07 prevented vaginal and rectal FIV transmission in cats |
| [8399067](https://pubmed.ncbi.nlm.nih.gov/8399067/) | 1993 | Animal study | J Immunother | Combined adoptive lymphocyte transfer, interferon-alpha, and zidovudine reversed feline leukemia virus infection |
| [2178336](https://pubmed.ncbi.nlm.nih.gov/2178336/) | 1990 | Animal study | Antimicrob Agents Chemother | Interferon-alpha2b + AZT combination evaluated in presymptomatic FeLV-induced immunodeficiency syndrome (FAIDS) cats |
| [2164083](https://pubmed.ncbi.nlm.nih.gov/2164083/) | 1990 | Animal study | J Acquir Immune Defic Syndr | AZT + interferon-alpha + IL-2 as prophylactic therapy for FeLV-FAIDS; AZT inhibited FeLV replication in vitro |
| [1666108](https://pubmed.ncbi.nlm.nih.gov/1666108/) | 1991 | Review / animal research | J Am Vet Med Assoc | Review of chemotherapy options, including zidovudine, for feline immunodeficiency virus infection |

---

## Canada Market Information

Zidovudine currently has **no marketing authorization in Canada** (market status: Not Marketed; total DINs: 0). No product license records are available in this Evidence Pack, so a licensed-product table cannot be generated.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and drug-interaction data are recorded as Data Gaps in this Evidence Pack — see DG001, a Blocking-severity gap that also prevents entry into the S1 safety pre-assessment stage.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked TxGNN prediction points to a veterinary lentiviral disease (FIV/FAIDS in cats), not a human-relevant indication, and is supported only by preclinical/animal literature (Evidence Level L4) with zero clinical trials — it does not meet the bar for human repurposing evaluation.
- A Blocking data gap (DG001 — missing product label warnings/contraindications) prevents this candidate from even entering the S1 safety pre-assessment stage, and the drug is not currently marketed in Canada (0 DINs).

**To proceed, the following is needed:**
- Product label data (warnings, contraindications) to resolve the Blocking gap DG001 and enable S1 safety pre-assessment
- Mechanism-of-action documentation (DG002) from DrugBank or equivalent source
- Re-ranking or filtering of TxGNN predictions to prioritize disease candidates relevant to human clinical practice (e.g., items #5–#6 in this pack — congenital HIV and AIDS-related complex — which already show L1 evidence and a "Proceed with Guardrails" recommendation, though these largely reflect zidovudine's known original human HIV indication rather than a novel repurposing signal)
- Canadian market-authorization data (DIN/product listing) if human repurposing in this market is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

