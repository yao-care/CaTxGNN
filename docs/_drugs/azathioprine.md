---
layout: default
title: Azathioprine
parent: Model Prediction Only (L5)
nav_order: 89
evidence_level: L5
indication_count: 10
---

# Azathioprine
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

# Azathioprine: Repurposing Prediction for Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Azathioprine is a purine-synthesis antimetabolite and immunosuppressant marketed in Canada under 3 DINs. The TxGNN model predicts it may be effective for **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, a rare developmental malformation syndrome. **No clinical trials and no publications** support this prediction, so it is a graph-based model output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 99.999% (overall rank 35) |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source data, and no original indication was recorded. Azathioprine is known as a purine-synthesis antimetabolite. It is converted to 6-mercaptopurine and then to thioguanine nucleotides, which suppress lymphocyte proliferation and produce immunosuppression.

The predicted condition is a developmental malformation syndrome affecting the eye and skeleton. It has no known immune-mediated component that azathioprine could modify. We found no plausible mechanistic link. The very high TxGNN score reflects proximity in the knowledge graph, not biological or clinical support. It should not be read as evidence of efficacy.

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
| 2236819 | TEVA-AZATHIOPRINE |
| 4596 | IMURAN |
| 2242907 | APO-AZATHIOPRINE |

Dosage form, manufacturer and approved indication text were not provided in the source data.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials, no literature, and no plausible mechanism. Nothing supports advancing this indication.

**To proceed, the following is needed:**
- A biological rationale linking azathioprine to the pathogenesis of this syndrome, followed by preclinical or case-level evidence
- Approved indication text, dosage forms and package insert warnings for the three Canadian DINs
- Mechanism of action data for azathioprine from DrugBank

**Note on other candidates in the same Evidence Pack:** Two lower-ranked predictions have substantial evidence and are better evaluated as separate reports.
- **Inflammatory bowel disease** (rank 5) and **ulcerative colitis** (rank 9) are both scored L1 with a Proceed with Guardrails recommendation. Each has Phase 3 trials, and ulcerative colitis also has Cochrane reviews.
- These are established thiopurine uses rather than novel repurposing, so label status should be verified per jurisdiction.
- Suggested guardrails are TPMT/NUDT15 testing, blood count and liver function monitoring, infection and malignancy counseling, and caution with allopurinol and 5-ASA.
- Several Phase 3 entries were judged from truncated trial titles and should be confirmed against the full records.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

