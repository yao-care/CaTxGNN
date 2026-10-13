---
layout: default
title: Periciazine
parent: Model Prediction Only (L5)
nav_order: 722
evidence_level: L5
indication_count: 6
---

# Periciazine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Periciazine: From an Unspecified Original Indication to Migraine Disorder

## One-Sentence Summary

Periciazine is a phenothiazine-class antipsychotic marketed in Canada under the brand name NEULEPTIL. The approved indication text is not available in the data compiled for this report. The TxGNN model predicts it may be effective for **migraine disorder**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the UK-approved use is schizophrenia and other psychoses, plus short-term adjunctive management of severe anxiety, psychomotor agitation, and dangerously impulsive behaviour) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, periciazine is a phenothiazine antipsychotic. Its pharmacology includes activity at the dopamine D1 receptor (DRD1), and phenothiazines generally block dopamine D2, histamine H1, alpha-adrenergic and muscarinic receptors. The source data states that no peer-reviewed data could be found to map a primary molecular target for this drug, so the mechanism cannot be confirmed.

Other phenothiazines, such as chlorpromazine and prochlorperazine, are used for acute migraine, mainly for their antiemetic and central dopamine-blocking effects. This gives a plausible class-level rationale for migraine. However, there is no periciazine-specific clinical or literature evidence, and the high TxGNN score is a computational prediction only.

**Other predicted indications (all Hold, all L5, with no trials or publications):**

| Predicted Indication | TxGNN Score | Comment |
|------|------|------|
| Migraine with brainstem aura | 99.84% | A migraine subtype. It shares the class-level rationale and adds no independent support. |
| Atrophoderma vermiculata | 99.36% | A rare follicular atrophic skin disorder. No plausible mechanistic link was identified, and the score likely reflects knowledge-graph structure. |
| Dysthymic disorder | 99.25% | Only a weak, indirect link through monoaminergic systems. Sedation and side-effect burden make a first-line role unlikely. |
| Migraine with or without aura, susceptibility to | 99.22% | Describes genetic susceptibility rather than a treatable condition, so it is a poor drug target. |
| Ulerythema ophryogenesis | 99.16% | A rare follicular atrophic skin disorder of the eyebrows. No mechanistic link was identified. |

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
| 01926780 | NEULEPTIL | Not specified | Not specified |
| 01926756 | NEULEPTIL | Not specified | Not specified |
| 01926772 | NEULEPTIL | Not specified | Not specified |

All three authorizations are valid single-ingredient products.

---

## Safety Considerations

Please refer to the package insert for safety information.

The data compiled for this report did not include package insert warnings or contraindications, and no disease-level contraindications were found in the knowledge graph. The drug interaction query completed but returned only a pharmacology entry (periciazine acting at the D1 receptor), not a drug-drug interaction. As a phenothiazine antipsychotic, periciazine should be assessed for sedation, anticholinergic effects, and other class-related risks before any new use is considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score and a class-level mechanistic argument (other phenothiazines are used in acute migraine). There are no trials or publications specific to periciazine, the mechanism data is incomplete, and the Canadian safety information could not be retrieved, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications, approved indication, dosage forms), obtained by downloading and parsing the product monograph
- Mechanism of action data for periciazine from DrugBank
- A systematic literature search for periciazine or close phenothiazine analogues in migraine
- Route and formulation compatibility assessment, since migraine treatment may need different routes than the marketed products
- A benefit-risk assessment against established migraine therapies, including sedation and extrapyramidal side-effect burden
- Deprioritization of the dermatologic predictions (atrophoderma vermiculata, ulerythema ophryogenesis) and the genetic-susceptibility term, which have no identifiable mechanistic rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

