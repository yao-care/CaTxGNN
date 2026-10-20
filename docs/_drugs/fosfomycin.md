---
layout: default
title: Fosfomycin
parent: Model Prediction Only (L5)
nav_order: 413
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Fosfomycin: predicted new indication Ureaplasma urethritis (evidence level L5). Approved use: Urinary tract infection"
monitor_inn: "FOSFOMYCIN"
predicted_indications: ["Ureaplasma urethritis", "gonococcal urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "epiglottitis", "urogenital tuberculosis", "laryngitis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "pyelitis"]
---

# Fosfomycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Fosfomycin: From Urinary Tract Infection to Ureaplasma Urethritis

## One-Sentence Summary

Fosfomycin is an antibiotic originally used to treat urinary tract infection.
The TxGNN model's top-ranked prediction is **Ureaplasma urethritis** (score 99.99%), but the data compiled for this report show **no clinical trials and no publications** for it, so this top prediction rests on model output alone.
The best-supported candidate among the 10 predictions is **pyelitis** (L1 evidence, one Phase 2/3 RCT), and it is largely an extension of the existing urinary tract infection use. It is covered in a separate section below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection |
| Predicted New Indication | Ureaplasma urethritis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (for the top prediction) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold (top prediction). Pyelitis: Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data were not available in the compiled data. Based on general knowledge, fosfomycin inhibits MurA (UDP-N-acetylglucosamine enolpyruvyl transferase), which blocks an early step of bacterial cell wall (peptidoglycan) synthesis. It reaches high concentrations in urine, which is why it works for urinary tract infection.

**The top prediction (Ureaplasma urethritis) is biologically doubtful.** Ureaplasma species have no cell wall, so a drug that blocks peptidoglycan synthesis is not expected to work. The high score most likely reflects the disease's closeness to urinary and genital tract infection in the knowledge graph, not a real mechanistic link.

Other predictions fall into three groups:

- **Biologically plausible with clinical evidence:**
  - Gonococcal urethritis: *Neisseria gonorrhoeae* has a cell wall, and a 2016 RCT and a 1977 clinical series exist.
  - Pyelitis: it sits within the pyelonephritis/complicated UTI spectrum that fosfomycin already treats.
- **Related but weakly supported:** xanthogranulomatous pyelonephritis (usually needs surgery), uterine inflammatory disease, epiglottitis and laryngitis. There is no disease-specific evidence for these.
- **Likely network artifacts:** urogenital tuberculosis, polyclonal hyperviscosity syndrome and hyperamylasemia. No plausible mechanism links fosfomycin to these.

---

## Clinical Trial Evidence

For the top prediction (Ureaplasma urethritis): Currently no related clinical trials registered.

Across the other predictions, the only registered trials were for uterine inflammatory disease. Neither is specific to the disease or to fosfomycin efficacy:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | Completed | 3520 | Pediatric pharmacokinetics of understudied drugs given as standard care (general PK study, low relevance) |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Recruiting | 5000 | PK, pharmacodynamics and safety of understudied drugs in children and young adults (general program, low relevance) |

---

## Literature Evidence

For the top prediction (Ureaplasma urethritis): Currently no related literature available.

Selected publications for the more relevant alternative predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30861061](https://pubmed.ncbi.nlm.nih.gov/30861061/) | 2019 | RCT (Phase 2/3) | Clin Infect Dis | ZEUS trial: IV fosfomycin (ZTI-01) vs piperacillin-tazobactam in complicated UTI including acute pyelonephritis (pyelitis) |
| [27064136](https://pubmed.ncbi.nlm.nih.gov/27064136/) | 2016 | RCT | Clin Microbiol Infect | Open RCT of fosfomycin trometamol 3 g in 152 men with uncomplicated gonococcal urethritis (126 completed); efficacy outcome truncated in the data (gonococcal urethritis) |
| [39817442](https://pubmed.ncbi.nlm.nih.gov/39817442/) | 2025 | Systematic review / network meta-analysis | J Comp Eff Res | Efficacy of treatment options for complicated UTI including acute pyelonephritis (pyelitis) |
| [41711122](https://pubmed.ncbi.nlm.nih.gov/41711122/) | 2026 | Clinical study/Review | Ann Pharmacother | Place in therapy of IV fosfomycin for the newly FDA-approved complicated UTI indication (pyelitis) |
| [32303061](https://pubmed.ncbi.nlm.nih.gov/32303061/) | 2020 | Observational | J Antimicrob Chemother | One-year review of oral fosfomycin outcomes in pyelonephritis and complicated UTI (pyelitis) |
| [31160291](https://pubmed.ncbi.nlm.nih.gov/31160291/) | 2019 | Preclinical | Antimicrob Agents Chemother | Oral fosfomycin showed unexpected activity against resistant *E. coli* in murine pyelonephritis (pyelitis) |
| [832528](https://pubmed.ncbi.nlm.nih.gov/832528/) | 1977 | Clinical series (uncontrolled) | Chemotherapy | 70 patients with gonococcal urethritis given intramuscular fosfomycin; cure rates of 92% (4 g in divided doses) and 86% (single 4 g dose) (gonococcal urethritis) |
| [11489366](https://pubmed.ncbi.nlm.nih.gov/11489366/) | 2001 | Clinical study | Auris Nasus Larynx | Fosfomycin nebulizer therapy in chronic sinusitis; indirect, does not address laryngitis |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02488086 | IVOZFO | Not specified | Not specified |
| 02473801 | JAMP-FOSFOMYCIN | Not specified | Not specified |
| 02240335 | MONUROL | Not specified | Not specified |

All three authorizations are valid single-ingredient products.

---

## Safety Considerations

- **Contraindication-related diseases (from the knowledge graph, not label text):** kidney disease, pyoureter, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis.
- **Drug Interactions (3 found):**
  - Balsalazide: Moderate
  - Picosulfuric acid: Moderate
  - Metoclopramide: Minor
- For IV use, consider renal function dosing and sodium load.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold** (for the top prediction, Ureaplasma urethritis)

**Rationale:**
- Ureaplasma lacks a cell wall, so fosfomycin's mechanism is not expected to work, and no trials or literature support the prediction.
- Among the other predictions, **pyelitis** supports **Proceed with Guardrails**. It has L1 evidence, including a Phase 2/3 RCT of IV fosfomycin. However, it is largely an extension of the existing UTI indication, and the evidence applies mainly to the IV formulation.
- **Gonococcal urethritis** is a plausible research question (L2). It has a 2016 RCT and a 1977 series, but the RCT outcome is not confirmed.
- The remaining predictions should stay on Hold.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Full-text review of the ZEUS trial (PMID 30861061) and the gonococcal RCT (PMID 27064136) to confirm phase, size and efficacy results
- For pyelitis: confirmation of which formulation (IV vs oral) is available and appropriate in Canada, plus local resistance patterns and renal-function dosing
- For gonococcal urethritis: current resistance data and comparison with standard-of-care agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

