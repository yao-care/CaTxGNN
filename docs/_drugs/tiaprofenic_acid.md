---
layout: default
title: Tiaprofenic Acid
parent: Model Prediction Only (L5)
nav_order: 912
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Tiaprofenic Acid: predicted new indication Brachydactyly-syndactyly syndrome (evidence level L5). Approved use: Rheumatoid arthritis, osteoarthritis, arthropathy"
monitor_inn: "TIAPROFENIC ACID"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "myosclerosis", "spondyloarthropathy, susceptibility to", "brachyolmia", "factor 5 excess with spontaneous thrombosis", "heparin cofactor 2 deficiency", "pseudoachondroplasia"]
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

# Tiaprofenic Acid: From Rheumatoid Arthritis and Osteoarthritis to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Tiaprofenic acid is a nonsteroidal anti-inflammatory drug (NSAID) originally used for inflammatory and degenerative joint conditions such as rheumatoid arthritis and osteoarthritis.
The TxGNN model predicts it may be effective for **brachydactyly-syndactyly syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction. It rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, arthropathy (based on the knowledge-graph indication data; no approved indication text is available for the Canadian licences) |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tiaprofenic acid is a propionic acid-derivative NSAID, presumed to act through cyclooxygenase (COX) inhibition. Its use in rheumatoid arthritis and osteoarthritis rests on reducing inflammatory pain and stiffness.

Brachydactyly-syndactyly syndromes are congenital limb malformations, generally driven by developmental gene mutations (for example, HOXD13 and related pathways). COX inhibition is not expected to correct a structural genetic defect, so **no plausible mechanistic link has been established**. The very high TxGNN score most likely reflects the drug's proximity in the knowledge graph to the skeletal and joint-disorder neighbourhood of its original indications, not a biologically credible therapeutic effect.

### Other Predictions Reviewed

Nine other predictions were reviewed, and all are also at evidence level L5 with no trials or literature:

| Predicted Indication | TxGNN Score | Assessment |
|------|------|------|
| Spondyloarthropathy, susceptibility to | 99.99% | The most biologically plausible candidate. NSAIDs are first-line therapy for spondyloarthritis. However, the indication is a genetic predisposition rather than an active disease. Classified as a "Research Question"; a targeted literature search is a reasonable next step. |
| Pseudoachondroplasia | 99.98% | Limited and indirect. Early-onset joint degeneration might allow symptomatic pain relief, but the underlying disease would not be modified. |
| Myosclerosis | 99.99% | Weak and speculative. Fibrosis is not primarily driven by prostaglandin pathways. |
| Brachyolmia-amelogenesis imperfecta syndrome, brachyolmia, acromesomelic dysplasia (Hunter-Thompson type), colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.99% to 99.98% | No mechanistic link. These are genetic developmental disorders that NSAIDs do not address. |
| Factor 5 excess with spontaneous thrombosis, heparin cofactor 2 deficiency | 99.98% | No therapeutic link, and a safety concern. NSAIDs affect platelet function and carry cardiovascular and bleeding cautions in prothrombotic conditions. |

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
| 02179679 | TEVA-TIAPROFENIC ACID | Not specified | Not specified |
| 02179687 | TEVA-TIAPROFENIC ACID | Not specified | Not specified |

Both licences are valid single-ingredient products.

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug-interaction records were found in the data compiled for this report. Because NSAIDs can affect platelet function and carry cardiovascular and bleeding-related cautions, any use in a prothrombotic condition would need careful risk assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, brachydactyly-syndactyly syndrome, has no clinical, literature, or mechanistic support. It is most likely an artifact of knowledge-graph proximity. A congenital developmental defect is unlikely to respond to COX inhibition.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, which are required before any safety screening
- Mechanism of action data for tiaprofenic acid
- A targeted literature search on tiaprofenic acid in axial spondyloarthritis, the only prediction with a coherent rationale
- Evidence of any clinical benefit before reconsidering the brachydactyly-syndactyly prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

