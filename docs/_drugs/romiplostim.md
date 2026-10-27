---
layout: default
title: Romiplostim
parent: Model Prediction Only (L5)
nav_order: 822
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Romiplostim: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Idiopathic aplastic anemia, aplastic anemia…"
monitor_inn: "ROMIPLOSTIM"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "fetal and neonatal alloimmune thrombocytopenia", "Scott syndrome", "hemorrhagic disorder due to a constitutional thrombocytopenia", "bleeding diathesis due to a collagen receptor defect", "platelet-type bleeding disorder", "autosomal dominant macrothrombocytopenia", "Ehlers-Danlos syndrome, fibronectinemic type"]
---

# Romiplostim
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

## Romiplostim: From Aplastic Anemia and Autoimmune Thrombocytopenia to Primary Release Disorder of Platelets
{: .text-alpha }

## One-Sentence Summary

Romiplostim is a thrombopoietin receptor (MPL) agonist, originally used for autoimmune (immune) thrombocytopenia and listed in the knowledge graph for aplastic anemia.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but there are currently **0 clinical trials** and only **1 indirect publication** supporting this direction.
The mechanistic rationale is weak, because release disorders are defects of platelet function rather than platelet number.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Idiopathic aplastic anemia, aplastic anemia, autoimmune thrombocytopenic (from the knowledge graph; no approved indication text is available for the Canadian licences) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.99983% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. From general pharmacology, romiplostim is a peptide agonist of the thrombopoietin receptor (MPL). It stimulates megakaryocyte proliferation and platelet production, and it is used to raise platelet counts in chronic immune thrombocytopenia (ITP).

The prediction is hard to justify mechanistically. Primary release disorders are qualitative platelet defects in granule secretion, and platelet counts are usually normal. Raising platelet number is not expected to correct defective secretion. The only linked paper (PMID 25682608) studies autoantibody inhibition of proplatelet formation in ITP, not release disorders, so it gives only indirect context. The very high score most likely reflects network proximity to thrombocytopenia-related nodes in the knowledge graph rather than a true therapeutic link.

### Other predicted indications (for context)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|---|---|---|---|---|
| 2 | Pseudo-von Willebrand disease | 99.99977% | L5 | Platelet GPIb gain-of-function defect. TPO agonism may increase hyper-reactive platelets. No evidence. |
| 3 | Glanzmann thrombasthenia | 99.99954% | L5 | Qualitative defect with normal counts. Weak rationale. |
| 4 | Fetal and neonatal alloimmune thrombocytopenia | 99.98730% | L4 | Most plausible candidate. Immune-mediated platelet destruction resembles ITP, but only indirect evidence exists. |
| 5 | Scott syndrome | 99.96656% | L5 | Defect in phosphatidylserine exposure. TPO agonism does not address it. |
| 6 | Hemorrhagic disorder due to constitutional thrombocytopenia | 99.95290% | L5 | Plausible for some subtypes only. Subtype-specific evidence is needed. |
| 7 | Bleeding diathesis due to collagen receptor defect | 99.95080% | L5 | Receptor signalling defect. Not corrected by higher platelet counts. |
| 8 | Platelet-type bleeding disorder | 99.93190% | L5 | Broad, mostly qualitative category. Limited relevance. |
| 9 | Autosomal dominant macrothrombocytopenia | 99.88074% | L5 | Conceivable, but bleeding is usually mild and the defect is often downstream of TPO signalling. |
| 10 | Ehlers-Danlos syndrome, fibronectinemic type | 99.84516% | L5 | No clear link to the TPO/MPL pathway. |

Among these, fetal and neonatal alloimmune thrombocytopenia (FNAIT) has the most supporting literature, although it is still indirect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top-ranked indication (primary release disorder of platelets):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25682608](https://pubmed.ncbi.nlm.nih.gov/25682608/) | 2015 | Basic/mechanistic study | Haematologica | Antiplatelet autoantibodies from ITP patients inhibit proplatelet formation by megakaryocytes and impair platelet production in vitro. This concerns ITP, not release disorders. |

For the best-supported alternative (FNAIT), all of the following are indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31239245](https://pubmed.ncbi.nlm.nih.gov/31239245/) | 2019 | Review | Blood Advances | Romiplostim in paediatric ITP: drug development and current practice. FDA approval extended to children ≥1 year in December 2018. |
| [34711622](https://pubmed.ncbi.nlm.nih.gov/34711622/) | 2021 | Case report | BMJ Case Reports | Management of refractory ITP in pregnancy. |
| [23257464](https://pubmed.ncbi.nlm.nih.gov/23257464/) | 2012 | Review | Zhongguo Shi Yan Xue Ye Xue Za Zhi | Review of thrombopoietic drugs for childhood chronic and refractory ITP. |
| [27605856](https://pubmed.ncbi.nlm.nih.gov/27605856/) | 2016 | Case report | Asian J Transfus Sci | Refractory ITP in pregnancy managed with eltrombopag (a different TPO mimetic). |
| [20410910](https://pubmed.ncbi.nlm.nih.gov/20410910/) | 2010 | Review/Perspective | J Perinatol | Whether novel thrombopoietic agents could reduce platelet transfusions in neonates. |
| [23822831](https://pubmed.ncbi.nlm.nih.gov/23822831/) | 2013 | Case report | Eur J Haematol | Complete remission of refractory ITP after a short course of romiplostim. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02322854 | NPLATE | Not specified | Not specified |
| 02322862 | NPLATE | Not specified | Not specified |

## Safety Considerations

- **Drug Interactions**: A Major interaction with **carfilzomib** is recorded (DDInter). Romiplostim's pharmacology entry also confirms its target is the thrombopoietin receptor (MPL).
- **Theoretical concerns for predicted indications**: In pseudo-von Willebrand disease, raising the number of hyper-reactive platelets is a theoretical risk. Placental transfer and fetal/neonatal safety of romiplostim are unestablished for FNAIT.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction rests on a computational score alone. There are no trials, and the single linked paper concerns ITP rather than release disorders. Romiplostim raises platelet counts but would not be expected to correct a qualitative secretion defect.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data
- Approved indication text and dosage forms for the Canadian licences
- Direct evidence in the predicted indication. If the team wishes to pursue a lead, FNAIT or selected inherited thrombocytopenia subtypes are more plausible than release disorders. Those would need targeted literature review and fetal/neonatal safety data.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

