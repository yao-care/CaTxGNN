---
layout: default
title: Meropenem
parent: Model Prediction Only (L5)
nav_order: 588
evidence_level: L5
indication_count: 10
---

# Meropenem
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

# Meropenem: From Approved Antibacterial Use to Bacterial Arthritis

## One-Sentence Summary

Meropenem is a broad-spectrum carbapenem antibiotic injection, marketed in Canada under 16 licences. The supplied data do not include its approved indication text.
The TxGNN model predicts it may be effective for **bacterial arthritis** (score 99.92%), but only **1 clinical trial** (unrelated to meropenem) and **20 publications** were retrieved, and none is a controlled meropenem study in joint infection.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (approved indication text is empty for all listed licences) |
| Predicted New Indication | Bacterial arthritis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 (mechanism, in vitro and observational data only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 16 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the supplied data. Meropenem is a carbapenem β-lactam, a class that kills bacteria by binding penicillin-binding proteins and blocking cell wall synthesis. Its spectrum covers the usual septic arthritis pathogens: methicillin-susceptible *Staphylococcus aureus*, streptococci, Enterobacterales and *Pseudomonas*.

Bacterial arthritis is a bacterial infection, so the link to an antibacterial is plausible. However, this is closer to a new site of use for a general-purpose antibiotic than to true repurposing.

Meropenem is not a first-line joint-infection agent. Its bone and joint penetration is not established in the supplied data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01371656](https://clinicaltrials.gov/study/NCT01371656) | Phase 3 | Completed | 624 | Levofloxacin to prevent bacteremia in children with acute leukemia or undergoing stem cell transplant. It does not involve meropenem and does not address septic arthritis, so it provides no direct support. |

---

## Literature Evidence

No randomized trial of meropenem in bacterial arthritis was found. The publications below are the most relevant available.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Review | Int J Antimicrob Agents | Off-label use versus formal recommendations of antibiotics for multidrug-resistant bacterial infections |
| [36678359](https://pubmed.ncbi.nlm.nih.gov/36678359/) | 2022 | Review | Pathogens | Antibiotics versus phage therapy for melioidosis, a disease that can involve joints |
| [39489417](https://pubmed.ncbi.nlm.nih.gov/39489417/) | 2024 | Retrospective review | Indian J Med Microbiol | 22 musculoskeletal melioidosis cases, 9 with septic arthritis; all isolates were susceptible to meropenem |
| [35146367](https://pubmed.ncbi.nlm.nih.gov/35146367/) | 2021 | Retrospective cohort | Le Infezioni in Medicina | Characteristics of osteoarticular melioidosis |
| [33857030](https://pubmed.ncbi.nlm.nih.gov/33857030/) | 2021 | In vitro study | J Bone Joint Surg Am | Thermal stability and elution of meropenem and other antibiotics from bone cement |
| [31319190](https://pubmed.ncbi.nlm.nih.gov/31319190/) | 2019 | Animal study | Int J Antimicrob Agents | Colistin-containing cement spacer in a rabbit model of carbapenemase-producing *Klebsiella* prosthetic joint infection |
| [37713001](https://pubmed.ncbi.nlm.nih.gov/37713001/) | 2024 | Antibiogram study | Eur J Orthop Surg Traumatol | Antibiogram for empiric therapy of orthopaedic infections, including septic arthritis |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Pathogen and resistance analysis | Clin Lab | Pathogen distribution and antimicrobial resistance in bone and joint infections in young children |
| [38139869](https://pubmed.ncbi.nlm.nih.gov/38139869/) | 2023 | Case report | Pharmaceuticals (Basel) | Septic arthritis of the hip due to *Bacillus pumilus* and *Paenibacillus barengoltzii*, treated with linezolid |
| [39681779](https://pubmed.ncbi.nlm.nih.gov/39681779/) | 2025 | PK study | Clin Pharmacokinet | Population pharmacokinetics and optimal dosing of meropenem across the adult lifespan |

---

## Canada Market Information

Dosage form and approved indication text were not supplied for any of these licences.

| DIN | Product Name |
|---------|------|
| 2378787 | MEROPENEM FOR INJECTION |
| 2544334 | MEROPENEM FOR INJECTION USP AND SODIUM CHLORIDE INJECTION USP |
| 2415224 | MEROPENEM FOR INJECTION, USP |
| 2528819 | MEROPENEM FOR INJECTION |
| 2378795 | MEROPENEM FOR INJECTION |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but the only trial found is unrelated to meropenem. The literature is limited to reviews, susceptibility and antibiogram data, in vitro work and case reports. Meropenem's joint penetration is unestablished, and established agents remain standard for joint infections.

Other predicted indications in the pack are better supported. Complicated urinary tract infection (rank 6) has Phase 3 evidence, mostly with meropenem as the comparator or as meropenem-vaborbactam. It was assessed as Proceed with Guardrails, pending verification of the registry records.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications and approved indications
- Mechanism of action data from DrugBank
- Bone and joint penetration data for meropenem
- A comparative clinical study of meropenem in septic arthritis, restricted to resistant or complex cases
- Alignment with antimicrobial stewardship policy

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

