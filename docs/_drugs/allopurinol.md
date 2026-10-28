---
layout: default
title: Allopurinol
parent: Model Prediction Only (L5)
nav_order: 37
evidence_level: L5
indication_count: 10
monitor_inn: "ALLOPURINOL"
predicted_indications: ["hepatic porphyria", "primitive portal vein thrombosis", "idiopathic copper-associated cirrhosis", "early-onset familial noncirrhotic portal hypertension", "hepatoportal sclerosis", "hepatopulmonary syndrome", "disorder of phenylalanine metabolism", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "inflammatory myopathy with abundant macrophages"]
last_modified_at: 2026-10-28
description: "Allopurinol: predicted new indication hepatic porphyria (evidence level L5). Approved use: Not recorded in the local data"
---

# Allopurinol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Allopurinol: xanthine oxidase inhibitor → hepatic porphyria
{: .text-alpha }

## One-Sentence Summary

Allopurinol is a xanthine oxidase inhibitor that is marketed in Canada in 12 single-ingredient licences.
The TxGNN model predicts it may be effective for **hepatic porphyria**, but there are **no registered clinical trials** and only **2 publications** (a hypothesis paper and an animal study) that touch on the topic.
The evidence therefore rests on a model prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | hepatic porphyria |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 12 of 12) |
| Number of DINs | 12 (valid: 12) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for allopurinol is not available in the data compiled for this report. Allopurinol is generally known as a xanthine oxidase inhibitor that lowers uric acid production.

The link to hepatic porphyria is indirect and speculative. Older literature discusses effects of some drugs on hepatic haem metabolism and on 5-aminolevulinate synthase (ALAS), the rate-limiting enzyme of haem synthesis. A 2019 hypothesis paper proposes metabolic targeting of ALAS as a therapy for acute hepatic porphyrias. However, that paper does not test allopurinol in patients. Experimental reports also suggest allopurinol may modify porphyrin metabolism, so whether the effect would be beneficial or harmful is unresolved.

Because no cited study directly examines allopurinol in hepatic porphyria, the prediction should be treated as a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Review (hypothesis) | Medical Hypotheses | Proposes targeting 5-ALAS via tryptophan or inhibition of haem use by tryptophan 2,3-dioxygenase as a therapy for acute hepatic porphyrias; allopurinol is not tested |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Preclinical (animal) | Biochemical Pharmacology | Acute carbamazepine administration altered haem metabolism in rat liver, relevant to how drugs exacerbate hepatic porphyrias; not an allopurinol study |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02421593 | JAMP ALLOPURINOL | – | – |
| 00555681 | ALLOPURINOL-100 | – | – |
| 02396343 | MAR-ALLOPURINOL | – | – |
| 02130157 | ALLOPURINOL-200 | – | – |
| 02396327 | MAR-ALLOPURINOL | – | – |

All 12 licences are single-ingredient products and currently valid; the five above are shown as examples.

---

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 records. Those graded Moderate include aluminum hydroxide, attapulgite, kaolin, magaldrate and sucralfate. Amoxicillin and chlorpropamide are graded Minor. Several others (for example metformin, omeprazole, pantoprazole, morphine, doxycycline) are of unknown severity.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but no clinical trial or study directly tests allopurinol in hepatic porphyria. The mechanistic link is indirect, and the direction of effect (benefit or harm) is unresolved, so the evidence level is L5.

**To proceed, the following is needed:**
- Mechanism-of-action data for allopurinol
- Package insert warnings and contraindications from Health Canada
- Preclinical studies that directly test allopurinol on haem biosynthesis and porphyrin metabolism, with particular attention to the risk of exacerbating porphyria
- A review of whether any clinical reports exist on allopurinol use in patients with porphyria
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

