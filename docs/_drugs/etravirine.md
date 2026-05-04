---
layout: default
title: Etravirine
parent: 僅模型預測 (L5)
nav_order: 277
evidence_level: L5
indication_count: 10
---

# Etravirine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Etravirine: From HIV-1 Infection to Friedreich Ataxia

## One-Sentence Summary

Etravirine (Intelence®) is a second-generation non-nucleoside reverse transcriptase inhibitor (NNRTI) approved globally for the treatment of HIV-1 infection in treatment-experienced patients, including children from 2 years of age. The TxGNN model identifies **Friedreich Ataxia** — a rare, progressive neurodegenerative disease caused by frataxin protein deficiency — as the most clinically actionable repurposing target, supported by **1 completed Phase 2 clinical trial** (NCT04273165, n=30) and compelling preclinical mechanistic evidence showing frataxin protein upregulation in disease-relevant cell and animal models. Among the 10 TxGNN-predicted indications reviewed, Friedreich Ataxia is the only genuine non-HIV repurposing candidate with human trial data and a biologically coherent cross-indication mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (treatment-experienced adults and children ≥2 years) |
| Predicted New Indication | Friedreich Ataxia (neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on prediction landscape**: The two highest-ranked TxGNN predictions (rank 1: feline acquired immunodeficiency syndrome; rank 2: simian immunodeficiency virus infection) are veterinary and non-human primate conditions with no clinical evidence, likely reflecting topological clustering of immunodeficiency nodes in the knowledge graph rather than pharmacological relevance. Ranks 4–5 (congenital HIV, AIDS-related complex) are clinical extensions of the original approved HIV indication, not true repurposing. Ranks 6–10 (fibroma of prostate, Brenner tumor, benign reproductive neoplasms, obsolete hyperlipidemia) score high due to graph topology artifacts with no biological rationale. **Friedreich Ataxia (rank 3)** is selected as the primary focus because it is the only prediction with genuine cross-disease repurposing potential, human trial evidence, and mechanistic specificity.

---

## Why is This Prediction Reasonable?

Etravirine is a diarylpyrimidine (DAPY)-class NNRTI that binds HIV-1 reverse transcriptase in a uniquely flexible, adaptive conformation — often described as "wiggling and jiggling" — which enables it to overcome many mutations that confer resistance to first-generation NNRTIs. While its primary antiviral mechanism is inhibition of viral reverse transcriptase, emerging evidence suggests etravirine may also suppress endogenous retrotransposon activity (particularly LINE-1 elements) and modulate epigenetic regulatory pathways. These secondary mechanisms are completely independent of antiviral activity and may influence gene expression in disease contexts unrelated to viral infection.

Friedreich Ataxia (FRDA) is a rare autosomal recessive disease caused by GAA trinucleotide repeat expansions in intron 1 of the *FXN* gene, which silences transcription and leads to frataxin protein deficiency. Frataxin is essential for mitochondrial iron-sulfur cluster assembly; its loss drives progressive spinocerebellar neurodegeneration, hypertrophic cardiomyopathy, and sensory neuropathy. With very limited disease-modifying treatment options available, FRDA represents a high-priority unmet medical need. Preclinical studies found that etravirine increases frataxin protein expression in FRDA patient-derived iPSCs and in the heart and skeletal muscle of YG8 frataxin-deficient mice — an effect independent of its antiviral properties and possibly mediated through LINE-1 retrotransposon suppression or epigenetic de-repression of the *FXN* locus.

The translational conviction behind this hypothesis is evidenced by the initiation and completion of NCT04273165, a purpose-built Phase 2 clinical trial testing etravirine in FRDA patients (September 2020 – January 2023, n=30). Etravirine's established oral bioavailability, pediatric-approved dosing, and broadly characterized safety profile further support the feasibility of repurposing it for a genetic pediatric neurological disease.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04273165](https://clinicaltrials.gov/study/NCT04273165) | Phase 2 | Completed | 30 | Dedicated drug repurposing trial evaluating etravirine in Friedreich Ataxia patients (Sept 2020 – Jan 2023). Scientific basis: etravirine increases frataxin protein in patient-derived iPSCs *in vitro* and in heart/skeletal muscle of YG8 frataxin-deficient mice *in vivo*. Primary results publication status pending at data cutoff (2026-04-20). |

---

## Literature Evidence

Currently no related literature specifically linking etravirine to Friedreich Ataxia is available in this Evidence Pack.

> NCT04273165 completed in January 2023; primary results and any associated publications may have been released after the evidence collection date or may be in press. The preclinical frataxin-upregulation data (in iPSCs and YG8 mice) constitutes the mechanistic foundation for the trial but the relevant primary publications were not captured in the current PubMed query.

---

## Canada Market Information

Etravirine is not currently marketed in Canada. Health Canada has issued no Drug Identification Numbers (DINs).

| Item | Detail |
|------|------|
| Health Canada Status | Not marketed |
| Total DINs | 0 |
| Global Reference | Approved as **Intelence®** by the US FDA (January 2008) and EMA for HIV-1 treatment in adults and children ≥2 years. Available as 25 mg, 100 mg, and 200 mg tablets. |

For any Canadian repurposing initiative, a full regulatory submission to Health Canada would be required, with potential eligibility for Priority Review or Rare Disease designation (FRDA prevalence ~1–2/50,000).

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Data gaps**: Canadian labeling warnings and contraindications were not available in this Evidence Pack (Data Gap DG001, Blocking severity). Mechanism of action data was also not retrieved from DrugBank at time of report generation (Data Gap DG002, High severity). Based on the internationally approved Intelence® product monograph, clinicians should note: etravirine is a substrate and inducer of CYP3A4 and an inhibitor of CYP2C9/CYP2C19, creating a complex drug-drug interaction profile that requires careful evaluation in FRDA patients who may be taking antifungals, anticonvulsants, or other CYP-sensitive agents. Skin reactions (including rare cases of Stevens-Johnson syndrome) and hepatic adverse events have been reported in HIV populations. The safety profile in a non-HIV FRDA population without background antiretroviral co-medications has not been systematically characterized.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 clinical trial (NCT04273165) combined with coherent preclinical mechanistic data (frataxin upregulation in FRDA iPSCs and YG8 mice) provides sufficient translational basis to advance further evaluation. The unmet medical need in Friedreich Ataxia is substantial, and etravirine's established pediatric-approved safety record offers a practical development pathway.

**To proceed, the following is needed:**
- Obtain and critically review the published or pre-print results from NCT04273165, including primary endpoints (frataxin levels, neurological function scales), safety data in the FRDA population, and any dose-response signal
- Retrieve full MOA and pharmacology data from DrugBank (DB06414) to formally characterize the frataxin-upregulation mechanism and distinguish it from antiviral activity (remediate DG002)
- Download and parse the Intelence® product monograph from the FDA/EMA to complete the safety profile assessment (remediate DG001)
- Conduct a comprehensive CYP2C9/2C19/3A4 drug interaction analysis relevant to typical FRDA patient co-medications
- Assess orphan drug designation eligibility with Health Canada for FRDA
- If Phase 2 results demonstrate frataxin upregulation and acceptable tolerability, design a Phase 2b/3 trial with frataxin protein level and validated ataxia functional scales (e.g., mFARS) as co-primary endpoints

---

> **Additional note on HIV-adjacent predictions**: The congenital HIV prediction (rank 4, L1 evidence — multiple completed Phase 3 RCTs) represents a high-quality, well-evidenced clinical application. However, this is best characterized as a **population-specific extension** of the original HIV-1 indication (vertical transmission, pregnancy PK) rather than true drug repurposing. If a separate report is needed for etravirine in perinatal HIV management, the evidence base (including NCT00042289 pregnancy PK data and NCT00855335 DRV+ETR pregnancy PK) would support a **Go** decision with PK monitoring guardrails.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

