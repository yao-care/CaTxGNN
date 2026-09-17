---
layout: default
title: Prucalopride
parent: Model Prediction Only (L5)
nav_order: 658
evidence_level: L5
indication_count: 10
---

# Prucalopride
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

# Prucalopride: From Chronic Constipation (5-HT4 Agonist) to Amyloidosis-Related Gut Motility Dysfunction

> **Note on indication selection**: TxGNN's top-ranked hit (hypoalphalipoproteinemia, score 99.82%) and three of the next four candidates (homozygous familial hypercholesterolemia, duodenal ulcer, oral candidiasis, HIV, strongyloidiasis) have **zero clinical trial or literature support**, and the evidence pack itself flags them as likely knowledge-graph noise with no mechanistic plausibility. This report instead focuses on **amyloidosis** (rank 6), the highest-ranked candidate that is actually backed by literature and a coherent mechanistic hypothesis.

## One-Sentence Summary

Prucalopride's formal original-indication field is a data gap in this pack, but the model's own rationale identifies it as a selective 5-HT4 receptor agonist used for chronic bowel motility insufficiency (e.g., chronic constipation). TxGNN predicts potential relevance to **amyloidosis**-related gastrointestinal motility failure, but this is currently supported by only **2 case/cohort-level publications** and **no clinical trials**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Canadian regulatory data (drug not marketed in Canada); described in the model rationale as chronic constipation (5-HT4 agonist) |
| Predicted New Indication | Amyloidosis (gastrointestinal motility dysfunction) |
| TxGNN Prediction Score | 99.62% (rank 7664 of all candidates) |
| Evidence Level | L4 (case report / cohort-review only, no clinical trials) |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Prucalopride is not available in this evidence pack (formal `original_moa` field is a data gap). However, the model's repurposing rationale independently notes that Prucalopride is a selective 5-HT4 receptor agonist, clinically used to stimulate insufficient bowel motility (e.g., chronic constipation).

Amyloidosis can infiltrate the gastrointestinal autonomic nerves and smooth muscle, leading to impaired motility and, in severe cases, chronic intestinal pseudo-obstruction (CIPO). A prokinetic 5-HT4 agonist could plausibly address this downstream motility deficit — this is a reasonable pharmacological hypothesis, but it is an **external inference**, not something directly validated by trial data within this dataset.

Primary amyloidosis (rank 9) shares the same rationale and cites the same single publication, so it does not add independent evidentiary weight beyond the general amyloidosis candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40376135](https://pubmed.ncbi.nlm.nih.gov/40376135/) | 2025 | Case Report | Cureus | Case of amyloidosis presenting as chronic intestinal pseudo-obstruction in a 61-year-old man; extensive workup for vascular, paraneoplastic, infectious, and autoimmune causes failed to explain recurrent dilated small bowel and multiple non-diagnostic laparotomies. |
| [34231480](https://pubmed.ncbi.nlm.nih.gov/34231480/) | 2021 | Cohort/Review | Turkish Journal of Gastroenterology | Notes that specific GI motility disorders (gastroparesis, chronic intestinal pseudo-obstruction, colonic inertia) are commonly misdiagnosed as functional GI disorders due to low physician awareness in Asia; does not evaluate Prucalopride directly. |

## Canada Market Information

Prucalopride is not currently marketed in Canada — 0 DINs are registered in this evidence pack, so no approved-indication or product-level data is available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The amyloidosis link rests on a single case report and a review that doesn't test Prucalopride directly — no clinical trials exist for this pairing, and the drug's own safety/label data (TFDA warnings and contraindications) is marked as a **Blocking** data gap (DG001), which by itself prevents any safety-stage evaluation regardless of indication.

**To proceed, the following is needed:**
- TFDA/Health Canada product label data (warnings, contraindications) — currently Blocking gap (DG001)
- Confirmed original mechanism-of-action data from DrugBank (DG002)
- Dedicated preclinical or case-series research specifically evaluating Prucalopride for amyloidosis-associated GI motility failure
- If pursued, clarification of the Canadian access pathway given the drug's current "not marketed" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

