---
layout: default
title: Fosfomycin
parent: Model Prediction Only (L5)
nav_order: 410
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Fosfomycin: From Urinary Tract Infection to Ureaplasma Urethritis

## One-Sentence Summary

Fosfomycin is an antibiotic used in Canada, mainly for urinary tract infections (the licence records supplied do not state the approved indication).
The TxGNN model predicts it may be effective for **Ureaplasma urethritis**, but **0 clinical trials** and **0 publications** support this prediction, and the drug's mechanism argues against it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection (based on literature context; the Canadian licence records list no indication text) |
| Predicted New Indication | Ureaplasma urethritis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Fosfomycin inhibits MurA, an enzyme essential for the early steps of bacterial peptidoglycan (cell wall) synthesis. It reaches high concentrations in urine, which is why it is established for urinary tract infections.

The prediction is weak on mechanistic grounds. Ureaplasma has no cell wall, so a drug that blocks cell wall synthesis is not expected to work against it. The very high TxGNN score comes from the knowledge graph alone (rank 476), with no trials or publications behind it. It reflects the shared urogenital setting, not a plausible way the drug would act on this organism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Dosage forms and approved-indication text are not included in the supplied licence records.

| DIN | Product Name |
|---------|------|
| 02488086 | IVOZFO |
| 02473801 | JAMP-FOSFOMYCIN |
| 02240335 | MONUROL |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for fosfomycin in the evidence pack.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or literature behind it (L5), and fosfomycin's cell-wall mechanism is not expected to work against Ureaplasma, which has no cell wall. It should not advance on the model score alone.

**Other predictions in this pack are stronger and should be prioritised over this one:**
- **Pyelitis (L2, Proceed with Guardrails):** This has the most support. It includes the Phase 2/3 ZEUS randomized trial of IV fosfomycin versus piperacillin-tazobactam in complicated UTI and acute pyelonephritis ([PMID 30861061](https://pubmed.ncbi.nlm.nih.gov/30861061/)), plus a retrospective review of oral fosfomycin in pyelonephritis ([PMID 32303061](https://pubmed.ncbi.nlm.nih.gov/32303061/)). Guardrails are to restrict use to susceptible isolates, monitor for resistance, and note that oral evidence for upper-tract infection is weaker than for lower-tract infection.
- **Gonococcal urethritis (L2, Research Question):** This includes a 2016 randomized trial of fosfomycin trometamol in men ([PMID 27064136](https://pubmed.ncbi.nlm.nih.gov/27064136/)). The L2 grade is provisional because the trial's phase, sample size and outcome are not visible in the supplied data. Efficacy versus current standard-of-care regimens and resistance risk need checking against the full text.

**To reconsider Ureaplasma urethritis, the following is needed:**
- In vitro susceptibility data for Ureaplasma, or any clinical report of fosfomycin use in this infection
- The approved indication and package insert warnings and contraindications from Health Canada
- Confirmation of the mechanism of action in DrugBank (the record lists it as unavailable)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

