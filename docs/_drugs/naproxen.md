---
layout: default
title: Naproxen
parent: Model Prediction Only (L5)
nav_order: 540
evidence_level: L5
indication_count: 4
---

# Naproxen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Naproxen: From NSAID (Analgesic/Anti-Inflammatory Use) to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Naproxen is a nonsteroidal anti-inflammatory drug (NSAID) acting through COX enzyme inhibition, used for pain, fever, and inflammation. The TxGNN model predicts it may be effective for **Brachydactyly-Syndactyly Syndrome**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-derived hypothesis only, and the evidence pack's own mechanistic review flags it as biologically implausible.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — Naproxen is not currently marketed in Canada under this evidence pack, and no approved indication text was returned |
| Predicted New Indication | Brachydactyly-Syndactyly Syndrome |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Naproxen is not available in this evidence pack (flagged as a High-severity data gap). Based on the pharmacological description embedded in the evidence pack's own rationale, Naproxen acts as a COX enzyme inhibitor with anti-inflammatory and antipyretic-analgesic effects — the standard NSAID mechanism.

However, the top predicted indication, Brachydactyly-Syndactyly Syndrome, is a congenital limb malformation (shortened digits with syndactyly) caused by abnormal gene regulation during embryonic development — not an inflammatory, pain-related, or prostaglandin-mediated condition. According to the evidence pack's own mechanistic assessment, there is no plausible biological link between Naproxen's COX-inhibition mechanism and this structural developmental defect.

The same pattern holds across the other three ranked predictions (colobomatous microphthalmia-rhizomelic dysplasia syndrome, acromesomelic dysplasia Hunter-Thompson type, and brachyolmia-amelogenesis imperfecta syndrome): all are rare congenital skeletal/craniofacial dysplasia syndromes rooted in embryonic or genetic developmental pathways, with no established pharmacological connection to NSAID activity. The evidence pack explicitly characterizes these as statistical associations from the TxGNN knowledge graph rather than mechanistically grounded hypotheses.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Canada Market Information

Naproxen currently has 0 DINs on record and no active Canadian market authorizations in this evidence pack; no product listing is available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate sits at Evidence Level L5 (model prediction only) with no clinical trials or literature support, and the evidence pack's own mechanistic review finds no biological plausibility linking Naproxen's NSAID/COX-inhibition mechanism to any of the four predicted congenital skeletal/developmental syndromes. A Blocking-severity data gap (TFDA/regulatory warnings and contraindications) also prevents progression to the S1 safety review stage.

**To proceed, the following is needed:**
- TFDA/regulatory package insert (warnings, contraindications) to clear the Blocking data gap (DG001)
- Confirmed mechanism of action (MOA) data from DrugBank or equivalent source (DG002)
- A biologically plausible mechanistic hypothesis connecting Naproxen to any candidate indication before further evidence collection is warranted
- Consider re-screening lower-ranked TxGNN candidates for mechanistic fit, since the current top 4 are all rare congenital developmental syndromes unrelated to NSAID pharmacology
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

