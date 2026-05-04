---
layout: default
title: Amylmetacresol
parent: 僅模型預測 (L5)
nav_order: 52
evidence_level: L5
indication_count: 10
---

# Amylmetacresol
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

# Amylmetacresol: From Throat Antiseptic to Cauda Equina Syndrome

## One-Sentence Summary

Amylmetacresol (AMC) is a phenolic antiseptic agent best known as an active ingredient in over-the-counter throat lozenges, used for sore throat relief and oral antimicrobial action.
The TxGNN model predicts it may have relevance to **Cauda Equina Syndrome**, achieving a prediction score of **99.99%**; however, this is supported by **0 clinical trials** and **0 publications**, making this a model-only prediction with no empirical corroboration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not formally registered in Taiwan; known internationally as an OTC throat antiseptic |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, Amylmetacresol is a phenol-derived compound that exerts antimicrobial activity primarily by disrupting bacterial cell membrane phospholipids, making it effective against gram-positive bacteria and certain viruses in the oropharyngeal environment. It is also reported to possess mild local anesthetic properties, attributed to partial sodium channel blockade, which in principle could modulate pain signal transmission in peripheral nerves.

Cauda Equina Syndrome (CES) is a serious neurological emergency caused by mechanical compression of the cauda equina nerve roots at the base of the spinal cord. Its hallmark features — saddle anaesthesia, lower limb weakness, and bladder/bowel dysfunction — arise from physical impingement rather than from infection or a druggable biochemical pathway. While AMC's sodium channel activity has a tenuous theoretical connection to neurogenic pain, there is no established mechanism by which a topical mucosal antiseptic could address structural nerve root compression.

The very high TxGNN score most likely reflects **knowledge graph node clustering effects** — AMC and CES occupy adjacent regions of the neurological disease subgraph — rather than an independent pharmacological signal. The prediction should be treated as a computational artifact requiring substantial experimental validation before any scientific hypothesis can be formed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Amylmetacresol is currently **not marketed in Taiwan**. No drug licenses are on record with the Taiwan FDA (TFDA). The drug has no approved indications, no registered dosage forms, and no DIN equivalents in the Taiwan regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** TFDA package insert warnings, contraindications, and drug interaction data were not retrieved as part of this evidence pack. Completing the safety profile is a **Blocking** requirement before this candidate can advance to any formal evaluation stage.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a pure model-derived prediction (Evidence Level L5) with zero supporting clinical trials, zero literature, and a mechanistically implausible link — Cauda Equina Syndrome is a mechanical compressive emergency, and Amylmetacresol has no known pharmacological pathway relevant to nerve root decompression or neuroprotection. The high TxGNN score is most likely an artifact of knowledge graph topology rather than a genuine drug-disease signal.

**To proceed, the following is needed:**

- **Safety data (Blocking):** Retrieve TFDA package insert to complete warnings, contraindications, and drug interaction profile before any further evaluation
- **MOA confirmation (High priority):** Query DrugBank API for complete mechanism of action, pharmacokinetic parameters (systemic bioavailability, CNS penetration), and toxicity profile
- **KG topology audit:** Verify whether AMC's high scores across neurological and ophthalmic disease clusters (ranks 617–9,903) represent genuine drug-disease relationships or node proximity artifacts within the knowledge graph
- **Biological plausibility review:** Obtain independent pharmacology expert opinion before allocating further research resources to any of the 10 predicted indications
- **Broader indication screening:** Consider whether AMC's established antimicrobial activity supports repurposing into infectious disease indications (e.g., oral/mucosal infections) rather than the neurological and ophthalmic cluster currently predicted

---

*This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

