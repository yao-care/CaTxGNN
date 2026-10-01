---
layout: default
title: Bacitracin
parent: Model Prediction Only (L5)
nav_order: 92
evidence_level: L5
indication_count: 10
---

# Bacitracin
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

# Bacitracin: From Topical Antibacterial Use to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Bacitracin is a topical polypeptide antibiotic. The approved indication text is not recorded in the supplied Canadian licence data.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but **0 clinical trials** and **0 publications** currently support this specific prediction.
It is a model-only signal, and the mechanistic rationale is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.999% (model rank 47) |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the supplied data. Based on known pharmacology, bacitracin blocks bacterial cell-wall synthesis by interfering with undecaprenyl pyrophosphate recycling. It is active mainly against Gram-positive organisms and is used topically.

The link to punctate epithelial keratoconjunctivitis is weak. This condition is usually viral (adenovirus), toxic, or dry-eye related, so an antibacterial mechanism would help only if a bacterial superinfection were present. The very high score most likely reflects knowledge-graph structure rather than a demonstrated therapeutic signal. No supporting trial or publication is available.

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
| 2245571 | BACIJECT |
| 584908 | BACITIN |
| 2451026 | BACITRACIN OINTMENT |
| 621366 | BIODERM OINTMENT |
| 2236917 | OZONOL ANTIBIOTICS PLUS |

Dosage forms and approved indication text are not recorded in the supplied data for these licences.

---

## Safety Considerations

No drug-interaction records were found for this drug.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5), with no trials or publications. The proposed mechanism is indirect, since the condition is mostly non-bacterial.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Confirmed approved indications and dosage forms for the five DINs
- Mechanism-of-action data from DrugBank
- Any clinical evidence for bacitracin in punctate epithelial keratoconjunctivitis, or a bacterial-superinfection rationale

**Other predictions worth noting:**
- **Otitis externa** (rank 4) is the best-supported candidate (L4, Research Question). A 2007 double-blind study of 151 patients tested a polymyxin B + bacitracin ointment with and without hydrocortisone. The other five publications are older reviews or clinical reports, or non-bacitracin studies. Full-text review is needed to confirm which agents were tested.
- **Non-human animal disease** is a non-specific ontology category and should be excluded from review.
- **Infection-related hemolytic uremic syndrome** carries a safety concern, because bacitracin is nephrotoxic and antibiotics are generally not recommended in STEC-HUS.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

