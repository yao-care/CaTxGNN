---
layout: default
title: Glecaprevir
parent: Model Prediction Only (L5)
nav_order: 433
evidence_level: L5
indication_count: 10
---

# Glecaprevir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Glecaprevir: From Chronic Hepatitis C Virus Infection to HIV Infectious Disease

## One-Sentence Summary

Glecaprevir is a hepatitis C virus (HCV) NS3/4A protease inhibitor, originally used to treat chronic hepatitis C infection (marketed in Canada as MAVIRET).
The TxGNN model predicts it may be effective for **HIV infectious disease**, but the trials identified (**6 clinical trials** and **20 publications**) test HCV cure in patients who also have HIV, not treatment of HIV itself.
The evidence therefore supports the drug's original HCV use, even in HIV-coinfected patients, rather than a true new HIV indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C virus infection |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 (the Phase 3 trials are HCV studies in HIV-coinfected patients and do not test HIV treatment, so direct evidence for the new indication is lacking) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, glecaprevir is an NS3/4A protease inhibitor used with pibrentasvir (an NS5A inhibitor) for HCV, and its efficacy in HCV is well established.

The prediction is not supported mechanistically. Glecaprevir has no known direct anti-HIV activity. HIV uses an aspartyl protease, which is structurally and mechanistically different from the HCV NS3/4A serine protease. The high TxGNN score most likely reflects the frequent HIV/HCV comorbidity link in the knowledge graph rather than a true antiviral effect on HIV.

