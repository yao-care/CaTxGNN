---
layout: default
title: Bictegravir
parent: Model Prediction Only (L5)
nav_order: 114
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Bictegravir: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infection, AIDS"
monitor_inn: "BICTEGRAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Bictegravir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Bictegravir: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Bictegravir is an HIV-1 integrase strand transfer inhibitor, originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, but there are currently **0 clinical trials** and **0 publications** directly supporting this prediction. The prediction rests on model output and class-level reasoning only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infection, AIDS |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known drug class information, bictegravir belongs to the integrase strand transfer inhibitor (INSTI) class, and its efficacy in HIV infection is established.

Feline immunodeficiency virus (FIV) is a lentivirus related to HIV and also encodes an integrase enzyme. This gives a class-level mechanistic rationale for the prediction. However, no FIV-specific data on bictegravir binding, enzyme inhibition, or antiviral activity were available. The high score (0.998) is a computational prediction only, and the mechanistic link here is inferred from general drug class knowledge rather than from the supplied data.

It is also worth noting that feline AIDS is a veterinary disease, so any development path would differ substantially from human drug repurposing.

**Other predictions in the same output**

- **Simian immunodeficiency virus (SIV) infection** (same score, 99.82%; evidence level L4): Preclinical work includes an in vitro study of bictegravir and cabotegravir against integrase inhibitor-resistant SIVmac239 and HIV-1 (PMID 28923862), a structural review of HIV/SIV intasomes (PMID 32506843), and a humanized mouse model for testing SIV and HIV antiviral strategies (PMID 39559349). SIV is not a human disease, so its value lies mainly in nonhuman primate research models and resistance profiling.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (score 99.76%; evidence level L5): No plausible mechanistic link is apparent. Viral integrase is not a target in human neurodevelopmental biology, and the score likely reflects a knowledge-graph artifact. No trials or literature support it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for feline acquired immunodeficiency syndrome.

For reference, the following publications relate to the second-ranked prediction (SIV infection), which shares the same score:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28923862](https://pubmed.ncbi.nlm.nih.gov/28923862/) | 2017 | In vitro antiviral/resistance study | Antimicrob Agents Chemother | Antiviral activity of bictegravir and cabotegravir against integrase inhibitor-resistant SIVmac239 and HIV-1 |
| [32506843](https://pubmed.ncbi.nlm.nih.gov/32506843/) | 2021 | Review (structural biology) | FEBS J | HIV/SIV intasome structures clarify integrase inhibitor binding and viral escape mechanisms |
| [39559349](https://pubmed.ncbi.nlm.nih.gov/39559349/) | 2024 | Preclinical animal model | Front Immunol | Dual-purpose humanized mouse model for testing antiviral strategies against both SIV and HIV |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02478579 | BIKTARVY | Not specified | Not specified |

---

## Safety Considerations

**Drug Interactions**: The interaction screening completed with **81 interacting drugs** identified in total. The main ones listed in the data compiled for this report include:

- **Major**: Polyvalent cation products, including aluminum hydroxide, attapulgite, kaolin, magaldrate, iron, several calcium salts (acetate, carbonate, citrate, glubionate, gluconate, lactate, phosphate), and magnesium salts (carbonate, chloride, citrate)
- **Moderate**: Aprepitant, clarithromycin, dexamethasone, eliglustat, glycerol phenylbutyrate

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for feline acquired immunodeficiency syndrome is supported only by a model score and a class-level mechanistic argument, with no trials, literature, or FIV-specific data. It is also a veterinary indication, which falls outside a typical human drug repurposing path.

**To proceed, the following is needed:**
- Mechanism of action data for bictegravir
- FIV-specific preclinical data (integrase binding, enzymatic inhibition, in vitro antiviral activity)
- A decision on whether a veterinary indication is within the scope of this program
- Health Canada package insert warnings and contraindications for safety screening
- If the SIV indication is of interest, nonhuman primate or humanized mouse studies as a research-model use rather than a clinical indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

