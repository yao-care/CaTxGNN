---
layout: default
title: Abacavir
parent: 僅模型預測 (L5)
nav_order: 11
evidence_level: L5
indication_count: 3
---

# Abacavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Abacavir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Abacavir is a carbocyclic nucleoside analogue reverse transcriptase inhibitor (NRTI) used as part of combination antiretroviral therapy for HIV-1 infection in humans.
The TxGNN model predicts it may be effective for **Feline Acquired Immunodeficiency Syndrome (FIV)**,
with **4 clinical trials** (all conducted in human HIV-1, providing indirect mechanistic support) and **no direct FIV-specific publications** currently identified.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (combination antiretroviral therapy) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV) |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on contextual information from the clinical trial evidence and repurposing rationale provided, Abacavir is a carbocyclic nucleoside analogue that — once intracellularly phosphorylated to its active triphosphate form (carbovir triphosphate, CBV-TP) — acts as a competitive inhibitor and obligate chain terminator of viral reverse transcriptase, blocking RNA→DNA reverse transcription and thereby halting viral replication. This NRTI mechanism is the established basis for its efficacy across multiple large Phase 3 trials in HIV-1-infected patients.

Feline Immunodeficiency Virus (FIV) and HIV-1 both belong to the genus *Lentivirus* within the family *Retroviridae* and share an obligate dependence on viral reverse transcriptase for replication. This shared enzymatic target provides biochemically plausible grounds for cross-species antiviral activity. FIV is in fact recognized as a natural animal model for HIV disease research, lending additional biological coherence to the TxGNN prediction. Notably, a second top-ranked TxGNN prediction — **Simian Immunodeficiency Virus (SIV) infection** (score 99.79%) — is supported by a published in vitro study (PMID 15040537) that directly tested Abacavir and other antiretrovirals against SIV strains, further reinforcing the plausibility of cross-lentiviral NRTI activity.

However, FIV reverse transcriptase is structurally distinct from HIV-1 reverse transcriptase, with differences in active-site geometry that affect nucleoside analogue susceptibility. Therefore, while the mechanistic rationale is sound, the actual effective concentration, tolerability, and antiviral potency of Abacavir specifically against FIV reverse transcriptase must be established through dedicated experimental studies before any clinical application in cats can be considered.

---

## Clinical Trial Evidence

> **Important note:** No clinical trials specifically investigating Abacavir for Feline Acquired Immunodeficiency Syndrome (FIV) were identified. The four trials below are human HIV-1 studies that provide **indirect mechanistic support** (Grade B–C) for Abacavir's NRTI backbone activity.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | Large RCT demonstrating non-inferior antiviral activity of dolutegravir vs. raltegravir, both combined with ABC/3TC or TDF/FTC; confirms Abacavir as a robust NRTI backbone in HIV-1 ART-naïve patients over 96 weeks |
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Phase 3 RCT establishing non-inferiority of dolutegravir + ABC/3TC once daily vs. Atripla® over 96 weeks; confirms long-term efficacy and tolerability of the Abacavir/Lamivudine fixed-dose backbone |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Phase 2b dose-selection study evaluating once-daily GSK1349572 with either ABC/3TC or TDF/FTC; provides dose-optimization context for Abacavir-containing regimens in HIV-1 |
| [NCT01499199](https://clinicaltrials.gov/study/NCT01499199) | Phase 3 | Completed | 13 | Small open-label PK study evaluating CNS and plasma pharmacokinetics of dolutegravir + ABC/3TC; primarily a PK study with limited relevance to FIV efficacy assessment |

---

## Literature Evidence

Currently no literature directly investigating Abacavir for Feline Acquired Immunodeficiency Syndrome is available.

> For reference, one publication relevant to the **second-ranked prediction** (SIV infection) was identified:
>
> | PMID | Year | Type | Journal | Key Findings |
> |------|------|------|---------|---------|
> | [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro study | Antiviral Therapy | Evaluated antiviral activity of 16 approved antiretrovirals (including Abacavir-class NRTIs) against HIV-2, SIV mac251, SIV B670, and SHIV strains; provides direct in vitro evidence that nucleoside analogues active against HIV-1 may retain activity against closely related primate lentiviruses |

---

## Canada Market Information

Abacavir is currently **not marketed in Canada**. No Drug Identification Numbers (DINs) are on record in the current regulatory dataset.

> **Contextual note:** Abacavir (brand names Ziagen®, Kivexa®/Epzicom®, Triumeq®) holds regulatory approval and is widely used clinically in the United States, European Union, and many other jurisdictions for HIV-1 treatment. The absence of Canadian DINs may reflect a data gap in the current dataset rather than true global non-availability. Independent verification against the Health Canada Drug Product Database is recommended.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Contextual safety alert (from published medical literature):** Abacavir carries a well-characterized risk of severe, potentially life-threatening hypersensitivity reactions (HSR) linked to the HLA-B\*57:01 allele in humans. Pre-screening for HLA-B\*57:01 before treatment initiation is standard of care in human medicine. The applicability of this immunogenetic risk to feline species is unknown, and species-specific adverse event profiling would be required in any veterinary development program.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the TxGNN prediction is mechanistically coherent — FIV and HIV-1 share lentiviral biology and dependence on reverse transcriptase — all current clinical trial evidence is indirect (human HIV-1 studies only), no FIV-specific efficacy data exist in this Evidence Pack, and Abacavir is not currently approved or marketed in Canada. At L4 evidence, the mechanistic hypothesis is promising but unvalidated for the feline indication.

**To proceed, the following is needed:**

- **In vitro FIV susceptibility testing**: Conduct cell-based antiviral assays to determine Abacavir's EC₅₀ against FIV strains (e.g., FIV-Petaluma) and directly confirm NRTI activity against feline reverse transcriptase
- **Feline pharmacokinetics (PK) study**: Feline drug metabolism, oral bioavailability, and plasma half-life of Abacavir may differ substantially from human PK; dedicated feline PK/PD data are required
- **Veterinary safety assessment**: Evaluate species-specific tolerability in cats, including haematological parameters (CBC), hepatic and renal function, and any immunologically mediated adverse events distinct from the HLA-B\*57:01 mechanism
- **MOA documentation**: Retrieve complete mechanism of action data from DrugBank (DB01048) and available package inserts to support the mechanistic bridging argument
- **Veterinary regulatory pathway mapping**: A feline indication would require a veterinary drug submission pathway (e.g., Health Canada Veterinary Drugs Directorate), not the standard human DIN pathway; early regulatory consultation is recommended
- **Expanded literature search**: Search veterinary and comparative medicine databases (CAB Abstracts, VetMedResource, JAVMA) for published experience with nucleoside analogues in FIV-positive cats
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

