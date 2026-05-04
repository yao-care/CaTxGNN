---
layout: default
title: Cefoxitin
parent: 僅模型預測 (L5)
nav_order: 137
evidence_level: L5
indication_count: 10
---

# Cefoxitin
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

# Cefoxitin: From Broad-Spectrum Antibiotic to Infectious Otitis Media

## One-Sentence Summary

Cefoxitin is a cephamycin (second-generation cephalosporin) antibiotic with broad-spectrum activity against gram-negative bacteria and anaerobes, historically used for surgical prophylaxis and treatment of serious bacterial infections, though it currently holds no marketing authorization in Canada.
The TxGNN model's top prediction is **Infectious Otitis Media** (score 99.30%), supported only by **2 peripheral literature references** with no dedicated clinical trials; however, this is a multi-indication Evidence Pack where **Urinary Tract Infection** (4 clinical trials, 20 publications) and **Gonococcal Urethritis** (20 publications, multiple historical controlled trials) carry substantially stronger evidence.
Across all 10 predicted indications, the most actionable repurposing signal is **Gonococcal Urethritis** (Evidence Level L2, "Proceed with Guardrails"), while the majority of otitis media predictions remain at the hypothesis stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not marketed in Canada — no approved indication on record |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.30% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, cefoxitin is a cephamycin antibiotic that inhibits bacterial cell wall synthesis by covalently binding to penicillin-binding proteins (PBPs). Its cephamycin core confers resistance to hydrolysis by many plasmid-mediated β-lactamases, providing clinically useful activity against gram-negative bacilli (including some ESBL-producing strains) and anaerobes — a spectrum broader than first-generation cephalosporins.

For infectious otitis media specifically, the predominant causative pathogens are *Streptococcus pneumoniae*, *Haemophilus influenzae*, and *Moraxella catarrhalis*. Cefoxitin's coverage of these organisms is limited compared to preferred agents such as amoxicillin-clavulanate, and its IV-only formulation makes it unsuitable for the outpatient setting where most otitis media is managed. The two available literature references address MRSA epidemiology (where cefoxitin functions as a disk-diffusion surrogate marker for oxacillin resistance, *not* as a treatment agent) and a rare case of *Mycobacterium fortuitum* otitis media — both peripheral to typical disease management. The mechanistic basis for this specific prediction is therefore narrow.

