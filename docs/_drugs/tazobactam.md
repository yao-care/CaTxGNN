---
layout: default
title: Tazobactam
parent: High Evidence (L1-L2)
nav_order: 877
evidence_level: L1
indication_count: 2
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

# Tazobactam: From Antibacterial Combination Partner to Pneumonia

## One-Sentence Summary

Tazobactam is a beta-lactamase inhibitor that is not used alone. It is paired with partner antibiotics such as piperacillin and ceftolozane to protect them from bacterial enzymes.
The TxGNN model predicts it may be effective for **pneumonia**, with **50 clinical trials** and **20 publications** retrieved. Many of these are only loosely related, but several completed Phase 3 trials involve tazobactam-containing regimens.
Pneumonia is already a recognized use of these combinations, so this prediction mostly confirms existing use rather than opening a new indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Pneumonia |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L1 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 17 |
| Recommended Decision | Proceed with Guardrails |

The records do not list an original approved indication, so that row is omitted.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available from DrugBank. Based on known information, tazobactam has no meaningful antibacterial activity on its own. It is a beta-lactamase inhibitor that protects partner beta-lactams (piperacillin, ceftolozane) from hydrolysis by class A and some class C enzymes, including extended-spectrum beta-lactamases (ESBLs).

This protection extends the partner drug's coverage to Enterobacterales and *Pseudomonas aeruginosa*, which are major causes of hospital-acquired and ventilator-associated pneumonia. That fits the model's high score.

Tazobactam-containing combinations (piperacillin-tazobactam, ceftolozane-tazobactam) are already recognized treatments for pneumonia. The prediction is therefore better read as support for existing use. Any recommendation applies only to tazobactam as a combination partner, never as a single agent.

---

## Clinical Trial Evidence

