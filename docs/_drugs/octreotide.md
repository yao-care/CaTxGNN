---
layout: default
title: Octreotide
parent: Model Prediction Only (L5)
nav_order: 676
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-25
monitor_inn: "Octreotide"
predicted_indications: ["vulvar inverted follicular keratosis", "seborrheic keratosis"]
description: "Octreotide: predicted new indication Vulvar inverted follicular keratosis (evidence level L5). In Canada: 17 DINs (13 marketed, 1 dormant)"
---

# Octreotide
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

## Octreotide: Vulvar inverted follicular keratosis
{: .text-alpha }

## One-Sentence Summary

Octreotide is a somatostatin analogue originally used for acromegaly, hyperpituitarism and carcinoid syndrome.
The TxGNN model predicts it may be effective for **vulvar inverted follicular keratosis**,
but **no clinical trials and no publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Vulvar inverted follicular keratosis |
| TxGNN Prediction Score | 0.9958 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 13 of 17; dormant: 1; cancelled: 3) |
| Number of DINs | 17 (marketed: 13) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for octreotide: "Sandostatin Injection exerts pharmacologic actions similar to the natural hormone, somatostatin. It is an even more potent inhibitor of GH, glucagon, and insulin than somatostatin. […] By virtue of these pharmacological actions, octreotide has been used to treat the symptoms associated with metastatic carcinoid tumors (flushing and diarrhea), and VIP secreting adenomas (watery diarrhea)." ([DailyMed: Sandostatin (octreotide acetate) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4e2c9856-1836-49f0-9472-4dbeeb408f39), label version 2026-07-22; accessed 2026-11-19.) Based on known information, octreotide is a somatostatin analogue whose efficacy in acromegaly and carcinoid syndrome is established. It acts through somatostatin receptors, mainly in the pituitary and neuroendocrine tissue.

The predicted indication is a benign skin lesion. No somatostatin-receptor-mediated mechanism is documented for it. The high score comes from the TxGNN model (deep learning) and most likely reflects similarities the model learned between related diseases, not biological evidence. The prediction should be treated as a computational hypothesis only.

Other predictions ranked highly for this drug are also weakly supported:
- **Seborrheic keratosis** (0.9955): prediction only, with no trials or publications.
- The remaining predictions are rare renal and inflammatory conditions with no supporting evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top predicted indication.

<!-- review:begin ca-lic-20261105-octreotide-1 -->

> **Review correction (2026-11-05)**: Originally stated: "These are 5 of the 14 valid single-ingredient authorizations. None are cancelled." Removed: the number or status of DINs stated here did not match the Health Canada DPD data (the Health Canada Drug Product Database as of 2026-11-05). The Quick Overview and the table under Canada Market Information show the current number and status of DINs. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261105-octreotide-1 -->

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02239323 | SANDOSTATIN LAR | OCTREOTIDE (OCTREOTIDE ACETATE) | Marketed |
| 02239324 | SANDOSTATIN LAR | OCTREOTIDE (OCTREOTIDE ACETATE) | Marketed |
| 02239325 | SANDOSTATIN LAR | OCTREOTIDE (OCTREOTIDE ACETATE) | Marketed |
| 02248639 | OCTREOTIDE ACETATE OMEGA | OCTREOTIDE (OCTREOTIDE ACETATE) | Marketed |
| 02248640 | OCTREOTIDE ACETATE OMEGA | OCTREOTIDE (OCTREOTIDE ACETATE) | Marketed |
| 02248641 | OCTREOTIDE ACETATE OMEGA | OCTREOTIDE (OCTREOTIDE ACETATE) | Marketed |
| 02248642 | OCTREOTIDE ACETATE OMEGA | OCTREOTIDE (OCTREOTIDE ACETATE) | Marketed |
| 02560240 | OCTREOTIDE INJECTION | OCTREOTIDE (OCTREOTIDE ACETATE) | Marketed |
| 02560283 | OCTREOTIDE INJECTION | OCTREOTIDE (OCTREOTIDE ACETATE) | Marketed |
| 02560291 | OCTREOTIDE INJECTION | OCTREOTIDE (OCTREOTIDE ACETATE) | Marketed |
| 02567776 | OCTREOTIDE DEPOT | OCTREOTIDE (OCTREOTIDE ACETATE) | Marketed |
| 02567784 | OCTREOTIDE DEPOT | OCTREOTIDE (OCTREOTIDE ACETATE) | Marketed |
| 02567792 | OCTREOTIDE DEPOT | OCTREOTIDE (OCTREOTIDE ACETATE) | Marketed |
| 00839191 | SANDOSTATIN | OCTREOTIDE (OCTREOTIDE ACETATE) | Dormant |
| 02503751 | OCTREOTIDE FOR INJECTABLE SUSPENSION | OCTREOTIDE (OCTREOTIDE ACETATE) | Cancelled post market |
| 02503778 | OCTREOTIDE FOR INJECTABLE SUSPENSION | OCTREOTIDE (OCTREOTIDE ACETATE) | Cancelled post market |
| 02503786 | OCTREOTIDE FOR INJECTABLE SUSPENSION | OCTREOTIDE (OCTREOTIDE ACETATE) | Cancelled post market |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

## Cytotoxicity

Octreotide is not a cytotoxic anticancer drug. It is a hormone-modulating peptide, so this section does not apply.

## Safety Considerations

- **Contraindications and disease associations (from the knowledge graph, not label text)**: hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, hypoglycaemia, hypothyroidism (including myxedema and congenital hypothyroidism), liver disease and cirrhosis, gallbladder disease and gallstones (cholelithiasis, cholecystolithiasis, choledocholithiasis), ileus, intestinal obstruction, sudden cardiac arrest, heart conduction disease, kidney failure, uraemia and vitamin B12 deficiency.
- **Drug Interactions**: 100 interactions were identified, and the 20 reviewed here are all Moderate severity. Most involve glucose-lowering agents, which fits the glycaemic effects above. Examples include insulins (aspart, degludec, detemir, glargine, glulisine, human), metformin, acarbose, glimepiride, chlorpropamide, the GLP-1 agonists albiglutide, dulaglutide and semaglutide, the DPP-4 inhibitors alogliptin and linagliptin, and the SGLT2 inhibitors canagliflozin, dapagliflozin and empagliflozin.

Please refer to the package insert for official warnings and contraindications, as label text was not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no trials or literature, and no plausible mechanism links somatostatin-receptor agonism to vulvar inverted follicular keratosis. Evidence is at level L5. The other top-ranked predictions are also unsupported or only weakly supported.

**To proceed, the following is needed:**
- Mechanism of action data for octreotide
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text and dosage forms for the Canadian licences
- A biological rationale or preclinical evidence linking somatostatin signalling to the predicted skin condition
- Review of other predictions with some biological plausibility, such as pituitary-related ACTH disorders, though current data are largely negative or indirect

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-05 | Removed: "These are 5 of the 14 valid single-ingredient authorizations. None are cancelled" | Corrected (revised 2026-11-24; earlier version kept in the record) | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Sandostatin (octreotide acetate) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4e2c9856-1836-49f0-9472-4dbeeb408f39) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

