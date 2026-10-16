---
layout: default
title: Isosorbide Mononitrate
parent: Model Prediction Only (L5)
nav_order: 503
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Isosorbide Mononitrate: predicted new indication Hypertrichosis (disease) (evidence level L5). Approved use: Not stated in the available licence records"
---

# Isosorbide Mononitrate
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

# Isosorbide Mononitrate: From Angina-Type Cardiovascular Use to Hypertrichosis

## One-Sentence Summary

Isosorbide mononitrate is a nitric oxide (NO)-releasing vasodilator that is marketed in Canada in 4 single-ingredient products. The TxGNN model predicts it may be effective for **hypertrichosis** (score 99.995%), but **no clinical trials and no publications** support this prediction. It is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available licence records |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.995% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, isosorbide mononitrate is an organic nitrate that releases nitric oxide, activates soluble guanylate cyclase and raises cGMP, which causes vasodilation.

The link to hypertrichosis is weak. Nitrates are not known to cause excess hair growth. A minoxidil-like vasodilation argument is sometimes raised for hair growth, but minoxidil acts mainly through potassium channel opening, and there is no direct evidence for isosorbide mononitrate. The high TxGNN score appears to reflect knowledge-graph proximity rather than established biology.

The other top predictions are mostly hair-related or congenital conditions (Ambras-type hypertrichosis, alopecia, hair shaft abnormalities, hypotrichosis, alopecia areata, and developmental malformation syndromes). None has trial or literature support, and most are genetic or autoimmune diseases that a vasodilator would not be expected to address. The only prediction with some biological plausibility is **pulmonary arterial hypertension** (rank 10, score 99.94%), where the NO-cGMP pathway is a validated target. Even there, organic nitrates are not recommended, and tolerance and hypotension are concerns.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for hypertrichosis.

For the most plausible alternative prediction (pulmonary arterial hypertension), only indirect studies were found:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16422873](https://pubmed.ncbi.nlm.nih.gov/16422873/) | 2005 | Clinical hemodynamic study | J Sex Med | Hemodynamic effects of sildenafil and isosorbide mononitrate in men with coronary artery disease and erectile dysfunction (not a PAH population) |
| [29705351](https://pubmed.ncbi.nlm.nih.gov/29705351/) | 2018 | Preclinical animal study | Life Sci | sGC stimulation in monocrotaline-induced pulmonary hypertensive rats; examined whether NO-enhancing drugs can halt disease progression |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02126559 | IMDUR | Not listed | Not listed |
| 02311321 | PRO-ISMN - 60 | Not listed | Not listed |
| 02272830 | APO-ISMN | Not listed | Not listed |
| 02301288 | PMS-ISMN | Not listed | Not listed |

All four licences are valid single-ingredient products.

---

## Safety Considerations

- **Disease-level cautions from the knowledge graph** (drug-disease contraindication links, not label text): hypotensive disorder, hypertrophic cardiomyopathy, myocardial infarction, coronary thrombosis, hemoglobinopathy, anaemia (including macrocytic anaemia), hyperthyroidism, Graves disease, thyrotoxicosis, and intracerebral haemorrhage.
- **Drug Interactions**: 100 interactions were identified. Those listed as moderate include bupropion, morphine, opium, dronabinol, nabilone, sapropterin, and the SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), as well as rosiglitazone. Omeprazole is listed as minor. Several others (e.g., calcitriol, pantoprazole, glimepiride, metformin) have an unclassified severity.

Please refer to the package insert for the official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone, with no clinical trials, no literature, and no plausible mechanism for hypertrichosis. Nitrates are not known to affect hair growth, and the same applies to the other hair and congenital disorder predictions.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, and approved indication text for each DIN
- Mechanism of action data
- Any preclinical or clinical evidence linking NO donors to hair follicle biology, if this indication is to be pursued
- Consider redirecting evaluation to pulmonary arterial hypertension as a research question only, with a review of nitrate tolerance, hypotension risk, and the guideline position against organic nitrates in PAH
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

