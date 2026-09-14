---
layout: default
title: Tazobactam
parent: 僅模型預測 (L5)
nav_order: 750
evidence_level: L5
indication_count: 2
---

# Tazobactam
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

Using no additional tooling — this is a direct content-generation task against the fully-specified template already provided, so I'll produce the report directly from the Evidence Pack.

# Tazobactam: From Antibacterial Combination Therapy to Pneumonia

## One-Sentence Summary

> Tazobactam is a β-lactamase inhibitor that has no standalone approved indication of its own — it is used exclusively as a component of combination antibiotics (e.g., piperacillin/tazobactam, ceftolozane/tazobactam).
> The TxGNN model predicts it may be effective for **Pneumonia**,
> with **50 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | None on file — tazobactam is not marketed as a standalone product; it is used exclusively as a β-lactamase inhibitor component in combination antibiotics (e.g., piperacillin/tazobactam, ceftolozane/tazobactam) |
| Predicted New Indication | Pneumonia |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L1 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available directly from DrugBank for this entry (data gap DG002). Based on information within the clinical literature captured in this evidence pack, tazobactam is a β-lactamase inhibitor with negligible intrinsic antibacterial activity on its own; it is co-administered with β-lactam antibiotics such as piperacillin to protect them from hydrolysis by extended-spectrum and AmpC β-lactamases, thereby restoring activity against β-lactamase-producing Gram-negative and Gram-positive organisms (Perry & Markham, 1999, PMID 10353303).

Because tazobactam has no standalone original indication, "pneumonia" is not truly a novel target — it reflects the already well-established clinical use of tazobactam-containing combinations (piperacillin/tazobactam, ceftolozane/tazobactam) in hospital-acquired and ventilator-associated bacterial pneumonia (HABP/VABP). This is confirmed repeatedly in the evidence base, where piperacillin/tazobactam and ceftolozane/tazobactam appear as either the active comparator or the study drug in multiple completed Phase 3 trials for exactly this indication.

