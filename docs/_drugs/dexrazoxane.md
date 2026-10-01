---
layout: default
title: Dexrazoxane
parent: Model Prediction Only (L5)
nav_order: 270
evidence_level: L5
indication_count: 10
---

# Dexrazoxane
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

# Dexrazoxane: From Anthracycline Cardioprotection to Sclerosing Cholangitis

## One-Sentence Summary

Dexrazoxane is marketed in Canada, and is generally known as a cardioprotective agent used alongside anthracycline chemotherapy. The Canadian license data in the Evidence Pack do not state an indication.
The TxGNN model predicts it may be effective for **sclerosing cholangitis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so it is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian license data (anthracycline cardioprotection is the drug's generally known use) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The Evidence Pack has no formal mechanism-of-action entry for dexrazoxane. The following comes from the mechanistic rationale in the pack. Dexrazoxane acts as an iron chelator through its metabolite ADR-925, and as a catalytic inhibitor of topoisomerase II. In theory, iron chelation could limit iron-driven oxidative injury.

This is a hypothesis, not an established link. The pack states that no direct link between dexrazoxane and sclerosing cholangitis has been established. Sclerosing cholangitis is a chronic inflammatory and fibrosing disease of the bile ducts, and no clinical or literature evidence connects it to dexrazoxane. The very high TxGNN score (0.9999) is a model output. It should not be read as evidence of efficacy, and may partly reflect knowledge-graph topology.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2153432 | ZINECARD |
| 2544083 | DEXRAZOXANE FOR INJECTION |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no registered clinical trials, no publications and no established mechanistic link, so it rests on the model score alone (Evidence Level L5). The Health Canada package insert data are also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications, approved indication), obtained and parsed
- Confirmed mechanism-of-action data from DrugBank
- A systematic literature search on iron chelation or oxidative injury in cholestatic and sclerosing bile duct disease
- Preclinical evidence (for example, animal models of cholangitis) before any clinical consideration
- Review of dosage form and route compatibility, since the Canadian license data list no dosage forms

**Other predictions:** Among the other top predictions, only cystitis (rank 10) is flagged as a "Research Question". It is a hypothesis-level link, through ferroptosis in cyclophosphamide-induced hemorrhagic cystitis, and mesna remains the standard uroprotectant. The remaining predictions have no plausible mechanism and are likely graph artifacts.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

