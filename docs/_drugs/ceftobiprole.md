---
layout: default
title: Ceftobiprole
parent: Model Prediction Only (L5)
nav_order: 168
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ceftobiprole: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Not stated in the data compiled for this report (ceftobiprole is a ce…"
monitor_inn: "Ceftobiprole"
predicted_indications: ["rheumatoid arthritis", "osteoarthritis", "osteoarthritis susceptibility", "gout", "pseudoachondroplasia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "hemoglobinopathy", "brachyolmia", "acromesomelic dysplasia, Hunter-Thompson type", "myosclerosis"]
---

# Ceftobiprole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Ceftobiprole: From Bacterial Infection to Rheumatoid Arthritis

## One-Sentence Summary

Ceftobiprole is a cephalosporin antibiotic with activity against MRSA, marketed in Canada as ZEVTERA. The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on a graph-based score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (ceftobiprole is a cephalosporin antibiotic) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 98.45% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, ceftobiprole is a cephalosporin antibiotic that inhibits penicillin-binding proteins (PBPs) and blocks bacterial cell wall synthesis, including in MRSA. Its proven role is in bacterial infection.

The analysis found **no established mechanism** linking ceftobiprole to rheumatoid arthritis. It has no known immunomodulatory action relevant to autoimmune synovitis. The high TxGNN score reflects proximity in a knowledge graph, not a demonstrated therapeutic signal. The same applies to the other top predictions, all scored 97–98%:

- Osteoarthritis and osteoarthritis susceptibility: a degenerative joint disease and a genetic susceptibility phenotype, neither of which an antibacterial mechanism addresses.
- Gout: no known effect on urate metabolism or inflammasome activity.
- Rare skeletal dysplasias (pseudoachondroplasia, brachyolmia, Hunter-Thompson acromesomelic dysplasia, colobomatous microphthalmia-rhizomelic dysplasia syndrome) and myosclerosis: likely artifacts of network proximity among related nodes.
- Hemoglobinopathy: no known action on globin synthesis or function.

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
| 02446685 | ZEVTERA | Not listed | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information. No interaction records were found in the data compiled for this report, and no drug-disease contraindications were identified from the knowledge graph.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials, no literature, and no plausible mechanism linking an anti-MRSA cephalosporin to rheumatoid arthritis. The other top nine predictions are similarly unsupported.

**To proceed, the following is needed:**
- Mechanism of action data, to test whether any immunomodulatory or anti-inflammatory activity exists.
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening).
- Approved indication text and dosage form for the ZEVTERA license.
- Preclinical or literature evidence of ceftobiprole activity in inflammatory arthritis models.
- Route-of-administration compatibility and similarity to the original indication, both still pending.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

