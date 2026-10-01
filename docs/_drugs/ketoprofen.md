---
layout: default
title: Ketoprofen
parent: Model Prediction Only (L5)
nav_order: 507
evidence_level: L5
indication_count: 10
---

# Ketoprofen
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

# Ketoprofen: From Pain and Inflammation Relief to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ketoprofen is a non-steroidal anti-inflammatory drug (NSAID) used for pain and inflammation.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, but **0 clinical trials** and **0 publications** support this prediction.
The high score most likely reflects a knowledge-graph artifact rather than a real therapeutic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the license data (ketoprofen is an NSAID used for pain and inflammation) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Based on known information, ketoprofen is a non-selective COX-1/COX-2 inhibitor. It reduces prostaglandin-mediated pain and inflammation, and its efficacy in these settings is well established.

Acromesomelic dysplasia, Hunter-Thompson type, is a genetic skeletal dysplasia caused by defects in the CDMP1/GDF5 pathway, which controls growth-plate signaling. Nothing suggests that COX inhibition alters this pathway or the disease course. No plausible mechanistic link was identified, so the very high TxGNN score is likely a knowledge-graph artifact.

The other top-ranked predictions show the same pattern. Most are rare genetic skeletal or developmental disorders (brachyolmia, pseudoachondroplasia, brachydactyly-syndactyly syndrome and others) with no mechanistic rationale. The two most biologically plausible candidates are spondyloarthropathy and LACC1-related juvenile arthritis. In both, the rationale is the general symptomatic use of NSAIDs, not a new ketoprofen-specific signal.

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
| 2172577 | KETOPROFEN SR |
| 790435 | KETOPROFEN-E |
| 842664 | KETOPROFEN-E |

Dosage form and approved indication text were not provided for these authorizations.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical or literature support (L5), and no plausible mechanistic link exists between COX inhibition and a genetic growth-plate disorder. Ketoprofen is already marketed in Canada, but that does not support this new indication.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data from DrugBank
- Any preclinical or mechanistic evidence linking ketoprofen to GDF5/CDMP1 signaling
- If the aim is a more credible use, re-prioritize spondyloarthropathy or LACC1-related juvenile arthritis. Those would need ketoprofen-specific data and a comparison against approved NSAIDs.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

