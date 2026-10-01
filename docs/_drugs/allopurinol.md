---
layout: default
title: Allopurinol
parent: Moderate Evidence (L3-L4)
nav_order: 37
evidence_level: L4
indication_count: 10
---

# Allopurinol
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Allopurinol: From Gout and Hyperuricemia to Hepatic Porphyria

## One-Sentence Summary

Allopurinol is a xanthine oxidase inhibitor, widely known as a treatment for gout and hyperuricemia. The TxGNN model predicts it may be effective for **hepatic porphyria**, but there are **0 clinical trials** and only **2 publications** on the topic. One is a hypothesis paper and the other is a rat study, and neither tests allopurinol as a therapy. The high model score is not backed by clinical evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout / hyperuricemia (general drug knowledge; the Canadian licence records provided contain no indication text) |
| Predicted New Indication | Hepatic porphyria |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 12 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Allopurinol is known to inhibit xanthine oxidase, which lowers uric acid production. That mechanism has no obvious direct link to porphyria.

The only mechanistic thread in the evidence is indirect. One hypothesis paper proposes that acute hepatic porphyrias could be treated by controlling 5-aminolevulinate synthase (ALAS1), the rate-limiting enzyme of heme synthesis, through the hepatic heme pool. This is a plausible but unproven connection to allopurinol.

The preclinical literature also raises a safety concern. Some drugs exacerbate hepatic porphyria by depleting the hepatic heme pool, and allopurinol may perturb hepatic heme and CYP turnover. It could therefore be porphyrinogenic rather than therapeutic. The very high TxGNN score most likely reflects knowledge-graph proximity, not demonstrated efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Review (hypothesis) | Medical Hypotheses | Proposes metabolic targeting of hepatic ALAS1, via tryptophan or inhibition of heme use by tryptophan 2,3-dioxygenase, as a therapy for acute hepatic porphyrias. Allopurinol is not shown to be effective. |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Preclinical (animal) | Biochemical Pharmacology | In rat liver, very low-dose carbamazepine depleted heme and exacerbated porphyria. It illustrates how a drug can worsen hepatic porphyria, but it does not test allopurinol as a treatment. |

---

## Canada Market Information

Health Canada lists 12 licences in total; the first 5 are shown below. Dosage form and approved indication text are not included in the provided records.

| DIN | Product Name |
|---------|------|
| 2421593 | JAMP ALLOPURINOL |
| 555681 | ALLOPURINOL-100 |
| 2396343 | MAR-ALLOPURINOL |
| 2130157 | ALLOPURINOL-200 |
| 2396327 | MAR-ALLOPURINOL |

---

## Safety Considerations

Please refer to the package insert for safety information.

- **Drug Interactions**: The interaction query returned no records. This means no information was found, not that no interactions exist.
- **Porphyria-specific concern**: Preclinical literature suggests allopurinol may disturb hepatic heme metabolism. It could worsen porphyria rather than help, so this needs to be resolved before any clinical consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a knowledge-graph score alone. There are no clinical trials, and the two publications are a hypothesis paper and an animal study that do not test allopurinol for hepatic porphyria. There is also a plausible risk that allopurinol is porphyrinogenic.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications
- Mechanism of action data, for example from DrugBank
- Targeted literature review of allopurinol and heme, ALAS1, or CYP effects, including any reports of porphyria exacerbation
- Preclinical or in vitro data on allopurinol's effect on hepatic heme synthesis
- A check of whether the nine lower-ranked predictions have any support. None of them currently has clinical trials, and their literature does not address the predicted disease.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

