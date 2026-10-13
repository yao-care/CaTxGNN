---
layout: default
title: Vaborbactam
parent: Model Prediction Only (L5)
nav_order: 961
evidence_level: L5
indication_count: 10
---

# Vaborbactam
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

# Vaborbactam: From Bacterial Infection Treatment to Osteoarthritis

## One-Sentence Summary

Vaborbactam is a beta-lactamase inhibitor marketed in Canada as VABOMERE. The TxGNN model predicts it may be effective for **osteoarthritis**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on a computational prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the Canadian licence has no indication text) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 98.52% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Vaborbactam is known as a cyclic boronic acid beta-lactamase inhibitor. It protects partner antibiotics from enzymatic breakdown by bacteria, and it has no known direct activity on joint cartilage, inflammation, or pain pathways.

No mechanistic link between vaborbactam and osteoarthritis has been established. The high TxGNN score (0.985) is a knowledge-graph prediction only. The same pattern appears across the other top predictions, which include osteoarthritis susceptibility, rheumatoid arthritis, gout, and several rare skeletal dysplasias. These predictions most likely reflect graph-neighbourhood artefacts rather than biology. The score should therefore be treated as a hypothesis-generating signal, not as evidence of efficacy.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02554151 | VABOMERE | Not specified | Not specified |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or literature (Evidence Level L5) and no plausible mechanistic link between a beta-lactamase inhibitor and osteoarthritis. Safety label data are also missing, so the candidate cannot move to safety screening.

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications, approved indication) obtained and reviewed
- Mechanism of action data from DrugBank
- A credible biological rationale for joint disease, plus preclinical or observational evidence
- Confirmation of route and formulation compatibility, since no dosage form is recorded
- Review of the other top predictions (rheumatoid arthritis, gout, and the rare skeletal disorders), which are equally unsupported by evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

