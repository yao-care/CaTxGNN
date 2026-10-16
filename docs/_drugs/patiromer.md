---
layout: default
title: Patiromer
parent: Model Prediction Only (L5)
nav_order: 709
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Patiromer: predicted new indication Mitochondrial oxidative phosphorylation disorder due to nuclear DNA a… (evidence level L5). Approved use: Not stated in the Canadian licence data compiled for this…"
monitor_inn: "Patiromer"
predicted_indications: ["mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "exocrine pancreatic insufficiency", "colonic neoplasm", "cecum villous adenoma", "cecum neuroendocrine tumor G1", "rectosigmoid junction neoplasm", "cecal disease", "lipoma of colon", "severe nonproliferative diabetic retinopathy", "colonic lymphangioma"]
---

# Patiromer
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

# Patiromer: From Hyperkalaemia Management to Mitochondrial Oxidative Phosphorylation Disorder (Nuclear DNA Anomalies)

## One-Sentence Summary

Patiromer is a non-absorbed potassium-binding polymer marketed in Canada as VELTASSA. The TxGNN model predicts it may be effective for **mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies**, but **no clinical trials and no publications** currently support this prediction. The score appears to be a knowledge-graph artifact rather than a pharmacologically grounded signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence data compiled for this report |
| Predicted New Indication | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 98.72% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, patiromer is a non-absorbed polymer that exchanges calcium for potassium in the colonic lumen, lowering systemic potassium by removing it in the stool.

This mechanism has no known link to mitochondrial function, nuclear-encoded oxidative phosphorylation genes, or cellular energy metabolism. The high TxGNN score is therefore best read as a graph-based prediction artifact, not a result supported by pharmacological reasoning. Mechanistic plausibility is low.

### Other Top-Ranked Predictions

The next nine predictions show the same pattern. All have only model-based support (L5), with no trials or literature.

| Rank | Predicted Indication | Score | Comment |
|------|------|------|------|
| 2 | Exocrine pancreatic insufficiency | 98.53% | No direct mechanism. The drug's GI adverse effects could worsen symptoms. |
| 3 | Colonic neoplasm | 97.42% | Anatomical co-location with the site of action only. No anti-tumour mechanism. |
| 4 | Cecum villous adenoma | 97.20% | Anatomical association only. |
| 5 | Cecum neuroendocrine tumor G1 | 97.19% | No link to neuroendocrine tumour biology. |
| 6 | Rectosigmoid junction neoplasm | 97.19% | Anatomical proximity only. |
| 7 | Cecal disease | 97.16% | Vague, broad category. |
| 8 | Lipoma of colon | 97.14% | No mechanism. |
| 9 | Severe nonproliferative diabetic retinopathy | 97.14% | Only a speculative supportive-care link through hyperkalaemia control. |
| 10 | Colonic lymphangioma | 97.14% | No mechanism. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02481359 | VELTASSA | Not stated | Not stated |
| 02481367 | VELTASSA | Not stated | Not stated |

Both licences are valid single-ingredient products.

## Safety Considerations

**Drug Interactions**: The interaction screening found 48 potential interacting drugs. The entries below are from the first 20 returned.

- **Major**: magnesium oxide, aluminium hydroxide, calcium carbonate
- **Moderate**: rabeprazole, omeprazole, dexlansoprazole, hydrocortisone, dexamethasone, triamcinolone, beclomethasone dipropionate, betamethasone, metformin, iron, attapulgite, and several calcium salts (phosphate, acetate, citrate, glubionate, gluconate, lactate)

Other safety information (warnings and contraindications) was not available. Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a knowledge-graph score. There are no trials or publications, and no plausible mechanism links a non-absorbed potassium binder to mitochondrial oxidative phosphorylation disorders. The same applies to the other top-ranked predictions, most of which reflect anatomical proximity to the colon.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (required before safety screening)
- Mechanism of action data and the approved indication text from the Canadian licences
- A credible mechanistic hypothesis, followed by preclinical or observational evidence, before any further evaluation of this prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

