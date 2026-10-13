---
layout: default
title: Brolucizumab
parent: Model Prediction Only (L5)
nav_order: 127
evidence_level: L5
indication_count: 4
---

# Brolucizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Brolucizumab: From Macular Degeneration to Mitochondrial Oxidative Phosphorylation Disorder Due to Nuclear DNA Anomalies

## One-Sentence Summary

Brolucizumab is an anti-VEGF-A antibody fragment given by intravitreal injection, originally used to treat macular degeneration.
The TxGNN model predicts it may be effective for **mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Macular degeneration |
| Predicted New Indication | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, brolucizumab is a single-chain antibody fragment (scFv) that inhibits VEGF-A. It is given by intravitreal injection, and its efficacy in macular degeneration comes from reducing abnormal blood vessel growth and leakage in the retina.

For the predicted indication, no mechanistic link is established. Primary mitochondrial oxidative phosphorylation disorders arise from nuclear DNA defects in respiratory chain subunits or assembly factors. VEGF-A inhibition does not address this pathology. The high score (0.997) is a graph-based prediction only, and because the annotated mechanism is missing, it cannot be cross-checked.

Practical concerns also apply. Systemic VEGF blockade in a multisystem metabolic disease would raise safety questions, and intravitreal dosing is unlikely to reach relevant tissues beyond the eye.

**Other predicted indications (all L5, all Hold):**

| Predicted Indication | TxGNN Score | Assessment |
|------|------|------|
| Esophageal varices without bleeding | 99.12% | Only an indirect theoretical link (VEGF-driven angiogenesis in portal hypertension). Systemic exposure from an intravitreal agent is doubtful, and anti-VEGF class bleeding and GI perforation risks are a concern. |
| Esophageal varices with bleeding | 99.12% | Same theoretical rationale, but anti-VEGF agents carry hemorrhagic risk. Established standard care exists, and there is no rationale for use in the acute setting. |
| Exocrine pancreatic insufficiency | 99.07% | No credible mechanistic link. The condition results from loss of pancreatic enzyme secretion, which VEGF-A inhibition does not restore. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02496976 | BEOVU | Not specified | Not specified |

## Safety Considerations

- **Contraindications suggested by the knowledge graph (not label text):** uveitis, iris disease, ciliary body disease, panuveitis, eye infectious disease, conjunctivitis. These come from drug-disease contraindication edges and should be verified against the official product monograph.
- **Class-level concerns for the predicted indications:** anti-VEGF therapy is associated with bleeding, thromboembolic events and GI perforation risk. These are especially relevant for esophageal varices.

No drug interaction records were found. For full warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four predictions are supported only by the TxGNN graph score, with no clinical trials or publications. No credible mechanistic link exists for any of them, and the intravitreal route and class bleeding risks argue against repurposing.

**To proceed, the following is needed:**
- Health Canada product monograph warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank, to enable a proper mechanistic-link analysis
- Any preclinical or clinical evidence linking VEGF-A inhibition to the predicted conditions
- Route compatibility assessment, since systemic delivery would be needed for most predicted indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

