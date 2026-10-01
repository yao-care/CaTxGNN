---
layout: default
title: Nafarelin
parent: Model Prediction Only (L5)
nav_order: 635
evidence_level: L5
indication_count: 10
---

# Nafarelin
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

# Nafarelin: From GnRH Agonist Therapy (Original Indication Not Recorded) to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Nafarelin is a GnRH (gonadotropin-releasing hormone) agonist that suppresses sex hormones, and the Evidence Pack does not record its original indication.
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita** with a very high score, but **0 clinical trials** and **0 publications** support this specific prediction. It is a model output only, and the mechanism does not appear plausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Evidence Pack (the Canadian license entry has no indication text) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.87% (model rank 3224) |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Nafarelin is known as a GnRH agonist. Continuous exposure desensitizes pituitary GnRH receptors and lowers LH/FSH and gonadal sex steroids.

Ambras syndrome is a congenital disorder of hair follicle development. No plausible mechanism links GnRH receptor agonism or gonadal steroid suppression to it. The high TxGNN score is most likely an artifact of knowledge-graph topology, not a pharmacological signal. This prediction is not supported.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Other Predictions in This Pack

The other nine predictions are also model-driven, and only two have any supporting information. These are the ones that matter for follow-up:

| Predicted Indication | TxGNN Score | Evidence | Assessment |
|------|------|------|------|
| Physiological sexual disorder | 99.75% | L4, 1 publication ([PMID 7951404](https://pubmed.ncbi.nlm.nih.gov/7951404/), 1994, nafarelin vs danazol for endometriosis pain) | The paper is about endometriosis, an established GnRH agonist use, and relates to the predicted term only indirectly (dyspareunia). Hypoestrogenism may worsen sexual function. This is not a new repurposing signal. |
| Central precocious puberty 1 | 99.70% | L5, no evidence supplied | The mechanism is strong, but nafarelin is generally understood to be already labeled for this use. It is probably a rediscovery of an on-label indication, to be verified against the current label. |
| Malformation syndrome with odontal/periodontal component | 99.77% | 20 retrieved publications, all general periodontitis literature | None mentions nafarelin or GnRH agonists. These are keyword matches and are not drug-specific evidence. |
| Pelvic organ prolapse | 99.77% | None | Estrogen deprivation may weaken pelvic floor tissue, so harm cannot be excluded. |

The remaining predictions (hypertrichosis, Dandy-Walker malformation syndrome, female genital tuberculosis, isolated genetic hair shaft abnormality, cervical dysplasia) have no evidence and no plausible mechanism.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2188783 | SYNAREL |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no trials, no literature, and no plausible mechanism, so it is treated as a knowledge-graph artifact. The only predictions with a credible mechanistic basis (central precocious puberty) or indirect clinical data (sexual disorder, via endometriosis pain) either appear to be on-label uses or are not true repurposing signals.

**To proceed, the following is needed:**
- Health Canada package insert (indications, warnings, contraindications), which is also needed to confirm the original indication
- Mechanism of action data from DrugBank
- Confirmation of whether central precocious puberty is already a labeled indication
- If pursuing the sexual-disorder signal, a dedicated study with a specific endpoint such as dyspareunia, with attention to hypoestrogenic adverse effects

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

