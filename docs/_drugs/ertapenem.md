---
layout: default
title: Ertapenem
parent: Model Prediction Only (L5)
nav_order: 347
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-05
monitor_inn: "ERTAPENEM"
predicted_indications: ["bacterial arthritis"]
description: "Ertapenem: predicted new indication Bacterial arthritis (evidence level L5). Approved use: Not recorded in the local data"
---

# Ertapenem
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Ertapenem: Bacterial arthritis
{: .text-alpha }

## One-Sentence Summary

Ertapenem is a broad-spectrum carbapenem antibiotic, originally used for bacterial pneumonia, streptococcal pneumonia, and *Peptostreptococcus* infections.
The TxGNN model predicts it may be effective for **bacterial arthritis**, supported by **no registered clinical trials** and **10 publications**, mostly case reports and cohort studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Bacterial arthritis |
| TxGNN Prediction Score | 0.9972 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 6 of 6) |
| Number of DINs | 6 (marketed: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, ertapenem is a carbapenem that inhibits bacterial cell wall synthesis by binding penicillin-binding proteins. It is active against many Enterobacterales (including ESBL producers), streptococci, methicillin-susceptible staphylococci, and anaerobes.

These pathogens are commonly involved in septic arthritis and bone and joint infections. Ertapenem's original indications (pneumonia, anaerobic infections) already overlap with this pathogen spectrum, so the prediction is an extension of use rather than a novel mechanism. Once-daily dosing also supports outpatient parenteral therapy.

The evidence is indirect, however. It consists of case reports and uncontrolled series, such as septic arthritis treated successfully with ertapenem, and a retrospective cohort of 306 outpatients on long-term ertapenem in which bone and joint infections were among the indications.


## Clinical Trial Evidence

For bacterial arthritis (the top prediction), currently no related clinical trials are registered.

For the second prediction, *Staphylococcus aureus* infection:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07148960](https://clinicaltrials.gov/study/NCT07148960) | Phase 4 | Enrolling by invitation | 300 | Open-label randomized trial testing whether early dual IV antibiotic therapy shortens *S. aureus* bacteremia (<6 days) and improves outcomes versus single therapy. No results yet; the dual regimen needs confirmation against the protocol. |
| [NCT04886284](https://clinicaltrials.gov/study/NCT04886284) | Phase 2 | Recruiting | 60 | Cefazolin plus ertapenem for MSSA bacteremia (CERT), a sub-study of the SNAP platform trial. No results yet; small sample. |

## Literature Evidence

**Bacterial arthritis (top prediction)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24709258](https://pubmed.ncbi.nlm.nih.gov/24709258/) | 2014 | Cohort | Antimicrob Agents Chemother | Retrospective study of 306 outpatients on long-term ertapenem; indications included intra-abdominal infection (38%), pneumonia (12%), and bone and joint infection |
| [31220276](https://pubmed.ncbi.nlm.nih.gov/31220276/) | 2019 | Cohort | J Antimicrob Chemother | Subcutaneous suppressive β-lactam therapy in 10 patients with bone and joint infections |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Cohort | Clin Lab | Pathogen distribution and antimicrobial resistance in bone and joint infections in young children |
| [22233826](https://pubmed.ncbi.nlm.nih.gov/22233826/) | 2011 | Case report | J Chemother | *Klebsiella pneumoniae* septic wrist arthritis treated successfully with ertapenem and levofloxacin |
| [31352398](https://pubmed.ncbi.nlm.nih.gov/31352398/) | 2019 | Case report | BMJ Case Rep | *Citrobacter koseri* osteomyelitis with septic arthritis in a diabetic foot, treated successfully with ertapenem |
| [31585203](https://pubmed.ncbi.nlm.nih.gov/31585203/) | 2020 | Case report with review | Anaerobe | *Clostridium paraputrificum* septic arthritis and osteomyelitis of the shoulder |
| [37578166](https://pubmed.ncbi.nlm.nih.gov/37578166/) | 2023 | Case report with review | J Investig Med High Impact Case Rep | *Prevotella bivia* septic arthritis in an immunocompetent adult |
| [38924836](https://pubmed.ncbi.nlm.nih.gov/38924836/) | 2024 | In vitro study | Diagn Microbiol Infect Dis | Auranofin restores ertapenem susceptibility in carbapenem-resistant *E. coli* |


## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02247437 | INVANZ | Not specified | Not specified |
| 02492148 | ERTAPENEM FOR INJECTION | Not specified | Not specified |
| 02496127 | ERTAPENEM FOR INJECTION | Not specified | Not specified |
| 02490773 | ERTAPENEM FOR INJECTION | Not specified | Not specified |
| 02537176 | ERTAPENEM FOR INJECTION | Not specified | Not specified |

A sixth licence (DIN 02511150, ERTAPENEM FOR INJECTION) is also valid. All 6 licences are single-ingredient products in valid status.

## Safety Considerations

- **Contraindication-related conditions (knowledge graph, not label text)**: epilepsy, kidney disease, pyoureter, *Clostridium difficile* colitis, and perinatal necrotizing enterocolitis. These come from a drug-disease relationship database and should be verified against the product labelling.
- **Drug Interactions**: 38 interactions were identified. The only one rated Major is **bupropion**. Moderate interactions involve **picosulfuric acid**, **polyethylene glycol (3350 with electrolytes)**, and **sodium sulfate**. The remaining listed interactions (e.g., vancomycin, metronidazole, morphine, metformin, omeprazole) have an unclassified severity level.
- Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold** (for bacterial arthritis)

**Rationale:**
The bacterial arthritis prediction has a high model score, but the supporting evidence is limited to case reports, small cohorts, and in vitro work, with no registered clinical trials. This corresponds to evidence level L4. The *S. aureus* infection prediction is more advanced (L2, with two ongoing trials of the cefazolin combination) and is better framed as a research question awaiting trial results.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data from DrugBank
- Approved indication text and dosage forms for the Canadian licences
- Prospective or comparative studies of ertapenem in bone and joint infections
- Results from NCT04886284 and NCT07148960 for the *S. aureus* combination indication
- A dose and renal function plan, given the kidney disease and seizure-related flags and the Major bupropion interaction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

