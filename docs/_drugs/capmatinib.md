---
layout: default
title: Capmatinib
parent: Model Prediction Only (L5)
nav_order: 152
evidence_level: L5
indication_count: 10
---

# Capmatinib
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

# Capmatinib: From MET-Driven Cancer to Rheumatoid Arthritis

## One-Sentence Summary

Capmatinib is a selective MET kinase inhibitor used in oncology and marketed in Canada as TABRECTA.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but there are **0 clinical trials** and only **1 general review article** (no RA-specific data), so this is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | MET-driven cancer (the licence records supplied contain no indication text) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the supplied record. Capmatinib is known to be a selective MET inhibitor, and its efficacy in MET-dysregulated tumours is the basis of its marketed use. Mechanistically, it may be applicable to rheumatoid arthritis, but this is speculative.

MET/HGF signalling has been discussed in synovial inflammation and angiogenesis, both features of rheumatoid arthritis. This makes a link plausible. However, the only linked paper is a general review of FDA-approved kinase inhibitors, and it contains no RA-specific data for capmatinib. The high model score reflects a knowledge-graph prediction, not experimental or clinical support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33513356](https://pubmed.ncbi.nlm.nih.gov/33513356/) | 2021 | Review | Pharmacological Research | 2021 update on the properties of FDA-approved small-molecule protein kinase inhibitors. It is a general overview and has no RA-specific data for capmatinib. |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2527405 | TABRECTA |
| 2527391 | TABRECTA |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (MET kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: A completed Phase 1 study (NCT02626234, n=32) assessed the effect of capmatinib on the pharmacokinetics of digoxin and rosuvastatin in patients with MET-dysregulated solid tumours. Its results are not summarised in the supplied data, so please consult the source record.
- **Class caution**: Kinase inhibitors can carry cardiac safety liabilities. This has not been assessed for capmatinib in RA.

For all other safety information, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but it rests on the model alone. There are no trials, and the only paper is a general kinase inhibitor review. The MET–RA link is biologically plausible but unsupported by any capmatinib-specific data.

**To proceed, the following is needed:**
- Preclinical evidence, such as arthritis models or synovial-tissue studies, testing MET inhibition or capmatinib in RA
- Mechanism of action data for capmatinib
- Health Canada package insert warnings and contraindications, for safety screening
- Approved indication text for the two DINs, to confirm the original indication

**Note on other candidates:** Among the other predictions, **heart disease** (score 98.64%) has slightly stronger support (Evidence Level L4). One preclinical mouse study (PMID 32333917) reports that capmatinib offset doxorubicin-induced cardiotoxicity and cisplatin nephrotoxicity. This evidence is indirect and limited to chemotherapy-induced toxicity. It is best treated as a research question rather than a treatment candidate. The remaining predictions (rare congenital syndromes and hyperthyroidism) have no supporting evidence.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

