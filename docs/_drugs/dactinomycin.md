---
layout: default
title: Dactinomycin
parent: Model Prediction Only (L5)
nav_order: 240
evidence_level: L5
indication_count: 9
---

# Dactinomycin
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

# Dactinomycin: From Antineoplastic Use to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

Dactinomycin is a cytotoxic anticancer antibiotic, best known as a component of vincristine, actinomycin D and cyclophosphamide (VAC) chemotherapy for childhood sarcomas.
The TxGNN model predicts it may be effective for **relapsing-remitting multiple sclerosis**, but **0 clinical trials** and **0 publications** currently support this direction, so it is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Relapsing-remitting multiple sclerosis |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied dataset. Based on known information, dactinomycin is a cytotoxic transcription inhibitor that blocks DNA-dependent RNA synthesis. Its efficacy in rhabdomyosarcoma and other paediatric tumours is established. Mechanistically, an immunosuppressive effect on proliferating immune cells is conceivable, which could be relevant to multiple sclerosis.

The link is weak, though. Dactinomycin's toxicity (myelosuppression, hepatotoxicity, extravasation injury) makes a chronic-use benefit-risk profile unfavourable compared with approved multiple sclerosis therapies. The high score is most likely a knowledge-graph artifact from shared immunomodulatory or antineoplastic neighbours, rather than a signal of real clinical promise.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 213071 | COSMEGEN |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antitumour antibiotic, transcription inhibitor) |
| Myelosuppression Risk | High (myelosuppression is a recognised toxicity) |
| Emetogenicity Classification | Moderate to high; please refer to the package insert |
| Monitoring Items | CBC with differential, liver function (watch for veno-occlusive disease), renal function, infusion site |
| Handling Protection | Must follow cytotoxic drug handling regulations; strong tissue irritant, so avoid extravasation |

---

## Safety Considerations

- **Key Warnings**: The supplied analysis notes myelosuppression, hepatotoxicity (including hepatic veno-occlusive disease in combination chemotherapy) and extravasation injury. These are not taken from the Health Canada package insert, which has not yet been obtained.

Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5), with no trials or literature. The drug's toxicity profile is difficult to justify for a chronic, non-malignant autoimmune disease with many approved alternatives.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence for dactinomycin in demyelinating or autoimmune disease
- Health Canada package insert warnings and contraindications
- Detailed mechanism of action data and an analysis of the mechanistic link to multiple sclerosis
- Approved indication text for the Canadian licence (currently missing)

**Note on other predictions:** The rhabdomyosarcoma-related predictions for this drug are much better supported. Parameningeal embryonal rhabdomyosarcoma reaches L1 with a "Proceed with Guardrails" recommendation. This reflects established standard-of-care use (VAC regimens) rather than true repurposing, so on-label status should be checked against the label. Those predictions merit review ahead of the multiple sclerosis prediction.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

