---
layout: default
title: Folic Acid
parent: Model Prediction Only (L5)
nav_order: 408
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
monitor_inn: "FOLIC ACID"
predicted_indications: ["biotin metabolic disease"]
description: "Folic Acid: predicted new indication Biotin metabolic disease (evidence level L5). Approved use: Not recorded in the local data"
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
| Canada Market Status | Marketed (valid licenses: 9 of 9) |
| Number of DINs | 9 (valid: 9) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, folic acid is a water-soluble B vitamin whose efficacy in folate-deficiency anemia is established, and it may be mechanistically linked to biotin metabolic disease only through shared vitamin-dependent metabolism.

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

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00426849 | FOLIC ACID | Not specified | Not specified |
| 02366061 | JAMP-FOLIC ACID | Not specified | Not specified |
| 02139480 | FOLIC ACID INJECTION, USP | Injection | Not specified |
| 02100606 | MULTI 12 | Not specified | Not specified |
| 02242529 | MULTI-12/K1 PEDIATRIC | Not specified | Not specified |

Nine valid single-ingredient licences are registered in total; the five main ones are shown above.

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

