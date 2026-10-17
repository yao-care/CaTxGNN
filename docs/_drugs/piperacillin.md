---
layout: default
title: Piperacillin
parent: Model Prediction Only (L5)
nav_order: 740
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
description: "Piperacillin: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "PIPERACILLIN"
predicted_indications: ["rheumatoid arthritis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "sclerosing cholangitis", "osteoarthritis susceptibility", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies", "diabetic nephropathy", "WHIM syndrome"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Piperacillin: From Bacterial Infection Treatment to Rheumatoid Arthritis

## One-Sentence Summary

Piperacillin is a beta-lactam antibiotic marketed in Canada as a combination injection with tazobactam.
The TxGNN model predicts it may be effective for **rheumatoid arthritis** with a very high network-based score, but **no clinical trials** and **no publications showing therapeutic benefit** support this prediction. The 15 retrieved articles are mostly case reports in which rheumatoid arthritis is only the patient's background condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (Canadian license entries have no indication text) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 16 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, piperacillin is a beta-lactam antibiotic that inhibits bacterial cell wall synthesis. It has no known immunomodulatory activity relevant to rheumatoid arthritis.

The high TxGNN score (99.94%) comes from a network-based prediction only. The retrieved literature describes patients who happen to have rheumatoid arthritis, for example methotrexate toxicity, infections in immunosuppressed patients and antibiotic-associated liver injury. Any use of piperacillin in these patients was to treat infection, not the arthritis. At present, no plausible mechanistic link between the original use and the predicted indication has been established.

Other predicted indications (sclerosing cholangitis, osteoarthritis susceptibility, diabetic nephropathy, WHIM syndrome and several rare genetic syndromes) are likewise prediction-only, with no supportive evidence and no plausible mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No randomized trials or studies of therapeutic benefit were found. The most relevant retrieved publications are listed below. They are mostly case reports and do not support efficacy.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33987340](https://pubmed.ncbi.nlm.nih.gov/33987340/) | 2021 | Cohort | Ann Transl Med | Prevalence and clinical features of antibiotic-associated drug-induced liver injury (a safety signal, not efficacy) |
| [41257433](https://pubmed.ncbi.nlm.nih.gov/41257433/) | 2026 | Cohort (predictive model) | Br J Clin Pharmacol | Risk model for eosinophilia in patients treated with ampicillin/sulbactam or piperacillin/tazobactam |
| [37599303](https://pubmed.ncbi.nlm.nih.gov/37599303/) | 2023 | Case report | Orthopadie (Heidelberg) | Prosthetic knee joint infection in a patient with rheumatoid arthritis; piperacillin/tazobactam used for pneumonia |
| [22605835](https://pubmed.ncbi.nlm.nih.gov/22605835/) | 2012 | Case report | BMJ Case Rep | Purulent pericarditis in a patient with rheumatoid arthritis on etanercept and methotrexate; empirical piperacillin-tazobactam for infection |
| [41268563](https://pubmed.ncbi.nlm.nih.gov/41268563/) | 2025 | Case report | Front Immunol | Atypical bullous erysipelas from *E. coli* in an immunosuppressed patient with long-standing rheumatoid arthritis |
| [40119266](https://pubmed.ncbi.nlm.nih.gov/40119266/) | 2025 | Case report/Review | BMC Infect Dis | Septic shock caused by drug-resistant *Edwardsiella tarda* |
| [38343452](https://pubmed.ncbi.nlm.nih.gov/38343452/) | 2024 | Case report | Proc (Bayl Univ Med Cent) | Low-dose methotrexate toxicity with pancytopenia in a patient with rheumatoid arthritis, treated with leucovorin |
| [34178513](https://pubmed.ncbi.nlm.nih.gov/34178513/) | 2021 | Case report | Cureus | Pancytopenia from low-dose methotrexate in rheumatoid arthritis |
| [36945293](https://pubmed.ncbi.nlm.nih.gov/36945293/) | 2023 | Case report | Cureus | Recurrent pleural effusions in a patient with rheumatoid arthritis in long-term remission |
| [39104733](https://pubmed.ncbi.nlm.nih.gov/39104733/) | 2024 | Case report | Clin Case Rep | Pauci-immune necrotizing glomerulonephritis with negative ANCA |

## Canada Market Information

The 16 valid Canadian authorizations are all single-ingredient entries named "Piperacillin and Tazobactam for Injection". Dosage form, manufacturer and approved indication text are not available in the compiled data. The first five are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02402068 | Piperacillin and Tazobactam for Injection | Not available | Not available |
| 02377748 | Piperacillin and Tazobactam for Injection | Not available | Not available |
| 02528703 | Piperacillin and Tazobactam for Injection | Not available | Not available |
| 02362627 | Piperacillin and Tazobactam for Injection | Not available | Not available |
| 02521539 | Piperacillin and Tazobactam for Injection | Not available | Not available |

## Safety Considerations

- **Drug Interactions**: 81 interactions were identified. The main ones by severity are:
  - **Major**: Vancomycin
  - **Moderate**: Doxycycline, Tetracycline, Minocycline, Kanamycin, Streptomycin, Picosulfuric acid
  - **Minor**: Clarithromycin
- **Additional cautions from the retrieved data**: Beta-lactam antibiotics are associated with drug-induced liver injury and eosinophilia (see the two cohort studies above), and piperacillin requires renal dose adjustment. This matters for patients with rheumatoid arthritis, who are often on immunosuppressants.

Please refer to the package insert for warnings and contraindications, which were not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a network-based model score. There are no clinical trials, no studies of therapeutic benefit, and no plausible mechanism linking a bacterial cell wall synthesis inhibitor to rheumatoid arthritis. The retrieved articles describe infections in patients who already have the disease.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications and approved indications (currently missing and blocking safety screening)
- Mechanism of action data and a testable biological hypothesis for rheumatoid arthritis
- Preclinical evidence of any anti-inflammatory or immunomodulatory effect
- Review of whether the high score reflects a model artifact, such as co-occurrence of infection in patients with rheumatoid arthritis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

