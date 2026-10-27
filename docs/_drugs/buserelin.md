---
layout: default
title: Buserelin
parent: Model Prediction Only (L5)
nav_order: 137
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Buserelin: predicted new indication Hypertrichosis (evidence level L5). Approved use: Prostate cancer"
monitor_inn: "BUSERELIN"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality"]
---

# Buserelin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Buserelin: From Prostate Cancer to Hypertrichosis
{: .text-alpha }

## One-Sentence Summary

Buserelin is a GnRH (gonadotropin-releasing hormone) agonist used to treat prostate cancer.
The TxGNN model predicts it may be effective for **hypertrichosis**,
but there are currently **0 clinical trials** and only **1 loosely related publication** (a case report on a hypertrichosis-associated syndrome, not on buserelin treatment), so the evidence is essentially model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate cancer (based on pharmacology data; the Health Canada licence record contains no indication text) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, buserelin is a GnRH agonist that acts on the GnRH receptor (GNRHR). It suppresses the pituitary-gonadal axis and lowers sex steroid levels, which is the basis of its use in prostate cancer.

The link to hypertrichosis is weak and speculative. Hypertrichosis is not a recognised GnRH-driven condition. The only retrieved publication concerns Cantu syndrome (a hypertrichosis-associated syndrome) and hypopituitarism, and it addresses endocrine monitoring rather than buserelin treatment. The high TxGNN score most likely reflects proximity in the knowledge graph through endocrine and genetic syndrome nodes, not a demonstrated therapeutic mechanism.

Other top-ranked predictions show the same pattern. These include Ambras-type hypertrichosis universalis congenita, malformation syndromes with dental involvement, syndromes with Dandy-Walker malformation, and isolated genetic hair shaft abnormalities. All are developmental or genetic conditions with no plausible GnRH-based mechanism, and none has trials or literature support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31743099](https://pubmed.ncbi.nlm.nih.gov/31743099/) | 2019 | Review/Case series | Endocrinology, Diabetes & Metabolism Case Reports | Cantu syndrome (hypertrichotic osteochondrodysplasia) case with multiple pituitary hormone deficiencies; supports endocrine monitoring in this condition. It does not evaluate buserelin or any treatment for hypertrichosis. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02225166 | SUPREFACT | Not specified | Not specified in the licence record |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal therapy (GnRH agonist), not a conventional cytotoxic agent |
| Myelosuppression Risk | Low (not expected to be a significant myelosuppressive agent) |
| Emetogenicity Classification | Low |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: The interaction query completed with one pharmacology record: buserelin acts on the GnRH1 receptor (GNRHR, human). No interaction severity level was provided.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no clinical trials, the single publication does not address buserelin treatment, and no plausible mechanism links GnRH agonism to hypertrichosis or the other predicted conditions.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data (for example from DrugBank)
- Licence details for the Canadian product (indication text, dosage form, manufacturer)
- Evidence of a mechanistic or clinical rationale linking GnRH agonism to hypertrichosis, such as preclinical or observational studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

