---
layout: default
title: Glecaprevir
parent: 僅模型預測 (L5)
nav_order: 365
evidence_level: L5
indication_count: 10
---

# Glecaprevir
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

# Glecaprevir: From Chronic Hepatitis C to HIV Infectious Disease

## One-Sentence Summary

Glecaprevir is an HCV NS3/4A serine protease inhibitor, marketed internationally in combination with pibrentasvir (Mavyret) for the treatment of chronic hepatitis C virus (HCV) infection across all genotypes.
The TxGNN model predicts it may be effective for **HIV Infectious Disease**, with **15 clinical trials** and **20 publications** currently identified — however, critical examination reveals that this evidence reflects GLE/PIB use in HIV/HCV co-infected patients being treated **for HCV**, not for HIV, meaning the model prediction lacks direct mechanistic or clinical support.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic Hepatitis C Virus (HCV) Infection — international regulatory approval; no Canadian DIN on file |
| Predicted New Indication | HIV Infectious Disease |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Canada Market Status | Not marketed (未上市) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on published clinical literature, Glecaprevir is an **NS3/4A serine protease inhibitor** that blocks the processing of the HCV polyprotein — a step essential for viral replication. Formulated as a fixed-dose combination with pibrentasvir (an NS5A inhibitor) under the brand name Mavyret, GLE/PIB has demonstrated SVR12 rates above 97% across HCV genotypes 1–6 in multiple Phase 3 trials.

The TxGNN model's HIV prediction, despite its high score (99.87%), faces a fundamental mechanistic obstacle. HIV-1 replication depends on an **aspartyl protease** — the target of established antiretroviral drugs such as darunavir and lopinavir — which belongs to a completely different enzyme family from the **serine protease** targeted by Glecaprevir. These two enzyme classes differ in their catalytic residues, active site architecture, and three-dimensional binding pockets. There is no known cross-inhibition activity, and no in vitro data suggesting GLE binds to any HIV replication target.

