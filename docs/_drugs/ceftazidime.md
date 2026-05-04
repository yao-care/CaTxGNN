---
layout: default
title: Ceftazidime
parent: 僅模型預測 (L5)
nav_order: 139
evidence_level: L5
indication_count: 10
---

# Ceftazidime
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

# Ceftazidime: From Gram-Negative Bacterial Infections to Urinary Tract Infection

## One-Sentence Summary

Ceftazidime is a third-generation cephalosporin antibiotic with well-established global use for serious gram-negative bacterial infections, including pneumonia, septicemia, and complicated intra-abdominal infections — yet it carries no current Canadian Drug Identification Number (DIN).
The TxGNN model predicts it may be effective for **Urinary Tract Infection (UTI)**, with **17 clinical trials** and **20 publications** currently supporting this direction.
Notably, this prediction does not represent a novel repurposing hypothesis; it reflects an already-established global clinical application, and the "not marketed in Canada" status almost certainly reflects a regulatory/commercial data gap rather than an absence of clinical evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gram-negative bacterial infections (established globally; no Canadian DIN on record) |
| Predicted New Indication | Urinary Tract Infection (UTI) |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L1 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data was not available in this Evidence Pack. Based on established pharmacology, ceftazidime exerts bactericidal activity by inhibiting bacterial cell wall synthesis through irreversible binding to penicillin-binding proteins (PBPs) — specifically PBP-3 — in gram-negative organisms. This disrupts cell wall cross-linking, triggering bacterial lysis. Critically, ceftazidime maintains potent activity against the most common uropathogens: *Escherichia coli*, *Klebsiella pneumoniae*, and *Pseudomonas aeruginosa*, the last of which is uniquely difficult to treat and represents ceftazidime's key clinical niche.

From a pharmacokinetic standpoint, ceftazidime is predominantly renally eliminated unchanged, resulting in high urinary drug concentrations after intravenous administration. This makes it inherently well-suited for treating lower and upper urinary tract infections. For complicated UTIs — particularly in ICU patients, post-surgical patients, and those with urinary catheters — *Pseudomonas aeruginosa* and carbapenem-resistant gram-negative organisms are major concerns, and ceftazidime (especially in combination with avibactam) represents a guideline-supported treatment option.

