---
layout: default
title: Finasteride
parent: Model Prediction Only (L5)
nav_order: 387
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-28
description: "Finasteride: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Benign prostatic hyperplasia"
monitor_inn: "FINASTERIDE"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly"]
---

# Finasteride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Finasteride: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita
{: .text-alpha }

## One-Sentence Summary

Finasteride was originally used to treat benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, but **no clinical trials and no publications** currently support this prediction.
The result is a model-based signal only, and it needs careful scrutiny before any further investment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses on record: at least 20) |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, finasteride inhibits type II 5-alpha-reductase, which lowers dihydrotestosterone (DHT) in androgen-sensitive tissue. This is the basis of its use in BPH.

Ambras syndrome is a congenital hypertrichosis caused by genomic rearrangements affecting TRPS1 regulation, not by androgen excess. Lowering DHT would therefore not be expected to address the underlying cause. The mechanistic link is weak. The very high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other predictions in the same list show a similar pattern:

- **Hypertrichosis (rank 2):** Finasteride plausibly helps androgen-dependent hair conditions such as hirsutism and androgenetic alopecia. Non-androgen-dependent hypertrichosis does not follow this pathway, so the link is only partial.
- **Malformation syndromes with a dental component, Dandy-Walker malformation syndromes, isolated genetic hair shaft abnormality and familial isolated trichomegaly (ranks 3–6):** No plausible mechanism is evident, and no trials or literature were found.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Ambras type hypertrichosis universalis congenita.

---

## Literature Evidence

Currently no related literature available for the top predicted indication.

For context, the second-ranked prediction, hypertrichosis, has four publications. All are narrative reviews or methods papers, so they provide indirect background only and no controlled evidence of benefit:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12942187](https://pubmed.ncbi.nlm.nih.gov/12942187/) | 2003 | Review | Der Hautarzt | Overview of hair disease therapy: finasteride for male pattern hair loss, laser hair removal for hypertrichosis and hirsutism |
| [12223963](https://pubmed.ncbi.nlm.nih.gov/12223963/) | 2002 | Review | Ann Dermatol Venereol | Work-up and treatment of adult hirsutism and hypertrichosis; hypertrichosis occurs in non-androgen-dependent areas and is often iatrogenic or metabolic |
| [10330884](https://pubmed.ncbi.nlm.nih.gov/10330884/) | 1999 | Review | Ther Umsch | Treatment advances in androgenetic alopecia and hirsutism |
| [12444520](https://pubmed.ncbi.nlm.nih.gov/12444520/) | 2002 | Methods paper | Der Hautarzt | TrichoScan digital hair analysis tool; not a clinical study of finasteride |

---

## Canada Market Information

Finasteride has 20 valid single-ingredient licenses in Canada, with no cancelled licenses. Dosage form and indication text are not available in the data compiled for this report. Main authorizations:

| DIN | Product Name |
|---------|------|
| 02238213 | PROPECIA |
| 02339471 | SANDOZ FINASTERIDE A |
| 02322579 | SANDOZ FINASTERIDE |
| 02348500 | TEVA-FINASTERIDE |
| 02310112 | PMS-FINASTERIDE |

---

## Safety Considerations

- **Contraindications (from the TxGNN model (deep learning), not label text; may reflect similarities the model learned between related diseases, not biological evidence):** liver disease and gallbladder disease.
- **Pregnancy:** Finasteride carries a risk of feminizing male fetuses. Any use in developmental or congenital conditions is therefore inappropriate.
- **Drug Interactions:** A screening query returned 100 potential interacting drugs, but none has an assigned severity level. Examples include calcitriol, doxycycline, bupropion, metformin, omeprazole, morphine and acetylsalicylic acid. The list needs clinical review before drawing conclusions.

Please refer to the package insert for complete warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high model score. There are no trials or publications, and the biology does not fit: Ambras syndrome is not driven by DHT. The mechanistic link is also weak for the other top predictions.

**To proceed, the following is needed:**
- Mechanism of action data and a documented biological rationale linking 5-alpha-reductase inhibition to TRPS1-related hypertrichosis
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Dosage form and approved indication details for the Canadian licenses
- Severity grading and clinical review of the drug interaction list
- A targeted literature search for finasteride in congenital hypertrichosis
- Consideration of hypertrichosis or other androgen-dependent hair conditions as better-supported alternatives, with the caveat that hirsutism evidence should not be extrapolated to hypertrichosis without a clear rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

