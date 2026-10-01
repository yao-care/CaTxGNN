---
layout: default
title: Danaparoid
parent: Model Prediction Only (L5)
nav_order: 243
evidence_level: L5
indication_count: 6
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Danaparoid: From Anticoagulation to Glanzmann Thrombasthenia

## One-Sentence Summary

Danaparoid is a heparinoid anticoagulant, marketed in Canada as ORGARAN.
The TxGNN model predicts it may be relevant to **Glanzmann thrombasthenia**, an inherited platelet bleeding disorder, but **0 clinical trials** and **0 publications** support this.
The prediction looks biologically implausible and may reflect a contraindication signal rather than a therapeutic opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anticoagulation (heparinoid anticoagulant; no approved indication text in the Canadian record) |
| Predicted New Indication | Glanzmann thrombasthenia |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source record. Danaparoid is a heparinoid that acts through antithrombin-mediated anti-Xa activity, which suppresses thrombin generation and reduces clotting.

Glanzmann thrombasthenia is an inherited bleeding disorder caused by defective platelet integrin alphaIIb-beta3. Patients bleed too easily, so an anticoagulant would be expected to worsen the condition. The high score most likely reflects proximity in the knowledge graph through shared coagulation and platelet nodes, not a therapeutic link.

The other five predictions are all platelet or bleeding disorders and have the same problem:

- Primary release disorder of platelets (99.88%)
- Pseudo-von Willebrand disease (99.83%)
- Bleeding diathesis due to a collagen receptor defect (99.30%)
- Hemorrhagic disorder due to constitutional thrombocytopenia (99.30%)
- Scott syndrome (99.28%)

None has any trial or literature support. In each case the anticoagulant effect runs opposite to the clinical need, so these predictions should be treated as possible safety warnings.

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
| 2129043 | ORGARAN |

---

## Safety Considerations

No drug interactions were found in the queried data.

Please refer to the package insert for safety information. Because the predicted indications are bleeding disorders, a heparinoid anticoagulant could increase bleeding risk in these patients.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no trials or literature (L5). The mechanism points in the opposite direction from the disease, since an anticoagulant would likely aggravate bleeding. Treat the result as a graph-proximity artifact or a possible contraindication signal, not a repurposing candidate.

**To proceed, the following is needed:**
- The Health Canada package insert warnings and contraindications
- Confirmed mechanism-of-action data from DrugBank
- Any preclinical or clinical evidence showing a plausible benefit in platelet function disorders
- A review of whether the predictions should be reclassified as safety signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

