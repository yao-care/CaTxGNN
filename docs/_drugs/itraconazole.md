---
layout: default
title: Itraconazole
parent: Moderate Evidence (L3-L4)
nav_order: 427
evidence_level: L4
indication_count: 1
---

# Itraconazole
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

# Itraconazole: From Fungal Infections to Pneumocystosis

## One-Sentence Summary

Itraconazole is a triazole antifungal originally developed for systemic and superficial fungal infections (e.g., aspergillosis, histoplasmosis, candidiasis). The TxGNN model predicts potential efficacy against **Pneumocystosis** (Pneumocystis jirovecii pneumonia), but this prediction is currently supported only by **20 publications** (mostly reviews and case reports) with **no dedicated clinical trials**, and the underlying mechanistic rationale itself raises a notable concern about target relevance.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Systemic/superficial fungal infections (not currently licensed in Canada, so formal indication text is unavailable) |
| Predicted New Indication | Pneumocystosis (Pneumocystis pneumonia) |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L4 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Itraconazole's established antifungal mechanism is inhibition of fungal lanosterol 14α-demethylase (CYP51), which blocks ergosterol synthesis and disrupts fungal cell membrane integrity. This mechanism underlies its efficacy against classic fungal pathogens such as *Aspergillus*, *Candida*, and *Histoplasma* species.

Pneumocystosis, caused by *Pneumocystis jirovecii*, has historically been grouped with fungal/opportunistic infections in immunocompromised patients (HIV, transplant recipients), which is likely why azole-class drugs and Pneumocystis-related diseases co-occur frequently in literature and knowledge graphs — a plausible driver of the high TxGNN score.

However, the evidence review flags an important caveat: *Pneumocystis*'s cell membrane is composed predominantly of **cholesterol scavenged from the host**, not self-synthesized ergosterol, and its endogenous ergosterol-synthesis pathway is only weakly expressed. This means azole antifungals generally lack a reliable, direct mechanistic target in *Pneumocystis*, and one literature source in this evidence set (PMID 12606318) specifically characterizes the organism's demethylase enzyme in the context of azole resistance. The mechanistic link here should therefore be read as a **class-level inference** ("antifungal drug ↔ fungal-adjacent infection") rather than a target-specific rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | RCT | HIV Medicine | Double-blind, placebo-controlled Phase III trial of itraconazole capsules for prevention of deep fungal infections in HIV-infected patients |
| [30429396](https://pubmed.ncbi.nlm.nih.gov/30429396/) | 2018 | Cohort | Indian J Med Microbiol | Compared respiratory fungal pathogen profiles and susceptibility in immunocompetent vs. immunocompromised hosts by CD4 count |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Cohort | Transplantation Proceedings | Single-center experience of invasive fungal infections after kidney transplantation |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | Summarizes therapy/prophylaxis for *Pneumocystis carinii* and other systemic protozoan infections, including antifungal agent mechanisms |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Review/Case series | Seminars in Respiratory Infections | Infection (including fungal) as a major cause of morbidity/mortality after lung transplantation |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Review | Current Clinical Topics in Infectious Diseases | Prophylaxis and treatment of infection in bone marrow transplant recipients |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Review | BMJ Clinical Evidence | Primary and secondary prophylaxis for opportunistic infections in HIV, including Pneumocystis |
| [12606318](https://pubmed.ncbi.nlm.nih.gov/12606318/) | 2003 | Mechanism study | Am J Respir Cell Mol Biol | Characterizes *Pneumocystis carinii*'s lanosterol 14α-demethylase (azole target) and notes intrinsic azole resistance |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Case report | Frontiers in Immunology | Talaromyces marneffei and Pneumocystis jirovecii coinfection in a child with STAT1 mutation |
| [8967681](https://pubmed.ncbi.nlm.nih.gov/8967681/) | 1996 | Case report | Annals of Internal Medicine | Uveitis associated with rifabutin prophylaxis and itraconazole therapy |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No dedicated clinical trials support itraconazole for pneumocystosis, and the evidence level (L4) reflects literature/mechanism studies only. More importantly, the available evidence itself indicates that *Pneumocystis* relies on host-derived cholesterol rather than self-synthesized ergosterol, undermining the specificity of itraconazole's core antifungal mechanism for this pathogen.

**To proceed, the following is needed:**
- TFDA/Health Canada label warnings and contraindications (currently a Blocking data gap — required before any S1 safety screening)
- Confirmed mechanism of action data from DrugBank (currently a High-severity data gap)
- Preclinical or in vitro data specifically evaluating itraconazole activity against *Pneumocystis jirovecii*
- Drug-drug interaction profile, given itraconazole's well-known CYP3A4 interaction liability in the target immunocompromised population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

