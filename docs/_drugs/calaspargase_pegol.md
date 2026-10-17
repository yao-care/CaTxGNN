---
layout: default
title: Calaspargase Pegol
parent: Model Prediction Only (L5)
nav_order: 146
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Calaspargase Pegol: predicted new indication Insomnia (evidence level L5). Approved use: Not stated in the Canadian license data compiled for this report (the…"
monitor_inn: "Calaspargase pegol"
predicted_indications: ["insomnia (disease)", "factor 5 excess with spontaneous thrombosis", "heparin cofactor 2 deficiency", "antithrombin deficiency type 2", "thrombophilia", "endocardial fibroelastosis", "sleep disorder, initiating and maintaining sleep", "endocarditis", "benign recurrent intrahepatic cholestasis", "thrombotic disease"]
---

# Calaspargase Pegol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Calaspargase Pegol: From Acute Lymphoblastic Leukemia Treatment to Insomnia (Model Prediction Only)

## One-Sentence Summary

Calaspargase pegol is a long-acting PEGylated asparaginase that depletes circulating asparagine, a mechanism used in acute lymphoblastic leukemia (ALL).
The TxGNN model predicts it may be effective for **insomnia**, but there are **0 clinical trials** and **0 publications** supporting this prediction.
The high score is a graph-based output without a plausible mechanistic link, so this candidate is not recommended for advancement.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license data compiled for this report (the drug's established use is in ALL) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, calaspargase pegol is a PEGylated asparaginase. It breaks down circulating asparagine, which leukemic cells depend on, and this is the basis of its use in acute lymphoblastic leukemia.

The prediction for insomnia does not have a plausible mechanistic link. Insomnia is better understood as a non-specific central nervous system side-effect context for chemotherapy regimens than as a therapeutic target. The high TxGNN score (0.998) comes from relationships in the knowledge graph and is not backed by any trial or publication.

The other predicted indications show the same pattern. Several are coagulation-related (factor 5 excess with spontaneous thrombosis, heparin cofactor 2 deficiency, antithrombin deficiency type 2, thrombophilia, thrombotic disease). Asparaginase therapy is known to lower the liver's production of antithrombin, fibrinogen and other coagulation proteins, and it raises thrombosis risk. These associations most likely reflect adverse effects, not treatment benefits. The remaining predictions (sleep disorder, endocardial fibroelastosis, endocarditis, benign recurrent intrahepatic cholestasis) also have no identifiable mechanistic rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top predicted indication (insomnia).

For reference, the only publication found across the ten predictions relates to the rank 10 prediction, thrombotic disease:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34228505](https://pubmed.ncbi.nlm.nih.gov/34228505/) | 2021 | Review | J Clin Oncol | DFCI 11-001 compared the efficacy and toxicity of calaspargase pegol with standard pegaspargase in childhood ALL. Thrombosis is a documented toxicity of these agents, so this is indirect evidence of an adverse-effect association, not support for a therapeutic use. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02542943 | ASPARLAS | Not specified | Not specified |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Enzyme-based antineoplastic (asparagine-depleting agent), not a conventional DNA-damaging cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions. Coagulation parameters (antithrombin, fibrinogen) and liver function are relevant given the known effects of asparaginase products |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

**Drug Interactions**: 100 interactions were identified in the DDI screen. The 20 entries reviewed are all Moderate level, from the DDInter source. They include:
- Corticosteroids: hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone
- Antidiabetic agents: acarbose, albiglutide, alogliptin, metformin, pioglitazone, acetohexamide, canagliflozin, chlorpropamide, dapagliflozin
- Antibiotics and antifungals: doxycycline, clarithromycin, clotrimazole
- Others: bupropion, acetylsalicylic acid, chenodeoxycholic acid

**Safety signals from the prediction analysis**: Asparaginase products are associated with thrombosis, reduced coagulation-inhibitor synthesis, hepatotoxicity and cholestasis. Several predicted indications (thrombotic and coagulation disorders, cholestasis) overlap with these known toxicities, which makes a therapeutic use of the drug in them a safety concern.

Please refer to the package insert for warnings and contraindications, which were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based model score. There are no clinical trials, no supporting literature, and no plausible mechanism for insomnia. Most other top predictions overlap with known adverse effects of asparaginase therapy, so they point to safety concerns, not opportunities.

**To proceed, the following is needed:**
- A plausible biological rationale linking asparagine depletion to insomnia or sleep regulation
- Mechanism of action data for the drug
- Health Canada package insert warnings and contraindications, and the approved indication text for the license
- Any preclinical or clinical signal for the predicted indication. Without it, this candidate should be deprioritized.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

