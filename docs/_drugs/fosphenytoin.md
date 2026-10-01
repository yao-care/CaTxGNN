---
layout: default
title: Fosphenytoin
parent: Model Prediction Only (L5)
nav_order: 412
evidence_level: L5
indication_count: 7
---

# Fosphenytoin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Fosphenytoin: From Anticonvulsant Use to Conjunctivitis

## One-Sentence Summary

Fosphenytoin is a prodrug of phenytoin, a voltage-gated sodium channel blocker used as an anticonvulsant, and is marketed in Canada as CEREBYX.
The TxGNN model predicts it may be effective for **conjunctivitis**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting this specific indication.
Among the other predicted indications, only manic bipolar affective disorder has any human data (one small early-phase study).

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for fosphenytoin is not currently available in the input. Fosphenytoin is a prodrug of phenytoin, which blocks voltage-gated sodium channels and reduces neuronal excitability.

For conjunctivitis, no mechanistic rationale is evident. The condition is an inflammatory or infectious disease of the conjunctiva. Sodium channel blockade has no known link to it, so the high TxGNN score (0.994) cannot be explained by any pharmacological reasoning in the data. It should be treated as a statistical artefact of the knowledge graph until proven otherwise.

The remaining candidates also have weak support. For example, nephrogenic syndrome of inappropriate antidiuresis is caused by gain-of-function variants in the vasopressin V2 receptor, which sodium channel blockade would not address. The one exception is **manic bipolar affective disorder** (rank 4). Other sodium-channel-modulating anticonvulsants (carbamazepine, valproate, lamotrigine) are used in mania, which gives a plausible class-level rationale. One small early-phase study of IV fosphenytoin in acute mania was found (see below).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for conjunctivitis.

For reference, the only literature retrieved in this Evidence Pack relates to a different predicted indication, manic bipolar affective disorder:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12716241](https://pubmed.ncbi.nlm.nih.gov/12716241/) | 2003 | Early-phase clinical study (design not confirmed; likely small pilot) | J Clin Psychiatry | Tested whether high-dose IV fosphenytoin might be acutely antimanic. Results were not verified beyond the title and abstract introduction. |
| [23205958](https://pubmed.ncbi.nlm.nih.gov/23205958/) | 2012 | Review | Epilepsia | How phenobarbital's chemical structure shaped later antiepileptic drugs. Background only, not direct evidence for repurposing. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2230988 | CEREBYX |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The conjunctivitis prediction rests on a model score alone, with no trials, no literature and no plausible mechanism (Evidence Level L5). A high TxGNN score is not enough to justify further investment here.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Fosphenytoin mechanism of action data from DrugBank
- Any supporting preclinical or clinical evidence for conjunctivitis. Absent that, redirect effort to manic bipolar affective disorder (Evidence Level L3, Research Question), starting with retrieval and appraisal of the full text of PMID 12716241 (design, sample size, outcomes)
- Route compatibility assessment. Fosphenytoin is given intravenously or intramuscularly, which is impractical for chronic or ocular use.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

