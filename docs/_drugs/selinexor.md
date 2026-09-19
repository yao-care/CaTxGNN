---
layout: default
title: Selinexor
parent: Model Prediction Only (L5)
nav_order: 709
evidence_level: L5
indication_count: 1
---

# Selinexor
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Selinexor: From Multiple Myeloma to Drug-Induced Osteoporosis

## One-Sentence Summary

> Selinexor (DB11942) is a selective nuclear export inhibitor (XPO1/CRM1 inhibitor), currently approved internationally for multiple myeloma and diffuse large B-cell lymphoma, but has not yet obtained market approval in Canada.
> The TxGNN model predicts it may be effective for **Drug-Induced Osteoporosis**,
> but currently **there are no clinical trials and no literature** supporting this direction; evidence level is L5, and mechanistic analysis suggests this prediction is likely a false positive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple Myeloma / DLBCL (internationally approved indication, not Canada official drug approval data; Canada Not marketed) |
| Predicted New Indication | Drug-Induced Osteoporosis |
| TxGNN Prediction Score | 99.22% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The `original_moa` field currently lacks formal DrugBank mechanistic data (Data Gap, see DG002). Based on the mechanism-related association analysis in the evidence pack, selinexor is a selective nuclear export inhibitor (SINE) that targets XPO1/CRM1, exerting anti-tumor activity by inhibiting nuclear export of tumor suppressor proteins (p53, FOXO, etc.), and is currently approved for multiple myeloma and diffuse large B-cell lymphoma.

However, this mechanism has **no known direct association** with bone metabolism regulation (RANKL/OPG, Wnt signaling pathway, osteoclast activity inhibition, etc.), and there is no literature supporting that XPO1 inhibition has protective or therapeutic effects on drug-induced osteoporosis. Rather, selinexor clinically is frequently accompanied by systemic side effects such as weight loss, anorexia, and fatigue, which in theory might **aggravate** rather than ameliorate bone loss risk.

In comprehensive assessment, this indication is merely an association score from the TxGNN knowledge graph, lacks mechanistic evidence support, and is **likely a false positive prediction**. It is not recommended to invest further verification resources at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Canada Market Information

Selinexor has **not obtained market approval in Canada** (0 DINs), with no authorized product data available for listing.

---

## Cytotoxicity

Selinexor is an anti-tumor drug (XPO1/CRM1 targeting inhibitor), hence this section is provided.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (SINE, XPO1/CRM1 inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

(Note: The `safety.key_warnings`, `contraindications`, and DDI query results are all Data Gaps, wherein "product package insert warnings/contraindications" is marked as **Blocking** level gap; a preliminary safety assessment at S1 cannot be conducted before this is filled.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction has an evidence level of only L5 (no clinical trials, no literature support), and mechanistic analysis clearly indicates that XPO1 inhibition has no known association with bone metabolism protection and may even aggravate bone loss due to systemic side effects, suggesting a likely false positive. Additionally, the drug has not yet been marketed in Canada (Not marketed), with safety data (product package insert warnings, contraindications) as a Blocking level gap; it cannot proceed to the next stage of assessment.

**To proceed, the following is needed:**
- Complete formal DrugBank MOA data (DG002)
- Obtain official product insert/drug label warnings and contraindications data (DG001, Blocking)
- Identify preclinical or mechanistic studies on XPO1 inhibitors and bone metabolism to verify or exclude this association
- If no supporting evidence can be found, recommend marking this candidate indication as low priority and closing tracking

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

