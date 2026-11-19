---
layout: default
title: Cefuroxime
parent: Model Prediction Only (L5)
nav_order: 171
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-20
monitor_inn: "CEFUROXIME"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "Peptostreptococcus infectious disease", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy"]
description: "Cefuroxime: predicted new indication Hyperamylasemia (evidence level L5). In Canada: 9 DINs (9 marketed)"
---

# Cefuroxime
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Cefuroxime: Hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Cefuroxime is a beta-lactam antibiotic that inhibits bacterial cell-wall synthesis and is marketed in Canada in several single-ingredient products.
The TxGNN model predicts it may be effective for **hyperamylasemia**, but the data compiled for this report contain **no clinical trials and no publications** for this prediction.
The prediction is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 9 of 9) |
| Number of DINs | 9 (marketed: 9) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for cefuroxime: "Cefuroxime is a bactericidal agent that acts by inhibition of bacterial cell wall synthesis. Cefuroxime has activity in the presence of some beta-lactamases, both penicillinases and cephalosporinases, of Gram-negative and Gram-positive bacteria." ([DailyMed: cefuroxime sodium prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0a145288-733a-4966-b7ae-dc96eb103d8c), label version 2025-03-27; accessed 2026-11-19.) Cefuroxime belongs to the cephalosporin class of beta-lactam antibiotics, which block bacterial cell-wall synthesis.

For hyperamylasemia (elevated serum amylase), no plausible mechanistic link to this action has been identified. Nothing about cell-wall synthesis inhibition connects to amylase regulation. It should be treated as a hypothesis-generating signal, not as a rationale for use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02344831 | AURO-CEFUROXIME | Not specified | Not specified |
| 02241638 | CEFUROXIME FOR INJECTION, USP | Not specified | Not specified |
| 02244394 | APO-CEFUROXIME | Not specified | Not specified |
| 02344823 | AURO-CEFUROXIME | Not specified | Not specified |
| 02212307 | CEFTIN | Not specified | Not specified |

Nine single-ingredient licences are currently valid; the five above are a selection.

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the interaction screen. The ones listed here are all rated Moderate: acid-reducing agents (famotidine, ranitidine, cimetidine, nizatidine, omeprazole, rabeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole), antacids (aluminum hydroxide, calcium carbonate, magaldrate, magnesium carbonate, magnesium hydroxide, magnesium oxide), aminoglycosides (kanamycin, neomycin) and balsalazide.

Please also refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no supporting trials or publications and no plausible mechanistic link, so the evidence level is L5.

**To proceed, the following is needed:**
- Mechanism-of-action data and a biological rationale connecting cefuroxime to amylase regulation
- Any clinical or preclinical study that directly examines hyperamylasemia
- Review of the Health Canada package insert for warnings and contraindications

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: cefuroxime sodium prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0a145288-733a-4966-b7ae-dc96eb103d8c) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

