---
layout: default
title: Ergometrine
parent: Model Prediction Only (L5)
nav_order: 343
evidence_level: L5
indication_count: 10
monitor_inn: "Ergometrine"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "nephrogenic syndrome of inappropriate antidiuresis", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "migraine disorder", "migraine with brainstem aura", "leprosy", "pulmonary hypertension"]
last_modified_at: 2026-10-23
description: "Ergometrine: predicted new indication hypertrichosis (disease) (evidence level L5). Approved use: Not stated in the licence record"
---

# Ergometrine
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

## Ergometrine: From Uterotonic Use to hypertrichosis (disease)
{: .text-alpha }

## One-Sentence Summary

Ergometrine (ergonovine) is an ergot alkaloid uterotonic. It is listed with one Canadian licence (ERGONOVINE MALEATE INJECTION USP), but the licence record contains no approved indication text.
The TxGNN model's top-ranked prediction is **hypertrichosis**, but **no clinical trials and no publications** support it, so this is a model-only (L5) signal.
Among the ten predictions, only migraine disorder has indirectly related literature, and none of it studies ergometrine as a treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence record |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, ergometrine is an ergot alkaloid that acts on alpha-adrenergic, serotonergic and dopaminergic receptors and is used as a uterotonic.

For hypertrichosis, **no plausible mechanistic link was identified**. Hair growth is not a recognised target of this receptor pharmacology, and the high score (rank 1205 overall) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No trial or publication supports it.

The other predictions do not fare better:

- **Ambras-type congenital hypertrichosis, nephrogenic syndrome of inappropriate antidiuresis, malformation syndromes (odontal/periodontal, Dandy-Walker), genetic hair shaft abnormality, leprosy:** no mechanistic rationale and no evidence.
- **Migraine disorder:** biologically plausible, because related ergots (ergotamine, dihydroergotamine, methysergide) are used in migraine through serotonergic and vasoconstrictive effects. However, the evidence concerns related compounds and one case report, not ergometrine itself, and that case report describes a vasoconstrictive safety risk.
- **Migraine with brainstem aura:** vasoconstrictive ergots carry ischaemic risk in this setting. Only a case report and a historical review were retrieved.
- **Pulmonary hypertension:** ergometrine is more likely to cause harm, because it can raise pulmonary vascular resistance. This is a safety signal, not an opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature is available for the top-ranked prediction (hypertrichosis). The literature below was retrieved for other predictions and is indirect.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9793694](https://pubmed.ncbi.nlm.nih.gov/9793694/) | 1998 | Review | Cephalalgia | Methysergide, an ergometrine derivative, is used for migraine prophylaxis (5-HT receptor activity); relates to a related drug, not ergometrine |
| [10971665](https://pubmed.ncbi.nlm.nih.gov/10971665/) | 2000 | Case report | Headache | Postpartum cerebral angiopathy in a woman with chronic migraine with aura; vasoconstrictive safety concern |
| [41844474](https://pubmed.ncbi.nlm.nih.gov/41844474/) | 2026 | Review | Int J Obstet Anesth | Focused review of uterotonic use in pregnant patients with cardiac disease, including pulmonary hypertension |
| [22731893](https://pubmed.ncbi.nlm.nih.gov/22731893/) | 2012 | Review | Anaesthesia | Management issues in pre-eclampsia for anaesthetists; obstetric context, not therapeutic benefit |
| [20509463](https://pubmed.ncbi.nlm.nih.gov/20509463/) | 2009 | Review (historical) | J R Coll Physicians Edinb | History of ergot of rye, 1900–1940 |
| [3214444](https://pubmed.ncbi.nlm.nih.gov/3214444/) | 1988 | Preclinical (animal) | Arzneimittel-Forschung | Cardiovascular effects of nilvadipine in animals; unrelated to ergometrine |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02441241 | ERGONOVINE MALEATE INJECTION USP | Not stated | Not stated |

---

## Safety Considerations

- **Contraindications recorded in the knowledge graph** (drug–disease relations, not label text): hypertensive disorder, hypertension, epilepsy, kidney disease, pyoureter, liver disease, gallbladder disease, stroke disorder, cerebrovascular disorder, susceptibility to ischaemic stroke (obsolete term), cerebral infarction, arteriosclerosis obliterans, HELLP syndrome.
- **Drug interactions:** 83 interactions were found in total. Major-level examples among those listed: isometheptene, epinephrine (including topical), ephedrine, lorcaserin, clarithromycin, cobicistat. Moderate-level examples: doxycycline, tetracycline, minocycline, aprepitant, dexamethasone, cimetidine, miconazole, clotrimazole.
- **Vasoconstrictive risk:** the retrieved literature flags cerebral angiopathy risk after postpartum ergot exposure and caution in cardiac disease and pulmonary hypertension.

Package insert warnings and contraindications were not available for this report; please refer to the Health Canada package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (hypertrichosis) rests only on a TxGNN model (deep learning) score, which may reflect similarities the model learned between related diseases, not biological evidence, with no trials, no literature and no plausible mechanism. The one biologically plausible direction, migraine, is supported only by evidence on related ergots and a case report that raises a safety concern, so no prediction reaches the evidence level needed to proceed. The migraine predictions are not backed by a study of ergometrine in that disease, so they are also treated as L5 under the evidence rules.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications, dosage form and approved indication text (currently a blocking gap)
- Mechanism-of-action data from DrugBank
- For migraine, if pursued: a targeted literature review of ergometrine itself and a vascular safety assessment
- No further work is suggested for the other predicted diseases without new supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

