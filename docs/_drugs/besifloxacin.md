---
layout: default
title: Besifloxacin
parent: Model Prediction Only (L5)
nav_order: 106
evidence_level: L5
indication_count: 8
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Besifloxacin: From Ocular Bacterial Infection to Bronchitis

## One-Sentence Summary

Besifloxacin is a fluoroquinolone antibacterial marketed in Canada as the ophthalmic product BESIVANCE. The registered trials in the pack concern bacterial conjunctivitis and other ocular bacterial infections.
The TxGNN model predicts it may be effective for **bronchitis** with a high score, but there are **0 clinical trials** and **0 publications** for this indication, so it rests on model prediction alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ocular bacterial infection (bacterial conjunctivitis). The licence record has no indication text, so this is inferred from the registered trials. |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Besifloxacin is a fluoroquinolone with broad Gram-positive and Gram-negative activity, so a respiratory-pathogen link is theoretically conceivable.

However, besifloxacin is marketed only as a topical ophthalmic suspension with minimal systemic exposure, so there is no plausible route for it to reach lung tissue. The high TxGNN score most likely reflects a class-level fluoroquinolone signal rather than a property specific to this drug. The bronchitis prediction is therefore not well supported biologically or by the available route of administration.

Of the other seven predictions, most (post-infectious vasculitis, post-infectious syndrome, infective urethral stricture, Chagas cardiomyopathy, infection-related hemolytic uremic syndrome) have no mechanistic rationale. The one credible hypothesis is **otitis externa**. Topical fluoroquinolones such as ciprofloxacin and ofloxacin are established for it, and the usual pathogens (*Pseudomonas aeruginosa*, *Staphylococcus aureus*) fall within the fluoroquinolone spectrum. No besifloxacin-specific data exist, though.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for bronchitis.

For reference, the only trials in the pack are those linked to the rank 3 prediction, "post-bacterial disorder". They all concern besifloxacin's existing ocular use and do not validate a new indication.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01175590](https://clinicaltrials.gov/study/NCT01175590) | Phase 3 | Completed | 518 | Safety of besifloxacin 0.6% versus vehicle, dosed three times daily for 7 days |
| [NCT01740388](https://clinicaltrials.gov/study/NCT01740388) | Phase 3 | Terminated | 136 | Clinical and microbial efficacy versus vehicle in bacterial conjunctivitis. Early termination limits interpretation. |
| [NCT01478256](https://clinicaltrials.gov/study/NCT01478256) | Phase 4 | Completed | 30 | Versus erythromycin ointment in acute blepharitis |
| [NCT01296542](https://clinicaltrials.gov/study/NCT01296542) | Phase 4 | Completed | 60 | Prophylactic antibacterial efficacy versus moxifloxacin before cataract surgery |
| [NCT04542759](https://clinicaltrials.gov/study/NCT04542759) | Phase 1 | Completed | 60 | Effect on ocular surface bacterial microbiota before cataract surgery |
| [NCT00407589](https://clinicaltrials.gov/study/NCT00407589) | Phase 1 | Completed | 24 | Systemic pharmacokinetics after ocular instillation, supporting low systemic exposure |

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2336847 | BESIVANCE |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (bronchitis) rests on model output alone (L5), with no trials or literature. The ophthalmic-only formulation has negligible systemic exposure, so it cannot plausibly reach the airways. The only trials found relate to the existing ocular use, not a new indication.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for any safety screening)
- Mechanism of action data (MOA) from DrugBank
- For otitis externa, the one plausible hypothesis (a research question, not a recommendation): in vitro susceptibility data against common otic pathogens and otic safety data, including with a perforated tympanic membrane
- For any systemic or respiratory route, a new formulation and pharmacokinetic evidence
- Caution on infection-related hemolytic uremic syndrome: antibiotic use in STEC-associated HUS is controversial, so this prediction should not be pursued

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

