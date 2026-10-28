---
layout: default
title: Danaparoid
parent: Model Prediction Only (L5)
nav_order: 245
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-28
description: "Danaparoid: predicted new indication Glanzmann thrombasthenia (evidence level L5). Approved use: Not available in the data compiled for this report (anticoagulant hep…"
monitor_inn: "Danaparoid"
predicted_indications: ["Glanzmann thrombasthenia", "primary release disorder of platelets", "pseudo-von Willebrand disease", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "Scott syndrome"]
---

# Danaparoid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Danaparoid: From Anticoagulation to Glanzmann Thrombasthenia (Prediction Not Supported)
{: .text-alpha }

## One-Sentence Summary

Danaparoid (marketed in Canada as ORGARAN) is a heparinoid anticoagulant. The TxGNN model predicts it may be effective for **Glanzmann thrombasthenia**, a bleeding disorder, but there are **0 clinical trials** and **0 publications** supporting this. The prediction conflicts with the drug's pharmacology and is most likely a computational artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (anticoagulant heparinoid) |
| Predicted New Indication | Glanzmann thrombasthenia |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, danaparoid is an anticoagulant heparinoid whose effect comes mainly from anti-Xa activity through potentiation of antithrombin.

Glanzmann thrombasthenia is a bleeding disorder caused by absent or defective platelet integrin alpha-IIb/beta-3. Anticoagulation would be expected to **worsen** the bleeding tendency, not treat it. The high score (0.9988) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other five predicted indications show the same pattern. All are bleeding or platelet-function disorders where an anticoagulant would be counterproductive:

| Predicted Disease | TxGNN Score | Concern |
|------|------|------|
| Primary release disorder of platelets | 0.9988 | Platelet secretion defect; anticoagulant adds bleeding risk |
| Pseudo-von Willebrand disease | 0.9983 | GPIbα gain-of-function; anticoagulation expected to aggravate bleeding |
| Bleeding diathesis due to a collagen receptor defect | 0.9930 | Defect is in collagen-platelet signaling, not the coagulation cascade |
| Hemorrhagic disorder due to constitutional thrombocytopenia | 0.9930 | Danaparoid does not correct platelet count |
| Scott syndrome | 0.9928 | Impaired phosphatidylserine exposure; danaparoid further suppresses coagulation |

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
| 02129043 | ORGARAN | Not specified | Not specified |

---

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 interacting drugs. The entries reviewed include many Major-level interactions, which are consistent with additive bleeding risk:
  - Antiplatelet and NSAID agents: acetylsalicylic acid, ibuprofen, ketorolac, abciximab
  - Thrombolytic: alteplase
  - Other Major-level interactions: deferasirox, acalabrutinib, trastuzumab emtansine, ibritumomab tiuxetan, tositumomab (I-131)
  - Moderate-level examples: celecoxib, amiloride, aliskiren, sugammadex
- **Disease-specific concern**: Because all predicted indications are bleeding disorders, use of danaparoid is potentially contraindicated in these conditions.

Please refer to the package insert for warnings and contraindications, which were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. The drug's anticoagulant action runs opposite to what bleeding disorders require, and no trials or publications support the prediction. The safety risk is also plausible.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data confirmed from DrugBank
- Original approved indication text for ORGARAN
- Any mechanistic or preclinical rationale showing how an anticoagulant could benefit these bleeding disorders. Without it, deprioritising this candidate and reviewing other predictions is advisable.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

