---
layout: default
title: Ceftazidime
parent: Model Prediction Only (L5)
nav_order: 167
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ceftazidime: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Bacterial infections (e.g. streptococcal infection…"
monitor_inn: "CEFTAZIDIME"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "urinary tract infection (disease)", "epiglottitis", "Ureaplasma urethritis", "gonococcal urethritis", "blood group incompatibility", "infectious otitis media", "Peptostreptococcus infectious disease"]
---

# Ceftazidime
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

## Ceftazidime: From Bacterial Infections to Hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Ceftazidime is a third-generation cephalosporin antibiotic, used to treat bacterial infections such as pneumonia, meningitis and peritonitis.
The TxGNN model predicts it may be effective for **hyperamylasemia**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction.
It is a graph-based computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (e.g. streptococcal infection, bacterial pneumonia, peritonitis, bacterial meningitis). Product-level indication text is not available in the Canadian licence records, so this comes from the knowledge-graph indication list. |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, ceftazidime belongs to the cephalosporin class of antibiotics, which kill bacteria by blocking cell wall synthesis. Its efficacy in bacterial infections is well established.

Hyperamylasemia means elevated amylase in the blood. It is a laboratory finding rather than an infection. No plausible antibacterial mechanism links ceftazidime to this condition. The high score (99.51%) reflects patterns in the knowledge graph and is not supported by any trial or publication, so the prediction should be treated as a computational artefact until proven otherwise.

For context, other predictions for this drug have more support. The best-supported one is **urinary tract infection** (TxGNN score 99.41%, Evidence Level L2). It is backed by a completed Phase 2 randomized trial (NCT00921024) and several ceftazidime-avibactam studies. It is largely an on-label or near-label use rather than true repurposing. It is not the lead prediction evaluated here, and a separate evaluation would be appropriate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Dosage form and approved-indication text are not available in the licence records compiled for this report.

| DIN | Product Name |
|---------|------|
| 02437848 | Ceftazidime for Injection BP |
| 00886955 | Ceftazidime for Injection, USP |
| 02437856 | Ceftazidime for Injection BP |
| 02437864 | Ceftazidime for Injection BP |
| 00886971 | Ceftazidime for Injection, USP |

Six single-ingredient licences are valid in total (0 cancelled); the table shows the first five.

## Safety Considerations

- **Contraindications / disease cautions (from the knowledge graph, not label text)**: kidney disease, pyoureter, liver disease, gallbladder disease, blood coagulation disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, congenital prothrombin deficiency.
- **Drug Interactions**: 100 interactions were recorded. The ones rated Moderate are:
  - amphotericin B (including cholesteryl sulfate, lipid complex and liposomal forms)
  - the aminoglycosides kanamycin, neomycin and streptomycin
  - picosulfuric acid

  Several others (e.g. vancomycin, omeprazole, metformin, morphine) have an unclassified severity.

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical, trial or literature support (Evidence Level L5). No biologically plausible mechanism links an antibiotic to an elevated amylase level.

**To proceed, the following is needed:**
- A plausible mechanistic hypothesis, which is currently missing (and detailed MOA data)
- Any clinical or observational evidence, which would need to be generated or identified
- Review of the official package insert warnings and contraindications
- Consideration of the better-supported urinary tract infection prediction as a separate, higher-priority candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

