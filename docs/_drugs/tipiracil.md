---
layout: default
title: Tipiracil
parent: Model Prediction Only (L5)
nav_order: 777
evidence_level: L5
indication_count: 10
---

# Tipiracil
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

# Tipiracil: From Metastatic Colorectal Cancer to Cecum Villous Adenoma

## One-Sentence Summary

Tipiracil has no independent pharmacological activity on its own; combined with trifluridine as TAS-102 (Lonsurf), it is used internationally for refractory metastatic colorectal cancer. The TxGNN model's top prediction for tipiracil is **Cecum Villous Adenoma**, but this candidate currently has **no supporting clinical trials or literature**, and the evidence pack itself flags the mechanistic link as weak, since villous adenoma is a benign lesion rather than a typical chemotherapy target.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established in Canadian regulatory filings (drug not marketed); internationally, tipiracil is used only as a component of trifluridine/tipiracil (TAS-102/Lonsurf) for metastatic colorectal cancer |
| Predicted New Indication | Cecum Villous Adenoma |
| TxGNN Prediction Score | 99.99% (rank 458) |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Tipiracil itself has no independent pharmacological activity. It must be combined with trifluridine to form TAS-102, in which tipiracil inhibits thymidine phosphorylase, preventing degradation of trifluridine and allowing it to be incorporated into DNA to exert a cytotoxic effect. TAS-102 is used internationally for refractory metastatic colorectal cancer, a proliferative malignant disease driven by DNA replication.

The predicted new indication, cecum villous adenoma, is anatomically located in the colon — the same organ system as the approved indication — but is a benign glandular polypoid lesion rather than an actively proliferating malignancy. Benign lesions are not standard targets of cytotoxic antimetabolite chemotherapy, since TAS-102's mechanism depends on incorporation into rapidly dividing malignant cell DNA.

Per the evidence pack's own mechanistic assessment, this prediction most likely reflects TxGNN's knowledge-graph proximity between "colonic lesions" in general, rather than a genuine pharmacological rationale. No clinical trial or literature evidence directly supports this specific indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Cytotoxicity

Tipiracil (as part of trifluridine/tipiracil, TAS-102) is an antineoplastic cytotoxic agent used in refractory metastatic colorectal cancer, meeting antineoplastic classification criteria (mechanism of action, indication, and drug class).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — nucleoside antimetabolite (trifluridine/tipiracil, TAS-102) |
| Myelosuppression Risk | High — reported adverse effects include leukopenia and neutropenia (PMID 30677817) |
| Emetogenicity Classification | Moderate — vomiting reported as a common adverse effect (PMID 30677817) |
| Monitoring Items | CBC with differential (leukopenia/neutropenia surveillance), liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

**Reported Adverse Event Signal**: A published case report (PMID 30677817) describes trifluridine/tipiracil-induced leukocytoclastic vasculitis with late-onset Henoch-Schönlein purpura, in addition to labeled effects of leukopenia, neutropenia, fatigue, diarrhea, and vomiting.

Formal key warnings, contraindications, and drug-drug interaction data are not currently available in this evidence pack (flagged as a Blocking data gap — TFDA/Health Canada label not yet retrieved); please refer to the official product label once available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (cecum villous adenoma) is supported only by a TxGNN score (L5, decision stage S0), with no clinical trial or literature evidence, and the mechanistic assessment itself flags it as a likely false positive due to poor biological plausibility (benign lesion vs. a cytotoxic antimetabolite mechanism targeting proliferating malignant DNA).
- Across all 10 predicted candidates for tipiracil, only rank 6 ("cecal disease") reaches L4/S1 with literature support — but those 4 publications describe TAS-102 use in already-approved metastatic colorectal cancer, not a novel indication, and may be worth tracking separately as a "Research Question" rather than as new evidence for this candidate.

**To proceed, the following is needed:**
- TFDA/Health Canada product label (warnings, contraindications) — currently Blocking gap
- Formal DrugBank-sourced MOA confirmation
- Any prospective clinical or preclinical evidence specifically addressing cecum villous adenoma (none currently exists)
- If pursuing repurposing research further, consider re-scoping toward mCRC-adjacent colonic malignancies rather than benign lesions, given the drug's cytotoxic antimetabolite mechanism
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

