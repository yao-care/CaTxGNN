---
layout: default
title: Rivaroxaban
parent: Model Prediction Only (L5)
nav_order: 817
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-31
description: "Rivaroxaban: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "RIVAROXABAN"
predicted_indications: ["rheumatoid arthritis", "gout", "HIV infectious disease", "brachydactyly-syndactyly syndrome"]
---

# Rivaroxaban
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Rivaroxaban: From Thromboembolic Disease to Rheumatoid Arthritis
{: .text-alpha }

## One-Sentence Summary

Rivaroxaban is an oral Factor Xa inhibitor (anticoagulant) marketed in Canada. The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but this prediction currently has **no registered clinical trials** and **no publications that test rivaroxaban in rheumatoid arthritis**. Evidence rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the Canadian licence records contain no indication text) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 0.9957 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses on record: at least 20) |
| Number of DINs | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, rivaroxaban is a direct Factor Xa inhibitor, and its anticoagulant effect is well established. The Canadian licence records do not list the approved indications.

A possible link to rheumatoid arthritis is the crosstalk between coagulation and inflammation. Factor Xa and thrombin signal through PAR receptors, and thrombin generation is altered in autoimmune conditions (PMID 34175144). This is a hypothesis only. No evidence shows that Factor Xa inhibition changes rheumatoid arthritis disease activity or outcomes.

The other retrieved papers concern venous thromboembolism, adherence in atrial fibrillation, and a perioperative embolic case in a patient who happened to have rheumatoid arthritis. They do not test rivaroxaban as a treatment for the disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Review | La Revue de médecine interne | Thrombin generation assay can assess hypercoagulability in autoimmune diseases; it is a mechanistic context paper, not a treatment study |
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | Review of lower extremity venous thromboembolism diagnosis and treatment; not related to RA treatment |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohort | PLoS One | Adherence to rivaroxaban versus apixaban in non-valvular atrial fibrillation; not related to RA |
| [41918541](https://pubmed.ncbi.nlm.nih.gov/41918541/) | 2026 | Case report | Cureus | Recurrent embolic events in an 88-year-old woman with atrial fibrillation who was also taking steroids for RA; RA was a comorbidity, not the treatment target |

---

## Canada Market Information

Rivaroxaban has 20 valid single-ingredient authorizations in Canada. The records compiled for this report do not include dosage form or approved indication text. The first five are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02378612 | XARELTO | Not available | Not available |
| 02316986 | XARELTO | Not available | Not available |
| 02507196 | TEVA-RIVAROXABAN | Not available | Not available |
| 02482223 | SANDOZ RIVAROXABAN | Not available | Not available |
| 02527537 | PMS-RIVAROXABAN | Not available | Not available |

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph** (taken from drug-disease contraindication links in the TxGNN knowledge graph, not from label text): liver failure, kidney disease, pyoureter, liver disease, gallbladder disease, and blood coagulation disease.
- **Drug Interactions**: 100 interactions were identified. Examples rated **Major**: acetylsalicylic acid (aspirin), cobicistat, deferasirox, ibritumomab tiuxetan, and tositumomab (I-131). Examples rated **Moderate**: aprepitant, dexamethasone, cimetidine, clarithromycin, miconazole, and clotrimazole.
- Relevant to the predicted indication: patients with rheumatoid arthritis often take corticosteroids (for example dexamethasone) and NSAIDs or aspirin. These add to bleeding risk or interact with rivaroxaban, so co-prescribing needs careful review.

Please also refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (0.9957), but there are no clinical trials, no studies testing rivaroxaban in rheumatoid arthritis, and no confirmed mechanism. The evidence level is L5 (model prediction only). Bleeding risk and interactions with common arthritis medicines add further caution.

**To proceed, the following is needed:**
- Mechanism of action data and a testable biological hypothesis linking Factor Xa inhibition to RA pathogenesis
- Preclinical evidence (for example, animal arthritis models or synovial tissue studies)
- Approved indication text and package insert warnings from Health Canada
- A bleeding-risk and interaction assessment for RA patients using corticosteroids, NSAIDs or aspirin

---

### Other Predictions Reviewed (for context)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Gout | 0.9951 | L5 | No trials; the literature is about drug interactions and a case report, with no credible mechanism. Likely a network-proximity artifact. Hold. |
| 3 | HIV infectious disease | 0.9917 | L4 | One unrelated Phase 2 VTE cohort study; the literature concerns safe co-prescribing. Ritonavir- or cobicistat-boosted antiretrovirals raise rivaroxaban exposure and bleeding risk. This is an interaction issue, not a repurposing signal. Hold. |
| 4 | Brachydactyly-syndactyly syndrome | 0.9910 | L5 | No trials, no literature and no plausible mechanism. Hold. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

