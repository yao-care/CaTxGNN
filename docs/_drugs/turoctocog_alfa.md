---
layout: default
title: Turoctocog Alfa
parent: Model Prediction Only (L5)
nav_order: 948
evidence_level: L5
indication_count: 10
---

# Turoctocog Alfa
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

# Turoctocog Alfa: From Hemophilia A to Primary Release Disorder of Platelets

## One-Sentence Summary

Turoctocog alfa is a recombinant, B-domain truncated factor VIII (FVIII), a replacement therapy for hemophilia A.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but **0 clinical trials** and **0 publications** support this direction.
The score most likely reflects network proximity in the hemostasis knowledge graph rather than a real therapeutic effect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hemophilia A (inferred from the drug class; the licence records list no indication text) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the database. Based on known information, turoctocog alfa replaces missing FVIII in the intrinsic tenase complex. Its efficacy therefore applies to FVIII deficiency, not to platelet disorders.

Primary release disorder of platelets is a defect in platelet granule secretion, not a lack of FVIII. Supplying more FVIII does not correct it, so there is no clear mechanistic rationale. The high score appears to come from the drug and the disease sitting close together in the hemostasis network.

The other top-ranked predictions show the same pattern. Pseudo-von Willebrand disease, Glanzmann thrombasthenia, Scott syndrome, collagen receptor defects and constitutional thrombocytopenia are all platelet-intrinsic or VWF-platelet defects that FVIII replacement does not address. The one biologically plausible candidate is **acquired coagulation factor deficiency** (rank 5), such as acquired hemophilia A. Even there, autoantibody inhibitors would likely neutralize standard recombinant FVIII, and the category is too broad to evaluate as it stands.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

20 authorizations are recorded. The first 5 are shown below. The data do not list dosage form or approved indication text for these entries.

| DIN | Product Name |
|---------|------|
| 2435217 | ZONOVATE |
| 2435187 | ZONOVATE |
| 2435209 | ZONOVATE |
| 2451484 | KOVALTRY |
| 2451476 | KOVALTRY |

## Safety Considerations

Please refer to the package insert for safety information.

One predicted indication raises a specific concern. In thrombotic thrombocytopenic purpura (rank 9), raising FVIII could be pro-thrombotic and harmful, so that prediction should be treated as a likely false positive. The same applies to hereditary thrombocytosis with transverse limb defect (rank 10), where thrombosis, not bleeding, is the clinical risk.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials or publications for any of the 10 predicted indications, and the mechanisms do not support FVIII replacement for platelet-function disorders. The top-ranked prediction is most likely a graph-proximity artifact.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- A specific, well-defined subtype of acquired coagulation factor deficiency (for example, non-inhibitor acquired FVIII deficiency) to pursue as a research question, since it is the only biologically plausible candidate
- Verification of the "flood factor deficiency" concept (rank 8) in the source knowledge graph, since it may be a mapping artifact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

