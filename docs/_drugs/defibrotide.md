---
layout: default
title: Defibrotide
parent: Model Prediction Only (L5)
nav_order: 255
evidence_level: L5
indication_count: 10
---

# Defibrotide
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

# Defibrotide: From Hepatic Veno-Occlusive Disease to Pseudo-von Willebrand Disease

## One-Sentence Summary

Defibrotide is an endothelial-protective, profibrinolytic, antithrombotic oligonucleotide, marketed in Canada as DEFITELIO. The TxGNN model predicts it may be effective for **pseudo-von Willebrand disease** with a very high score, but **0 clinical trials** and **0 publications** support this prediction. Because the mechanism points in the opposite direction from what this bleeding disorder needs, the recommendation is **Hold**.

*Note: The Evidence Pack has no approved-indication text for the Canadian licence. Hepatic veno-occlusive disease is used as the original indication based on general knowledge of the drug and on the linked prevention trial for that condition.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hepatic veno-occlusive disease (not stated in the Evidence Pack; see note above) |
| Predicted New Indication | Pseudo-von Willebrand disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Defibrotide is generally described as an endothelial-protective agent with profibrinolytic and antithrombotic activity. Its effects include increased t-PA activity and reduced PAI-1.

The prediction is not mechanistically convincing. Pseudo-von Willebrand disease is a bleeding disorder caused by a platelet GPIb gain-of-function defect. A drug that promotes fibrinolysis and inhibits thrombosis has no plausible therapeutic rationale here and could worsen bleeding. The high TxGNN score most likely reflects network-level associations in the knowledge graph rather than a real biological link. No supporting clinical or literature evidence was found.

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
| 2465981 | DEFITELIO |

---

## Safety Considerations

- **Bleeding risk**: Defibrotide's antithrombotic and profibrinolytic activity raises a bleeding-risk concern in a disorder that is already characterised by bleeding.

Please refer to the package insert for full warnings, contraindications and drug interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone. Defibrotide's mechanism is opposed to the clinical need in pseudo-von Willebrand disease, and no trials or publications support the link.

**Other candidates in the same prediction set:**
- **Thrombotic thrombocytopenic purpura (rank 4)** is the only candidate with meaningful literature. It has small case series and reports from 1984–2002 and reviews of transplant-associated thrombotic microangiopathy, so the evidence level is L3. There is no RCT. One report describes TTP occurring after defibrotide therapy, which is a safety signal. This is a Research Question, not a recommendation.
- **Primary release disorder of platelets (rank 2)** is linked to NCT02851407, a Phase 3 trial (n=372, completed) of hepatic VOD prevention after stem cell transplant. This trial does not study the predicted disease and is likely a spurious match.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications
- Mechanism of action data from DrugBank
- For TTP or transplant-associated TMA: a prospective study with safety monitoring, positioned only for refractory cases beyond standard care (plasma exchange, caplacizumab, rituximab)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

