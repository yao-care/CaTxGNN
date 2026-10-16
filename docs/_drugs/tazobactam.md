---
layout: default
title: Tazobactam
parent: High Evidence (L1-L2)
nav_order: 884
evidence_level: L1
indication_count: 2
last_modified_at: 2026-10-13
description: "Tazobactam: predicted new indication Pneumonia (evidence level L1). Approved use: Bacterial pneumonia, peritonitis, appendicitis…"
monitor_inn: "TAZOBACTAM"
predicted_indications: ["pneumonia", "urinary tract infection (disease)"]
---

# Tazobactam
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **2** 
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

# Tazobactam: From Bacterial Pneumonia to Pneumonia (Hospital-Acquired and Ventilator-Associated)

## One-Sentence Summary

Tazobactam is a beta-lactamase inhibitor used with partner antibiotics such as piperacillin and ceftolozane. It was originally used for bacterial pneumonia, peritonitis, appendicitis and staphylococcal infections.
The TxGNN model predicts it may be effective for **pneumonia**, and the data compiled for this report include **20 clinical trials** and **20 publications** for this indication. Because bacterial pneumonia is already an original indication, this is closer to an on-label or closely related use than to true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial pneumonia, peritonitis, appendicitis, staphylococcal infections (the Canadian licence records contain no indication text) |
| Predicted New Indication | Pneumonia |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L1 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 17 |
| Recommended Decision | Proceed with Guardrails |

A second prediction, urinary tract infection (score 99.12%), is also supported by evidence and is summarised at the end of this report.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, tazobactam is a beta-lactamase inhibitor. It protects partner beta-lactams (piperacillin, ceftolozane) from breakdown by bacterial beta-lactamases and restores their activity against Gram-negative bacteria.

Hospital-acquired and ventilator-associated pneumonia are frequently caused by such Gram-negative bacteria. Bacterial pneumonia is already listed among the drug's original indications, so the predicted indication is a close extension of existing use. This also fits the very high TxGNN score.

All of the evidence concerns tazobactam as part of a combination product (piperacillin-tazobactam or ceftolozane-tazobactam), not as a standalone agent.

---

## Clinical Trial Evidence

