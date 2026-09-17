---
layout: default
title: Trimethoprim
parent: Model Prediction Only (L5)
nav_order: 805
evidence_level: L5
indication_count: 2
---

# Trimethoprim
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Trimethoprim: From Antibacterial Therapy to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Trimethoprim is a broad-spectrum antibacterial agent (dihydrofolate reductase inhibitor); no specific original approved indication is on file in this evidence pack.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**,
but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-score-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication text on file; drug not marketed in Canada) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on other information in the pack (drawn from the drug's alternate predicted indication, conjunctivitis), trimethoprim is known to act as a dihydrofolate reductase inhibitor with broad-spectrum antibacterial activity.

Punctate epithelial keratoconjunctivitis, however, is most commonly caused by viral pathogens (e.g., adenovirus), not bacteria. Since trimethoprim is an antibacterial — not antiviral — agent, the mechanistic link to this specific indication is weak. It could theoretically play only an adjunctive role in cases where a bacterial co-infection is present, but no clinical trial or literature evidence currently supports this. This prediction rests solely on the TxGNN model score, with no independent corroboration.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Trimethoprim currently has no market authorizations (DINs) on file in this evidence pack; the product is listed as **not marketed** in Canada.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5-level prediction (model score only) with no clinical trials or literature evidence, and the underlying mechanistic rationale is weak given the largely viral etiology of the target condition. There is insufficient basis to advance this candidate at this time.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank
- Health Canada / TFDA-equivalent label warnings and contraindications (currently a blocking data gap for safety review)
- Preclinical or clinical evidence specifically linking trimethoprim to punctate epithelial keratoconjunctivitis, or evidence of efficacy in bacterial co-infection subtypes
- Confirmation of route compatibility (ophthalmic formulation availability)

---

**Additional Note:** This evidence pack contains a second predicted indication for trimethoprim — **conjunctivitis** (TxGNN score 99.17%) — which is substantially better supported: L1 evidence level, 3 clinical trials (including a Phase 4 head-to-head RCT of a marketed trimethoprim/polymyxin B ophthalmic product vs. moxifloxacin for bacterial conjunctivitis), 20 literature entries, and a "Proceed with Guardrails" recommendation. Given the marked contrast in evidence strength, this second candidate warrants prioritized review as a stronger repurposing opportunity for trimethoprim.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

