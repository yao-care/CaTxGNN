---
layout: default
title: Valine
parent: Moderate Evidence (L3-L4)
nav_order: 962
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-28
description: "Valine: predicted new indication Sclerosing cholangitis (evidence level L4). Approved use: Not available"
monitor_inn: "Valine"
predicted_indications: ["sclerosing cholangitis", "angle-closure glaucoma", "hyperthyroidism", "traumatic glaucoma", "aqueous misdirection", "neovascular glaucoma", "glaucomatous atrophy of optic disc", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "obsolete bundle branch block", "hyperthyroxinemia"]
---

# Valine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

## Valine: From Parenteral Nutrition Amino Acid Component to Sclerosing Cholangitis
{: .text-alpha }

## One-Sentence Summary

Valine is an essential branched-chain amino acid (BCAA) used as a component of parenteral nutrition amino acid solutions in Canada.
The TxGNN model predicts it may be effective for **sclerosing cholangitis**,
but there are currently **no registered clinical trials** and only **2 publications** (observational or genetic-causal studies), so this remains a model prediction with indirect support only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication text in the Canadian licence records; products are parenteral nutrition amino acid solutions) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 0.9942 |
| Evidence Level | L4 |
| Canada Market Status | Marketed (valid licenses on record: at least 20) |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, valine is a branched-chain amino acid and a component of parenteral nutrition products. It serves as a nutritional substrate, and its mechanistic applicability to sclerosing cholangitis is only indirect.

The link to sclerosing cholangitis comes from altered amino acid metabolism in cholestatic liver disease, notably an imbalance between aromatic amino acids and BCAAs. A Mendelian randomization study has examined blood metabolites and their causal relationship with primary biliary cholangitis and primary sclerosing cholangitis. A cohort study has also examined plasma amino acid patterns, specifically tyrosine, and fatigue in these patients.

These are associations in metabolism, not evidence that valine supplementation treats the disease. No interventional study shows a therapeutic benefit. The high TxGNN score is a computational prediction only.

## Literature Evidence

Currently no related clinical trials are registered.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39015781](https://pubmed.ncbi.nlm.nih.gov/39015781/) | 2024 | Mendelian randomization | Frontiers in Medicine | Examines causal links between blood metabolites and metabolic pathways and the risk of primary biliary cholangitis and primary sclerosing cholangitis |
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Cohort | BMC Gastroenterology | Studies abnormal amino acid patterns and the relation between plasma tyrosine and fatigue in primary biliary cirrhosis and primary sclerosing cholangitis |

## Canada Market Information

Licence records for these products do not include dosage form or approved indication text. The products are single-ingredient authorizations, all valid, and the 5 listed here are a selection from 20.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02046709 | CLINIMIX | Not specified | Not specified |
| 02013932 | CLINIMIX | Not specified | Not specified |
| 00872296 | TRAVASOL | Not specified | Not specified |
| 02141450 | 20% PROSOL | Not specified | Not specified |
| 02236875 | PRIMENE 10% | Not specified | Not specified |

Other authorized products include further CLINIMIX and CLINIMIX E strengths, ESSEPNA, OLIMEL 7.6% and 5.7%, and SMOFKABIVEN (including the extra nitrogen version).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on indirect metabolic associations only. There are no clinical trials and no interventional evidence that valine supplementation treats sclerosing cholangitis. Valine is also already widely marketed in Canada as a nutritional component, but that gives no information on this new use.

**To proceed, the following is needed:**
- Mechanism of action data, and a clearer rationale for how valine or BCAA modulation could affect cholestatic disease
- Safety information from Canadian package inserts (warnings and contraindications), particularly for patients with liver impairment
- Preclinical or early-phase studies testing BCAA or valine supplementation in cholestatic liver disease
- Approved indication text for the Canadian products, to define the original indication and available routes

**Notes on other predictions:** The other nine predicted indications (angle-closure glaucoma, hyperthyroidism, traumatic glaucoma, aqueous misdirection, neovascular glaucoma, glaucomatous optic disc atrophy, resistance to thyroid hormone, obsolete bundle branch block, hyperthyroxinemia) have no clinical trials and no credible therapeutic rationale. Much of the retrieved literature concerns receptor mutations in which "valine" is only an amino acid residue, not the drug. Their scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, and all are rated Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

