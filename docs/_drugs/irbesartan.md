---
layout: default
title: Irbesartan
parent: Model Prediction Only (L5)
nav_order: 495
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
description: "Irbesartan: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension, diabetic nephropathy"
monitor_inn: "IRBESARTAN"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
---

# Irbesartan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Irbesartan: From Hypertension to Malignant Hypertensive Renal Disease
{: .text-alpha }

## One-Sentence Summary

Irbesartan is an angiotensin II receptor blocker, originally used to treat hypertension and diabetic nephropathy.
The TxGNN model (deep learning) predicts it may be effective for **malignant hypertensive renal disease**, with a score of 0.9931.
However, **no clinical trials or publications** currently support this specific prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, diabetic nephropathy (the Canadian licence records provide no indication text) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9931 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs on record: at least 17; cancelled: 3) |
| Number of DINs | at least 20 |
| Recommended Decision | Hold |

Other high-scoring predictions: malignant renovascular hypertension (0.9931), pulmonary hypertension with unclear multifactorial mechanism (0.9925), and pulmonary hypertension owing to lung disease and/or hypoxia (0.9925). The last has preclinical literature (L4).

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for irbesartan: "Angiotensin II is a potent vasoconstrictor formed from angiotensin I in a reaction catalyzed by angiotensin-converting enzyme (ACE, kininase II). Angiotensin II is the primary vasoactive hormone of the renin-angiotensin system, and an important component in the pathophysiology of hypertension. […] Irbesartan blocks the vasoconstrictor and aldosterone-secreting effects of angiotensin II by selectively binding to the AT 1 angiotensin II receptor found in many tissues (e.g., vascular smooth muscle, adrenal gland)." ([DailyMed: Avapro (irbesartan) prescribing information, Sanofi-Aventis U.S. LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7885b2a8-be4e-48ab-8113-4e6ab791eb98), label version 2026-08-24; accessed 2026-11-19.) Based on known information, irbesartan is an AT1 receptor antagonist (an angiotensin II receptor blocker, ARB). Its efficacy in hypertension and diabetic nephropathy is established, and mechanistically it may be applicable to malignant hypertensive renal disease.

In malignant hypertensive nephrosclerosis, angiotensin II is thought to drive vascular injury. Blocking the renin-angiotensin system could lower blood pressure and protect the kidney. This overlaps closely with the approved indications, which explains the high prediction score.

The same logic applies to malignant renovascular hypertension, which is strongly angiotensin II-dependent. ARBs carry a recognised caution in bilateral renal artery stenosis because of the risk of acute decline in renal function, so this would need explicit safety review.

For pulmonary hypertension, the link is weaker. Angiotensin II contributes to pulmonary vascular remodelling in preclinical models, but systemic ARBs are not an established treatment. Preclinical work on hypoxia-related pulmonary hypertension (see below) is indirect, mostly cardiac or rodent-based.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction or for any of the other three predicted indications.

## Literature Evidence

For the top-ranked prediction (malignant hypertensive renal disease), currently no related literature available.

