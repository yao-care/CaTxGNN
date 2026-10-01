---
layout: default
title: Emicizumab
parent: Model Prediction Only (L5)
nav_order: 323
evidence_level: L5
indication_count: 10
---

# Emicizumab
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

# Emicizumab: From Congenital Hemophilia A to Pseudo-von Willebrand Disease

## One-Sentence Summary

Emicizumab is a bispecific antibody approved for congenital hemophilia A, where it prevents bleeding by replacing the missing function of activated factor VIII.
The TxGNN model predicts it may be effective for **pseudo-von Willebrand disease** (platelet-type von Willebrand disease), but there are **0 clinical trials** and **0 publications** supporting this direction, and the mechanism does not fit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Congenital hemophilia A (from the literature in the evidence pack; the Canadian licence records list no indication text) |
| Predicted New Indication | Pseudo-von Willebrand disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the evidence pack. Emicizumab is a bispecific antibody that bridges factor IXa and factor X, taking over the role of activated factor VIII in the intrinsic tenase complex. Because it is not neutralized by anti-FVIII antibodies, it works in hemophilia A with or without inhibitors.

The prediction is **not well supported mechanistically**. Platelet-type von Willebrand disease is caused by a gain-of-function defect in platelet GPIb-alpha. This increases VWF binding and leads to platelet clearance. Emicizumab does not act on this pathway, so it would not be expected to correct the underlying problem.

The very high score (99.99%) probably reflects proximity between the two conditions in the knowledge graph, since both are bleeding disorders. It should not be read as evidence of a therapeutic relationship.

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
| 2479621 | HEMLIBRA |
| 2479648 | HEMLIBRA |
| 2479656 | HEMLIBRA |
| 2479664 | HEMLIBRA |

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the database. However, the evidence pack flags that emicizumab combined with bypassing agents (activated prothrombin complex concentrate, aPCC, or FVIIa) increases the risk of thrombotic events and thrombotic microangiopathy.

For other safety information, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone, with no clinical trials or publications, and the drug's mechanism does not address the platelet GPIb-alpha defect behind this disease.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Detailed mechanism-of-action data from DrugBank
- Any mechanistic or preclinical evidence linking emicizumab to platelet-type von Willebrand disease. Without it, this candidate should not advance.

**Other candidates in the same evidence pack:**
- **Acquired coagulation factor deficiency (rank 5)** is the only candidate with substantial support, at evidence level L2 (Proceed with Guardrails).
  - Two prospective single-arm studies in acquired hemophilia A show benefit: the phase III AGEHA study and the phase 2 GTH-AHA-EMI study. Consensus recommendations and real-world cohorts point the same way.
  - No randomized trial exists, and the evidence covers acquired hemophilia A only, not other acquired factor deficiencies.
  - This candidate is the better one to evaluate first.
- **Thrombotic thrombocytopenic purpura (rank 8)** should not be pursued. Emicizumab is pro-hemostatic and has been associated with thrombotic microangiopathy, so the predicted link is biologically implausible and potentially hazardous.
- **"Flood factor deficiency" (rank 10)** may be a data or ontology artifact, and the term needs validation before any assessment.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