Of the 50 trials retrieved, the most relevant are listed below. Several others cover stewardship, diagnostics, or other drugs, and are not tazobactam-specific.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02070757](https://clinicaltrials.gov/study/NCT02070757) | Phase 3 | Completed | 726 | Ceftolozane/tazobactam vs meropenem in ventilated nosocomial pneumonia; primary endpoint is non-inferiority on Day 28 all-cause mortality |
| [NCT02493764](https://clinicaltrials.gov/study/NCT02493764) | Phase 3 | Completed | 537 | Imipenem/relebactam vs piperacillin/tazobactam in HABP/VABP; non-inferiority on all-cause mortality |
| [NCT03583333](https://clinicaltrials.gov/study/NCT03583333) | Phase 3 | Completed | 274 | Multi-national study of imipenem/relebactam vs piperacillin/tazobactam in HABP/VABP |
| [NCT00253955](https://clinicaltrials.gov/study/NCT00253955) | Phase 3 | Completed | 460 | Levofloxacin vs piperacillin/tazobactam in mild to moderate hospital-acquired pneumonia; clinical non-inferiority at test of cure |
| [NCT01853982](https://clinicaltrials.gov/study/NCT01853982) | Phase 3 | Terminated | 4 | Ceftolozane/tazobactam vs piperacillin/tazobactam in ventilator-associated pneumonia; stopped very early, so little usable data |
| [NCT01796717](https://clinicaltrials.gov/study/NCT01796717) | Phase 2/3 | Unknown | 50 | Prolonged vs regular infusion of piperacillin/tazobactam in ICU nosocomial pneumonia; clinical, bacteriologic, PK and safety endpoints |
| [NCT02387372](https://clinicaltrials.gov/study/NCT02387372) | Phase 1 | Completed | 37 | Plasma pharmacokinetics and lung penetration of ceftolozane/tazobactam in critically ill patients |
| [NCT03581370](https://clinicaltrials.gov/study/NCT03581370) | Phase 3 | Recruiting | 80 | Short vs prolonged infusion of ceftolozane-tazobactam in *P. aeruginosa* VAP; compares PK exposure |
| [NCT06972537](https://clinicaltrials.gov/study/NCT06972537) | N/A | Recruiting | 42 | Model-guided vs empirical piperacillin-tazobactam dosing for pneumonia in elderly patients |
| [NCT06977347](https://clinicaltrials.gov/study/NCT06977347) | N/A | Not yet recruiting | 100 | Piperacillin/tazobactam alone vs plus a fluoroquinolone in severe community-acquired pneumonia (Korea) |

---

## Literature Evidence

Of the 20 publications retrieved, the most relevant are listed below. The abstracts available here describe study design and aims, so findings are summarized at that level.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31563344](https://pubmed.ncbi.nlm.nih.gov/31563344/) | 2019 | RCT | Lancet Infect Dis | ASPECT-NP: double-blind Phase 3 non-inferiority trial of ceftolozane-tazobactam vs meropenem in Gram-negative nosocomial pneumonia |
| [32785589](https://pubmed.ncbi.nlm.nih.gov/32785589/) | 2021 | RCT | Clin Infect Dis | RESTORE-IMI 2: imipenem/cilastatin/relebactam vs piperacillin/tazobactam in HABP/VABP |
| [39674398](https://pubmed.ncbi.nlm.nih.gov/39674398/) | 2025 | RCT | Int J Infect Dis | Phase III non-inferiority trial of imipenem/cilastatin/relebactam vs piperacillin/tazobactam in HABP/VABP |
| [38823453](https://pubmed.ncbi.nlm.nih.gov/38823453/) | 2024 | Systematic Review / NMA | Clin Microbiol Infect | Network meta-analysis of RCTs on empiric antibiotic regimens in non-ventilator hospital-acquired pneumonia |
| [38971203](https://pubmed.ncbi.nlm.nih.gov/38971203/) | 2024 | Systematic Review | Int J Antimicrob Agents | PK/PD of novel beta-lactam/inhibitor combinations for pneumonia caused by carbapenem-resistant Gram-negative bacteria |
| [39701120](https://pubmed.ncbi.nlm.nih.gov/39701120/) | 2025 | Cohort | Lancet Infect Dis | CACTUS: multicentre retrospective comparison of ceftolozane-tazobactam and ceftazidime-avibactam for multidrug-resistant *P. aeruginosa* |
| [38902935](https://pubmed.ncbi.nlm.nih.gov/38902935/) | 2025 | Cohort | Clin Infect Dis | Resistance emergence was 10% with ceftolozane-tazobactam vs 40% with ceftazidime-avibactam in MDR *P. aeruginosa* bacteremia or pneumonia |
| [32662691](https://pubmed.ncbi.nlm.nih.gov/32662691/) | 2020 | Review | Expert Rev Anti Infect Ther | Review of ceftolozane and tazobactam in hospital-acquired pneumonia |
| [34158237](https://pubmed.ncbi.nlm.nih.gov/34158237/) | 2021 | Observational (propensity-matched) | J Infect Chemother | Ceftriaxone vs piperacillin-tazobactam or carbapenems in aspiration pneumonia |
| [41305690](https://pubmed.ncbi.nlm.nih.gov/41305690/) | 2025 | Case report | Medicine | Piperacillin-tazobactam-induced hemophagocytic lymphohistiocytosis in a patient with community-acquired pneumonia; a rare but serious adverse reaction |

---

## Canada Market Information

17 DINs are on record. The first five are shown below. Dosage form and approved-indication text are not available in the current records.

| DIN | Product Name |
|---------|------|
| 2402068 | Piperacillin and Tazobactam for Injection |
| 2446901 | Zerbaxa (ceftolozane/tazobactam) |
| 2377748 | Piperacillin and Tazobactam for Injection |
| 2528703 | Piperacillin and Tazobactam for Injection |
| 2362627 | Piperacillin and Tazobactam for Injection |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several completed Phase 3 trials, including ASPECT-NP, RESTORE-IMI 2 and NCT00253955, test tazobactam-containing regimens in nosocomial pneumonia, which supports L1 evidence. Tazobactam works only as a combination partner, so any use must be as piperacillin-tazobactam or ceftolozane-tazobactam, never alone.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are not yet available and are needed for safety screening
- Detailed mechanism of action data from DrugBank
- Approved indication text for the 17 Canadian DINs, to confirm whether pneumonia is already on label
- Verification of study drugs for trials with truncated records (for example, NCT02387372)
- A dosing and monitoring plan for special populations, since several trials show exposure varies in critically ill patients, those on renal replacement therapy, and the elderly
- Awareness of rare serious adverse reactions reported in the literature (for example, drug-induced hemophagocytic lymphohistiocytosis)

A second predicted indication, urinary tract infection (score 99.1%), also has Phase 3 trial support involving piperacillin-tazobactam comparators and could be evaluated separately.

---

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

