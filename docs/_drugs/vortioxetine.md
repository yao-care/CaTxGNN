---
layout: default
title: Vortioxetine
parent: Model Prediction Only (L5)
nav_order: 983
evidence_level: L5
indication_count: 5
---

# Vortioxetine
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

# Vortioxetine: From Major Depressive Disorder to Neurotic Disorder

## One-Sentence Summary

Vortioxetine is a multimodal serotonergic antidepressant originally used for depressive and anxiety disorders.
The TxGNN model predicts it may be effective for **neurotic disorder**, but **no clinical trials** and only **1 publication** (a single case report) are currently linked to this prediction.
Because "neurotic disorder" is a legacy, broad diagnostic label that overlaps with vortioxetine's existing indications, this is better seen as a labelling overlap than a true new therapeutic opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Unipolar depression, endogenous depression, major depressive disorder, anxiety disorder |
| Predicted New Indication | Neurotic disorder |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Published reviews describe vortioxetine as a serotonin transporter (SERT) inhibitor that also acts on several serotonin receptors: 5-HT1A agonist, 5-HT1B partial agonist, and 5-HT3, 5-HT7 and 5-HT1D antagonist. This multimodal profile is plausibly relevant to both the depressive and anxiety components of neurotic conditions.

"Neurotic disorder" is an older, broad category that overlaps heavily with depression and anxiety disorders, which are vortioxetine's established indications. The high TxGNN score most likely reflects this overlap rather than a distinct new use. No specific mechanism has been established for this label.

The other top-ranked predictions are also depression-related (neurotic depression, melancholia, dysthymic disorder). They are mostly on-label or near-label rather than genuine repurposing. Benign paroxysmal torticollis of infancy (score 99.07%) has no plausible mechanistic link, no trials and no literature, and appears to be a model artifact.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for neurotic disorder.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31006795](https://pubmed.ncbi.nlm.nih.gov/31006795/) | 2019 | Case report / Review | Zhurnal nevrologii i psikhiatrii imeni S.S. Korsakova | Describes a patient with neurotic depression and favours an integrated approach combining antidepressants with cognitive behavioural therapy. It does not study vortioxetine specifically. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02432927 | TRINTELLIX | Not listed | Not listed |
| 02432943 | TRINTELLIX | Not listed | Not listed |
| 02432919 | TRINTELLIX | Not listed | Not listed |
| 02552744 | APO-VORTIOXETINE | Not listed | Not listed |
| 02552779 | APO-VORTIOXETINE | Not listed | Not listed |

One further authorization (DIN 02552752, APO-VORTIOXETINE) is also valid. All 6 licences are single-ingredient products and none are cancelled.

---

## Safety Considerations

**Drug Interactions**: The interaction screening recorded 100 potential interactions. The main ones, from the 20 reviewed entries, are:
- **Major**: bupropion, lorcaserin, diethylpropion, dolasetron, palonosetron, phentermine
- **Moderate**: morphine, acetylsalicylic acid, dexamethasone, chlorpropamide, glimepiride, several insulins (aspart, degludec, detemir, glargine, glulisine), eliglustat, and bowel-preparation agents (picosulfuric acid, sodium sulfate, polyethylene glycol with electrolytes)

**Other considerations from the literature:**
- CYP2D6 and related pharmacogenetic dosing guidance exists (CPIC guideline).
- Reported adverse effects include hyperhidrosis, gastrointestinal effects and sexual dysfunction.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone, with no trials and only one non-vortioxetine case report. "Neurotic disorder" is a legacy umbrella term that overlaps with vortioxetine's existing depression and anxiety indications, so there is little distinct repurposing value to pursue.

**To proceed, the following is needed:**
- Clarify how "neurotic disorder" maps onto current diagnoses (for example, anxiety or depressive disorders), and evaluate those on-label uses instead
- Mechanism of action data from DrugBank
- Health Canada package insert warnings and contraindications, which are required before any safety screening
- Vortioxetine-specific clinical or observational evidence for the mapped condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

