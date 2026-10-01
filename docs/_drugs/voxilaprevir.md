---
layout: default
title: Voxilaprevir
parent: Model Prediction Only (L5)
nav_order: 977
evidence_level: L5
indication_count: 10
---

# Voxilaprevir
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

# Voxilaprevir: From Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

Voxilaprevir is a hepatitis C virus (HCV) protease inhibitor, marketed only inside the fixed-dose combination sofosbuvir/velpatasvir/voxilaprevir (Vosevi).
The TxGNN model predicts it may be effective for **hepatitis B virus infection**, and **5 clinical trials** and **10 publications** were retrieved for this prediction. All of them concern HCV, and none shows anti-HBV activity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C (inferred from the Vosevi combination; the Canadian licence text is blank) |
| Predicted New Indication | Hepatitis B virus infection |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 (model prediction only; no HBV-specific studies. The input pack lists L4) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Voxilaprevir is a pan-genotypic HCV NS3/4A protease inhibitor. It is sold only as the Vosevi combination for HCV, and no detailed mechanism-of-action record was supplied.

The link to HBV is weak. HBV is a hepadnavirus that replicates by reverse transcription and has no NS3/4A-type protease target. The high score most likely reflects graph proximity among hepatitis viruses, not a shared drug target. No credible mechanism currently supports anti-HBV activity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02533427](https://clinicaltrials.gov/study/NCT02533427) | Phase 1 | Completed | 15 | Drug-interaction study of the SOF/VEL/VOX combination with a hormonal contraceptive; PK data only, no HBV efficacy |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular risk after HCV cure in HIV/HCV patients; no HBV treatment |
| [NCT04695769](https://clinicaltrials.gov/study/NCT04695769) | Phase 4 | Completed | 281 | Ribavirin plus SOF/VEL/VOX in chronic hepatitis C non-responders (randomized); any HBV endpoint is unverified |
| [NCT06180590](https://clinicaltrials.gov/study/NCT06180590) | N/A | Recruiting | 200 | Prospective cohort of Vosevi after DAA failure; HCV setting |
| [NCT02938013](https://clinicaltrials.gov/study/NCT02938013) | Phase 4 | Completed | 15 | DAA effects on the liver (HCV kinetics with SOF/VEL ± VOX); not an HBV efficacy trial |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35248212](https://pubmed.ncbi.nlm.nih.gov/35248212/) | 2022 | Single-arm trial | Lancet Gastroenterol Hepatol | SOF/VEL/VOX retreatment of HCV after DAA failure in Rwanda (SHARED-3) |
| [36535062](https://pubmed.ncbi.nlm.nih.gov/36535062/) | 2022 | Cohort | J Gastrointestin Liver Dis | Real-world SOF/VEL/VOX in Romanian genotype 1b HCV patients who failed DAAs |
| [40611935](https://pubmed.ncbi.nlm.nih.gov/40611935/) | 2025 | Cohort | J Clin Exp Hepatol | Resistance-associated substitutions and treatment-failure predictors after DAA therapy in an HCV elimination cohort |
| [41570233](https://pubmed.ncbi.nlm.nih.gov/41570233/) | 2025 | Cohort | Vopr Virusol | Prevalence of HIV, HBV and HCV markers among dental patients; epidemiology only, no treatment data |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | Review | Semin Liver Dis | Retreatment of HCV patients after DAA failure |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Review | Clin Pharmacokinet | Pharmacokinetic and pharmacodynamic considerations for HCV therapy |
| [31915372](https://pubmed.ncbi.nlm.nih.gov/31915372/) | 2020 | Review | Nat Rev Gastroenterol Hepatol | Viraemic organ transplantation and antiviral therapies; general review, no abstract available |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | Review | Ann Hepatol | Global price comparison of HBV and HCV antivirals; economic, not efficacy |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Conference report | AIDS Rev | International Conference on Viral Hepatitis 2017 summary |
| [30964552](https://pubmed.ncbi.nlm.nih.gov/30964552/) | 2019 | Preclinical/Virology | Hepatology | Resistance pathways of HCV protease inhibitor escape variants |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2467542 | VOSEVI |

Dosage form and approved indication text are not available in the source record.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All retrieved trials and publications are HCV studies matched through the drug name, and none tests HBV. There is no plausible shared target, so the 99.84% score is most likely a graph-proximity artefact.

**To proceed, the following is needed:**
- Mechanism-of-action data and any in vitro evidence of anti-HBV activity
- Health Canada package insert warnings and contraindications
- Direct HBV efficacy data, which does not currently exist

Under current evidence, this drug is not a repurposing candidate for the other nine predicted indications either: hepatitis E, hepatitis A, HIV and the flaviviral diseases have the same lack of mechanism and support, and the animal-disease nodes have no data at all.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