The TxGNN model has predicted a cluster of otitis media-related indications (ranks 1, 3, 4, 5, 9, 10) alongside urinary tract and urethral infections, suggesting the model is capturing cefoxitin's broad antibacterial spectrum rather than any ear-specific pharmacology. The biologically strongest predictions are the UTI-related indications (cefoxitin's documented anti-ESBL *E. coli* activity, confirmed in murine models) and gonococcal urethritis (demonstrated in multiple historical controlled clinical trials as an effective alternative to penicillin against penicillinase-producing *Neisseria gonorrhoeae*).

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Infectious Otitis Media.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33061472](https://pubmed.ncbi.nlm.nih.gov/33061472/) | 2020 | Review | Infection and Drug Resistance | MRSA as a cause of otitis media among other severe infections; cefoxitin cited as a surrogate disk-diffusion marker for MRSA identification, not as therapeutic agent |
| [8783722](https://pubmed.ncbi.nlm.nih.gov/8783722/) | 1996 | Case Report + Case Series Review | Clinical Infectious Diseases | *Mycobacterium fortuitum* as a rare cause of otitis media and mastoiditis; amikacin-resistant isolate reported — cefoxitin is not a first-line or recommended treatment for NTM infections |

---

## Supplementary Evidence: Urinary Tract Infection (Rank #2)

> **TxGNN Score:** 99.26% | **Evidence Level:** L3 | **Recommendation:** Research Question

Cefoxitin's anti-ESBL *E. coli* activity makes urinary tract infection (particularly complicated UTI and acute pyelonephritis) the most scientifically plausible indication in this pack. Two dedicated Phase 4 RCTs were designed to test this hypothesis but both terminated early due to recruitment challenges, leaving the field without conclusive clinical data.

### Clinical Trials — Urinary Tract Infection

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT01820793](https://clinicaltrials.gov/study/NCT01820793) | N/A | TERMINATED | 9 | Directly studied cefoxitin PK/PD in acute pyelonephritis caused by CTX-M-type ESBL-producing *E. coli*; terminated due to recruitment difficulties — no efficacy conclusions possible |
| [NCT02474706](https://clinicaltrials.gov/study/NCT02474706) | Phase 4 | TERMINATED | 6 | Non-inferiority RCT: cefoxitin vs. imipenem/cilastatin for ESBL-producing *E. coli* UTI; terminated after enrolling only 6 patients — entirely underpowered |
| [NCT02959957](https://clinicaltrials.gov/study/NCT02959957) | Phase 4 | COMPLETED | 157 | RCT comparing temocillin vs. cefotaxime for febrile UTI; primary endpoint was intestinal microbiota collateral damage, not cefoxitin efficacy — provides indirect ecological safety context only |
| [NCT01426191](https://clinicaltrials.gov/study/NCT01426191) | N/A | COMPLETED | 2032 | Study of cefotaxime/sulbactam (not cefoxitin) for respiratory and UTI — low relevance |

### Key Literature — Urinary Tract Infection

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [22214774](https://pubmed.ncbi.nlm.nih.gov/22214774/) | 2012 | Animal Model | Antimicrobial Agents and Chemotherapy | Cefoxitin equivalent to carbapenems in murine UTI model caused by CTX-M-15 ESBL-producing *E. coli* CFT073 — proof-of-concept for biological plausibility |
| [357399](https://pubmed.ncbi.nlm.nih.gov/357399/) | 1978 | Clinical Study | J Antimicrobial Chemotherapy | Early clinical report of cefoxitin sodium in complicated UTI |
| [4046178](https://pubmed.ncbi.nlm.nih.gov/4046178/) | 1985 | Clinical Trial | Japanese Journal of Antibiotics | Cefoxitin evaluated in 46 patients for prevention and treatment of postoperative UTI and pulmonary infections; generally favorable results |
| [400934](https://pubmed.ncbi.nlm.nih.gov/400934/) | 1979 | Clinical Study | Reviews of Infectious Diseases | Intramuscular cefoxitin in 102 patients with mild-to-moderate infections; UTI among indications included |
| [40165096](https://pubmed.ncbi.nlm.nih.gov/40165096/) | 2025 | Retrospective Cohort | BMC Infectious Diseases | Cefepime vs. carbapenem for complicated UTI caused by cefoxitin-nonsusceptible ESCPM organisms; uses cefoxitin disk result as AmpC phenotyping surrogate |
| [37284390](https://pubmed.ncbi.nlm.nih.gov/37284390/) | 2023 | Observational | Cureus | MDR-UTI in chronic kidney disease patients; cefoxitin included in susceptibility profiling panel |
| [40057723](https://pubmed.ncbi.nlm.nih.gov/40057723/) | 2025 | Cross-sectional | BMC Microbiology | Uropathogen antimicrobial susceptibility and risk factors in Ethiopia; regional surveillance data |
| [34659966](https://pubmed.ncbi.nlm.nih.gov/34659966/) | 2021 | Cross-sectional | Cureus | Frequency and resistance patterns of UTI-causing bacteria in Turkey; cefoxitin susceptibility data included |
| [22749057](https://pubmed.ncbi.nlm.nih.gov/22749057/) | 2012 | Surveillance | International Journal of Antimicrobial Agents | SMART Asia-Pacific UTI Gram-negative surveillance (2009–2010); cefoxitin MIC data across 11 countries |
| [7004691](https://pubmed.ncbi.nlm.nih.gov/7004691/) | 1980 | Review | Clinical Obstetrics and Gynecology | Review of puerperal infections including UTI; cefoxitin discussed as an option for polymicrobial infections |

---

## Supplementary Evidence: Gonococcal Urethritis (Rank #6)

> **TxGNN Score:** 99.09% | **Evidence Level:** L2 | **Recommendation:** Proceed with Guardrails

No contemporary registered clinical trials were found. However, the 1970s–1980s literature contains multiple controlled clinical trials demonstrating that cefoxitin was an effective alternative to penicillin for gonorrhea treatment, particularly against penicillinase-producing *Neisseria gonorrhoeae* (PPNG). This represents the most robust historical clinical evidence in the entire Evidence Pack.

### Key Literature — Gonococcal Urethritis

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [400933](https://pubmed.ncbi.nlm.nih.gov/400933/) | 1979 | Controlled Clinical Trial | Reviews of Infectious Diseases | 143 men with uncomplicated gonococcal urethritis; cefoxitin 2g IM + probenecid 1g vs. penicillin G — cefoxitin failure rate 1.8% vs. 3.6% (penicillin); effective against both PPNG and non-PPNG strains |
| [111119](https://pubmed.ncbi.nlm.nih.gov/111119/) | 1979 | Controlled Clinical Trial | New England Journal of Medicine | 107 men in region with 40% PPNG prevalence; single-dose cefoxitin vs. procaine penicillin G — cefoxitin effective against penicillinase-resistant strains where penicillin failed |
| [6658629](https://pubmed.ncbi.nlm.nih.gov/6658629/) | 1983 | RCT | Sexually Transmitted Diseases | 406 men and women; cefoxitin 2g vs. penicillin G — no statistically significant difference in failure rate (5.1% vs. 4.3%); active in PPNG and proctitis |
| [6303490](https://pubmed.ncbi.nlm.nih.gov/6303490/) | 1983 | Controlled Clinical Trial | British Journal of Venereal Diseases | 128 men with culture-confirmed PPNG urethritis; cefoxitin 2g IM vs. ceftriaxone 250mg IM — both effective; ceftriaxone showed slightly superior cure rate |
| [6228024](https://pubmed.ncbi.nlm.nih.gov/6228024/) | 1983 | Clinical Study | Sexually Transmitted Diseases | Cefoxitin 1g IM + probenecid 1g: 86/89 (97%) cure rate; 60% of infections caused by penicillin-resistant strains |
| [3089907](https://pubmed.ncbi.nlm.nih.gov/3089907/) | 1986 | Clinical Study | Genitourinary Medicine | 136 patients; cefoxitin 1g overall 96% cure rate for PPNG and non-PPNG strains; post-gonococcal urethritis rate noted |
| [119328](https://pubmed.ncbi.nlm.nih.gov/119328/) | 1979 | Clinical Trial | Sexually Transmitted Diseases | 25 patients (10 men, 15 women); cefoxitin 1g and 2g IM against PPNG strains — both doses effective |
| [3319500](https://pubmed.ncbi.nlm.nih.gov/3319500/) | 1987 | Review | Drugs | Comprehensive review of cephalosporins in gonorrhea; cefoxitin specifically identified as active for penicillin-resistant strains including PPNG |
| [6234346](https://pubmed.ncbi.nlm.nih.gov/6234346/) | 1984 | Case Report | Journal of the American Optometric Association | Gonococcal conjunctivitis caused by PPNG treated successfully with cefoxitin 2g IM + probenecid 1g single dose |
| [3929408](https://pubmed.ncbi.nlm.nih.gov/3929408/) | 1985 | Case Report | Sexually Transmitted Diseases | PPNG conjunctivitis in a 21-year-old man; single dose cefoxitin 2g IM + probenecid 1g resulted in satisfactory outcome |

---

## Summary of All Predicted Indications

| Rank | Indication | TxGNN Score | Evidence Level | Recommendation | Assessment |
|------|-----------|-------------|----------------|----------------|------------|
| 1 | Infectious Otitis Media | 99.30% | L4 | Hold | Narrow mechanistic link; cefoxitin covers few typical pathogens; MRSA/NTM angle only |
| 2 | Urinary Tract Infection | 99.26% | L3 | Research Question | 2 terminated Phase 4 RCTs + animal model support; ESBL-UTI niche is biologically plausible |
| 3 | Chronic Otitis Media | 99.12% | L4 | Research Question | Anaerobic coverage relevant; no direct cefoxitin-specific clinical data |
| 4 | Suppurative Otitis Media | 99.11% | L4 | Research Question | Cefoxitin acts as MRSA surrogate test marker — diagnostic role, not therapeutic |
| 5 | Middle Ear Disease | 99.11% | L3 | Hold | One 1982 unregistered case series for cholesteatoma surgery prophylaxis; insufficient evidence |
| 6 | Gonococcal Urethritis | 99.09% | L2 | **Proceed with Guardrails** | Strongest evidence; multiple 1979–1986 controlled trials; contemporary susceptibility data needed |
| 7 | Ureaplasma Urethritis | 99.09% | L5 | Hold | Biological contradiction — β-lactams have no activity against cell wall-deficient *Ureaplasma* |
| 8 | Toxocariasis | 99.09% | L5 | Hold | Biological contradiction — cefoxitin is an antibacterial; no antiparasitic activity against nematodes |
| 9 | Otosalpingitis | 99.08% | L5 | Hold | No evidence; theoretical partial coverage only |
| 10 | Non-Suppurative Otitis Media | 99.07% | L5 | Hold | Primarily non-bacterial (eustachian tube dysfunction, allergy, viral); antibiotics not indicated per guidelines |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Two data gaps were flagged in this Evidence Pack. DG001 (Blocking): TFDA package insert warnings and contraindications are unavailable — required before formal safety screening. DG002 (High): Formal MOA data is absent — impacts mechanistic analysis quality.

---

## Conclusion and Next Steps

**Decision: Hold** *(Primary prediction: Infectious Otitis Media, L4)*
**Decision: Proceed with Guardrails** *(Strongest signal: Gonococcal Urethritis, L2)*

**Rationale:**

The top-ranked TxGNN prediction (infectious otitis media) is not supported by meaningful clinical evidence and lacks a compelling mechanistic basis given cefoxitin's limited coverage of typical otitis media pathogens. A "Hold" decision is appropriate for this and the other five otitis media-cluster predictions (ranks 1, 3, 4, 5, 9, 10), as these require at minimum prospective in vitro susceptibility data against local pathogen populations before further clinical consideration.

The most actionable finding is **gonococcal urethritis**: multiple controlled clinical trials from 1979–1986 established cefoxitin as an effective single-dose treatment for uncomplicated gonorrhea, including against penicillinase-producing strains. The primary caveat is that these data are 35–45 years old and predate modern fluoroquinolone resistance patterns in *N. gonorrhoeae*. Cefoxitin is not featured in current CDC or WHO gonorrhea treatment guidelines, representing a gap to be addressed before clinical use.

**To proceed, the following is needed:**

- **Immediate (blocking):** Obtain TFDA package insert PDF and extract warnings, contraindications, and dosing information (DG001)
- **High priority:** Confirm formal MOA via DrugBank API (DG002)
- **For Gonococcal Urethritis (Proceed with Guardrails):**
  - Obtain contemporary *N. gonorrhoeae* cefoxitin MIC surveillance data from target region
  - Assess whether a cefoxitin-based regimen offers advantages over current guideline-recommended cephalosporins (e.g., ceftriaxone)
  - Evaluate whether the historical dosing regimen (2g IM + probenecid 1g) remains appropriate given modern PK/PD standards
- **For Urinary Tract Infection (Research Question):**
  - Review reasons for early termination of NCT01820793 and NCT02474706 to inform feasibility of a new study design
  - Conduct a prospective PK/PD study in ESBL-UTI patients with a revised and powered protocol
  - Address IV-only formulation limitation — cefoxitin's lack of oral bioavailability restricts outpatient UTI management utility
- **For all otitis media predictions:**
  - Collect in vitro susceptibility data for cefoxitin against regional middle ear pathogen isolates before investing further resources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

