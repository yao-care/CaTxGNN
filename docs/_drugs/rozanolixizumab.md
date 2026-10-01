---
layout: default
title: Rozanolixizumab
parent: Model Prediction Only (L5)
nav_order: 820
evidence_level: L5
indication_count: 10
---

# Rozanolixizumab
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

# Rozanolixizumab: From Generalized Myasthenia Gravis to Bronchitis

## One-Sentence Summary

Rozanolixizumab (brand name RYSTIGGO) is an anti-FcRn antibody that lowers circulating IgG. The licence record in the Evidence Pack does not list its original indication, but it is known for generalized myasthenia gravis.
The TxGNN model predicts it may be effective for **bronchitis**, but there are currently **0 clinical trials** and **0 publications** supporting this, and the pack's own mechanistic review judges the link implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the licence record (known use: generalized myasthenia gravis) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 95.28% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. Rozanolixizumab is an anti-FcRn antibody. By blocking FcRn recycling, it lowers circulating IgG, which suits IgG-mediated autoimmune disease.

This mechanism does not support a benefit in bronchitis. Lowering IgG weakens humoral defence and raises infection risk, so respiratory infection is a safety concern rather than a treatment target. The high TxGNN score is most likely a knowledge-graph artifact, not a real pharmacological signal.

The other top-ranked predictions look no better. All are scored L5 with a Hold recommendation:

| Rank | Predicted Indication | TxGNN Score | Assessment |
|------|------|------|------|
| 2 | Plasma cell myeloma | 95.05% | Theoretical only. FcRn blockade might lower M-protein in IgG myeloma but would not treat the malignant clone, and infection risk is already high. |
| 3 | Indolent plasma cell myeloma | 94.73% | Same weak rationale. No IgG-mediated pathology to target, so the benefit-risk balance is unfavorable. |
| 4 | Hemoglobinopathy | 94.17% | No mechanistic link. Inherited globin defect, not IgG-mediated. |
| 5 | Gastric carcinoma | 93.59% | No evidence for FcRn blockade as an anti-tumour strategy. |
| 6 | Partial deletion of the short arm of chromosome 16 | 93.39% | No plausible link. Likely a graph artifact. |
| 7 | Diffuse gastric adenocarcinoma | 93.36% | Subtype of rank 5, so redundant with it. |
| 8 | Beta-thalassemia with other manifestations | 93.13% | No link. Genetic globin synthesis defect. |
| 9 | Hemolytic anemia due to glucophosphate isomerase deficiency | 92.75% | No link. Non-immune hereditary enzymopathy. |
| 10 | Pyruvate kinase deficiency of red cells | 92.56% | No link. IgG lowering would not address the metabolic defect. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2556081 | RYSTIGGO | — | — |

The licence record does not include the dosage form, manufacturer or approved indication text.

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug-drug interaction records were found in the pack. Because the drug lowers IgG, infection risk is the main concern for any new use, especially in respiratory infection or in diseases that already involve hypogammaglobulinemia, such as myeloma.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predictions are model-only (L5) with no registered trials or publications. None has a plausible mechanistic link to FcRn blockade. For bronchitis, IgG lowering would raise rather than reduce risk.

**To proceed, the following is needed:**
- The Health Canada package insert warnings and contraindications, which block the safety screening step
- Mechanism-of-action data from DrugBank
- Any clinical or preclinical evidence for the predicted indications. Without it, the top candidates should not advance beyond the current stage.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

