---
layout: default
title: Salbutamol
parent: Model Prediction Only (L5)
nav_order: 833
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-05
monitor_inn: "SALBUTAMOL"
predicted_indications: ["papillary conjunctivitis", "nasal cavity disease", "pharyngitis", "acute laryngopharyngitis", "anaphylaxis", "common cold", "atopic conjunctivitis", "anorectal stricture"]
description: "Salbutamol: predicted new indication Papillary conjunctivitis (evidence level L5). In Canada: 15 DINs (15 marketed)"
---

# Salbutamol
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

## Salbutamol: Papillary conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Salbutamol is a short-acting beta-2 adrenergic agonist that is marketed in Canada in several inhaled and injectable products.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**, with a score of 0.9999.
However, **no clinical trials and no publications** were found for this disease, so the prediction currently rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 15 of 15) |
| Number of DINs | 15 (marketed: 15) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for salbutamol: "Albuterol sulfate is a beta 2 -adrenergic agonist. The pharmacologic effects of albuterol sulfate are attributable to activation of beta 2 -adrenergic receptors on airway smooth muscle. Activation of beta 2 -adrenergic receptors leads to the activation of adenylcyclase and to an increase in the intracellular concentration of cyclic-3', 5’-adenosine monophosphate (cyclic AMP)." ([DailyMed: Albuterol Sulfate Inhalation (albuterol sulfate) prescribing information, Amneal Pharmaceuticals NY LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2e449282-ee58-4e36-b983-85c4e6f0864d), label version 2024-12-20; accessed 2026-11-19.) Based on general pharmacology, salbutamol activates beta-2 adrenergic receptors. Preclinical work on beta-2 agonists has suggested anti-inflammatory and mast-cell-stabilizing effects in conjunctival tissue, which could in theory be relevant to an allergic eye condition such as papillary conjunctivitis.

This link is speculative. No clinical trial or publication retrieved for this report studies salbutamol in papillary conjunctivitis, so the prediction cannot be considered supported beyond the model score. Because there is no direct study of this disease, the evidence level is L5.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02208229 | PMS-SALBUTAMOL | Not listed | Not listed |
| 02326450 | TEVA-SALBUTAMOL HFA | Not listed | Not listed |
| 02243115 | VENTOLIN DISKUS | Not listed | Not listed |
| 02241497 | VENTOLIN HFA | Not listed | Not listed |
| 02213486 | VENTOLIN RESPIRATOR SOLUTION | Not listed | Not listed |

All 15 licences in the local records are currently valid; the five above are shown as examples.

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the interaction databases. Examples at moderate level include acarbose, epinephrine, famotidine, clarithromycin, cisapride, and several antidiabetic drugs (e.g., alogliptin, canagliflozin, dapagliflozin, chlorpropamide). Corticosteroids such as hydrocortisone, budesonide, and dexamethasone are listed at minor level.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there are no clinical trials or publications on salbutamol in papillary conjunctivitis. The only supporting idea is a general, preclinical anti-inflammatory effect of beta-2 agonists in the conjunctiva, which is not enough to justify moving forward.

**To proceed, the following is needed:**
- Preclinical or early clinical data directly studying salbutamol, or a topical ocular formulation, in papillary conjunctivitis
- Mechanism of action data
- Assessment of whether an ocular route of administration is feasible, since the current Canadian products are inhaled or injectable
- Review of package insert warnings and contraindications, including cardiovascular and metabolic cautions

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available for this drug" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Albuterol Sulfate Inhalation (albuterol sulfate) prescribing information, Amneal Pharmaceuticals NY LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2e449282-ee58-4e36-b983-85c4e6f0864d) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

