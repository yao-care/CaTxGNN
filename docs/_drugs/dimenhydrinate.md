---
layout: default
title: Dimenhydrinate
parent: Moderate Evidence (L3-L4)
nav_order: 284
evidence_level: L4
indication_count: 2
---

# Dimenhydrinate
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **2** 
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

# Dimenhydrinate: From Nausea/Motion Sickness to Allergic Urticaria

## One-Sentence Summary

Dimenhydrinate is marketed in Canada in products such as Gravol, Travel Tabs and Gaviscon Nausea, which points to nausea and travel-related use. The licence indication text is not recorded in the Evidence Pack.
The TxGNN model predicts it may be effective for **allergic urticaria**, but there are currently **0 clinical trials** and only **1 publication** (a veterinary pharmacokinetic pilot study), so this remains a model-driven hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the licence data. Nausea/motion sickness is inferred from product names only |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for dimenhydrinate is not available in the DrugBank fields of this pack. Based on known pharmacology, dimenhydrinate is the 8-chlorotheophylline salt of diphenhydramine, a first-generation H1 receptor antagonist.

Histamine acting on H1 receptors in the skin's blood vessels and sensory nerves causes the wheals and itching of histamine-mediated urticaria. Blocking these receptors is the recognised way to relieve them. The link between the drug and the predicted indication is therefore biologically plausible.

There is one important caveat. No efficacy data exist for dimenhydrinate itself in urticaria. The 0.997 score is a model prediction, not clinical evidence. A second predicted condition, cold urticaria (score 99.24%), rests on the same H1-antagonist logic. It has no trials or literature at all (Evidence Level L5).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30779257](https://pubmed.ncbi.nlm.nih.gov/30779257/) | 2019 | Pharmacokinetic pilot study (healthy dogs) | Veterinary Dermatology | Compared diphenhydramine exposure after oral and IV diphenhydramine and after oral dimenhydrinate. Used histamine-induced wheal formation as the pharmacodynamic readout. The abstract excerpt available does not report results. |

This is animal data on drug exposure, not human evidence of efficacy in urticaria.

---

## Canada Market Information

Dosage form and approved-indication text are not recorded for these licences. Five of the 20 authorizations are listed.

| DIN | Product Name |
|---------|------|
| 00783595 | KIDS GRAVOL SUPPOSITORIES |
| 00392553 | CONFAB DIMENHYDRINATE 50 MG |
| 00605786 | TRAVEL TABS 50 MG |
| 02490528 | GAVISCON NAUSEA |
| 00013803 | GRAVOL TABLETS |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible because of H1 antagonism. However, it is supported only by model output and one veterinary pharmacokinetic study, with no registered human trials. Health Canada safety labelling has also not been obtained, so the candidate cannot move past early screening. Since diphenhydramine is already an established H1 antagonist, the more useful question is whether dimenhydrinate adds anything for urticaria.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap)
- Licence indication text and dosage forms for the Canadian products
- Detailed mechanism-of-action data from DrugBank
- Human clinical or observational evidence of dimenhydrinate or diphenhydramine in allergic urticaria, and a comparison against existing antihistamine treatment
- Route compatibility assessment

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

