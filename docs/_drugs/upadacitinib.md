---
layout: default
title: Upadacitinib
parent: Model Prediction Only (L5)
nav_order: 958
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Upadacitinib: predicted new indication Colobomatous microphthalmia-rhizomelic dysplasia syndrome (evidence level L5). Approved use: Rheumatoid arthritis"
monitor_inn: "UPADACITINIB"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
---

# Upadacitinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Upadacitinib: From Rheumatoid Arthritis to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome
{: .text-alpha }

## One-Sentence Summary

Upadacitinib was originally used to treat rheumatoid arthritis.
The TxGNN model predicts it may be effective for **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, a rare developmental disorder.
This prediction currently has **no supporting clinical trials or publications**, and no plausible mechanistic link has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis |
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 0.9961 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 3 of 3) |
| Number of DINs | 3 (valid: 3) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, upadacitinib is a selective JAK1 inhibitor that blocks cytokine signaling through the JAK-STAT pathway. This explains its efficacy in rheumatoid arthritis and other autoimmune and inflammatory diseases.

The predicted indication is a rare developmental disorder involving ocular coloboma and microphthalmia together with skeletal rhizomelic dysplasia. Such conditions are presumed to be genetic and structural. No clear link to JAK1-mediated inflammatory signaling is evident. Developmental malformations are also not expected to respond to an immunomodulator in postnatal patients.

The high score (0.9961) therefore comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The prediction should be treated as a hypothesis with very low plausibility until independent evidence emerges.

A second prediction, brachydactyly-syndactyly syndrome (score 0.9958), has the same weaknesses: no trials, no literature, and no mechanistic rationale for JAK inhibition in a congenital limb malformation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02539721 | RINVOQ | Not specified | Not specified |
| 02520893 | RINVOQ | Not specified | Not specified |
| 02495155 | RINVOQ | Not specified | Not specified |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the data compiled for this report. The main ones listed include:
  - **Major**: corticosteroids (hydrocortisone, prednisone, prednisolone, dexamethasone, betamethasone, triamcinolone, budesonide, beclomethasone dipropionate), clarithromycin, cobicistat, deferiprone, iobenguane (I-131)
  - **Moderate**: aprepitant, cimetidine, miconazole, deferasirox
  - **Minor**: zinc salts (sulfate, acetate, gluconate)
- **Class-level concerns**: Upadacitinib is a JAK inhibitor, and this drug class is associated with serious infections, thrombosis, malignancy and major adverse cardiovascular events (MACE). These risks are not justified without supporting evidence of benefit in the predicted indication.

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for this prediction is a high model score. There are no clinical trials, no publications, and no plausible mechanistic link between JAK1 inhibition and a congenital developmental syndrome. Given the safety profile of JAK inhibitors, there is no basis to advance this candidate.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, to allow a proper mechanistic-link analysis
- Any preclinical or genetic evidence connecting JAK-STAT signaling to the pathology of this syndrome
- Approved indication text and dosage form details for the Canadian DINs
- Consideration of other candidate indications with stronger biological plausibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

