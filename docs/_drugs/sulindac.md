---
layout: default
title: Sulindac
parent: Model Prediction Only (L5)
nav_order: 866
evidence_level: L5
indication_count: 10
---

# Sulindac
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

# Sulindac: From NSAID Use to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Sulindac is a non-steroidal anti-inflammatory drug (NSAID) that is currently marketed in Canada.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, with a score of 99.92%.
However, there are **0 clinical trials** and **0 publications** behind this prediction, and no plausible mechanistic link has been identified. It is most likely a knowledge-graph artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Sulindac is an NSAID that works by inhibiting cyclooxygenase (COX), which reduces inflammation and pain. The approved indication text for the Canadian products was also not supplied.

The predicted disease is a rare skeletal dysplasia caused by variants in the GDF5/CDMP1 gene. It arises from disrupted BMP/GDF5 signalling during bone development. COX inhibition has no known effect on this pathway, so the mechanistic review found no plausible link. The very high score of 0.999 reflects a pattern in the knowledge graph, not biological or clinical support.

The other nine top-ranked predictions (scores 99.56%–99.90%) are in the same position. Most are rare genetic skeletal or developmental disorders (e.g., brachyolmia, pseudoachondroplasia, myosclerosis, WHIM syndrome), with no mechanistic rationale and no supporting studies. Two have only a weak symptom-level rationale:

- **Rheumatoid vasculitis:** NSAIDs relieve inflammatory symptoms in rheumatoid disease, but this complication is treated with immunosuppression.
- **Hypermobility of coccyx:** NSAIDs are used for musculoskeletal pain such as coccydynia, but no studies of sulindac in this condition were supplied.

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
| 745596 | TEVA-SULINDAC |
| 745588 | TEVA-SULINDAC |

Dosage form, manufacturer and approved indication text were not available for these authorizations.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no publications, and no plausible mechanism linking COX inhibition to a GDF5-related skeletal dysplasia. This is not enough evidence to justify further investment at this time.

**To proceed, the following is needed:**
- Mechanism of action data for sulindac (e.g., from DrugBank) to test any pathway-level link to the predicted disease
- Health Canada package insert warnings and contraindications, which are blocking for safety screening
- Approved indication text for the two Canadian licenses, to confirm the original indication
- A review of the knowledge-graph edges behind the prediction to rule out an artifact
- Any preclinical or clinical evidence in the predicted disease. Without it, consider moving to the lower-ranked candidates with a plausible symptom-level rationale (rheumatoid vasculitis, hypermobility of coccyx), though these also have no supporting studies.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

