---
layout: default
title: Iodixanol
parent: Model Prediction Only (L5)
nav_order: 484
evidence_level: L5
indication_count: 10
---

# Iodixanol
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

# Iodixanol: From Diagnostic Contrast Imaging to Osteoarthritis Susceptibility

## One-Sentence Summary

Iodixanol is an iso-osmolar iodinated contrast agent used in diagnostic imaging, not a disease-modifying drug.
The TxGNN model predicts it may be relevant to **osteoarthritis susceptibility**, but **0 clinical trials** and **0 publications** support this specific prediction.
The high score is most likely a knowledge-graph artifact rather than a real therapeutic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Iodinated contrast agent for diagnostic imaging (approved indication text is not provided in the Canadian licence records) |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Iodixanol is an iso-osmolar iodinated contrast medium. It works by attenuating X-rays for imaging and has no known disease-modifying pharmacology.

No mechanistic link between iodixanol and osteoarthritis susceptibility has been identified. The very high TxGNN score has no supporting trials or literature, so it likely reflects the drug's position in the knowledge graph, not a genuine biological effect.

A related prediction, **osteoarthritis** (score 99.07%), has 7 publications. All of them use iodixanol as an imaging or transport probe, for example CT imaging of cartilage or measuring solute diffusion across cartilage and subchondral bone. None tests a treatment effect, so this is indirect evidence at best.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for osteoarthritis susceptibility.

For the closely related prediction **osteoarthritis** (rank 2), the following publications were retrieved. They show iodixanol only as a diagnostic or research tool:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40155520](https://pubmed.ncbi.nlm.nih.gov/40155520/) | 2025 | Preclinical imaging study | Ann Biomed Eng | Dual-contrast agent in photon-counting CT to assess articular cartilage health |
| [39012563](https://pubmed.ncbi.nlm.nih.gov/39012563/) | 2024 | Preclinical imaging study | Ann Biomed Eng | Nanoparticle diffusion imaging with CT and finite element modelling of cartilage function |
| [30145230](https://pubmed.ncbi.nlm.nih.gov/30145230/) | 2018 | Ex vivo animal study | Osteoarthritis Cartilage | Ageing did not change compressive stiffness of equine mandibular condylar cartilage |
| [30374787](https://pubmed.ncbi.nlm.nih.gov/30374787/) | 2018 | In vitro study | J Exp Orthop | Iodine contrast agents did not affect platelet-rich plasma function early in vitro (compatibility observation) |
| [28063646](https://pubmed.ncbi.nlm.nih.gov/28063646/) | 2017 | Ex vivo / computational | J Biomech | Iodixanol used as a CT probe of solute transport across the cartilage–subchondral bone interface |
| [28518064](https://pubmed.ncbi.nlm.nih.gov/28518064/) | 2017 | Experimental / computational protocol | J Vis Exp | Protocol for studying neutral and charged solute transport across articular cartilage |
| [27793406](https://pubmed.ncbi.nlm.nih.gov/27793406/) | 2016 | Computational (finite element) | J Biomech | Finite element model of neutral solute transport across the osteochondral interface |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02145766 | VISIPAQUE 270 |
| 02145774 | VISIPAQUE 320 |
| 02553953 | IODIXANOL INJECTION 270 |
| 02553961 | IODIXANOL INJECTION 320 |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials, no literature and no plausible pharmacological mechanism. The related osteoarthritis literature treats iodixanol only as an imaging probe, so there is no evidence of therapeutic benefit.

**To proceed, the following is needed:**
- The Health Canada product monograph, to establish warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data, to test whether any biological link to osteoarthritis exists
- Preclinical or clinical studies that test a therapeutic effect on osteoarthritis, since the current publications only cover imaging use

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

