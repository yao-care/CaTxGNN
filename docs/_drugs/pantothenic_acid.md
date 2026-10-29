---
layout: default
title: Pantothenic Acid
parent: Model Prediction Only (L5)
nav_order: 705
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-30
monitor_inn: "Pantothenic acid"
predicted_indications: ["congenital prothrombin deficiency", "ochronosis disorder", "glycerol metabolism disease", "folic acid deficiency anemia", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "urinary tract infection (disease)", "gonococcal urethritis", "Ureaplasma urethritis"]
description: "Pantothenic Acid: predicted new indication Congenital prothrombin deficiency (evidence level L5). Approved use: Not recorded in the local data"
---

# Pantothenic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Pantothenic Acid: Congenital prothrombin deficiency
{: .text-alpha }

## One-Sentence Summary

Pantothenic acid (vitamin B5) was originally used for nutritional deficiency conditions, namely ascorbic acid deficiency and scurvy.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, but this prediction is **computational only, with no clinical trials and no publications** supporting it.
Among the other predicted indications, **folic acid deficiency anemia** and **uterine inflammatory disease** have the most (still indirect) supporting literature.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 3 of 5) |
| Number of DINs | 5 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, pantothenic acid is the precursor of coenzyme A (CoA), which is central to energy and lipid metabolism. It is used to correct vitamin deficiency states, but a mechanistic link to the predicted new indication cannot be established from the data compiled for this report.

For the top-ranked prediction, congenital prothrombin deficiency, no supporting mechanism was found. It is a genetic coagulation factor disorder, and pantothenic acid has no established role in prothrombin synthesis. The very high score (0.9996) reflects a model output only.

Other predictions have somewhat more context:
- **Folic acid deficiency anemia (score 0.9960)**: B-vitamin deficiencies often occur together, and a 1946 report and a 1986 primate review discuss pantothenic acid and folic acid deficiencies in relation to anemia. This suggests pantothenic acid is a co-factor in nutritional anemia, not a replacement for folic acid, which remains the standard treatment.
- **Uterine inflammatory disease (score 0.9914)**: One 2026 mouse study reports that pantothenic acid alleviated vagotomy-induced endometrial injury. The model differs from clinical endometritis, and there is no human data.
- **Glycerol metabolism disease (score 0.9977)**: CoA participates in lipid and glycerol-related metabolism, giving a weak, general rationale. The retrieved papers are profiling studies that do not test pantothenic acid.

## Clinical Trial Evidence

Currently no related clinical trials registered for congenital prothrombin deficiency, or for any of the other eight predicted indications.

## Literature Evidence

Currently no related literature available for congenital prothrombin deficiency.

The literature below relates to other predicted indications and is shown for context.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21021037](https://pubmed.ncbi.nlm.nih.gov/21021037/) | 1946 | Historical report | Nutrition Reviews | Anemia and granulocytopenia in relation to pantothenic acid and folic acid deficiencies (folic acid deficiency anemia) |
| [3724048](https://pubmed.ncbi.nlm.nih.gov/3724048/) | 1986 | Review | Laboratory Animal Science | Review of nutritional deficiency anemias in nonhuman primates, including pantothenic acid and folic acid deficiencies |
| [21929634](https://pubmed.ncbi.nlm.nih.gov/21929634/) | 2011 | Review | Maternal & Child Nutrition | Fortified foods in pregnancy help prevent maternal anemia and iron deficiency; not specific to pantothenic acid |
| [41223999](https://pubmed.ncbi.nlm.nih.gov/41223999/) | 2026 | Preclinical (mouse) | Mucosal Immunology | Pantothenic acid alleviated vagotomy-induced endometrial injury (uterine inflammatory disease) |
| [40272030](https://pubmed.ncbi.nlm.nih.gov/40272030/) | 2025 | Case series | Am J Med Genet A | Prenatal brain abnormalities in sodium-dependent multivitamin transporter deficiency, which is treatable with high-dose pantothenic acid, biotin and alpha lipoic acid; not related to the predicted UTI indication |

Five further papers retrieved for glycerol metabolism disease are metabolomics or microbiome profiling studies and do not test pantothenic acid, so they are not listed.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00586315 | MULTI 1000 | Not listed | Not listed |
| 02552639 | PREGVIT FOLIC 5 | Not listed | Not listed |
| 02535718 | PREGNANCY MULTIVITAMIN | Not listed | Not listed |
| 02552620 | PREGVIT | Not listed | Not listed |
| 02537478 | PREGNANCY MULTIVITAMIN FOLIC 5 | Not listed | Not listed |

All five licences are valid single-ingredient entries, with none cancelled.

## Safety Considerations

- **Disease associations flagged by the TxGNN model (deep learning), not label text**: kidney disease, pyoureter, sickle cell anemia, hereditary persistence of fetal hemoglobin, primary hyperoxaluria, hereditary hemochromatosis, hemosiderosis, iron metabolism disease and Wilson disease. These come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. They need verification against official labelling.
- **Drug interactions**: No interaction records were found.

Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, congenital prothrombin deficiency, rests on a model score alone, with no trials, no literature and no plausible mechanism. Evidence is at level L5. Folic acid deficiency anemia and uterine inflammatory disease reach only L4, from historical, review or single-animal-study evidence, so they are better treated as research questions than as repurposing candidates.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data for pantothenic acid
- Approved indication text and dosage forms for the Canadian products
- For uterine inflammatory disease, confirmation of the mouse findings in a model closer to clinical endometritis, followed by human data
- For folic acid deficiency anemia, clinical data showing a benefit beyond standard folic acid replacement
- Review of the knowledge-graph contraindications (kidney disease, iron metabolism disorders, Wilson disease and others) against official labelling
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

