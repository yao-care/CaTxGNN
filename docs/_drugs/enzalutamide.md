---
layout: default
title: Enzalutamide
parent: 僅模型預測 (L5)
nav_order: 284
evidence_level: L5
indication_count: 10
---

# Enzalutamide
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

# Enzalutamide: From Prostate Cancer to Prostate Cancer/Brain Cancer Susceptibility

## One-Sentence Summary

Enzalutamide (Xtandi®) is a second-generation non-steroidal androgen receptor (AR) inhibitor, established in multiple jurisdictions for the treatment of advanced prostate cancer across castration-resistant and hormone-sensitive settings.
The TxGNN model predicts it may be relevant for **prostate cancer/brain cancer susceptibility** with a prediction score of **99.71%**; however, **no clinical trials or published literature** currently support this specific combined-susceptibility indication.
Among all 10 predicted indications, the strongest supporting evidence base lies in adjacent prostate neoplasm categories (ranks 8–9), which collectively yield over 50 clinical trials and 20 publications.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prostate cancer (castration-resistant and hormone-sensitive; established international approvals) |
| Predicted New Indication | Prostate cancer/brain cancer susceptibility |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed (no DINs found in current database) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established scientific literature, enzalutamide is a potent competitive AR inhibitor that binds the androgen receptor with approximately 5–8× greater affinity than first-generation antiandrogens such as bicalutamide. It prevents androgen binding, blocks nuclear translocation of the ligand–receptor complex, and inhibits AR–DNA interaction and co-activator recruitment — collectively suppressing AR-driven transcription. This multi-step blockade is what distinguishes it from older agents and drives its efficacy in both hormone-sensitive and castration-resistant prostate cancer.

The predicted indication "prostate cancer/brain cancer susceptibility" represents a disease entity in the TxGNN knowledge graph corresponding to hereditary or genetic predisposition to both prostate and brain malignancies. The AR pathway is not limited to the prostate: androgen receptor expression has been documented in glioma and other CNS tumors, and overlapping hereditary syndromes (notably BRCA1/2 mutations and mismatch repair deficiency) confer simultaneous elevated risk for prostate and brain cancers. TxGNN may be recognizing that enzalutamide's AR-targeting mechanism has latent relevance to shared upstream biology in this susceptibility phenotype.

The practical implication of this prediction is speculative and distinct from enzalutamide's established therapeutic role. A "susceptibility" context implies either chemoprevention — suppressing AR signaling in individuals at elevated genetic risk before malignancy develops — or perhaps adjuvant use targeting residual AR-expressing microenvironments. Neither application has been evaluated in clinical trials to date. The high TxGNN score (99.71%) more likely reflects the model's strong association between enzalutamide and prostate-biology nodes in the knowledge graph than a validated novel use case.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the specific indication of prostate cancer/brain cancer susceptibility.

---

## Literature Evidence

Currently no related literature available for the specific indication of prostate cancer/brain cancer susceptibility.

---

## Canada Market Information

No Health Canada product authorizations (DINs) were found in the current database for enzalutamide.

> **Note:** This likely represents a data gap in the pipeline rather than a true absence of authorization. Enzalutamide (Xtandi®) is known to be approved by the FDA, EMA, and PMDA for multiple prostate cancer indications. Health Canada authorization status should be verified directly at the Health Canada Drug Product Database before drawing regulatory conclusions.

---

## Cytotoxicity

Enzalutamide is classified as an antineoplastic agent (androgen receptor inhibitor used in cancer treatment); this section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Androgen receptor inhibitor (non-cytotoxic; hormonal/endocrine mechanism) |
| Myelosuppression Risk | Low — enzalutamide does not directly suppress bone marrow; neutropenia is uncommon and not dose-limiting |
| Emetogenicity Classification | Low — nausea occurs in ~10–20% of patients but is generally mild |
| Monitoring Items | Liver function tests (ALT/AST), seizure history and neurological status, blood pressure, complete metabolic panel; ECG in patients with cardiac risk factors |
| Handling Protection | Standard oral medication handling; cytotoxic drug handling regulations are not required for this agent |

---

## Safety Considerations

Please refer to the Health Canada-approved package insert for safety information. No warning or contraindication data was available in this Evidence Pack.

> Known class-level concerns from published literature include seizure risk (particularly in patients with predisposing conditions), fatigue and asthenia, hypertension, hot flushes, and falls/fractures in elderly patients. These should be reviewed in the official product monograph.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score of 99.71% reflects the model's strong mechanistic linkage between enzalutamide and prostate-biology nodes in its knowledge graph, but the specific "prostate cancer/brain cancer susceptibility" indication is supported by zero clinical trials and zero published literature, placing it at the lowest evidence tier (L5). Without a clearer disease definition and supporting preliminary data, proceeding with any repurposing programme for this indication is premature.

**To proceed, the following is needed:**
- Confirm Health Canada authorization status for enzalutamide (Xtandi®) directly from the Health Canada Drug Product Database
- Retrieve TFDA/Health Canada product monograph to address the blocking safety data gap (DG001)
- Clarify how "prostate cancer/brain cancer susceptibility" is operationalized in the TxGNN disease ontology — determine whether this is a phenotype, a hereditary syndrome, or a composite node
- Query DrugBank API for full mechanism of action documentation (DG002)
- Commission a targeted literature search on: (1) AR inhibition in hereditary prostate/brain cancer syndromes, (2) enzalutamide in non-malignant or pre-malignant prostate contexts (BPH, benign neoplasm), which showed richer evidence at ranks 8–9
- Consider whether adjacent high-evidence predictions (e.g., rank 8 benign neoplasm of prostate, supported by 2 trials and 20 publications) represent more actionable near-term repurposing candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

