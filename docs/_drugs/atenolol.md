---
layout: default
title: Atenolol
parent: Model Prediction Only (L5)
nav_order: 78
evidence_level: L5
indication_count: 5
monitor_inn: "ATENOLOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-11-24
description: "Atenolol: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension"
---

# Atenolol
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

## Atenolol: From Hypertension to Malignant Hypertensive Renal Disease
{: .text-alpha }

## One-Sentence Summary

Atenolol is a beta-1 selective blocker, with hypertension and myocardial infarction among the uses recorded for it in the knowledge graph.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**.
This prediction has **no clinical trials and no publications** supporting it so far, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (a relation recorded in the knowledge graph; the Canadian licence records provide no indication text) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs on record: at least 15; dormant: 3; cancelled: 2) |
| Number of DINs | at least 20 |
| Number of approvals | At least 20 licences (the list may be partial) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for atenolol: "TENORMIN is a beta 1 -selective (cardioselective) beta-adrenergic receptor blocking agent without membrane stabilizing or intrinsic sympathomimetic (partial agonist) activities. This preferential effect is not absolute, however, and at higher doses, TENORMIN inhibits beta 2 -adrenoreceptors, chiefly located in the bronchial and vascular musculature." ([DailyMed: Tenormin (atenolol) prescribing information, Upsher-Smith Laboratories, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6e850b1e-28a4-4ff8-8ed7-bb0b29faa28a), label version 2025-09-18; accessed 2026-11-19.) Based on known information, atenolol is a beta-1 selective blocker that lowers blood pressure and reduces renin release. This is plausibly relevant to hypertensive kidney injury, because activation of the renin-angiotensin system drives malignant hypertension.

The link between the original and new indication is therefore a shared blood-pressure and renin pathway. However, this reasoning rests only on the TxGNN score. No trials or publications were found for this disease.

There are also practical concerns. Atenolol is cleared by the kidneys and needs dose adjustment in renal impairment. Malignant hypertension is usually managed with titratable intravenous agents, so an oral beta-blocker is unlikely to be first-line.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for malignant hypertensive renal disease.

Other predicted indications were also screened. Pulmonary hypertension owing to lung disease or hypoxia and chronic pulmonary heart disease returned literature. It was mostly preclinical or concerned hypertension and lung comorbidity, and it did not directly address malignant hypertensive renal disease.

## Canada Market Information

Health Canada records show atenolol single-ingredient products as valid and marketed. No dosage form or indication text was available in the records.

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 00773689 | APO-ATENOL TAB 50MG | ATENOLOL | Marketed |
| 02171791 | TEVA-ATENOLOL | ATENOLOL | Marketed |
| 02171805 | TEVA-ATENOLOL | ATENOLOL | Marketed |
| 02237600 | PMS-ATENOLOL | ATENOLOL | Marketed |
| 02237601 | PMS-ATENOLOL | ATENOLOL | Marketed |
| 02238316 | ATENOLOL | ATENOLOL | Marketed |
| 02238318 | ATENOLOL | ATENOLOL | Marketed |
| 02246581 | PMS-ATENOLOL | ATENOLOL | Marketed |
| 02266660 | TEVA-ATENOLOL | ATENOLOL | Marketed |
| 02267985 | TARO-ATENOLOL | ATENOLOL | Marketed |
| 02267993 | TARO-ATENOLOL | ATENOLOL | Marketed |
| 02367572 | JAMP-ATENOLOL | ATENOLOL | Marketed |
| 02368021 | MINT-ATENOL | ATENOLOL | Marketed |
| 02373963 | TARO-ATENOLOL | ATENOLOL | Marketed |
| 02541564 | ATENOLOL | ATENOLOL | Marketed |
| 02242093 | RIVA-ATENOLOL | ATENOLOL | Dormant |
| 02242094 | RIVA-ATENOLOL | ATENOLOL | Dormant |
| 02277379 | RIVA-ATENOLOL | ATENOLOL | Dormant |
| 02466465 | ATENOLOL | ATENOLOL | Cancelled post market |
| 02466473 | ATENOLOL | ATENOLOL | Cancelled post market |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

The data contain only part of the DINs for this ingredient; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** The knowledge graph links atenolol with contraindication to several conditions. These include asthma, atrioventricular block, diabetes mellitus (types 1 and 2) and diabetic ketoacidosis, Raynaud disease, anaphylaxis, liver failure, pancreatitis, systemic lupus erythematosus, psoriasis, gout, anuria, and anxiety-related disorders. These should be checked against the official label.
- **Drug Interactions:** 100 interactions were found. Those shown include moderate-level interactions with epinephrine, hydrocortisone, hyoscyamine, bupropion, triamcinolone, morphine, atropine, betamethasone, budesonide, and several calcium salts. Interactions with acetylsalicylic acid and aluminum hydroxide are minor.
- **Other considerations:** Atenolol needs dose adjustment in renal impairment. Beta-blockade may worsen bronchospasm and hypoxic states.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no trials or publications on malignant hypertensive renal disease, so the evidence level is L5. Kidney clearance of atenolol and its usual place behind parenteral agents in this condition further weaken the case.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Targeted literature review and any clinical data on beta-blockers in malignant hypertension with kidney involvement
- Renal dosing and safety evaluation in this population

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not currently available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Tenormin (atenolol) prescribing information, Upsher-Smith Laboratories, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6e850b1e-28a4-4ff8-8ed7-bb0b29faa28a) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

