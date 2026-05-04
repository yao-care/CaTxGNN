---
layout: default
title: Dexrazoxane
parent: 僅模型預測 (L5)
nav_order: 220
evidence_level: L5
indication_count: 10
---

# Dexrazoxane
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

# Dexrazoxane: From Anthracycline Cardiotoxicity Protection to Sclerosing Cholangitis

## One-Sentence Summary

Dexrazoxane is a cardioprotective agent used as an adjunct to reduce anthracycline-induced cardiomyopathy during cancer chemotherapy, with additional clinical use for managing anthracycline extravasation injuries. The TxGNN model ranks **Sclerosing Cholangitis** as its top predicted new indication with a score of **99.99%**; however, there are currently **no supporting clinical trials** and **no relevant publications**, leaving this prediction entirely unvalidated at the evidence level.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cardioprotection during anthracycline-based chemotherapy; treatment of anthracycline extravasation |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on established clinical and pharmacological knowledge, Dexrazoxane (Zinecard®) is a cyclic derivative of EDTA that acts primarily as an **iron chelator**: it reduces intracellular free iron, which otherwise catalyzes reactive oxygen species (ROS) formation via the Fenton reaction — the principal driver of anthracycline-induced cardiotoxicity. A secondary mechanism involves inhibition of topoisomerase IIβ, contributing to its cardioprotective profile.

Sclerosing cholangitis — particularly primary sclerosing cholangitis (PSC) — is a chronic biliary tract disease characterized by progressive immune-mediated inflammation and fibrosis of the bile ducts. Oxidative stress and iron dysregulation have been proposed as contributing pathological factors in hepatobiliary inflammation. In theory, Dexrazoxane's iron chelation could modulate ROS-driven oxidative injury in the liver or biliary epithelium. This represents the theoretical basis the TxGNN model may have leveraged via iron-related node proximity in the knowledge graph.

However, the mechanistic overlap is weak and indirect. PSC is predominantly driven by autoimmune T-cell activation, gut-liver axis dysregulation, and biliary fibrogenesis — pathways entirely distinct from the anthracycline-ROS axis Dexrazoxane was designed to interrupt. The TxGNN prediction likely reflects graph-level proximity between biliary/hepatic inflammation nodes and Dexrazoxane's iron metabolism connections, rather than a genuine pharmacological relationship. No clinical trials or published literature corroborate this direction, and this prediction should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Dexrazoxane is currently not marketed in Canada. No Drug Identification Numbers (DINs) have been issued by Health Canada.

> **Note:** Dexrazoxane (Zinecard®) is approved in other jurisdictions — including by the U.S. FDA for prevention of anthracycline-induced cardiomyopathy and treatment of anthracycline extravasation — but this approval has not been replicated in Canada based on available regulatory data. This absence limits any near-term clinical repurposing pathway within the Canadian context without first establishing a regulatory foundation.

---

## Cytotoxicity

Dexrazoxane is used exclusively in oncology settings alongside cytotoxic anthracycline chemotherapy, and holds secondary topoisomerase II inhibitory activity that overlaps with cytotoxic mechanisms.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Chemoprotectant / Iron chelator; secondary Topoisomerase IIβ inhibitor (not a primary cytotoxic agent) |
| Myelosuppression Risk | Moderate — myelosuppression is a recognized risk, particularly when administered concurrently with myelotoxic chemotherapy regimens |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver function tests, renal function; cardiac monitoring in the context of concurrent anthracycline use |
| Handling Protection | Used exclusively in oncology settings; follow institutional cytotoxic drug handling and disposal protocols |

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety warnings and contraindications data were not available in this Evidence Pack (classified as a blocking data gap). Retrieval from the Health Canada product monograph or equivalent package insert is required before any safety assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (sclerosing cholangitis, 99.99%) has no supporting clinical trials, no relevant literature, and only a distant theoretical mechanistic link via iron chelation — placing it firmly at Evidence Level L5. Across all 10 predicted indications evaluated in this Evidence Pack, none have progressed beyond L5, with the sole partial exception being cystitis (rank #10, L4), where a ferroptosis–iron chelation hypothesis warrants exploratory investigation but remains mechanistically indirect.

**To proceed, the following is needed:**

- **Retrieve full MOA data from DrugBank** — required for mechanistic link analysis across all predicted indications (currently a High-severity data gap)
- **Obtain Health Canada product monograph / package insert** — required to assess safety warnings and contraindications before any indication-specific safety profiling can begin (currently a Blocking-severity data gap)
- **Targeted mechanistic literature review** — evaluate whether iron chelation has any documented role in biliary fibrosis or PSC pathophysiology before elevating this prediction from L5
- **Re-evaluate the cystitis indication** (rank #10) — the ferroptosis mechanism in cyclophosphamide-induced hemorrhagic cystitis (PMID 37690746) represents the most mechanistically plausible repurposing hypothesis in this pack; a focused preclinical study could elevate evidence from L4
- **Establish a Canadian regulatory pathway** — with 0 DINs and no existing Health Canada approval, any repurposing effort for Canadian use would require a new drug submission or supplemental NDS
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

