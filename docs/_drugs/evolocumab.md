---
layout: default
title: Evolocumab
parent: Model Prediction Only (L5)
nav_order: 369
evidence_level: L5
indication_count: 10
---

# Evolocumab
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

# Evolocumab: From LDL-Cholesterol Lowering to Symptomatic Hemophilia in Female Carriers

## One-Sentence Summary

Evolocumab is a PCSK9-inhibiting monoclonal antibody that lowers LDL cholesterol, and it is marketed in Canada as REPATHA.
The TxGNN model predicts it may be effective for **symptomatic form of hemophilia in female carriers**,
but **0 clinical trials** and **0 publications** support this direction, so the prediction is not actionable at present.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Symptomatic form of hemophilia in female carriers |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the Evidence Pack. Based on known information, evolocumab is a PCSK9 monoclonal antibody. It increases LDL receptor recycling and lowers LDL-C.

**The prediction is not biologically supported.** Evolocumab has no known role in coagulation factor VIII or IX synthesis or function, and the hemophilia carrier state involves a clotting-factor deficiency that PCSK9 inhibition does not correct. The high TxGNN score (99.82%) most likely reflects proximity within the knowledge graph, not a real biological signal.

The other top-ranked predictions show the same pattern. Most are coagulation or bleeding disorders, or very broad ontology categories, and none has a plausible mechanistic link to PCSK9 inhibition:

| Rank | Predicted Indication | Score | Mechanistic Assessment |
|------|------|------|------|
| 2 | Familial apolipoprotein C-II deficiency | 99.50% | Weak, indirect lipid link. Evolocumab does not address the lipoprotein lipase activation defect. |
| 3 | Thrombocytopenic purpura | 99.42% | No link. The disease involves autoantibodies or ADAMTS13 deficiency. |
| 4 | Factor XI deficiency | 99.29% | No plausible mechanism. |
| 5 | Hemophilia A with vascular abnormality | 99.22% | No plausible mechanism. |
| 6 | Disease of catalytic activity | 99.08% | Too broad to evaluate. |
| 7 | Hemorrhagic disease of newborn | 98.89% | No mechanism (vitamin K deficiency). Neonatal antibody use would raise separate safety concerns. |
| 8 | X-linked ichthyosis without steroid sulfatase deficiency | 98.84% | Tangential cholesterol link only. |
| 9 | Inherited thrombophilia | 98.82% | Speculative preclinical PCSK9–platelet link. Not established clinically. |
| 10 | Disorder of other vitamins and cofactors metabolism and transport | 98.80% | Too broad, no identified connection. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2446057 | REPATHA |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5) with no supporting trials or literature. The mechanism is implausible: PCSK9 inhibition does not replace or upregulate clotting factors. The high score is likely a knowledge-graph artifact. None of the top 10 predicted indications has clinical support.

**To proceed, the following is needed:**
- Mechanistic evidence linking PCSK9 inhibition to the predicted indication. Without it, further investment is not justified.
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening).
- Approved indication text and dosage form for the Canadian license.
- Detailed mechanism of action data from DrugBank.
- Any clinical or preclinical studies in the predicted indication. If none exist, consider re-ranking predictions by biological plausibility, for example indications closer to lipid metabolism.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

