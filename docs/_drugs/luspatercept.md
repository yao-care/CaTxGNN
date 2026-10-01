---
layout: default
title: Luspatercept
parent: Model Prediction Only (L5)
nav_order: 563
evidence_level: L5
indication_count: 10
---

# Luspatercept
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

# Luspatercept: From Anemia in Beta-Thalassemia and MDS to Monosomy X

## One-Sentence Summary

Luspatercept is marketed in Canada as REBLOZYL and is known for treating anemia in beta-thalassemia and myelodysplastic syndromes (MDS).
The TxGNN model predicts it may be effective for **monosomy X (Turner syndrome)**, but there are **0 clinical trials** and **0 publications** supporting this, so the score is most likely a graph artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Monosomy X |
| TxGNN Prediction Score | 96.00% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

The original indication is taken from the mechanistic notes in the Evidence Pack. The Canadian license records do not include approved-indication text.

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data is not available. Luspatercept is described as an activin receptor IIB ligand trap that promotes late-stage erythroid maturation, which is why it is used for anemia caused by ineffective red blood cell production.

Monosomy X (Turner syndrome) is a chromosomal disorder, not a disease of erythroid maturation. No plausible mechanistic link to luspatercept has been identified. The high TxGNN score most likely reflects a graph artifact rather than real biological or clinical relevance.

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
| 2505568 | REBLOZYL |
| 2505541 | REBLOZYL |

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction records were found for luspatercept in the queried sources.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no trials, no literature, and no plausible mechanism linking luspatercept to monosomy X. The other nine top-ranked predictions are also L5 and mostly lack a mechanistic rationale. Hepatic infarction is a particular concern, because raising hemoglobin could theoretically increase thrombotic risk.

**Other predicted candidates:**
- **Pyruvate kinase deficiency of red cells** (score 93.84%) is biologically plausible, since it involves chronic hemolytic anemia with some ineffective erythropoiesis. It is flagged as a **Research Question** to check against published literature and registries.
- **Beta-thalassemia silent allele** (93.32%) and **Hb Bart's hydrops fetalis** (92.75%) belong to the thalassemia family, but the silent allele has minimal unmet need and Hb Bart's has no evidence of usability or safety. Both stay on Hold.
- The remaining candidates (hepatic infarction, hepatic veno-occlusive disease, peliosis hepatis, combined immunodeficiency, familial apolipoprotein C-II deficiency, adenosine deaminase deficiency) have no mechanistic link and stay on Hold.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data, for example from the DrugBank API
- Approved-indication text, dosage forms, and manufacturer for the two REBLOZYL licenses
- A systematic literature and registry search, starting with pyruvate kinase deficiency
- Route-of-administration compatibility and similarity-to-original-indication assessments (both currently pending)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

