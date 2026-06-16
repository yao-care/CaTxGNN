---
layout: default
title: Emtricitabine
parent: 僅模型預測 (L5)
nav_order: 278
evidence_level: L5
indication_count: 3
---

# Emtricitabine
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

# Emtricitabine: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Emtricitabine (FTC) is a nucleoside reverse transcriptase inhibitor (NRTI) belonging to the antiretroviral drug class, established as a cornerstone agent in combination HIV-1 treatment regimens in humans.
The TxGNN model predicts it may be effective for **Feline Acquired Immunodeficiency Syndrome (FIV infection)**,
with **4 human-context clinical trials** (all indirect) and **1 veterinary preclinical study** currently supporting this direction.
Evidence is limited to the preclinical stage, and a Hold decision is recommended pending direct feline pharmacokinetic and efficacy data.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (antiretroviral background therapy; inferred from drug class; no Canada DIN on file) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV infection) |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 — Preclinical/veterinary study only |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack (DrugBank query returned no MOA record). Based on established pharmacological knowledge, emtricitabine is a cytidine analogue NRTI: it is phosphorylated intracellularly to emtricitabine-5′-triphosphate, which competitively inhibits the RNA-dependent DNA polymerase (reverse transcriptase, RT) of retroviruses and terminates nascent viral DNA chain elongation once incorporated. Its proven efficacy in human HIV-1 infection is mechanistically grounded in this RT inhibition.

Feline Immunodeficiency Virus (FIV) and HIV-1 are both lentiviruses within the *Retroviridae* family, both depending on RT for replication. FTC, as a deoxycytidine analogue, can terminate DNA chain extension by FIV RT in an analogous fashion. This makes the mechanistic extrapolation from HIV-1 to FIV biologically plausible. However, important caveats apply: the catalytic domain of FIV RT differs structurally from HIV-1 RT, and the drug resistance mutation landscape (e.g., equivalent of M184V) may not be fully conserved, meaning efficacy and resistance profiles cannot be directly assumed.

One 2023 veterinary study (PMID 37112803) directly tested cART including emtricitabine (40 mg/kg) combined with dolutegravir and tenofovir in FIV-infected domestic cats, providing the first direct pharmacokinetic and clinical outcome evidence in the target species. While this supports the biological premise, the dataset remains insufficient for regulatory or clinical translation without dedicated controlled feline trials.

---

## Clinical Trial Evidence

> **Note:** All retrieved clinical trials are human HIV-1 trials where emtricitabine was used as a background NRTI component, not primary investigational agent. No clinical trial directly evaluating emtricitabine for FIV (feline AIDS) was identified. These trials are included for context on emtricitabine's safety and use in retroviral infections.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | Dolutegravir vs. Raltegravir in ART-naïve HIV-1 adults; FTC used as background NRTI (TDF/FTC arm) over 96 weeks — establishes safety of FTC in long-term regimens |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Dose-selection study for dolutegravir with TDF/FTC or ABC/3TC backbones in HIV-1 ART-naïve adults — indirect support of FTC tolerability |
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | Dolutegravir + ABC/3TC vs. Efavirenz/FTC/TDF (Atripla) over 96 weeks in HIV-1 ART-naïve adults; FTC in comparator arm |
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | Completed | 145 | Boosted darunavir + lamivudine vs. boosted darunavir + FTC/TDF or 3TC/TDF in naïve HIV-1 patients — FTC as reference comparator |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Veterinary/Preclinical | *Viruses* | Evaluated cART (dolutegravir 2.5 mg/kg + tenofovir 20 mg/kg + **emtricitabine 40 mg/kg**) pharmacokinetics and clinical outcomes in FIV-infected domestic cats; first direct evidence of FTC use in the target species |

---

## Canada Market Information

Emtricitabine currently has **no approved Drug Identification Numbers (DINs) in Canada** and is not marketed as a standalone product under this Evidence Pack. No license table can be generated.

> Emtricitabine is available in Canada as part of fixed-dose combination products (e.g., Truvada, Descovy, Biktarvy), but no standalone DIN data was captured in this evidence pack. Refer to Health Canada's Drug Product Database for current status of combination products.

---

## Safety Considerations

No structured safety data was available in this Evidence Pack (TFDA/Health Canada package insert warnings, contraindications, and drug interaction records all returned as data gaps).

> Please refer to the package insert for safety information. Key areas to review include: renal toxicity (when used with tenofovir), hepatic flare risk upon discontinuation in HBV co-infected patients, and lactic acidosis risk common to the NRTI class.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic analogy between FIV and HIV-1 is biologically sound, and one 2023 preclinical veterinary study has directly evaluated emtricitabine-containing cART in FIV-infected cats with reported pharmacokinetic data. However, evidence remains at the L4 preclinical level with no controlled feline efficacy trial, no approved veterinary formulation, and no Canada regulatory pathway — insufficient to advance without further foundational data.

**To proceed, the following is needed:**

- **Pharmacokinetic data in cats**: Confirm adequate plasma/intracellular drug exposure at proposed doses (40 mg/kg per the 2023 study vs. human 200 mg/day equivalent); formal PK/PD modelling for FIV RT inhibition
- **Controlled feline efficacy study**: Randomized trial in FIV-infected cats measuring viral load suppression, CD4+ T cell recovery, and clinical outcome scores
- **FIV RT inhibition assays**: Biochemical confirmation that emtricitabine-triphosphate inhibits FIV RT with acceptable Ki values; characterize FIV M184-equivalent resistance mutation emergence
- **Veterinary safety profile**: Identify species-specific toxicities (feline cytidine deaminase activity differs from humans); rule out myelosuppression and renal concerns in cats
- **Regulatory pathway**: Determine whether a Canadian veterinary drug submission (Health Canada HVDD) or off-label use framework applies; assess availability of oral formulation suitable for feline dosing
- **Full safety data gap resolution**: Obtain emtricitabine package insert (human) warnings and contraindications to complete S1 safety screen before any veterinary trial design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

