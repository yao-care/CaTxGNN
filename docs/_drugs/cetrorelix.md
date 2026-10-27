---
layout: default
title: Cetrorelix
parent: Model Prediction Only (L5)
nav_order: 178
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Cetrorelix: predicted new indication Hypertrichosis (evidence level L5). Approved use: Prevention of premature LH surges in women undergoing controlled ovar…"
monitor_inn: "CETRORELIX"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "persistent fetal circulation syndrome", "familial isolated trichomegaly", "familial male-limited precocious puberty", "aromatase excess syndrome", "centra precocious puberty 1"]
---

# Cetrorelix
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Cetrorelix: From Ovarian Stimulation Support to Hypertrichosis
{: .text-alpha }

## One-Sentence Summary

Cetrorelix is a GnRH (gonadotropin-releasing hormone) antagonist used in fertility treatment to prevent premature LH surges during controlled ovarian stimulation.
The TxGNN model predicts it may be effective for **hypertrichosis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
This prediction is based on model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prevention of premature LH surges in women undergoing controlled ovarian stimulation (the Health Canada licence text is not available; this is based on pharmacology reference data) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, cetrorelix blocks the GnRH1 receptor (encoded by *GNRHR*). This suppresses LH and FSH release and lowers downstream sex-steroid (androgen and estrogen) production.

In theory, lowering androgens could reduce androgen-driven hair growth (hirsutism). However, hypertrichosis is generally not androgen-dependent. It is often genetic or drug-induced, so the mechanistic link is speculative. The very high TxGNN score (99.98%) reflects proximity in the knowledge graph, not clinical support.

Other top-ranked predictions are also poorly supported mechanistically:
- **Ambras-type hypertrichosis, isolated hair shaft abnormalities, familial trichomegaly:** these are developmental or genetic hair disorders that GnRH antagonism does not address.
- **Dental/periodontal malformation syndromes, Dandy-Walker–related syndromes, persistent fetal circulation:** no plausible mechanism.
- **Familial male-limited precocious puberty, aromatase excess syndrome:** related to the sex-hormone axis but mismatched. The pathology lies downstream of the pituitary or outside the gonads.
- **Central precocious puberty (rank 10):** the most biologically credible prediction. The disease is driven by premature activation of the hypothalamic-pituitary-gonadal axis, and GnRH axis suppression is pharmacologically coherent. The standard of care, however, is GnRH agonists. No trial or literature data were supplied for cetrorelix in children, and its short-acting formulation limits practicality. It is flagged as a research question.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02247766 | CETROTIDE | Not specified | Not specified |

## Safety Considerations

- **Drug Interactions:** No drug-drug interactions were identified. The only record is pharmacological: cetrorelix acts on the human GnRH1 receptor and is used to inhibit premature LH surges in women undergoing controlled ovarian stimulation.

Please refer to the package insert for other safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational score, with no clinical trials or literature, and the mechanistic link to hypertrichosis is weak. Package-insert safety data have also not been obtained.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data (for example from DrugBank)
- Literature and trial searches for hypertrichosis, and separately for central precocious puberty, the most plausible candidate
- Assessment of route and formulation suitability, including pediatric suitability if central precocious puberty is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

