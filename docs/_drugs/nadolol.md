---
layout: default
title: Nadolol
parent: Model Prediction Only (L5)
nav_order: 634
evidence_level: L5
indication_count: 5
---

# Nadolol
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

# Nadolol: From Beta-Blocker Therapy to Malignant Renovascular Hypertension

## One-Sentence Summary

> Nadolol is a non-selective beta-blocker that is marketed in Canada.
> The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
> but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on model output and class-level reasoning alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 (model prediction only; the source pack labelled it L4 on class-level mechanistic reasoning, but no actual studies were supplied) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for nadolol. Based on known information, nadolol is a non-selective beta-blocker. Beta-blockade lowers renin release, and renin activity is central to renovascular hypertension. This is indirect, class-level reasoning only.

The link between the two conditions is blood pressure control through renin suppression. There are also important reasons for caution:

- Malignant hypertension is a hypertensive emergency, usually managed with titratable IV agents. The role of an oral, long-acting beta-blocker is uncertain.
- Beta-blockers can worsen renal perfusion in bilateral renal artery stenosis.
- The TxGNN score is a model prediction, not clinical evidence.

**Other predicted indications** (all Hold, no clinical trials):

- **Malignant hypertensive renal disease** (99.59%, L4): This has the same rationale and an identical score, so it is likely a near-duplicate ontology node rather than an independent signal. Nadolol is renally cleared, so renal dosing would need consideration.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (99.53%, L5): No credible mechanistic link was found. The 20 retrieved publications concern general hypoxia biology (neurodegeneration, cancer, keloid, altitude), and none of the 10 titles shown mentions nadolol or pulmonary hypertension. This appears to be a keyword match. Non-selective beta-blockers may also worsen gas exchange and bronchospasm in lung disease.
- **Pulmonary hypertension with unclear multifactorial mechanism** (99.53%, L5): There is no evidence beyond the model score. Beta-blockers may reduce cardiac output and right ventricular function, so any effect may be harmful.
- **Braddock syndrome** (99.43%, L5): No mechanistic link could be established for this ultra-rare syndrome.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN / Licence No. | Product Name |
|---------|------|
| 782467 | APO-NADOLOL |
| 782475 | APO-NADOLOL |
| 782505 | APO-NADOLOL |
| 2496399 | MINT-NADOLOL |
| 2496380 | MINT-NADOLOL |

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction records were retrieved (the drug interaction query returned no results).

Indication-specific concerns from the mechanistic review:

- Possible worsening of renal perfusion in bilateral renal artery stenosis.
- Renal clearance of nadolol, so dose adjustment may be needed in renal impairment.
- Possible worsening of bronchospasm and gas exchange in lung disease.
- Possible reduction of cardiac output and right ventricular function in pulmonary hypertension.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high model score and indirect class-level reasoning, with no clinical trials or relevant publications. The disease context (hypertensive emergency) and the safety concerns above weaken the case further.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A targeted search for nadolol-specific studies in renovascular or malignant hypertension
- Approved indication text for the Canadian licences, to define the original indication and compare it with the new one
- Assessment of route and dosing suitability, since nadolol is oral and long-acting and the target condition is usually treated with IV agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

