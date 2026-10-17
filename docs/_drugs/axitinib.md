---
layout: default
title: Axitinib
parent: Model Prediction Only (L5)
nav_order: 88
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Axitinib: predicted new indication Unclassified renal cell carcinoma (evidence level L5). Approved use: Renal cell carcinoma (including clear cell and non-papillary subtypes)"
monitor_inn: "Axitinib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "angiolipoma", "familial spontaneous pneumothorax"]
---

# Axitinib
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

# Axitinib: From Renal Cell Carcinoma to Unclassified Renal Cell Carcinoma

## One-Sentence Summary

Axitinib is an oral kinase inhibitor originally used to treat renal cell carcinoma (RCC).
The TxGNN model predicts it may be effective for **unclassified renal cell carcinoma**, a histologic subgroup of RCC.
This prediction currently rests on the model alone, with **0 clinical trials** and **0 publications** supporting this specific subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal cell carcinoma (including clear cell and non-papillary subtypes) |
| Predicted New Indication | Unclassified renal cell carcinoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Axitinib is known as a tyrosine kinase inhibitor that targets VEGFR-1, -2 and -3, which blocks the formation of new blood vessels that tumours depend on. Its efficacy in RCC is well established.

Unclassified RCC is a histologic subgroup of RCC that likely shares the same angiogenic signalling. That makes a response to VEGFR inhibition plausible. This is a mechanistic inference only, and no studies specific to this subtype were found.

The prediction is also very close to the drug's existing indication, so it may be a refinement of the same disease family rather than a truly new use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Status |
|---------|------|------|
| 02389649 | INLYTA | Valid (single-ingredient) |
| 02389630 | INLYTA | Valid (single-ingredient) |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (VEGFR tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Blood pressure, signs of bleeding or thromboembolism, and liver function. Please also refer to the package insert. |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 records. Of the 20 shown in the data compiled for this report:
  - **Major**: clarithromycin, dexamethasone
  - **Moderate**: aprepitant, clotrimazole, miconazole, naltrexone
  - **Minor**: mostly acid-reducing agents and antacids, such as famotidine, ranitidine, cimetidine, nizatidine, rabeprazole, esomeprazole, lansoprazole, dexlansoprazole, aluminum hydroxide, calcium carbonate and magnesium salts
- The pattern of interactions suggests that CYP3A-related interactions need attention.

Warnings and contraindications from the Canadian package insert were not available. Please refer to the package insert for these.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for unclassified RCC is the model prediction (L5), with no trials or publications for this subtype. Axitinib's benefit in broader RCC is established, but that does not by itself establish benefit in this subgroup.

**To proceed, the following is needed:**
- Subtype-specific clinical or observational data, such as a case series or a retrospective analysis of unclassified RCC patients treated with axitinib
- Clarification of how "unclassified RCC" overlaps with the already approved RCC indication, since this may be covered by the current label
- Canadian package insert warnings and contraindications
- Detailed mechanism of action data
- A safety and drug-interaction management plan, particularly for CYP3A-related interactions

Related RCC subtypes in the same data have more evidence and may be better candidates to pursue first:
- **Translocation (TFE3) RCC**: a randomized Phase 2 trial of axitinib plus nivolumab (15 patients, results not yet available)
- **Collecting duct carcinoma**: a Phase 2 trial of checkpoint inhibitors plus axitinib (30 patients, recruiting)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

