---
layout: default
title: Filgrastim
parent: Model Prediction Only (L5)
nav_order: 386
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
monitor_inn: "FILGRASTIM"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "Scott syndrome", "hemorrhagic disorder due to a constitutional thrombocytopenia", "bleeding diathesis due to a collagen receptor defect", "C1 inhibitor deficiency", "serpinopathy with toxic serpin polymerization", "fetal and neonatal alloimmune thrombocytopenia", "platelet-type bleeding disorder"]
description: "Filgrastim: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Not recorded in the local data"
---

# Filgrastim
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

## Filgrastim: Primary release disorder of platelets
{: .text-alpha }

## One-Sentence Summary

Filgrastim (a recombinant G-CSF) was originally used to treat chronic neutropenic conditions such as constitutional neutropenia, severe congenital neutropenia, cyclic hematopoiesis and chronic familial neutropenia.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but this is a computational prediction only, with **0 clinical trials** and **0 publications** supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 13 of 13) |
| Number of DINs | 13 (valid: 13) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, filgrastim is a G-CSF that acts on the G-CSF receptor to stimulate the production, maturation and release of neutrophils.

Primary release disorder of platelets is a qualitative platelet function defect, in which platelets fail to release their granule contents properly. G-CSF acts on the neutrophil lineage and would not be expected to correct this defect, so no direct mechanistic link is established. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other top-ranked predictions have the same problem. They include pseudo-von Willebrand disease, Glanzmann thrombasthenia, Scott syndrome, constitutional thrombocytopenia, collagen receptor defects, C1 inhibitor deficiency, serpinopathy and fetal/neonatal alloimmune thrombocytopenia. Each has a different underlying cause (platelet receptor defects, complement dysregulation, protein misfolding or maternal alloantibodies) that G-CSF does not address.

The only prediction with any related studies is **platelet-type bleeding disorder** (rank 10). The link is indirect: filgrastim is used for stem cell mobilization and engraftment support in allogeneic transplantation, which can be curative for severe inherited platelet disorders. The linked trials, however, enrolled patients with hematologic malignancies and did not test filgrastim as a treatment for the bleeding disorder itself.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for primary release disorder of platelets.

For reference, the seven trials linked to the rank-10 prediction (platelet-type bleeding disorder) are all transplant-related. All were graded as low relevance (C), because they mostly address hematologic malignancies and transplant conditioning.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00296023](https://clinicaltrials.gov/study/NCT00296023) | NA | Completed | 25 | Low-dose allogeneic PBSC transplantation for high-risk low-grade hematologic malignancies |
| [NCT00004232](https://clinicaltrials.gov/study/NCT00004232) | Phase 1 | Completed | Not reported | CD34-enriched PBSC augmentation in allogeneic transplantation for hematologic malignancies |
| [NCT00054236](https://clinicaltrials.gov/study/NCT00054236) | Phase 1 | Completed | 55 | Multiple cord blood unit transplantation after non-myeloablative conditioning |
| [NCT00301912](https://clinicaltrials.gov/study/NCT00301912) | Phase 2 | Withdrawn | 0 | Busulfan/fludarabine preparative regimen; no participants enrolled |
| [NCT00295997](https://clinicaltrials.gov/study/NCT00295997) | NA | Unknown | 35 | Non-myeloablative matched unrelated donor transplantation |
| [NCT00080925](https://clinicaltrials.gov/study/NCT00080925) | Phase 1 | Completed | 20 | T-cell depleted reduced-intensity haploidentical transplantation |
| [NCT00004904](https://clinicaltrials.gov/study/NCT00004904) | Phase 1 | Completed | Not reported | T-cell depleted partially matched related donor transplantation |

---

## Canada Market Information

Thirteen valid single-ingredient authorizations are listed. Dosage form and approved indication text were not available.

| DIN | Product Name |
|---------|------|
| 02441489 | GRASTOFIL |
| 01968017 | NEUPOGEN |
| 02521008 | NYPOZI |
| 02485591 | NIVESTYM |
| 02485656 | NIVESTYM |

Other authorizations cover the same brands (NEUPOGEN, NYPOZI, NIVESTYM, GRASTOFIL) as well as FILRA.

---

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 records. The 20 reviewed are all rated **Moderate**. They include radiopharmaceuticals and radioimmunotherapies (iobenguane I-131, fludeoxyglucose F-18, ibritumomab tiuxetan, tositumomab) and cytotoxic or antineoplastic agents (paclitaxel, mercaptopurine, azacitidine, bendamustine, arsenic trioxide, trimetrexate, altretamine). Other agents on the list are abemaciclib, acalabrutinib, aldesleukin, alemtuzumab, asparaginase, avapritinib, belantamab mafodotin and levamisole.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high model score. There are no trials or publications for primary release disorder of platelets, and no biological rationale links G-CSF to a platelet granule release defect. Even the best-supported neighbouring prediction (platelet-type bleeding disorder) has only indirect, transplant-related trial evidence.

**To proceed, the following is needed:**
- Mechanism of action data for filgrastim, to support any mechanistic-link analysis
- Canadian package insert warnings and contraindications, which are required before safety screening
- Evidence of a plausible biological pathway (preclinical or case-level) connecting G-CSF to platelet function
- A review of whether any value lies in transplant or stem cell mobilization settings, rather than direct treatment of the platelet disorder
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

