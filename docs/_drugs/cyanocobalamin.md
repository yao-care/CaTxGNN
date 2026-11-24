---
layout: default
title: Cyanocobalamin
parent: Model Prediction Only (L5)
nav_order: 229
evidence_level: L5
indication_count: 1
monitor_inn: "Cyanocobalamin"
predicted_indications: ["biotin metabolic disease"]
last_modified_at: 2026-11-24
description: "Cyanocobalamin: predicted new indication biotin metabolic disease (evidence level L5). In Canada: 10 DINs (8 marketed, 2 dormant)"
---

# Cyanocobalamin
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

## Cyanocobalamin: Water-soluble vitamin B12 → biotin metabolic disease
{: .text-alpha }

## One-Sentence Summary

Cyanocobalamin is a synthetic form of vitamin B12 and is marketed in Canada in several products.
The TxGNN model predicts it may be relevant to **biotin metabolic disease**, but this rests on a model score alone: there are **no registered clinical trials** and only **1 general review** that does not directly study this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | biotin metabolic disease |
| TxGNN Prediction Score | 0.9960 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 8 of 10; dormant: 2) |
| Number of DINs | 10 (marketed: 8) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for cyanocobalamin: "CLINICAL PHAMRACOLOGY Vitamin B12 is essential to growth, cell reproduction, hematopoiesis, and nucleoprotein and myelin synthesis." ([DailyMed: cyanocobalamin prescribing information, SOLA Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e559c6c8-2973-77fb-e053-2995a90af43d), label version 2025-12-08; accessed 2026-11-19.) What is known is that it is a form of vitamin B12, a water-soluble B vitamin that acts as a cofactor in human metabolism.

A possible indirect link is that B12 and biotin are both water-soluble B vitamins that act as cofactors in related pathways. Adenosylcobalamin is needed by methylmalonyl-CoA mutase, while biotin is needed by propionyl-CoA carboxylase, and both enzymes work in propionate metabolism. This link is speculative.

The only cited publication is a 1992 review of biotechnological production of vitamins and coenzymes. It does not report any clinical use of cyanocobalamin in biotin-related disorders such as biotinidase or holocarboxylase synthetase deficiency. Standard care for biotin metabolic disease is biotin supplementation, and nothing in the data suggests that cyanocobalamin adds benefit. The high score (0.9960) is a model output only and should not be read as clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1368195](https://pubmed.ncbi.nlm.nih.gov/1368195/) | 1992 | Review | Journal of Chemical Technology and Biotechnology | General overview of biotechnological production of vitamins, coenzymes and related biochemicals; does not address cyanocobalamin treatment of biotin metabolic disease |

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 00521515 | VITAMIN B12 | VITAMIN B12 | Marketed |
| 01987003 | CYANOCOBALAMIN INJECTION USP | VITAMIN B12 | Marketed |
| 02100606 | MULTI 12 | ASCORBIC ACID; BIOTIN; DEXPANTHENOL; FOLIC ACID; NICOTINAMIDE; PYRIDOXINE HYDROCHLORIDE; VITAMIN A; VITAMIN B… | Marketed |
| 02242529 | MULTI-12/K1 PEDIATRIC | ASCORBIC ACID (ASCORBIC ACID); BIOTIN; DEXPANTHENOL; FOLIC ACID; NICOTINAMIDE; PYRIDOXINE HYDROCHLORIDE; VITA… | Marketed |
| 02463393 | CYANOCOBALAMIN INJECTION USP | VITAMIN B12 | Marketed |
| 02465507 | CYANOCOBALAMIN INJECTION USP | VITAMIN B12 | Marketed |
| 02552620 | PREGVIT | ASCORBIC ACID; BETA-CAROTENE; CALCIUM (CALCIUM CARBONATE); COPPER (CUPRIC OXIDE); D-PANTOTHENIC ACID (CALCIUM… | Marketed |
| 02552639 | PREGVIT FOLIC 5 | ASCORBIC ACID (ASCORBIC ACID); BETA-CAROTENE; CALCIUM (CALCIUM CARBONATE); COPPER (CUPRIC OXIDE); D-PANTOTHEN… | Marketed |
| 02535718 | PREGNANCY MULTIVITAMIN | ASCORBIC ACID (ASCORBIC ACID); BETA-CAROTENE; CALCIUM (CALCIUM CARBONATE); COPPER (COPPER GLUCONATE); D-PANTO… | Dormant |
| 02537478 | PREGNANCY MULTIVITAMIN FOLIC 5 | ASCORBIC ACID; BETA-CAROTENE; CALCIUM (CALCIUM CARBONATE); COPPER (COPPER GLUCONATE); D-PANTOTHENIC ACID (CAL… | Dormant |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

## Safety Considerations

**Drug Interactions**: 100 interactions were found in the interaction database. The ones listed here are mostly minor:
- Minor: famotidine, ranitidine, cimetidine, nizatidine, rabeprazole, omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole, potassium chloride. These are acid-reducing drugs and potassium chloride, which may reduce B12 absorption.
- Severity not classified: metformin, glimepiride, acarbose, rosiglitazone, mesalazine, doxycycline, morphine, sucralfate.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. No clinical trial or publication directly studies cyanocobalamin in biotin metabolic disease, and the standard treatment is biotin itself.

**To proceed, the following is needed:**
- Studies or case reports showing cyanocobalamin benefit in biotin metabolic disorders
- Mechanism-of-action data for cyanocobalamin
- Warnings and contraindications from the Health Canada package inserts
- Clarification of which biotin-related disorders are meant, and whether they have any unmet need beyond biotin therapy

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for cyanocobalamin is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: cyanocobalamin prescribing information, SOLA Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e559c6c8-2973-77fb-e053-2995a90af43d) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

