---
layout: default
title: Isoprenaline
parent: Model Prediction Only (L5)
nav_order: 501
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
monitor_inn: "Isoprenaline"
predicted_indications: ["nasal cavity disease", "headache disorder", "pharyngitis", "acute laryngopharyngitis", "trigeminal autonomic cephalalgia", "bronchial disease", "endobronchial leiomyoma", "allergic urticaria", "endobronchial lipoma", "bronchus adenoma"]
description: "Isoprenaline: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Isoprenaline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Isoprenaline: Nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Isoprenaline (isoproterenol) is a non-selective beta-adrenergic agonist, originally used for conditions such as cardiac arrest and atrioventricular block.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but there are **no clinical trials** and only **1 unrelated case report** supporting this prediction.
The strongest supporting signal in the data is actually for a different prediction, **bronchial disease**, which is a historical use of the drug.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 3 of 3) |
| Number of DINs | 3 (valid: 3) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, isoprenaline is a non-selective beta-1/beta-2 adrenergic agonist. Its efficacy in cardiac conditions (heart rate and conduction support) is established, and mechanistically it could influence nasal mucosal blood vessels and secretions through adrenergic pathways.

However, this link is only theoretical. The single paper retrieved for this prediction is a case report of coronary artery spasm and ventricular tachycardia during surgery, in which epinephrine-soaked nasal packing was used. It has no bearing on treating nasal disease. The high score of 0.9995 comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as the listed cold and nasopharyngitis indications, not biological evidence.

**Other predictions worth noting:**

| Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|
| Headache disorder | 0.9994 | L4 | Mechanistic studies only, with isoprenaline used as a research probe. As a vasodilator, it could plausibly provoke headache rather than treat it. |
| Pharyngitis | 0.9994 | L5 | The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as the existing cold indication, not biological evidence. No literature and no clear mechanism. |
| Acute laryngopharyngitis | 0.9993 | L5 | Same pattern as pharyngitis. |
| Trigeminal autonomic cephalalgia | 0.9992 | L4 | One mechanistic paper on cluster headache, which overlaps with the headache evidence. |
| Bronchial disease | 0.9977 | L4 | The best mechanistic fit. Isoprenaline is a bronchodilator that was historically used in asthma. It was displaced by selective beta-2 agonists because of cardiac effects and asthma mortality concerns. It is a rediscovery of past use, not a new opportunity. |
| Endobronchial leiomyoma, endobronchial lipoma, bronchus adenoma | 0.9964–0.9968 | L5 | Rare airway tumours. No plausible mechanism and no evidence. The scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. |
| Allergic urticaria | 0.9967 | L5 | Weak, speculative mast-cell stabilisation link, with unattractive cardiovascular risks. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Only one publication was retrieved for nasal cavity disease, and it is not relevant to the predicted indication.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14711196](https://pubmed.ncbi.nlm.nih.gov/14711196/) | 2003 | Case report | Japanese Heart Journal | Perioperative ventricular tachycardia in a 26-year-old man after nasal epinephrine packing and intubation. Coronary artery spasm was found on work-up. It is unrelated to treating nasal disease. |

**Supporting literature for the better-evidenced bronchial disease prediction (selected):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27878470](https://pubmed.ncbi.nlm.nih.gov/27878470/) | 2017 | Review | Handb Exp Pharmacol | Beta-agonists remain frontline bronchodilators for asthma and COPD. |
| [11534892](https://pubmed.ncbi.nlm.nih.gov/11534892/) | 2001 | Review | Respiratory Medicine | Asthma mortality epidemics were linked to high-dose isoprenaline in the 1960s. Selective beta-2 agonists are now vital. |
| [29906501](https://pubmed.ncbi.nlm.nih.gov/29906501/) | 2018 | Review | Adv Drug Deliv Rev | Describes isoprenaline's history as an inhaled asthma therapy and its unwanted effects. |
| [15715182](https://pubmed.ncbi.nlm.nih.gov/15715182/) | 2005 | Review | Respiratory Medicine | Early agents such as isoprenaline lacked bronchial selectivity and had cardiac side effects. |
| [5411446](https://pubmed.ncbi.nlm.nih.gov/5411446/) | 1970 | Clinical comparison | Br Med J | In 13 asthmatic patients, isoprenaline and salbutamol were equipotent bronchodilators, but isoprenaline caused greater increases in pulse rate and blood pressure. |
| [5440568](https://pubmed.ncbi.nlm.nih.gov/5440568/) | 1970 | Clinical comparison | Br Med J | In 11 asthmatic subjects, both drugs reduced airway obstruction similarly. Isoprenaline caused tachycardia and a small fall in arterial oxygen tension. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02502623 | Isoproterenol Hydrochloride Injection USP | Not listed | Not listed |
| 00897639 | Isoproterenol Hydrochloride Injection USP | Not listed | Not listed |
| 02502615 | Isoproterenol Hydrochloride Injection USP | Not listed | Not listed |

All three licences are valid single-ingredient injection products.

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** hypertension, diabetes mellitus, diabetic ketoacidosis, coronary artery disease, myocardial infarction, coronary thrombosis, hemoglobinopathy, hyperthyroidism, Graves disease and thyrotoxicosis.
- **Drug interactions:** 100 interactions were identified. Examples:
  - **Major:** dolasetron.
  - **Moderate:** epinephrine, isometheptene, diethylpropion, clarithromycin, famotidine, and several antidiabetic agents (acarbose, alogliptin, canagliflozin, chlorpropamide, dapagliflozin, empagliflozin, albiglutide, dulaglutide).
  - **Minor:** corticosteroids such as hydrocortisone, dexamethasone, budesonide, betamethasone, triamcinolone and beclomethasone.
- **Repurposing-specific concern:** systemic isoprenaline has strong beta-1 cardiac effects (tachycardia, arrhythmia risk). This is a significant liability for any non-cardiac use, and the available literature links high-dose isoprenaline to increased asthma mortality.

Please refer to the package insert for warnings and contraindications, as label text was not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The nasal cavity disease prediction has a very high model score but no clinical trials, and its only publication is unrelated. The score appears to reflect proximity to the existing cold and nasopharyngitis indications rather than real evidence. Across the other predictions, the only mechanistically credible one is bronchial disease, which is a historical use already replaced by safer selective beta-2 agonists. The injectable formulation and cardiac risk profile further reduce attractiveness for upper airway or headache indications.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data for isoprenaline
- Any direct preclinical or clinical evidence for isoprenaline in nasal disease
- Evaluation of whether a non-systemic route (topical or inhaled) is feasible, since only injectable products are currently licensed in Canada
- A comparison against selective beta-2 agonists if bronchial disease is pursued as a research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

