---
layout: default
title: Ertapenem
parent: 僅模型預測 (L5)
nav_order: 259
evidence_level: L5
indication_count: 2
---

# Ertapenem
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Ertapenem: From Complicated Bacterial Infections to Bacterial Arthritis

## One-Sentence Summary

Ertapenem is a broad-spectrum carbapenem antibiotic widely used internationally for complicated bacterial infections including intra-abdominal infections, community-acquired pneumonia, and complicated urinary tract infections — though it is not currently marketed in Canada.
The TxGNN model predicts it may be effective for **Bacterial Arthritis** (rank 1, score 99.72%) and **Staphylococcus aureus Infection** (rank 2, score 99.28%),
supported by **9 publications** for the primary indication and **8 clinical trials + 20 publications** for the secondary indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Complicated bacterial infections (intra-abdominal, pneumonia, UTI, skin/soft tissue — established internationally; not registered in Canada) |
| Predicted New Indication | Bacterial Arthritis |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L3 (Bacterial Arthritis) / L2 (Staphylococcus aureus Infection) |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Ertapenem belongs to the carbapenem class of β-lactam antibiotics, exerting bactericidal activity by binding to penicillin-binding proteins (PBP-2 and PBP-3) and irreversibly inhibiting bacterial cell wall synthesis. Detailed MOA data was not retrievable from this evidence pack, but pharmacological literature confirms a broad antimicrobial spectrum covering Gram-negative Enterobacterales (Klebsiella, Citrobacter, Proteus, E. coli), anaerobes (Bacteroides, Clostridium, Prevotella), and methicillin-susceptible Staphylococcus aureus (MSSA). Critically, its extended half-life (~4 hours) enables once-daily intravenous dosing — a feature uncommon among carbapenems — making it the preferred carbapenem for outpatient parenteral antimicrobial therapy (OPAT).

Bacterial arthritis (septic arthritis) is most often caused by hematogenous seeding of joint spaces with bacteria. The most clinically problematic pathogens — Gram-negative rods (Klebsiella pneumoniae, Citrobacter koseri) and anaerobes (Prevotella bivia, Clostridium species) — fall squarely within ertapenem's spectrum. Because septic arthritis often requires 4–6 weeks of parenteral therapy, ertapenem's once-daily OPAT compatibility makes it mechanistically and logistically well-suited. Multiple case reports (PMIDs 22233826, 31352398, 37578166) directly document its use in Gram-negative and anaerobic septic arthritis, and a retrospective OPAT cohort of 306 patients (PMID 24709258) confirms its real-world safety for extended bone and joint infection treatment.

For the secondary predicted indication — **Staphylococcus aureus bacteremia** — the mechanism is distinct but scientifically compelling. In high-inoculum MSSA bacteremia, excess β-lactamase production overwhelms cefazolin's bactericidal capacity (the "inoculum effect" or Eagle Effect). Ertapenem competitively occupies and consumes this excess β-lactamase pool, restoring cefazolin's activity and producing synergistic bacterial killing. This mechanism has been confirmed in vitro, in murine endocarditis models, and across multiple clinical case series, and is now being formally evaluated in randomized controlled trials.

---

## Clinical Trial Evidence

### Bacterial Arthritis (Rank 1)

Currently no related clinical trials registered for bacterial arthritis.

---

