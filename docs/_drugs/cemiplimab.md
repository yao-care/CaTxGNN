---
layout: default
title: Cemiplimab
parent: Model Prediction Only (L5)
nav_order: 173
evidence_level: L5
indication_count: 5
monitor_inn: "Cemiplimab"
predicted_indications: ["gallbladder adenosquamous carcinoma", "rectal cloacogenic carcinoma", "adenosquamous prostate carcinoma", "urethral verrucous carcinoma", "pancreatic adenosquamous carcinoma"]
last_modified_at: 2026-11-24
description: "Cemiplimab: predicted new indication gallbladder adenosquamous carcinoma (evidence level L5). In Canada: 1 DIN (1 marketed)"
---

# Cemiplimab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Cemiplimab: anti-PD-1 antibody → gallbladder adenosquamous carcinoma
{: .text-alpha }

## One-Sentence Summary

Cemiplimab is an anti-PD-1 (programmed cell death 1) antibody that is marketed in Canada under the brand name LIBTAYO.
The TxGNN model predicts it may be effective for **gallbladder adenosquamous carcinoma**, with a score of 0.9999.
Currently there are **0 clinical trials** and **0 publications** that directly study this disease, so the support is model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | gallbladder adenosquamous carcinoma |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 1 of 1) |
| Number of DINs | 1 (marketed: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Cemiplimab is a monoclonal antibody that binds human PD-1 (gene PDCD1) and blocks its interaction with PD-L1, with an IC50 below 1 nM in an ELISA. By releasing this checkpoint, it can restore T-cell activity against tumours. According to the Mechanism of Action section of the US FDA-approved prescribing information for cemiplimab: "Binding of the PD-1 ligands PD-L1 and PD-L2 to the PD-1 receptor found on T cells inhibits T-cell proliferation and cytokine production. Upregulation of PD-1 ligands occurs in some tumors and signaling through this pathway can contribute to inhibition of active T-cell immune surveillance of tumors. […] Cemiplimab-rwlc is a recombinant human immunoglobulin G4 (IgG4) monoclonal antibody that binds to PD-1 and blocks its interaction with PD-L1 and PD-L2, releasing PD-1 pathway-mediated inhibition of the immune response, including the anti-tumor immune response." ([DailyMed: Libtayo (cemiplimab-rwlc) prescribing information, Regeneron Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4347ae1f-d397-4f18-8b70-03897e1c054a), label version 2026-08-31; accessed 2026-11-19.) The pharmacology data confirm the PD-1 target.

The link to the predicted disease is mainly histological. Cemiplimab is established in cutaneous squamous cell carcinoma, and the predicted tumour has a squamous component, so PD-1 blockade could plausibly act on it. This reasoning is speculative. Adenosquamous biliary tumours are rare and have distinct biology, and no trial or publication in the data compiled for this report addresses this disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02487144 | LIBTAYO | CEMIPLIMAB | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-1 checkpoint inhibitor) |
| Myelosuppression Risk | Low; not a conventional cytotoxic agent. Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Low |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: Ten interaction records were compiled. Nine are Moderate-level interactions with corticosteroids: hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone, methylprednisolone and deflazacort. The tenth is the pharmacological target record for PD-1 (CD279), which is not a drug interaction. Corticosteroids may blunt the immune activity that PD-1 blockade relies on, so their use should be reviewed case by case.

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (0.9999), but no clinical trial or publication directly studies cemiplimab in gallbladder adenosquamous carcinoma. This disease is rare, and its biology differs from the cutaneous squamous cell carcinoma where cemiplimab works. The evidence level is therefore L5.

**To proceed, the following is needed:**
- Clinical or real-world data on PD-1 blockade in adenosquamous biliary tumours (case series, registry data, PD-L1 and mutational-burden profiling)
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Detailed mechanism-of-action data from DrugBank
- A defined rationale for corticosteroid co-medication management

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action text is not available in the DrugBank data compiled for this report, but t" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Libtayo (cemiplimab-rwlc) prescribing information, Regeneron Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4347ae1f-d397-4f18-8b70-03897e1c054a) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

