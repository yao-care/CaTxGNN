---
layout: default
title: Docusate
parent: Model Prediction Only (L5)
nav_order: 295
evidence_level: L5
indication_count: 2
monitor_inn: "Docusate"
predicted_indications: ["Plummer-Vinson syndrome", "vitamin B12- and folate-independent constitutional megaloblastic anemia"]
last_modified_at: 2026-11-24
description: "Docusate: predicted new indication Plummer-Vinson syndrome (evidence level L5). In Canada: at least 20 DINs"
---

# Docusate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Docusate: Surfactant stool softener → Plummer-Vinson syndrome
{: .text-alpha }

## One-Sentence Summary

Docusate is a surfactant-type stool softener marketed in Canada in many single-ingredient products.
The TxGNN model predicts it may be relevant to **Plummer-Vinson syndrome**, but this is a model prediction only: **0 clinical trials** and **0 publications** were found to support it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Plummer-Vinson syndrome |
| TxGNN Prediction Score | 0.9918 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs on record: at least 17; dormant: 1; cancelled: 2) |
| Number of DINs | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of docusate as: Surfactant laxative ([ChEMBL CHEMBL1477036 (docusate): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1477036), CC BY-SA 3.0; accessed 2026-11-19.) Docusate is generally understood as a surfactant stool softener, and it has no known effect on iron status.

Plummer-Vinson syndrome is characterised by iron deficiency anemia, dysphagia and oesophageal webs. The model's high score most likely reflects shared anemia-related connections rather than a biological mechanism. Docusate does not treat iron deficiency, dysphagia or oesophageal webs, and the standard of care (iron replacement, with endoscopic dilation of webs when needed) is unrelated to docusate's pharmacology. No plausible mechanistic rationale can be established from the available data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

At least 20 valid single-ingredient licences are recorded, and the list may be partial.

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 00514888 | SELAX CAP 100MG | DOCUSATE SODIUM | Marketed |
| 00703494 | PMS-DOCUSATE SODIUM | DOCUSATE SODIUM | Marketed |
| 00716731 | TARO-DOCUSATE | DOCUSATE SODIUM | Marketed |
| 00870226 | RATIO-DOCUSATE SODIUM | DOCUSATE SODIUM | Marketed |
| 01994344 | SOFLAX CAPSULES 100MG | DOCUSATE SODIUM | Marketed |
| 02086018 | COLACE SYRUP | DOCUSATE SODIUM | Marketed |
| 02090163 | COLACE | DOCUSATE SODIUM | Marketed |
| 02106256 | COLACE CAPSULES | DOCUSATE SODIUM | Marketed |
| 02232969 | STOOL SOFTENER | DOCUSATE SODIUM | Marketed |
| 02238283 | SIROP DOCUSATE DE SODIUM U.S.P. 4MG/ML | DOCUSATE SODIUM | Marketed |
| 02281031 | STOOL SOFTENER | DOCUSATE SODIUM | Marketed |
| 02357305 | STOOL SOFTENER | DOCUSATE SODIUM | Marketed |
| 02426838 | DOCUSATE SODIUM | DOCUSATE SODIUM | Marketed |
| 02437317 | M-DOCUSATE SODIUM 100 MG | DOCUSATE SODIUM | Marketed |
| 02484226 | COLACE CLEAR | DOCUSATE SODIUM | Marketed |
| 02526492 | ENEMEEZ | DOCUSATE SODIUM | Marketed |
| 02536412 | STOOL SOFTENER CLEAR | DOCUSATE SODIUM | Marketed |
| 02245946 | JAMP-DOCUSATE SODIUM | DOCUSATE SODIUM | Dormant |
| 02247385 | SANDOZ DOCUSATE SODIUM | DOCUSATE SODIUM | Cancelled post market |
| 02530538 | NRA-DOCUSATE SODIUM | DOCUSATE SODIUM | Cancelled post market |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

The data contain only part of the DINs for this ingredient; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions** (4 recorded):
  - Lactulose: Moderate
  - Mineral oil: Moderate
  - Phenolphthalein: Moderate
  - Linaclotide: Minor

Please refer to the package insert for other safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. No trials or publications study docusate in Plummer-Vinson syndrome, and no mechanistic link is apparent, so the evidence level is L5.

**To proceed, the following is needed:**
- Mechanism-of-action data for docusate
- Package insert warnings and contraindications from Health Canada
- Any preclinical or clinical study directly addressing docusate in Plummer-Vinson syndrome

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for docusate are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL1477036 (docusate): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1477036) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

