---
layout: default
title: Ibuprofen
parent: 僅模型預測 (L5)
nav_order: 390
evidence_level: L5
indication_count: 7
---

# Ibuprofen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Ibuprofen: From NSAID (Pain/Inflammation) to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ibuprofen is a globally established nonsteroidal anti-inflammatory drug (NSAID) that inhibits COX-1/COX-2 and is conventionally used for pain, fever, and inflammation; no Canadian market authorization record is present in this evidence pack.
The TxGNN model predicts it may be relevant to **Acromesomelic Dysplasia, Hunter-Thompson Type**, a rare GDF5-gene-mutation skeletal dysplasia, but this is currently supported by **0 clinical trials** and **0 publications** — the prediction rests entirely on knowledge-graph embedding similarity, and the evidence pack's own mechanistic rationale states there is **no known biological connection** between COX inhibition and this structural/developmental disorder.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Canadian regulatory data (no licenses on file; drug currently 未上市/Not Marketed in Canada). Ibuprofen is universally known as an NSAID for pain, fever, and inflammation, but this is general pharmacological knowledge, not sourced from the regulatory dataset. |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 (model prediction only — no clinical trials, no literature) |
| Canada Market Status | ✗ Not Marketed (未上市) |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed, drug-specific mechanism-of-action documentation is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on well-established pharmacological knowledge, Ibuprofen acts as a **COX-1/COX-2 inhibitor**, blocking prostaglandin synthesis to reduce pain, fever, and inflammation.

Acromesomelic Dysplasia, Hunter-Thompson Type, however, is caused by mutations in **GDF5**, a gene governing cartilage and joint morphogenesis. Its pathology is structural/developmental (abnormal skeletal patterning), not inflammation-mediated. The evidence pack's own repurposing rationale is explicit on this point: there is **no known mechanistic link** between prostaglandin-pathway inhibition and GDF5-driven skeletal dysplasia.

In other words, the high TxGNN score (99.74%) most likely reflects graph-embedding proximity (e.g., shared metadata, co-occurring nodes, or structural similarity in the knowledge graph) rather than a plausible pharmacological pathway. Because Ibuprofen's own original-indication and MOA records are themselves incomplete in this dataset, there is also no verified baseline to compare against. This prediction should be treated as a hypothesis-generating signal only, not as evidence of therapeutic relevance.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

No active Health Canada market authorizations (DINs) were found for Ibuprofen in this dataset — market status is recorded as **未上市 (Not Marketed)**, with 0 total licenses on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

Note: TFDA/Health Canada label warnings and contraindications are recorded as a **Blocking** data gap (DG001) — this absence by itself prevents the candidate from entering the S1 safety pre-assessment stage, independent of the efficacy evidence discussed above.

---

## Other Model-Predicted Candidates (Same Drug, Not Detailed Above)

For context, TxGNN generated several similarly-scored rare skeletal/developmental disease predictions for Ibuprofen in this run, none of which have clinical trial or literature support and all of which carry the same "Hold" recommendation:

| Rank | Predicted Disease | TxGNN Score | Evidence Level | Decision |
|------|-------------------|-------------|-----------------|----------|
| 2 | Brachyolmia-amelogenesis imperfecta syndrome | 99.71% | L5 | Hold |
| 3 | Myosclerosis | 99.68% | L5 | Hold |
| 4 | Brachyolmia | 99.67% | L5 | Hold |
| 5 | Brachydactyly-syndactyly syndrome | 99.66% | L5 | Hold |
| 6 | Pseudoachondroplasia | 99.66% | L5 | Hold |
| 7 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.60% | L5 | Hold |

The clustering of Ibuprofen's top predictions around rare structural/skeletal dysplasias — rather than inflammation-related conditions — further supports the interpretation that these scores reflect knowledge-graph artifacts rather than genuine mechanistic candidates.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction has no clinical trial or literature support (Evidence Level L5), and the evidence pack's own mechanistic rationale states there is no known biological link between Ibuprofen's COX-inhibition mechanism and this GDF5-driven skeletal dysplasia.
- A Blocking-severity data gap (missing TFDA/Health Canada label warnings and contraindications) independently prevents this candidate from entering safety pre-assessment, and the drug currently has no active Canadian market authorization.

**To proceed, the following is needed:**
- Health Canada / TFDA product monograph data (warnings, contraindications) to resolve the Blocking data gap (DG001)
- Confirmed original indication and MOA data for Ibuprofen (DG002)
- Any preclinical or mechanistic studies specifically linking prostaglandin-pathway modulation to GDF5-related skeletal development, if such a hypothesis is to be pursued further
- Given the consistent lack of mechanistic and empirical support across all top-ranked predictions for this drug, reprioritization toward other TxGNN candidates with plausible mechanistic rationale is recommended before committing further review resources here
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

