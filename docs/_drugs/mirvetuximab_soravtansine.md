---
layout: default
title: Mirvetuximab Soravtansine
parent: 僅模型預測 (L5)
nav_order: 402
evidence_level: L5
indication_count: 10
---

# Mirvetuximab Soravtansine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Mirvetuximab Soravtansine: From Platinum-Resistant Ovarian Cancer to Antithrombin Deficiency Type 2

## One-Sentence Summary

Mirvetuximab Soravtansine (ELAHERE™) is an antibody-drug conjugate (ADC) targeting folate receptor alpha (FRα/FOLR1), approved in the US and EU for platinum-resistant ovarian cancer.
The TxGNN model predicts it may be effective for **Antithrombin Deficiency Type 2**, assigning a score of **97.95%** (top-ranked prediction).
However, **no clinical trials or supporting publications** exist for this indication, and mechanistic analysis indicates this is most likely a knowledge graph false positive.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Platinum-resistant ovarian cancer (FDA/EMA approved; not marketed in Canada) |
| Predicted New Indication | Antithrombin Deficiency Type 2 |
| TxGNN Prediction Score | 97.95% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the DrugBank record. Based on known published information, Mirvetuximab Soravtansine is an anti-FOLR1 antibody-drug conjugate in which the humanized anti-FRα antibody is linked to the maytansinoid cytotoxin DM4 (soravtansine). Its antitumour mechanism relies on selective binding to folate receptor alpha (FRα) overexpressed on epithelial tumour cell surfaces, receptor-mediated internalization, and intracellular release of DM4, which disrupts microtubule polymerization and triggers apoptosis. FRα is characteristically overexpressed in ovarian, endometrial, and certain lung cancers, but has no established functional role in haemostasis or coagulation biology.

Antithrombin Deficiency Type 2 is a hereditary thrombophilia caused by SERPINC1 gene mutations that impair antithrombin function, producing a hypercoagulable state. This condition is managed with anticoagulants (heparins, direct oral anticoagulants) or antithrombin concentrate — not cytotoxic agents. FRα is not expressed on coagulation proteins or the cell types implicated in this disease.

This prediction is assessed as a **model false positive**. The TxGNN knowledge graph score almost certainly reflects indirect graph connectivity between haematological system nodes, rather than a genuine mechanistic bridge between FOLR1-targeting ADC pharmacology and antithrombin deficiency. There is no published preclinical rationale, no registered clinical trial, and no supporting literature for this repurposing direction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Mirvetuximab Soravtansine is not approved or marketed in Canada (Health Canada DINs: 0). For reference, the drug holds FDA accelerated approval (November 2022) and full approval (March 2024) in the United States under the brand name ELAHERE™, for FRα-positive, platinum-resistant epithelial ovarian, fallopian tube, or primary peritoneal cancer in adults who have received 1–3 prior systemic treatment regimens.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted cytotoxic — Antibody-Drug Conjugate (anti-FOLR1 antibody × DM4 maytansinoid payload) |
| Myelosuppression Risk | Moderate — thrombocytopenia and neutropenia reported in ADC/maytansinoid class; CBC monitoring required |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (each cycle), liver function, renal function, visual acuity and ocular symptoms (DM4 class ocular toxicity risk), peripheral neuropathy |
| Handling Protection | Must follow cytotoxic drug handling regulations — biohazard and cytotoxic precautions apply to preparation, administration, and waste disposal |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score of 97.95% for antithrombin deficiency type 2 does not correspond to biological plausibility — FOLR1 and DM4 have no mechanistic relevance to the coagulation deficiency pathway, and this prediction is assessed as a knowledge graph artifact with zero clinical or preclinical supporting evidence.

**To proceed, the following is needed:**
- Obtain full MOA data from the DrugBank API (DB12489) to formally document the FOLR1/DM4 mechanism
- Obtain Health Canada or TFDA package insert to complete warnings and contraindications assessment
- Consider redirecting analysis to **plasma cell myeloma (rank 5, score 97.61%)**, which carries partial mechanistic rationale (FOLR1 low-level expression has been reported in some plasma cell lines) and has 4 indirect literature references — it represents the most defensible repurposing hypothesis among all 10 predictions
- Any further evaluation of Mirvetuximab in haematological indications should begin with FRα expression profiling in the target cell population before any clinical hypothesis is formed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

