---
layout: default
title: Besifloxacin
parent: Model Prediction Only (L5)
nav_order: 108
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
description: "Besifloxacin: predicted new indication Bronchitis (evidence level L5). Approved use: Conjunctivitis"
monitor_inn: "BESIFLOXACIN"
predicted_indications: ["bronchitis", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "otitis externa"]
---

# Besifloxacin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Besifloxacin: From Conjunctivitis to Bronchitis
{: .text-alpha }

## One-Sentence Summary

Besifloxacin is a fluoroquinolone antibiotic, originally used to treat bacterial conjunctivitis (including acute contagious conjunctivitis).
The TxGNN model predicts it may be effective for **bronchitis**, with a very high score, but **no clinical trials and no publications** currently support this direction.
This is a computational prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Conjunctivitis; acute contagious conjunctivitis |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, besifloxacin is a fluoroquinolone, a class that inhibits bacterial DNA gyrase and topoisomerase IV. Its efficacy in bacterial conjunctivitis has been established, and mechanistically it could be applicable to other bacterial infections.

Systemic fluoroquinolones have activity against respiratory pathogens, so a class-level link to bacterial bronchitis is plausible. However, besifloxacin is marketed only as an ophthalmic suspension with minimal systemic exposure. It is unlikely to reach relevant concentrations in the airways. The high score therefore comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence of a demonstrated pharmacological or clinical link.

**Other predicted indications (all L5, all Hold):**

| Rank | Predicted Indication | Score | Assessment |
|------|------|------|------|
| 2 | Postinfectious vasculitis | 0.9931 | Immune-mediated; no clear antibacterial rationale |
| 3 | Post-bacterial disorder | 0.9931 | Vague category; only a Phase 1 PK study is linked |
| 4 | Post-infectious syndrome | 0.9929 | Immune or sequelae-driven; weak rationale |
| 5 | Infective urethral stricture | 0.9921 | Fibrotic, structural condition; ocular drug does not reach the urinary tract |
| 6 | Chagas cardiomyopathy | 0.9916 | Protozoal cause; not mechanistically plausible, likely a network artifact |
| 7 | Infection-related hemolytic uremic syndrome | 0.9913 | Antibiotics may worsen risk; a safety concern rather than a benefit |
| 8 | Otitis externa | 0.9903 | Most biologically plausible; topical fluoroquinolones are established treatments, but besifloxacin is untested for otic use |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for bronchitis.

For context, one trial is linked to the rank 3 prediction (post-bacterial disorder). It is not an efficacy study:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00407589](https://clinicaltrials.gov/study/NCT00407589) | Phase 1 | Completed | 24 | Systemic pharmacokinetics after single and multiple ocular instillations in people with suspected bacterial conjunctivitis; indicates low systemic exposure |

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02336847 | BESIVANCE | Not specified | Not specified |

---

## Safety Considerations

- **Contraindications (knowledge graph, not label text)**: The knowledge graph lists an association with obsolete superimposed infection.
- **Drug Interactions**: No interactions were found in the queried data.

For full warnings and contraindications, please refer to the package insert.

For the hemolytic uremic syndrome prediction, antibiotics (fluoroquinolones in particular) may increase Shiga toxin release, which would be a potential harm rather than a benefit.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction rests on a model score alone, with no trials or literature. Besifloxacin is an ophthalmic product with minimal systemic exposure, so it is unlikely to reach the airways. Safety review is also incomplete because package insert warnings are not yet available.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Evidence that a non-ocular route or formulation could deliver adequate drug levels to the airways
- For a more feasible research question, a preclinical or early clinical assessment of topical besifloxacin in otitis externa, including safety with a perforated tympanic membrane
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

