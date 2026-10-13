---
layout: default
title: Lumacaftor
parent: Model Prediction Only (L5)
nav_order: 565
evidence_level: L5
indication_count: 10
---

# Lumacaftor
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

# Lumacaftor: From Cystic Fibrosis to Leprosy

## One-Sentence Summary

Lumacaftor is a CFTR corrector originally used to treat cystic fibrosis (marketed in Canada as ORKAMBI).
The TxGNN model predicts it may be effective for **leprosy**,
but **no clinical trials and no publications** currently support this prediction. It is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cystic fibrosis |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, lumacaftor is a CFTR corrector that improves the folding and trafficking of F508del-CFTR protein, and its use in cystic fibrosis is established.

Leprosy is a chronic infection caused by *Mycobacterium leprae*, and no plausible CFTR-related pathway is evident. The high TxGNN score (0.994) is a computational prediction only. It may reflect proximity in the knowledge graph rather than true biology, and the prediction is not supported by any trial or publication.

Other top-ranked predictions (migraine subtypes, rheumatoid arthritis, pulmonary hypertension, kyphoscoliotic heart disease, multiple endocrine neoplasia, brachydactyly-syndactyly syndrome, nephrogenic syndrome of inappropriate antidiuresis) share the same limitation: high scores, no clinical or literature support, and no established mechanistic link.

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
| 02451379 | ORKAMBI | Not specified | Not specified |
| 02483831 | ORKAMBI | Not specified | Not specified |
| 02463040 | ORKAMBI | Not specified | Not specified |
| 02483858 | ORKAMBI | Not specified | Not specified |
| 02537087 | ORKAMBI | Not specified | Not specified |

---

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 interacting drugs. The first 20 returned are summarized below.
  - **Major**: Eliglustat, Naldemedine, Naloxegol, Rolapitant
  - **Moderate**: Acetohexamide, Betamethasone, Bupropion, Dexlansoprazole, Esomeprazole, Glimepiride, Lansoprazole, Linagliptin, Nitisinone, Omeprazole, Pantoprazole, Pioglitazone, Prednisone, Rabeprazole, Ranitidine, Repaglinide
- Lumacaftor induces CYP3A, which would complicate co-administration with many drugs, including agents commonly used in pulmonary hypertension.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN score, with no clinical trials, no publications, and no plausible mechanistic link between CFTR correction and *M. leprae* infection. Lumacaftor also carries a substantial interaction burden, so there is no basis to advance.

**To proceed, the following is needed:**
- Mechanism of action data and a testable biological hypothesis linking CFTR correction to leprosy
- Preclinical or in vitro evidence (e.g., activity against *M. leprae* or relevant host pathways)
- Health Canada package insert warnings and contraindications, to enable safety screening
- A review of the interaction profile in the context of standard leprosy regimens
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

