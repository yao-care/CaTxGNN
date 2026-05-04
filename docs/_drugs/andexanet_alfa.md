---
layout: default
title: Andexanet Alfa
parent: 僅模型預測 (L5)
nav_order: 56
evidence_level: L5
indication_count: 4
---

# Andexanet Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Andexanet Alfa: From Factor Xa Inhibitor Reversal to Glanzmann Thrombasthenia

## One-Sentence Summary

Andexanet Alfa is a recombinant modified human Factor Xa decoy protein, approved internationally (as Andexxa/Ondexxya) as a specific antidote for life-threatening bleeding in patients taking Factor Xa inhibitors such as apixaban and rivaroxaban.
The TxGNN model predicts it may be effective for **Glanzmann Thrombasthenia**, a rare inherited platelet disorder — however, with **0 clinical trials** and **0 publications** supporting this direction, and the mechanistic rationale assessed as biologically implausible, this prediction is most likely a knowledge graph artifact.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Reversal of Factor Xa inhibitor anticoagulation in life-threatening or uncontrolled bleeding (approved in US/EU; not registered in Taiwan) |
| Predicted New Indication | Glanzmann Thrombasthenia |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on published information, Andexanet Alfa is a catalytically inactive recombinant human Factor Xa variant. It acts as a high-affinity "decoy receptor" that binds and sequesters direct Factor Xa inhibitors — including apixaban and rivaroxaban — in the bloodstream, preventing them from blocking endogenous Factor Xa activity and thereby restoring thrombin generation along the coagulation cascade. This is a secondary hemostasis mechanism operating at the coagulation factor level.

Glanzmann Thrombasthenia, by contrast, is a disorder of **primary hemostasis**. It is caused by loss-of-function mutations in the *ITGA2B* or *ITGB3* genes, resulting in deficiency or dysfunction of the GPIIb/IIIa (αIIbβ3) integrin receptor on the platelet surface. Without functional GPIIb/IIIa, platelets cannot bind fibrinogen and aggregate, causing a lifelong bleeding tendency that is entirely independent of the coagulation cascade.

These two conditions operate at fundamentally different levels of the hemostatic system: Andexanet Alfa targets the coagulation waterfall (Factor Xa → thrombin), while Glanzmann Thrombasthenia is a platelet surface receptor defect. There is no recognized biological pathway by which a Factor Xa decoy protein could rescue or compensate for GPIIb/IIIa dysfunction. The very high TxGNN score (99.77%) most likely reflects non-specific similarity propagation — often called a "graph diffusion artifact" — among bleeding disorder nodes in the knowledge graph, rather than a genuine mechanistic connection.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Andexanet Alfa in Glanzmann Thrombasthenia.

---

## Literature Evidence

Currently no related literature available for Andexanet Alfa in Glanzmann Thrombasthenia.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite the high TxGNN prediction score (99.77%), the biological mechanism of Andexanet Alfa (Factor Xa decoy receptor) is fundamentally incompatible with the pathophysiology of Glanzmann Thrombasthenia (GPIIb/IIIa platelet receptor defect); there is zero supporting clinical or preclinical evidence, placing this at the lowest evidence tier (L5), and the prediction is most likely a knowledge graph artifact rather than a genuine repurposing signal.

**To proceed, the following would be needed:**
- A credible mechanistic hypothesis explaining how Factor Xa pathway modulation could influence GPIIb/IIIa function or platelet aggregation (none currently exists in the literature)
- Preclinical data (in vitro or animal model) demonstrating any biological effect of Andexanet Alfa in GPIIb/IIIa-deficient models
- Expert hemostologist consultation to formally evaluate whether any indirect pathway could plausibly link this drug's mechanism to this disease
- Retrieval of the full package insert (TFDA or FDA/EMA label) to complete the safety profile before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

