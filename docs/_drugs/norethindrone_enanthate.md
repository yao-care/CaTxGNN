---
layout: default
title: Norethindrone Enanthate
parent: Model Prediction Only (L5)
nav_order: 660
evidence_level: L5
indication_count: 10
---

# Norethindrone Enanthate
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

# Norethindrone enanthate: From Injectable Contraception to Antithrombin Deficiency Type 2

## One-Sentence Summary

Norethindrone enanthate is a long-acting injectable progestin. The publications in this pack describe it as a contraceptive, but the Canadian licence records provided do not state an approved indication.
The TxGNN model predicts it may be effective for **antithrombin deficiency type 2** with a high score, but there are **0 clinical trials** and **0 publications** for this prediction.
It is therefore a model-only (L5) prediction, and related literature points to thrombosis risk rather than benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records provided (literature describes use as an injectable contraceptive) |
| Predicted New Indication | Antithrombin deficiency type 2 |
| TxGNN Prediction Score | 98.93% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 18 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Norethindrone enanthate is a progestin, and the literature shows it has been used as an injectable contraceptive. No mechanistic link to antithrombin deficiency type 2 is supported by the data provided.

Antithrombin deficiency type 2 is an inherited thrombophilia, a condition that raises the risk of blood clots. Progestins are generally treated with caution in inherited thrombophilias. The high score (rank 17,392 overall) most likely reflects an association in the knowledge graph, not a therapeutic benefit. Other top predictions are thrombophilia-type disorders (heparin cofactor 2 deficiency, factor 5 excess with spontaneous thrombosis), which suggests the model may be picking up a shared thrombosis-related pattern. This should not be read as evidence of benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

The drug has 18 authorizations in Canada. The records provided do not include dosage form or approved indication text, so only the first 5 DINs and product names are listed.

| DIN | Product Name |
|---------|------|
| 2458683 | MAEVE |
| 2441306 | JENCYCLA |
| 23760 | NORLUTATE |
| 2410303 | MOVISSE |
| 2187108 | SYNPHASIC 21 TABLETS |

---

## Safety Considerations

No label warnings, contraindications or drug interaction data were available in the pack (the drug interaction query returned no results). Please refer to the package insert for safety information.

Literature retrieved for other predicted indications raises these safety signals:
- **Thrombosis:** A 2017 case report (PMID [29141931](https://pubmed.ncbi.nlm.nih.gov/29141931/)) describes cerebral venous sinus thrombosis in a young woman three weeks after a norethisterone enanthate injection. Thrombophilia screens were normal. This is a single case and does not establish causality, but it is directly relevant to any thrombophilia indication.
- **Lipid and cardiovascular effects:** Cohort studies (PMIDs [1533383](https://pubmed.ncbi.nlm.nih.gov/1533383/) and [1424623](https://pubmed.ncbi.nlm.nih.gov/1424623/)) examined lipid changes during use. The long-term study reported no significant difference in most lipid fractions versus non-users, but a significant reduction in mean HDL level.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no trials, no literature and no known mechanism. The available related evidence suggests a possible thrombosis risk in a prothrombotic condition, so the safety concern outweighs any suggested benefit.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank)
- Health Canada package insert warnings and contraindications, including thrombosis-related precautions
- Any pharmacological or clinical evidence linking progestins to antithrombin deficiency type 2
- A specific thrombosis risk assessment for patients with inherited thrombophilia
- Approved indication text and dosage forms for the Canadian licences

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

