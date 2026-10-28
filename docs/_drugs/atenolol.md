---
layout: default
title: Atenolol
parent: Model Prediction Only (L5)
nav_order: 78
evidence_level: L5
indication_count: 5
monitor_inn: "ATENOLOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-10-28
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
| Canada Market Status | Marketed (valid licenses on record: at least 20) |
| Number of DINs | at least 20 |
| Number of approvals | At least 20 licences (the list may be partial) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, atenolol is a beta-1 selective blocker that lowers blood pressure and reduces renin release. This is plausibly relevant to hypertensive kidney injury, because activation of the renin-angiotensin system drives malignant hypertension.

The link between the original and new indication is therefore a shared blood-pressure and renin pathway. However, this reasoning rests only on the TxGNN score. No trials or publications were found for this disease.

There are also practical concerns. Atenolol is cleared by the kidneys and needs dose adjustment in renal impairment. Malignant hypertension is usually managed with titratable intravenous agents, so an oral beta-blocker is unlikely to be first-line.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for malignant hypertensive renal disease.

Other predicted indications were also screened. Pulmonary hypertension owing to lung disease or hypoxia and chronic pulmonary heart disease returned literature. It was mostly preclinical or concerned hypertension and lung comorbidity, and it did not directly address malignant hypertensive renal disease.

## Canada Market Information

Health Canada records show atenolol single-ingredient products as valid and marketed. No dosage form or indication text was available in the records. Only the first 5 of at least 20 licences are listed below, and the full list may be partial.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02266660 | TEVA-ATENOLOL | Not stated | Not stated |
| 02171805 | TEVA-ATENOLOL | Not stated | Not stated |
| 02466465 | ATENOLOL | Not stated | Not stated |
| 02541564 | ATENOLOL | Not stated | Not stated |
| 02277379 | RIVA-ATENOLOL | Not stated | Not stated |

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

