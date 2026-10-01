---
layout: default
title: Teprotumumab
parent: Model Prediction Only (L5)
nav_order: 888
evidence_level: L5
indication_count: 10
---

# Teprotumumab
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

# Teprotumumab: From Its Marketed Use to Monosomy X (Turner Syndrome)

## One-Sentence Summary

Teprotumumab is an IGF-1R-inhibiting monoclonal antibody marketed in Canada as TEPEZZA, though the record does not state its approved indication.
The TxGNN model predicts it may be effective for **monosomy X** with a score of 99.79%, but there are **0 clinical trials** and **0 publications** supporting this direction.
This is a model-only prediction, and the mechanistic rationale is speculative and possibly counterproductive.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Monosomy X |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. The prediction review notes that teprotumumab inhibits IGF-1R. The IGF-1/growth hormone axis is relevant to growth failure in Turner syndrome (monosomy X), which is the only plausible link to this prediction.

That link is weak. Blocking IGF-1R would be expected to oppose growth, which is the opposite of the growth-promoting therapy used in Turner syndrome. The high score most likely reflects shared gene or phenotype neighbours in the knowledge graph, not a real therapeutic signal.

The other nine top predictions are also L5 and Hold. Five are Turner-spectrum or X-chromosome entries: Turner syndrome due to structural X anomalies, mosaic monosomy X, mixed gonadal dysgenesis, sex chromosome disorder of sex development, and X chromosome number anomaly. They share the same graph neighbourhood and are not independent signals. The remaining four are esophageal varices with and without bleeding, varicose disease, and mitochondrial OXPHOS disorder due to nuclear DNA anomalies. None has a supported mechanism.

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
| 2557061 | TEPEZZA | Not recorded | Not recorded |

---

## Safety Considerations

Please refer to the package insert for safety information.

The prediction review for esophageal varices notes that teprotumumab carries ototoxicity and hyperglycemia risks, which weigh against use in unsupported indications. No drug-interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score, with no trials or publications. The one plausible mechanism, IGF-1R inhibition, would likely work against growth in Turner syndrome. This is a probable graph artifact and does not justify further investment now.

**To proceed, the following is needed:**
- Mechanism of action data (MOA), to test whether any link to X-chromosome disorders exists
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Approved indication text for the Canadian licence
- Preclinical or clinical evidence for any predicted indication, ideally with a rationale that does not depend on IGF-1R blockade being beneficial
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

