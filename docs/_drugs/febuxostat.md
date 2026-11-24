---
layout: default
title: Febuxostat
parent: Moderate Evidence (L3-L4)
nav_order: 377
evidence_level: L4
indication_count: 3
last_modified_at: 2026-11-24
description: "Febuxostat: predicted new indication Hypouricemia, renal (evidence level L4). Approved use: Hyperuricemia"
monitor_inn: "FEBUXOSTAT"
predicted_indications: ["hypouricemia, renal", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "Lesch-Nyhan syndrome"]
---

# Febuxostat
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

## Febuxostat: From Hyperuricemia to hypouricemia, renal
{: .text-alpha }

## One-Sentence Summary

Febuxostat is a xanthine oxidase inhibitor originally used to treat hyperuricemia.
The TxGNN model predicts it may be effective for **renal hypouricemia**, but only **1 clinical trial** (of low relevance) and **2 publications** are linked to this prediction.
The mechanistic reasoning argues against the prediction, so it is best treated as a likely model artefact rather than a real therapeutic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperuricemia |
| Predicted New Indication | Hypouricemia, renal |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L4 |
| Canada Market Status | Marketed (marketed DINs: 6 of 6) |
| Number of DINs | 6 (marketed: 6) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for febuxostat: "ULORIC, a xanthine oxidase inhibitor, achieves its therapeutic effect by decreasing serum uric acid. ULORIC is not expected to inhibit other enzymes involved in purine and pyrimidine synthesis and metabolism at therapeutic concentrations." ([DailyMed: Uloric (febuxostat) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=54de10ef-fe5f-4930-b91d-6bbb04c664bd), label version 2025-12-24; accessed 2026-11-19.) Based on known pharmacology, febuxostat is a non-purine selective xanthine oxidase inhibitor that lowers serum uric acid, and its efficacy in hyperuricemia is established.

Renal hypouricemia is the opposite problem. Serum uric acid is already low because the kidney reabsorbs urate poorly (for example, loss of function in URAT1/SLC22A12 or GLUT9/SLC2A9). Lowering urate further has no mechanistic therapeutic rationale and could be harmful. The high TxGNN score most likely reflects a network association with uric acid metabolism rather than a true treatment signal, which may be a directionality error.

The only link in the literature is indirect. One case report describes using a xanthine oxidoreductase inhibitor, febuxostat, to try to prevent exercise-induced acute kidney injury, a complication of renal hypouricemia, in a young athlete. This is a prevention concept, not treatment of the underlying condition.

**Other predictions in the data (for context):**
- **Partial HPRT deficiency** (score 0.9998): Purine overproduction causes hyperuricemia and juvenile gout. Xanthine oxidase inhibition is mechanistically plausible, and febuxostat could be an alternative for patients who cannot tolerate allopurinol. Evidence consists of case reports only.
- **Lesch-Nyhan syndrome** (score 0.9968): Urate lowering may help the metabolic and renal problems, but it does not address the neurological and behavioural features. Evidence is limited to case-level reports, and pediatric use would be off-label.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Phase 4 | Unknown | 100 | Prospective controlled study of how uric acid control affects stone recurrence and renal function in patients with calculi and hyperuricemia. Relevance to renal hypouricemia could not be verified, so it is not direct evidence. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | Narrative review of hypouricemia (serum urate < 2 mg/dL) for rheumatologists, covering its causes. |
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Case report (indexed as review) | Internal Medicine | A 16-year-old footballer with familial renal hypouricemia (URAT1 mutations) and recurrent exercise-induced acute kidney injury; a xanthine oxidoreductase inhibitor (febuxostat) was explored as prophylaxis when hydration failed. |

---

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02466198 | TEVA-FEBUXOSTAT | FEBUXOSTAT (FEBUXOSTAT HEMIHYDRATE) | Marketed |
| 02473607 | MAR-FEBUXOSTAT | FEBUXOSTAT (FEBUXOSTAT HEMIHYDRATE) | Marketed |
| 02490870 | JAMP FEBUXOSTAT | FEBUXOSTAT | Marketed |
| 02533243 | AURO-FEBUXOSTAT | FEBUXOSTAT (FEBUXOSTAT HEMIHYDRATE) | Marketed |
| 02539837 | FEBUXOSTAT | FEBUXOSTAT (FEBUXOSTAT HEMIHYDRATE) | Marketed |
| 02549425 | M-FEBUXOSTAT | FEBUXOSTAT (FEBUXOSTAT HEMIHYDRATE) | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

<!-- review:begin ca-lic-20261124b-febuxostat-1 -->

> **Review correction (2026-11-24)**: Originally stated: "A sixth authorization, M-FEBUXOSTAT (DIN 02549425), is also valid." Removed: it referred to the earlier licence table, which showed only some of the DINs (for example "the sixth", "the remaining …", "shown here"). The table under Canada Market Information is now generated from the Health Canada DPD data and lists every DIN in the data with its current status. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261124b-febuxostat-1 -->

All six are single-ingredient products.

---

## Safety Considerations

**Disease-level contraindication signals (from the knowledge graph, not label text):** stroke and cerebrovascular disorders, cerebral infarction, myocardial infarction, coronary thrombosis, and hemoglobinopathy. These should be checked against the official labelling.

**Drug Interactions:** 22 interactions were recorded, including 4 or more rated **Major**:
- Mercaptopurine
- Azathioprine
- Leflunomide
- Teriflunomide

Moderate interactions include:
- Theophylline-type drugs (theophylline, dyphylline, aminophylline, oxtriphylline)
- Methotrexate
- Tioguanine
- Clofarabine
- Asparaginase and pegaspargase
- Interferon beta products
- Epirubicin
- Trabectedin
- Brentuximab vedotin
- Naltrexone

Please refer to the package insert for warnings and label contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication, renal hypouricemia, is mechanistically contradictory because it is a condition of already low urate. The supporting evidence is a single low-relevance trial and indirect literature, so the high TxGNN score is likely a network artefact.

**To proceed, the following is needed:**
- Confirmation that the prediction is not a directionality error
- Official Health Canada package insert warnings and contraindications
- Mechanism of action data
- If a related direction is pursued, consider the HPRT-deficiency spectrum (partial HPRT deficiency, Lesch-Nyhan syndrome) as a better-supported research question. Both rest on case reports only, and xanthine stone risk and pediatric safety would need evaluation.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Uloric (febuxostat) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=54de10ef-fe5f-4930-b91d-6bbb04c664bd) |
| 2026-11-24 | Removed: "A sixth authorization, M-FEBUXOSTAT (DIN 02549425), is also valid." | Corrected | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

