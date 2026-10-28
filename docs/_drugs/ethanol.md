---
layout: default
title: Ethanol
parent: Moderate Evidence (L3-L4)
nav_order: 363
evidence_level: L4
indication_count: 2
last_modified_at: 2026-10-13
description: "Ethanol: predicted new indication Migraine disorder (evidence level L5). Approved use: Not available"
monitor_inn: "Ethanol"
predicted_indications: ["migraine disorder", "migraine with brainstem aura"]
---

# Ethanol
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **2** 
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

## Ethanol: From an Antiseptic Use (Original Indication Not Specified) to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Ethanol is marketed in Canada in two licensed single-ingredient products (AVAGARD CHG and DALMACOL), but the data compiled for this report do not list an approved indication for either.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are **0 clinical trials** and no publication showing that ethanol treats migraine. The available literature points the other way: alcohol is a known migraine trigger.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication text in the Canadian license records) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9929 |
| Evidence Level | L4 (preclinical and mechanistic studies only; they suggest a trigger role, not a therapeutic one) |
| Canada Market Status | Marketed (valid licenses: 2 of 2) |
| Number of DINs | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for ethanol, and no original indication could be extracted from the license records. The reasoning below relies only on the literature retrieved for the predicted indication.

The very high model score (0.9929) appears to reflect network proximity to migraine biology (CGRP, TRPA1, GABA signalling) rather than a therapeutic effect. A preclinical mouse study (PMID 37101198) found that ethanol is metabolised to acetaldehyde, which acts through the CGRP receptor and TRPA1 in Schwann cells to cause periorbital mechanical allodynia. This is a pro-pain pathway relevant to migraine, but it suggests ethanol would **worsen** migraine rather than relieve it. A review of alcohol and migraine (PMID 36373782) and work on ATP-sensitive potassium channels in meningeal nociceptors (PMID 40785517) are consistent with this trigger role.

Genetic association studies (ADH2 genotype, GABA receptor and NOS3 polymorphisms) link alcohol metabolism and GABA/nitric oxide signalling to migraine risk. They are associational and do not support therapeutic use.

The second-ranked prediction, **migraine with brainstem aura** (score 0.9914), appears to be inherited from the general migraine node. No retrieved paper addresses ethanol as a treatment for it, and several hits are false matches (palmitoylethanolamide, menthol and carisbamate are different compounds).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the publications below tests ethanol as a migraine treatment. Many retrieved papers are unrelated or involve other compounds and are omitted.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36373782](https://pubmed.ncbi.nlm.nih.gov/36373782/) | 2022 | Review | Headache | Reviews the complex relationship between alcohol and migraine; consistent with alcohol acting as a trigger |
| [37101198](https://pubmed.ncbi.nlm.nih.gov/37101198/) | 2023 | Preclinical (mouse) | J Biomed Sci | Ethanol-derived acetaldehyde acts via CGRP receptor and TRPA1 to cause allodynia, relevant to migraine triggering |
| [40785517](https://pubmed.ncbi.nlm.nih.gov/40785517/) | 2025 | Preclinical (mechanistic) | Cephalalgia | Opening of KATP channels activates meningeal nociceptors, with implications for migraine origin |
| [19486361](https://pubmed.ncbi.nlm.nih.gov/19486361/) | 2010 | Genetic association | Headache | Examines ADH2 genotype (ethanol metabolism) and migraine risk; alcohol is traditionally considered a trigger |
| [35063053](https://pubmed.ncbi.nlm.nih.gov/35063053/) | 2022 | Retrospective cohort | Aerosp Med Hum Perform | Migraine history and outcomes in military pilots; no ethanol treatment data |
| [29299688](https://pubmed.ncbi.nlm.nih.gov/29299688/) | 2018 | Genetic association | J Neural Transm | GABA receptor gene polymorphisms and migraine risk |
| [28699326](https://pubmed.ncbi.nlm.nih.gov/28699326/) | 2017 | Genetic association | Headache | GABA receptor rho gene polymorphisms and migraine risk |
| [42153521](https://pubmed.ncbi.nlm.nih.gov/42153521/) | 2026 | Scoping review | Drug Alcohol Rev | CGRP signalling in alcohol use disorders; links a migraine target to alcohol biology |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02246888 | AVAGARD CHG | Not specified | Not specified |
| 02230769 | DALMACOL | Not specified | Not specified |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were found. Of the 20 reviewed, most are Moderate and a few Minor. One is **Major**: eluxadoline. Moderate interactions include antidiabetic drugs (acarbose, albiglutide, acetohexamide, alogliptin, canagliflozin, chlorpropamide, dapagliflozin, dulaglutide, empagliflozin), anticholinergics (atropine, clidinium, dicyclomine), aspirin, bupropion and dronabinol. Minor interactions include doxycycline and cimetidine.
- **Pro-migraine signal**: the retrieved literature indicates alcohol can trigger migraine attacks, a safety concern for this proposed use.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The high TxGNN score is not supported by any clinical or therapeutic evidence. The literature indicates ethanol is a migraine trigger, so the prediction likely reflects network proximity rather than benefit. The brainstem aura prediction has even weaker support (Evidence Level L5).

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication and dosage form details for the two Canadian licenses
- Mechanism of action data
- Any human evidence that ethanol relieves migraine rather than provoking it; without it, the prediction should be treated as a likely false positive
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

