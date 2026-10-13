---
layout: default
title: Obinutuzumab
parent: Model Prediction Only (L5)
nav_order: 673
evidence_level: L5
indication_count: 3
---

# Obinutuzumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Obinutuzumab: From Acute Lymphoblastic Leukaemia and Richter Syndrome to Pregerminal Center CLL/SLL

## One-Sentence Summary

Obinutuzumab (Canadian brand GAZYVA) is an anti-CD20 antibody. The knowledge graph lists its original indications as acute lymphoblastic leukaemia and Richter syndrome.
The TxGNN model predicts it may be effective for **pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma (CLL/SLL)**, an unmutated-IGHV subtype of CLL.
**No clinical trials and no publications** specific to this subtype were compiled, so the prediction rests on the model score and indirect mechanistic reasoning.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute lymphoblastic/lymphocytic leukaemia; Richter syndrome (from the knowledge graph, because Canadian licence text was not available) |
| Predicted New Indication | Pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma |
| TxGNN Prediction Score | 99.21% |
| Evidence Level | L5 (model prediction only, no subtype-specific studies) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data were not available in the compiled data. Obinutuzumab is a known glycoengineered type II anti-CD20 monoclonal antibody. It acts through direct B-cell death and enhanced antibody-dependent cellular cytotoxicity and phagocytosis.

The predicted disease is the unmutated-IGHV molecular subtype of CLL/SLL. CD20 is expressed on CLL cells, and obinutuzumab is an established anti-CD20 treatment for CLL. The subtype is therefore largely covered by the parent-disease indication. CD20 expression does not depend on IGHV status, so anti-CD20 activity is mechanistically plausible.

This is **not a clearly novel repurposing finding**. The high score (99.21%) mostly reflects overlap with the drug's established CLL use. No subtype-specific data support it independently.

**Other predictions in the data.** Two other predictions have similar scores:
- The mutated-IGHV CLL/SLL subtype, which has the same limitations as the one above.
- **Follicular lymphoma** (score 99.18%), which has far more evidence. This includes randomised phase 3 data such as GALLIUM, obinutuzumab versus rituximab immunochemotherapy in previously untreated follicular lymphoma. Follicular lymphoma appears to be already established in practice, so it is better described as label-aligned than as a new indication.

The listed original indications (ALL, Richter syndrome) also look incomplete for this drug. The repurposing framing should be checked against the actual Canadian label.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this predicted indication.

---

## Literature Evidence

Currently no related literature available for this predicted indication.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02434806 | GAZYVA | Not specified in the compiled data | Not specified in the compiled data |

The licence is a valid single-ingredient product with no cancelled licences.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy / immunotherapy (anti-CD20 monoclonal antibody), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; blood counts and routine laboratory monitoring are typical for anti-CD20 therapy |
| Handling Protection | Please refer to the package insert and local institutional policy for handling antineoplastic biologics |

---

## Safety Considerations

Package-insert warnings and contraindications were not compiled for this report. Please refer to the package insert for these.

**Drug Interactions:** The interaction database returned 81 interacting drugs. Examples of the main ones:

- **Major:** deferiprone, samarium (153Sm) lexidronam, adalimumab, baricitinib, certolizumab pegol, cladribine, clozapine
- **Moderate:** strontium chloride Sr-89, roflumilast, chloramphenicol, zidovudine, alemtuzumab, alefacept, anakinra, azathioprine, canakinumab, and several vaccines (tetanus toxoid, anthrax, live cholera)

Many of these are immunosuppressive or myelosuppressive agents, or vaccines. This points to additive immunosuppression, additive myelosuppression, and vaccine-response concerns.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but it is not backed by any subtype-specific trials or publications. The prediction mostly restates obinutuzumab's established use in CLL rather than identifying a new indication. At this stage it does not justify a separate repurposing programme.

**To proceed, the following is needed:**
- Confirmation of the approved indications on the Canadian label (the licence text was not available), to establish whether CLL/SLL is already covered
- Subtype-specific evidence for unmutated-IGHV CLL/SLL, such as analyses of CLL trials stratified by IGHV status
- Mechanism-of-action data (MOA) in the structured record
- Package-insert warnings and contraindications, to complete safety screening
- Consideration of the follicular lymphoma prediction as a separate evaluation, since it has the strongest evidence, while recognising that it appears to be established practice
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

