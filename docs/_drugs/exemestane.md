---
layout: default
title: Exemestane
parent: Model Prediction Only (L5)
nav_order: 370
evidence_level: L5
indication_count: 7
---

# Exemestane
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

# Exemestane: From Breast Cancer to Antithrombin Deficiency Type 2

## One-Sentence Summary

Exemestane is an irreversible steroidal aromatase inhibitor that lowers estrogen. It is used in hormone-driven breast cancer, and the indication text was not captured in the licence records, so this is inferred from its drug class.
The TxGNN model predicts it may be effective for **antithrombin deficiency type 2**, but there are **0 clinical trials** and **0 publications** supporting this direction, and no plausible mechanism has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Breast cancer (inferred from drug class; not stated in the Canadian licence records) |
| Predicted New Indication | Antithrombin deficiency type 2 |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Exemestane is a steroidal aromatase inhibitor. It permanently blocks the enzyme that converts androgens into estrogens, which lowers circulating estradiol. That is the basis of its use in estrogen-dependent breast cancer.

Type 2 antithrombin deficiency is an inherited defect in the antithrombin protein (SERPINC1 gene). Aromatase inhibition does not correct this defect, so no plausible mechanistic link to the original use exists.

The 99.83% score is most likely a graph-proximity artifact. The scores of all seven predicted candidates cluster above 99%, so they do not discriminate between candidates. The prediction should not be read as a real repurposing signal.

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
| 2390183 | ACT EXEMESTANE |
| 2407841 | MED-EXEMESTANE |
| 2242705 | AROMASIN |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal therapy (steroidal aromatase inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Low |
| Emetogenicity Classification | Low |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert and your institution's hazardous-drug handling policy |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no trials or publications for this indication, and the evidence is model prediction only (L5). Aromatase inhibition has no known effect on the antithrombin defect, and the high score looks like a graph artifact.

The other six candidates do not change this decision:
- **Thrombosis-related candidates** (factor V excess, heparin cofactor II deficiency, thrombophilia): also L5, with no direct mechanism.
- **Amenorrhea:** five papers exist (L4), but they concern amenorrhea or ovarian suppression as an on-treatment effect in breast cancer, not amenorrhea as a target for exemestane.
- **Migraine and migraine with brainstem aura:** L5. Estrogen depletion could plausibly worsen migraine, so these are better treated as possible adverse-effect signals than as therapeutic candidates.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data from DrugBank
- A mechanistic rationale for antithrombin deficiency type 2 that goes beyond the model score
- For the amenorrhea literature, a review of the full abstracts before any upgrade in evidence level (study types are currently inferred from titles only)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

