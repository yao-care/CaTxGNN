---
layout: default
title: Alfacalcidol
parent: 僅模型預測 (L5)
nav_order: 31
evidence_level: L5
indication_count: 5
---

# Alfacalcidol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Alfacalcidol: From Vitamin D-Related Bone Disease to Familial Isolated Hypoparathyroidism Due to Impaired PTH Secretion

## One-Sentence Summary

Alfacalcidol (1α-hydroxyvitamin D3) is a synthetic active vitamin D analog classically used in the management of calcium-phosphate metabolism disorders, including renal osteodystrophy and hypoparathyroidism.
The TxGNN model predicts it may be effective for **familial isolated hypoparathyroidism due to impaired PTH secretion**, with **0 registered clinical trials** and **0 publications** specifically addressing this rare genetic subtype — support currently rests entirely on model prediction and a near-perfect mechanistic rationale.
The exceptionally high prediction score (99.61%) is consistent with alfacalcidol's unique pharmacological property of bypassing the PTH-dependent renal hydroxylation step that is precisely deficient in this condition.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Vitamin D-related calcium/bone metabolism disorders (no Canada DIN data available in dataset) |
| Predicted New Indication | Familial isolated hypoparathyroidism due to impaired PTH secretion |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Alfacalcidol is a synthetic prodrug form of active vitamin D. Unlike native vitamin D3, which requires two sequential hydroxylation steps — first in the liver (25-hydroxylation) and then in the kidney (1α-hydroxylation, tightly regulated by PTH) — alfacalcidol has already undergone 1α-hydroxylation. After a single hepatic conversion step, it becomes fully active calcitriol (1,25-dihydroxyvitamin D3) and directly activates the vitamin D receptor (VDR). This makes alfacalcidol functionally independent of PTH signaling for its activation.

Familial isolated hypoparathyroidism due to impaired PTH secretion is a rare genetic condition in which the parathyroid glands fail to produce sufficient PTH. Since PTH is the principal inducer of renal 1α-hydroxylase (CYP27B1), its deficiency leads to a critical block in calcitriol biosynthesis — resulting in hypocalcemia, hyperphosphatemia, and downstream sequelae affecting bone, neuromuscular function, and renal handling of minerals. This is precisely the enzymatic bottleneck that alfacalcidol bypasses by design.

The mechanistic fit is therefore near-perfect: the drug's pre-hydroxylated structure directly compensates for the exact enzymatic deficiency caused by PTH absence. The TxGNN model score of 99.61% most likely reflects the model's capture of this tightly shared calcium homeostasis node between the drug's mechanism and the disease's pathophysiology. Clinically, alfacalcidol and calcitriol are already the standard of care for hypoparathyroidism broadly in many jurisdictions; this prediction extends the rationale to a specific molecularly-defined genetic subtype, further strengthening the biological plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this specific indication.

---

## Literature Evidence

Currently no related literature available for this specific indication.

---

## Canada Market Information

Alfacalcidol is currently **not marketed in Canada** according to this dataset — no Drug Identification Numbers (DINs) are on record.

> **Note:** Alfacalcidol preparations (e.g., One-Alpha®) are marketed in multiple international jurisdictions. Canadian regulatory status should be independently verified via Health Canada's Drug Product Database (DPD) and the Drugs@FDA or Health Canada online portal, as dataset coverage may be incomplete.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale for alfacalcidol in familial isolated hypoparathyroidism due to impaired PTH secretion is among the strongest possible for a repurposing candidate — the drug directly compensates for the precise biochemical defect caused by PTH deficiency — yet the evidence base for this specific rare genetic subtype is currently at L5 (model prediction only), with no clinical trial or literature support identified. The "Hold" decision reflects the absence of direct evidence, not a mechanistic concern.

**To proceed, the following is needed:**

- Retrieve full safety data: package insert warnings, contraindications, and drug–drug interactions for alfacalcidol (currently all data gaps)
- Independently verify Canadian regulatory status via Health Canada's Drug Product Database; update DIN count and approved indication text
- Retrieve MOA documentation from DrugBank (DB01436) to formally document the 1α-hydroxylation bypass mechanism
- Conduct targeted PubMed/EMBASE search for alfacalcidol or calcitriol specifically in familial isolated hypoparathyroidism and PTH-secretion defects to identify any bridging case reports or observational data
- Leverage existing evidence for alfacalcidol in broader hypoparathyroidism (e.g., post-surgical, autoimmune) as indirect supporting evidence for this subtype
- Consult endocrinology/rare disease clinical experts to assess whether this genetic subtype would be eligible for an orphan drug designation pathway
- If bridging evidence is identified, escalate to "Proceed with Guardrails" with a focused case series protocol
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

