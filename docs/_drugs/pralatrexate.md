---
layout: default
title: Pralatrexate
parent: Model Prediction Only (L5)
nav_order: 752
evidence_level: L5
indication_count: 10
---

# Pralatrexate
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

# Pralatrexate: From an Approved Antifolate Chemotherapy to Pleural Adenomatoid Tumor

## One-Sentence Summary

Pralatrexate is a cytotoxic antifolate that is marketed in Canada as FOLOTYN. The license record supplied does not state its approved indication.
The TxGNN model predicts it may be effective for **pleural adenomatoid tumor**, but **0 clinical trials** and **0 publications** currently support this specific prediction.
It is a model-only prediction, and the high score most likely reflects the drug's proximity to mesothelioma in the knowledge graph.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the supplied license record |
| Predicted New Indication | Pleural adenomatoid tumor |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Pralatrexate is a folate analog that inhibits dihydrofolate reductase (DHFR) and is taken up into cells through the reduced folate carrier RFC-1. It is a cytotoxic, antiproliferative agent.

Adenomatoid tumors are generally benign lesions of mesothelial origin, so a cytotoxic antifolate has no clear rationale for them. The high score most likely reflects the drug's closeness to mesothelioma in the knowledge graph rather than a true treatment signal. The pack contains no pralatrexate-specific clinical or preclinical data for this condition. I therefore consider the prediction weak and a low priority for follow-up.

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
| 2481820 | FOLOTYN | Not recorded | Not recorded |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antifolate class) |
| Myelosuppression Risk | High (significant myelosuppression noted alongside mucositis) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Haematological parameters (CBC with differential); please also refer to the package insert warnings and precautions |
| Handling Protection | Follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is model prediction only (L5). The condition is typically benign, so the benefit-risk balance of a cytotoxic drug with significant mucositis and myelosuppression is unfavorable without supporting data.

Among the other predicted indications in this pack, **pleural mesothelioma** and **pleural epithelioid mesothelioma** are better supported. Each rests on a single-arm Phase 2 trial (PMID 17409804) and is rated L3 (Research Question). Those candidates deserve attention before this one.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are blocking for safety screening
- Mechanism of action data, for example from the DrugBank API
- Any pralatrexate-specific evidence for adenomatoid tumor, and a clinical rationale for systemic cytotoxic therapy in a generally benign lesion
- Full-text review of the Phase 2 mesothelioma trial, to redirect effort toward the better-supported mesothelioma candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

