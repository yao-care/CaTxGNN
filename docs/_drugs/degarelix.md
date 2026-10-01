---
layout: default
title: Degarelix
parent: Model Prediction Only (L5)
nav_order: 256
evidence_level: L5
indication_count: 10
---

# Degarelix
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

# Degarelix: From Advanced Prostate Cancer to Hypertrichosis

## One-Sentence Summary

Degarelix (marketed as FIRMAGON) is a GnRH receptor antagonist, generally used for hormone-dependent prostate cancer. The TxGNN model predicts it may be effective for **hypertrichosis** with a very high score, but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it is a model output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Advanced prostate cancer (general drug knowledge; no approved indication text is present in the Canadian licence data provided) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Degarelix blocks the GnRH receptor, which lowers LH, FSH and gonadal androgens. Detailed mechanism data were not supplied with this evidence pack, so this description reflects the known drug class.

This mechanism could help only androgen-driven hair growth (hirsutism). Hypertrichosis is generally not androgen-dependent, so the link is weak. The 99.99% score comes from graph-based similarity in the knowledge graph, not from clinical observation, and should be read as a hypothesis-generating signal rather than support.

The other nine predictions have the same problem. Most are genetic or structural conditions with no hormonal mechanism: Ambras syndrome, Dandy-Walker malformation syndromes, hair shaft abnormalities, trichomegaly. Two are mast-cell mediated (allergic and cold urticaria). Degarelix is known to cause injection-site and hypersensitivity reactions, so it may worsen rather than treat allergic conditions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for hypertrichosis.

Note: 20 publications were retrieved for the rank 4 prediction (malformation syndrome with periodontal component). They are general periodontitis papers (guidelines, reviews, diabetes association). None mentions degarelix or GnRH antagonism, so they are keyword matches and not evidence for this drug.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2337029 | FIRMAGON |
| 2337037 | FIRMAGON |

Dosage form and approved indication text were not available in the licence data.

---

## Other Predicted Indications

| Rank | Predicted Indication | TxGNN Score | Evidence | Assessment |
|------|------|------|------|------|
| 1 | Hypertrichosis | 99.99% | None | Weak link; hair growth is generally not androgen-driven |
| 2 | Ambras type hypertrichosis universalis congenita | 99.98% | None | Genetic; no plausible mechanism |
| 3 | Syndrome with Dandy-Walker malformation | 99.98% | None | Structural anomaly; no mechanism |
| 4 | Malformation syndrome with periodontal component | 99.98% | Irrelevant keyword matches | No mechanism |
| 5 | Isolated genetic hair shaft abnormality | 99.98% | None | Gene-driven, not hormone-responsive |
| 6 | Allergic urticaria | 99.97% | None | Mast-cell/IgE mediated; drug may cause hypersensitivity |
| 7 | Cold urticaria | 99.86% | None | No GnRH-related mechanism |
| 8 | Familial male-limited precocious puberty | 99.84% | None | Driven by LHCGR mutations, independent of GnRH |
| 9 | Central precocious puberty 1 | 99.67% | None | **Most plausible**; GnRH-dependent, so suppressing the axis is the established principle |
| 10 | Familial isolated trichomegaly | 99.65% | None | Genetic; no mechanism |

Central precocious puberty (rank 9) is the only candidate with a credible mechanism, since GnRH agonists are already used for it. Practical barriers remain: the monthly depot injection, formulation and dosing, and the absence of pediatric data. It is flagged as a **Research Question**, meaning a literature and feasibility review is warranted before any further step.

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction records were found in the query.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (hypertrichosis) rests on a model score alone, with no trials, no literature, and a weak mechanistic link. The same holds for nine of the ten candidates. Only central precocious puberty has a plausible mechanism, and it merits a feasibility review rather than a Go decision.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmed approved indication text and dosage forms for both DINs
- Mechanism of action data from DrugBank
- A targeted literature and feasibility review for central precocious puberty, covering pediatric data, depot formulation and dosing
- Confirmation that the hypertrichosis and other low-plausibility candidates have no androgen-driven component before any further investigation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

