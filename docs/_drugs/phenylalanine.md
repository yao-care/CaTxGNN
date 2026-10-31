---
layout: default
title: Phenylalanine
parent: Moderate Evidence (L3-L4)
nav_order: 731
evidence_level: L4
indication_count: 2
last_modified_at: 2026-10-31
description: "Phenylalanine: predicted new indication Sclerosing cholangitis (evidence level L4). Approved use: Not available"
monitor_inn: "PHENYLALANINE"
predicted_indications: ["sclerosing cholangitis", "congenital prothrombin deficiency"]
---

# Phenylalanine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **2** 
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

## Phenylalanine: From Parenteral Amino Acid Nutrition to Sclerosing Cholangitis
{: .text-alpha }

## One-Sentence Summary

Phenylalanine is an essential amino acid. In Canada it is marketed as a component of parenteral nutrition and amino acid solutions, although the data compiled for this report do not include indication text.
The TxGNN model predicts it may be effective for **sclerosing cholangitis**, but the evidence is weak: **0 clinical trials** and **3 publications**, all indirect, currently relate to this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication text in the licence data) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 0.9943 |
| Evidence Level | L4 |
| Canada Market Status | Marketed (valid licenses on record: at least 20) |
| Number of DINs | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, phenylalanine is an essential amino acid and a component of amino acid and parenteral nutrition products. Its role in protein synthesis is well established, but a mechanism for treating sclerosing cholangitis has not been identified.

The only loosely related literature is a cohort study of plasma tyrosine (a phenylalanine metabolite) and fatigue in primary biliary cirrhosis and primary sclerosing cholangitis. It suggests aromatic amino acid metabolism may be altered in cholestatic liver disease. It does not show that phenylalanine supplementation is therapeutic. The other two papers concern a cholangiocarcinoma serum metabolic signature and an assay of a phenylalanine-containing bacterial peptide; neither addresses treatment.

The very high TxGNN score (0.9943) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It should be read as a hypothesis, not as evidence of efficacy.

A second prediction, congenital prothrombin deficiency (score 0.9926), has no supporting trials or literature and no plausible mechanism. It is not pursued here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Cohort | BMC Gastroenterology | Examined amino acid patterns and plasma tyrosine in relation to fatigue in primary biliary cirrhosis and primary sclerosing cholangitis |
| [32025163](https://pubmed.ncbi.nlm.nih.gov/32025163/) | 2020 | Cohort | Journal of Clinical and Experimental Hepatology | Serum metabolic profiles of cholangiocarcinoma versus benign hepatobiliary disease, seeking biomarkers; not treatment-related |
| [2103382](https://pubmed.ncbi.nlm.nih.gov/2103382/) | 1990 | Preclinical/assay development | Journal of Gastroenterology and Hepatology | Radio-immunoassay showing enterohepatic circulation of bacterial chemotactic peptides (fMLP); not treatment-related |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02046709 | CLINIMIX | Not specified | Not specified |
| 02013932 | CLINIMIX | Not specified | Not specified |
| 02013940 | CLINIMIX | Not specified | Not specified |
| 00872296 | TRAVASOL | Not specified | Not specified |
| 02013886 | CLINIMIX | Not specified | Not specified |

Showing 5 of 20 valid single-ingredient licences. Other products include CLINIMIX E, OLIMEL, PRIMENE 10%, 20% PROSOL, ESSEPNA and SMOFKABIVEN.

## Safety Considerations

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for safety information.

Contraindication links in the TxGNN knowledge graph (not label text) list the following conditions:
- **Metabolic:** phenylketonuria and other disorders of phenylalanine metabolism, phosphorus metabolism disease
- **Renal:** kidney disease, chronic kidney disease, chronic renal failure, end stage renal failure, nephrolithiasis, nephrocalcinosis, acute urate nephropathy
- **Calcium-related:** hypercalcemia, humoral hypercalcemia of malignancy, sarcoidosis
- **Cardiac:** heart disease, cardiovascular disease, digitalis poisoning, ventricular fibrillation

Drug interaction data were not found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score with no clinical trials and only indirect literature. No mechanism links phenylalanine to sclerosing cholangitis. Safety label data are also missing, and the knowledge graph flags several renal, cardiac and metabolic contraindications.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) and a plausible mechanistic hypothesis for cholestatic liver disease
- Health Canada package insert warnings and contraindications, and approved indication text for the listed products
- Preclinical or mechanistic studies of phenylalanine or aromatic amino acid metabolism in sclerosing cholangitis
- A safety assessment for patients with liver disease, given the contraindications flagged in the knowledge graph
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