The 15 clinical trials and 20 publications identified through evidence retrieval are **not evidence of HIV repurposing**. They predominantly represent research conducted in HIV/HCV co-infected populations, where HIV-positive patients received GLE/PIB specifically to cure their hepatitis C (EXPEDITION-2 series). All primary endpoints measured HCV virologic cure (SVR12); HIV viral load or CD4 count improvement were not study objectives. Any observed indirect health benefit — such as improved cardiovascular outcomes after HCV clearance — reflects downstream effects of HCV cure rather than direct anti-HIV activity, and does not constitute repurposing evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02738138](https://clinicaltrials.gov/study/NCT02738138) | Phase 3 | Completed | 153 | EXPEDITION-2: GLE/PIB in adults with chronic HCV genotypes 1–6 and HIV-1 co-infection; primary endpoint was HCV SVR12, not HIV outcomes |
| [NCT04042740](https://clinicaltrials.gov/study/NCT04042740) | Phase 2 | Completed | 45 | PURGE-C: 4-week GLE/PIB for acute HCV with or without HIV-1 co-infection; endpoint was HCV SVR — HIV co-infection was a background characteristic |
| [NCT03235349](https://clinicaltrials.gov/study/NCT03235349) | Phase 3 | Completed | 160 | GLE/PIB in Asian adults with compensated cirrhosis with or without HIV co-infection; primary endpoint HCV SVR12 |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular risk outcomes in HIV/HCV co-infected individuals after HCV eradication; measures indirect benefit of HCV cure, not anti-HIV activity |
| [NCT03222583](https://clinicaltrials.gov/study/NCT03222583) | Phase 3 | Completed | 546 | GLE/PIB in non-cirrhotic Asian adults with HCV genotypes 1–6, with or without HIV co-infection; primary endpoint HCV SVR12 |
| [NCT02939989](https://clinicaltrials.gov/study/NCT02939989) | Phase 3 | Completed | 33 | MAGELLAN-3: GLE/PIB + sofosbuvir + ribavirin in participants with prior AbbVie trial virologic failure, including HIV/HCV co-infected subgroup |
| [NCT07040319](https://clinicaltrials.gov/study/NCT07040319) | Phase 1/2 | Not Yet Recruiting | 30 | PK and safety of GLE/PIB initiated during pregnancy in women with HCV with and without HIV |
| [NCT04352309](https://clinicaltrials.gov/study/NCT04352309) | N/A | Completed | 99 | EASY: Real-world 8-week GLE/PIB in HCV cirrhosis patients in Russia; HIV co-infection a minor secondary subgroup |
| [NCT04577482](https://clinicaltrials.gov/study/NCT04577482) | N/A | Completed | 42 | CHOICE: Real-world GLE/PIB in DAA-experienced HCV genotype 1 patients in Russia; HCV effectiveness study |
| [NCT05108935](https://clinicaltrials.gov/study/NCT05108935) | NA | Completed | 17 | Telemedicine program providing HIV PrEP, MOUD, and HCV treatment at syringe service programs; not a drug efficacy study |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37671831](https://pubmed.ncbi.nlm.nih.gov/37671831/) | 2023 | Real-world Cohort | J Antimicrobial Chemotherapy | GLE/PIB real-world response in HIV/HCV co-infected patients in clinical practice — HCV SVR endpoints, not HIV viral outcomes; notes limited data outside clinical trials |
| [31504702](https://pubmed.ncbi.nlm.nih.gov/31504702/) | 2020 | DDI Study | J Infectious Diseases | Pharmacokinetic assessment of GLE/PIB co-administered with HIV antiretrovirals; identifies compatible and incompatible ART combinations |
| [36415300](https://pubmed.ncbi.nlm.nih.gov/36415300/) | 2022 | Case Report | J Prev Med Hygiene | Indirect hyperbilirubinemia and jaundice in HIV-infected patient on GLE/PIB + ART — first reported case in Italy; highlights drug monitoring needs |
| [34664197](https://pubmed.ncbi.nlm.nih.gov/34664197/) | 2021 | Case Report | Clin J Gastroenterology | Successful HCV genotype 4a treatment with GLE/PIB in Japanese patient with HIV/hemophilia co-infection; endpoint was HCV clearance |
| [31284039](https://pubmed.ncbi.nlm.nih.gov/31284039/) | 2019 | Meta-analysis | Int J Antimicrobial Agents | Systematic review of GLE/PIB in HCV genotypes 1–6 (13 studies, n=3,082); overall SVR12 rate 97.8% — establishes HCV efficacy baseline |
| [29845496](https://pubmed.ncbi.nlm.nih.gov/29845496/) | 2018 | Drug Economics | Hepatology International | GLE/PIB as pangenotypic DAA — expands HCV treatment reach while reducing cost and treatment duration versus prior regimens |
| [29595065](https://pubmed.ncbi.nlm.nih.gov/29595065/) | 2018 | Review | Expert Opin Pharmacotherapy | HCV protease inhibitor review; notes 25–30% of HIV patients in Europe/US are HCV co-infected, providing context for co-infection data |
| [35877601](https://pubmed.ncbi.nlm.nih.gov/35877601/) | 2022 | Policy Analysis | PLoS ONE | Comparison of drug approval timelines for TB, HIV, and HCV; contextual background on drug development ecosystems |
| [30671330](https://pubmed.ncbi.nlm.nih.gov/30671330/) | 2017 | Review | GMS Infect Dis | Protease inhibitors for HCV — mechanistic and clinical overview noting high SVR rates in HIV/HCV co-infected patients with DAA regimens |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Conference Report | AIDS Reviews | International Conference on Viral Hepatitis 2017 — overview of pan-genotypic DAA therapies including GLE/PIB in co-infected populations |

## Canada Market Information

Glecaprevir is currently **not registered in Canada**. No Drug Identification Numbers (DINs) are on file with Health Canada, and there are no approved product licences for any dosage form.

> Mavyret (glecaprevir/pibrentasvir) has received regulatory approval in the United States (FDA, August 2017), the European Union (EMA, July 2017), Japan, Taiwan, and numerous other jurisdictions for chronic HCV genotypes 1–6. Canadian Health Canada approval status should be confirmed directly via the Health Canada Drug Product Database.

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for reviewers**: Based on FDA Mavyret labelling, the following safety signals are known internationally: (1) **Black box warning** — risk of hepatitis B virus (HBV) reactivation in HCV/HBV co-infected patients; (2) drug-drug interactions with atazanavir (contraindicated), rifampin, carbamazepine, and other strong P-gp/CYP3A inducers; (3) hepatic decompensation risk in patients with Child-Pugh B/C cirrhosis. These should be formally confirmed from the Canadian product monograph once available (Data Gap DG001).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's prediction of HIV as a new indication for Glecaprevir is mechanistically implausible — GLE targets the HCV NS3/4A serine protease, an enzyme class with no functional equivalent in HIV replication (which depends on an aspartyl protease). All 15 identified clinical trials and 20 publications reflect HCV treatment in HIV/HCV co-infected populations, not evidence of anti-HIV activity. Furthermore, Glecaprevir is not registered in Canada, making any near-term clinical development pathway in this jurisdiction doubly challenging.

**To proceed, the following is needed:**

- In vitro binding or inhibition data demonstrating GLE activity against any HIV target (HIV protease, reverse transcriptase, integrase, or envelope entry machinery)
- A mechanistically coherent hypothesis linking HCV NS3/4A serine protease inhibition to HIV biology
- Retrieval of TFDA/Health Canada package insert for complete safety and contraindication data (Data Gap DG001 — currently Blocking severity)
- DrugBank MOA data retrieval (Data Gap DG002 — currently High severity)
- If a novel mechanism is identified, Health Canada registration for the Canadian indication would need to precede any local clinical development
- Should any in vitro signal emerge, a Phase 1 safety/PK study specifically in HIV-mono-infected patients (without HCV co-infection) would be the first required step before efficacy testing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

