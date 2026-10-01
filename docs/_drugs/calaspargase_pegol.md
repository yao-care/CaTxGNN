---
layout: default
title: Calaspargase Pegol
parent: Model Prediction Only (L5)
nav_order: 144
evidence_level: L5
indication_count: 10
---

# Calaspargase Pegol
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

# Calaspargase pegol: From Acute Lymphoblastic Leukemia to Insomnia

## One-Sentence Summary

Calaspargase pegol is a pegylated asparaginase, an enzyme therapy that depletes circulating asparagine. It is used in acute lymphoblastic leukemia (ALL), based on the trial data in the Evidence Pack. The TxGNN model predicts it may be effective for **insomnia** with a very high score, but **no clinical trials and no publications** support this prediction, and no plausible mechanism is apparent.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license record; the linked trials and drug class indicate acute lymphoblastic leukemia / lymphoblastic lymphoma |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Based on the drug class, calaspargase pegol is a pegylated asparaginase. It depletes circulating asparagine, which leukemic cells depend on, and this is the basis of its use in ALL.

This mechanism has no evident connection to sleep regulation, and the Evidence Pack review found no plausible mechanistic link to insomnia. The score of 0.998 most likely reflects a knowledge-graph propagation artifact, not pharmacology. The near-duplicate prediction "sleep disorder, initiating and maintaining sleep" (rank 7) likely shares the same artifact.

The wider prediction list points the same way. Many of the other top-ranked predictions are coagulation-related (thrombophilia, antithrombin deficiency type 2, heparin cofactor 2 deficiency, thrombotic disease) or hepatic (benign recurrent intrahepatic cholestasis). These appear to reflect known **adverse effects** of asparaginase, such as lowered antithrombin and fibrinogen, thrombosis and cholestasis, not therapeutic benefit. All ten predictions are L5 except thrombotic disease (L4).

---

## Clinical Trial Evidence

Currently no related clinical trials registered for insomnia.

---

## Literature Evidence

Currently no related literature available for insomnia.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2542943 | ASPARLAS | — | — |

The license record does not list a dosage form or approved indication text.

---

## Cytotoxicity

This drug is used in leukemia, so it is treated as antineoplastic.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Enzyme-based antineoplastic (asparagine depletion), not a conventional DNA-damaging cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Coagulation parameters and liver function are relevant given the class effects noted below; full monitoring requirements are in the package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Package insert warnings, contraindications and drug interaction data were not available for this report (the DDI query returned no results). Please refer to the package insert for these.

Class-level concerns noted in the Evidence Pack:
- **Coagulation effects**: asparaginase lowers antithrombin, fibrinogen and other coagulation proteins and is associated with thrombosis.
- **Hepatotoxicity**: hepatotoxicity and cholestasis are associated adverse effects.

Repurposing this drug for a non-oncology condition such as insomnia would expose patients to these risks with no supporting benefit.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The insomnia prediction rests on a model score alone. There are no trials or publications, and no plausible mechanism links asparagine depletion to sleep. The drug's known toxicity profile makes a non-oncology repurposing attempt hard to justify.

**To proceed, the following is needed:**
- The Health Canada package insert, including warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank, to allow a proper mechanistic-link analysis
- Any preclinical or clinical evidence linking asparaginase activity to sleep regulation, which does not currently exist in the input
- Results from NCT07071051 (coagulation effects in pediatric ALL), which would help characterize the thrombosis risk, though it does not address insomnia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

