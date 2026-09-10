---
layout: default
title: Insulin Degludec
parent: 僅模型預測 (L5)
nav_order: 406
evidence_level: L5
indication_count: 6
---

# Insulin Degludec
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Insulin Degludec: From Diabetes Mellitus to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin degludec is an ultra-long-acting basal insulin analogue already used broadly in diabetes management. The TxGNN model assigns a high prediction score for **Type 1 Diabetes Mellitus**, but this is best understood as a **confirmatory signal rather than a novel repurposing candidate** — insulin degludec is already a standard basal insulin therapy for T1DM, and the supporting evidence (largely Phase 3 RCTs and large real-world studies) reflects existing clinical use rather than a new mechanism-of-action hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes Mellitus (basal insulin therapy) — detailed approved indication text not available in this evidence pack |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L1 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is currently a data gap. However, the evidence pack's own mechanistic rationale explains the link clearly: insulin degludec is an ultra-long-acting basal insulin analogue that binds the insulin receptor, promoting glucose utilization and suppressing hepatic gluconeogenesis. This mode of action maps directly onto the pathophysiology of Type 1 Diabetes Mellitus, where autoimmune destruction of pancreatic β-cells causes absolute endogenous insulin deficiency.

Importantly, this is **not a strict case of drug repurposing** — insulin degludec is already an established treatment option for T1DM. The clinical trial evidence therefore functions as confirmatory/extension evidence for an existing indication rather than validation of a genuinely new therapeutic hypothesis. The TxGNN high score reflects this tight, well-established drug–disease relationship in the underlying knowledge graph.

Because this candidate does not represent a novel indication, the primary value of this evaluation lies in verifying local (Taiwan) regulatory status and safety documentation rather than establishing efficacy, which is already well supported globally.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05463744](https://clinicaltrials.gov/study/NCT05463744) | Phase 3 | Completed | 692 | Weekly insulin efsitora alfa vs. insulin degludec in T1DM patients on multiple daily injections — head-to-head efficacy/safety comparator trial |
| [NCT01835431](https://clinicaltrials.gov/study/NCT01835431) | Phase 3 | Completed | 362 | Insulin degludec/aspart once daily vs. insulin detemir in children/adolescents with T1DM |
| [NCT03952130](https://clinicaltrials.gov/study/NCT03952130) | Phase 3 | Completed | 354 | LY900014 vs. insulin lispro, both combined with glargine or degludec, in adults with T1DM |
| [NCT04450407](https://clinicaltrials.gov/study/NCT04450407) | Phase 2 | Completed | 266 | Comparator-controlled RCT of LY3209590 vs. degludec-based regimens in T1DM; direct safety/efficacy evaluation |
| [NCT05434559](https://clinicaltrials.gov/study/NCT05434559) | N/A (retrospective) | Completed | 475 | Large retrospective study of glycemic control before/after switching to insulin degludec in T1DM patients |
| [NCT02117622](https://clinicaltrials.gov/study/NCT02117622) | N/A (PMS) | Completed | 1056 | Post-marketing surveillance of Tresiba® (insulin degludec) long-term safety/efficacy in India, real-world diabetes population |
| [NCT03416855](https://clinicaltrials.gov/study/NCT03416855) | N/A (PMS) | Completed | 768 | Post-marketing surveillance of Ryzodeg® (degludec/aspart) safety and effectiveness in Korea |
| [NCT04692415](https://clinicaltrials.gov/study/NCT04692415) | Phase 4 | Completed | 25 | Degludec vs. glargine U300: glycaemic variability, oxidative stress, and arterial stiffness outcomes |
| [NCT01076634](https://clinicaltrials.gov/study/NCT01076634) | Phase 1 | Completed | 33 | Pharmacodynamic characterization of insulin degludec formulations in T1DM subjects |
| [NCT00964964](https://clinicaltrials.gov/study/NCT00964964) | Phase 1 | Completed | 18 | Hypoglycaemic episode frequency and glycaemic variability comparison in T1DM subjects |

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Insulin degludec is not currently marketed in this jurisdiction — no DIN (Drug Identification Number) records are available in the evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: DG001 — TFDA label warnings/contraindications data is flagged as a Blocking data gap, meaning safety screening (S1) cannot currently be completed with this evidence pack.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base easily meets L1 criteria, with multiple completed Phase 3 RCTs plus large real-world/PMS studies (n=768–1056) supporting insulin degludec's use in T1DM. However, because the drug is not currently marketed locally (0 DINs) and TFDA-specific safety/label data is a Blocking gap, this cannot yet be advanced without further local regulatory input — and note that this is a confirmatory-use case rather than a novel repurposing opportunity.

**To proceed, the following is needed:**
- TFDA package insert warnings and contraindications (DG001, Blocking)
- DrugBank-sourced mechanism-of-action confirmation (DG002, High)
- Local Taiwan market authorization / DIN status verification, since current data shows the drug as not marketed
- Clarification on whether this candidate should be scoped as "existing indication confirmation" rather than a repurposing opportunity, given overlap with the drug's established use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

