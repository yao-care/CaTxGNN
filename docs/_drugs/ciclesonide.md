---
layout: default
title: Ciclesonide
parent: 僅模型預測 (L5)
nav_order: 158
evidence_level: L5
indication_count: 6
---

# Ciclesonide
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

# Ciclesonide: From Asthma to Atopic Eczema

## One-Sentence Summary

Ciclesonide is an inhaled corticosteroid (ICS) prodrug used internationally for asthma control and allergic rhinitis (marketed as Alvesco® and Omnaris®), though it carries no current regulatory approval in the Canadian database.
The TxGNN model predicts it may be effective for **Atopic Eczema**, with a confidence score of **99.96%**.
However, **no clinical trials and no supporting publications** have been identified for this repurposing direction, and a fundamental route-of-administration barrier makes the prediction pharmacologically implausible with existing formulations.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in Canadian regulatory data (internationally: asthma, allergic rhinitis) |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed (0 registered licenses) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, ciclesonide belongs to the inhaled corticosteroid (ICS) class and functions as a prodrug — it is converted to its active metabolite des-ciclesonide upon contact with airway esterases. This active form binds glucocorticoid receptors in bronchial epithelial cells, suppressing the release of pro-inflammatory cytokines, reducing eosinophil infiltration, decreasing mucus hypersecretion, and attenuating airway hyperresponsiveness. A defining pharmacokinetic feature is extremely low systemic bioavailability (<1%), which sharply limits systemic side effects.

The conceptual link to atopic eczema is mechanistically understandable: topical corticosteroids such as hydrocortisone, betamethasone, and clobetasol — which share the same glucocorticoid receptor pathway — are the cornerstone of atopic eczema management. If ciclesonide were deliverable to the skin, its potent anti-inflammatory profile could theoretically translate into benefit for atopic eczema.

However, there is a critical and currently insurmountable feasibility barrier. Ciclesonide's approved formulations — metered-dose inhalers and intranasal sprays — provide negligible cutaneous drug delivery. With systemic bioavailability below 1%, transdermal exposure from existing routes is essentially zero and cannot reach therapeutic skin concentrations. Addressing this repurposing hypothesis would require the development of an entirely new topical formulation (cream, ointment, or gel), which is a substantial pharmaceutical development programme rather than a straightforward repurposing exercise.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Ciclesonide is not currently registered in the Canadian regulatory database, with no DINs on file.

> **Note for reviewers:** Internationally, ciclesonide is marketed in multiple jurisdictions — including the United States and EU — under Alvesco® (inhaled, for asthma) and Omnaris®/Zetonna® (intranasal, for allergic rhinitis). If Canadian regulatory data retrieval was incomplete, manual verification via Health Canada's Drug Product Database is recommended.

---

## Safety Considerations

Please refer to the package insert for safety information.

> The TFDA package insert warnings, contraindications, and drug-drug interaction data were not available at the time of this report. Manual retrieval from the regulatory authority's official portal is required before any clinical or formulary evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the TxGNN model assigns a high mechanistic similarity score (99.96%), this prediction reflects the shared glucocorticoid biology between ciclesonide and atopic eczema treatments — not an actionable repurposing opportunity. The existing inhaled and intranasal formulations cannot deliver drug to the skin at therapeutic concentrations, and no clinical or preclinical evidence supports pursuing this pathway.

**To proceed, the following is needed:**

- **Formulation feasibility assessment**: Determine whether a topical ciclesonide formulation (cream/ointment) is chemically and commercially viable; benchmark against existing topical ICS agents (fluticasone propionate, mometasone furoate)
- **MOA documentation**: Retrieve full mechanism of action data from DrugBank (DB01410) to complete mechanistic rationale analysis
- **Safety data retrieval**: Obtain and review Health Canada or TFDA package insert warnings and contraindications before any clinical planning
- **Preclinical skin absorption data**: If a topical formulation is pursued, cutaneous permeation and efficacy studies in validated atopic dermatitis models are required before human investigation
- **Regulatory pathway review**: Assess whether a new topical formulation would qualify as a new drug application or a line extension of an existing approval
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

