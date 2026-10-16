---
layout: default
title: Selinexor
parent: Model Prediction Only (L5)
nav_order: 841
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Selinexor: predicted new indication Drug-induced osteoporosis (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "SELINEXOR"
predicted_indications: ["drug-induced osteoporosis"]
---

# Selinexor
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Selinexor: From an Unspecified Original Indication to Drug-Induced Osteoporosis

## One-Sentence Summary

Selinexor is marketed in Canada under the brand name XPOVIO, but the data compiled for this report do not list its approved indication text.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**, but there are currently **no clinical trials** and **no publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.22% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Selinexor is generally known as an inhibitor of XPO1 (exportin-1), a selective inhibitor of nuclear export. This general knowledge has not been verified against the data compiled for this report.

A possible but unverified link is that XPO1 inhibition changes the nuclear retention of tumour suppressors and signalling regulators (for example in the NF-kB and Wnt pathways). These pathways are involved in bone remodelling, so in theory they could affect osteoclast and osteoblast activity. The data give no indication of whether the effect would be protective or harmful.

The prediction should be treated with caution. Drug-induced osteoporosis is a drug-adverse-effect category, so the model may be reflecting network proximity in the knowledge graph rather than a true therapeutic relationship. At this point the link is a hypothesis only and needs experimental validation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02527677 | XPOVIO | Not listed | Not listed |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (XPO1 / nuclear export inhibitor), based on general drug knowledge; not confirmed in the compiled data |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions (typically CBC, liver and renal function, electrolytes) |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: The interaction query found **81 interacting drugs** in total. The first 20 returned are shown below, and the full list was not reviewed.
  - **Major**: Deferiprone, Samarium (153Sm) lexidronam, Adalimumab, Baricitinib, Certolizumab pegol, Cladribine, Clozapine
  - **Moderate**: Strontium chloride Sr-89, Roflumilast, Chloramphenicol (systemic and ophthalmic), Zidovudine, Alefacept, Alemtuzumab, Anakinra, Azathioprine, Canakinumab, tetanus toxoid vaccine, anthrax vaccine, live oral cholera vaccine

  Many of the listed drugs are immunosuppressants, myelosuppressive agents or live vaccines, so combined use needs careful review.

For warnings and contraindications, please refer to the package insert, as no label data were available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score (99.22%) but no clinical trials, no literature and no verified mechanism, which places it at evidence level L5. Drug-induced osteoporosis is also an adverse-effect category, so the prediction may reflect a knowledge-graph artefact. The label warnings and contraindications are missing, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications and approved indication), which currently blocks safety screening
- Mechanism of action data from DrugBank, to support analysis of the mechanistic link
- Preclinical or literature evidence on the effect of XPO1 inhibition on bone metabolism, including whether the effect is protective or harmful
- Review of the full list of 81 drug interactions
- Confirmation of the original indication, dosage form and manufacturer for the XPOVIO licence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

