---
layout: default
title: L-Lysine
parent: Model Prediction Only (L5)
nav_order: 509
evidence_level: L5
indication_count: 3
---

# L-Lysine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# L-Lysine: From Amino Acid Nutrition Component to Gastroparesis

## One-Sentence Summary

L-Lysine is an essential amino acid. In Canada it is marketed as a component of parenteral nutrition products such as CLINIMIX and TRAVASOL.
The TxGNN model predicts it may be effective for **gastroparesis**, but there are **0 clinical trials** and only **1 publication**, a preclinical stem-cell study that does not test L-lysine.
The prediction is model-only and unsupported by direct evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records (inferred from product names: amino acid component of parenteral nutrition) |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. L-lysine is an essential amino acid supplied in parenteral nutrition solutions, and no approved indication text is recorded in the licence data. No established mechanistic route from nutritional lysine supply to gastroparesis can be drawn from the available information.

The only retrieved paper studies mesenchymal stem cell delivery from gelatin-alginate hydrogels to the stomach lumen. It does not evaluate L-lysine as a therapy, and any link is incidental (for example, lysine residues in the gelatin matrix). The high score (0.998) is therefore best read as a knowledge-graph association, not a validated pharmacological rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29414870](https://pubmed.ncbi.nlm.nih.gov/29414870/) | 2018 | Preclinical | Bioengineering (Basel) | Mesenchymal stem cells delivered from gelatin-alginate hydrogels to the stomach lumen as a potential gastroparesis therapy. L-lysine is not evaluated. |

## Canada Market Information

Dosage form and approved indication text are not recorded for these licences. Five of the 20 authorizations are listed.

| DIN | Product Name |
|---------|------|
| 2046709 | CLINIMIX |
| 2013932 | CLINIMIX |
| 2013940 | CLINIMIX |
| 872296 | TRAVASOL |
| 2013886 | CLINIMIX |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials and no literature that tests L-lysine in gastroparesis. The other two predictions are also weak. Congenital prothrombin deficiency is supported only by a paper on a lysine substitution in a mutant factor X protein. "Obsolete vitamin D deficiency" has no evidence at all, and its disease label is obsolete.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (e.g., from DrugBank) to test for a plausible link to gastric motility
- Direct evidence, such as preclinical or clinical studies of L-lysine in gastroparesis
- The approved indication text for the listed DINs, to confirm the original indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

