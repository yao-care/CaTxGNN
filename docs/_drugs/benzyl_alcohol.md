---
layout: default
title: Benzyl Alcohol
parent: Model Prediction Only (L5)
nav_order: 105
evidence_level: L5
indication_count: 1
---

# Benzyl Alcohol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Benzyl Alcohol: From Topical Pain Relief Products to Bronchitis

## One-Sentence Summary

Benzyl alcohol is an ingredient in topical pain-relief products marketed in Canada (Salonpas solution and cream). The TxGNN model predicts it may be effective for **bronchitis**, but there are **0 clinical trials** and only **4 publications** on the topic. Those publications suggest benzyl alcohol may *cause* bronchitis rather than treat it, so the prediction is not supported.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the licence data (the marketed products are topical pain-relief products) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 (model prediction only; the pack lists L4, but no retrieved study tests benzyl alcohol as a treatment) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for benzyl alcohol, and no original approved indication text is listed. The two marketed products are pain-relieving topical products, but a mechanistic bridge from topical pain relief to bronchitis cannot be established from the available information.

The retrieved literature points the opposite way. Benzyl alcohol is the preservative in bacteriostatic saline. Reports from 1990 and 1995 describe bronchitis and airway irritation after nebulizing that saline. The link between benzyl alcohol and bronchitis therefore looks like a probable adverse effect, not a therapeutic one.

The very high TxGNN score (99.46%) is most likely a knowledge-graph association artifact driven by co-occurrence, not evidence of benefit. Route compatibility is also unassessed: the marketed products are topical, while the bronchitis signal comes from inhaled exposure.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7807035](https://pubmed.ncbi.nlm.nih.gov/7807035/) | 1995 | Case report (adverse event) | J Fam Pract | Tested whether nebulized bacteriostatic saline, which contains the preservative benzyl alcohol, irritates the tracheobronchial mucosa in healthy adults. Title suggests it can cause bronchitis. |
| [7775900](https://pubmed.ncbi.nlm.nih.gov/7775900/) | 1995 | Letter/Commentary | J Fam Pract | Commentary on nebulized saline and bronchitis (no abstract available). |
| [2355429](https://pubmed.ncbi.nlm.nih.gov/2355429/) | 1990 | Case report (adverse event) | JAMA | Reports nebulizer bronchitis induced by bacteriostatic saline (no abstract available). |
| [36747926](https://pubmed.ncbi.nlm.nih.gov/36747926/) | 2023 | In vitro/phytochemical study | Heliyon | Evaluates Senna tora leaf extracts for antioxidant, anti-inflammatory and antibacterial activity. The plant is used traditionally for bronchitis, but the study is not about benzyl alcohol therapy. |

None of these publications supports benzyl alcohol as a treatment for bronchitis.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2511428 | SALONPAS PAIN RELIEVING SOLUTION |
| 2511339 | SALONPAS PAIN RELIEVING CREAM |

---

## Safety Considerations

Please refer to the package insert for safety information.

Literature signal: nebulized bacteriostatic saline containing benzyl alcohol has been reported to irritate the airways and cause bronchitis (JAMA 1990; J Fam Pract 1995). This is a safety concern for any inhaled use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. The available literature suggests benzyl alcohol is associated with bronchitis as an adverse effect, and there are no clinical trials and no mechanistic support.

**To proceed, the following is needed:**
- The Health Canada package insert (warnings, contraindications, approved indications)
- Mechanism of action data (for example from DrugBank)
- Evidence that benzyl alcohol has therapeutic activity in bronchitis, and a review of the adverse-event signal in inhaled exposure
- Assessment of route compatibility (topical products versus the airway exposure seen in the reports)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

