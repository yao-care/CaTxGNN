---
layout: default
title: Gefitinib
parent: Model Prediction Only (L5)
nav_order: 427
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Gefitinib: predicted new indication Fibromatosis, gingival (evidence level L5). Approved use: Non-small cell lung cancer (lung cancer). The Canadian licence record…"
---

# Gefitinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Gefitinib: From Non-Small Cell Lung Cancer to Fibromatosis, Gingival

## One-Sentence Summary

Gefitinib is an EGFR tyrosine kinase inhibitor originally used to treat non-small cell lung cancer.
The TxGNN model predicts it may be effective for **Gingival Fibromatosis**, but **no clinical trials and no publications** currently support this direction, so it is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung cancer (lung cancer). The Canadian licence records compiled for this report contain no indication text, so this comes from the knowledge graph. |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, gefitinib is a selective inhibitor of the epidermal growth factor receptor (EGFR) tyrosine kinase. Its efficacy in EGFR-mutant non-small cell lung cancer is established, and mechanistically it may be applicable to conditions driven by EGFR signalling.

A plausible but unproven link is EGFR-driven fibroblast proliferation in gingival fibromatosis. Nothing in the compiled data supports this. The high score (rank 2721 in the model's ordering) reflects a graph-based prediction only, and the relationship to the original indication has not been assessed.

The other top-ranked predictions are similarly weak. Several (fibroma of lung, hamartoma of lung, lung benign neoplasm) are benign lung conditions, and the supporting literature for lung-related entries is almost entirely about gefitinib in lung cancer rather than in those diseases. Others (e.g., the VCP-related myopathy and junctional epidermolysis bullosa) have no evident mechanistic connection, and for epidermolysis bullosa, gefitinib's known skin toxicity is a concern rather than a therapeutic signal.

## Clinical Trial Evidence

Currently no related clinical trials registered for this predicted indication.

## Literature Evidence

Currently no related literature available for this predicted indication.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02248676 | IRESSA | Not specified | Not specified |
| 02468050 | APO-GEFITINIB | Not specified | Not specified |
| 02487748 | SANDOZ GEFITINIB | Not specified | Not specified |
| 02491796 | NAT-GEFITINIB | Not specified | Not specified |
| 02500663 | JAMP GEFITINIB | Not specified | Not specified |

All five authorisations are valid single-ingredient products.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (EGFR tyrosine kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function (the knowledge graph lists liver disease as a contraindication-related condition), respiratory status for signs of interstitial lung disease; please also refer to the package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

**Contraindication-related conditions (from the knowledge graph, not label text):** liver disease, gallbladder disease, interstitial lung disease, pulmonary fibrosis, postinflammatory pulmonary fibrosis. These should be verified against the Canadian package insert.

**Drug Interactions:** 100 interactions were identified. The ones listed in the compiled data are mostly Moderate severity:
- Acid-suppressing drugs (likely through raised gastric pH): famotidine, ranitidine, cimetidine, nizatidine, and the proton pump inhibitors omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole, rabeprazole
- Enzyme-pathway drugs: clarithromycin, aprepitant, dexamethasone, miconazole, clotrimazole, troglitazone, naltrexone
- Unknown severity: calcitriol, glimepiride

**Other signals from the literature retrieved for related predictions (not specific to gingival fibromatosis):** gefitinib-associated pneumonitis/interstitial lung disease (including a fatal case), skin toxicity, and a preclinical report of QT prolongation.

Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a graph-model score, with no clinical trials, no literature, and no assessed link to the original indication. The prediction is at evidence level L5. Safety screening cannot proceed because the Canadian package insert warnings and contraindications are missing.

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications, approved indication text, dosage forms)
- Detailed mechanism of action data (e.g., from DrugBank)
- A targeted literature search on EGFR signalling in gingival fibroblasts/fibromatosis, and a trial registry search
- An assessment of similarity to the original indication and of route compatibility
- Consideration of higher-ranked alternatives with some supporting evidence only if they represent genuine repurposing. The lung-related entries largely restate the original lung cancer indication and are not true repurposing.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

