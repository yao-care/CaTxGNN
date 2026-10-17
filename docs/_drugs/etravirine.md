---
layout: default
title: Etravirine
parent: Model Prediction Only (L5)
nav_order: 368
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Etravirine: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infection, AIDS"
monitor_inn: "ETRAVIRINE"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "benign prostate phyllodes tumor", "obsolete familial combined hyperlipidemia"]
---

# Etravirine
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

# Etravirine: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Etravirine is an antiviral (an HIV-1 reverse transcriptase inhibitor) originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, but **no clinical trials and no publications** currently support this prediction.
It is a model-only prediction, and the high score most likely reflects the drug's closeness to HIV in the knowledge graph rather than real pharmacology.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infection, AIDS (the licence records compiled for this report contain no indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data are not available in the data compiled for this report. Based on known information, etravirine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) that targets HIV-1 reverse transcriptase, and its efficacy in HIV infection is established.

Feline immunodeficiency virus (FIV) is a lentivirus related to HIV, which is the apparent basis of the prediction. However, FIV reverse transcriptase is generally considered intrinsically resistant to NNRTIs. The 99.98% score therefore most likely comes from graph proximity to HIV, not from a true pharmacological match. This is also a veterinary disease, not a human therapeutic indication.

Other predictions in the same list include simian immunodeficiency virus infection (a primate lentivirus with the same NNRTI resistance concern), congenital HIV and AIDS-related complex (extensions of the existing HIV indication), and several benign neoplasms and rare disorders with no plausible mechanistic link. Congenital HIV is the only one with some supporting data. It has a 2010 report of two pregnant women treated with etravirine-containing regimens, which is observational and limited.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for feline acquired immunodeficiency syndrome.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02306778 | INTELENCE | Not stated | Not stated |
| 02375931 | INTELENCE | Not stated | Not stated |

Both licences are valid single-ingredient products.

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: The knowledge graph lists chronic hepatitis C virus infection, hepatitis C virus infection, chronic hepatitis B virus infection, peripheral nervous system disease and peripheral neuropathy.
- **Drug Interactions**: 100 interactions were found. The first 20 records reviewed are mostly Moderate, with one Minor (ranitidine). Examples of Moderate interactions:
  - Acid-lowering drugs: omeprazole, rabeprazole, cimetidine
  - Corticosteroids: dexamethasone, hydrocortisone, betamethasone, triamcinolone
  - Antidiabetic drugs: pioglitazone, glimepiride, saxagliptin, linagliptin, chlorpropamide
  - Others: clarithromycin, metronidazole, aprepitant, eliglustat, dronabinol, naloxegol, naldemedine

Please refer to the package insert for the full set of warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no trials or publications, and FIV is expected to be intrinsically resistant to NNRTIs, so the mechanistic basis is weak. The disease is also a veterinary condition.

**To proceed, the following is needed:**
- In vitro activity data of etravirine against FIV reverse transcriptase to test the resistance concern
- Mechanism-of-action data from DrugBank
- Health Canada package insert warnings and contraindications, and indication text for the two DINs
- If a human-relevant direction is wanted, review the congenital HIV prediction (the only one with some supporting data), which is an extension of the existing indication to pregnancy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

