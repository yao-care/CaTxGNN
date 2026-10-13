---
layout: default
title: Voxilaprevir
parent: Model Prediction Only (L5)
nav_order: 984
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

# Voxilaprevir: From Chronic Hepatitis C Infection to Hepatitis B Virus Infection

## One-Sentence Summary

Voxilaprevir is a hepatitis C virus (HCV) protease inhibitor, originally used to treat chronic hepatitis C infection.
The TxGNN model predicts it may be effective for **hepatitis B virus infection**, but **no clinical trials** and **no HBV-specific publications** support this direction.
The 9 publications retrieved all concern HCV retreatment, resistance, pricing, or epidemiology.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C virus infection |
| Predicted New Indication | Hepatitis B virus infection |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, voxilaprevir is an HCV NS3/4A protease inhibitor. It is marketed as part of the fixed-dose combination sofosbuvir/velpatasvir/voxilaprevir, which is used mainly to retreat patients who failed earlier direct-acting antiviral therapy.

The mechanistic link to hepatitis B is weak. HBV has no NS3/4A protease counterpart. It replicates through a reverse transcriptase/polymerase and follows a different replication cycle. The high TxGNN score (99.84%) most likely reflects proximity between viral hepatitis nodes in the knowledge graph rather than true overlap in drug targets.

The other top predictions point the same way. Hepatitis A, hepatitis E, HIV, feline and simian immunodeficiency viruses, and chronic HBV use proteases or other targets unrelated to HCV NS3/4A. Omsk hemorrhagic fever and Kyasanur forest disease are caused by flaviviruses with an NS2B/NS3 protease. They offer only a speculative, family-level rationale, and no experimental evidence exists for them.

## Clinical Trial Evidence

Currently no related clinical trials are registered for hepatitis B virus infection.

## Literature Evidence

None of the publications below tests voxilaprevir in HBV. HBV appears only as a co-topic. Because none is HBV-specific, they are listed by study type (cohort, then review, then other) rather than by relevance.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35248212](https://pubmed.ncbi.nlm.nih.gov/35248212/) | 2022 | Cohort (single-arm trial) | Lancet Gastroenterol Hepatol | Sofosbuvir-velpatasvir-voxilaprevir retreatment of HCV after DAA failure in Rwanda (SHARED-3) |
| [36535062](https://pubmed.ncbi.nlm.nih.gov/36535062/) | 2022 | Cohort | J Gastrointestin Liver Dis | Real-world efficacy and safety of SOF/VEL/VOX in Romanian genotype 1b patients who failed prior DAA therapy |
| [40611935](https://pubmed.ncbi.nlm.nih.gov/40611935/) | 2025 | Cohort | J Clin Exp Hepatol | Resistance-associated substitutions and predictors of DAA treatment failure in an HCV elimination cohort |
| [41570233](https://pubmed.ncbi.nlm.nih.gov/41570233/) | 2025 | Cohort | Vopr Virusol | Prevalence of HIV, HBV, and HCV markers among dental patients (epidemiology only) |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | Review | Semin Liver Dis | Retreatment of HCV patients after DAA failure |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Review | Clin Pharmacokinet | Pharmacokinetic and pharmacodynamic considerations for HCV therapy, including SOF/VEL/VOX |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Review | AIDS Rev | Report from the International Conference on Viral Hepatitis 2017 |
| [30964552](https://pubmed.ncbi.nlm.nih.gov/30964552/) | 2019 | Other | Hepatology | Evolution of HCV protease inhibitor escape variants |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | Other | Ann Hepatol | Global comparison of hepatitis B and C drug pricing |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02467542 | VOSEVI | Not specified | Not specified in the data compiled |

## Safety Considerations

- **Drug Interactions**: 19 interactions were identified. Three are rated **Major**: rosuvastatin, edoxaban, and cyclosporine. The other 16 are rated Moderate, including eluxadoline, obeticholic acid, cobicistat, apixaban, eltrombopag, artesunate, afatinib, bosutinib, cobimetinib, ethinylestradiol, idelalisib, lapatinib, lenvatinib, olaparib, pazopanib, and teriflunomide.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (Evidence Level L5). There are no HBV clinical trials or HBV-specific publications, and the mechanism does not support activity against HBV. Voxilaprevir targets the HCV NS3/4A protease, which HBV lacks. The high score likely reflects graph proximity between viral hepatitis nodes.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) to support a formal mechanistic-link analysis
- Package insert warnings and contraindications from Health Canada, which are required before safety screening
- In vitro evidence that voxilaprevir has any anti-HBV activity
- Review of the Canadian product listing, since dosage form and approved indication text are missing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

