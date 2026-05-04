---
layout: default
title: Fedratinib
parent: 僅模型預測 (L5)
nav_order: 287
evidence_level: L5
indication_count: 10
---

# Fedratinib
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

# Fedratinib: From Myelofibrosis to Benign PEComa

## One-Sentence Summary

Fedratinib (Inrebic) is a selective JAK2 kinase inhibitor originally approved for adults with intermediate-2 or high-risk primary or secondary myelofibrosis.
The TxGNN model predicts it may be effective for **Benign PEComa** (perivascular epithelioid cell tumor),
with **no clinical trials and no publications** currently supporting this specific direction — the prediction rests entirely on model inference.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Myelofibrosis (intermediate-2 or high-risk, primary or secondary) |
| Predicted New Indication | Benign PEComa |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Fedratinib is a selective inhibitor of Janus kinase 2 (JAK2), with additional activity against BRD4 (bromodomain-containing protein 4). In myelofibrosis, constitutive JAK2 signalling — most often driven by the JAK2 V617F mutation — leads to unchecked myeloid proliferation. Fedratinib suppresses this pathway and has demonstrated clinical benefit in both JAK-inhibitor–naïve patients and those who have relapsed or are refractory to ruxolitinib.

Benign PEComa (perivascular epithelioid cell tumor), however, is mechanistically distinct. Its principal oncogenic driver is loss-of-function mutation in TSC1/TSC2, which derepresses mTORC1 signalling — a pathway that sits entirely downstream of and parallel to JAK2. The current standard investigational approach for PEComa is mTOR inhibition with everolimus or sirolimus, not JAK2 inhibition. No established functional or genetic link between JAK2 activity and TSC/mTOR-driven tumorigenesis has been reported in PEComa.

The TxGNN graph-neural-network model identifies statistical proximity between nodes in a large heterogeneous knowledge graph; high scores reflect learned co-occurrence or pathway adjacency patterns rather than direct mechanistic evidence. For this particular drug–disease pair, the mechanistic bridge is weak: JAK2 inhibition does not address the fundamental mTOR pathway dysregulation that characterises PEComa. The prediction therefore requires substantial biological validation before it can be considered actionable.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Fedratinib in benign PEComa.

---

## Literature Evidence

Currently no related literature available for Fedratinib in benign PEComa.

---

## Canada Market Information

Fedratinib has not received Health Canada authorization and is not marketed in Canada. No Drug Identification Numbers (DINs) are on record.

---

## Cytotoxicity

Fedratinib is an antineoplastic targeted therapy (JAK2 / BRD4 kinase inhibitor) indicated for a myeloproliferative neoplasm.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective JAK2 kinase inhibitor with secondary BRD4 activity |
| Myelosuppression Risk | Moderate–High (anaemia, thrombocytopenia, and neutropenia are among the most common grade ≥3 adverse events reported in myelofibrosis trials) |
| Emetogenicity Classification | Low to moderate (nausea and vomiting reported; routine antiemetic prophylaxis typically not required but should be considered) |
| Monitoring Items | CBC with differential (baseline and at least every 4 weeks), liver function tests (ALT/AST/bilirubin), renal function, serum thiamine levels (Wernicke's encephalopathy risk — thiamine supplementation recommended) |
| Handling Protection | Oral capsule formulation; follow institutional cytotoxic drug handling procedures for preparation and disposal |

---

## Safety Considerations

Please refer to the package insert for safety information. (No key warnings, contraindications, or drug interaction data were available in the current Evidence Pack.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high confidence score (99.84%) to Fedratinib for benign PEComa, but the mechanistic link is extremely weak — PEComa is driven by TSC/mTOR dysregulation, not JAK2 activity — and there is no supporting clinical trial or published literature evidence whatsoever (Evidence Level L5).

**To proceed, the following is needed:**

- **Preclinical mechanistic data**: Demonstrate JAK2 or BRD4 activity in TSC-mutant PEComa cell lines or patient-derived organoids before any clinical hypothesis can be formed.
- **Drug MOA data from DrugBank**: Retrieve the full Fedratinib mechanism-of-action profile (currently a data gap) to determine whether off-target activities could plausibly affect PEComa biology.
- **Safety and package insert review**: Obtain the full prescribing information (Wernicke's encephalopathy black-box warning is a key concern) before any repurposing protocol is drafted.
- **Comparative KG analysis**: Evaluate why TxGNN ranks PEComa, lymphangiomyoma, and uterine PEComa (all TSC/mTOR-driven) together at the top — this cluster may reflect a graph topology artefact rather than a genuine biological signal.
- **Consider higher-ranked mechanistically plausible alternatives**: Indications #8 and #9 (HLH / hemophagocytic syndromes) have a stronger mechanistic rationale via the IFN-γ / JAK1–JAK2 / STAT1 cytokine storm axis, where ruxolitinib class-effect data already exist. These may be more productive repurposing candidates for further investigation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

