---
layout: default
title: Sevoflurane
parent: Model Prediction Only (L5)
nav_order: 715
evidence_level: L5
indication_count: 10
---

# Sevoflurane
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

# Sevoflurane: From General Anesthesia to Prinzmetal Angina

## One-Sentence Summary

Sevoflurane is a halogenated inhalational agent used internationally for induction and maintenance of general anesthesia. The TxGNN model's top-ranked prediction is **Prinzmetal angina** (score 99.78%, global rank 4,874), but this is supported by **zero clinical trials and zero publications** — a pure computational hypothesis with no real-world evidence. Across all 10 predicted indications in this pack, none reach a clinically credible evidence level.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no Canada licence on file); sevoflurane is internationally indicated for induction/maintenance of general anesthesia |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.78% (global rank 4,874 of all candidates) |
| Evidence Level | L5 (model prediction only, no clinical or mechanistic study) |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002). Based on known information, sevoflurane is a halogenated inhalational general anesthetic whose efficacy in inducing and maintaining general anesthesia is well established. The evidence pack's own rationale proposes a theoretical link to Prinzmetal angina via coronary vasodilation and ischemic-preconditioning-like myocardial protection — but this is explicitly flagged as speculative, with **no clinical or mechanistic literature to support it**.

More importantly, this pattern repeats across the other 9 candidates. Where literature does exist (fibromyalgia, tendinitis, migraine, inclusion body myositis), it consistently describes **how to safely anesthetize patients who already have the disease** (e.g., "Anesthetic Management for a Patient with Fibromyalgia," "Anesthetic Considerations of Sporadic Inclusion Body Myositis") — not sevoflurane being used to *treat* that disease. Similarly, the one clinical trial retrieved (NCT03789370) compares sevoflurane vs. propofol for **postoperative headache incidence**, not migraine treatment. This is a known TxGNN failure mode: co-occurrence in "anesthesia for disease X" literature is being misread as a treatment signal for disease X.

Given this, none of the 10 ranked candidates currently justify further investment without independent mechanistic validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Sevoflurane has no marketing authorization on file in this evidence pack — market status is **Not Marketed**, with **0 DINs**. There is no domestic regulatory foothold to build a repurposing case on.

---

## Safety Considerations

Warning, contraindication, and drug-interaction data are not yet available in this evidence pack (DG001 — source: TFDA package insert, pending retrieval and parsing). This is classified as a **Blocking** severity gap and must be resolved before the candidate can enter S1 safety review, independent of the indication-level evidence quality.

---

## Full List of Predicted Indications (Ranks 1–10)

For transparency, all 10 candidates in this pack show the same weak-evidence pattern:

| Rank | Disease | TxGNN Score | Evidence Level | Evidence Summary |
|------|---------|-------------|-----------------|-------------------|
| 1 | Prinzmetal angina | 99.78% | L5 | No trials, no literature — pure model prediction |
| 2 | Tourette syndrome | 99.50% | L5 | No trials, no literature — pure model prediction |
| 3 | Fibromyalgia | 99.42% | L4 | 1 case report on anesthetizing an FM patient (not FM treatment) |
| 4 | Tendinitis | 99.41% | L4 | 11 papers, all on perioperative anesthesia for tendon/orthopedic surgery, not tendinitis treatment |
| 5 | Idiopathic granulomatous myositis | 99.41% | L5 | No trials, no literature |
| 6 | Myositis fibrosa | 99.41% | L5 | No trials, no literature |
| 7 | Nephrogenic SIAD | 99.40% | L5 | No trials, no literature |
| 8 | Trichotillomania | 99.33% | L5 | No trials, no literature |
| 9 | Migraine disorder | 99.23% | L4 | 1 trial on postoperative headache (side effect, not migraine treatment) + 1 pediatric MRI sedation cohort |
| 10 | Inclusion body myositis | 99.09% | L4 | 1 case report on anesthetizing an IBM patient (not IBM treatment) |

All 10 candidates carry a system recommendation of **Hold**.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- None of the 10 TxGNN-predicted indications have genuine supporting evidence — the top candidate is model-prediction-only (L5), and where literature exists for other candidates, it reflects "anesthesia for a patient with disease X" rather than "sevoflurane as treatment for disease X."
- A **blocking** safety data gap (DG001 — TFDA warnings/contraindications) independently prevents entry into S1 review.
- Sevoflurane is not marketed in Canada (0 DINs), leaving no domestic regulatory basis to build on.

**To proceed, the following is needed:**
- Retrieve and parse the TFDA package insert for warnings/contraindications (resolves DG001, blocking)
- Query DrugBank API for mechanism of action data (resolves DG002)
- Independent pharmacology review of the coronary-vasodilation hypothesis before investing further in the Prinzmetal angina candidate
- Re-run evidence classification with filters that exclude "anesthetic management of patients with disease X" papers, which are being systematically conflated with therapeutic evidence across this drug's candidate list
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

