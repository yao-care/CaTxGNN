---
layout: default
title: Carvedilol
parent: Model Prediction Only (L5)
nav_order: 161
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Carvedilol: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertension (hypertensive disorder)"
monitor_inn: "CARVEDILOL"
predicted_indications: ["malignant hypertensive renal disease"]
---

# Carvedilol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Carvedilol: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Carvedilol is a combined beta- and alpha-1 adrenergic blocker, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction. It is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, carvedilol is a non-selective beta-blocker with additional alpha-1 adrenergic blocking activity. Its blood-pressure-lowering efficacy in hypertension is established, so a mechanistic link to other hypertensive conditions is plausible.

Malignant renovascular hypertension is driven mainly by activation of the renin-angiotensin system due to renal artery stenosis. Carvedilol's beta-blockade can reduce renin release and its alpha-1 blockade causes vasodilation, so a partial benefit is conceivable. However, this is reasoning from general pharmacology, not evidence. Malignant hypertension is also usually an acute emergency managed with parenteral agents, which limits the relevance of an oral drug.

The TxGNN score (99.55%) is a model output only. No clinical trials or literature were found for this indication.

### Other Predicted Indications (for context)

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Malignant hypertensive renal disease | 99.55% | L5 | No trials or literature; acute emergency usually treated with parenteral agents |
| 3 | Pulmonary hypertension with unclear multifactorial mechanism | 99.54% | L5 | Beta-blockers are approached with caution because of right ventricular function concerns |
| 4 | Pulmonary hypertension owing to lung disease and/or hypoxia | 99.54% | L4 | Indirect preclinical evidence only (see below) |
| 5 | Braddock syndrome | 99.37% | L5 | Very rare genetic disorder; no plausible mechanistic link evident |

For rank 4, a rat study (PMID 26291659) found carvedilol reversed hypertension induced by chronic intermittent hypoxia, and a rat study of adrenergic blockade (PMID 20508210) reported reversal of right heart remodelling in pulmonary hypertensive rats. These are animal data measuring systemic blood pressure or right heart changes, not pulmonary arterial pressure in patients. A small crossover study (PMID 24798657) compared carvedilol with nifedipine on sleep blood pressure in hypertensive patients with sleep apnoea. Most other retrieved papers were off-target.

## Clinical Trial Evidence

Currently no related clinical trials registered for malignant renovascular hypertension.

## Literature Evidence

Currently no related literature available for malignant renovascular hypertension.

## Canada Market Information

Carvedilol is marketed in Canada with 20 valid single-ingredient licences (no combination products, none cancelled). The data compiled for this report do not include dosage forms or approved indication text. Five main authorizations:

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02324520 | CARVEDILOL | Not available | Not available |
| 02368900 | JAMP-CARVEDILOL | Not available | Not available |
| 02247935 | APO-CARVEDILOL | Not available | Not available |
| 02252309 | TEVA-CARVEDILOL | Not available | Not available |
| 02245914 | PMS-CARVEDILOL | Not available | Not available |

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: liver failure; asthma (including intrinsic and allergic asthma); bronchitis; pulmonary emphysema and bronchial disease; diabetes mellitus and diabetic ketoacidosis; hypotensive disorder; peripheral vascular disease (including intermittent claudication and peripheral arterial disease); atrioventricular block; sick sinus syndrome (including the familial form); Prinzmetal angina; anaphylaxis; intraoperative floppy iris syndrome.
- **Drug Interactions**: 100 interactions were identified. The main ones in the data compiled for this report:
  - **Major**: epinephrine.
  - **Moderate**: corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), anticholinergics (atropine, hyoscyamine), bupropion, morphine, lorcaserin, canagliflozin, acetohexamide, and calcium salts (phosphate, acetate, carbonate, citrate).
  - **Minor**: acetylsalicylic acid, aluminum hydroxide, attapulgite.
- **Relevance to the predicted indications**: The listed contraindications involving the lungs (asthma, emphysema, bronchial disease) and the caution regarding beta-blockers in pulmonary hypertension are directly relevant if pulmonary indications are pursued. Beta-blocker intoxication can also be severe (PMID 10862260).

Please refer to the package insert for label warnings, as these were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no clinical trials or literature for malignant renovascular hypertension (evidence level L5). Carvedilol is already marketed for hypertension in Canada, which is reassuring on availability, but this does not establish benefit in this specific, acute and severe condition.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A targeted literature and trial search for carvedilol in renovascular and malignant hypertension
- Review of the relevance of an oral agent to an emergency setting usually managed with parenteral therapy
- If pulmonary hypertension is pursued instead, a dedicated safety assessment of beta-blockade and right ventricular function, with clinical rather than animal-only evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

