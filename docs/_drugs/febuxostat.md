---
layout: default
title: Febuxostat
parent: Moderate Evidence (L3-L4)
nav_order: 377
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-13
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

# Febuxostat: From Hyperuricemia to Renal Hypouricemia

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
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, febuxostat is a non-purine selective xanthine oxidase inhibitor that lowers serum uric acid, and its efficacy in hyperuricemia is established.

Renal hypouricemia is the opposite problem. Serum uric acid is already low because the kidney reabsorbs urate poorly (for example, loss of function in URAT1/SLC22A12 or GLUT9/SLC2A9). Lowering urate further has no mechanistic therapeutic rationale and could be harmful. The high TxGNN score most likely reflects a network association with uric acid metabolism rather than a true treatment signal, which may be a directionality error.

The only link in the literature is indirect. One case report describes using a xanthine oxidoreductase inhibitor, febuxostat, to try to prevent exercise-induced acute kidney injury, a complication of renal hypouricemia, in a young athlete. This is a prevention concept, not treatment of the underlying condition.

**Other predictions in the data (for context):**
- **Partial HPRT deficiency** (score 99.98%): Purine overproduction causes hyperuricemia and juvenile gout. Xanthine oxidase inhibition is mechanistically plausible, and febuxostat could be an alternative for patients who cannot tolerate allopurinol. Evidence consists of case reports only.
- **Lesch-Nyhan syndrome** (score 99.68%): Urate lowering may help the metabolic and renal problems, but it does not address the neurological and behavioural features. Evidence is limited to case-level reports, and pediatric use would be off-label.

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

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02466198 | TEVA-FEBUXOSTAT | Not specified | Not specified |
| 02490870 | JAMP FEBUXOSTAT | Not specified | Not specified |
| 02473607 | MAR-FEBUXOSTAT | Not specified | Not specified |
| 02533243 | AURO-FEBUXOSTAT | Not specified | Not specified |
| 02539837 | FEBUXOSTAT | Not specified | Not specified |

A sixth authorization, M-FEBUXOSTAT (DIN 02549425), is also valid. All six are single-ingredient products.

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

