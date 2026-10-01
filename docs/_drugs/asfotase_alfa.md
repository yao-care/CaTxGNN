---
layout: default
title: Asfotase Alfa
parent: Model Prediction Only (L5)
nav_order: 75
evidence_level: L5
indication_count: 10
---

# Asfotase Alfa
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

# Asfotase alfa: From Hypophosphatasia to Mitochondrial Oxidative Phosphorylation Disorder (Nuclear DNA Anomalies)

## One-Sentence Summary

Asfotase alfa is a recombinant enzyme replacement therapy (tissue-nonspecific alkaline phosphatase, TNSALP), marketed in Canada as STRENSIQ. The license records do not state an indication, but the product is known to be used for hypophosphatasia.
The TxGNN model predicts it may be effective for **mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies**.
There are **0 clinical trials** and **0 publications** behind this prediction, so it is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypophosphatasia (not stated in the license records; based on the drug's known use) |
| Predicted New Indication | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Asfotase alfa is a recombinant TNSALP. It hydrolyzes extracellular substrates such as inorganic pyrophosphate and acts on bone mineralization. Detailed mechanism of action data is not available in the input.

**No established mechanistic link supports this prediction.** TNSALP has no known role in mitochondrial oxidative phosphorylation (OXPHOS). The high score comes from the knowledge-graph structure, not from biological or clinical evidence.

Other high-scoring predictions show the same pattern:
- **Steel syndrome (rank 2):** a skeletal dysplasia, so the only link is bone biology. It involves a collagen-related defect that TNSALP replacement is not known to address.
- **Scheie syndrome, Hurler syndrome and lysosomal storage disease with skeletal involvement (ranks 4-6):** these likely reflect the shared "enzyme replacement plus skeletal phenotype" class. TNSALP does not act on the substrates that accumulate in these diseases.
- **Exocrine pancreatic insufficiency, familial apolipoprotein C-II deficiency, esophageal varices and cystinosis (ranks 3, 7-10):** no plausible mechanism was identified, and these are probably graph artifacts. The two esophageal varices entries have identical scores and look like duplicate predictions from one graph signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2444623 | STRENSIQ |
| 2444615 | STRENSIQ |
| 2444631 | STRENSIQ |
| 2444658 | STRENSIQ |

Dosage form, manufacturer and approved indication text are blank in the license records.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no supporting clinical trials or publications (L5). The biology does not support it, because TNSALP replacement has no known connection to mitochondrial OXPHOS. The other top-ranked predictions are also unsupported.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank, to allow a proper mechanistic-link analysis
- Approved indication text for the four licenses
- Preclinical or mechanistic evidence that TNSALP activity affects mitochondrial function or nuclear-DNA-related OXPHOS disease
- A re-run of the evidence search for this and the other predicted indications, to check that no relevant trials or publications were missed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

