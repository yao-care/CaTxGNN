---
layout: default
title: Leucovorin
parent: 僅模型預測 (L5)
nav_order: 458
evidence_level: L5
indication_count: 2
---

# Leucovorin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Leucovorin: From Folate Rescue Therapy to Primary Hyperoxaluria

## One-Sentence Summary

Leucovorin (folinic acid, DB00650) is classically used as a folate-replacement / chemotherapy rescue agent (e.g., methotrexate toxicity, 5-FU potentiation), though this evidence pack has no confirmed original-indication or Canadian licensing record on file. The TxGNN model predicts possible activity in **Primary Hyperoxaluria** (and, as a secondary candidate, **Congenital Intrinsic Factor Deficiency**), but **no clinical trials and no literature** currently support either direction — this is a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in this dataset (no approved indication text available; leucovorin is generally used as folate replacement / chemotherapy rescue) |
| Predicted New Indication | Primary Hyperoxaluria |
| TxGNN Prediction Score | 99.41% (rank 10,491) |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for leucovorin in this dataset. Based on general pharmacology, leucovorin (folinic acid / 5-formyl-THF) supplies reduced folate for one-carbon metabolism (methylation, purine/pyrimidine synthesis) and is used clinically as a rescue agent against dihydrofolate reductase inhibitors such as methotrexate.

Primary Hyperoxaluria (PH1/2/3) is a genetic disorder of glyoxylate/glycine metabolism (AGXT, GRHPR, or HOGA1 defects) causing oxalate overproduction. The established cofactor therapy for the PH1 subtype is **pyridoxine (vitamin B6)**, not the folate pathway. The TxGNN score most likely reflects graph-level proximity between one-carbon metabolism nodes and the glycine–serine–glyoxylate pathway rather than a demonstrated pharmacological effect — there is currently no evidence that leucovorin reduces oxalate production or stone burden.

A secondary candidate, **Congenital Intrinsic Factor Deficiency** (score 99.34%, rank 11,488), shows a similarly speculative link: this condition impairs ileal absorption of vitamin B12 and is treated with parenteral B12, not folate. Folate and B12 share a role in DNA synthesis and megaloblastic anemia pathways, but supplementing folate in B12 deficiency is a known clinical *risk* (it can mask the hematologic picture while neurologic damage progresses) rather than a therapeutic rationale. Both predictions appear to be graph-proximity artifacts rather than mechanistically grounded repurposing candidates.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

No Canadian marketing authorization (DIN) is on file for leucovorin in this dataset (market status: Not Marketed; total licenses: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Secondary Predicted Indication (for reference)

| Item | Content |
|------|------|
| Disease | Congenital Intrinsic Factor Deficiency |
| TxGNN Score | 99.34% (rank 11,488) |
| Evidence | No clinical trials, no literature |
| Rationale | Graph-proximity via folate/B12 megaloblastic-anemia pathway; no direct pharmacological support, and folate supplementation is a known confounder/risk in B12 deficiency |
| Recommendation | Hold |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predictions are Evidence Level L5 (model prediction only) — no clinical trials, no literature, and the mechanistic rationale explicitly documented in this evidence pack describes the link as speculative graph proximity rather than a pharmacologically supported connection. There is also a blocking data gap on TFDA/Health Canada label warnings, which prevents any safety assessment.

**To proceed, the following is needed:**
- Confirmed original indication and mechanism of action (MOA) for leucovorin (currently missing)
- Health Canada product monograph warnings/contraindications (blocking gap, DG001)
- Preclinical or mechanistic studies directly linking folate metabolism to oxalate reduction (for Primary Hyperoxaluria) or to intrinsic factor/B12 absorption pathways (for Congenital Intrinsic Factor Deficiency)
- Confirmation of current Canadian licensing/DIN status, since this dataset shows the drug as not marketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

