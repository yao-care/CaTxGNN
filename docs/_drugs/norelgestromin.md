---
layout: default
title: Norelgestromin
parent: Model Prediction Only (L5)
nav_order: 664
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Norelgestromin: predicted new indication Amenorrhea (evidence level L5). Approved use: Not stated in the Health Canada licence data compiled for this report…"
---

# Norelgestromin
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

# Norelgestromin: From Hormonal Contraception to Amenorrhea

## One-Sentence Summary

Norelgestromin is a progestin used in a transdermal contraceptive patch (marketed in Canada as EVRA).
The TxGNN model predicts it may be useful for **amenorrhea**,
but there are currently **no clinical trials** and **no publications** supporting this direction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Health Canada licence data compiled for this report (the product is a transdermal contraceptive patch) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, norelgestromin is the active progestin metabolite of norgestimate and is delivered through a transdermal patch, usually combined with ethinyl estradiol. As a progestin, it suppresses the hypothalamic-pituitary-ovarian axis and causes changes in the endometrium.

Progestins are mechanistically plausible for some forms of amenorrhea, for example inducing withdrawal bleeding in estrogen-primed patients or protecting the endometrium. This link is inferred from the drug class and the model score, and it has not been verified for this specific drug.

One caution applies: hormonal contraceptives often *cause* amenorrhea or altered bleeding as a side effect. This may inflate the knowledge-graph association without reflecting a true therapeutic use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02248297 | EVRA | Not specified | Not specified |

## Safety Considerations

- **Drug Interactions**: One interaction is on record: **Sugammadex** (Major severity).
- **Disease contraindications from the knowledge graph** (derived from drug-disease relationships in the model's knowledge base, not from package insert text). Listed conditions include:
  - Cardiovascular and metabolic: hypertension, coronary artery disease, thrombophlebitis, diabetes mellitus, diabetic ketoacidosis, hyperglycemia, hyperlipidemia, familial hyperlipidemia, hypertriglyceridemia
  - Hepatic and renal: liver disease, gallbladder disease, kidney disease
  - Neurological and psychiatric: epilepsy, migraine disorder, anxiety disorder, neurotic disorder, dysthymic disorder
  - Other: female breast carcinoma, systemic lupus erythematosus, asthma, porphyria (including inherited forms)

Please refer to the package insert for confirmed warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (L5), with no registered trials or publications. The apparent link to amenorrhea may reflect a side effect of hormonal contraception rather than a treatment benefit. Label-based safety information is also missing.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data for norelgestromin (for example from DrugBank)
- Original indication and dosage form details from the licence record
- A literature and trial search to separate therapeutic use in amenorrhea from amenorrhea as a side effect
- Assessment of whether the transdermal patch route suits the target patient group
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

