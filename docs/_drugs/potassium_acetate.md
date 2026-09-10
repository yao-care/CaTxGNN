---
layout: default
title: Potassium Acetate
parent: 僅模型預測 (L5)
nav_order: 636
evidence_level: L5
indication_count: 1
---

# Potassium Acetate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Potassium Acetate: Toward Renal Tubular Acidosis (Original Indication Not on File)

## One-Sentence Summary

Potassium acetate (DrugBank DB14498) has no approved-indication text on file in this evidence pack, and its mechanism of action is also not yet documented, so its established therapeutic role cannot be confirmed from available data. The TxGNN model predicts a possible link to **Renal Tubular Acidosis (RTA)**, with a very high similarity score, but this is currently supported only by **9 case-report/mechanistic-level publications** and **zero clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established — drug is not currently marketed in Canada and no approved indication text is on file |
| Predicted New Indication | Renal Tubular Acidosis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for potassium acetate in this evidence pack (flagged as a High-severity data gap). Based on general pharmacology, potassium acetate is metabolized to bicarbonate in the body, so it could theoretically serve as an alkalinizing agent to replenish bicarbonate stores while also supplying potassium — a rationale that would fit **hypokalemic distal RTA (Type 1)**.

However, a review of the 9 supporting publications shows most describe the opposite clinical picture: **hyperkalemic RTA (Type 4)**, driven by hyporeninemic hypoaldosteronism, Gordon syndrome, or tubular potassium-handling defects (PMIDs 6758113, 3398981, 4015282, 2973296, 637641). In these patients, potassium handling is already impaired and administering a potassium-containing salt could mechanistically worsen hyperkalemia rather than treat the acidosis. Only one case report (PMID 37224266, a veterinary case) describes the hypokalemic subtype where the proposed mechanism would actually apply.

This suggests the TxGNN high score likely reflects a strong knowledge-graph association between "potassium metabolism" and "renal tubular acidosis" broadly, rather than validated causal evidence that potassium acetate treats RTA safely. The RTA subtype must be distinguished before this prediction can be considered clinically actionable.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33771116](https://pubmed.ncbi.nlm.nih.gov/33771116/) | 2021 | RCT | BMC Nephrology | Comparing 0.9% saline vs Plasma-Lyte in hip replacement; saline linked to hyperchloremic acidosis risk — indirect chloride/acid-base relevance, not a direct potassium acetate–RTA trial |
| [6758113](https://pubmed.ncbi.nlm.nih.gov/6758113/) | 1982 | Review | Schweizerische medizinische Wochenschrift | Review of hyporeninemic hypoaldosteronism causing hyperkalemic acidosis (Type 4 RTA) — subtype where potassium supplementation is mechanistically inappropriate |
| [3398981](https://pubmed.ncbi.nlm.nih.gov/3398981/) | 1988 | Mechanistic/Cohort | Nephron | Hyperkalemia identified as primary driver of acidosis in hyporeninemic hypoaldosteronism; corrected with fludrocortisone, not potassium repletion |
| [37224266](https://pubmed.ncbi.nlm.nih.gov/37224266/) | 2023 | Case Report | Veterinary Medicine and Science | Transient hypokalemic, hyperchloremic distal RTA post-anaesthesia (dog) — the subtype consistent with the proposed alkalinizing/potassium-repletion mechanism |
| [34442051](https://pubmed.ncbi.nlm.nih.gov/34442051/) | 2021 | Case Report | Journal of Clinical Medicine | Patiromer (potassium-binding resin, not potassium acetate) induced hypercalcemia/hypokalemia/metabolic alkalosis in CKD |
| [4015282](https://pubmed.ncbi.nlm.nih.gov/4015282/) | 1985 | Case Report | Archives of Internal Medicine | Hyperkalemic distal RTA with selective aldosterone deficiency in lead nephropathy; fludrocortisone failed to correct acidosis |
| [2973296](https://pubmed.ncbi.nlm.nih.gov/2973296/) | 1988 | Case Report | Archives des Maladies du Coeur et des Vaisseaux | Hypertension with hyperkalemia and tubular acidosis (Gordon syndrome / pseudohypoaldosteronism type II) |
| [637641](https://pubmed.ncbi.nlm.nih.gov/637641/) | 1978 | Case Report | Archives of Internal Medicine | Familial hyperkalemia, hypertension, hyporeninemia with normal aldosterone — a tubular potassium-handling defect |
| [239022](https://pubmed.ncbi.nlm.nih.gov/239022/) | 1975 | Animal/Basic Research | The Journal of Clinical Investigation | Rat study of renal citrate/ammonia metabolism under KCl deficiency — basic mechanistic renal physiology |

---

## Canada Market Information

Potassium acetate is not currently marketed in Canada under this evidence pack (0 DIN records on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L4 — no clinical trials and only case-report/mechanistic-level literature support this indication. More importantly, most of the supporting literature describes the hyperkalemic RTA subtype, where potassium supplementation is mechanistically counter-indicated, creating a real risk that this prediction reflects a spurious knowledge-graph association rather than a viable repurposing signal.

**To proceed, the following is needed:**
- Confirm the drug's original approved indication and mechanism of action (both currently missing)
- Regulatory product monograph / label warnings and contraindications, particularly regarding hyperkalemia risk
- Clarification of target RTA subtype (Type 1 hypokalemic distal RTA vs. Type 4 hyperkalemic RTA) before any further evaluation
- Serum potassium monitoring plan if this candidate advances past Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