The trials listed below enroll HIV/HCV-coinfected patients, but their endpoint is HCV cure (sustained virologic response). They show that glecaprevir/pibrentasvir works for HCV in the presence of HIV, including drug-interaction considerations with antiretrovirals. They do not show treatment of HIV.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02738138](https://clinicaltrials.gov/study/NCT02738138) | Phase 3 | Completed | 153 | EXPEDITION-2: glecaprevir/pibrentasvir in adults with HCV genotype 1-6 and HIV-1 coinfection; HCV cure is the endpoint |
| [NCT03222583](https://clinicaltrials.gov/study/NCT03222583) | Phase 3 | Completed | 546 | Randomized, placebo-controlled study in non-cirrhotic Asian adults with HCV genotype 1-6, with or without HIV coinfection |
| [NCT03235349](https://clinicaltrials.gov/study/NCT03235349) | Phase 3 | Completed | 160 | Open-label study in Asian adults with HCV and compensated cirrhosis, with or without HIV coinfection |
| [NCT02634008](https://clinicaltrials.gov/study/NCT02634008) | Phase 3 | Completed | 83 | Pilot study of DAA regimens, including glecaprevir/pibrentasvir, in recently acquired HCV with or without HIV; the glecaprevir link is uncertain because the regimen also includes paritaprevir |
| [NCT04042740](https://clinicaltrials.gov/study/NCT04042740) | Phase 2 | Completed | 45 | PURGE-C: 4-week glecaprevir/pibrentasvir in acute HCV, with or without HIV-1 coinfection |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular risk outcomes after HCV eradication in HCV mono-infected and HIV/HCV-coinfected people |
| [NCT07040319](https://clinicaltrials.gov/study/NCT07040319) | Phase 1/2 | Recruiting | 30 | Pharmacokinetics and safety of glecaprevir/pibrentasvir started in pregnancy in women with HCV, with or without HIV |

All of these trials target HCV outcomes. None tests HIV efficacy.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37671831](https://pubmed.ncbi.nlm.nih.gov/37671831/) | 2023 | Cohort | J Antimicrob Chemother | Real-world response to glecaprevir/pibrentasvir in HIV/HCV-coinfected patients |
| [39697370](https://pubmed.ncbi.nlm.nih.gov/39697370/) | 2024 | Cohort | Clin Exp Hepatol | Effectiveness and safety of glecaprevir/pibrentasvir in HIV/HCV patients on bictegravir/emtricitabine/tenofovir alafenamide |
| [41297677](https://pubmed.ncbi.nlm.nih.gov/41297677/) | 2026 | Phase 3b single-arm trial | J Hepatol | 8-week glecaprevir/pibrentasvir in adults with acute HCV |
| [32754824](https://pubmed.ncbi.nlm.nih.gov/32754824/) | 2020 | Cohort | Adv Ther | Real-world 8-week glecaprevir/pibrentasvir in treatment-naïve patients with compensated cirrhosis |
| [31504702](https://pubmed.ncbi.nlm.nih.gov/31504702/) | 2020 | Pharmacokinetic study | J Infect Dis | Drug-drug interactions of glecaprevir/pibrentasvir with HIV antiretrovirals |
| [31284039](https://pubmed.ncbi.nlm.nih.gov/31284039/) | 2019 | Systematic review/meta-analysis | Int J Antimicrob Agents | 13 studies, 3,082 patients; pooled SVR12 of 97.8% for HCV |
| [30499343](https://pubmed.ncbi.nlm.nih.gov/30499343/) | 2019 | Review | Future Microbiol | Review of glecaprevir/pibrentasvir for chronic HCV |
| [29595065](https://pubmed.ncbi.nlm.nih.gov/29595065/) | 2018 | Review | Expert Opin Pharmacother | Protease inhibitor therapy for HCV; notes 25-30% of HIV patients in Europe and the US are HCV-coinfected |
| [38293756](https://pubmed.ncbi.nlm.nih.gov/38293756/) | 2024 | Systematic review/meta-analysis | Liver Int | Direct-acting antivirals, including glecaprevir/pibrentasvir, in children and adolescents with HCV |
| [31537106](https://pubmed.ncbi.nlm.nih.gov/31537106/) | 2020 | Review | Ann Pharmacother | First 8-week pangenotypic HCV regimen for patients 12 years and older |

The literature concerns HCV treatment and drug interactions in HIV-coinfected patients. None shows an anti-HIV effect.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02522470 | MAVIRET | Not listed | Not listed |
| 02467550 | MAVIRET | Not listed | Not listed |

---

## Safety Considerations

- **Drug Interactions**: 57 interactions were identified. Those rated Major are:
  - Rosuvastatin
  - Simvastatin
  - Edoxaban

  Moderate-level interactions include:
  - Dexamethasone
  - Omeprazole
  - Esomeprazole
  - Apixaban
  - Betrixaban
  - Cobicistat
  - Deferasirox
  - Metreleptin
  - Naldemedine
  - Troglitazone
  - Lusutrombopag
  - Revefenacin
  - Griseofulvin

  Interactions with HIV antiretrovirals, including cobicistat-boosted regimens, need particular attention in coinfected patients.
- **Literature signal**: One case report (PMID 31129632) describes glecaprevir/pibrentasvir-associated acute liver injury in a non-cirrhotic patient without HBV coinfection.

For warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high prediction score appears to reflect HIV/HCV comorbidity in the knowledge graph rather than anti-HIV activity. Glecaprevir targets an HCV-specific protease with no known counterpart in HIV, and the available Phase 3 evidence supports HCV cure in coinfected patients only.

**To proceed, the following is needed:**
- In vitro anti-HIV activity data showing any effect of glecaprevir on HIV replication
- Detailed mechanism of action data
- Health Canada package insert warnings and contraindications, which are required before safety screening
- A clear decision on whether the real opportunity is HCV treatment in HIV-coinfected populations, which is already within the approved HCV use, rather than a new HIV indication

**Other predictions reviewed:** The other nine predictions (such as hepatitis B, hepatitis E, hepatitis A, Omsk hemorrhagic fever and Kyasanur forest disease) have no direct supporting evidence and are also placed on Hold. The hepatitis A entry lists many glecaprevir/pibrentasvir trials, but they are HCV studies with no hepatitis A endpoint and should not be counted as evidence. For hepatitis B, HBV reactivation during HCV antiviral therapy is a safety risk, not a benefit.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

