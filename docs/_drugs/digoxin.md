---
layout: default
title: Digoxin
parent: Model Prediction Only (L5)
nav_order: 283
evidence_level: L5
indication_count: 5
monitor_inn: "DIGOXIN"
predicted_indications: ["Prinzmetal angina", "duodenal obstruction", "duodenal ulcer (disease)", "duodenogastric reflux", "hypoalphalipoproteinemia"]
last_modified_at: 2026-10-27
description: "Digoxin: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Not recorded in the local data"
---

# Digoxin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Digoxin: Cardiac glycoside (Na⁺/K⁺-ATPase inhibitor) → Prinzmetal angina
{: .text-alpha }

## One-Sentence Summary

Digoxin is a cardiac glycoside that is marketed in Canada under several single-ingredient licences.
The TxGNN model predicts it may be effective for **Prinzmetal angina**, but there are currently **0 clinical trials** and **1 publication** (an unrelated review of antihypertensive chronopharmacology) on file, so the support is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 0.9981 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 8 of 8) |
| Number of DINs | 8 (valid: 8) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, digoxin inhibits the Na⁺/K⁺-ATPase pump, which raises intracellular calcium and increases cardiac contractility, and it also has vagotonic effects.

Prinzmetal angina is caused by coronary artery vasospasm and is treated mainly with calcium channel blockers and nitrates. Digoxin has no recognized antispasmodic action, and the extra intracellular calcium could in theory worsen vasospasm. No direct mechanistic link between digoxin and this condition has been established. The high score (0.9981) is a model output only and should not be read as proof of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Review | Acta Physiol Pharmacol Bulg | General review of chronopharmacology and antihypertensive treatment; it does not address digoxin in vasospastic angina |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02498510 | JAMP DIGOXIN | Not recorded | Not recorded |
| 02335719 | PMS-DIGOXIN | Not recorded | Not recorded |
| 02498502 | JAMP DIGOXIN | Not recorded | Not recorded |
| 02335700 | PMS-DIGOXIN | Not recorded | Not recorded |
| 02554402 | AURO-DIGOXIN | Not recorded | Not recorded |

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the interaction screen. Moderate-level examples include acarbose, rabeprazole, doxycycline, epinephrine, hydrocortisone, metformin, amphotericin B, bupropion, dexamethasone and acetylsalicylic acid. Minor-level examples include albiglutide, hyoscyamine, atropine and glycopyrronium.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone. No clinical trial or publication directly studies digoxin in Prinzmetal angina, and the known pharmacology gives no support (and a theoretical concern about vasospasm).

**To proceed, the following is needed:**
- Mechanism of action data and a plausible vasospasm-related rationale
- Direct preclinical or clinical studies of digoxin in Prinzmetal angina
- Package insert warnings and contraindications from Health Canada, to start safety screening
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

