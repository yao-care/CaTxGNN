---
layout: default
title: Voxilaprevir
parent: Model Prediction Only (L5)
nav_order: 833
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

Using the drug-repurposing-evaluation-report skill (v5 template) to structure this Evidence Pack into the standard report.

# Voxilaprevir: From Chronic Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

Voxilaprevir is an HCV NS3/4A protease inhibitor marketed only as a component of the fixed-dose combination Sofosbuvir/Velpatasvir/Voxilaprevir (Vosevi), used for chronic hepatitis C virus infection. The TxGNN model predicts it may be effective for **hepatitis B virus infection**, but the underlying evidence — 5 clinical trials and 9 publications — all describe voxilaprevir's use against **HCV**, not HBV, and the drug's own mechanism (serine protease inhibition) has no known target overlap with HBV's polymerase/reverse-transcriptase–driven replication.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in Canadian regulatory data (drug not marketed); per clinical trial evidence, voxilaprevir is a component of the Vosevi (SOF/VEL/VOX) combination indicated for chronic hepatitis C virus infection |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for voxilaprevir is not available in this Evidence Pack (flagged as a High-severity data gap). Based on known pharmacology, voxilaprevir is an NS3/4A serine protease inhibitor that blocks HCV polyprotein processing; it is used exclusively as part of the triple combination Vosevi (sofosbuvir + velpatasvir + voxilaprevir) for chronic hepatitis C, including in patients who failed prior direct-acting antiviral (DAA) therapy.

Mechanistically, this prediction is weak. HBV is a hepadnavirus that replicates via reverse transcription of pregenomic RNA and does not depend on an NS3/4A-type serine protease for its life cycle; there is no known structural or catalytic homology between HBV's replication machinery and HCV's NS3/4A protease. Every clinical trial and publication retrieved for this candidate — including drug-drug interaction studies, pediatric PK studies, hepatic/renal impairment studies, and multiple Phase 2/3 registrational trials — describes voxilaprevir's use in **HCV-infected** populations, with no direct evidence of anti-HBV activity.

Notably, this same pattern repeats across the full top-10 TxGNN prediction list for this candidate: hepatitis E, hepatitis A, animal viral hepatitis, HIV, chronic HBV, feline immunodeficiency virus, and simian immunodeficiency virus all score similarly high (>99%) despite belonging to virus families with no confirmed protease-target overlap with HCV. Only the two flavivirus predictions (Omsk hemorrhagic fever, Kyasanur forest disease) have a plausible — but entirely untested — structural rationale, since Flaviviridae share the NS3 protease superfamily with HCV. Taken together, this suggests the high TxGNN scores for this candidate likely reflect clustering around a "viral hepatitis / hemorrhagic fever" phenotype node in the knowledge graph, rather than a genuine mechanism-level drug–disease relationship.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02533427](https://clinicaltrials.gov/study/NCT02533427) | Phase 1 | Completed | 15 | Drug-interaction study of SOF/VEL/VOX with hormonal contraceptives in HCV patients — not an HBV efficacy study |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular outcomes after HCV eradication in HIV/HCV co-infected patients — unrelated to HBV |
| [NCT04695769](https://clinicaltrials.gov/study/NCT04695769) | Phase 4 | Completed | 281 | Ribavirin + SOF/VEL/VOX in chronic HCV DAA non-responders — unrelated to HBV |
| [NCT06180590](https://clinicaltrials.gov/study/NCT06180590) | N/A | Recruiting | 200 | Real-world cohort evaluating Vosevi in HCV patients who failed prior DAA therapy — unrelated to HBV |
| [NCT02938013](https://clinicaltrials.gov/study/NCT02938013) | Phase 4 | Completed | 15 | Liver sampling study of HCV viral kinetics during DAA (including SOF/VEL/VOX) therapy — unrelated to HBV |

**None of the retrieved trials studied voxilaprevir in HBV-infected patients or evaluated anti-HBV efficacy.**

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35248212](https://pubmed.ncbi.nlm.nih.gov/35248212/) | 2022 | Cohort (Tier 2) | Lancet Gastroenterol Hepatol | SOF/VEL/VOX retreatment of HCV genotype 4 non-a/d subtypes in Rwanda (SHARED-3) — HCV, not HBV |
| [36535062](https://pubmed.ncbi.nlm.nih.gov/36535062/) | 2022 | Real-world Cohort (Tier 2) | J Gastrointestin Liver Dis | Real-world SOF/VEL/VOX efficacy/safety in Romanian genotype 1b HCV DAA non-responders |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | Cohort (Tier 2) | Semin Liver Dis | Review of retreatment strategies for HCV patients who failed DAA regimens |
| [40611935](https://pubmed.ncbi.nlm.nih.gov/40611935/) | 2025 | Cohort (Tier 2) | J Clin Exp Hepatol | Resistance-associated substitutions and predictors of DAA treatment failure in an HCV elimination cohort |
| [30964552](https://pubmed.ncbi.nlm.nih.gov/30964552/) | 2019 | Basic/Resistance (Tier 3) | Hepatology | Evolutionary persistence of HCV protease-inhibitor resistance variants (mechanistic, HCV-specific) |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Review (Tier 3) | Clin Pharmacokinet | PK/PD review of HCV DAA regimens including SOF/VEL/VOX |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Conference Report (Tier 3) | AIDS Reviews | General viral hepatitis conference report covering both HBV and HCV burden/eradication goals |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | Economic (Tier 3) | Annals of Hepatology | Cross-country pricing comparison of HBV vs. HCV antivirals — economic analysis, not efficacy data |
| [31915372](https://pubmed.ncbi.nlm.nih.gov/31915372/) | 2020 | Review (Tier 3) | Nat Rev Gastroenterol Hepatol | General review of antiviral therapy in viraemic organ transplantation |

**None of the literature provides direct evidence of anti-HBV activity for voxilaprevir.**

## Canada Market Information

Voxilaprevir is **not currently marketed in Canada** — no Drug Identification Numbers (DINs) are on record (0 licenses).

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Key warnings, contraindications, and drug-interaction data for voxilaprevir could not be retrieved for this Evidence Pack — see Conclusion below.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.84%), there is no mechanistic, preclinical, or clinical evidence that voxilaprevir's NS3/4A serine protease inhibition has any activity against HBV, whose replication does not depend on this protease family. All retrieved trials and publications describe voxilaprevir's established use against HCV, and the same pattern of mechanistically implausible high-scoring predictions (HEV, HAV, HIV, FIV, SIV, animal hepatitis) appears throughout this candidate's top-10 list, suggesting a knowledge-graph clustering artifact rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- Health Canada / manufacturer product monograph data on warnings, contraindications, and drug interactions (currently a Blocking data gap — required before any S1 safety pre-assessment)
- Confirmed mechanism-of-action documentation from DrugBank or primary literature
- In vitro or in vivo evidence of anti-HBV activity before this candidate can advance beyond a research hypothesis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

