---
layout: default
title: Latanoprostene Bunod
parent: Model Prediction Only (L5)
nav_order: 448
evidence_level: L5
indication_count: 10
---

# Latanoprostene Bunod
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

# Latanoprostene Bunod: From Glaucoma/Ocular Hypertension to Visceral Calciphylaxis

## One-Sentence Summary

Latanoprostene bunod is a nitric oxide (NO)-donating prostaglandin analog used internationally to lower intraocular pressure in open-angle glaucoma and ocular hypertension. The TxGNN model's top-ranked prediction points to **Visceral Calciphylaxis**, but this signal is currently backed by **0 clinical trials** and **0 publications**, and the model itself flags no plausible mechanistic link. This candidate should be treated as speculative pending further evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not marketed in Canada; internationally indicated for Open-Angle Glaucoma / Ocular Hypertension |
| Predicted New Indication | Visceral Calciphylaxis |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed (Not Marketed) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA field returned a data gap). Based on known information, latanoprostene bunod is a nitric oxide-donating prostaglandin F2α analog: after ocular application it is metabolized to latanoprost acid (which increases uveoscleral outflow to lower intraocular pressure) and butanediol mononitrate (a NO donor that relaxes trabecular meshwork/Schlemm's canal tissue). Its established use is confined to intraocular pressure reduction in open-angle glaucoma and ocular hypertension.

Visceral calciphylaxis, by contrast, is a disorder driven by vascular medial calcification and microthrombosis, typically in the setting of end-stage renal disease and dysregulated calcium-phosphate metabolism. The evidence pack's own rationale for this candidate is explicit that there is **no direct or indirect mechanistic support**: the known pharmacologic targets of latanoprostene bunod (prostaglandin FP receptors and NO-mediated vascular smooth muscle relaxation in ocular tissue) have no established connection to the vascular calcification and microthrombotic pathology that defines calciphylaxis. This ranking therefore reflects a TxGNN network-embedding score only, with no corroborating clinical or mechanistic evidence.

Notably, other TxGNN-ranked candidates in this evidence pack are mechanistically more coherent — rank 2 (primary hereditary glaucoma) aligns directly with the drug's approved IOP-lowering action, and rank 6 (vascular disease) has supporting Phase 4 human trial data on NO-mediated microvascular blood flow. These may merit separate, dedicated evaluation outside the scope of this report's top-ranked candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Canada Market Information

This drug is not currently authorized for sale in Canada — market status is "Not marketed" (not marketed) with 0 DINs on record. No product licenses are available to summarize.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (visceral calciphylaxis) has no supporting clinical trials or literature, and the mechanistic rationale explicitly finds no plausible link between the drug's known ocular NO-PGF2α activity and calciphylaxis pathophysiology. This is an L5, TxGNN-score-only signal and does not meet the threshold to advance.

**To proceed, the following is needed:**
- Detailed mechanism of action data from DrugBank (DG002)
- TFDA/product monograph warnings and contraindications (DG001 — currently blocking safety evaluation)
- Direct clinical or preclinical evidence specifically linking latanoprostene bunod (or NO-donor/prostaglandin agents generally) to vascular calcification disorders
- If pursuing a repurposing signal for this drug, consider prioritizing rank 2 (primary hereditary glaucoma) or rank 6 (vascular disease) instead, given their stronger mechanistic and/or clinical evidence base
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

