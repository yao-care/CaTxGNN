---
layout: default
title: Indacaterol
parent: Model Prediction Only (L5)
nav_order: 472
evidence_level: L5
indication_count: 10
---

# Indacaterol
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

# Indacaterol: From Obstructive Airway Disease to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Indacaterol is an ultra-long-acting beta2-agonist (LABA). Its marketed products in Canada are used for obstructive airway disease. The source record lists no original indications, so this is inferred from the product names and the linked COPD and asthma trials.
The TxGNN model ranks **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)** as its top prediction with a very high graph score. This prediction has **0 clinical trials** and **0 publications** behind it, so it is a model output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the source data (inferred: COPD / asthma) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Based on known pharmacology, indacaterol is a beta2-adrenergic agonist. It relaxes airway smooth muscle through beta2-receptor and cAMP signaling, which gives sustained bronchodilation.

The prediction does not hold up mechanistically. NSIAD is caused by gain-of-function variants in the vasopressin V2 receptor gene (*AVPR2*). Beta2-agonism has no established link to this defect. The high score most likely reflects network proximity in the knowledge graph rather than a real therapeutic relationship. No trial or publication supports it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Other Predicted Indications

Nine further candidates were returned. Only one has any real evidence, and it is largely a confirmation of existing use.

| Rank | Predicted Indication | Score | Evidence Level | Decision | Comment |
|------|------|------|------|------|------|
| 2 | Headache disorder | 99.53% | L5 | Hold | The two linked trials are COPD studies. Headache is a common adverse event of inhaled beta2-agonists, so this is more likely a safety signal than a benefit. |
| 3 | Trigeminal autonomic cephalalgia | 99.33% | L5 | Hold | Graph prediction only. |
| 4 | Paratenonitis | 99.26% | L5 | Hold | No known link to beta2-agonism. |
| 5 | Calcific tendinitis | 99.25% | L5 | Hold | Graph prediction only. |
| 6 | Hypertrichosis | 99.23% | L5 | Hold | No plausible link. |
| 7 | Bronchial disease | 99.18% | L1 | Proceed with Guardrails | 37 trials and 20 publications. See below. |
| 8 | Myositis | 99.12% | L5 | Hold | Graph prediction only. |
| 9 | Anaphylaxis | 99.07% | L5 | Hold | Epinephrine is the standard treatment. Indacaterol's slow onset makes it unsuitable for acute use. |
| 10 | Ambras type hypertrichosis universalis congenita | 99.06% | L5 | Hold | Rare genetic disorder with no plausible link. |

**Rank 7, bronchial disease.** The support consists of the trials and papers below.
- **Large phase 3 RCTs:**
  - [NCT02571777](https://clinicaltrials.gov/study/NCT02571777): 52 weeks, n=3,092, indacaterol/glycopyrronium/mometasone vs indacaterol/mometasone in asthma.
  - [NCT02554786](https://clinicaltrials.gov/study/NCT02554786): n=2,216, indacaterol/mometasone vs mometasone.
  - [NCT03158311](https://clinicaltrials.gov/study/NCT03158311): n=1,426, non-inferiority vs a free triple combination.
- **Key publication:** the IRIDIUM RCT, [PMID 32653074](https://pubmed.ncbi.nlm.nih.gov/32653074/) (Lancet Respir Med, 2020).
- **Important caveats:**
  - COPD is already a labeled use, so this is mostly confirmation rather than true repurposing.
  - The asthma evidence applies to fixed-dose combinations with an inhaled corticosteroid (mometasone) and glycopyrronium.
  - LABA monotherapy is not appropriate in asthma because of the class boxed-warning risk.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2498685 | ATECTURA BREEZHALER |
| 2498707 | ATECTURA BREEZHALER |
| 2498693 | ATECTURA BREEZHALER |
| 2418282 | ULTIBRO BREEZHALER |
| 2501244 | ENERZAIR BREEZHALER |

The record does not include dosage forms or approved indication text for these licenses. Atectura and Enerzair are combination products with mometasone (Enerzair also contains glycopyrronium). Ultibro combines indacaterol with glycopyrronium.

---

## Safety Considerations

Please refer to the package insert for safety information.

As a class note from the evidence review, LABA monotherapy in asthma carries a boxed-warning class risk. Headache is a commonly reported adverse event of inhaled beta2-agonists.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, NSIAD, rests on a graph score alone. There are no trials or publications, and there is no credible mechanism linking beta2-agonism to a vasopressin V2 receptor gain-of-function disorder.

**To proceed, the following is needed:**
- Fill in the drug's original indication record, which is currently empty. This would clarify which predictions are true repurposing and which are existing uses.
- Obtain the mechanism of action data from DrugBank.
- Download and parse the Health Canada package insert to complete warnings and contraindications. This is currently a blocking gap for safety screening.
- If any follow-up is pursued, limit it to the labeled COPD use or ICS-containing asthma combinations (rank 7). Do not pursue NSIAD without new mechanistic or clinical evidence.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

