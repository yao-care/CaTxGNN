---
layout: default
title: Fomepizole
parent: 僅模型預測 (L5)
nav_order: 346
evidence_level: L5
indication_count: 1
---

# Fomepizole
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

# Fomepizole: From Methanol/Ethylene Glycol Poisoning to Sclerosing Cholangitis

## One-Sentence Summary

Fomepizole is an alcohol dehydrogenase (ADH) inhibitor approved as an antidote for methanol and ethylene glycol poisoning.
The TxGNN model predicts it may be effective for **Sclerosing Cholangitis**, with a prediction score of **99.28%**.
However, **no clinical trials and no supporting literature** currently exist for this indication, making this a model-only prediction at the lowest evidence level.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Methanol / Ethylene glycol poisoning (antidote) |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on known pharmacological information, Fomepizole is a competitive inhibitor of alcohol dehydrogenase (ADH), the enzyme responsible for converting methanol and ethylene glycol into their toxic metabolites (formate and oxalate, respectively). By blocking ADH, Fomepizole prevents accumulation of these harmful compounds and is therefore life-saving in acute poisoning scenarios.

The theoretical link to sclerosing cholangitis is indirect and speculative. One possible mechanistic thread is that ADH inhibition could reduce the local generation of toxic aldehyde metabolites in hepatic tissue, potentially lowering oxidative stress within biliary epithelial cells. Sclerosing cholangitis is characterised by progressive biliary inflammation and fibrosis, and oxidative injury is implicated in its pathogenesis — so a drug that dampens oxidative metabolite production could, in principle, be relevant.

However, the TxGNN high-confidence score (rank 12,400 in the model's output) most likely reflects a **network inference** through shared liver metabolism enzyme nodes or inflammation pathway nodes in the knowledge graph, rather than direct biological evidence. There is no published literature, no mechanistic experiment, and no clinical observation linking Fomepizole to sclerosing cholangitis. This prediction should be treated as a hypothesis-generation signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Fomepizole is not currently marketed in Canada. No Drug Identification Numbers (DINs) are on record.

> **Note:** Fomepizole (brand name Antizol) is approved in the United States by the FDA as an antidote for methanol and ethylene glycol poisoning. Canadian practitioners requiring this agent would likely access it through Special Access Programme (SAP) channels.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data were available in the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score, but this is a purely computational inference with zero supporting clinical or preclinical evidence — no trials, no publications, and no mechanistic studies link Fomepizole to sclerosing cholangitis. The drug is also not marketed in Canada, creating an additional regulatory barrier. Proceeding without any biological plausibility data would not be justifiable.

**To proceed, the following is needed:**

- **Mechanism of action verification**: Retrieve full MOA data from DrugBank (DB01213) to confirm whether ADH inhibition has any documented relevance to biliary or hepatic inflammatory pathways
- **Preclinical evidence search**: Conduct a broader literature search (beyond the current drug+disease query) to identify any animal model studies, cell studies, or mechanistic papers connecting ADH inhibition to cholestatic liver disease or biliary fibrosis
- **Safety data retrieval**: Obtain the full prescribing information (FDA label or manufacturer SDS) to document key warnings, contraindications, and interaction profile before any further evaluation
- **Regulatory pathway assessment**: If preclinical evidence emerges, assess Health Canada Special Access Programme eligibility given no active Canadian DINs
- **Expert consultation**: Engage a hepatologist or gastroenterologist to evaluate biological plausibility before allocating resources to formal repurposing study design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

