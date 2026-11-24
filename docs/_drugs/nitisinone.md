---
layout: default
title: Nitisinone
parent: Model Prediction Only (L5)
nav_order: 655
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "NITISINONE"
predicted_indications: ["renal tubular acidosis", "galactosemia", "serpinopathy with toxic serpin polymerization", "C1 inhibitor deficiency", "glycogen storage disease", "adult polyglucosan body disease", "glycogen storage disease due to glucose-6-phosphatase deficiency", "Griscelli syndrome", "granulomatous disease, chronic, X-linked", "ermine phenotype"]
description: "Nitisinone: predicted new indication Renal tubular acidosis (evidence level L5). In Canada: 8 DINs (8 marketed)"
---

# Nitisinone
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

## Nitisinone: Renal tubular acidosis
{: .text-alpha }

## One-Sentence Summary

Nitisinone was originally used to treat hereditary tyrosinemia.
The TxGNN model predicts it may be effective for **renal tubular acidosis** (score 0.9996), but **no clinical trials and no publications** currently support this specific prediction. It is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Renal tubular acidosis |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 8 of 8) |
| Number of DINs | 8 (marketed: 8) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for nitisinone: "Nitisinone is a competitive inhibitor of 4-hydroxyphenyl-pyruvate dioxygenase, an enzyme upstream of fumarylacetoacetate hydrolase (FAH) in the tyrosine catabolic pathway. By inhibiting the normal catabolism of tyrosine in patients with HT-1, nitisinone prevents the accumulation of the catabolic intermediates maleylacetoacetate and fumarylacetoacetate." ([DailyMed: Nityr (nitisinone) prescribing information, Cycle Pharmaceuticals Ltd.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=00fd1905-27e4-420e-8dc5-a69e4ddc1526), label version 2026-10-21; accessed 2026-11-19.) From general knowledge, nitisinone inhibits 4-hydroxyphenylpyruvate dioxygenase (HPPD), an enzyme in the tyrosine breakdown pathway. Blocking it prevents the build-up of toxic upstream metabolites such as succinylacetone.

In hereditary tyrosinemia type 1, these toxic metabolites are thought to cause kidney tubular damage (a Fanconi-type proximal tubulopathy). Nitisinone may therefore improve this *secondary* tubular dysfunction. However, this is not a mechanism for primary renal tubular acidosis, and no direct link has been established. The very high TxGNN score is a computational prediction only and should not be read as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for renal tubular acidosis.

For context, the second-ranked prediction (galactosemia) and the fifth-ranked prediction (glycogen storage disease) retrieved only general reviews of paediatric liver disease. These discuss the conditions side by side and do not show that nitisinone treats them.

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02457717 | MDK-NITISINONE | NITISINONE | Marketed |
| 02457725 | MDK-NITISINONE | NITISINONE | Marketed |
| 02457733 | MDK-NITISINONE | NITISINONE | Marketed |
| 02459698 | ORFADIN | NITISINONE | Marketed |
| 02459701 | ORFADIN | NITISINONE | Marketed |
| 02459728 | ORFADIN | NITISINONE | Marketed |
| 02459736 | ORFADIN | NITISINONE | Marketed |
| 02469693 | ORFADIN | NITISINONE | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

Eight single-ingredient licences are currently valid (none cancelled).

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not from label text): kidney disease, pyoureter, thrombocytopenia, leukopenia, hypophosphatemia, tyrosinemia. These should be verified against the official product monograph.
- **Drug Interactions**: The interaction screen returned 100 potential interactions, mostly of Moderate severity. Examples include abiraterone, amiodarone, amlodipine, nifedipine, ibuprofen, isotretinoin, dexamethasone, pioglitazone, aprepitant, atazanavir, bicalutamide and apalutamide. Armodafinil is rated Minor.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5), with no trials or literature. The only plausible biology is relief of secondary tubular injury in tyrosinemia type 1, not primary renal tubular acidosis. Nitisinone's kidney-related contraindication signals add further caution.

**To proceed, the following is needed:**
- Official Health Canada product monograph warnings and contraindications
- Confirmed mechanism of action data
- Preclinical or clinical evidence in renal tubular acidosis, or clear separation of primary from secondary forms
- A defined target population and a safety plan that accounts for kidney and blood-count signals
- Approved indication text and dosage forms for the Canadian licences

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Nityr (nitisinone) prescribing information, Cycle Pharmaceuticals Ltd.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=00fd1905-27e4-420e-8dc5-a69e4ddc1526) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

