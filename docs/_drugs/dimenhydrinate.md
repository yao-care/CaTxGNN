---
layout: default
title: Dimenhydrinate
parent: 僅模型預測 (L5)
nav_order: 228
evidence_level: L5
indication_count: 2
---

# Dimenhydrinate
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

# Dimenhydrinate: From Motion Sickness to Allergic Urticaria

## One-Sentence Summary

Dimenhydrinate is a combination compound of diphenhydramine and 8-chlorotheophylline, widely used for the prevention and treatment of motion sickness, nausea, and vomiting.
The TxGNN model predicts it may be effective for **Allergic Urticaria**, with **0 clinical trials** and **1 publication** currently supporting this specific direction.
The supporting evidence is limited to a veterinary pharmacokinetics study, though the mechanistic case is strengthened by the well-established anti-allergic activity of its active moiety, diphenhydramine.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Motion sickness, nausea and vomiting (based on known pharmacology; formal regulatory text not available in dataset) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed (0 DINs registered) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current dataset. However, based on known pharmacology, dimenhydrinate is a salt composed of two active components: **diphenhydramine** (a first-generation H1 receptor antagonist) and **8-chlorotheophylline** (a mild stimulant added to offset sedation). The therapeutic activity relevant to this prediction resides almost entirely in the diphenhydramine moiety.

Diphenhydramine competitively blocks histamine H1 receptors, thereby inhibiting the vasodilation, increased vascular permeability, and pruritus triggered by histamine release — all of which are central to the pathophysiology of allergic urticaria. This mechanistic link is direct and well-established: diphenhydramine as a standalone agent carries Level 1 evidence for allergic urticaria and is incorporated into international guidelines including those of the EAACI and WAO.

The gap between the component (diphenhydramine) and the compound (dimenhydrinate) is the key limitation here. Dimenhydrinate as a fixed combination has never been evaluated as a primary treatment for allergic urticaria in independent clinical trials. The 8-chlorotheophylline component contributes no direct anti-urticaria activity. TxGNN's high prediction score therefore reflects the strong mechanistic signal from diphenhydramine, rather than evidence specific to dimenhydrinate as a formulation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for dimenhydrinate in allergic urticaria.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [30779257](https://pubmed.ncbi.nlm.nih.gov/30779257/) | 2019 | Pharmacokinetics / Clinical Pharmacology Study | Veterinary Dermatology | Compared oral dimenhydrinate vs. oral/IV diphenhydramine in healthy dogs; dimenhydrinate provided superior oral absorption of diphenhydramine and pharmacodynamic suppression of histamine-induced wheal formation was assessed, supporting the notion that dimenhydrinate can deliver therapeutically relevant diphenhydramine exposure |

> **Note:** The sole available publication is a pilot veterinary pharmacokinetics study. No human clinical trials or clinical efficacy studies for dimenhydrinate in allergic urticaria were identified.

---

## Safety Considerations

Detailed warnings, contraindications, and drug interaction data are not available in the current dataset.

> Please refer to the package insert for complete safety information, including anticholinergic effects, CNS depression, sedation risk, and use in specific populations (elderly, paediatric, pregnancy).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic basis for this prediction is scientifically sound — diphenhydramine, the active moiety of dimenhydrinate, has established Level 1 evidence and guideline endorsement for allergic urticaria. However, dimenhydrinate as a combined formulation has no independent clinical evidence in this indication, and the 8-chlorotheophylline component adds complexity without anti-urticaria benefit.

**To proceed, the following is needed:**

- **Mechanism of action documentation**: Obtain full DrugBank MOA record and pharmacology profile for dimenhydrinate to formally confirm H1 receptor binding data
- **Regulatory safety data**: Download and parse the package insert (monograph) to extract warnings, contraindications, and drug interactions — currently a blocking data gap
- **Clinical evidence specific to dimenhydrinate**: Search for any head-to-head or comparative studies of dimenhydrinate vs. diphenhydramine in allergic conditions in humans
- **Comparative positioning analysis**: Evaluate dimenhydrinate against second-generation H1 antihistamines (cetirizine, loratadine, fexofenadine) which are the current first-line agents for allergic urticaria per EAACI guidelines — a key question is whether the sedation/anticholinergic burden of a first-generation agent is acceptable in this indication
- **Formulation justification**: Determine whether the 8-chlorotheophylline component poses any safety or efficacy trade-offs for urticaria patients that would not be present with diphenhydramine alone
- **Market registration pathway**: Given 0 DINs in the current dataset, verify the actual Canadian market status and determine the regulatory pathway required
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

