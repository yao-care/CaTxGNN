---
layout: default
title: Tiaprofenic Acid
parent: Model Prediction Only (L5)
nav_order: 773
evidence_level: L5
indication_count: 10
---

# Tiaprofenic Acid
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

# Tiaprofenic Acid: From NSAID Anti-Inflammatory Therapy to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

> Tiaprofenic acid is a propionic-acid class NSAID (COX-1/2 inhibitor), though its specific original approved indication is not captured in the current dataset.
> The TxGNN model predicts a possible association with **Brachydactyly-Syndactyly Syndrome**, a rare congenital limb-development disorder,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug is not marketed in Canada and no license/indication text exists in this dataset (drug class inferred as propionic-acid NSAID from evidence context) |
| Predicted New Indication | Brachydactyly-Syndactyly Syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug in the evidence pack. Based on contextual information embedded in the rationale fields, tiaprofenic acid belongs to the propionic-acid class of NSAIDs, acting through COX-1/2 inhibition — a mechanism typically applied to inflammatory and pain-related conditions.

However, the evidence pack's own mechanistic assessment for the top-ranked prediction is explicitly negative: brachydactyly-syndactyly syndrome is a structural, genetically-driven limb-development disorder, and the rationale states there is **no plausible pathophysiological connection** to NSAID/COX-inhibition pharmacology. This pattern repeats across nearly all 10 ranked candidates in this pack — most are rare skeletal, ocular, or coagulation-related genetic syndromes with rationale text explicitly noting "no mechanistic relevance" or only weak, indirect associations (e.g., secondary joint pain in skeletal dysplasias). Only rank 6 (spondyloarthropathy susceptibility) and rank 10 (pseudoachondroplasia) note any plausible symptomatic rationale (joint pain/inflammation), and even these are caveated as lacking direct supporting evidence.

In short, this set of predictions appears to reflect knowledge-graph embedding similarity rather than a biologically grounded repurposing signal. All 10 candidates are rated **L5 (model prediction only)**, with zero corroborating trials or literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Canada Market Information

This drug is not currently marketed in Canada (0 DINs on record). No license or product information is available in this dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Key warnings, contraindications, and drug-interaction data are flagged as a Blocking data gap in this evidence pack — see below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 ranked predictions are L5 evidence (model prediction only), with zero clinical trials or literature support, and the top-ranked candidate's own mechanistic rationale states there is no plausible pathophysiological link between the drug's NSAID mechanism and the predicted rare genetic syndrome. Combined with the drug's absence from the Canadian market and a Blocking-severity safety data gap, this candidate does not meet the threshold to advance past initial screening.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert (warnings, contraindications, DDI) — currently a Blocking gap (DG001)
- Confirmed mechanism of action from DrugBank or primary literature (DG002)
- Any preclinical or case-level evidence directly linking tiaprofenic acid to skeletal/connective-tissue or genetic-syndrome pathways, if this candidate is to be re-evaluated
- Given the absence of supporting evidence across all 10 candidates, consider deprioritizing this drug in favor of candidates with higher evidence levels (L1–L3)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

