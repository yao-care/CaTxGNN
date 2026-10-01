---
layout: default
title: Pertuzumab
parent: Model Prediction Only (L5)
nav_order: 718
evidence_level: L5
indication_count: 10
---

# Pertuzumab
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

# Pertuzumab: From HER2-Positive Breast Cancer to Normal Breast-Like Subtype of Breast Carcinoma

## One-Sentence Summary

Pertuzumab is a HER2-targeted antibody marketed in Canada for HER2-positive breast cancer.
The TxGNN model predicts it may be effective for the **normal breast-like subtype of breast carcinoma**,
but **no clinical trials and no publications** currently support this specific prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (the approved indication text was not supplied in the licence records) |
| Predicted New Indication | Normal breast-like subtype of breast carcinoma |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Based on known information, pertuzumab blocks HER2 dimerization. Its efficacy in HER2-positive breast cancer is established, usually together with trastuzumab and a taxane.

The link to the predicted indication is weak. The normal-like intrinsic subtype is generally not HER2-driven, so there is little mechanistic reason to expect benefit. The very high TxGNN score is probably inherited from neighbouring breast cancer nodes in the knowledge graph rather than from subtype-specific biology. Treat this as a model artifact until evidence shows otherwise.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Dosage form and approved indication text were not supplied for these authorizations.

| DIN | Product Name |
|---------|------|
| 2405016 | PERJETA |
| 2512920 | PHESGO |
| 2512912 | PHESGO |
| 2405024 | PERJETA-HERCEPTIN |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HER2-directed monoclonal antibody) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature and a weak mechanistic link. HER2 blockade is not expected to drive benefit in the normal-like subtype.

Other candidates in the same breast cancer family have more evidence, but they are mostly subtypes of the already-marketed HER2-positive indication rather than new uses:
- **Progesterone-receptor negative breast cancer** (Proceed with Guardrails, L1): it has pertuzumab biosimilar equivalence trials and de-escalation studies in HER2-positive, ER/PR-negative disease. Benefit depends on confirmed HER2 positivity, not on PR status.
- **Breast tumor luminal A or B** (Research Question, L3): the ADEPT trial (NCT04569747, Phase 2, recruiting, no results) tests pertuzumab and trastuzumab with endocrine therapy in HR+/HER2+ disease.

**To proceed, the following is needed:**
- HER2-status-stratified evidence for the normal-like subtype, via re-queried trials and literature
- Mechanism of action data (e.g., from DrugBank)
- Health Canada package insert warnings and contraindications, which block safety screening
- Approved indication text and dosage forms for the four Canadian authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

