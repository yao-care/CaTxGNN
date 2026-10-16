---
layout: default
title: Nebivolol
parent: Model Prediction Only (L5)
nav_order: 645
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Nebivolol: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension (hypertensive disorder)"
---

# Nebivolol
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

# Nebivolol: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Nebivolol is a beta-blocker originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but **no clinical trials and no directly relevant publications** currently support this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 9 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, nebivolol is a highly selective beta-1 blocker that also promotes nitric oxide-mediated vasodilation. Its efficacy in hypertension is established, and mechanistically it may be relevant to hypertensive end-organ damage.

Malignant hypertensive renal disease is a severe kidney complication of extreme blood pressure elevation, so it is closely related to the original indication. Blood pressure control and endothelial protection are plausible links. However, the connection rests on nebivolol's approved antihypertensive use, not on direct evidence in this kidney condition.

Other predictions with the same high score (99.4%) include malignant renovascular hypertension (beta-1 blockade reduces renin release, which is relevant because this condition is renin-driven), two forms of pulmonary hypertension, and Braddock syndrome. None has clinical trial support. For pulmonary hypertension in particular, beta-blockers may reduce cardiac output and right ventricular function, so safety in this setting is unestablished. For Braddock syndrome, no clear mechanistic connection can be identified, and the score is likely driven by knowledge-graph associations.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for malignant hypertensive renal disease.

For reference, the publications retrieved for the lower-ranked prediction of pulmonary hypertension are mostly indirect (preclinical organ-protection studies, beta-blocker studies in heart failure and at altitude), and none studies pulmonary hypertension directly. The most relevant human studies are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23506636](https://pubmed.ncbi.nlm.nih.gov/23506636/) | 2013 | Randomized comparative study | Int J Cardiol | CARNEBI trial: carvedilol vs nebivolol vs bisoprolol in moderate heart failure |
| [21883997](https://pubmed.ncbi.nlm.nih.gov/21883997/) | 2012 | Randomized placebo-controlled trial | Cardiovasc Ther | Nebivolol vs carvedilol on exercise performance in healthy subjects at high-altitude hypoxia |
| [21045724](https://pubmed.ncbi.nlm.nih.gov/21045724/) | 2011 | Clinical study | J Hypertens | Selective vs nonselective beta-blockade on 24-hour blood pressure under hypobaric hypoxia |
| [19789971](https://pubmed.ncbi.nlm.nih.gov/19789971/) | 2009 | Review | Cardiovasc Drugs Ther | Effects of beta-blockers on lung function in heart failure patients |
| [32128711](https://pubmed.ncbi.nlm.nih.gov/32128711/) | 2020 | Preclinical (animal) | Pharmacol Rep | Nebivolol protected against acute renal injury in rats, possibly via SGLT2 and the ERK-HIF1α pathway |
| [36947849](https://pubmed.ncbi.nlm.nih.gov/36947849/) | 2023 | Preclinical (animal) | Can J Physiol Pharmacol | Nebivolol reduced methotrexate nephrotoxicity in rats via AKT1/Hif-1α/eNOS signaling |
| [34693844](https://pubmed.ncbi.nlm.nih.gov/34693844/) | 2022 | Preclinical (animal) | Drug Chem Toxicol | Nebivolol alleviated methotrexate-induced liver damage via AKT1/Hif1α/eNOS signaling |
| [35202159](https://pubmed.ncbi.nlm.nih.gov/35202159/) | 2022 | Preclinical (in vitro) | Toxins | Nebivolol protected endothelial cells from aristolochic acid-induced oxidative stress |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02543508 | JAMP NEBIVOLOL | – | – |
| 02399016 | BYSTOLIC | – | – |
| 02399024 | BYSTOLIC | – | – |
| 02548704 | PRZ-NEBIVOLOL | – | – |
| 02548720 | PRZ-NEBIVOLOL | – | – |

There are 9 valid single-ingredient licences in total (no combination products, none cancelled). Dosage form and approved indication text were not available for these entries.

---

## Safety Considerations

**Contraindications / conditions of concern (from the drug-disease knowledge graph, not label text):**
liver failure, liver disease, gallbladder disease, diabetes mellitus, diabetic ketoacidosis, peripheral vascular disease, intermittent claudication, peripheral arterial disease, hypoglycemia, atrioventricular block, bronchial disease, sick sinus syndrome, familial sick sinus syndrome.

**Drug Interactions:** The interaction query returned 100 records. Most of those listed are of Moderate severity, including:
- Epinephrine, morphine, bupropion, lorcaserin
- Corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone)
- Anticholinergics (atropine, hyoscyamine, glycopyrronium, dicyclomine)
- Antidiabetic agents (canagliflozin, dapagliflozin, chlorpropamide)
- Calcium salts (calcium phosphate, calcium acetate)

Minor interactions include acetylsalicylic acid and magnesium oxide.

**Additional caution:** Beta-blockade may be harmful in pulmonary hypertension because of right ventricular dependence on heart rate and contractility. A preclinical study also reported that high-dose selective beta-1 blockade impaired cerebral perfusion after hemodilution in rats.

Please refer to the package insert for full warnings, as label-based warnings and contraindications are not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (99.4%), but there are no clinical trials and no direct literature for malignant hypertensive renal disease, so the evidence level is L5 (model prediction only). Nebivolol is already widely marketed in Canada for hypertension, which makes further evaluation feasible, but the prediction should not be acted on yet.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A targeted literature search and trial registry review for nebivolol in malignant hypertensive nephropathy
- Clinical data on nebivolol in severe or malignant hypertension with renal involvement
- Safety assessment for patients with the contraindicated conditions listed above, particularly bradyarrhythmias, hepatic impairment, and diabetes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

