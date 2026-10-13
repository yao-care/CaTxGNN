---
layout: default
title: Amlodipine
parent: Model Prediction Only (L5)
nav_order: 53
evidence_level: L5
indication_count: 10
---

# Amlodipine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Amlodipine: From Hypertension and Stroke to Brain Stem Infarction

## One-Sentence Summary

Amlodipine is a calcium channel blocker originally used to treat hypertension, stroke and cerebrovascular disorders, and Prinzmetal angina.
The TxGNN model's top-ranked prediction is **Brain Stem Infarction**, which currently has **no clinical trials and no publications** behind it. Among the ten predicted indications, the best-supported is **Intracerebral Hemorrhage** (recurrent stroke prevention), with **4 clinical trials** and **9 publications**, including one completed Phase 3 trial that tested a combination pill containing amlodipine.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder / hypertension, stroke and cerebrovascular disorders, cerebral infarction, Prinzmetal angina |
| Predicted New Indication | Brain stem infarction (top-ranked prediction) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

> The highest-ranked prediction is not the best-supported one. Intracerebral hemorrhage (score 99.79%, Evidence Level L1) is the most evidence-backed candidate and is covered in the supplementary section below.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, amlodipine is a calcium channel blocker that lowers blood pressure by reducing systemic vascular resistance. Its efficacy in hypertension and in cerebrovascular indications (stroke, cerebral infarction) is already recognised, and mechanistically it may be applicable to brain stem infarction.

Brain stem infarction is a type of ischaemic stroke. It is closely related to the cerebral infarction and stroke indications already linked to amlodipine, and blood pressure control is a key part of stroke prevention. This makes the prediction plausible. However, it is not direct evidence for brain stem infarction specifically, and it may overlap with existing indications rather than represent true repurposing.

## Clinical Trial Evidence

Currently no related clinical trials registered for brain stem infarction.

## Literature Evidence

Currently no related literature available for brain stem infarction.

## Supplementary: Other Predicted Indications

| Rank | Predicted Indication | Score | Evidence Level | Evidence Summary | Decision |
|---|---|---|---|---|---|
| 2 | Pulmonary hypertension owing to lung disease and/or hypoxia | 99.91% | L4 | No trials. Literature is mostly in vitro, animal or case reports. Vasodilators may worsen ventilation-perfusion matching, and amlodipine overdose is linked to non-cardiogenic pulmonary oedema | Hold |
| 3 | Pulmonary hypertension with unclear multifactorial mechanism | 99.91% | L5 | Prediction only. Calcium channel blockers are used only in a narrow vasoreactive subset | Hold |
| 4 | Malignant renovascular hypertension | 99.90% | L4 | Two paediatric case reports only | Hold |
| 5 | Malignant hypertensive renal disease | 99.90% | L5 | Prediction only | Hold |
| 6 | Cerebral artery occlusion | 99.89% | L3 | 3 trials (terminated or indirect), 5 rodent studies | Research question |
| 7 | Braddock syndrome | 99.88% | L5 | Prediction only, no clear mechanistic rationale | Hold |
| 8 | MRI-defined brain infarct | 99.86% | L5 | Prediction only, overlaps with the approved cerebral infarction indication | Hold |
| 9 | ABri amyloidosis | 99.84% | L5 | Prediction only, speculative link | Hold |
| 10 | Intracerebral hemorrhage | 99.79% | L1 | Completed Phase 3 TRIDENT trial (combination pill) | Proceed with Guardrails |

### Best-Supported Candidate: Intracerebral Hemorrhage

**Clinical trials**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Phase 3 | Completed | 1671 | TRIDENT main trial: double-blind, placebo-controlled test of a low-dose triple-combination blood-pressure pill (containing amlodipine) to prevent recurrent stroke after intracerebral haemorrhage |
| [NCT07458880](https://clinicaltrials.gov/study/NCT07458880) | N/A | Recruiting | 140 | Triple antihypertensive therapy after ICH for blood pressure control (TRICH score); no results yet |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | N/A | Terminated | 4 | TRIDENT MRI sub-study; too small for conclusions |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Terminated | 1 | TRIDENT cognitive sub-study; no analysable data |

**Literature**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42019018](https://pubmed.ncbi.nlm.nih.gov/42019018/) | 2026 | RCT | N Engl J Med | Three low-dose antihypertensives in a single pill after intracerebral haemorrhage (TRIDENT results) |
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | Trial design | Int J Stroke | Rationale and design of TRIDENT; single-pill combination for secondary prevention |
| [3154329](https://pubmed.ncbi.nlm.nih.gov/3154329/) | 1988 | Review | Cardiovasc Drugs Ther | Calcium antagonists in hypertension; decrease systemic vascular resistance |
| [19299323](https://pubmed.ncbi.nlm.nih.gov/19299323/) | 2009 | Case report | Ann Pharmacother | Probable amlodipine-induced angioedema in a patient with haemorrhagic stroke (safety signal) |

Amlodipine is only one component of the TRIDENT combination pill, so any benefit cannot be attributed to amlodipine alone.

## Canada Market Information

Amlodipine has 20 valid single-ingredient authorisations in Canada, with no cancelled licences. Dosage form and approved-indication text were not available for these products. The main ones are:

| DIN | Product Name |
|---------|------|
| 02490781 | AMLODIPINE |
| 02490803 | AMLODIPINE |
| 02468018 | M-AMLODIPINE |
| 02371707 | MAR-AMLODIPINE |
| 02522527 | PRZ-AMLODIPINE |

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text):** liver failure and liver disease, kidney disease, pancreatitis, gallbladder disease, hypothyroidism and myxedema, angioedema (including hereditary and RAAS-blocker-induced), systemic lupus erythematosus, myopathy and muscle disease, familial periodic paralysis, potassium deficiency, diabetes mellitus and diabetic ketoacidosis, neutropenia and agranulocytosis, hypotensive disorder, hyperparathyroidism. These come from model-derived drug-disease links and need verification against the product label.
- **Drug interactions:** 100 interactions were found, and the 20 listed are all rated Moderate. They include corticosteroids (hydrocortisone, betamethasone, budesonide, dexamethasone), aspirin, aprepitant, bupropion, clarithromycin, clotrimazole, SGLT2 inhibitors (canagliflozin, dapagliflozin) and multiple calcium salts.
- **Literature signals:** amlodipine overdose has been linked to non-cardiogenic pulmonary oedema and diffuse alveolar haemorrhage, and one case report links amlodipine to angioedema. A case report also suggests it may inhibit hypoxic pulmonary vasoconstriction.
- Hypotension risk should be considered in any blood-pressure-lowering strategy after stroke.

Please refer to the Health Canada package insert for official warnings and contraindications, as these were not available for this report.

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, brain stem infarction)

**Rationale:**
The top prediction has a very high model score but no trials or publications, and it overlaps with indications amlodipine already carries. The only candidate with strong clinical support is intracerebral hemorrhage (Proceed with Guardrails), but the evidence comes from a combination pill, not amlodipine alone.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- For brain stem infarction: any direct clinical or mechanistic evidence, and a check on whether it is truly distinct from the existing cerebral infarction indication
- For intracerebral hemorrhage: independent review of the TRIDENT results, an assessment of amlodipine's individual contribution, a hypotension monitoring plan, and confirmation of regulatory fit in Canada
- Dosage form and approved-indication data for the Canadian licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

