---
layout: default
title: Mirvetuximab Soravtansine
parent: Model Prediction Only (L5)
nav_order: 617
evidence_level: L5
indication_count: 10
---

# Mirvetuximab Soravtansine
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

# Mirvetuximab Soravtansine: From Platinum-Resistant Ovarian Cancer to Antithrombin Deficiency Type 2

## One-Sentence Summary

Mirvetuximab soravtansine (ELAHERE) is a folate receptor alpha (FRα)-directed antibody-drug conjugate used for platinum-resistant ovarian cancer.
The TxGNN model predicts it may be effective for **antithrombin deficiency type 2**, but **0 clinical trials** and **0 publications** support this prediction, and no plausible mechanistic link exists. The high score is most likely a knowledge-graph artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Platinum-resistant ovarian cancer (from the published literature in the pack; the Canadian license text was not supplied) |
| Predicted New Indication | Antithrombin deficiency type 2 |
| TxGNN Prediction Score | 97.95% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

It is not well supported. Mirvetuximab soravtansine is an antibody-drug conjugate. The antibody binds FRα on tumour cells, and the conjugate delivers the DM4 microtubule-inhibitor payload, which kills the cell. Detailed mechanism data were not supplied in the input, so this description comes from the candidate's mechanistic assessment.

Antithrombin deficiency type 2 is an inherited defect in a coagulation inhibitor. The disease is caused by a dysfunctional protein, not by proliferating FRα-positive cells. A cytotoxic ADC cannot correct that defect. Cytotoxic cancer therapy is also generally associated with increased thrombotic risk, which would work against patients with this condition.

The TxGNN score is high (rank 30,079 overall), but it reflects graph-based association rather than biological rationale. Other top-ranked predictions for this drug (heparin cofactor 2 deficiency, factor V excess, candidiasis, tinea corporis, thrombophilia) show the same pattern. None has a plausible mechanism or any supporting study.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2560771 | ELAHERE |

Dosage form, manufacturer and approved indication text were not supplied for this license.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antibody-drug conjugate with a cytotoxic microtubule-inhibitor payload (DM4) |
| Myelosuppression Risk | Myelosuppression is a recognised concern for this class. Please refer to the package insert for grading. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Haematological parameters (CBC), ophthalmic examination, neurological assessment. Please refer to the package insert for the full schedule. |
| Handling Protection | Follow institutional cytotoxic drug handling regulations |

---

## Safety Considerations

The Evidence Pack has no package insert warnings, contraindications or drug interaction records for this product. The candidate assessment does flag the following concerns:

- **Ocular toxicity, peripheral neuropathy and myelosuppression** are the main toxicities of concern. Myelosuppression may also raise infection risk.
- **Thrombotic risk** is generally increased with cytotoxic cancer therapy, which is relevant to any coagulation-related indication.
- **Paediatric use** would be a serious concern given this toxicity profile.

Please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no trials or publications, the mechanism does not fit the disease, and the drug's toxicity and thrombotic-risk profile argue against use. All ten TxGNN predictions for this drug are currently Hold. The only one with any literature is plasma cell myeloma (L4). That literature consists of reviews of ADCs and immunotherapy, mostly in gynaecologic cancers, and does not test mirvetuximab in myeloma.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (currently a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Any preclinical or clinical evidence linking FRα-targeted delivery to antithrombin function. Without it, this candidate should not advance beyond model prediction.
- If the team wants a more tractable candidate from this list, a preclinical FRα expression check in plasma cells would be the minimum step for the myeloma prediction.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

