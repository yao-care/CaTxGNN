---
layout: default
title: Spironolactone
parent: Model Prediction Only (L5)
nav_order: 861
evidence_level: L5
indication_count: 2
---

# Spironolactone
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

# Spironolactone: From Aldosterone-Antagonist Therapy to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Spironolactone is a marketed drug in Canada, and the Canadian licence records supplied do not state its approved indication. The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**, but **no clinical trials and no publications** currently support this prediction, which rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied Canadian licence records |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Spironolactone is generally known as a mineralocorticoid receptor antagonist with anti-androgen activity. It is used off-label for androgen-mediated hair loss such as female pattern hair loss. This background is general pharmacology, not something confirmed by the supplied data.

Hypotrichosis simplex of the scalp is a rare hereditary hair-loss disorder linked to genes such as CDSN, APCDD1 and SNRPE. It is not primarily androgen-driven, so any mechanistic link to an anti-androgen is speculative and unverified. The high graph score may reflect general hair-loss associations in the knowledge graph rather than disease-specific biology.

The model also ranks a second, related condition, **congenital hypotrichosis milia** (score 99.04%). It likewise has no supporting trials or literature, and no established connection to spironolactone's anti-androgen activity. That prediction probably reflects network proximity to other hypotrichosis phenotypes.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Ten authorisations are on record. Dosage form, manufacturer and approved-indication text were not provided for any of them. Five are listed below.

| DIN | Product Name |
|---------|------|
| 2518821 | JAMP SPIRONOLACTONE |
| 613223 | TEVA-SPIRONOLACTONE |
| 2488159 | MINT-SPIRONOLACTONE |
| 613215 | TEVA-SPIRONOLACTONE |
| 2518848 | JAMP SPIRONOLACTONE |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high model score. There are no clinical trials or publications, and the plausible mechanism (anti-androgen) does not fit a hereditary, non-androgen-driven hair disorder. The Health Canada safety data is also missing.

**To proceed, the following is needed:**
- Health Canada product monograph (warnings, contraindications, approved indications), which is a blocking gap for safety screening
- Mechanism of action data from DrugBank
- A targeted literature and trial search on spironolactone in hereditary hypotrichosis
- A review of whether the disease genes (CDSN, APCDD1, SNRPE) have any pharmacological link to mineralocorticoid or androgen receptor signalling
- Route compatibility assessment, since only the oral route is evident and scalp conditions may call for topical delivery

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

