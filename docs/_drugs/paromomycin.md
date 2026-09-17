---
layout: default
title: Paromomycin
parent: Model Prediction Only (L5)
nav_order: 597
evidence_level: L5
indication_count: 8
---

# Paromomycin
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

# Paromomycin: From Intestinal Amebiasis to Idiopathic Copper-Associated Cirrhosis

## One-Sentence Summary

Paromomycin is a non-systemically absorbed aminoglycoside antibiotic; its confirmed Canadian regulatory record is empty (drug not currently marketed, 0 DINs), and detailed mechanism-of-action data is not yet available.
The TxGNN model predicts it may be effective for **idiopathic copper-associated cirrhosis**, but this is currently supported by **0 clinical trials** and **0 publications** — the model itself flags no known pharmacological link to copper metabolism or hepatic fibrosis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented — drug not marketed in Canada, no approved indication text on file |
| Predicted New Indication | Idiopathic copper-associated cirrhosis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed (Not marketed) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank query pending — see data gap DG002). Based on other information in this evidence pack, paromomycin is a non-systemically absorbed aminoglycoside antibiotic; elsewhere in this same evidence set it is described as the standard treatment for intestinal amebiasis and is also used to reduce ammonia-producing gut flora in hepatic encephalopathy, and as an antileishmanial agent.

For the top-ranked prediction, idiopathic copper-associated cirrhosis, the evidence pack's own rationale is explicit: *"與銅代謝或肝纖維化無已知藥理連結，無臨床或文獻證據，屬模型純預測結果"* — there is no known pharmacological connection between paromomycin and copper metabolism or hepatic fibrosis, and no clinical or literature evidence exists. This is a pure knowledge-graph link prediction rather than a mechanistically grounded hypothesis.

Notably, a lower-ranked prediction in this same pack (rank 8, peritonitis) does have a plausible indirect mechanistic story — paromomycin treats intestinal amebiasis, and untreated amebiasis can progress to amebic peritonitis — and is backed by 20 literature references, though relevance of those references is still marked "pending" review. That candidate carries a higher internal evidence grade (L4/S1) than the top-ranked candidate reported here.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is evidence level L5 — a knowledge-graph model output with no supporting clinical trials, no supporting literature, and no identified mechanistic link to copper metabolism or hepatic fibrosis. There is no basis to advance it beyond hypothesis generation at this time.

**To proceed, the following is needed:**
- Health Canada/TFDA package insert data on warnings and contraindications (Blocking data gap, DG001)
- Confirmed mechanism of action from DrugBank (High-priority data gap, DG002)
- Preclinical or mechanistic studies specifically linking aminoglycosides to copper metabolism or hepatic fibrosis pathways
- If pursuing paromomycin repurposing more broadly, consider prioritizing the peritonitis signal (rank 8 in this pack, L4/S1, "Research Question"), which has an indirect mechanistic rationale via intestinal amebiasis and 20 associated publications, over this top-ranked but mechanistically unsupported candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

