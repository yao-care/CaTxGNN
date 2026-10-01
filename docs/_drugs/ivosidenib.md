---
layout: default
title: Ivosidenib
parent: Model Prediction Only (L5)
nav_order: 504
evidence_level: L5
indication_count: 3
---

# Ivosidenib
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

# Ivosidenib: From IDH1-Mutant Malignancies to Bulbar Polio

## One-Sentence Summary

Ivosidenib (marketed in Canada as TIBSOVO) is a mutant IDH1 inhibitor used in IDH1-mutant cancers. The TxGNN model predicts it may be effective for **bulbar polio**, but this prediction has **0 clinical trials** and **0 publications** behind it, and no plausible biological link was identified. The supplied record lists no original indication, so the IDH1-mutant malignancy framing comes from the mechanistic analysis, not from the licensing data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied record (mechanistically, IDH1-mutant malignancies such as AML/MDS) |
| Predicted New Indication | Bulbar polio |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

It is probably not reasonable. Ivosidenib inhibits mutant IDH1, lowering 2-hydroxyglutarate (2-HG) and relieving the differentiation block in IDH1-mutant malignancies. Poliomyelitis is a viral infection of motor neurons, and no IDH1-dependent pathway is known in it.

The high score (0.993) most likely reflects an artifact of the knowledge graph, not biology. The record also has no original indication or formal mechanism-of-action entry, so the prediction cannot be checked against established pharmacology.

**Better-supported predictions for the same drug:** The model's rank 2 and 3 predictions are therapy-related myeloid neoplasms. These are AML/MDS related to alkylating agents and AML/MDS related to radiation, both with a score of 99.26%. They are biologically plausible because some therapy-related myeloid neoplasms carry IDH1 mutations. Any benefit would be expected only in IDH1-mutant cases. These entries also have no supporting trials or literature in the record, and they share the same graph neighborhood, so they are best treated as one research question.

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
| 2549980 | TIBSOVO | Not listed | Not listed |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mutant IDH1 inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bulbar polio prediction is a model-only result (L5) with no trials, no literature, and no plausible mechanism. It most likely reflects a knowledge-graph artifact, so it should not advance.

**To proceed, the following is needed:**
- Retrieve the Health Canada package insert to confirm approved indications, warnings, and contraindications. This is currently a blocking gap for safety screening.
- Obtain mechanism-of-action data from DrugBank to allow a proper mechanistic-link analysis.
- Redirect attention to the therapy-related AML/MDS entities. Search for IDH1-mutant therapy-related AML/MDS subgroup data in the ivosidenib AML/MDS trials.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

