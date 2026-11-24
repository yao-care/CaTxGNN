---
layout: default
title: Emtricitabine
parent: Model Prediction Only (L5)
nav_order: 327
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
description: "Emtricitabine: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infectious disease"
monitor_inn: "EMTRICITABINE"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Emtricitabine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Emtricitabine: From HIV Infection to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Emtricitabine is a nucleoside reverse transcriptase inhibitor originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (FIV)**,
but there are **0 clinical trials** and only **1 publication** (a veterinary study whose design could not be verified) behind this top-ranked prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs on record: at least 20) |
| Number of DINs | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for emtricitabine: "Emtricitabine is an antiretroviral drug. […] FTC, a synthetic nucleoside analog of cytidine, is phosphorylated by cellular enzymes to form emtricitabine 5'-triphosphate (FTC-TP), which inhibits the activity of the HIV-1 reverse transcriptase (RT) by competing with the natural substrate deoxycytidine 5'-triphosphate and by being incorporated into nascent viral DNA resulting in chain termination. FTC-TP is a weak inhibitor of mammalian DNA polymerases α, β, ε, and mitochondrial DNA polymerase γ." ([DailyMed: Emtriva (emtricitabine) prescribing information, Gilead Sciences, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d6599395-3944-44f9-97f2-e0424c6b6a1f), label version 2026-11-06; accessed 2026-11-19.) Based on known information, emtricitabine is a nucleoside reverse transcriptase inhibitor (NRTI), and its efficacy in HIV-1 infection is established. Mechanistically, it may be applicable to feline immunodeficiency virus.

FIV is a lentivirus related to HIV. It causes progressive immune dysfunction in cats, much like HIV in humans, and it also depends on reverse transcriptase to replicate. NRTI activity against it is therefore biologically plausible.

The very high TxGNN score (0.9992) mostly reflects how similar this disease is to HIV, not independent clinical evidence. This prediction is also veterinary, so it is not a new human indication.

The second-ranked prediction, simian immunodeficiency virus (SIV) infection, has more supporting literature. These are mostly macaque studies in which emtricitabine, usually combined with tenofovir, prevented or suppressed SHIV infection. They validate the existing HIV mechanism in animal models rather than opening a new human indication. The third-ranked prediction, a rare neurodevelopmental disorder with ataxic gait, absent speech and decreased cortical white matter, has no plausible mechanistic link, no trials and no literature. It should be treated as a likely false positive.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

For the top-ranked prediction (FIV):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Preclinical/veterinary study (design not verified) | Viruses | Evaluated pharmacokinetics and clinical outcomes of combination antiretroviral therapy (dolutegravir, tenofovir, emtricitabine) in FIV-infected domestic cats |

