---
layout: default
title: Telotristat Ethyl
parent: Model Prediction Only (L5)
nav_order: 886
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Telotristat Ethyl: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Diarrheal disease"
monitor_inn: "Telotristat ethyl"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)"]
---

# Telotristat Ethyl
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Telotristat ethyl: From Diarrheal Disease to Cauda Equina Syndrome
{: .text-alpha }

## One-Sentence Summary

Telotristat ethyl was originally used to treat diarrheal disease. The TxGNN model predicts it may be effective for **cauda equina syndrome**, but **no clinical trials and no publications** currently support this direction. The prediction is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diarrheal disease (the Canadian licence has no indication text on file) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 0.9938 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, telotristat ethyl inhibits tryptophan hydroxylase (TPH), the enzyme that makes serotonin, and so lowers serotonin produced outside the brain. This is the likely basis for its effect on diarrhoea caused by excess serotonin.

Cauda equina syndrome is a compressive neurological condition, in which the bundle of nerve roots at the base of the spinal cord is squeezed. No established link exists between lowering peripheral serotonin and this condition. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other top predictions are equally weakly supported (all L5, all Hold). The second-ranked term, "obsolete neurogenic bladder", is flagged as obsolete, which points to a mapping problem and lowers confidence further.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02481553 | XERMELO | Not listed | Not listed |

---

## Cytotoxicity

Telotristat ethyl is not an antineoplastic drug. It is a serotonin synthesis inhibitor, so this section does not apply.

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the interaction database. The 20 shown in the data are all rated Moderate. They include:
  - Corticosteroids: hydrocortisone, prednisone, dexamethasone, betamethasone, triamcinolone
  - Antiemetics: aprepitant, rolapitant, ondansetron, granisetron
  - Antibiotics: clarithromycin
  - Antidiabetics: saxagliptin, linagliptin, repaglinide
  - Others: bupropion, simvastatin, cisapride, eliglustat, naldemedine, naloxegol, nitisinone

Warnings and contraindications from the Canadian product label were not available. Please refer to the package insert for these.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no trials, no publications and no mechanistic link to cauda equina syndrome. The label safety data needed for screening is also missing.

**To proceed, the following is needed:**
- The Health Canada package insert (warnings and contraindications), which blocks safety screening
- Confirmed mechanism of action data from DrugBank
- A literature and trial search that shows a plausible biological link to cauda equina syndrome
- Review of whether other predictions with better-grounded mechanisms (for example, those involving autonomic regulation) merit evaluation instead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