The table below covers the fourth-ranked prediction, pulmonary hypertension owing to lung disease and/or hypoxia. It lists the most relevant irbesartan-specific publications. All are preclinical or review articles.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34147903](https://pubmed.ncbi.nlm.nih.gov/34147903/) | 2021 | Preclinical (animal) | Biomed Pharmacother | Irbesartan improved pulmonary artery lesions in a rat model of chronic mountain sickness, via cholesterol metabolism |
| [34286497](https://pubmed.ncbi.nlm.nih.gov/34286497/) | 2021 | Preclinical (type not classified) | Eur Rev Med Pharmacol Sci | Irbesartan improved oxidative stress in rats with high-altitude pulmonary hypertension, via intestinal flora |
| [30356256](https://pubmed.ncbi.nlm.nih.gov/30356256/) | 2018 | Preclinical (in vitro) | PLoS One | Irbesartan protected cardiomyocytes under hypoxic stress |
| [34626328](https://pubmed.ncbi.nlm.nih.gov/34626328/) | 2022 | Preclinical (animal) | Sleep Breath | Irbesartan reduced sleep apnoea-induced cardiac apoptosis and upregulated Sirtuin 1 |
| [17142340](https://pubmed.ncbi.nlm.nih.gov/17142340/) | 2007 | Preclinical (animal) | Am J Physiol Heart Circ Physiol | Irbesartan inhibited coronary angiogenesis stimulated by chronic intermittent hypoxia in neonatal rats |
| [35288835](https://pubmed.ncbi.nlm.nih.gov/35288835/) | 2022 | Review | Inflammopharmacology | Reviews pleiotropic effects of AT-1 receptor antagonists in hypoxia induced by cardiac ischaemia |
| [15526904](https://pubmed.ncbi.nlm.nih.gov/15526904/) | 2004 | Preclinical (animal) | Renal Failure | Irbesartan ameliorated cyclosporine nephrotoxicity in an animal model (kidney-related, not pulmonary) |

## Canada Market Information

Irbesartan is a marketed single-ingredient product. The data compiled for this report do not include dosage forms or approved indication text.

<!-- review:begin ca-lic-20261105-irbesartan-1 -->

> **Review correction (2026-11-05)**: Originally stated: "Irbesartan is a marketed single-ingredient product with 20 valid licences (none cancelled). The data compiled for this report do not include dosage forms or approved indication text." Removed: the number or status of DINs stated here did not match the Health Canada DPD data (the Health Canada Drug Product Database as of 2026-11-05). Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261105-irbesartan-1 -->

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02237924 | AVAPRO | IRBESARTAN | Marketed |
| 02237925 | AVAPRO | IRBESARTAN | Marketed |
| 02328461 | SANDOZ IRBESARTAN | IRBESARTAN | Marketed |
| 02328488 | SANDOZ IRBESARTAN | IRBESARTAN | Marketed |
| 02328496 | SANDOZ IRBESARTAN | IRBESARTAN | Marketed |
| 02365197 | IRBESARTAN | IRBESARTAN | Marketed |
| 02365200 | IRBESARTAN | IRBESARTAN | Marketed |
| 02372347 | IRBESARTAN | IRBESARTAN | Marketed |
| 02372398 | IRBESARTAN | IRBESARTAN | Marketed |
| 02385309 | IRBESARTAN | IRBESARTAN | Marketed |
| 02406829 | TARO-IRBESARTAN | IRBESARTAN | Marketed |
| 02406837 | TARO-IRBESARTAN | IRBESARTAN | Marketed |
| 02422980 | MINT-IRBESARTAN | IRBESARTAN | Marketed |
| 02422999 | MINT-IRBESARTAN | IRBESARTAN | Marketed |
| 02524821 | M-IRBESARTAN | IRBESARTAN | Marketed |
| 02524848 | M-IRBESARTAN | IRBESARTAN | Marketed |
| 02545241 | JAMP IRBESARTAN | IRBESARTAN | Marketed |
| 02316390 | TEVA-IRBESARTAN | IRBESARTAN | Cancelled post market |
| 02316404 | TEVA-IRBESARTAN | IRBESARTAN | Cancelled post market |
| 02316412 | TEVA-IRBESARTAN | IRBESARTAN | Cancelled post market |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

The data contain only part of the DINs for this ingredient; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

Package insert warnings and contraindications are not available in the data compiled for this report. Please refer to the package insert for these.

- **Contraindications and cautions from the knowledge graph (not label text):**
  - Angioedema, including hereditary, acquired and RAAS-blocker-induced forms
  - Pancreatitis
  - Systemic lupus erythematosus
  - Myopathy and rhabdomyolysis
  - Diabetes and diabetic ketoacidosis
  - Gout and hyperuricaemia
  - Hypotensive disorders
  - Anuria and renal artery obstruction
  - Hepatic coma and encephalopathy
  - Hyperparathyroidism, hypercalcaemia and nephrocalcinosis

  Renal artery obstruction is directly relevant to the renovascular hypertension prediction.
- **Drug Interactions:** 100 interactions were identified. The 20 listed in the data compiled for this report include two **Major** interactions, both potassium salts (risk of hyperkalaemia):
  - Potassium citrate
  - Potassium bicarbonate

  The remaining listed interactions are Moderate. Examples:
  - Corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone)
  - SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin)
  - Insulins (aspart, degludec)
  - Acetylsalicylic acid
  - Morphine
  - Bupropion
  - Aprepitant
  - Dronabinol
  - Bowel-preparation agents

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (malignant hypertensive renal disease) has a high score (0.9931) and a plausible mechanism close to the approved indications. It has no trials or literature behind it (Evidence Level L5). The pulmonary hypertension predictions have only indirect preclinical support (L4). Package insert safety data are missing, which blocks safety screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, including approved indication text and dosage forms
- Detailed mechanism of action data from DrugBank
- A literature and trial search specific to malignant hypertensive nephrosclerosis and renovascular hypertension
- A safety review for bilateral renal artery stenosis and hyperkalaemia risk
- For the pulmonary hypertension prediction, direct clinical evidence beyond rodent and cardiac studies

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "with 20 valid licences (none cancelled)" | Corrected | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Avapro (irbesartan) prescribing information, Sanofi-Aventis U.S. LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7885b2a8-be4e-48ab-8113-4e6ab791eb98) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

