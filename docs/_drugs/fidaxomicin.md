---
layout: default
title: Fidaxomicin
parent: Model Prediction Only (L5)
nav_order: 383
evidence_level: L5
indication_count: 10
---

# Fidaxomicin
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

# Fidaxomicin: From *Clostridioides difficile* Infection to Staphylococcal Scalded Skin Syndrome

## One-Sentence Summary

Fidaxomicin is an oral macrocyclic antibiotic, known for treating *Clostridioides difficile* infection, and marketed in Canada as DIFICID.
The TxGNN model predicts it may be effective for **staphylococcal scalded skin syndrome (SSSS)**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The score reflects proximity in the knowledge graph rather than pharmacological plausibility, so this is a hypothesis only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian licence data; fidaxomicin is generally known as a treatment for *C. difficile* infection |
| Predicted New Indication | Staphylococcal scalded skin syndrome |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Based on general knowledge, fidaxomicin is a narrow-spectrum macrocyclic inhibitor of bacterial RNA polymerase. It is active mainly against *Clostridium* species and has some in vitro activity against *Staphylococcus aureus*. This in vitro activity is the only mechanistic bridge to SSSS, which is caused by *S. aureus* toxins.

The link is weak, for two reasons:

- **Minimal absorption:** Oral fidaxomicin is barely absorbed, so systemic exposure is negligible. SSSS is a toxin-mediated systemic disease that needs drug levels in blood and skin tissue.
- **Graph proximity is not pharmacology:** The high TxGNN score most likely reflects how close the drug and disease sit in the knowledge graph, not a demonstrated therapeutic rationale.

No route-compatibility or similarity analysis has been completed yet.

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
| 2387174 | DIFICID |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on model output. There are no trials or literature, and the mechanistic link is weak because oral fidaxomicin is minimally absorbed and SSSS needs systemic and tissue drug levels.

**To proceed, the following is needed:**
- The Health Canada package insert, including approved indication, warnings and contraindications (a blocking gap for safety screening)
- Verified mechanism of action data from DrugBank
- Evidence of drug exposure at the site of disease, or a feasible alternative route or formulation
- Any in vitro or preclinical data on fidaxomicin against toxin-producing *S. aureus* strains

Other skin-infection predictions for this drug (bullous impetigo and impetigo) are flagged as research questions, but they face the same absorption and formulation limits.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

