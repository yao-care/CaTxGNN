---
layout: default
title: Moroctocog Alfa
parent: Model Prediction Only (L5)
nav_order: 626
evidence_level: L5
indication_count: 8
---

# Moroctocog Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Moroctocog Alfa: From Hemophilia A to Primary Release Disorder of Platelets

## One-Sentence Summary

Moroctocog alfa is a B-domain-deleted recombinant factor VIII (marketed as XYNTHA), a coagulation factor replacement product. The license records in the Evidence Pack do not state the approved indication, so hemophilia A is inferred from the product class.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but only **6 loosely matched clinical trials** (all graded C, none testing this drug in this disease) and **0 publications** are linked, so the prediction is essentially model-only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hemophilia A (inferred from product class; not stated in license records) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Based on known information, moroctocog alfa is a recombinant factor VIII that replaces a missing plasma coagulation factor. Its efficacy in hemophilia A is established, but that mechanism does not carry over to the predicted indication.

Primary release disorders of platelets are defects in platelet granule secretion, with normal FVIII activity. Supplying more FVIII does not correct a platelet function defect, so there is no plausible mechanistic link. The very high TxGNN score most likely reflects proximity in the knowledge graph through shared hemostasis nodes, not a therapeutic relationship.

The other predicted indications show the same pattern. Most are platelet or membrane defects (pseudo-von Willebrand disease, Glanzmann thrombasthenia, Scott syndrome, collagen receptor defect, constitutional thrombocytopenia) that FVIII replacement does not address. One is an unverifiable term ("flood factor deficiency") that needs ontology review. The only more plausible candidate is **acquired hemophilia A** within acquired coagulation factor deficiency (rank 4, L4). Human rFVIII is usually neutralized by the inhibitory autoantibodies there, so bypassing agents or porcine FVIII are used instead.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04759131](https://clinicaltrials.gov/study/NCT04759131) | Phase 3 | Completed | 74 | Safety and efficacy of rFVIIIFc-VWF-XTEN (BIVV001) in children under 12 with severe hemophilia A. Not a platelet disorder population. |
| [NCT04161495](https://clinicaltrials.gov/study/NCT04161495) | Phase 3 | Completed | 159 | BIVV001 prophylaxis in patients 12 and older with severe hemophilia A. No direct evidence for the predicted indication. |
| [NCT01913405](https://clinicaltrials.gov/study/NCT01913405) | Phase 3 | Completed | 30 | PEGylated rFVIII (BAX 855) in hemophilia A patients undergoing surgery. Different product and disease. |
| [NCT07329036](https://clinicaltrials.gov/study/NCT07329036) | Not applicable | Recruiting | 25 | Artificial liver support (DPMAS plus plasma exchange) in acute-on-chronic liver failure, with effects on primary coagulation. Unrelated. |
| [NCT07400848](https://clinicaltrials.gov/study/NCT07400848) | Not applicable | Recruiting | 200 | Laboratory and symptom study in post-COVID-19-vaccination syndrome. Unrelated. |
| [NCT07343687](https://clinicaltrials.gov/study/NCT07343687) | Not applicable | Not yet recruiting | 80 | Observational coagulation profiling in newly diagnosed AML. Does not test moroctocog alfa. |

All six trials were graded C for relevance. The registry matches appear to be keyword-driven. NCT07439939 (hemostasis exploration in TIPS patients, observational) is also linked but unrelated.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Six licenses are recorded, and five are listed below. Dosage form and approved indication text were not provided in the records.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2374072 | XYNTHA SOLOFUSE | — | — |
| 2309491 | XYNTHA | — | — |
| 2309483 | XYNTHA | — | — |
| 2374099 | XYNTHA SOLOFUSE | — | — |
| 2374080 | XYNTHA SOLOFUSE | — | — |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a graph-proximity signal alone. There is no mechanistic plausibility, no relevant clinical trial and no literature for primary release disorder of platelets, so the evidence level is L5.

**To proceed, the following is needed:**
- Pull the Health Canada package insert (warnings, contraindications and approved indications) to complete safety screening.
- Obtain mechanism of action data from DrugBank to support any mechanistic analysis.
- Redirect attention to **acquired hemophilia A** (rank 4, L4, Research Question). It is the only more plausible candidate, but the support is indirect (other FVIII-class products such as porcine rFVIII) and inhibitor neutralization of human rFVIII is a major limitation.
- Review the ontology for "flood factor deficiency" before any assessment.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