Mechanistically, nosocomial and ventilator-associated pneumonia are frequently caused by β-lactamase-producing Gram-negative pathogens (e.g., *Pseudomonas aeruginosa*, ESBL-producing Enterobacterales). Tazobactam's role in restoring β-lactam efficacy against these organisms directly supports its continued applicability in this indication class, making this prediction a **confirmatory** rather than **exploratory** finding.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02070757](https://clinicaltrials.gov/study/NCT02070757) | Phase 3 | Completed | 726 | Ceftolozane/tazobactam non-inferior to meropenem in ventilated nosocomial pneumonia (Day 28 all-cause mortality) |
| [NCT02493764](https://clinicaltrials.gov/study/NCT02493764) | Phase 3 | Completed | 537 | Imipenem/relebactam vs. piperacillin/tazobactam in HABP/VABP; piperacillin/tazobactam as active comparator |
| [NCT03583333](https://clinicaltrials.gov/study/NCT03583333) | Phase 3 | Completed | 274 | Multinational confirmatory trial, imipenem/cilastatin/relebactam vs. piperacillin/tazobactam in HABP/VABP |
| [NCT00253955](https://clinicaltrials.gov/study/NCT00253955) | Phase 3 | Completed | 460 | Levofloxacin vs. piperacillin/tazobactam in mild-to-moderate hospital-acquired pneumonia |
| [NCT01853982](https://clinicaltrials.gov/study/NCT01853982) | Phase 3 | Terminated | 4 | Ceftolozane/tazobactam vs. piperacillin/tazobactam in ventilator-associated pneumonia |
| [NCT03006679](https://clinicaltrials.gov/study/NCT03006679) | Phase 3b | Withdrawn | 0 | Meropenem-vaborbactam vs. piperacillin/tazobactam in HABP/VABP (TANGO III) |
| [NCT04986254](https://clinicaltrials.gov/study/NCT04986254) | N/A | Completed | 179 | Individualized dosing regimens for ICU pneumonia including piperacillin/tazobactam; PK/PD optimization |
| [NCT03581370](https://clinicaltrials.gov/study/NCT03581370) | Phase 3 | Recruiting | 80 | Infusion strategy comparison for ceftolozane-tazobactam in *P. aeruginosa* VAP |
| [NCT02735707](https://clinicaltrials.gov/study/NCT02735707) | Phase 3 | Recruiting | 20,000 | REMAP-CAP adaptive platform trial for community-acquired pneumonia, includes beta-lactam treatment arms |
| [NCT04223752](https://clinicaltrials.gov/study/NCT04223752) | Phase 1 | Completed | 41 | Ceftolozane/tazobactam PK/safety in pediatric nosocomial pneumonia |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30208454](https://pubmed.ncbi.nlm.nih.gov/30208454/) | 2018 | RCT | JAMA | Piperacillin-tazobactam vs. meropenem for ceftriaxone-resistant *E. coli*/*K. pneumoniae* bloodstream infection — 30-day mortality outcomes |
| [32785589](https://pubmed.ncbi.nlm.nih.gov/32785589/) | 2021 | RCT | Clin Infect Dis | RESTORE-IMI 2: Imipenem/cilastatin/relebactam vs. piperacillin/tazobactam in HABP/VABP |
| [31563344](https://pubmed.ncbi.nlm.nih.gov/31563344/) | 2019 | RCT | Lancet Infect Dis | ASPECT-NP: Ceftolozane-tazobactam vs. meropenem in Gram-negative nosocomial pneumonia |
| [39674398](https://pubmed.ncbi.nlm.nih.gov/39674398/) | 2025 | RCT | Int J Infect Dis | Phase 3 non-inferiority trial of imipenem/cilastatin/relebactam vs. piperacillin/tazobactam in HABP/VABP |
| [38971203](https://pubmed.ncbi.nlm.nih.gov/38971203/) | 2024 | Systematic Review | Int J Antimicrob Agents | PK/PD review of novel beta-lactams and beta-lactam/inhibitor combinations for MDR pneumonia |
| [38823453](https://pubmed.ncbi.nlm.nih.gov/38823453/) | 2024 | Systematic Review / Meta-analysis | Clin Microbiol Infect | Network meta-analysis of empiric antibiotic regimens for non-ventilator HAP |
| [35488823](https://pubmed.ncbi.nlm.nih.gov/35488823/) | 2022 | Review | Rev Esp Quimioter | Review of ceftolozane-tazobactam in nosocomial pneumonia |
| [32662691](https://pubmed.ncbi.nlm.nih.gov/32662691/) | 2020 | Review | Expert Rev Anti Infect Ther | Ceftolozane and tazobactam for hospital-acquired pneumonia |
| [34598422](https://pubmed.ncbi.nlm.nih.gov/34598422/) | 2021 | Review | Rev Esp Quimioter | Clinical positioning of ceftolozane-tazobactam: when, how and why to use it |
| [10353303](https://pubmed.ncbi.nlm.nih.gov/10353303/) | 1999 | Review | Drugs | Foundational review of piperacillin/tazobactam spectrum and clinical efficacy across respiratory and other infections |

---

## Canada Market Information

Tazobactam is not currently marketed in Canada as a standalone product; no Health Canada Drug Identification Numbers (DINs) were found for this ingredient. Tazobactam is only available in Canada as a component of fixed-dose combination products (e.g., piperacillin/tazobactam, ceftolozane/tazobactam), which are not captured under this ingredient-level regulatory record.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Note:** Canadian product-specific warnings, contraindications, and drug interaction data for tazobactam are not currently available in this evidence pack. This is flagged internally as a **Blocking**-severity data gap (DG001), which prevents completion of the initial safety screening (S1) required before this candidate can advance further.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Efficacy evidence is strong — tazobactam-containing combinations (piperacillin/tazobactam, ceftolozane/tazobactam) already have multiple completed Phase 3 RCTs demonstrating efficacy in hospital-acquired and ventilator-associated bacterial pneumonia, meeting the L1 evidence bar. However, a Blocking-severity gap in TFDA/Health Canada product safety labeling (DG001) currently prevents a complete safety assessment, and formal MOA documentation (DG002) is also missing. A secondary predicted indication, urinary tract infection (TxGNN score 99.12%), shows the same L1 evidence pattern and was independently assessed as "Proceed with Guardrails" at decision stage S3 — reinforcing that both predictions largely confirm existing, well-established clinical use of tazobactam-based combinations rather than identifying a truly novel indication.

**To proceed, the following is needed:**
- Health Canada / manufacturer product monograph for tazobactam-containing combinations, to resolve the blocking safety data gap (DG001)
- Formal DrugBank mechanism-of-action documentation (DG002)
- Clarification of which specific tazobactam-containing product (piperacillin/tazobactam vs. ceftolozane/tazobactam) is the intended repurposing target, since tazobactam itself holds no standalone Canadian license
- Explicit acknowledgment that this candidate is confirmatory of existing standard-of-care use rather than an exploratory repurposing signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

