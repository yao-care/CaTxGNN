---
layout: default
title: Alglucosidase Alfa
parent: Model Prediction Only (L5)
nav_order: 33
evidence_level: L5
indication_count: 10
---

# Alglucosidase Alfa
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

# Alglucosidase Alfa: From Pompe Disease to Adult Polyglucosan Body Disease

## One-Sentence Summary

Alglucosidase alfa is a recombinant lysosomal acid alpha-glucosidase (GAA) enzyme replacement therapy, marketed in Canada as MYOZYME and used for Pompe disease.
The TxGNN model predicts it may be effective for **Adult Polyglucosan Body Disease**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so this is a research question rather than a candidate for development.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pompe disease (from the drug's known class; the Canadian license record supplied has no indication text) |
| Predicted New Indication | Adult polyglucosan body disease |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, alglucosidase alfa is a recombinant form of lysosomal acid alpha-glucosidase (GAA). It breaks down glycogen inside lysosomes, and its efficacy in Pompe disease has been established.

Adult polyglucosan body disease is caused by a deficiency of the glycogen branching enzyme (GBE1). The result is poorly branched polyglucosan that accumulates mainly in the cytosol of neurons and axons. The link to alglucosidase alfa is biologically plausible but weak, for three reasons:
- The two diseases involve different enzymes and different cellular compartments (lysosomal versus cytosolic glycogen).
- GAA does not correct the primary branching defect, and it is unclear whether it could clear cytosolic polyglucosan.
- The enzyme does not cross the blood-brain barrier well, which limits delivery to the nervous system.

The high score probably reflects shared glycogen-metabolism neighbours in the knowledge graph, not proven pharmacology.

The other nine predictions fall into two groups:
- **Glycogen branching enzyme deficiency (GSD IV):** the congenital neuromuscular form (rank 2) and the fatal perinatal form (rank 3) have the same weak rationale as above. The fatal perinatal course also limits feasibility.
- **Eyelid, ptosis and ocular syndromes (ranks 4–10):** these include congenital entropion, congenital ectropion, congenital Horner syndrome, ptosis-vocal cord paralysis syndrome, camptodactyly-myopia-medial rectus fibrosis, epiblepharon and ptosis-strabismus-ectopic pupils syndrome. There is no credible mechanistic link. These scores most likely reflect knowledge-graph artefacts or phenotype overlap, such as ptosis in late-onset Pompe disease. All seven are rated Hold.

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
| 2284863 | MYOZYME |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5), with no trials or publications. The biology argues against it: the enzyme targets lysosomal glycogen, whereas the disease is a cytosolic branching defect, and CNS delivery is poor. The remaining nine predictions have weak or no credible mechanistic support.

**To proceed, the following is needed:**
- The Health Canada package insert, to establish the approved indication, warnings and contraindications
- Mechanism of action data from DrugBank
- Preclinical evidence that GAA can reduce cytosolic polyglucosan in a GBE1-deficiency model
- A CNS delivery strategy, since the enzyme crosses the blood-brain barrier poorly
- A literature and trial search specific to glycogen branching enzyme deficiency

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

