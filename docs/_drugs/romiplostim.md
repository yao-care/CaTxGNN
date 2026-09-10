---
layout: default
title: Romiplostim
parent: 僅模型預測 (L5)
nav_order: 693
evidence_level: L5
indication_count: 10
---

# Romiplostim
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

# Romiplostim: From Immune Thrombocytopenia to Primary Release Disorder of Platelets

## One-Sentence Summary

> Romiplostim is a thrombopoietin (TPO) receptor agonist whose established global indication is chronic immune thrombocytopenia (ITP), used to stimulate platelet production.
> The TxGNN model predicts it may also be effective for **Primary Release Disorder of Platelets**,
> but this is currently supported by only **1 observational clinical trial** and **2 indirect mechanistic publications**, with no direct interventional evidence for this specific disease entity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Immune Thrombocytopenia (ITP) — inferred from established global use; no Canadian regulatory license text is available (drug is not currently marketed in Canada) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.9998% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for romiplostim is not available in the source dataset (flagged as a data gap). However, based on the evidence collected, romiplostim is known to act as a **TPO receptor agonist**, stimulating megakaryocyte proliferation and differentiation to increase platelet production. This mechanism underlies its established core global indication of immune thrombocytopenia (ITP), where platelet destruction outpaces production.

The predicted indication, "primary release disorder of platelets," is conceptually and ontologically very close to ITP itself — both involve inadequate platelet availability that a TPO receptor agonist could theoretically compensate for by boosting megakaryocytopoiesis. The predicted score is extremely high, but this largely reflects the mechanistic and terminological overlap with romiplostim's known indication rather than a genuinely novel disease-drug relationship.

Critically, the supporting evidence is indirect: the single clinical trial identified is a large observational registry studying thrombosis risk factors in ITP patients (not a treatment trial), and the literature consists of general reviews and cohort studies on megakaryocytopoiesis and platelet production biology — not interventional studies of romiplostim specifically for this named disease entity. As a result, while the mechanistic rationale is sound, there is currently no direct trial evidence testing romiplostim's efficacy for this indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03820960](https://clinicaltrials.gov/study/NCT03820960) | N/A | Completed | 10,039 | Large observational registry study of thrombosis risk factors in immune thrombocytopenia (ITP) patients; does not directly test romiplostim, only shares an overlapping patient population (Relevance grade: C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23594368](https://pubmed.ncbi.nlm.nih.gov/23594368/) | 2013 | Review | British Journal of Haematology | Reviews megakaryocytopoiesis and thrombopoiesis biology, describing thrombopoietin (TPO) as the primary growth factor for the megakaryocyte lineage — the mechanistic basis for TPO receptor agonists. |
| [25682608](https://pubmed.ncbi.nlm.nih.gov/25682608/) | 2015 | Cohort | Haematologica | Shows that antiplatelet autoantibodies in ITP inhibit proplatelet formation and impair platelet production in vitro, supporting a rationale for TPO-driven compensation but without testing romiplostim directly. |

---

## Canada Market Information

Romiplostim currently has **no authorized products (DINs) in Canada** according to the available regulatory dataset (market status: Not Marketed, 0 total licenses). No approved indication text is available for extraction from Canadian licenses.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data are currently available in the evidence pack for this drug.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The mechanistic rationale linking romiplostim's TPO receptor agonism to "primary release disorder of platelets" is plausible and consistent with its known ITP mechanism, but the current evidence base consists only of an indirect observational trial and general mechanistic literature — there is no interventional study testing romiplostim for this specific disease entity. This does not yet meet the threshold for a "Go" or "Proceed with Guardrails" decision.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action documentation from DrugBank or the manufacturer (currently a data gap, DG002)
- Canadian regulatory safety data — key warnings and contraindications (currently a blocking data gap, DG001) before any S1 safety pre-assessment can proceed
- A direct interventional trial or case series specifically evaluating romiplostim in patients with this named disease entity, rather than the closely related but distinct ITP population
- Clarification of how "primary release disorder of platelets" is diagnostically distinguished from ITP, since current evidence suggests substantial ontological overlap between the two terms

**Note:** Within this same evidence pack, a separate predicted indication — *platelet-type bleeding disorder* (rank 8) — shows substantially stronger evidence (L1, multiple completed Phase 3 RCTs including RECITE and a Phase 4 switch study) and a "Proceed with Guardrails" recommendation. If a broader repurposing decision for romiplostim is needed, that indication should be evaluated separately as it represents materially different evidence strength.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

