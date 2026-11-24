---
layout: default
title: Folic Acid
parent: Model Prediction Only (L5)
nav_order: 408
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "FOLIC ACID"
predicted_indications: ["biotin metabolic disease"]
description: "Folic Acid: predicted new indication Biotin metabolic disease (evidence level L5). In Canada: 9 DINs (7 marketed, 2 dormant)"
---

# Folic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Folic Acid: Biotin metabolic disease
{: .text-alpha }

## One-Sentence Summary

Folic acid (vitamin B9) is originally used to treat vitamin deficiency disorders and folate-deficiency and other deficiency anemias.
The TxGNN model predicts it may be effective for **biotin metabolic disease**,
but there are currently **0 registered clinical trials** and only **indirect literature** (mostly general reviews on B vitamins), so this prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Biotin metabolic disease |
| TxGNN Prediction Score | 0.9949 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 7 of 9; dormant: 2) |
| Number of DINs | 9 (marketed: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for folic acid: "Folic acid acts on megaloblastic bone marrow to produce a normoblastic marrow. In man, an exogenous source of folate is required for nucleoprotein synthesis and the maintenance of normal erythropoiesis. Folic acid is the precursor of tetrahydrofolic acid, which is involved as a cofactor for transformylation reactions in the biosynthesis of purines and thymidylates of nucleic acids." ([DailyMed: Quiofic (folic acid) prescribing information, Solubiomix, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b868b314-591d-458b-be82-2bcd0b73cce1), label version 2026-10-05; accessed 2026-11-19.) Based on known information, folic acid is a water-soluble B vitamin whose efficacy in folate-deficiency anemia is established, and it may be mechanistically linked to biotin metabolic disease only through shared vitamin-dependent metabolism.

Folate supports one-carbon transfer reactions, such as nucleotide synthesis and homocysteine remethylation. Biotin is a cofactor for carboxylases such as propionyl-CoA carboxylase and pyruvate carboxylase. The two vitamins therefore sit in a related, vitamin-responsive metabolic network.

This link is weak, however. Biotin metabolic diseases (for example biotinidase deficiency and holocarboxylase synthetase deficiency) result from defects in biotin recycling or attachment, and the standard treatment is biotin supplementation. Nothing shows that folic acid corrects these underlying enzyme defects. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence or a validated therapeutic relationship.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The 18 publications retrieved are mostly narrative reviews of B vitamins in general. None tests folic acid as a treatment for biotin metabolic disease. The most relevant are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Review | Handbook of Clinical Neurology | Reviews vitamin-responsive disorders (cobalamin, folate, biotin, B1, E); describes inborn errors of vitamin absorption, transport and metabolism |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Review | Int J Mol Sci | Vitamin B12 deficiency and the nervous system; notes B12's role alongside biotin and folate in key biochemical reactions |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review | Acta Vitaminol Enzymol | Vitamins in metabolic diseases: malabsorption, errors of vitamin metabolism and vitamin-dependent syndromes, which may need pharmacological doses |
| [14989256](https://pubmed.ncbi.nlm.nih.gov/14989256/) | 2004 | Review | Arch Biochem Biophys | Deficiency of B12, folic acid, B6, C, E, iron or zinc may damage DNA; argues for supplements to optimise metabolism |
| [37123774](https://pubmed.ncbi.nlm.nih.gov/37123774/) | 2023 | Review | Cureus | Vitamins and type 2 diabetes; thiamine, pyridoxine and biotin levels are lower in people with diabetes |
| [25388747](https://pubmed.ncbi.nlm.nih.gov/25388747/) | 2015 | Review | Endocr Metab Immune Disord Drug Targets | Individual and combined vitamins in type 2 diabetes |
| [41692080](https://pubmed.ncbi.nlm.nih.gov/41692080/) | 2026 | Review | Clinics in Dermatology | B vitamins in cellular metabolism and erythrocyte synthesis, with a dermatology focus |
| [13199008](https://pubmed.ncbi.nlm.nih.gov/13199008/) | 1954 | Animal study | Biologica Latina | Combined biotin and folic acid deficiency induced in rats on a purified diet with phthalylsulfathiazole |

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 00426849 | FOLIC ACID | FOLIC ACID | Marketed |
| 02100606 | MULTI 12 | ASCORBIC ACID; BIOTIN; DEXPANTHENOL; FOLIC ACID; NICOTINAMIDE; PYRIDOXINE HYDROCHLORIDE; VITAMIN A; VITAMIN B… | Marketed |
| 02139480 | FOLIC ACID INJECTION, USP | FOLIC ACID (SODIUM FOLATE) | Marketed |
| 02242529 | MULTI-12/K1 PEDIATRIC | ASCORBIC ACID (ASCORBIC ACID); BIOTIN; DEXPANTHENOL; FOLIC ACID; NICOTINAMIDE; PYRIDOXINE HYDROCHLORIDE; VITA… | Marketed |
| 02366061 | JAMP-FOLIC ACID | FOLIC ACID | Marketed |
| 02552620 | PREGVIT | ASCORBIC ACID; BETA-CAROTENE; CALCIUM (CALCIUM CARBONATE); COPPER (CUPRIC OXIDE); D-PANTOTHENIC ACID (CALCIUM… | Marketed |
| 02552639 | PREGVIT FOLIC 5 | ASCORBIC ACID (ASCORBIC ACID); BETA-CAROTENE; CALCIUM (CALCIUM CARBONATE); COPPER (CUPRIC OXIDE); D-PANTOTHEN… | Marketed |
| 02535718 | PREGNANCY MULTIVITAMIN | ASCORBIC ACID (ASCORBIC ACID); BETA-CAROTENE; CALCIUM (CALCIUM CARBONATE); COPPER (COPPER GLUCONATE); D-PANTO… | Dormant |
| 02537478 | PREGNANCY MULTIVITAMIN FOLIC 5 | ASCORBIC ACID; BETA-CAROTENE; CALCIUM (CALCIUM CARBONATE); COPPER (COPPER GLUCONATE); D-PANTOTHENIC ACID (CAL… | Dormant |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

The table above lists each DIN with its current status in the DPD.

<!-- review:begin ca-lic-20261106-folic_acid-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Nine valid single-ingredient licences are registered in total; the five main ones are shown above." Removed: it described the products as single-ingredient or combination products in a way that did not match the Health Canada DPD data (the Health Canada Drug Product Database as of 2026-11-06). Revised 2026-11-24: the number of DINs and any reference to the earlier licence table, which showed only some of the DINs, were removed from the corrected sentence; the Quick Overview and the table under Canada Market Information show the current number and status of DINs. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261106-folic_acid-1 -->

## Safety Considerations

Package insert warnings and contraindications were not available. Please refer to the package insert for safety information.

- **Contraindication signals from the knowledge graph (not label text)**: The knowledge graph links folic acid to a long list of disease contraindications. These include kidney disease, nephrolithiasis, diabetes mellitus and diabetic ketoacidosis, bipolar disorder, peptic ulcer disease, inflammatory bowel disease and ulcerative colitis, sickle cell anemia, hemolytic anemia, hereditary hemochromatosis, Wilson disease, hypercalcemia and hyperparathyroidism. They should be verified against the official label before any use.
- **Drug Interactions**: The interaction screen returned 100 interacting drugs. Of the 20 reviewed, only two have a graded severity:
  - Moderate: pancrelipase
  - Minor: sulfasalazine
  - The rest are ungraded (severity unknown), including metformin, omeprazole, pantoprazole, lansoprazole, prednisone, simvastatin, morphine, mesalazine and vancomycin.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (L5). There are no clinical trials and no literature showing that folic acid treats biotin metabolic disease. The standard treatment is biotin itself, and the mechanistic link is only a shared vitamin network. Mechanism of action and label safety data are also missing.

**To proceed, the following is needed:**
- Mechanism of action data for folic acid (from DrugBank)
- Health Canada package insert warnings and contraindications (download and parse the PDF)
- Evidence that folic acid corrects, or adds benefit to, biotin-pathway defects (preclinical or clinical)
- Clarification of which specific biotin metabolic disorders are meant (for example biotinidase or holocarboxylase synthetase deficiency) and whether folic acid has any role next to biotin
- Review of the knowledge-graph contraindication signals against the official label
- Approved indication text and dosage forms for the Canadian licences

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "single-ingredient"; revised 2026-11-24 to remove the DIN count and the reference to the earlier licence table | Corrected (revised 2026-11-24; earlier version kept in the record) | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Quiofic (folic acid) prescribing information, Solubiomix, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b868b314-591d-458b-be82-2bcd0b73cce1) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

