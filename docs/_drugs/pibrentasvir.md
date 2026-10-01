---
layout: default
title: Pibrentasvir
parent: Model Prediction Only (L5)
nav_order: 727
evidence_level: L5
indication_count: 10
---

# Pibrentasvir
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

# Pibrentasvir: From Chronic Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

Pibrentasvir is an HCV NS5A inhibitor, marketed in Canada as part of the glecaprevir/pibrentasvir combination (MAVIRET) for chronic hepatitis C.
The TxGNN model predicts it may be effective for **hepatitis B virus infection**. Although **13 clinical trials** and **20 publications** were retrieved, they all concern hepatitis C, so **no direct HBV evidence** currently supports this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C (inferred from the trial and literature evidence; the licence records contain no indication text) |
| Predicted New Indication | Hepatitis B virus infection |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 (as assigned in the Evidence Pack; no HBV-specific study was found) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, pibrentasvir is part of a fixed-dose combination with glecaprevir (an NS3/4A protease inhibitor). Its efficacy in hepatitis C has been established, but its applicability to hepatitis B is unproven.

Hepatitis B and hepatitis C are both hepatotropic viral infections, which is probably why the model places them close together. The mechanistic link is weak, however. Pibrentasvir targets NS5A, a protein HBV does not have. No data in the supplied evidence show anti-HBV activity. The very high score (99.84%) most likely reflects proximity in the knowledge graph among liver-infecting viruses, not a demonstrated pharmacological effect.

HBV appears in the retrieved evidence only as a safety issue (HBV reactivation during direct-acting antiviral therapy for HCV) and in a vaccination commentary. Neither supports treating HBV with this drug.

---

## Clinical Trial Evidence

All retrieved trials study pibrentasvir (usually with glecaprevir) in **hepatitis C**. None reports an HBV endpoint; the Evidence Pack's own relevance reviews that reached a grade rate them C (indirect at best).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02640482](https://clinicaltrials.gov/study/NCT02640482) | Phase 3 | Completed | 304 | Placebo-controlled study in HCV genotype 2 (ENDURANCE-2); no HBV evidence |
| [NCT02640157](https://clinicaltrials.gov/study/NCT02640157) | Phase 3 | Completed | 506 | Compared with sofosbuvir plus daclatasvir in HCV genotype 3 (ENDURANCE-3) |
| [NCT02707952](https://clinicaltrials.gov/study/NCT02707952) | Phase 3 | Completed | 295 | Japanese adults with chronic HCV (CERTAIN-1); matched to HBV by drug name only |
| [NCT02723084](https://clinicaltrials.gov/study/NCT02723084) | Phase 3 | Completed | 136 | Versus sofosbuvir plus ribavirin in Japanese HCV genotype 2 (CERTAIN-2) |
| [NCT03092375](https://clinicaltrials.gov/study/NCT03092375) | Phase 3 | Completed | 177 | Glecaprevir/pibrentasvir ± ribavirin in HCV genotype 1 patients previously treated with NS5A inhibitor plus sofosbuvir |
| [NCT03219216](https://clinicaltrials.gov/study/NCT03219216) | Phase 3 | Completed | 100 | Treatment-naïve HCV genotype 1–6 in Brazil; 8 or 12 weeks of therapy |
| [NCT02243293](https://clinicaltrials.gov/study/NCT02243293) | Phase 2/3 | Completed | 694 | HCV genotypes 2–6, with or without ribavirin (SURVEYOR-II) |
| [NCT02446717](https://clinicaltrials.gov/study/NCT02446717) | Phase 2/3 | Completed | 141 | HCV patients who failed a prior direct-acting antiviral regimen |
| [NCT02243280](https://clinicaltrials.gov/study/NCT02243280) | Phase 2 | Completed | 174 | Open-label dose study in HCV genotype 1, 4, 5 and 6 (SURVEYOR-I); no HBV efficacy endpoint |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular outcomes after HCV eradication in HIV/HCV patients; unrelated to HBV |

---

## Literature Evidence

No retrieved publication reports pibrentasvir treating HBV. The items below are the most relevant ones; all concern HCV, or HBV only as a comparison or safety context.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29485084](https://pubmed.ncbi.nlm.nih.gov/29485084/) | 2018 | Review | The Lancet Infectious Diseases | Commentary on vaccinating against hepatitis B after hepatitis C treatment |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Review | World Journal of Gastroenterology | Pediatric HBV and HCV management; HCV has effective direct-acting antivirals, while HBV treatment is still far from curative |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Review | European Journal of General Practice | Diagnosis and treatment of chronic HCV with direct-acting antivirals |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Review | Clinical Pharmacokinetics | Pharmacokinetic and pharmacodynamic update on HCV regimens, including glecaprevir/pibrentasvir |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Conference report | AIDS Reviews | Viral hepatitis conference summary covering HBV and HCV burden and new pan-genotypic HCV antivirals |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | Retrospective study | Klinicka mikrobiologie a infekcni lekarstvi | Frequency, efficacy and tolerance of antiviral treatment for chronic HBV and HCV in children in Ostrava |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | Cross-sectional study | Annals of Hepatology | International price comparison of HBV and HCV antivirals |
| [31981264](https://pubmed.ncbi.nlm.nih.gov/31981264/) | 2020 | Retrospective cohort | Journal of Viral Hepatitis | Real-world glecaprevir/pibrentasvir in 108 Taiwanese HCV patients with CKD stage 4–5; HCV only |
| [34344581](https://pubmed.ncbi.nlm.nih.gov/34344581/) | 2021 | Case report | Journal of Infection and Chemotherapy | Glecaprevir/pibrentasvir for HCV exacerbation triggered by daratumumab therapy; mentions HBV reactivation only as a comparison |
| [31129632](https://pubmed.ncbi.nlm.nih.gov/31129632/) | 2019 | Case report | BMJ Case Reports | Acute liver injury during glecaprevir/pibrentasvir in non-cirrhotic HCV patient without HBV co-infection |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2522470 | MAVIRET |
| 2467550 | MAVIRET |

Dosage form and approved indication text were not provided in the licence records.

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the queried data.

Please refer to the Health Canada package insert for warnings, contraindications and interaction details.

The retrieved literature raises HBV reactivation during direct-acting antiviral therapy for HCV as a known safety concern. Any use in people with HBV would need dedicated safety evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a graph-proximity score alone. Every retrieved trial and publication addresses HCV, and pibrentasvir's NS5A target has no HBV counterpart. No direct evidence of anti-HBV activity exists. The other nine predicted indications (including HIV, HEV and HAV) are also rated Hold, mostly at the model-prediction-only level.

**To proceed, the following is needed:**
- Mechanism of action data (currently a data gap)
- In vitro anti-HBV activity data for pibrentasvir (for example in HBV replication cell models)
- Health Canada package insert warnings and contraindications (currently a blocking gap for safety screening)
- Assessment of HBV reactivation risk and a monitoring plan for patients with HBV co-infection
- Any HBV-specific clinical studies, if preclinical data show activity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

