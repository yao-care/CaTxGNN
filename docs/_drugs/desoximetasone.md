---
layout: default
title: Desoximetasone
parent: High Evidence (L1-L2)
nav_order: 266
evidence_level: L2
indication_count: 10
last_modified_at: 2026-11-20
description: "Desoximetasone: predicted new indication Alopecia areata (evidence level L2). Approved use: Inflammatory skin conditions, including atopic eczema…"
monitor_inn: "DESOXIMETASONE"
predicted_indications: ["alopecia areata", "alopecia mucinosa", "telogen effluvium", "hereditary hypotrichosis with recurrent skin vesicles", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "primary cutaneous B-cell lymphoma", "atrichia with papular lesions", "vulvar inverted follicular keratosis"]
---

# Desoximetasone
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Desoximetasone: From Inflammatory Skin Conditions to Alopecia Areata
{: .text-alpha }

## One-Sentence Summary

Desoximetasone is a potent topical corticosteroid originally used for inflammatory skin conditions such as eczema, dermatitis and discoid lupus erythematosus.
The TxGNN model predicts it may be effective for **alopecia areata**,
with **no registered clinical trials** and **1 publication** (a randomized, double-blind, placebo-controlled trial) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Inflammatory skin conditions, including atopic eczema, contact dermatitis, seborrheic dermatitis and discoid lupus erythematosus (the Canadian licence records contain no indication text) |
| Predicted New Indication | Alopecia areata |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L2 |
| Canada Market Status | Marketed (marketed DINs: 4 of 4) |
| Number of DINs | 4 (marketed: 4) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for desoximetasone: "Corticosteroids play a role in cellular signaling, immune function, inflammation and protein regulation; however, the precise mechanism of action in psoriasis is unknown." ([DailyMed: Topicort (desoximetasone) prescribing information, Sun Pharmaceutical Industries, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e417856a-b760-4626-bc34-8e4bc62c026c), label version 2025-07-02; accessed 2026-11-19.) Based on known information, desoximetasone is a topical corticosteroid. Its pharmacology record lists the glucocorticoid receptor (NR3C1) as its target. Drugs of this class have anti-inflammatory and immunosuppressive activity.

Alopecia areata is a T-cell-mediated autoimmune disease in which immune cells attack the hair follicle. Topical corticosteroids are an established treatment class for it, because they suppress the inflammation around the follicle. The drug's original indications (eczema, dermatitis, lupus erythematosus and others) are also inflammatory or immune-driven skin diseases. This makes the prediction mechanistically consistent. Note that this link rests on the general class mechanism, not on drug-specific mechanism data.

Other predictions for this drug are weaker. Alopecia mucinosa, folliculitis decalvans and primary cutaneous B-cell lymphoma have some plausibility but no direct evidence. Predictions for genetic hair disorders and for telogen effluvium have little mechanistic support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11030789](https://pubmed.ncbi.nlm.nih.gov/11030789/) | 2000 | RCT | Archives of Dermatology | Randomized, double-blind, placebo-controlled trial of 0.25% desoximetasone cream in alopecia areata (no abstract available, so results are not summarized here) |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02221918 | TOPICORT | Not specified | Not specified |
| 02221926 | TOPICORT | Not specified | Not specified |
| 02221934 | TOPICORT | Not specified | Not specified |
| 02221896 | TOPICORT | Not specified | Not specified |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not from label text): hypopituitarism and related pituitary hormone deficiencies, hypogonadotropic hypogonadism (including Kallmann syndrome), Sheehan syndrome, thymus gland disease, skin atrophy, and peripheral vascular or arterial disease. These should be checked against the official product monograph.
- **Drug Interactions**: The interaction query returned only a pharmacological target record (glucocorticoid receptor, NR3C1). No drug-drug interactions were identified.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One randomized, double-blind, placebo-controlled trial of desoximetasone 0.25% cream in alopecia areata exists, and the mechanism fits the known class action of topical corticosteroids. However, the trial's results could not be reviewed, no clinical trials are registered, and the safety data are incomplete. The other nine predicted indications have prediction-only or indirect evidence and should stay on Hold.

**To proceed, the following is needed:**
- Review of the full text of the 2000 RCT (PMID 11030789) to confirm efficacy, effect size and safety
- Health Canada product monograph warnings and contraindications (a blocking gap for safety screening)
- Dosage form and approved indication details for the four TOPICORT DINs
- Confirmation that the available strengths and formulations suit scalp or hair-bearing skin
- Drug-specific mechanism of action data
- A monitoring plan for local adverse effects such as skin atrophy, and for systemic absorption with prolonged use

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Topicort (desoximetasone) prescribing information, Sun Pharmaceutical Industries, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e417856a-b760-4626-bc34-8e4bc62c026c) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

