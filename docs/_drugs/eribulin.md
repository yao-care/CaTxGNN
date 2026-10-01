---
layout: default
title: Eribulin
parent: Model Prediction Only (L5)
nav_order: 342
evidence_level: L5
indication_count: 10
---

# Eribulin
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

# Eribulin: From an Unrecorded Original Indication to Autosomal Recessive Familial Mediterranean Fever

## One-Sentence Summary

Eribulin is a cytotoxic microtubule-dynamics inhibitor marketed in Canada, but the supplied Health Canada records do not state its approved indication.
The TxGNN model's top-ranked prediction is **autosomal recessive familial Mediterranean fever (FMF)**, with **0 clinical trials** and **0 publications** supporting it. This looks like a knowledge-graph artifact rather than a real therapeutic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (Health Canada indication text is empty) |
| Predicted New Indication | Autosomal recessive familial Mediterranean fever |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, eribulin is a cytotoxic antimitotic agent that inhibits microtubule dynamics.

This prediction is **not well supported**. FMF is an autoinflammatory disease driven by dysregulation of the MEFV/pyrin inflammasome and is treated with colchicine. Eribulin has no recognised link to this pathway, and its significant myelosuppression and neuropathy risks make it a poor fit for a non-malignant inflammatory disease. The very high TxGNN score most likely reflects shared microtubule-related nodes in the knowledge graph, not a therapeutic signal.

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
| 2539136 | NAT-ERIBULIN |
| 2545950 | ERIBULIN MESYLATE INJECTION |
| 2377438 | HALAVEN |

Dosage form, manufacturer and approved indication text were not supplied for these products.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antimitotic, microtubule-dynamics inhibitor) |
| Myelosuppression Risk | High (significant myelosuppression is noted for this drug) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential; peripheral neuropathy assessment; other items per package insert |
| Handling Protection | Must follow cytotoxic drug handling regulations |

Neuropathy is also a notable risk.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the supplied data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The FMF prediction has no supporting trials or literature and no credible mechanistic link. The toxicity profile of eribulin also argues against use in a non-malignant autoinflammatory disease.

**Other candidates in the same prediction set:**
- **Fibroblastic neoplasm (TxGNN rank 8)** has the strongest evidence. It has a completed Phase 2 trial of eribulin in advanced solitary fibrous tumor ([NCT03840772](https://clinicaltrials.gov/study/NCT03840772), n=16, no results supplied), plus preclinical fibrosarcoma data.
- **Ovarian myxoid liposarcoma** would be an extrapolation from liposarcoma.
- **Dermatofibrosarcoma protuberans** is supported only by a general soft tissue sarcoma review ([27434055](https://pubmed.ncbi.nlm.nih.gov/27434055/)).
- **Mesothelioma subtypes, pleural adenomatoid tumor and heart fibrosarcoma** have no supporting evidence.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications and approved indications, which is a blocking gap for safety screening
- Mechanism of action data from DrugBank
- The published results of the ERASING trial, and a check of primary sources for the sarcoma-related candidates
- Any further work on FMF should be deprioritised unless new mechanistic evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

