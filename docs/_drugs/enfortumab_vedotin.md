---
layout: default
title: Enfortumab Vedotin
parent: Model Prediction Only (L5)
nav_order: 327
evidence_level: L5
indication_count: 10
---

# Enfortumab Vedotin
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

# Enfortumab Vedotin: From Urothelial Cancer to Leprosy

## One-Sentence Summary

Enfortumab vedotin is a Nectin-4-directed antibody-drug conjugate (ADC) marketed for urothelial cancer.
The TxGNN model predicts it may be effective for **leprosy**, but **no clinical trials and no publications** support this prediction, and the biology argues against it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urothelial cancer (Canadian licence records list no indication text; this is taken from the drug's known labelling) |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. From general knowledge, enfortumab vedotin is an antibody-drug conjugate. The antibody binds Nectin-4, a protein on the surface of tumour cells. The drug is then taken up and releases MMAE, a payload that disrupts microtubules and kills the cell.

The prediction is **not mechanistically reasonable**. Leprosy is a bacterial infection (*Mycobacterium leprae*), and a cytotoxic anticancer ADC has no known antibacterial activity. The MMAE payload can cause neutropenia and immunosuppression, which could make infections worse. The high score most likely reflects a knowledge-graph artifact rather than a real therapeutic signal.

The other top-ranked predictions have the same problem. They include infections (cytomegalovirus, HIV, candidiasis), metabolic and vascular diseases, and two veterinary diseases (infectious bovine rhinotracheitis and malignant catarrh). The veterinary ones do not apply to human use at all.

The only candidate with an oncology rationale is **HER2-positive breast carcinoma** (rank 10, score 98.99%, evidence level L4). Nectin-4 is expressed in a subset of breast cancers, mainly triple-negative disease. However, the evidence for HER2-positive disease is indirect.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for leprosy.

---

## Literature Evidence

Currently no related literature available for leprosy.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2521903 | PADCEV |
| 2521911 | PADCEV |

Dosage form, manufacturer and approved-indication text are not recorded for these licences.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (antibody-drug conjugate with a microtubule-disrupting MMAE payload) |
| Myelosuppression Risk | Medium (MMAE-related neutropenia is a recognised concern) |
| Emetogenicity Classification | Low (general class knowledge; confirm against the product monograph) |
| Monitoring Items | CBC with differential, liver and renal function, blood glucose, and skin and neuropathy assessments (from general knowledge of the drug; confirm against the monograph) |
| Handling Protection | Follow institutional cytotoxic drug handling procedures |

---

## Safety Considerations

Please refer to the package insert for safety information.

In the leprosy setting specifically, myelosuppression and immunosuppression from the MMAE payload could increase infection risk. A FAERS pharmacovigilance analysis of ADCs in bladder cancer (PMID 41341429) also points to safety signals rather than benefit.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The leprosy prediction rests on the model score alone. No trials or literature support it, and no plausible mechanism links a cytotoxic anticancer ADC to *M. leprae* infection. The expected direction of effect is unfavourable.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A decision on whether to drop the veterinary artifacts (infectious bovine rhinotracheitis, malignant catarrh) from the human candidate list
- If an oncology direction is pursued, re-prioritise **HER2-positive breast carcinoma**. This starts with Nectin-4 expression profiling in HER2-positive breast tumours. The related phase 2 basket study NCT04225117 (EV-202) is non-randomised, and its breast cohorts, as far as I know, are not HER2-positive.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

