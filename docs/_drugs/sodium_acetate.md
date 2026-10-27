---
layout: default
title: Sodium Acetate
parent: Model Prediction Only (L5)
nav_order: 854
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Sodium Acetate: predicted new indication Congenital prothrombin deficiency (evidence level L5). Approved use: Not stated in the Canadian license records compiled for this report (…"
monitor_inn: "SODIUM ACETATE"
predicted_indications: ["congenital prothrombin deficiency", "epiglottitis", "urinary tract infection (disease)", "sclerosing cholangitis", "gonococcal urethritis", "Ureaplasma urethritis", "dyspepsia", "uterine inflammatory disease", "gastroparesis (disease)", "xanthogranulomatous pyelonephritis"]
---

# Sodium Acetate
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

## Sodium Acetate: From Electrolyte Replenishment to Congenital Prothrombin Deficiency
{: .text-alpha }

## One-Sentence Summary

Sodium acetate is an electrolyte and alkalinizing agent. It is marketed in Canada as a single-ingredient injection and as a component of multi-electrolyte, dialysis and irrigation solutions. The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, but **no clinical trials and no publications** support this prediction, and the data compiled for this report show no plausible mechanistic link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license records compiled for this report (the drug is used as a sodium source and alkalinizing agent) |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, sodium acetate is an electrolyte, a sodium source and an alkalinizing agent (acetate is metabolized to bicarbonate). It is used in fluid and electrolyte replacement and as a component of dialysis and irrigation solutions.

Congenital prothrombin deficiency is a rare inherited coagulation disorder caused by reduced or abnormal prothrombin (factor II). Sodium acetate has no known effect on prothrombin synthesis or on the coagulation cascade. The very high TxGNN score (0.9998) appears to be an artifact of the knowledge-graph structure rather than a drug-specific signal, because no trial or publication supports it.

Other top-ranked predictions (epiglottitis, gonococcal urethritis, Ureaplasma urethritis, xanthogranulomatous pyelonephritis, uterine inflammatory disease) also lack a mechanistic rationale. The only speculative link is for urinary tract infection, where acetate-derived urinary alkalinization might change urine pH. Alkalinization may even favor growth of some uropathogens. Literature found for dyspepsia and gastroparesis most likely reflects the use of 13C-sodium acetate as a tracer in gastric emptying breath tests, not a therapeutic effect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for congenital prothrombin deficiency.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02139529 | Sodium Acetate Injection, USP | Not specified | Not specified |
| 02181746 | Sodium Acetate Injection USP | Not specified | Not specified |
| 00039470 | Lactated Ringer's Injection | Not specified | Not specified |
| 01931636 | Lactated Ringer's Injection USP | Not specified | Not specified |
| 00799971 | Lactated Ringer's Irrigation Sol | Not specified | Not specified |

A total of 20 valid licenses are on record. The list shows only the first 5. All are single-ingredient entries, and none is cancelled.

## Safety Considerations

Label-based warnings and contraindications were not available. Please refer to the package insert for safety information.

**Contraindication signals from the knowledge graph** (not label text, so interpret with caution): kidney disease (including chronic kidney disease, chronic renal failure and end-stage renal failure), anuria, heart disease and cardiovascular disease, atrioventricular block, ventricular fibrillation, digitalis poisoning, hypercalcemia (including humoral hypercalcemia of malignancy), sarcoidosis, nephrocalcinosis, nephrolithiasis, acute urate nephropathy, phosphorus metabolism disorders, hyperkalemic periodic paralysis, hypoaldosteronism, myotonia congenita, phenylketonuria and other disorders of phenylalanine metabolism.

**Drug interactions:** 30 interactions were recorded. The 20 listed in the data compiled for this report are mostly Moderate or Minor. No severe interactions are shown among those 20.
- **Moderate:** doxycycline, tetracycline, minocycline, acetylsalicylic acid, choline salicylate, ephedrine (including nasal), pseudoephedrine, amphetamine, dextroamphetamine, benzphetamine, methenamine
- **Minor:** sulfonylureas (chlorpropamide, tolazamide, glipizide, glyburide, acetohexamide, tolbutamide), memantine, methotrexate

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction has no supporting clinical trials or literature (evidence level L5).
- Sodium acetate has no known effect on the coagulation cascade, so the high score is likely a graph artifact.
- Health Canada label warnings and contraindications are missing, which blocks safety screening.

**To proceed, the following is needed:**
- The Health Canada package insert, to obtain approved indications, warnings and contraindications
- Mechanism of action data (for example from DrugBank)
- A credible mechanistic hypothesis and preclinical evidence linking sodium acetate to prothrombin or coagulation biology
- Review of other candidates. Urinary tract infection is the only prediction with even a speculative link, and it would also need supporting evidence before any further evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

