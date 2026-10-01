---
layout: default
title: Guaiacol
parent: Model Prediction Only (L5)
nav_order: 439
evidence_level: L5
indication_count: 2
---

# Guaiacol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Guaiacol: From an Unspecified Original Indication to Acute Laryngopharyngitis

## One-Sentence Summary

Guaiacol is marketed in Canada under two DEMO-CINEOL products (children and adult versions), but the approved indication text is not available in the records.
The TxGNN model predicts it may be effective for **acute laryngopharyngitis**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it directly.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Acute laryngopharyngitis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data and the original approved indication are not available for guaiacol, so the mechanistic link cannot be confirmed from this dataset.

As background knowledge only (not evidence from this dataset), guaiacol has a history of use as an expectorant and mild antiseptic in upper-respiratory products. That makes a benefit in an upper-airway inflammatory condition such as acute laryngopharyngitis plausible. The very high TxGNN score (0.996) fits this picture, but the model score alone is not clinical support.

A second prediction, nasal cavity disease (score 99.51%), has one indirect signal. The Phase 2 pilot [NCT01364467](https://clinicaltrials.gov/study/NCT01364467) tested guaifenesin, a structurally related but different compound, in pediatric chronic rhinitis. It cannot be counted as direct evidence for guaiacol.

## Clinical Trial Evidence

Currently no related clinical trials registered for acute laryngopharyngitis.

## Literature Evidence

Currently no related literature available for acute laryngopharyngitis.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 319724 | DEMO-CINEOL ENFANTS/CHILDREN |
| 319716 | DEMO-CINEOL ADULTES/ADULTS |

Dosage form and approved indication details are not available in the records.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the TxGNN score alone. There are no trials or publications for guaiacol in acute laryngopharyngitis, and the original indication and mechanism are unknown. The only related clinical signal (guaifenesin in chronic rhinitis) is indirect and concerns a different condition.

**To proceed, the following is needed:**
- The Health Canada package insert for the DEMO-CINEOL products, covering approved indications, warnings and contraindications
- Mechanism-of-action data for guaiacol (e.g., from DrugBank)
- Direct clinical or preclinical studies of guaiacol in acute laryngopharyngitis
- Assessment of route and formulation compatibility with the target condition
- Evidence that guaiacol shares guaifenesin's activity, if the nasal-disease direction is pursued

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

