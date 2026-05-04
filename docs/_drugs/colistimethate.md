---
layout: default
title: Colistimethate
parent: 僅模型預測 (L5)
nav_order: 180
evidence_level: L5
indication_count: 10
---

# Colistimethate
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

# Colistimethate: From Gram-Negative Bacterial Infections to Osteoarthritis

## One-Sentence Summary

Colistimethate (colistimethate sodium) is a last-resort polymyxin antibiotic of the polymyxin E class, used parenterally and by inhalation to treat severe infections caused by multidrug-resistant gram-negative bacteria such as *Pseudomonas aeruginosa*, *Acinetobacter baumannii*, and *Klebsiella pneumoniae*.
The TxGNN model predicts it may be effective for **Osteoarthritis**, ranking it 32,378th out of all drug-disease pairs with a score of 97.78%.
However, there are currently **0 clinical trials** and **0 publications** supporting this direction, and the mechanistic link is considered extremely weak.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multidrug-resistant gram-negative bacterial infections (e.g., *P. aeruginosa*, *A. baumannii*) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 97.78% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacology, Colistimethate is a prodrug of colistin, a polycationic polymyxin antibiotic whose primary mechanism involves electrostatic binding to lipopolysaccharide (LPS) on the outer membrane of gram-negative bacteria, disrupting membrane integrity and causing cell death. It is not known to directly modulate mammalian inflammatory signalling pathways, cartilage metabolism, or chondrocyte biology.

Osteoarthritis is characterised by progressive degradation of articular cartilage mediated by matrix metalloproteinases (MMPs), ADAMTS proteases, and low-grade chronic synovial inflammation. There is no established direct pharmacological bridge between polymyxin antibiotics and these processes. The most plausible theoretical pathway would be the **gut-joint axis**: gut microbiota dysbiosis has been implicated in OA pathogenesis, and antibiotics that alter microbial composition could theoretically modulate systemic inflammation. However, colistimethate is poorly absorbed after oral administration and is not used to selectively target gut-resident species; its clinical use is entirely parenteral or inhaled for systemic/pulmonary MDR infections.

The Evidence Pack's own mechanistic analysis notes that this prediction most likely arises from an **indirect knowledge graph (KG) linkage** through "bacterial infection → arthritis" intermediate nodes, rather than from any genuine biological mechanism. With a TxGNN rank of 32,378 and zero corroborating evidence, this prediction should be interpreted as a graph connectivity artefact rather than a biologically actionable hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Colistimethate is currently **not marketed in Canada** (0 DINs on file). No product authorisations are available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Colistimethate is well-known in the clinical literature for **dose-dependent nephrotoxicity** and **neurotoxicity** (including peripheral neuropathy and neuromuscular blockade). These risks are particularly relevant when evaluating any chronic-use repurposing scenario such as osteoarthritis, which would require long-term administration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Colistimethate are rated L5 (model prediction only) with zero supporting clinical trials or publications, and the mechanistic analysis consistently identifies these predictions as knowledge graph diffusion artefacts rather than biologically plausible targets. The drug is not marketed in Canada, is a last-resort antibiotic with significant toxicity concerns, and has no known pharmacological activity relevant to osteoarthritis, rheumatoid arthritis, or any of the other predicted musculoskeletal, hepatic, or metabolic conditions.

**To proceed, the following would be needed:**

- **Basic mechanistic data**: Retrieval of full DrugBank MOA entry and pharmacodynamic profile to confirm whether any anti-inflammatory or cartilage-protective off-target effects have been reported.
- **Preclinical evidence**: Identification of any in vitro or animal model data (e.g., LPS-induced synovitis, gut microbiome-OA models) before this candidate could be elevated above L5.
- **Safety feasibility assessment**: Formal analysis of whether colistimethate's known nephrotoxicity and neurotoxicity profile is compatible with the chronic dosing regimens required for osteoarthritis treatment.
- **Canada regulatory status**: If any clinical development were considered, a regulatory pathway assessment (New Drug Submission or Clinical Trial Application) would be required given the absence of Canadian market authorisation.
- **Alternative candidates**: Given the profile of all 10 predicted indications, it is recommended to deprioritise Colistimethate as a repurposing candidate and redirect research resources to drugs with stronger mechanistic plausibility and existing clinical evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

