---
layout: default
title: Avelumab
parent: Model Prediction Only (L5)
nav_order: 86
evidence_level: L5
indication_count: 10
---

# Avelumab
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

# Avelumab: From Merkel Cell Carcinoma and Urothelial Carcinoma to Human Herpesvirus 8-Related Tumor

## One-Sentence Summary

Avelumab is a PD-L1 checkpoint inhibitor. According to the rationale text in the Evidence Pack, it is marketed for Merkel cell carcinoma and urothelial carcinoma.
The TxGNN model predicts it may be effective for **human herpesvirus 8-related tumor**, but there are currently **0 clinical trials** and **0 publications** supporting this specific direction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Merkel cell carcinoma and urothelial carcinoma (taken from the rationale text; the license record has no indication text, so this needs checking against the label) |
| Predicted New Indication | Human herpesvirus 8-related tumor |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, avelumab is an antibody that blocks PD-L1. Its efficacy in Merkel cell carcinoma and urothelial carcinoma has been proven, and mechanistically it may be applicable to HHV-8-driven tumors.

HHV-8-related tumors, such as Kaposi sarcoma and primary effusion lymphoma, can evade the immune system through PD-1/PD-L1 signalling. Blocking PD-L1 is therefore biologically plausible.

However, the TxGNN score alone is not clinical evidence. No trials or publications were provided, and the relationship to the original indications has not yet been assessed. Immune-related toxicity in patients with HIV or other immunosuppression would need to be evaluated before any further work.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2469723 | BAVENCIO |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-L1 antibody), not a conventional cytotoxic |
| Myelosuppression Risk | Low (not a typical effect of checkpoint inhibitors) |
| Emetogenicity Classification | Low |
| Monitoring Items | Immune-related adverse events, including liver function, thyroid function, and renal function; CBC as clinically indicated |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

The rationale notes that immune-related toxicity in patients with HIV or immunosuppression would need to be assessed, since HHV-8-related tumors often occur in these populations.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no trials or literature, so it sits at L5. The mechanistic link is plausible but unverified for this indication.

Two other predictions in the pack have more support, and they could be considered first:
- Kidney pelvis sarcomatoid transitional cell carcinoma (L3, one retrospective observational study whose link to avelumab is unconfirmed).
- Prostatic urethra urothelial carcinoma (L4, extrapolated from urothelial carcinoma).

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently blocking safety screening)
- Mechanism of action data from DrugBank
- Approved indication text for the Canadian license, to confirm the original indications
- A literature and trial search on PD-L1 or checkpoint blockade in Kaposi sarcoma and primary effusion lymphoma
- A safety assessment for HIV-positive and immunosuppressed populations

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

