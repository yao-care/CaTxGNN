---
layout: default
title: Ipilimumab
parent: Model Prediction Only (L5)
nav_order: 488
evidence_level: L5
indication_count: 2
---

# Ipilimumab
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

# Ipilimumab: From Melanoma to Choroideremia

## One-Sentence Summary

Ipilimumab (marketed in Canada as YERVOY) is an anti-CTLA-4 antibody. The Evidence Pack does not list an approved indication, so the original use, melanoma, comes from general knowledge.
The TxGNN model predicts it may be effective for **choroideremia**, an inherited retinal degeneration, but **no clinical trials and no publications** support this prediction, so it is only a model output.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the record (melanoma, by general knowledge) |
| Predicted New Indication | Choroideremia |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Ipilimumab is known to block CTLA-4, which releases T-cell inhibition, and its efficacy in melanoma is established. Based on that mechanism, however, there is no clear rationale for choroideremia.

Choroideremia is an X-linked retinal degeneration caused by loss of function of the CHM gene (REP1). Its pathology is not driven by CTLA-4-mediated T-cell suppression. The high score (0.99) is therefore most likely a knowledge-graph artifact rather than a biologically grounded signal.

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
| 2379384 | YERVOY |

Dosage form, manufacturer and approved indication text are not provided in the record.

---

## Cytotoxicity

Ipilimumab is an anticancer drug. The record contains no DrugBank category or toxicity data, so the entries below rely on general knowledge and should be checked against the product monograph.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-CTLA-4 monoclonal antibody), not a conventional cytotoxic |
| Myelosuppression Risk | Not a typical feature; please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Low |
| Monitoring Items | Signs of immune-related adverse events, including liver function, thyroid function, and blood counts as clinically indicated |
| Handling Protection | Please refer to the package insert; conventional cytotoxic handling rules generally do not apply to monoclonal antibodies |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The choroideremia prediction rests only on a knowledge-graph score. It has no trials, no literature, and no plausible mechanistic link to CTLA-4 blockade.

**To proceed, the following is needed:**
- Mechanism of action data (DrugBank) and the Health Canada product monograph (warnings and contraindications)
- A credible biological hypothesis linking CTLA-4 blockade to choroideremia; without one, the candidate should be dropped

**Note on the second prediction in the pack:** *non-cutaneous melanoma* (uveal and mucosal), score 99.02%, is far better supported than choroideremia.
- Ipilimumab already has a melanoma role, so this is an extension to other subtypes rather than a distant repurposing.
- The pack lists 46 trials and 5 publications, including a completed randomized Phase 2 trial in unresectable melanoma (NCT01950390, n=169) and a terminated uveal melanoma pilot (NCT01730157, n=6).
- The pack assigns L2 and "Research Question". Subtype-specific evidence is thin, and the proportion of non-cutaneous patients in the larger trials is unverified.
- Uveal melanoma has a low mutational burden and an immune-privileged site, and mucosal melanoma responds less well to checkpoint inhibitors than cutaneous disease.
- This candidate is the more useful one to pursue, starting with subtype-level data extraction from the listed trials.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

