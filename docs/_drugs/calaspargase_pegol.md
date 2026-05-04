---
layout: default
title: Calaspargase Pegol
parent: 僅模型預測 (L5)
nav_order: 129
evidence_level: L5
indication_count: 10
---

# Calaspargase Pegol
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

# Calaspargase Pegol: From Acute Lymphoblastic Leukemia to Insomnia

## One-Sentence Summary

Calaspargase pegol (Asparlas) is a pegylated recombinant L-asparaginase enzyme used as part of chemotherapy regimens for Acute Lymphoblastic Leukemia (ALL) and lymphoblastic lymphoma in pediatric and young adult patients.
The TxGNN model's top prediction identifies **insomnia** as a potential new indication (score 99.80%), yet there are **0 clinical trials** and **0 publications** supporting this direction.
More critically, systematic review of all 10 predicted indications reveals a pattern of false positives and pharmacologically contradicted predictions — this entire prediction set is recommended as **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute Lymphoblastic Leukemia (ALL) / Lymphoblastic Lymphoma |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, calaspargase pegol is a pegylated recombinant bacterial L-asparaginase. Its antitumor mechanism depends on depleting circulating L-asparagine: leukemic lymphoblasts lack the enzyme asparagine synthetase and cannot synthesize their own asparagine, so they die when the extracellular supply is exhausted. This is a highly tumor-specific mechanism with no established connection to central nervous system function, sleep regulation, or circadian biology.

The prediction of insomnia is assessed in the evidence pack's own mechanistic analysis as a **false positive**. The proposed explanation is that the TxGNN knowledge graph contains confounding edges linking "ALL chemotherapy" to "fatigue and sleep disturbance" (well-known treatment side effects), causing the model to incorrectly infer a therapeutic — rather than adverse — relationship. In short, the model appears to have learned that this drug is associated with sleep-related nodes in the graph, but for the wrong reason.

Across all 10 predicted indications, a serious systemic problem emerges. Four indications — Factor V excess with thrombosis, antithrombin deficiency type 2, heparin cofactor 2 deficiency, and thrombophilia — carry explicit **reverse mechanism warnings**: L-asparaginase is known to *cause* these conditions by suppressing hepatic protein synthesis, which simultaneously depletes coagulation factors (fibrinogen, antithrombin III, Protein C, Protein S, Factor V). Using this drug to treat conditions it pharmacologically induces would be clinically unsafe. The two clinical trials retrieved for the rank-10 prediction (thrombotic disease) are not evidence of therapeutic benefit — both studies investigate coagulation as a *safety monitoring* endpoint in ALL patients, confirming the drug's role as a thrombosis risk factor rather than a treatment.

---

## Clinical Trial Evidence

Currently no clinical trials related to insomnia are registered for calaspargase pegol.

---

## Literature Evidence

Currently no related literature is available for calaspargase pegol in insomnia.

---

## Canada Market Information

Calaspargase pegol is not currently approved or marketed in Canada. No Health Canada DINs are on file. For reference, the drug is FDA-approved in the United States (Asparlas, Jazz Pharmaceuticals) for ALL in patients aged 1 month to 21 years as part of a multi-agent chemotherapy regimen.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Enzyme-based antineoplastic (L-asparaginase class) |
| Myelosuppression Risk | Low as a primary effect; indirect marrow suppression may occur in combination regimens |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Coagulation panel (PT, aPTT, fibrinogen, antithrombin III), liver function tests (ALT, AST, bilirubin), serum amylase/lipase, blood glucose, CBC with differential |
| Handling Protection | Handle as a hazardous pharmaceutical per cytotoxic drug handling regulations; standard PPE required |

---

## Safety Considerations

Please refer to the package insert for safety information.

Based on the mechanistic analysis contained within this evidence pack, the following drug-class safety concerns are documented in clinical literature and warrant attention regardless of indication:

- **Coagulopathy**: Suppression of hepatic protein synthesis depletes antithrombin III, fibrinogen, and Protein C/S simultaneously, creating a paradoxical pro-thrombotic and pro-hemorrhagic state. Thromboembolic events (including cerebral sinus thrombosis) occur in approximately 1–3% of patients during treatment.
- **Hepatotoxicity**: Elevated transaminases, hepatic steatosis, and cholestatic dysfunction are documented adverse effects and are particularly relevant given that several predicted indications (e.g., benign recurrent intrahepatic cholestasis) involve pre-existing liver pathology.
- **Pancreatitis**: A known serious adverse reaction requiring immediate discontinuation if suspected.
- **Hypersensitivity**: Anaphylactic reactions may occur, relevant to the pegylated formulation specifically.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for calaspargase pegol are classified at Evidence Level L5 (model prediction only, zero supporting studies). More importantly, mechanistic review demonstrates that the majority of high-scoring predictions are either false positives arising from graph artifact (sleep-related nodes), or represent conditions that calaspargase pegol is known to *cause* as adverse effects — making repurposing both scientifically unsupported and potentially dangerous. No indication in this prediction set offers a credible therapeutic rationale.

**To proceed, the following is needed:**

- Retrieve complete MOA data from DrugBank (DB14730) to enable proper mechanistic evaluation in future prediction cycles
- Apply graph denoising or adversarial filtering to the TxGNN model to reduce side-effect node confounding, which appears to be driving the majority of these false-positive predictions
- Obtain full Canadian product monograph (or U.S. FDA label) to populate the safety fields currently flagged as data gaps
- Consider whether ALL / lymphoblastic lymphoma itself should be formally registered as the primary indication in future evidence pack versions to ground the repurposing evaluation
- Do not advance any of the current 10 predicted indications to further evaluation without new mechanistic evidence; the reverse-mechanism warnings for thrombosis-related indications in particular should be flagged as contraindicated use cases in the knowledge graph
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

