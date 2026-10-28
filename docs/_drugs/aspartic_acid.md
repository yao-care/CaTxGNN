---
layout: default
title: Aspartic Acid
parent: Model Prediction Only (L5)
nav_order: 76
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Aspartic Acid: predicted new indication Renal tubular acidosis (evidence level L5). Approved use: Potassium deficiency disease"
monitor_inn: "Aspartic acid"
predicted_indications: ["renal tubular acidosis"]
---

# Aspartic Acid
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

## Aspartic Acid: From Potassium Deficiency to Renal Tubular Acidosis
{: .text-alpha }

## One-Sentence Summary

Aspartic acid is a non-essential amino acid, originally associated with the treatment of potassium deficiency and used in parenteral nutrition products in Canada.
The TxGNN model predicts it may be effective for **renal tubular acidosis**, but there are currently **no registered clinical trials** and only **4 loosely related publications** (none testing aspartic acid as a treatment), so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Potassium deficiency disease |
| Predicted New Indication | Renal tubular acidosis |
| TxGNN Prediction Score | 0.9947 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 7 of 7) |
| Number of DINs | 7 (valid: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, aspartic acid is a non-essential amino acid. It is used for potassium deficiency (typically as potassium/magnesium aspartate salts) and is a component of amino acid solutions for parenteral nutrition.

A plausible but unverified rationale is that aspartate takes part in renal ammoniagenesis and acid-base handling through glutamine/glutamate/aspartate metabolism. Aspartate salts might also act as a potassium source or an alkali precursor, and potassium repletion is part of managing some forms of renal tubular acidosis.

However, this link is weak. Renal tubular acidosis is mainly caused by genetic or acquired defects in tubular transporters (for example SLC4A1/AE1 in distal RTA) or in bicarbonate reabsorption. Aspartic acid supplementation is not obviously able to correct these defects. Established treatment relies on alkali therapy (bicarbonate or citrate) and potassium repletion, and aspartic acid has no documented role in it. The prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26208211](https://pubmed.ncbi.nlm.nih.gov/26208211/) | 2015 | Diagnostic genetic study | Jornal de pediatria | Whole-exome sequencing gave a genetic diagnosis in four children with distal RTA; no aspartic acid treatment studied |
| [20068363](https://pubmed.ncbi.nlm.nih.gov/20068363/) | 2010 | Genetic case series | Nephron. Physiology | Distal RTA in Filipino children linked to SLC4A1 (AE1, Band 3) mutations; no aspartic acid treatment studied |
| [6422151](https://pubmed.ncbi.nlm.nih.gov/6422151/) | 1983 | Case report | Journal of inherited metabolic disease | Neonate with pyruvate carboxylase deficiency, proximal RTA and cystinuria; the patient began to thrive when the diet was supplemented with aspartic acid and other amino acids. Single case, confounded by multiple supplements |
| [14301365](https://pubmed.ncbi.nlm.nih.gov/14301365/) | 1965 | Basic physiology | American Journal of Physiology | Relationship of tubular cell pNH3 to renal ammonia production; background physiology only |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02141450 | 20% PROSOL | Not specified | Not specified |
| 02352540 | OLIMEL 5.7% | Not specified | Not specified |
| 02236875 | PRIMENE 10% | Not specified | Not specified |
| 02477947 | OLIMEL 7.6% | Not specified | Not specified |
| 02352494 | PERIOLIMEL 2.5% E | Not specified | Not specified |

Seven valid single-ingredient authorizations are listed in total; the five above are shown.

## Safety Considerations

- **Disease associations flagged as contraindications in the knowledge graph (not label text):** kidney disease, pyoureter, diarrheal disease, chronic diarrheal disease, atrioventricular block, hyperkalemic periodic paralysis, periodic paralysis, hypoaldosteronism, myotonia congenita, gastroparesis. Many of these relate to potassium load when aspartate is given as a potassium salt, so they are particularly relevant in kidney disease, the setting of renal tubular acidosis.

Please refer to the package insert for labelled warnings, contraindications and drug interaction information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (0.9947), but there are no clinical trials, the literature does not test aspartic acid for renal tubular acidosis, and the mechanistic link is not convincing. Established alkali and potassium therapies already exist, and the knowledge graph flags kidney disease as a contraindication.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (e.g., from DrugBank)
- Preclinical or mechanistic evidence that aspartic acid affects renal acid-base handling in RTA
- Review of the safety of potassium-containing aspartate salts in patients with impaired kidney function
- Comparison against standard alkali and potassium therapy to show any added benefit
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

