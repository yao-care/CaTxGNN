---
layout: default
title: Piperacillin
parent: Model Prediction Only (L5)
nav_order: 733
evidence_level: L5
indication_count: 9
---

# Piperacillin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Piperacillin: From Bacterial Infections to Rheumatoid Arthritis

## One-Sentence Summary

Piperacillin is a beta-lactam antibiotic, marketed in Canada mainly as piperacillin/tazobactam for injection.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis** (score 99.94%), but **no clinical trials** are registered and the **18 retrieved publications** are mostly incidental case reports, not evidence of efficacy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (antibacterial use; the Canadian licence records provided contain no indication text) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 (weak; the literature is incidental, with no efficacy data) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 16 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Piperacillin belongs to the beta-lactam class, which kills bacteria by inhibiting penicillin-binding proteins. Its established efficacy is in bacterial infections.

No anti-inflammatory or immunomodulatory mechanism relevant to rheumatoid arthritis (RA) is established. The link between piperacillin and RA in the literature is incidental. RA patients are often immunosuppressed (methotrexate, glucocorticoids, TNF or JAK inhibitors), so they develop infections that are then treated with piperacillin/tazobactam. This shows the drug is used for complications in RA patients, not that it treats RA itself.

The high TxGNN score (0.999) is not supported by any mechanistic or clinical evidence in the data provided. The other predicted indications are weaker still. They include rare congenital syndromes, sclerosing cholangitis, osteoarthritis susceptibility, diabetic nephropathy and WHIM syndrome. All are Hold, most with no trials or literature at all.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the articles below tests piperacillin as a treatment for RA. The table lists the 10 most relevant of the 18 retrieved. There are no RCTs, so cohort studies come first, then case reports.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41257433](https://pubmed.ncbi.nlm.nih.gov/41257433/) | 2025 | Cohort | Br J Clin Pharmacol | Predictive risk model for eosinophilia in patients on ampicillin/sulbactam or piperacillin/tazobactam (a safety study, not RA efficacy) |
| [33987340](https://pubmed.ncbi.nlm.nih.gov/33987340/) | 2021 | Cohort | Ann Transl Med | Prevalence and clinical features of antibiotic-associated drug-induced liver injury |
| [37599303](https://pubmed.ncbi.nlm.nih.gov/37599303/) | 2023 | Case report | Orthopadie (Heidelberg) | RA patient on a JAK1 inhibitor developed a Haemophilus influenzae prosthetic knee infection; piperacillin/tazobactam was started for pneumonia |
| [22605835](https://pubmed.ncbi.nlm.nih.gov/22605835/) | 2012 | Case report | BMJ Case Rep | Purulent pericarditis in an RA patient on etanercept and methotrexate; empirical piperacillin/tazobactam was used |
| [19621776](https://pubmed.ncbi.nlm.nih.gov/19621776/) | 2009 | Case report | No Shinkei Geka | Hypertrophic pachymeningitis with raised CRP treated with several antibiotics, including piperacillin; minocycline had the notable effect |
| [30371923](https://pubmed.ncbi.nlm.nih.gov/30371923/) | 2019 | Case report | Orthopedics | E. coli femoral osteomyelitis in an RA patient on long-term prednisone, treated with antibiotic cement rods and IV antibiotics |
| [41268563](https://pubmed.ncbi.nlm.nih.gov/41268563/) | 2025 | Case report | Front Immunol | Severe atypical bullous erysipelas with septic shock in a patient with 20 years of RA on immunosuppressants |
| [38343452](https://pubmed.ncbi.nlm.nih.gov/38343452/) | 2024 | Case report | Proc (Bayl Univ Med Cent) | Low-dose methotrexate toxicity causing pancytopenia in an RA patient, rescued with leucovorin |
| [34178513](https://pubmed.ncbi.nlm.nih.gov/34178513/) | 2021 | Case report | Cureus | Pancytopenia from low-dose methotrexate in RA, presented as a diagnostic challenge |
| [17576563](https://pubmed.ncbi.nlm.nih.gov/17576563/) | 2007 | Case report | Rheumatol Int | Disseminated candidiasis in a patient with Felty's syndrome and severe granulocytopenia |

---

## Canada Market Information

16 licences in total; 5 main authorizations are listed. Dosage form and approved-indication text are not recorded in the licence data provided.

| DIN | Product Name |
|---------|------|
| 2402068 | PIPERACILLIN AND TAZOBACTAM FOR INJECTION |
| 2377748 | PIPERACILLIN AND TAZOBACTAM FOR INJECTION |
| 2528703 | PIPERACILLIN AND TAZOBACTAM FOR INJECTION |
| 2362627 | PIPERACILLIN AND TAZOBACTAM FOR INJECTION |
| 2521539 | PIPERACILLIN AND TAZOBACTAM FOR INJECTION |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug in the data provided.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone. There are no registered trials, no mechanistic link to RA, and the literature only shows antibiotic use for infections in RA patients. The remaining predicted indications have equally little or no support.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data (for example from DrugBank) to test for any anti-inflammatory or immunomodulatory rationale in RA
- Evidence that the drug itself, not the treatment of infections, has an effect on RA (preclinical or clinical)
- Approved-indication text and dosage-form details for the Canadian licences

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

