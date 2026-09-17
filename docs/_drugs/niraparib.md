---
layout: default
title: Niraparib
parent: Model Prediction Only (L5)
nav_order: 551
evidence_level: L5
indication_count: 10
---

# Niraparib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Niraparib: From Ovarian Cancer Maintenance Therapy to Epiglottis Neoplasm

## One-Sentence Summary

Niraparib is a PARP1/2 inhibitor whose approved use — per trial and literature context found in this evidence pack — is maintenance treatment of recurrent epithelial ovarian, fallopian tube, or primary peritoneal cancer. The TxGNN model predicts it may also be effective for **Epiglottis Neoplasm**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only signal with no corroborating clinical or mechanistic evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in Canadian regulatory data (drug not marketed); trial/literature context indicates approval for maintenance treatment of recurrent epithelial ovarian, fallopian tube, or primary peritoneal cancer |
| Predicted New Indication | Epiglottis Neoplasm |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Niraparib is not available in this evidence pack (flagged as a High-severity data gap). Based on information found within the evidence pack itself — including trial and literature descriptions collected under other predicted indications — Niraparib is a PARP1/2 inhibitor that exploits synthetic lethality in tumors with homologous recombination deficiency (HRD), such as BRCA1/2-mutated disease, and is used as maintenance therapy in ovarian cancer.

Epiglottis neoplasm is a head-and-neck squamous tissue tumor with a biological profile that is generally not characterized by the HRD/BRCA-driven genomic instability that underlies PARP inhibitor efficacy. No clinical trials or publications in this evidence pack link Niraparib to epiglottis, laryngeal, or other head-and-neck neoplasms.

This ranking reflects the TxGNN model's statistical prediction score alone. Without mechanistic or clinical corroboration, the biological rationale for applying a PARP-inhibitor mechanism to this indication is currently weak.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Canada Market Information

Niraparib is not currently marketed in Canada (0 DINs registered; no active licenses on file).

## Cytotoxicity

Niraparib is an antineoplastic agent (PARP inhibitor class, referenced throughout this evidence pack in the context of ovarian and other cancers), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PARP inhibitor) |
| Myelosuppression Risk | Not specified in this evidence pack — PARP inhibitors as a class are commonly associated with haematologic toxicity; please refer to the package insert |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential; renal and hepatic function (standard for PARP inhibitor therapy) |
| Handling Protection | Cytotoxic drug handling precautions apply per institutional protocol |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (Epiglottis Neoplasm) has zero clinical trials and zero publications in support, and the TxGNN score is the only available evidence (L5 — model prediction only). The known PARP-inhibitor mechanism has no established biological link to this tumor type, so the risk/benefit case cannot currently be assessed.

**To proceed, the following is needed:**
- Confirmed mechanism of action data from DrugBank (currently a data gap)
- TFDA/Health Canada product label — warnings, contraindications, DDI (currently a Blocking-severity data gap)
- Any preclinical or case-level evidence connecting PARP inhibition to head-and-neck/epiglottis tumor biology
- Continued literature/trial surveillance, as no current evidence exists to re-evaluate against

**Note:** Within this same evidence pack, a different candidate indication — *cystic neoplasm* (rank 2, score 99.99%, Evidence Level L2, recommendation "Proceed with Guardrails") — is backed by 3 clinical trials and 9 publications, largely reflecting real-world use of Niraparib in serous ovarian/endometrial carcinoma. That candidate represents a materially stronger repurposing signal and may warrant its own evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

