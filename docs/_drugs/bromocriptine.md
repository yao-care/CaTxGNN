---
layout: default
title: Bromocriptine
parent: Model Prediction Only (L5)
nav_order: 128
evidence_level: L5
indication_count: 10
---

# Bromocriptine
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

# Bromocriptine: From an Unrecorded Original Indication to Congenital Disorder of Glycosylation with Defective Fucosylation

## One-Sentence Summary

The supplied data does not record what bromocriptine was originally approved to treat in Canada.
The TxGNN model predicts it may be effective for **congenital disorder of glycosylation with defective fucosylation**, but this rests on a model score alone, with **0 clinical trials** and **0 publications** supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Congenital disorder of glycosylation with defective fucosylation |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied records. The mechanism described elsewhere in the evidence is dopamine D2 receptor agonism, which has no evident connection to defective fucosylation, a rare inherited disorder of protein glycosylation.

No trials or literature were retrieved to bridge the gap. The only basis for this prediction is the high knowledge-graph score (99.83%, model rank 3,916). A score this high does not by itself indicate a real therapeutic link. It should be treated as a hypothesis-generating signal, not evidence of efficacy.

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
| 2230454 | BROMOCRIPTINE |
| 2087324 | BROMOCRIPTINE |

The approved indication text and dosage forms are not available in the supplied records.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no mechanistic link, no registered trials and no literature. It is a prediction-only signal at evidence level L5, so there is no basis to advance it.

**Other predicted indications in the same run:**

| Predicted Indication | Score | Evidence Level | Note |
|------|------|------|------|
| Schizophrenia (rank 9) | 99.73% | L4 | The only prediction with trials (3 registered). Bromocriptine is a D2 agonist, the opposite of standard antipsychotics, and one case report describes bromocriptine-induced schizophrenia. The trials address antipsychotic side effects (metabolic problems, hyperprolactinemia), not schizophrenia itself. Decision: Research Question, for adjunctive use only, with relapse monitoring. |
| Retinal dystrophy with or without extraocular anomalies (rank 3) | 99.82% | L5 | The retrieved literature is mostly general reviews and case reports on congenital eye anomalies. One 2024 preclinical repurposing study (PMID 39009597) needs manual checking to confirm bromocriptine was actually tested. |
| Hydranencephaly, myopia entries, and other rare disorders | 99.73–99.83% | L5 | No supporting evidence. |

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data from DrugBank
- The approved indications and dosage forms for DINs 2230454 and 2087324
- Manual review of PMID 39009597 to decide whether the retinal indication can move to L4
- For schizophrenia, a protocol focused on adjunctive use for antipsychotic-related adverse effects
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