The 10 most relevant of the 20 trials are listed below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02070757](https://clinicaltrials.gov/study/NCT02070757) | Phase 3 | Completed | 726 | Ceftolozane/tazobactam vs meropenem in ventilated nosocomial pneumonia; primary endpoint is non-inferiority on Day 28 all-cause mortality (ASPECT-NP) |
| [NCT02493764](https://clinicaltrials.gov/study/NCT02493764) | Phase 3 | Completed | 537 | Imipenem/relebactam vs piperacillin/tazobactam in HABP/VABP; piperacillin/tazobactam is the comparator |
| [NCT00253955](https://clinicaltrials.gov/study/NCT00253955) | Phase 3 | Completed | 460 | Levofloxacin 750 mg vs piperacillin/tazobactam in mild to moderate hospital-acquired pneumonia; non-inferiority design |
| [NCT00438269](https://clinicaltrials.gov/study/NCT00438269) | Phase 2 | Completed | 80 | Pilot randomized trial of appropriate antimicrobial therapy in critical care; tazobactam-specific attribution is indirect |
| [NCT04223752](https://clinicaltrials.gov/study/NCT04223752) | Phase 1 | Completed | 41 | Safety, tolerability and pharmacokinetics of ceftolozane/tazobactam in children with nosocomial pneumonia |
| [NCT02387372](https://clinicaltrials.gov/study/NCT02387372) | Phase 1 | Completed | 37 | Plasma pharmacokinetics and lung penetration of ceftolozane/tazobactam in critically ill patients |
| [NCT06972537](https://clinicaltrials.gov/study/NCT06972537) | N/A | Recruiting | 42 | Model-guided vs empirical dosing of piperacillin-tazobactam in elderly pneumonia patients |
| [NCT06977347](https://clinicaltrials.gov/study/NCT06977347) | N/A | Not yet recruiting | 100 | Piperacillin/tazobactam alone vs plus a fluoroquinolone in severe community-acquired pneumonia (South Korea) |
| [NCT07004049](https://clinicaltrials.gov/study/NCT07004049) | Phase 4 | Recruiting | 600 | TREAT-GNB platform trial of antibiotic strategies for multidrug-resistant Gram-negative bloodstream and lower respiratory infections |
| [NCT01853982](https://clinicaltrials.gov/study/NCT01853982) | Phase 3 | Terminated | 4 | Ceftolozane/tazobactam vs piperacillin/tazobactam in ventilator-associated pneumonia; terminated early, so no usable efficacy data |

Note that several other Phase 3 trials were withdrawn or terminated with very few participants (for example NCT03006679, 0 participants). They provide no evidence.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31563344](https://pubmed.ncbi.nlm.nih.gov/31563344/) | 2019 | RCT | Lancet Infect Dis | ASPECT-NP: ceftolozane-tazobactam vs meropenem in Gram-negative nosocomial pneumonia, double-blind Phase 3 non-inferiority trial |
| [32785589](https://pubmed.ncbi.nlm.nih.gov/32785589/) | 2021 | RCT | Clin Infect Dis | RESTORE-IMI 2: imipenem/cilastatin/relebactam vs piperacillin/tazobactam in HABP/VABP |
| [39674398](https://pubmed.ncbi.nlm.nih.gov/39674398/) | 2025 | RCT | Int J Infect Dis | Phase 3 non-inferiority trial of imipenem/cilastatin/relebactam vs piperacillin/tazobactam in HABP/VABP |
| [38823453](https://pubmed.ncbi.nlm.nih.gov/38823453/) | 2024 | Systematic review | Clin Microbiol Infect | Network meta-analysis of empiric antibiotic regimens in non-ventilator hospital-acquired pneumonia |
| [38971203](https://pubmed.ncbi.nlm.nih.gov/38971203/) | 2024 | Systematic review | Int J Antimicrob Agents | Pharmacokinetics and pharmacodynamics of novel beta-lactam/inhibitor combinations in carbapenem-resistant Gram-negative pneumonia |
| [36543346](https://pubmed.ncbi.nlm.nih.gov/36543346/) | 2022 | Review | Eur Respir Rev | Overview of new antibiotics for Gram-negative pneumonia |
| [35088403](https://pubmed.ncbi.nlm.nih.gov/35088403/) | 2022 | Review | Semin Respir Crit Care Med | New antibiotics for HAP and VAP |
| [32600375](https://pubmed.ncbi.nlm.nih.gov/32600375/) | 2020 | Review | Crit Care | Update on treatment of nosocomial pneumonia in the ICU |
| [38902935](https://pubmed.ncbi.nlm.nih.gov/38902935/) | 2025 | Cohort | Clin Infect Dis | Resistance developed less often with ceftolozane-tazobactam (10%) than with ceftazidime-avibactam (40%) in multidrug-resistant *P. aeruginosa* bacteremia or pneumonia |
| [35699444](https://pubmed.ncbi.nlm.nih.gov/35699444/) | 2022 | Observational | Antimicrob Agents Chemother | Machine-learning analysis of beta-lactam target attainment and outcomes in ICU HAP/VAP |

---

## Canada Market Information

Health Canada records show 17 valid single-ingredient licences and no cancelled ones. The compiled data do not include dosage form or approved indication text. Five of the licences are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02402068 | Piperacillin and Tazobactam for Injection | Not recorded | Not recorded |
| 02446901 | ZERBAXA (ceftolozane/tazobactam) | Not recorded | Not recorded |
| 02377748 | Piperacillin and Tazobactam for Injection | Not recorded | Not recorded |
| 02528703 | Piperacillin and Tazobactam for Injection | Not recorded | Not recorded |
| 02362627 | Piperacillin and Tazobactam for Injection | Not recorded | Not recorded |

---

## Safety Considerations

Label warnings and contraindications were not available. Please refer to the package insert for safety information.

The following comes from the TxGNN knowledge graph (disease-level contraindication links, not label text). Diseases linked to tazobactam as contraindications or cautions include:
- Kidney disease
- Neutropenia and agranulocytosis
- Blood coagulation disease
- *Clostridium difficile* colitis
- Perinatal necrotizing enterocolitis
- Pyoureter
- Infectious mononucleosis and chronic Epstein-Barr virus infection syndrome

No drug interaction records were found.

---

## Second Predicted Indication: Urinary Tract Infection

The TxGNN score is 99.12% and the evidence level is L1. Key support comes from:
- **[NCT03687255](https://clinicaltrials.gov/study/NCT03687255)** (Phase 3, completed, 1,043 participants): cefepime-enmetazobactam vs piperacillin/tazobactam in complicated UTI. Piperacillin/tazobactam is the comparator (published as [PMID 36194218](https://pubmed.ncbi.nlm.nih.gov/36194218/), JAMA 2022).
- **[PMID 30861061](https://pubmed.ncbi.nlm.nih.gov/30861061/)** (RCT, 2019): fosfomycin vs piperacillin-tazobactam in complicated UTI.
- **[PMID 29486041](https://pubmed.ncbi.nlm.nih.gov/29486041/)** (2018): meropenem-vaborbactam vs piperacillin-tazobactam in complicated UTI (TANGO I).
- **[NCT02728089](https://clinicaltrials.gov/study/NCT02728089)** (Phase 3, completed, 115 participants): ceftolozane/tazobactam in Japanese patients with pyelonephritis and complicated UTI.
- **[NCT03891433](https://clinicaltrials.gov/study/NCT03891433)** (Phase 4, suspended, 198 participants): piperacillin/tazobactam vs carbapenems in ESBL-producing UTI. No conclusions can be drawn while it is suspended.

In these trials piperacillin-tazobactam is mostly the comparator, so they show its role as a reference treatment but not its own superiority. There are also efficacy concerns for ESBL-producing organisms, which call for guardrails.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several completed Phase 3 randomized trials (ASPECT-NP, RESTORE-IMI 2 and others) involve tazobactam-containing regimens in pneumonia, and the drug is already marketed in Canada. However, the evidence concerns combination products, tazobactam is often only the comparator, and label safety data are missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (a blocking gap for safety screening)
- Detailed mechanism of action data
- Approved indication text and dosage forms for the Canadian licences
- Clarification of which partner antibiotic and dosing regimen apply, since tazobactam is not used alone
- A plan for monitoring kidney function, blood counts, coagulation and *C. difficile* risk
- Review of resistance patterns, especially ESBL-producing organisms, before use in specific populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