### Staphylococcus aureus Infection (Rank 2)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04886284](https://clinicaltrials.gov/study/NCT04886284) | Phase 2 | Recruiting | 60 | **CERT Trial**: Directly tests cefazolin + ertapenem combination for MSSA bacteremia; sub-study of the SNAP adaptive platform (NCT05137119); highest-priority evidence source |
| [NCT07376889](https://clinicaltrials.gov/study/NCT07376889) | Phase 4 | Not Yet Recruiting | 2,096 | **COMBAT-SAB**: Large-scale combination antibiotic therapy for S. aureus bacteremia; ertapenem-based regimens expected; results will be landmark |
| [NCT07148960](https://clinicaltrials.gov/study/NCT07148960) | Phase 4 | Enrolling by Invitation | 300 | **SABEDTIO**: Early dual IV antibiotic therapy vs single-agent for SAB; tests whether combination reduces bacteremia duration to <6 days |
| [NCT00366249](https://clinicaltrials.gov/study/NCT00366249) | Phase 3 | Completed | 1,061 | Tigecycline vs ertapenem for diabetic foot infections (RCT); co-primary endpoints not met, but provides large-scale safety and efficacy baseline for ertapenem including MSSA subgroup |
| [NCT06634940](https://clinicaltrials.gov/study/NCT06634940) | N/A | Recruiting | 1,000 | International AMR surveillance in cirrhosis-related bacterial infections; documents resistance context relevant to carbapenem prescribing |
| [NCT06174649](https://clinicaltrials.gov/study/NCT06174649) | N/A | Completed | 900 | FAST Trial: Rapid phenotypic AST for Gram-negative bacteremia; provides diagnostic infrastructure context; indirect relevance only |
| [NCT03218397](https://clinicaltrials.gov/study/NCT03218397) | N/A | Completed | 500 | RAPIDS-GN: Rapid ID and AST for Gram-negative bacteremia; diagnostic study, indirect relevance |
| [NCT06044272](https://clinicaltrials.gov/study/NCT06044272) | N/A | Completed | 10,000 | AMR resistance profiles in Colombian healthcare facilities 2018–2022; epidemiological background data |

---

## Literature Evidence

### Bacterial Arthritis (Rank 1)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31220276](https://pubmed.ncbi.nlm.nih.gov/31220276/) | 2019 | Retrospective Cohort | J Antimicrob Chemother | Subcutaneous ertapenem as prolonged suppressive therapy for prosthetic joint infection and chronic osteomyelitis in 10 patients ineligible for optimal surgery; demonstrates safety and off-label efficacy for bone and joint infection salvage |
| [24709258](https://pubmed.ncbi.nlm.nih.gov/24709258/) | 2014 | Observational/Safety Study | Antimicrob Agents Chemother | Retrospective cohort of 306 OPAT patients on ertapenem (2010–2013); bone and joint infections were a leading indication; confirms long-term safety and efficacy in outpatient settings |
| [37578166](https://pubmed.ncbi.nlm.nih.gov/37578166/) | 2023 | Case Report + Review | J Investig Med High Impact Case Rep | Prevotella bivia (anaerobic Gram-negative) native knee septic arthritis in immunocompetent adult; case initially misdiagnosed; highlights ertapenem's anaerobic coverage critical for unusual pathogens |
| [22233826](https://pubmed.ncbi.nlm.nih.gov/22233826/) | 2011 | Case Report | J Chemotherapy | Klebsiella pneumoniae septic wrist arthritis resolved with ertapenem + levofloxacin combination; direct clinical documentation of ertapenem in septic arthritis |
| [31352398](https://pubmed.ncbi.nlm.nih.gov/31352398/) | 2019 | Case Report | BMJ Case Reports | Citrobacter koseri septic arthritis with osteomyelitis in a diabetic patient; initially misdiagnosed as gout; successfully treated with ertapenem; confirms Gram-negative coverage in metabolically complex patients |
| [31585203](https://pubmed.ncbi.nlm.nih.gov/31585203/) | 2020 | Case Report | Anaerobe | First reported case of Clostridium paraputrificum native shoulder septic arthritis and osteomyelitis; highlights rare anaerobic pathogen requiring broad spectrum coverage |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Retrospective Epidemiology | Clinical Laboratory | Pathogen distribution and AMR patterns in bone and joint infections in children <4 years; informs spectrum coverage requirements and highlights drug resistance trends |
| [38924836](https://pubmed.ncbi.nlm.nih.gov/38924836/) | 2024 | In vitro Research | Diagn Microbiol Infect Dis | Auranofin synergistically restores ertapenem susceptibility in carbapenem-resistant E. coli; mechanistic study supporting novel combination approaches for resistant pathogens |

---

### Staphylococcus aureus Infection (Rank 2)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38946294](https://pubmed.ncbi.nlm.nih.gov/38946294/) | 2024 | Retrospective Comparative Cohort | J Antimicrob Chemother | Carbapenem combination (cefazolin or oxacillin + carbapenem) vs. standard of care for MSSA bacteremia; first comparative effectiveness data supporting the combination strategy |
| [40448546](https://pubmed.ncbi.nlm.nih.gov/40448546/) | 2025 | Retrospective Cohort | J Antimicrob Chemother | Critical safety finding: ertapenem combination therapy for MSSA bacteremia associated with faster blood culture sterilization, but hypoalbuminemia (albumin <2.5 g/dL) may cause suboptimal drug exposure due to high protein binding |
| [31773134](https://pubmed.ncbi.nlm.nih.gov/31773134/) | 2020 | Case Series | Clin Infect Dis | Cefazolin + ertapenem salvage therapy cleared persistent MSSA bacteremia in 11 cases (6 with endocarditis); immediate clearance (≤24 h) achieved in 8 cases; synergistic activity confirmed in rat endocarditis model |
| [27572414](https://pubmed.ncbi.nlm.nih.gov/27572414/) | 2016 | Case Series + Lab | Antimicrob Agents Chemother | Foundational report establishing cefazolin + ertapenem for refractory MSSA bacteremia; in vitro synergy confirmed; murine skin infection model validates combination |
| [39230345](https://pubmed.ncbi.nlm.nih.gov/39230345/) | 2025 | Review | Am J Health-Syst Pharm | Comprehensive review of management strategies for persistent MSSA bacteremia; positions cefazolin + ertapenem as a key salvage strategy with emphasis on timely intervention |
| [15164963](https://pubmed.ncbi.nlm.nih.gov/15164963/) | 2004 | RCT Subgroup Analysis | Int J Antimicrob Agents | Double-blind RCT subgroup: ertapenem 1 g/day vs piperacillin-tazobactam for complicated skin/soft tissue infections caused by MSSA; establishes ertapenem's monotherapy baseline activity against MSSA |
| [35493130](https://pubmed.ncbi.nlm.nih.gov/35493130/) | 2022 | Laboratory Study | Open Forum Infect Dis | Ertapenem + cefazolin shows potent activity within staphylococcal biofilms; explains why the combination is effective in endocarditis, where biofilm is a key resistance mechanism |
| [34978891](https://pubmed.ncbi.nlm.nih.gov/34978891/) | 2022 | Laboratory Study | Antimicrob Agents Chemother | Cefazolin + ertapenem stimulates IL-1β release from peripheral blood monocytes; suggests an immunological augmentation mechanism partially explaining the combination's marked in vivo potency |
| [34599521](https://pubmed.ncbi.nlm.nih.gov/34599521/) | 2021 | Case Series | J Cardiac Surgery | Cefazolin + ertapenem + heart transplantation as salvage for refractory LVAD-related MSSA infection; demonstrates utility in the most complex cardiac device infection scenarios |
| [39935929](https://pubmed.ncbi.nlm.nih.gov/39935929/) | 2025 | Case Report | Cureus | Isolated native pulmonary valve infective endocarditis with persistent S. aureus bacteremia; rapid blood culture clearance achieved with ertapenem + cefazolin combination |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note**: One clinically important signal emerges from the literature (PMID 40448546): ertapenem is highly protein-bound, and patients with **hypoalbuminemia (serum albumin <2.5 g/dL)** may have suboptimal ertapenem plasma exposures. Current guidance advises caution in using ertapenem for Gram-negative infections in this population. This consideration would apply to any MSSA bacteremia or bacterial arthritis indication as well.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
For bacterial arthritis (L3), ertapenem's antimicrobial spectrum directly covers the most common causative pathogens, multiple case reports confirm direct clinical use, and OPAT compatibility makes it logistically practical — but the complete absence of prospective trials limits the evidence grade. For Staphylococcus aureus bacteremia (L2), the cefazolin + ertapenem combination has a well-articulated mechanistic basis, multiple case series, a comparative cohort study, and an actively recruiting Phase 2 RCT (CERT), placing it on an accelerating evidence trajectory.

**To proceed, the following is needed:**

- **MOA documentation**: Retrieve complete mechanism of action from DrugBank API (currently flagged as a data gap)
- **Canada regulatory filing**: Ertapenem is not marketed in Canada (0 DINs); market entry would require a New Drug Submission (NDS) or reliance on a reference country approval
- **Package insert warnings and contraindications**: Download and parse product monograph from Health Canada or a reference jurisdiction (flagged as blocking data gap)
- **Drug interaction assessment**: No DDI data available; a full interaction screen is required before any clinical use
- **Albumin monitoring protocol**: A safety guardrail requiring baseline serum albumin measurement should be established before using ertapenem, with avoidance or dose adjustment in patients with albumin <2.5 g/dL
- **CERT trial results** (NCT04886284): Await Phase 2 data from the dedicated MSSA bacteremia RCT; results expected by July 2026
- **COMBAT-SAB results** (NCT07376889): Large Phase 4 trial; if ertapenem-inclusive arms show benefit, this would upgrade the MSSA indication to L1
- **Prospective study for bacterial arthritis**: A dedicated observational registry or pilot RCT for ertapenem OPAT in septic arthritis would be needed to upgrade from L3 to L2
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

