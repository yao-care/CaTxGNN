---
layout: default
title: Tapentadol
parent: Model Prediction Only (L5)
nav_order: 882
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Tapentadol: predicted new indication Migraine disorder (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "TAPENTADOL"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "migraine with or without aura, susceptibility to"]
---

# Tapentadol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Tapentadol: From Pain Management to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Tapentadol is an opioid analgesic marketed in Canada under the NUCYNTA brand, with immediate-release and extended-release products.
The TxGNN model predicts it may be effective for **migraine disorder**, but this is a graph-based prediction only, with **0 clinical trials** and **0 directly relevant publications** supporting it.
The two publications retrieved for a related migraine node argue against, rather than for, opioid use in migraine.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the Canadian licence records contain no indication text) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on general knowledge, tapentadol is a mu-opioid receptor agonist and a norepinephrine reuptake inhibitor. A plausible link to migraine is modulation of central pain pathways through opioid and noradrenergic signalling.

This rationale is speculative. The high TxGNN score comes from the knowledge graph, not from clinical observation. Opioids are generally not recommended for migraine because of the risks of medication-overuse headache, chronification of headache, and dependence.

Two related predictions were also generated: **migraine with brainstem aura** (score 99.57%) and **migraine with or without aura, susceptibility to** (score 99.08%). These most likely reflect similarity to the general migraine node in the graph rather than subtype-specific biology. The "susceptibility" node describes genetic risk, not a treatable clinical condition.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature was retrieved for the top prediction (migraine disorder). Two publications were retrieved for the related node "migraine with or without aura, susceptibility to". Neither provides direct evidence of tapentadol efficacy in migraine.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33689517](https://pubmed.ncbi.nlm.nih.gov/33689517/) | 2021 | Review | Expert Opin Pharmacother | Reviews NSAIDs and acetaminophen as alternatives to opioids for acute pain, in the context of the opioid overdose crisis. It argues against opioid use. |
| [29760569](https://pubmed.ncbi.nlm.nih.gov/29760569/) | 2018 | Cross-sectional utilization study | Drug Healthc Patient Saf | Notes that opioids are not recommended for routine migraine treatment because of medication-overuse headache and dependence risks. Examines co-prescription of opioids with triptans or serotonergic antidepressants, which carries a serotonin syndrome warning. It concerns safety and prescribing patterns, not efficacy. |

---

## Canada Market Information

Eight valid single-ingredient licences are on record. Dosage form, manufacturer and approved indication text are not available in the compiled data.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02378272 | NUCYNTA IR | Not available | Not available |
| 02378280 | NUCYNTA IR | Not available | Not available |
| 02378299 | NUCYNTA IR | Not available | Not available |
| 02415577 | NUCYNTA EXTENDED-RELEASE | Not available | Not available |
| 02415585 | NUCYNTA EXTENDED-RELEASE | Not available | Not available |

Three other NUCYNTA EXTENDED-RELEASE licences (02415593, 02415607, 02415615) are also valid.

---

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 interacting drugs. Examples of **Major** interactions include:
  - Bupropion
  - Morphine
  - Lorcaserin
  - Diethylpropion
  - Dolasetron
  - Palonosetron
  - Phentermine

  Examples of **Moderate** interactions include:
  - Epinephrine
  - Hyoscyamine
  - Atropine
  - Glycopyrronium
  - Dicyclomine
  - Naloxone
  - Dronabinol
  - Eluxadoline
  - Nabilone
  - Trospium
- **Serotonergic co-medication**: The retrieved literature notes a US FDA safety communication (March 2016) on the risk of serotonin syndrome when opioids are combined with triptans or serotonergic antidepressants (SSRIs, SNRIs). This matters because triptans are standard migraine therapy.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a graph-based score alone (Evidence Level L5). There are no clinical trials, and the available literature points away from opioid use in migraine because of medication-overuse headache, dependence and serotonergic interaction risks.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Approved indication text for the Canadian licences, to confirm the original indication
- Mechanism of action data (e.g. from DrugBank) to support a mechanistic-link analysis
- Any clinical or preclinical studies of tapentadol in migraine, and a benefit-risk assessment against guideline-recommended non-opioid therapies
- Evaluation of the serotonin syndrome risk with triptans and other serotonergic drugs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

