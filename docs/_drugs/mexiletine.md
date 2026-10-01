---
layout: default
title: Mexiletine
parent: Model Prediction Only (L5)
nav_order: 607
evidence_level: L5
indication_count: 10
---

# Mexiletine
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

# Mexiletine: From Ventricular Arrhythmia to Hypertrichosis

## One-Sentence Summary

Mexiletine is a class IB antiarrhythmic that blocks voltage-gated sodium channels. The Canadian licence records supplied do not state its approved indication, so the original use is inferred from its drug class.
The TxGNN model ranks **hypertrichosis** as its top prediction, but this signal rests on the model alone, with **0 clinical trials** and **0 publications** supporting it.
The best-supported prediction for this drug is actually **headache disorder** (rank 10), which has only small open-label studies and case series.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied licence data (inferred: ventricular arrhythmia, from drug class) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Mexiletine belongs to the class IB antiarrhythmics, which act by blocking sodium channels. Its efficacy in ventricular arrhythmias is established, but nothing in the supplied data links sodium channel blockade to hair growth regulation.

The hypertrichosis prediction looks like a graph-proximity artefact. Three other hair-related nodes also appear among the top-ranked predictions: Ambras-type hypertrichosis universalis congenita (rank 3), isolated genetic hair shaft abnormality (rank 7), and hypertrichosis itself (rank 1). Together they suggest one cluster of related nodes rather than independent signals. No mechanism is supported for any of them.

By contrast, headache disorder is mechanistically plausible: sodium channel blockade may reduce trigeminal neuronal excitability. Mexiletine and IV lidocaine have been reported in refractory headache and trigeminal autonomic cephalalgias.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for hypertrichosis. No trials were registered for any of the other nine predicted indications either.

---

## Literature Evidence

Currently no related literature available for hypertrichosis.

Among the other predicted indications, only headache disorder has mexiletine-specific literature. All of it is low-grade evidence: no randomized trials, only small open-label studies, case series and reviews.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20425204](https://pubmed.ncbi.nlm.nih.gov/20425204/) | 2010 | Review / case series | Curr Pain Headache Rep | IV lidocaine and mexiletine used in trigeminal autonomic cephalalgias, with a rationale from their benefit in neuropathic pain |
| [33361408](https://pubmed.ncbi.nlm.nih.gov/33361408/) | 2021 | Open-label study with single-arm meta-analysis | J Neurol Neurosurg Psychiatry | Medical treatment of SUNCT/SUNA; the mexiletine-specific content is not confirmed from the title |
| [18793209](https://pubmed.ncbi.nlm.nih.gov/18793209/) | 2008 | Case series (9 patients) | Headache | Mexiletine in refractory chronic daily headache |
| [6938859](https://pubmed.ncbi.nlm.nih.gov/6938859/) | 1981 | Clinical report | N Z Med J | Mexiletine in vascular headaches |

The periodontitis records retrieved for the rank 4 malformation syndrome do not mention mexiletine and are not counted as evidence.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02536846 | MINT-MEXILETINE | Not listed | Not listed |
| 02536854 | MINT-MEXILETINE | Not listed | Not listed |
| 02230359 | TEVA-MEXILETINE | Not listed | Not listed |
| 02230360 | TEVA-MEXILETINE | Not listed | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information.

The supplied data contain no warnings, contraindications or drug-interaction records for mexiletine. The review notes attached to the headache prediction flag cardiac proarrhythmia and GI/CNS tolerability as topics for a safety review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, hypertrichosis, is supported only by the model score, with no trials, no literature and no plausible mechanism. Evidence level is L5. Nine of the ten predictions have no mexiletine-specific evidence beyond the score.

**To proceed, the following is needed:**
- Health Canada package insert data: approved indications, warnings and contraindications. Without them, safety screening (S1) cannot start.
- Mechanism of action data from DrugBank to allow a proper mechanistic-link analysis.
- For the better-supported **headache disorder** candidate, a separate review as a research question. This should confirm the mexiletine-specific content of the SUNCT/SUNA meta-analysis and the design of the lidocaine/mexiletine study. It should also include a cardiac safety assessment before any prospective study.
- Dosage form and indication text for the four DINs, which are missing from the licence records.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

