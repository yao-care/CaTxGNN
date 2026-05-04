---
layout: default
title: Efavirenz
parent: 僅模型預測 (L5)
nav_order: 250
evidence_level: L5
indication_count: 3
---

# Efavirenz
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

# Efavirenz: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Efavirenz is a non-nucleoside reverse transcriptase inhibitor (NNRTI) widely used as a cornerstone component of combination antiretroviral therapy for HIV-1 infection in humans.
The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**,
with **1 clinical trial** (withdrawn, not directly relevant) and **16 publications**—primarily non-human primate studies using RT-SHIV chimeric models—currently available as supporting evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 Infection (standard NNRTI component of combination antiretroviral therapy) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L3 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Efavirenz inhibits HIV-1 reverse transcriptase (RT) by binding non-competitively to an allosteric pocket on the enzyme called the NNRTI binding pocket (NNIBP). This prevents RNA-to-DNA transcription and halts viral replication—a mechanism distinct from nucleoside analogues that work by competing at the active site. Because of this specificity for the HIV-1 RT structure, Efavirenz has long been a first-line treatment agent in combination regimens for HIV-1-infected adults.

SIV is the primate lentivirus most closely related to HIV and serves as a natural precursor to the human epidemic. However, wild-type SIV encodes its own RT, which differs significantly from HIV-1 RT in the NNIBP region—making native SIV largely insensitive to Efavirenz. The mechanistic rationale underpinning this prediction is therefore **indirect and model-specific**: researchers have created chimeric RT-SHIV viruses by replacing SIV's RT-coding region with that of HIV-1, yielding a primate-adapted model where NNRTIs including Efavirenz are pharmacologically active. The bulk of the literature evidence supporting this prediction derives from these RT-SHIV non-human primate (NHP) experiments in rhesus and pigtail macaques.

The TxGNN knowledge graph most likely captured shared disease-node relationships between HIV-1 and SIV infection, together with documented experimental use of Efavirenz within RT-SHIV macaque models. This makes the predicted link mechanistically coherent within that narrow experimental context—but it does **not** extend to wild-type SIV in natural primate hosts, substantially constraining real-world translational relevance.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | N/A | Withdrawn | 0 | Study of HIV RNA decay kinetics using Raltegravir (integrase inhibitor, not Efavirenz) in HIV-infected humans (not SIV). Withdrawn before enrolling any participants. |

> **Important caveat:** The single retrieved trial (NCT00863668) is not relevant to this repurposing hypothesis on three grounds: the study drug was Raltegravir (not Efavirenz), the disease was human HIV (not SIV), and the trial was withdrawn with zero enrollment. There are no valid clinical trials evaluating Efavirenz in SIV infection.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [15328115](https://pubmed.ncbi.nlm.nih.gov/15328115/) | 2004 | Animal Study (NHP) | Antimicrob Agents Chemother | First characterization of Efavirenz antiviral activity in rhesus macaques infected with RT-SHIV (SIV chimera carrying HIV-1 RT); established NNRTI proof-of-concept in this primate model |
| [15919889](https://pubmed.ncbi.nlm.nih.gov/15919889/) | 2005 | Animal Study (NHP) | J Virology | HAART regimen including Efavirenz 200 mg/day suppressed plasma viral RNA by >4 log in all 7 RT-SHIV-infected macaques, closely modeling human HIV treatment responses |
| [21084490](https://pubmed.ncbi.nlm.nih.gov/21084490/) | 2011 | Molecular Epidemiology | J Virology | SIV/HIV-1 genetic diversity persisted in macaques across Efavirenz monotherapy and subsequent combination ART; drug-resistant variants accumulated and were documented |
| [19889213](https://pubmed.ncbi.nlm.nih.gov/19889213/) | 2009 | Animal Study (NHP) | Retrovirology | Single-genome sequencing tracked RT-SHIV quasispecies dynamics in 3 pigtail macaques on Efavirenz monotherapy; documented real-time emergence and competitive dynamics of resistant clones |
| [35856680](https://pubmed.ncbi.nlm.nih.gov/35856680/) | 2022 | Translational/Imaging | Antimicrob Agents Chemother | Mass spectrometry imaging of 6 ARVs (including NNRTIs) in spleens of RT-SHIV-infected NHPs; revealed spatial relationship between drug penetration, viral RNA expression, and fibrosis |
| [22933296](https://pubmed.ncbi.nlm.nih.gov/22933296/) | 2012 | Virology/Molecular | J Virology | Ultrasensitive allele-specific PCR detected pre-existing NNRTI-resistant minority variants before Efavirenz initiation in RT-SHIV macaques, informing resistance emergence kinetics |
| [15564466](https://pubmed.ncbi.nlm.nih.gov/15564466/) | 2004 | In Vitro | J Virology | In vitro characterization confirmed RT-SHIV sensitivity to Efavirenz depends entirely on the presence of HIV-1 RT; wild-type SIV RT was not inhibited |
| [24777106](https://pubmed.ncbi.nlm.nih.gov/24777106/) | 2014 | Animal Study (NHP) | Antimicrob Agents Chemother | Four- and five-drug HAART combinations incorporating Efavirenz evaluated in RT-SHIV macaques; enhanced regimens produced faster early viral decay compared to three-drug HAART |
| [20032180](https://pubmed.ncbi.nlm.nih.gov/20032180/) | 2010 | Animal Study (NHP) | J Virology | Comprehensive mapping of viral sanctuary compartments during HAART in RT-SHIV macaques; identified tissues where Efavirenz-containing regimens could not fully suppress residual replication |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In Vitro | Antiviral Therapy | Susceptibility panel of HIV-2, wild-type SIV (mac251, B670), and SHIV strains against 16 antiretrovirals; Efavirenz showed negligible activity against wild-type SIV strains, confirming RT structural specificity |

---

## Canada Market Information

Efavirenz currently has **no registered Drug Identification Numbers (DINs) on file** in Canada based on the regulatory data available for this analysis. No licensed products or approved indications are recorded.

> Note: This finding warrants independent verification against the Health Canada Drug Product Database, as Efavirenz (brand name Sustiva®) has been approved in other major jurisdictions. A data retrieval gap cannot be excluded.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction linking Efavirenz to SIV infection is mechanistically plausible only within RT-SHIV chimeric animal models—where SIV is engineered to carry HIV-1 RT—and does not apply to wild-type SIV. The sole retrieved clinical trial was withdrawn and entirely irrelevant; all 16 literature citations are preclinical (NHP in vivo, in vitro, or molecular) studies. No human or veterinary clinical evidence exists, and Efavirenz's NNRTI mechanism is inherently HIV-1 RT–specific.

**To proceed, the following is needed:**

- **Clarify the clinical target:** Determine whether the intended application is (a) RT-SHIV as a research tool model, or (b) genuine treatment of SIV infection in non-human primates—these have very different feasibility profiles
- **Structural activity data:** Commission binding assays or in silico docking of Efavirenz against wild-type SIV-RT to quantify the activity gap relative to HIV-1 RT
- **MOA data retrieval:** Query the DrugBank API for Efavirenz's full mechanistic profile to support formal mechanistic link analysis
- **Safety data gap resolution:** Download and parse the Efavirenz package insert (Sustiva® or generic) to complete S1 safety screening (currently a blocking data gap)
- **Canada regulatory verification:** Cross-check Efavirenz DIN status against the Health Canada Drug Product Database to resolve the apparent discrepancy with its known international approval status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

