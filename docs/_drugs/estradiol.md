---
noindex: true
sitemap: false
layout: default
title: Estradiol
parent: Model Prediction Only (L5)
nav_order: 355
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Estradiol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **0** 
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

## Estradiol: Evaluation Incomplete — No Predicted Indications Available
{: .text-alpha }

## One-Sentence Summary

Estradiol (DB00783) is a naturally occurring steroidal estrogen hormone with well-established clinical use in hormone replacement therapy, hypogonadism, and reproductive health.
This Evidence Pack contains **no TxGNN predicted indications**, which means no repurposing hypothesis can be evaluated at this stage.
All downstream evidence layers — clinical trials, literature, and safety data — are also absent, making a repurposing assessment impossible until data gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in this Evidence Pack |
| Predicted New Indication | No predictions available |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — no supporting studies available |
| Canada Market Status | Marketed (marketed DINs on record: at least 20) |
| Number of DINs | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

No predicted indications were included in this Evidence Pack, so no repurposing hypothesis can be assessed for mechanistic plausibility.

Detailed mechanism of action data is also not available in this submission. Based on general pharmacological knowledge, Estradiol is the principal endogenous estrogen — a steroid hormone that binds to nuclear estrogen receptors (ERα and ERβ), regulating transcription of genes involved in reproduction, bone metabolism, cardiovascular function, and the central nervous system. It is the primary circulating estrogen during the reproductive years.

Without a TxGNN prediction target, it is not possible to evaluate whether this mechanism would be applicable to any new indication. A complete prediction run is required before mechanistic analysis can proceed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in this Evidence Pack.

---

## Literature Evidence

Currently no related literature available in this Evidence Pack.

---

## Canada Market Information

No product-level data is available for review.

<!-- review:begin ca-lic-20261105-estradiol-1 -->

> **Review correction (2026-11-05)**: Originally stated: "Estradiol has no recorded Health Canada authorizations in this Evidence Pack (0 DINs). No product-level data is available for review." Removed: the number or status of DINs stated here did not match the Health Canada DPD data (the Health Canada Drug Product Database as of 2026-11-05). Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261105-estradiol-1 -->

> Note: Estradiol-containing products are commercially available in Canada under various brand names. Health Canada's Drug Product Database (DPD) should be consulted directly.

<!-- review:begin ca-lic-20261105-estradiol-2 -->

> **Review correction (2026-11-05)**: Originally stated: "> Note: Estradiol-containing products are commercially available in Canada under various brand names. The absence of records here likely reflects a data collection gap rather than a true regulatory absence." Removed: it conflicted with the Health Canada DPD data (the Health Canada Drug Product Database as of 2026-11-05). Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261105-estradiol-2 -->

---

## Safety Considerations

Please refer to the package insert for safety information.

> Two data gaps have been flagged in this Evidence Pack and must be resolved before safety evaluation can proceed:
> - **Package insert warnings and contraindications** — Blocking severity; required for S1 safety screening
> - **Mechanism of action (MOA)** — High severity; required for mechanistic plausibility analysis

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for Estradiol (DB00783) is structurally incomplete — the `predicted_indications` array is empty, which means there is no repurposing hypothesis to evaluate. Without a predicted target indication, all downstream sections (evidence, safety linkage, mechanistic justification) cannot be populated.

**To proceed, the following is needed:**

- **Run TxGNN prediction pipeline** to generate `predicted_indications` with disease targets and confidence scores
- **Retrieve MOA data from DrugBank API** (DG002 — High severity) to enable mechanism-based reasoning
- **Query Health Canada DPD** for Estradiol DIN records to populate the regulatory section
- **Re-run evidence collection** (ClinicalTrials.gov, PubMed) once a target indication is identified

<!-- review:begin ca-lic-20261105-estradiol-3 -->

> **Review correction (2026-11-05)**: Originally stated: "**Retrieve MOA data from DrugBank API** (DG002 — High severity) to enable mechanism-based reasoning / **Download and parse TFDA package insert PDF** for warnings and contraindications (DG001 — Blocking severity)" Removed: leftover template text about Taiwan's TFDA, which does not apply to this Canadian page. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261105-estradiol-3 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "Estradiol has no recorded Health Canada authorizations in this Evidence Pack (0 DINs)" | Corrected | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |
| 2026-11-05 | Removed: "The absence of records here likely reflects a data collection gap rather than a true regulatory absence" | Corrected | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |
| 2026-11-05 | Removed: "**Download and parse TFDA package insert PDF** for warnings and contraindications (DG001 — Blocking severity)" | Corrected | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