For the second-ranked prediction (SIV infection), selected preclinical publications:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Preclinical animal study | J Infect Dis | Oral emtricitabine/tenofovir alafenamide protected macaques from rectal SHIV infection |
| [31362305](https://pubmed.ncbi.nlm.nih.gov/31362305/) | 2019 | Preclinical animal study | J Infect Dis | Oral TAF/emtricitabine or TAF alone tested against vaginal SHIV infection in macaques |
| [26743846](https://pubmed.ncbi.nlm.nih.gov/26743846/) | 2016 | Preclinical animal study | J Infect Dis | Emtricitabine/TDF prevented vaginal SHIV infection in macaques with Chlamydia and Trichomonas coinfection |
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | Preclinical animal study | Nat Commun | Early treatment with emtricitabine/TAF plus long-acting cabotegravir/rilpivirine achieved SHIV remission in macaques |
| [24914761](https://pubmed.ncbi.nlm.nih.gov/24914761/) | 2014 | Preclinical animal study | AIDS Res Hum Retroviruses | HIV vaccine combined with partially protective oral PrEP prevented SHIV infection in macaques |
| [12021341](https://pubmed.ncbi.nlm.nih.gov/12021341/) | 2002 | Preclinical virology study | J Virol | M184V resistance mutation emerged within 5 weeks of lamivudine or emtricitabine treatment in SIV-infected newborn macaques, with reduced viral fitness |
| [22964889](https://pubmed.ncbi.nlm.nih.gov/22964889/) | 2012 | Review | Curr Opin HIV AIDS | Lessons from animal models of antiretroviral PrEP |
| [20874040](https://pubmed.ncbi.nlm.nih.gov/20874040/) | 2010 | Review | Pharmacotherapy | Review of systemic pre-exposure prophylaxis for HIV |
| [22918448](https://pubmed.ncbi.nlm.nih.gov/22918448/) | 2012 | Review/Commentary | Curr Opin HIV AIDS | Considerations for antiretroviral chemoprophylaxis in men who have sex with men |
| [22814162](https://pubmed.ncbi.nlm.nih.gov/22814162/) | 2012 | Preclinical animal study | Jpn J Infect Dis | Double oral dose of emtricitabine/tenofovir before exposure protected macaques against highly pathogenic SHIV |

---

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02274906 | TRUVADA | EMTRICITABINE; TENOFOVIR DISOPROXIL FUMARATE | Marketed |
| 02374129 | COMPLERA | EMTRICITABINE; RILPIVIRINE (RILPIVIRINE HYDROCHLORIDE); TENOFOVIR DISOPROXIL FUMARATE | Marketed |
| 02393549 | TEVA-EFAVIRENZ/EMTRICITABINE/TENOFOVIR | EFAVIRENZ; EMTRICITABINE; TENOFOVIR DISOPROXIL FUMARATE | Marketed |
| 02399059 | TEVA-EMTRICITABINE/TENOFOVIR | EMTRICITABINE; TENOFOVIR DISOPROXIL FUMARATE | Marketed |
| 02443902 | MYLAN-EMTRICITABINE/TENOFOVIR DISOPROXIL | EMTRICITABINE; TENOFOVIR DISOPROXIL FUMARATE | Marketed |
| 02452006 | APO-EMTRICITABINE-TENOFOVIR | EMTRICITABINE; TENOFOVIR DISOPROXIL FUMARATE | Marketed |
| 02454416 | DESCOVY | EMTRICITABINE; TENOFOVIR ALAFENAMIDE (TENOFOVIR ALAFENAMIDE HEMIFUMARATE) | Marketed |
| 02454424 | DESCOVY | EMTRICITABINE; TENOFOVIR ALAFENAMIDE (TENOFOVIR ALAFENAMIDE HEMIFUMARATE) | Marketed |
| 02461110 | PMS-EMTRICITABINE-TENOFOVIR | EMTRICITABINE; TENOFOVIR DISOPROXIL FUMARATE | Marketed |
| 02461412 | MYLAN-EFAVIRENZ/EMTRICITABINE/TENOFOVIR DISOPROXIL FUMARATE | EFAVIRENZ; EMTRICITABINE; TENOFOVIR DISOPROXIL FUMARATE | Marketed |
| 02461463 | ODEFSEY | EMTRICITABINE; RILPIVIRINE (RILPIVIRINE HYDROCHLORIDE); TENOFOVIR ALAFENAMIDE (TENOFOVIR ALAFENAMIDE HEMIFUMA… | Marketed |
| 02468247 | APO-EFAVIRENZ-EMTRICITABINE-TENOFOVIR | EFAVIRENZ; EMTRICITABINE; TENOFOVIR DISOPROXIL FUMARATE | Marketed |
| 02473720 | SYMTUZA | COBICISTAT; DARUNAVIR (DARUNAVIR ETHANOLATE); EMTRICITABINE; TENOFOVIR ALAFENAMIDE (TENOFOVIR ALAFENAMIDE HEM… | Marketed |
| 02478404 | AURO-EFAVIRENZ-EMTRICITABINE-TENOFOVIR | EFAVIRENZ; EMTRICITABINE; TENOFOVIR DISOPROXIL FUMARATE | Marketed |
| 02478579 | BIKTARVY | BICTEGRAVIR (BICTEGRAVIR SODIUM); EMTRICITABINE; TENOFOVIR ALAFENAMIDE (TENOFOVIR ALAFENAMIDE HEMIFUMARATE) | Marketed |
| 02487012 | JAMP EMTRICITABINE/TENOFOVIR DISOPROXIL FUMARATE | EMTRICITABINE; TENOFOVIR DISOPROXIL FUMARATE | Marketed |
| 02490684 | AURO-EMTRICITABINE-TENOFOVIR | EMTRICITABINE; TENOFOVIR DISOPROXIL FUMARATE | Marketed |
| 02496356 | AG-EMTRICITABINE / TENOFOVIR DISOPROXIL FUMARATE | EMTRICITABINE; TENOFOVIR DISOPROXIL FUMARATE | Marketed |
| 02519461 | JAMP EFAVIRENZ/EMTRICITABINE/TENOFOVIR DISOPROXIL FUMARATE | EFAVIRENZ; EMTRICITABINE; TENOFOVIR DISOPROXIL FUMARATE | Marketed |
| 02521547 | MINT-EMTRICITABINE/TENOFOVIR | EMTRICITABINE; TENOFOVIR DISOPROXIL FUMARATE | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

The data contain only part of the DINs for this ingredient; the list may be incomplete.

<!-- licenses:end -->

All 20 licences are valid. Many are generic emtricitabine/tenofovir or efavirenz/emtricitabine/tenofovir combination products.

---

## Safety Considerations

**Contraindication signals from the knowledge graph (not label text):** these include liver failure, liver disease, kidney disease, chronic hepatitis B and C virus infection, lactic acidosis, Fanconi renotubular syndrome, hypophosphatemia, osteomalacia, rickets, long QT syndrome and torsades de pointes, fatty liver disease, non-alcoholic steatohepatitis, hypertriglyceridemia, epilepsy, and several psychiatric conditions (anxiety, dysthymic, delusional disorders, paranoid schizophrenia). Several of these probably come from combination partner drugs, so they should be verified against the package insert.

**Drug Interactions (20 recorded):**
- **Major:** leflunomide, teriflunomide
- **Moderate:** orlistat, naltrexone, cobicistat, asparaginase, interferon beta-1a/1b, peginterferon beta-1a, brentuximab vedotin, cabozantinib, cladribine, clofarabine, epirubicin, idelalisib, methotrexate, pegaspargase, tioguanine, trabectedin
- **Minor:** eribulin

Package insert warnings and contraindications from Health Canada were not available, so please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (FIV) is veterinary and rests on a single study of unverified design, with no clinical trials. The SIV evidence is solid but preclinical, and it supports the existing HIV indication rather than a new human one. The third prediction has no supporting evidence at all.

**To proceed, the following is needed:**
- Mechanism of action data for emtricitabine
- Health Canada package insert warnings and contraindications
- Verification of the FIV study's design and outcomes, and a decision on whether a veterinary indication is within scope
- A plausible biological rationale for the neurodevelopmental disorder prediction, or its removal as a likely false positive
- If a human indication is the goal, a review of other predicted indications beyond these top three

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Emtriva (emtricitabine) prescribing information, Gilead Sciences, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d6599395-3944-44f9-97f2-e0424c6b6a1f) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

