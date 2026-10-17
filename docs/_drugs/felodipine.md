---
layout: default
title: Felodipine
parent: Moderate Evidence (L3-L4)
nav_order: 379
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-13
description: "Felodipine: predicted new indication Pulmonary hypertension owing to lung disease and/or hypoxia (evidence level L4). Approved use: Hypertension (hypertensive disorder)"
monitor_inn: "FELODIPINE"
predicted_indications: ["pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "chronic pulmonary heart disease"]
---

# Felodipine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **7** 
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

# Felodipine: From Hypertension to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia

## One-Sentence Summary

Felodipine is a calcium channel blocker originally used to treat hypertension.
The TxGNN model predicts it may be effective for **pulmonary hypertension owing to lung disease and/or hypoxia**, but there are **0 registered clinical trials** and only **9 publications**, all preclinical or non-pulmonary models, so this prediction rests mainly on the model score.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Felodipine is a dihydropyridine L-type calcium channel blocker. It relaxes arterial smooth muscle and causes vasodilation, which is how it lowers blood pressure. Detailed mechanism-of-action data are not available in the data compiled for this report, so this description comes from its known drug class.

Hypoxic pulmonary vasoconstriction depends on calcium, so blocking calcium channels could in theory reduce pulmonary vascular tone. This gives the prediction a plausible mechanistic link.

However, the supporting literature has serious limits:
- The retrieved studies use rat kidney tubules, cerebral arteries, human atrial muscle, neutrophils and animal behaviour models. None studies pulmonary hypertension in patients.
- Guidelines generally discourage calcium channel blockers in pulmonary hypertension due to lung disease. They can inhibit protective hypoxic vasoconstriction and worsen gas exchange through ventilation-perfusion mismatch.

The mechanistic rationale is therefore plausible in theory but not supported by direct evidence, and it carries a real safety concern.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8160846](https://pubmed.ncbi.nlm.nih.gov/8160846/) | 1994 | Preclinical (vascular) | Am J Physiol | A prior anoxia episode reduced the vasorelaxation response to a later anoxia episode in rat aortic rings |
| [8584414](https://pubmed.ncbi.nlm.nih.gov/8584414/) | 1995 | Preclinical (rat tubules) | Pflugers Arch | Felodipine protected rat proximal tubules from hypoxic injury through a calcium-independent mechanism |
| [9431863](https://pubmed.ncbi.nlm.nih.gov/9431863/) | 1997 | Ex vivo (human atrial muscle) | Int J Cardiol | Felodipine pretreatment protected human atrial muscle from hypoxia-reoxygenation dysfunction in a stunning model |
| [3961832](https://pubmed.ncbi.nlm.nih.gov/3961832/) | 1986 | Preclinical (cerebral blood flow) | Stroke | Felodipine and nifedipine blunted the rise in rat cerebral blood flow during anoxia |
| [3343292](https://pubmed.ncbi.nlm.nih.gov/3343292/) | 1988 | Preclinical (rat cerebral cortex) | J Cereb Blood Flow Metab | Both drugs suppressed hypoxia-evoked adenosine and inosine release |
| [3142891](https://pubmed.ncbi.nlm.nih.gov/3142891/) | 1988 | Preclinical (cerebral arteries) | J Cereb Blood Flow Metab | Vasodilators affected reoxygenation- and calcium-induced contractions in dog cerebral arteries |
| [8394565](https://pubmed.ncbi.nlm.nih.gov/8394565/) | 1993 | Preclinical (cellular calcium) | Pflugers Arch | L-type calcium channel blockers, including felodipine, affected anoxia-induced rises in intracellular calcium in rabbit tubule cells |
| [8110031](https://pubmed.ncbi.nlm.nih.gov/8110031/) | 1993 | Preclinical (animal behaviour) | Arch Int Pharmacodyn Ther | Nicardipine, felodipine and nifedipine were tested on passive-avoidance learning in intact and hypoxia-exposed rats |
| [9864178](https://pubmed.ncbi.nlm.nih.gov/9864178/) | 1999 | Preclinical (neutrophils) | Blood | Nitric oxide modulated free radical generation by rat neutrophils after hypoxia-reoxygenation |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02280272 | SANDOZ FELODIPINE |
| 02057778 | PLENDIL |
| 02452367 | APO-FELODIPINE |
| 00851787 | PLENDIL |
| 00851779 | PLENDIL |

There are 8 valid single-ingredient licences in total (all currently valid, none cancelled). Only the first five are listed above.

---

## Safety Considerations

- **Contraindication signals from the knowledge graph** (these come from drug-disease relationships in the TxGNN knowledge graph, not from label text): kidney disease, liver disease, gallbladder disease, angioedema (several forms), neutropenia/agranulocytosis, aortic stenosis, hypotensive disorder, hypertrophic cardiomyopathy, renal artery obstruction, myocardial infarction, coronary artery disease/atherosclerosis, and others.
- **Drug interactions:** 100 interactions were found. The only one rated **Major** is dolasetron. **Moderate** ones include:
  - corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide)
  - CYP3A4-related drugs (clarithromycin, cimetidine, aprepitant)
  - bupropion, morphine, acetylsalicylic acid
  - SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin)
  - calcium salts, magnesium sulfate, dronabinol, nabilone
- **Indication-specific concern:** calcium channel blockers may worsen oxygenation in pulmonary hypertension due to lung disease (see above).

Package insert warnings and contraindications for the Canadian products were not available. Please refer to the package insert for label safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.91%), but there are no clinical trials and no patient studies in pulmonary hypertension. All literature is preclinical or from non-pulmonary models, and guidelines raise a gas-exchange safety concern for this class in this setting.

**To proceed, the following is needed:**
- Clinical evidence in pulmonary hypertension due to lung disease or hypoxia, ideally controlled studies with oxygenation and outcome endpoints
- Mechanism-of-action data and the Canadian package insert warnings and contraindications, to complete safety screening
- A review of the lower-ranked predictions from the same analysis. **Prinzmetal angina** (L2, Proceed with Guardrails) has the strongest evidence, with several small clinical studies from 1989–1995 including comparisons with nifedipine. **Chronic pulmonary heart disease** (L3) has small hemodynamic studies. Either may be a better candidate for further evaluation than the top-ranked prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

