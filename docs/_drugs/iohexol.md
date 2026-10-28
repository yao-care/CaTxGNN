---
layout: default
title: Iohexol
parent: Model Prediction Only (L5)
nav_order: 490
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
monitor_inn: "Iohexol"
predicted_indications: ["insomnia (disease)", "anxiety"]
description: "Iohexol: predicted new indication Insomnia (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Iohexol
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

## Iohexol: Insomnia (disease)
{: .text-alpha }

## One-Sentence Summary

Iohexol is a non-ionic iodinated radiographic contrast agent, used to visualise structures during imaging procedures.
The TxGNN model predicts it may be effective for **insomnia**, with a very high score but **no clinical trials** and **no publications** supporting this direction.
The prediction appears to be a TxGNN model (deep learning) artifact rather than a biologically plausible signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 0.9987 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 3 of 3) |
| Number of DINs | 3 (valid: 3) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, iohexol is an inert, non-ionic iodinated contrast agent that is cleared by the kidneys. Its role is diagnostic: it makes structures visible on X-ray and CT imaging.

Iohexol has no known pharmacological activity on sleep or central nervous system pathways. No mechanistic link to insomnia was identified, so the high TxGNN score is unlikely to reflect a real therapeutic signal.

The same applies to the other top-ranked predictions. Sleep disorder (initiating and maintaining sleep) is essentially a duplicate of the insomnia concept. Anxiety, rheumatoid arthritis, and tendinitis appear in the literature only because iohexol is used as a contrast or measurement tool, or is mentioned as an adverse-event context.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for insomnia.

---

## Literature Evidence

Currently no related literature available for insomnia.

For context, literature retrieved for other lower-ranked predictions concerns iohexol only as a diagnostic or procedural agent, not as a treatment:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8883531](https://pubmed.ncbi.nlm.nih.gov/8883531/) | 1996 | RCT | Academic Radiology | Iodixanol vs iohexol in extremity phlebography; compares contrast tolerability, not anxiety treatment (anxiety prediction) |
| [2352635](https://pubmed.ncbi.nlm.nih.gov/2352635/) | 1990 | Cohort | Neuroradiology | Side effects after lumbar iohexol myelography; anxiety appears as an adverse symptom (anxiety prediction) |
| [25889308](https://pubmed.ncbi.nlm.nih.gov/25889308/) | 2015 | RCT | Arthritis Res Ther | Tofacitinib effect on measured GFR in rheumatoid arthritis, with iohexol used as the GFR marker (rheumatoid arthritis prediction) |
| [35286798](https://pubmed.ncbi.nlm.nih.gov/35286798/) | 2022 | Case report | Korean J Anesthesiol | Fatal multiorgan dysfunction after repeated iodinated contrast in a patient on low-dose methotrexate (safety signal) |
| [36628042](https://pubmed.ncbi.nlm.nih.gov/36628042/) | 2022 | Case report | Cureus | Successful desensitisation to iohexol in a patient with rheumatoid arthritis-related amyloidosis (rheumatoid arthritis prediction) |
| [8000836](https://pubmed.ncbi.nlm.nih.gov/8000836/) | 1994 | Comparative imaging study | Br J Radiol | Iohexol vs iotrolan in CT arthrography of the shoulder (tendinitis prediction) |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02172739 | OMNIPAQUE 240 | Not specified | Not specified |
| 02172747 | OMNIPAQUE 300 | Not specified | Not specified |
| 02172755 | OMNIPAQUE 350 | Not specified | Not specified |

---

## Safety Considerations

**Drug Interactions:** The interaction screen returned 100 interacting drugs, many rated Major. Examples include:
- Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone
- Metformin
- Amphotericin B (including lipid complex)
- Aminoglycosides and other antibiotics: kanamycin, neomycin, vancomycin, levofloxacin
- Bupropion, metoclopramide, morphine
- Mesalazine and balsalazide
- Appetite suppressants and related agents: phentermine, diethylpropion, dronabinol
- Mannitol (Moderate)

The retrieved literature also includes a case report of fatal multiorgan dysfunction after repeated iodinated contrast injection in a patient taking low-dose oral methotrexate.

Warnings and contraindications from the package insert were not available. Please refer to the package insert for these.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The insomnia prediction has no clinical trials or literature, and iohexol has no known pharmacology related to sleep or the central nervous system. The high TxGNN score is best explained as a TxGNN model (deep learning) artifact. The same conclusion holds for the other top-ranked predictions reviewed.

**To proceed, the following is needed:**
- A plausible mechanistic hypothesis linking iohexol to sleep regulation, which is currently absent
- Mechanism of action data from DrugBank
- Health Canada package insert warnings and contraindications, along with approved indication text and dosage forms for the three DINs
- Any preclinical or clinical evidence for insomnia; without it, the prediction should not advance beyond model-level screening
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

