---
layout: default
title: Articaine
parent: Model Prediction Only (L5)
nav_order: 72
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
description: "Articaine: predicted new indication Gout (evidence level L5). Approved use: Not specified in the available license data (the products are markete…"
monitor_inn: "Articaine"
predicted_indications: ["gout", "exostosis", "allergic asthma", "intrinsic asthma"]
---

# Articaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Articaine: From Local Dental Anesthesia to Gout
{: .text-alpha }

## One-Sentence Summary

Articaine is an amide-type local anesthetic marketed in Canada in dental injection products, combined with epinephrine.
The TxGNN model predicts it may be effective for **gout**, but there are **0 clinical trials** and **0 publications** supporting this direction.
This is a model-only prediction with no supporting studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available license data (the products are marketed as dental local anesthetics) |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 0.9958 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 12 of 12) |
| Number of DINs | 12 (marketed: 12) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, articaine is an amide-type local anesthetic that blocks voltage-gated sodium channels. Its efficacy as a local anesthetic is established, but this has no recognized connection to gout.

Gout is driven by urate metabolism and inflammation (for example, xanthine oxidase activity and NLRP3 inflammasome signaling). Articaine has no known effect on these pathways. The high score (0.9958) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No clinical trial or publication backs it.

For this reason, the prediction should be treated as a computational hypothesis, not as a mechanistically supported candidate.

### Other Predicted Indications (for reference)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Exostosis | 0.9942 | L5 | No credible mechanistic link. Articaine could only serve as procedural anesthesia in surgery. |
| 3 | Allergic asthma | 0.9938 | L5 | The two retrieved papers concern allergy *to* local anesthetics, so they are a safety signal, not efficacy evidence. |
| 4 | Intrinsic asthma | 0.9934 | L5 | No articaine data. Caution is warranted because of possible sulfite excipients in epinephrine-containing products. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for gout.

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 01988530 | ULTRACAINE D-S INJECTION | ARTICAINE HYDROCHLORIDE; EPINEPHRINE | Marketed |
| 01988557 | ULTRACAINE D-S FORTE INJECTION | ARTICAINE HYDROCHLORIDE; EPINEPHRINE | Marketed |
| 02123371 | SEPTANEST N | ARTICAINE HYDROCHLORIDE; EPINEPHRINE (EPINEPHRINE BITARTRATE) | Marketed |
| 02123398 | SEPTANEST SP | ARTICAINE HYDROCHLORIDE; EPINEPHRINE (EPINEPHRINE BITARTRATE) | Marketed |
| 02248488 | 4% ASTRACAINE DENTAL WITH EPINEPHRINE FORTE 1:100,000 (0.01MG/ML) | ARTICAINE HYDROCHLORIDE; EPINEPHRINE (EPINEPHRINE BITARTRATE) | Marketed |
| 02248489 | 4% ASTRACAINE DENTAL WITH EPINEPHRINE 1:200,000 (0.005MG/ML) | ARTICAINE HYDROCHLORIDE; EPINEPHRINE (EPINEPHRINE BITARTRATE) | Marketed |
| 02339536 | ARTICAINE HYDROCHLORIDE AND EPINEPHRINE BITARTRATE INJECTION | ARTICAINE HYDROCHLORIDE; EPINEPHRINE BITARTRATE | Marketed |
| 02339544 | ARTICAINE HYDROCHLORIDE AND EPINEPHRINE BITARTRATE INJECTION | ARTICAINE HYDROCHLORIDE; EPINEPHRINE BITARTRATE | Marketed |
| 02361906 | ORABLOC 1:200,000 | ARTICAINE HYDROCHLORIDE; EPINEPHRINE BITARTRATE | Marketed |
| 02361914 | ORABLOC 1:100,000 | ARTICAINE HYDROCHLORIDE; EPINEPHRINE BITARTRATE | Marketed |
| 02381311 | POSICAINE N | ARTICAINE HYDROCHLORIDE; EPINEPHRINE (EPINEPHRINE BITARTRATE) | Marketed |
| 02381338 | POSICAINE SP | ARTICAINE HYDROCHLORIDE; EPINEPHRINE (EPINEPHRINE BITARTRATE) | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

The table above lists each DIN with its current status in the DPD.

<!-- review:begin ca-lic-20261106-articaine-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Twelve valid single-ingredient licenses exist in total; the five above are shown." Removed: it described the products as single-ingredient or combination products in a way that did not match the Health Canada DPD data (the Health Canada Drug Product Database as of 2026-11-06). Revised 2026-11-24: the number of DINs and any reference to the earlier licence table, which showed only some of the DINs, were removed from the corrected sentence; the Quick Overview and the table under Canada Market Information show the current number and status of DINs. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261106-articaine-1 -->

## Safety Considerations

- **Drug Interactions** (10 recorded interactions):
  - **Major**: Nitrous acid
  - **Moderate**: Morphine (liposomal), benzocaine (topical), lidocaine (ophthalmic and topical), oxybuprocaine (ophthalmic), cinchocaine (topical), tetracaine (ophthalmic and topical)
  - **Minor**: Hyaluronidase
- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not from label text): cardiovascular conditions (hypertension, coronary artery disease, myocardial infarction, heart conduction disease, cardiomyopathy), kidney and liver disease, diabetes and diabetic ketoacidosis, angle-closure glaucoma, myasthenia gravis and other neuromuscular junction disease, butyrylcholinesterase deficiency, hyperthyroidism, Parkinson disease and hemoglobinopathy. These should be verified against the official package insert.
- **Hypersensitivity**: the retrieved allergy literature suggests possible reactions to local anesthetics, though one case report found no cross-reactivity between prilocaine and articaine.

Please refer to the package insert for the official warnings and contraindications, as these were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a score from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, not biological evidence. There are no clinical trials or relevant publications, and there is no plausible mechanistic link between a sodium channel–blocking local anesthetic and gout. The same holds for the other three predicted indications.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any preclinical or mechanistic evidence linking articaine to urate metabolism or gout-related inflammation
- Confirmation of the approved indications, dosage forms and routes for the Canadian products
- A route compatibility assessment, since articaine is an injectable dental anesthetic and the route required for gout treatment is undefined

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "single-ingredient"; revised 2026-11-24 to remove the DIN count and the reference to the earlier licence table | Corrected (revised 2026-11-24; earlier version kept in the record) | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