The TxGNN model's strong prediction score (99.41%) for UTI is therefore clinically coherent and consistent with over three decades of published evidence. Multiple regulatory agencies worldwide — including the US FDA and EMA — have approved ceftazidime and ceftazidime-containing combinations specifically for complicated UTI. The absence of a Canadian DIN should be treated as an administrative/commercial gap requiring regulatory action, not as a signal of clinical uncertainty.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00690378](https://clinicaltrials.gov/study/NCT00690378) | Phase 2 | Completed | 137 | Multicenter, randomized, investigator-blinded trial of NXL104 + ceftazidime vs. comparator for complicated UTI in hospitalized adults; directly evaluates safety and efficacy for this indication |
| [NCT04882085](https://clinicaltrials.gov/study/NCT04882085) | Phase 4 | Completed | 60 | Open-label, randomized, multicenter active-controlled trial of ceftazidime-avibactam vs. best available therapy for carbapenem-resistant gram-negative infections (including cUTI) in Chinese adults |
| [NCT04628572](https://clinicaltrials.gov/study/NCT04628572) | N/A | Completed | 189 | Real-world retrospective multicenter analysis of ceftazidime-avibactam treatment patterns, effectiveness, and safety in India; includes UTI as a key infection type |
| [NCT02497781](https://clinicaltrials.gov/study/NCT02497781) | Phase 2 | Completed | 97 | Single-blind RCT of ceftazidime-avibactam vs. cefepime for complicated UTI in pediatric patients aged 3 months to under 18 years; evaluates safety, tolerability, and efficacy |
| [NCT00921024](https://clinicaltrials.gov/study/NCT00921024) | Phase 2 | Completed | 129 | Double-blind multicenter RCT using ceftazidime as active comparator arm for complicated UTI including pyelonephritis; validates ceftazidime as a reference standard |
| [NCT05258851](https://clinicaltrials.gov/study/NCT05258851) | Phase 3 | Terminated | 29 | Non-inferiority RCT of ceftazidime-avibactam vs. colistin for carbapenem-resistant Enterobacteriaceae infections in ICU (terminated early due to enrolment challenges) |
| [NCT01601093](https://clinicaltrials.gov/study/NCT01601093) | Phase 2 | Suspended | 288 | Phase 2 study evaluating efficacy and safety of ceftazidime sodium + sulbactam sodium for respiratory and urinary tract acute bacterial infections |
| [NCT05733104](https://clinicaltrials.gov/study/NCT05733104) | N/A | Recruiting | 600 | Post-marketing surveillance study of Zavicefta (ceftazidime-avibactam) required by Korean MFDS; observes safety and effectiveness for UTI and other serious infections |
| [NCT03147807](https://clinicaltrials.gov/study/NCT03147807) | N/A | Completed | 75 | ICU trial evaluating BetaLACTA test-guided de-escalation of carbapenems in urinary, pulmonary, and bloodstream infections; ceftazidime is a key de-escalation agent |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Recruiting | 5,000 | Large pediatric PK/PD and safety study collecting ceftazidime renal dosing data across understudied populations; highly relevant to UTI dosing optimization |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [39817442](https://pubmed.ncbi.nlm.nih.gov/39817442/) | 2025 | Systematic Review & NMA | J Comparative Effectiveness Research | Network meta-analysis comparing treatment options for complicated UTI including acute pyelonephritis; evaluates the role of ceftazidime-class agents relative to carbapenems and newer combinations |
| [32094128](https://pubmed.ncbi.nlm.nih.gov/32094128/) | 2020 | Head-to-Head Comparative Study | Antimicrob Agents Chemother | Multicenter retrospective cohort comparing ceftazidime-avibactam vs. meropenem-vaborbactam for carbapenem-resistant Enterobacteriaceae infections; characterizes ceftazidime-avibactam's comparative effectiveness |
| [33618353](https://pubmed.ncbi.nlm.nih.gov/33618353/) | 2021 | Retrospective Cohort | Clin Infect Dis | Multicenter observational study of ceftazidime-avibactam for KPC-producing *Klebsiella pneumoniae* infections; supports real-world efficacy in serious gram-negative infections including UTI |
| [38688353](https://pubmed.ncbi.nlm.nih.gov/38688353/) | 2024 | Clinical Practice Review | Int J Antimicrob Agents | Joint Italian (SIMIT) and French (SPILF) infectious disease society practice guidance for multidrug-resistant gram-negative bacilli; recommends ceftazidime-avibactam combinations |
| [35787918](https://pubmed.ncbi.nlm.nih.gov/35787918/) | 2022 | Review | Int J Antimicrob Agents | Review of clinical evidence for novel antibiotics against MDR gram-negative bacteria; highlights ceftazidime-avibactam trial data across UTI, HAP, and cIAI |
| [39934901](https://pubmed.ncbi.nlm.nih.gov/39934901/) | 2025 | Systematic Review & Meta-Analysis | Antimicrob Resist Infect Control | Global trends of ceftazidime-avibactam resistance in gram-negative bacteria; provides resistance surveillance context critical for UTI indication planning |
| [30219824](https://pubmed.ncbi.nlm.nih.gov/30219824/) | 2019 | Review / PK Analysis | Clin Infect Dis | Discusses regulatory landscape and clinical implications of antibiotic renal dose adjustments; highlights ceftazidime/avibactam PK considerations in AKI — directly relevant to UTI patients with renal compromise |
| [40530972](https://pubmed.ncbi.nlm.nih.gov/40530972/) | 2025 | PK/PD Modeling | Antimicrob Agents Chemother | Population PK/PD modeling for aztreonam-avibactam (a ceftazidime-class successor); cUTI is explicitly listed as one of the approved indications providing regulatory precedent context |
| [37873539](https://pubmed.ncbi.nlm.nih.gov/37873539/) | 2023 | Observational Study | Open Medicine | Antibiogram analysis of UTI-causing bacteria in chronic kidney disease patients; documents ceftazidime susceptibility profiles against common uropathogens in a real-world setting |
| [29493397](https://pubmed.ncbi.nlm.nih.gov/29493397/) | 2018 | Expert Review | Expert Rev Anti-infective Therapy | Review of ceftolozane/tazobactam (structurally related to ceftazidime); positions ceftazidime as the structural and pharmacological reference agent for complicated UTI treatment |

---

## Canada Market Information

No Drug Identification Numbers (DINs) are registered for ceftazidime in Canada. Ceftazidime is not currently marketed domestically; therefore, no approved indication text, product monograph, or Canadian regulatory history is available from this dataset.

Ceftazidime is broadly registered internationally under brand names such as **Fortaz** and **Tazicef** (US), and as part of the **Avycaz** combination (ceftazidime-avibactam) in the US and EU for complicated UTI, cIAI, and hospital-acquired pneumonia. The absence of a Canadian DIN is best interpreted as a commercial/historical regulatory gap rather than a signal of safety or efficacy concerns.

---

## Safety Considerations

No Canadian-specific safety data (warnings, contraindications, or drug-drug interactions) are available, as no Canadian product monograph exists for ceftazidime.

Please refer to internationally approved package inserts (e.g., US FDA full prescribing information, EMA Summary of Product Characteristics) for comprehensive safety information. Based on the broader third-generation cephalosporin class profile, clinicians should be aware of:

- **Hypersensitivity**: Risk of allergic reactions; cross-reactivity with penicillins occurs in a small minority of patients
- **Renal dosing**: Dose adjustment is required for creatinine clearance below 50 mL/min, particularly important in UTI patients who may have concurrent renal impairment
- **CNS effects**: Seizures, encephalopathy, and neuromuscular excitability reported at supratherapeutic concentrations, especially in renal failure
- **_Clostridioides difficile_-associated disease**: Risk of antibiotic-associated colitis, as with all broad-spectrum antibiotics

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ceftazidime has robust Phase 2–4 randomized clinical trial evidence and extensive real-world data confirming efficacy for urinary tract infections, particularly complicated UTIs caused by gram-negative organisms including *Pseudomonas aeruginosa* and carbapenem-resistant Enterobacteriaceae. The "not marketed in Canada" status represents an administrative gap — not a clinical evidence gap — and should not be a barrier to further evaluation.

**To proceed, the following is needed:**
- Obtain a product monograph from an approved jurisdiction (US FDA, EMA) to populate the missing warnings, contraindications, and dosing guidance required for a Canadian submission
- Consult Health Canada on the appropriate regulatory pathway (e.g., New Drug Submission under C.08.004, or reliance on a reference jurisdiction approval)
- Evaluate the strategic relationship to **ceftazidime-avibactam** (Avycaz), which may be the more clinically relevant formulation given the current landscape of resistance and may represent a more commercially viable filing
- Conduct a Canadian antimicrobial resistance surveillance review to quantify the local burden of ceftazidime-susceptible uropathogens and identify the patient population with unmet need
- Develop a pharmacovigilance and antimicrobial stewardship plan to accompany any market authorization application, consistent with Health Canada's AMROC (Antimicrobial Resistance and One Health Consortium) priorities

---

> ⚠️ **Disclaimer**: This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All content should be reviewed by qualified clinical and regulatory professionals before any decision-making.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

