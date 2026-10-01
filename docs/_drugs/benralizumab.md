---
layout: default
title: Benralizumab
parent: Model Prediction Only (L5)
nav_order: 101
evidence_level: L5
indication_count: 10
---

# Benralizumab
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

# Benralizumab: From Eosinophilic Airway Disease to Thrombocytopenia Due to Immune Destruction

## One-Sentence Summary

Benralizumab is an anti-IL-5Rα antibody that depletes eosinophils, and its established use is in eosinophilic airway disease.
The TxGNN model predicts it may be effective for **thrombocytopenia due to immune destruction**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Eosinophilic airway disease (the licence records contain no indication text; this comes from the mechanistic notes) |
| Predicted New Indication | Thrombocytopenia due to immune destruction |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Benralizumab binds the IL-5 receptor alpha chain and depletes eosinophils and basophils through antibody-dependent cellular cytotoxicity (ADCC). Its established role is in eosinophil-driven airway disease.

The link to the predicted indication is weak. Immune thrombocytopenia is driven mainly by anti-platelet autoantibodies, Fc-receptor-mediated platelet clearance and impaired megakaryopoiesis. There is no clear eosinophil-dependent pathway. The high TxGNN score is a graph-based computational prediction only, and no trials or literature were provided to support it.

Two other predictions in the same list, autoimmune thrombocytopenic and Evans syndrome, share the same autoantibody-driven biology. "Autoimmune thrombocytopenic" may be a duplicate of the same disease concept as the top prediction.

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
| 2496135 | FASENRA PEN |
| 2473232 | FASENRA |

Dosage form and approved indication text are not available in the licence records.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials or literature. The mechanism (eosinophil depletion) does not fit the autoantibody-mediated pathology of immune thrombocytopenia.

**To proceed, the following is needed:**
- A systematic search of trial registries and PubMed for benralizumab in immune thrombocytopenia, autoimmune thrombocytopenia and Evans syndrome
- Health Canada package insert warnings and contraindications for a safety screen
- Approved indication text and dosage forms for the two DINs
- Confirmation of whether the thrombocytopenia entries are duplicates
- Detailed mechanism of action data from DrugBank
- A separate endotype-specific literature search for the dermatitis prediction (rank 2, flagged as a research question)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

