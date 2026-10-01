---
layout: default
title: Ertapenem
parent: Model Prediction Only (L5)
nav_order: 345
evidence_level: L5
indication_count: 2
---

# Ertapenem
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Ertapenem: From Bacterial Infections to Bacterial Arthritis

## One-Sentence Summary

Ertapenem is a once-daily injectable carbapenem antibiotic, marketed in Canada for bacterial infections.
The TxGNN model predicts it may be effective for **bacterial arthritis**.
Currently **0 registered clinical trials** and **8 publications** relate to this direction, mostly case reports and indirect cohort data.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (carbapenem antibacterial; the licence records provided contain no indication text) |
| Predicted New Indication | Bacterial arthritis |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L4 (see note below) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

*Evidence level note: there are no trials for this indication and no observational study specific to bacterial arthritis. Only case reports and indirect cohort or in vitro data exist. That is below L3 and consistent with L4.*

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the DrugBank record. Based on known pharmacology, ertapenem is a carbapenem that inhibits bacterial cell wall synthesis by binding penicillin-binding proteins.

Bacterial arthritis (septic arthritis) and related bone and joint infections are caused by organisms that ertapenem covers. These include Enterobacterales such as *Klebsiella pneumoniae*, anaerobes such as *Prevotella* and *Clostridium*, and methicillin-susceptible *S. aureus* (MSSA). Published case reports describe ertapenem use in these settings. Once-daily dosing also makes it practical for outpatient or prolonged parenteral therapy.

There are important limits. Ertapenem does not reliably cover MRSA or *Pseudomonas*. The literature does not establish it as standard therapy for bacterial arthritis. The very high TxGNN score is a computational prediction only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24709258](https://pubmed.ncbi.nlm.nih.gov/24709258/) | 2014 | Retrospective cohort | Antimicrob Agents Chemother | 306 patients on outpatient ertapenem therapy, with bone and joint infection among the common indications. It is a long-term safety and efficacy study, not specific to arthritis. |
| [22233826](https://pubmed.ncbi.nlm.nih.gov/22233826/) | 2011 | Case report | J Chemother | *Klebsiella pneumoniae* septic wrist arthritis treated successfully with ertapenem and levofloxacin. |
| [31352398](https://pubmed.ncbi.nlm.nih.gov/31352398/) | 2019 | Case report | BMJ Case Rep | *Citrobacter koseri* septic arthritis with osteomyelitis in a diabetic foot, treated successfully with ertapenem. |
| [31585203](https://pubmed.ncbi.nlm.nih.gov/31585203/) | 2020 | Case report + review | Anaerobe | First reported *Clostridium paraputrificum* shoulder septic arthritis and osteomyelitis, with a literature review. |
| [37578166](https://pubmed.ncbi.nlm.nih.gov/37578166/) | 2023 | Case report + review | J Investig Med High Impact Case Rep | *Prevotella bivia* septic arthritis in an immunocompetent adult, with a literature review. |
| [31220276](https://pubmed.ncbi.nlm.nih.gov/31220276/) | 2019 | Cohort (n=10) | J Antimicrob Chemother | Subcutaneous suppressive β-lactam therapy for bone and joint infections. Ertapenem-specific data are unclear. |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Epidemiology | Clin Lab | Pathogen distribution and resistance in bone and joint infections in young children. Indirect evidence. |
| [38924836](https://pubmed.ncbi.nlm.nih.gov/38924836/) | 2024 | Preclinical (in vitro) | Diagn Microbiol Infect Dis | Auranofin restored ertapenem susceptibility in carbapenem-resistant *E. coli*. Indirect evidence. |

One further retrieved paper, a 2017 JAMA review on hidradenitis suppurativa (PMID 29183082), is off-target and was excluded.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02492148 | ERTAPENEM FOR INJECTION |
| 02496127 | ERTAPENEM FOR INJECTION |
| 02490773 | ERTAPENEM FOR INJECTION |
| 02247437 | INVANZ |
| 02537176 | ERTAPENEM FOR INJECTION |

The drug has 6 DINs in total, and the table shows the 5 available in the records. The records provided do not include dosage form or approved indication text.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (99.72%). However, the supporting evidence is limited to case reports and indirect cohort or in vitro data, with no registered trials. Ertapenem also lacks MRSA and *Pseudomonas* coverage, so it cannot serve as empiric therapy for bacterial arthritis. Health Canada safety data are also missing, which blocks S1 safety screening.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (download and parse the PDF)
- Mechanism of action data from DrugBank
- Dedicated comparative studies or registered trials of ertapenem in septic arthritis and bone and joint infection
- Approved indication text and dosage forms for the Canadian licences

**Related prediction:** the second-ranked prediction, *Staphylococcus aureus* infection, has stronger support. It rests on cefazolin plus ertapenem combination therapy for persistent MSSA bacteremia, backed by cohort studies and case series. A Phase 2 RCT ([NCT04886284](https://clinicaltrials.gov/study/NCT04886284)) is recruiting with no results yet. Evidence supports the combination for MSSA only, not ertapenem monotherapy or MRSA. This would be the more promising candidate for further evaluation.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

