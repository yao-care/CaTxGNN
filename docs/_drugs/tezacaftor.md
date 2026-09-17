---
layout: default
title: Tezacaftor
parent: Model Prediction Only (L5)
nav_order: 767
evidence_level: L5
indication_count: 10
---

# Tezacaftor
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

# Tezacaftor: From Cystic Fibrosis to HIV Infectious Disease

## One-Sentence Summary

Tezacaftor is a CFTR corrector originally developed for cystic fibrosis caused by specific CFTR mutations (e.g., F508del), typically used in combination with other CFTR modulators.
The TxGNN model predicts a possible association with **HIV Infectious Disease**,
but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack itself flags it as likely knowledge-graph noise.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cystic Fibrosis (CFTR mutation-associated) — formal regulatory indication text not available for this drug in the source data |
| Predicted New Indication | HIV Infectious Disease |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Tezacaftor is not available in this evidence pack. Based on known drug class information referenced in the accompanying rationale, Tezacaftor is a CFTR corrector, used as part of combination CFTR-modulator therapy (e.g., with ivacaftor) to correct protein folding defects in cystic fibrosis patients carrying mutations such as F508del.

There is no established biological pathway connecting CFTR protein folding correction to HIV pathogenesis (reverse transcriptase, protease, or host receptor entry pathways). The rationale provided for this prediction explicitly states that no known mechanistic link exists, and that the association may reflect embedding-space proximity noise in the TxGNN knowledge graph rather than a genuine pharmacological relationship — this is reinforced by several other top-ranked predictions for this drug (SIV infection, feline immunodeficiency syndrome, leprosy) clustering around unrelated infectious-disease nodes with identical lack of supporting evidence.

Given the complete absence of clinical trials or literature, and an explicit mechanistic implausibility noted in the source rationale, this prediction should be treated as exploratory/hypothesis-generating only, not as a basis for further clinical action at this time.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Tezacaftor is currently **not marketed in Canada** — no Drug Identification Numbers (DINs) are on file, so no authorization table is available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (HIV Infectious Disease) has no supporting clinical trials or literature, sits at evidence level L5 (model prediction only), and the mechanistic rationale itself identifies the association as likely graph noise rather than a plausible pharmacological link.

**To proceed, the following is needed:**
- Package insert warnings/contraindications (currently a Blocking data gap — required before any S1 safety screening)
- Confirmed mechanism of action (MOA) data from DrugBank or primary literature
- Independent biological or in vitro rationale connecting CFTR modulation to HIV pathways, if this hypothesis is to be pursued further
- Re-evaluation against alternative candidates in the same prediction set — rank 7 (rheumatoid arthritis, L4) shows at least indirect CFTR-neutrophil biology and one related trial, and may warrant closer review before this HIV signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

