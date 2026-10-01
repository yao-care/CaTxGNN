---
layout: default
title: Tapentadol
parent: Model Prediction Only (L5)
nav_order: 875
evidence_level: L5
indication_count: 3
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Tapentadol: From Pain (Opioid Analgesic) to Migraine Disorder

## One-Sentence Summary

Tapentadol is a centrally acting opioid analgesic, marketed in Canada as Nucynta. The licence records supplied here do not list an approved indication. The TxGNN model predicts it may be effective for **migraine disorder**, but there are **0 clinical trials** and only **2 loosely related publications** (neither studies tapentadol), so this is a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied licence data (tapentadol is generally known as an analgesic) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the supplied data. Tapentadol is generally described as a mu-opioid receptor agonist and norepinephrine reuptake inhibitor. Its efficacy in pain is established, but no direct mechanistic link to migraine pathophysiology (CGRP, 5-HT1B/1D, trigeminovascular activation) is supported by the supplied data.

The relationship between pain and migraine is the main basis for the prediction, since migraine is a pain condition. Opioids are generally discouraged for migraine because of limited efficacy, medication-overuse headache, and dependence risk. The high TxGNN score reflects graph-based proximity only and is not clinical evidence.

The other two predictions are weaker:
- **Migraine with brainstem aura** (99.57%): a rare subtype with no trials or literature. The prediction appears to come from proximity to the broader migraine node.
- **Migraine with or without aura, susceptibility to** (99.08%): a genetic susceptibility phenotype, not a treatable condition. The retrieved literature is about epilepsy genetics, and none of it mentions tapentadol.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27096438](https://pubmed.ncbi.nlm.nih.gov/27096438/) | 2016 | Review | Cochrane Database Syst Rev | Sumatriptan plus naproxen for acute migraine attacks in adults. This is background on migraine treatment, not tapentadol. |
| [27096578](https://pubmed.ncbi.nlm.nih.gov/27096578/) | 2016 | Review | Cochrane Database Syst Rev | Single-dose dipyrone (metamizole) for acute postoperative pain. Migraine is only mentioned as one use of dipyrone, and tapentadol is not studied. |

Neither publication evaluates tapentadol in migraine, so they do not support the prediction.

---

## Canada Market Information

Eight licences are recorded; the five below are the ones listed in the data. Dosage form, manufacturer, and approved indication text were not provided for any of them.

| DIN | Product Name |
|---------|------|
| 2415577 | NUCYNTA EXTENDED-RELEASE |
| 2378272 | NUCYNTA IR |
| 2415593 | NUCYNTA EXTENDED-RELEASE |
| 2415585 | NUCYNTA EXTENDED-RELEASE |
| 2415607 | NUCYNTA EXTENDED-RELEASE |

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug-interaction records were found for this drug in the supplied data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no clinical trials and no tapentadol-specific literature. There is also no supported mechanistic link, and opioids are generally discouraged for migraine because of limited efficacy, medication-overuse headache, and dependence risk.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data, for example from the DrugBank API, to assess any link to migraine
- Original approved indication text for the Canadian licences
- Targeted searches for tapentadol-specific migraine studies, since none were found
- A risk-benefit assessment covering medication-overuse headache and dependence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

