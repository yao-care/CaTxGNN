---
layout: default
title: Rilpivirine
parent: Model Prediction Only (L5)
nav_order: 808
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Rilpivirine: predicted new indication Simian immunodeficiency virus infection (evidence level L5). Approved use: HIV infectious disease"
monitor_inn: "RILPIVIRINE"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Rilpivirine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Rilpivirine: From HIV Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Rilpivirine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus infection**, a macaque model of HIV. Support is limited to **0 clinical trials** and **5 preclinical or review publications**. This is essentially a confirmation of the existing HIV indication, not a new human indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS (the Health Canada licence records contain no indication text) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 (preclinical studies only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, rilpivirine is an NNRTI that inhibits HIV-1 reverse transcriptase. Its efficacy in HIV infection is established, and it is marketed alone and in combination products in Canada.

Simian immunodeficiency virus (SIV) and chimeric SHIV infections in macaques are the standard preclinical surrogates for HIV. A prediction here is therefore expected, but it supports the original indication rather than a genuinely new one. SIV is naturally resistant to NNRTIs, so these models use SHIV carrying HIV reverse transcriptase. The macaque studies of long-acting rilpivirine with cabotegravir report sustained virologic suppression, remission after early treatment, and a low frequency of resistant variants. This is preclinical animal evidence, not a human repurposing indication.

The other predictions are weaker:
- **Feline acquired immunodeficiency syndrome**: only in vitro and structural comparisons of NNRTIs against feline immunodeficiency virus reverse transcriptase, which is generally less sensitive to NNRTIs. There are no clinical data in cats, and the relevance to human use is limited.
- **A rare neurodevelopmental disorder (ataxic gait, absent speech)**: no mechanistic link, no trials and no literature, so this is likely a graph artifact despite a score of 99.97%.
- **AIDS related complex** and **congenital HIV**: both overlap with the existing HIV indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top predicted indication.

(For the fifth-ranked prediction, congenital HIV, one completed Phase 4 trial is listed, [NCT04340388](https://clinicaltrials.gov/study/NCT04340388), with 10 participants. It studies dolutegravir and obesity or cardiovascular disease, not rilpivirine, and its relevance is low.)

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | Preclinical (macaque SHIV) | Nature Communications | Early treatment with long-acting cabotegravir/rilpivirine plus oral emtricitabine/tenofovir alafenamide was studied for SHIV remission in macaques |
| [26438501](https://pubmed.ncbi.nlm.nih.gov/26438501/) | 2015 | Preclinical (macaque) | Antimicrobial Agents and Chemotherapy | Long-acting rilpivirine selected drug-resistant variants at a low frequency in macaques infected with SIV containing HIV-1 reverse transcriptase |
| [41370971](https://pubmed.ncbi.nlm.nih.gov/41370971/) | 2026 | Preclinical (PEP model) | EBioMedicine | Evaluated whether a single injection of long-acting cabotegravir/rilpivirine could serve as post-exposure prophylaxis in macaques |
| [42040962](https://pubmed.ncbi.nlm.nih.gov/42040962/) | 2026 | Preclinical (macaque) | Research Square | Long-acting antiretrovirals (lenacapavir with cabotegravir) were studied in early-life SIV infection in newborn macaques; this is a preprint and rilpivirine is not the focus |
| [29746267](https://pubmed.ncbi.nlm.nih.gov/29746267/) | 2018 | Review | Current Opinion in HIV and AIDS | Review of cabotegravir for antiretroviral therapy and prevention; focused on cabotegravir rather than rilpivirine |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02370603 | EDURANT | Not specified | Not specified |
| 02497247 | CABENUVA | Not specified | Not specified |
| 02497220 | CABENUVA | Not specified | Not specified |
| 02475774 | JULUCA | Not specified | Not specified |
| 02374129 | COMPLERA | Not specified | Not specified |

A sixth authorization, ODEFSEY (DIN 02461463), is also valid.

---

## Safety Considerations

- **Contraindications recorded in the knowledge graph** (not taken from label text): long QT syndrome, familial long QT syndrome, torsades de pointes, liver failure, liver disease, fatty liver disease, non-alcoholic steatohepatitis, kidney disease, chronic hepatitis B virus infection, lactic acidosis, Fanconi renotubular syndrome, hypophosphatemia, osteomalacia, rickets, gallbladder disease, pyoureter, obesity disorder, monogenic obesity and pathologic fracture. Several of these probably reflect other components of combination products (for example tenofovir) rather than rilpivirine alone.
- **Drug interactions**: 100 interactions were found. The main **Major** interactions are acid-reducing agents (famotidine, ranitidine, cimetidine, omeprazole, esomeprazole, rabeprazole, dexlansoprazole), dexamethasone, and QT-related drugs (cisapride, dolasetron). **Moderate** interactions include clarithromycin, aprepitant, loperamide, antacids (aluminum hydroxide, calcium carbonate, magnesium oxide), clotrimazole, and several laxatives.
- **Pregnancy**: the literature on long-acting cabotegravir/rilpivirine in pregnancy includes a case report in which rilpivirine concentrations were 70–75% lower than in non-pregnant individuals, so monitoring is warranted.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is an animal model of HIV, the disease rilpivirine already treats, so it offers no new human indication. Evidence is preclinical only (L4) and there are no registered trials. The other predicted indications are either overlapping with HIV, veterinary, or unsupported.

**To proceed, the following is needed:**
- A clear human indication that differs from existing HIV approvals; none is currently identified
- Mechanism of action data
- Package insert warnings and contraindications from Health Canada, which are currently missing and block safety screening
- Product details (dosage form and approved indication text) for the Canadian licences
- A dedicated analysis of QT prolongation risk and the major interactions with acid-reducing agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

