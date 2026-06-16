---
layout: default
title: Ergometrine
parent: 僅模型預測 (L5)
nav_order: 291
evidence_level: L5
indication_count: 10
---

# Ergometrine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Ergometrine: From Oxytocic Agent to Migraine Disorder

## One-Sentence Summary

Ergometrine is an ergot alkaloid oxytocic agent historically used for preventing and treating postpartum hemorrhage and uterine atony.
The TxGNN model generates 10 predicted indications; **migraine disorder (rank #7)** is the only prediction with biological plausibility and literature support, backed by **20 publications** documenting the use of ergometrine and structurally related ergot derivatives in migraine prophylaxis.
Critically, two predicted indications — pulmonary hypertension (rank #10) and migraine with brainstem aura (rank #8) — are identified in the retrieved literature as **absolute contraindications**, not treatment targets; ranks #1–6 appear to be knowledge graph sparsity artifacts with no supporting evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Postpartum hemorrhage prevention and uterine atony (known pharmacological use; no Health Canada DIN on record) |
| Most Evidence-Supported Predicted Indication | Migraine disorder (TxGNN rank #7 of 10) |
| TxGNN Prediction Score | 99.93% (migraine, rank #7); highest-ranked prediction hypertrichosis at 99.96% is a KG artifact |
| Evidence Level | L4 — historical case series and observational studies (migraine); L5 for all other ranked indications |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, ergometrine (ergonovine) is an ergot alkaloid that acts as a partial agonist at α-adrenergic, serotonin (5-HT₂), and dopamine receptors, producing potent smooth muscle contraction — particularly in the uterus and vascular walls. Its established clinical role is in obstetrics for postpartum uterine contraction and hemorrhage control.

The connection to migraine is grounded in ergot alkaloid pharmacology. Ergot derivatives have a long history as migraine treatments: ergotamine and dihydroergotamine (DHE) remain pharmacopoeial options for acute migraine, and methysergide — explicitly described in the literature (PMID 9793694) as a "semisynthetic ergot alkaloid ergometrine derivative" — was for decades a standard prophylactic agent via 5-HT₁ agonism and 5-HT₂ antagonism. Methylergonovine, the direct N-methyl homolog of ergometrine, has been specifically studied for refractory migraine and cluster headache (PMID 23432443, 19895705). The trigeminal vascular hypothesis of migraine implicates 5-HT₁B/1D receptor–mediated cerebral vasoconstriction as a key therapeutic mechanism, which overlaps directly with ergometrine's receptor profile.

However, the same vasoconstrictive properties that may confer anti-migraine activity also generate a clinically significant safety burden: coronary artery vasospasm, QT prolongation, hypertensive crisis, and — of particular relevance — reversible cerebral vasoconstriction syndrome (RCVS) in migraine-with-aura patients. Modern migraine management has largely moved away from ergot vasoconstrictors toward triptans and CGRP pathway agents with better tolerability profiles.

**Regarding ranks #1–6 and #9:** The predictions for hypertrichosis, Ambras syndrome, nephrogenic SIAD, malformation syndrome with periodontal component, Dandy-Walker syndrome, isolated hair shaft abnormality, and leprosy all carry TxGNN scores above 99.8% yet have zero clinical trials, zero relevant literature, and no pharmacological mechanistic link to ergometrine. These are consistent with knowledge graph sparsity artifacts — rare disease nodes with few connections in the KG can produce artificially inflated prediction scores. None should be pursued.

---

## Clinical Trial Evidence

No clinical trials investigating ergometrine for migraine disorder, or for any of the other 9 predicted indications, are currently registered on ClinicalTrials.gov or the WHO ICTRP.

---

## Literature Evidence

The following are the most relevant publications for migraine (rank #7) — the only prediction with genuine supporting evidence. Literature retrieved for ranks #1–6 and #9 is either absent (0 results) or non-contributory (20 periodontology papers with no link to ergometrine, consistent with an indexing artifact). Additional safety signals from ranks #8 and #10 are summarised in a separate table below.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [2759844](https://pubmed.ncbi.nlm.nih.gov/2759844/) | 1989 | Case Series / Open-label | Headache | 40 menstrual migraine patients treated with intermittent prophylactic ergonovine maleate over 6 months; demonstrated meaningful headache reduction — the most direct evidence for ergometrine itself in migraine |
| [23432443](https://pubmed.ncbi.nlm.nih.gov/23432443/) | 2013 | Retrospective Study | Headache | Oral methylergonovine maleate (N-methyl homolog) for refractory migraine and cluster headache prevention; supports ergometrine-class activity in treatment-resistant headache |
| [19895705](https://pubmed.ncbi.nlm.nih.gov/19895705/) | 2009 | Clinical Observational | Head & Face Medicine | Pilot open-label study of intravenous methylergonovine in female ED migraine patients; assessed emergency use, effectiveness, and tolerability |
| [9793694](https://pubmed.ncbi.nlm.nih.gov/9793694/) | 1998 | Review | Cephalalgia | Methysergide described as an "ergometrine derivative"; documents efficacy in migraine prophylaxis including high-frequency resistant cases via 5-HT₁ agonism and 5-HT₂ antagonism |
| [7216754](https://pubmed.ncbi.nlm.nih.gov/7216754/) | 1980 | Observational Study | Headache | Long-term results of interval therapy in migraine including ergot alkaloid regimens; longitudinal tolerability data |
| [5761912](https://pubmed.ncbi.nlm.nih.gov/5761912/) | 1969 | Historical Clinical Study | British Medical Journal | Ergot-class preparations in recurrent headache prophylaxis; historical evidence base for the class |
| [556819](https://pubmed.ncbi.nlm.nih.gov/556819/) | 1977 | Case Report / Review | Neurology | Carotidynia (vascular neck pain) treated with migraine prophylactics including ergot alkaloids; supports vascular headache mechanistic overlap |
| [23216317](https://pubmed.ncbi.nlm.nih.gov/23216317/) | 2013 | Safety Review | Headache | QT prolongation, torsade de pointes, and myocardial ischaemia from coronary vasospasm with headache medications including ergot alkaloids — critical safety signal for any migraine application |
| [6773347](https://pubmed.ncbi.nlm.nih.gov/6773347/) | 1980 | Case Report | AJR | Pleural thickening caused by Sansert (methysergide) and Ergotrate (ergometrine brand) in migraine treatment — adverse event report directly implicating ergometrine by name |
| [10971665](https://pubmed.ncbi.nlm.nih.gov/10971665/) | 2000 | Case Report | Headache | ⚠️ Reversible cerebral vasoconstriction syndrome (RCVS) in a chronic migraine-with-aura patient following postpartum ergometrine — primary safety signal against use in aura-migraine subtypes |

### ⚠️ Contraindication Signals from Predicted Indications #8 and #10

| PMID | Predicted Indication (TxGNN rank) | Safety Signal |
|------|----------------------------------|--------------|
| [22731893](https://pubmed.ncbi.nlm.nih.gov/22731893/) | Pulmonary hypertension (#10) | Obstetric anaesthesia clinical review explicitly lists ergometrine as contraindicated in pulmonary hypertension due to pulmonary vasoconstriction |
| [26050249](https://pubmed.ncbi.nlm.nih.gov/26050249/) | Pulmonary hypertension (#10) | Case report: methylergonovine triggered acute pulmonary hypertensive crisis in a parturient with left ventricular noncompaction |
| [41844474](https://pubmed.ncbi.nlm.nih.gov/41844474/) | Pulmonary hypertension (#10) | 2026 focused review of uterotonics in cardiac disease reinforces ergometrine/methylergonovine contraindication in pulmonary hypertension |
| [10971665](https://pubmed.ncbi.nlm.nih.gov/10971665/) | Migraine with brainstem aura (#8) | RCVS with diffuse intracranial arterial narrowing following ergometrine in migraine-with-aura patient; strong contraindication signal for basilar/brainstem-aura migraine subtype |

---

## Canada Market Information

Ergometrine has **no Health Canada Drug Identification Numbers (DINs)** and is not currently marketed in Canada. No product licence data is available for this analysis.

Ergometrine (ergonovine maleate) may be obtainable through Health Canada's Special Access Programme (SAP) for exceptional obstetric use, but no formal approval is on record. Any repurposing pathway would require a new drug submission or clinical trial application under Health Canada regulations.

---

## Safety Considerations

No Health Canada package insert is available for this analysis. Based on literature evidence gathered during evidence collection:

- **Cardiovascular risk**: Ergometrine is a potent vasoconstrictor. Literature documents coronary artery vasospasm (Prinzmetal-type angina, PMID 15293589), QT prolongation and torsade de pointes risk (PMID 23216317), and hypertensive crisis. These cardiovascular signals are particularly concerning for any proposed migraine indication given the overlapping cardiovascular comorbidities in migraine populations.
- **Pulmonary hypertension — absolute contraindication**: Multiple independent publications (PMID 22731893, 26050249, 41844474) explicitly identify pulmonary hypertension as a contraindication to ergometrine and methylergonovine. The TxGNN rank #10 prediction is a pharmacovigilance-relevant false positive.
- **Migraine with brainstem aura — contraindication**: PMID 10971665 documents RCVS with cerebral oedema and occipital haemorrhage following ergometrine in a chronic migraine-with-aura patient. Ergometrine's potent cerebrovascular constriction is likely to exacerbate brainstem-aura physiology. The TxGNN rank #8 prediction is contraindicated.
- **Fibrotic complications**: Prolonged use of ergot alkaloids including ergotrate has been associated with pleural and potentially retroperitoneal fibrosis (PMID 6773347) — a class-level concern for any chronic migraine prophylaxis application.
- **Obstetric context caution**: Literature notes that ergometrine should be avoided in pre-eclampsia (PMID 22731893) and in patients with significant cardiac disease; this population overlaps with some severe migraine patient profiles.

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
Ergometrine and its structural relatives (methylergonovine, methysergide) have documented historical use in migraine prophylaxis, providing mechanistic plausibility and limited indirect clinical evidence (L4). However, the cardiovascular safety profile — coronary vasospasm, QT prolongation, RCVS in aura-migraine patients, and absolute contraindication in pulmonary hypertension — significantly narrows any viable therapeutic window, and contemporary migraine therapeutics (triptans, gepants, CGRP monoclonal antibodies) have supplanted vasoconstrictor-class ergot derivatives for both efficacy and safety reasons. No prospective clinical trials exist.

**To proceed, the following is needed:**
- Detailed MOA data from DrugBank to precisely map ergometrine's receptor binding profile relative to ergotamine and DHE, and to identify any differentiated pharmacological advantage
- Full safety data from a Health Canada–recognized source (WHO product monograph, EMEA SmPC, or equivalent) to establish the known contraindication list and monitoring requirements
- Patient stratification criteria excluding cardiovascular disease, hypertension, pulmonary hypertension, and migraine-with-aura subtypes before any study design is considered
- Comparative positioning analysis versus current standard-of-care (second- and third-line CGRP pathway agents) to define a potential niche, if any, in treatment-resistant migraine without cardiovascular comorbidity
- Pharmacovigilance review of the full ergot alkaloid class for cumulative fibrotic and vasospastic risk signals
- Health Canada SAP or IND pathway assessment for clinical trial feasibility given the absence of any current Canadian product licence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

