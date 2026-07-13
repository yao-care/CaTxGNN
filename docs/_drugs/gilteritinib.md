---
layout: default
title: Gilteritinib
parent: 僅模型預測 (L5)
nav_order: 362
evidence_level: L5
indication_count: 1
---

# Gilteritinib
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

# Gilteritinib: From Acute Myeloid Leukemia to Bulbar Polio

## One-Sentence Summary

Gilteritinib (Xospata) is a selective FLT3/AXL kinase inhibitor approved internationally for relapsed or refractory acute myeloid leukemia (AML) harbouring FLT3 mutations.
The TxGNN model predicts it may be effective for **Bulbar Polio**, a severe form of poliomyelitis affecting the brainstem.
However, **no clinical trials and no publications** currently support this direction — the evidence is limited to model prediction alone.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Relapsed/refractory AML with FLT3 mutation (international approval; not marketed in Canada) |
| Predicted New Indication | Bulbar Polio |
| TxGNN Prediction Score | 99.10% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Gilteritinib is a potent, selective inhibitor of two receptor tyrosine kinases: FLT3 (FMS-like Tyrosine Kinase 3) and AXL. Its primary clinical application is in AML, where activating FLT3 mutations (FLT3-ITD and FLT3-TKD) drive uncontrolled proliferation of myeloid blasts. By blocking FLT3 signalling, gilteritinib restores normal apoptotic pathways in these malignant cells.

The theoretical bridge to bulbar polio rests on AXL's secondary role. AXL belongs to the TAM receptor family (Tyro3/AXL/MerTK) and has been shown to facilitate cellular entry for several enveloped viruses — including Ebola, SARS-CoV-2, Zika, and Dengue — via a phosphatidylserine-bridging mechanism. AXL also suppresses type I interferon responses, meaning its inhibition could theoretically enhance antiviral innate immunity. On this basis, TxGNN's knowledge graph likely traces a path: FLT3/AXL inhibitor → AXL → viral infection node → poliomyelitis.

However, this rationale has a critical flaw: poliovirus does not use AXL as its cellular receptor. Poliovirus enters host cells via **CD155 (PVR, Poliovirus Receptor)**, a completely distinct surface molecule with no known functional interaction with AXL or FLT3. Furthermore, bulbar polio is caused by poliovirus serotype 1, 2, or 3 infecting the motor neurons of the medulla oblongata — a context bearing no established pharmacological overlap with haematopoietic kinase biology. The repurposing_rationale embedded in this Evidence Pack itself concludes the mechanistic link is "extremely weak" and the high TxGNN score is likely a **computational artefact** arising from non-specific AXL → viral infection linkage in the knowledge graph, not a genuine biological signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Gilteritinib has no approved DINs and is not currently marketed in Canada. No regulatory licence table is available.

---

## Cytotoxicity

Gilteritinib is a targeted antineoplastic agent (FLT3/AXL inhibitor) approved internationally for haematological malignancy.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective receptor tyrosine kinase inhibitor (FLT3 / AXL) |
| Myelosuppression Risk | Moderate — anaemia, thrombocytopenia, and neutropenia have been reported in AML trials; differentiation syndrome (a life-threatening complication) is a class-specific concern |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, hepatic function (ALT/AST), renal function, ECG (QTc prolongation), electrolytes (potassium, magnesium); watch for differentiation syndrome symptoms |
| Handling Protection | Oral tablet formulation; standard cytotoxic handling precautions recommended per institutional policy |

---

## Safety Considerations

Please refer to the package insert for safety information. No local regulatory warnings, contraindications, or drug interaction data were available in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score of 99.10% is assessed as a computational artefact rather than a genuine biological signal: poliovirus uses CD155 — not AXL — as its entry receptor, severing any plausible mechanistic link between gilteritinib's known pharmacology and bulbar polio pathophysiology. With zero supporting clinical trials, zero supporting publications, and a mechanistic hypothesis that does not withstand biological scrutiny, there is no basis to proceed.

**To proceed, the following would be needed:**
- Preclinical evidence (in vitro or animal model) demonstrating that FLT3 or AXL inhibition meaningfully alters poliovirus replication, CD155 expression, or neuronal survival in bulbar polio models
- A revised mechanistic hypothesis that connects gilteritinib's actual targets to poliovirus biology — absent such evidence, this candidate should be deprioritised in favour of higher-confidence predictions
- Canada DIN registration and full prescribing information (package insert) if the drug is later considered for any Canadian indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

