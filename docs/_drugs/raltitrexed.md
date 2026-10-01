---
layout: default
title: Raltitrexed
parent: Model Prediction Only (L5)
nav_order: 784
evidence_level: L5
indication_count: 10
---

# Raltitrexed
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

# Raltitrexed: From Antineoplastic Use to Sclerosing Cholangitis

## One-Sentence Summary

Raltitrexed is a thymidylate synthase-inhibiting antifolate cytotoxic drug, marketed in Canada as TOMUDEX.
The TxGNN model predicts it may be effective for **sclerosing cholangitis**, with a very high score (99.97%).
However, there are currently **0 clinical trials** and **0 publications** supporting this direction, so it remains a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the source data |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on known information, raltitrexed is a thymidylate synthase inhibitor (an antifolate cytotoxic agent). Its approved indication text was not captured, so the relationship between the original and new indication cannot be assessed directly.

For sclerosing cholangitis, no clear mechanistic link exists. It is an immune-mediated fibroinflammatory disease of the bile ducts, and a cytotoxic antimetabolite has no established rationale there. Raltitrexed is also associated with transaminase elevations, which is a concern in cholestatic liver disease. The high TxGNN score is a model output with no supporting trials or literature.

The model also produced nine further predictions for this drug. All are L5, with no trials or literature, and all are on Hold:

| Predicted Indication | Score | Assessment |
|------|------|------|
| Myelodysplastic syndrome (MDS) | 99.97% | Weak theoretical plausibility: antimetabolites could target clonal proliferation. Raltitrexed myelosuppression could worsen existing cytopenias. |
| Unclassified MDS, refractory cytopenia of childhood, partial deletion of the long arm of chromosome 5 | 99.96% | MDS-related subtypes and cytogenetic abnormality; likely propagated from the parent MDS node. There are no pediatric safety data. |
| Five sickle cell disease subtypes (HbE, HbC, HbD, beta-thalassemia, hereditary persistence of fetal hemoglobin) | 99.96% | Speculative HbF-induction rationale, which is not established for thymidylate synthase inhibitors. Identical scores suggest propagation from a shared parent node rather than independent signals. Myelosuppression is a safety concern. |

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
| 2229566 | TOMUDEX |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antifolate, thymidylate synthase inhibitor) |
| Myelosuppression Risk | Significant; myelosuppression is a dose-limiting toxicity |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC (with differential), liver function (transaminases), renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Hepatic**: Raltitrexed is associated with transaminase elevations, a concern in cholestatic liver disease such as sclerosing cholangitis.
- **Haematological**: Myelosuppression could worsen cytopenias in MDS and sickle cell populations.
- **Pediatric**: No pediatric safety data are available for the refractory cytopenia of childhood prediction.

No drug interaction records were found. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predictions are L5, supported only by the TxGNN model with no trials or literature. The mechanistic rationale is absent or weak for every one, and the known hepatic and myelosuppressive toxicities raise safety concerns in the predicted populations.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data from DrugBank
- Approved indication text and dosage form for the Canadian license
- A literature and trial search for the top candidates, especially MDS
- Confirmation of whether the sickle cell predictions are independent signals or propagated from a shared parent disease node
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

