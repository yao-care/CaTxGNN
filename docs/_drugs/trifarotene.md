---
layout: default
title: Trifarotene
parent: Model Prediction Only (L5)
nav_order: 938
evidence_level: L5
indication_count: 10
---

# Trifarotene
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

# Trifarotene: From Acne Vulgaris to Elevated Plasma Zinc

## One-Sentence Summary

Trifarotene is a topical retinoid (a selective RAR-gamma agonist) sold in Canada as AKLIEF. It is generally known for treating acne, though the Canadian license record supplied here does not state an indication.
The TxGNN model ranks **elevated plasma zinc** as its top prediction, but there are **0 clinical trials** and **0 publications** behind it, so the signal is most likely a knowledge-graph artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne vulgaris (general drug knowledge; the Canadian license text is blank in the record) |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Based on known information, trifarotene is a topical selective RAR-gamma agonist. RAR-gamma is the main retinoid receptor in the skin, and it regulates follicular keratinization and sebum-related biology.

The top prediction does not hold up mechanistically. Elevated plasma zinc is a biochemical lab finding, not a skin disease, and a topical retinoid with low systemic exposure has no known effect on zinc handling. The high score (0.994) is most likely a knowledge-graph artifact.

Some lower-ranked predictions are more plausible, though still unproven:
- **Demodicidosis of the sebaceous gland (score 98.42%):** Demodex mites live in the same pilosebaceous units that retinoids act on. Trifarotene is not an acaricide, so any benefit would be indirect, through the follicular environment or inflammation.
- **PAPA syndrome (score 99.32%):** Only the acne component could plausibly respond to a topical retinoid. The underlying IL-1/inflammasome-driven autoinflammation is not a known target of trifarotene.
- **Other candidates:** Malaria, Zollinger-Ellison syndrome, spondyloarthropathy, Ehlers-Danlos syndrome, Beare-Stevenson cutis gyrata syndrome, adermatoglyphia and malignant atrophic papulosis show no credible or only weak links. They are likely graph-propagation artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2494175 | AKLIEF |

The dosage form, manufacturer and approved indication text are blank in the record supplied.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no plausible mechanism, no trials and no literature (evidence level L5). It is best treated as a likely model artifact rather than a repurposing lead.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (this blocks any safety screening)
- Mechanism of action data from DrugBank
- The approved indication text for the Canadian license
- A decision on whether to deprioritize rank 1 and review demodicidosis of the sebaceous gland as a research question
- Any published or registered studies for the chosen indication, before re-evaluating

*This report is for research reference only and is not medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

