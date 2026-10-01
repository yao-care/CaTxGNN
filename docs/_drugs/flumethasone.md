---
layout: default
title: Flumethasone
parent: Model Prediction Only (L5)
nav_order: 389
evidence_level: L5
indication_count: 10
---

# Flumethasone
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

# Flumethasone: From an Unspecified Original Indication to Alopecia Areata

## One-Sentence Summary

Flumethasone is a corticosteroid marketed in Canada under two Locacorten Vioform products, but the supplied records do not state its original approved indication.
The TxGNN model predicts it may be effective for **alopecia areata**.
Currently **0 clinical trials** and **0 publications** support this direction, so the prediction rests on the model score and class-level reasoning alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied licence records |
| Predicted New Indication | Alopecia areata |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for flumethasone is not currently available. Flumethasone is a corticosteroid. Alopecia areata is a T-cell-mediated autoimmune attack on hair follicles, and corticosteroids are known to suppress this type of immune activity. This is why the class-level link is plausible.

This reasoning is indirect. It is drawn from the drug class, not from flumethasone-specific studies, and it was not verified against the supplied data. The high TxGNN score is a model prediction, not clinical evidence.

Nine other hair-related or dermatological predictions were also returned, and all are weaker:

- **Alopecia mucinosa, folliculitis decalvans, primary cutaneous B-cell lymphoma, alopecia universalis with onychodystrophy and vitiligo:** a corticosteroid rationale is conceivable, but no supporting evidence was supplied.
- **Telogen effluvium and the rare genetic hair disorders** (hereditary hypotrichosis with recurrent skin vesicles, atrichia with papular lesions, alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome): there is no plausible corticosteroid mechanism. The scores likely reflect knowledge-graph proximity to hair-loss phenotypes.
- **Alopecia antibody deficiency:** this carries a safety concern, because immunosuppression could worsen the underlying immunodeficiency.

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
| 74462 | LOCACORTEN VIOFORM |
| 74454 | LOCACORTEN VIOFORM EARDROPS |

The supplied records do not include dosage forms or approved indication text for these products.

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction records were found for flumethasone.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no supporting trials or literature, and the mechanism data is missing. The only support is a class-level corticosteroid rationale, so this is best treated as a research question.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which block any safety screening
- Mechanism of action data, for example from DrugBank
- The approved indications and dosage forms of the two Canadian products, to establish the original indication and route compatibility
- Flumethasone-specific trials or literature in alopecia areata
- A safety review before any further consideration of alopecia antibody deficiency
- Specialist oncology input before any consideration of primary cutaneous B-cell lymphoma
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

